# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2023 by the Free Software Foundation, Inc.
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


from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def common(request):
    context = {}
    for name in ('LOGIN_URL', 'LOGOUT_URL', 'INSTALLED_APPS'):
        context[name] = getattr(settings, name, None)
    context["site_name"] = get_current_site(request).name
    return context
