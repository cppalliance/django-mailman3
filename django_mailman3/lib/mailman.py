# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 by the Free Software Foundation, Inc.
#
# This file is part of Django-Mailman.
#
# Django-Mailman is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# Django-Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Django-Mailman.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Aurelien Bompard <abompard@fedoraproject.org>
#

from __future__ import absolute_import, unicode_literals

from urllib2 import HTTPError

from django.conf import settings
from django.core.cache import cache
from mailmanclient import Client as MailmanClient, MailmanConnectionError

import logging
logger = logging.getLogger(__name__)


def get_mailman_client():
    # easier to patch during unit tests
    client = MailmanClient(
        '%s/3.0' %
        settings.MAILMAN_REST_API_URL,
        settings.MAILMAN_REST_API_USER,
        settings.MAILMAN_REST_API_PASS)
    return client


def get_mailman_user(user):
    # Only cache the mailman user_id, not the whole user instance, because
    # mailmanclient is not pickle-safe
    cache_key = "User:%s:mailman_user_id" % user.id
    mm_user_id = cache.get(cache_key)
    try:
        mm_client = get_mailman_client()
        if mm_user_id is None:
            try:
                mm_user = mm_client.get_user(user.email)
            except HTTPError as e:
                if e.code != 404:
                    raise  # will be caught down there
                mm_user = mm_client.create_user(
                    user.email, user.get_full_name())
                # XXX The email is not set as verified, because we don't
                # know if the registration that was used verified it.
                logger.info("Created Mailman user for %s (%s)",
                            user.username, user.email)
            cache.set(cache_key, mm_user.user_id, None)
            return mm_user
        else:
            return mm_client.get_user(mm_user_id)
    except (HTTPError, MailmanConnectionError) as e:
        logger.warning(
            "Error getting or creating the Mailman user of %s (%s): %s",
            user.username, user.email, e)
        return None


def get_mailman_user_id(user):
    # TODO: Optimization: look in the cache first, if not found call
    # get_mailman_user() as before
    mm_user = get_mailman_user(user)
    if mm_user is None:
        return None
    return unicode(mm_user.user_id)


def add_address_to_mailman_user(user, address):
    """Associate a verified address with a Mailman user."""
    logger.debug("Associating address %s with user %s in Mailman",
                 address, user.username)
    mm_user = get_mailman_user(user)
    if mm_user is None:
        logger.info("Could not find or create a Mailman user for %s",
                    user.username)
        return
    existing_addresses = [unicode(addr) for addr in mm_user.addresses]
    if address not in existing_addresses:
        # Associate it with the user.
        try:
            mm_address = mm_user.add_address(address, absorb_existing=True)
            mm_address.verify()
            logger.debug("Associated address %s with %s",
                         address, user.username)
        except HTTPError as e:
            logger.warning("Can't add %s to %s: %s",
                           address, user.username, e)
    else:
        # Already associated, just mark it verified.
        mm_address = get_mailman_client().get_address(address)
        if mm_address.verified_on is None:
            mm_address.verify()
