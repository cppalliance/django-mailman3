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

from __future__ import absolute_import, print_function, unicode_literals


from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from mock import Mock

from django_mailman3.models import Profile
from django_mailman3.tests.utils import FakeMMList, TestCase


class ProfileViewTestCase(TestCase):

    def setUp(self):
        self.mm_user = Mock()
        self.mailman_client.get_user.side_effect = lambda e: self.mm_user
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'testPass',
            first_name="firstname", last_name="lastname",
            )
        self.client.login(username='testuser', password='testPass')

    def test_change_display_name(self):
        # We create a Mailman user, from the django user object.
        self.client.post(
            reverse('mm_user_profile'), {
                'first_name': 'test-first-name',
                'last_name': 'test-last-name',
                'timezone': 'Europe/Paris'})
        # The user's first and last name must be updated.
        user = User.objects.get(username='testuser')
        self.assertEqual(user.first_name, 'test-first-name')
        self.assertEqual(user.last_name, 'test-last-name')
        # The profile must have been created and populated.
        profile = Profile.objects.get(user=user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.timezone, 'Europe/Paris')
        # The Mailman user's display name must have been updated.
        self.assertEqual(
            self.mm_user.display_name, 'test-first-name test-last-name')
