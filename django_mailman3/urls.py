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


from django.urls import re_path

from django_mailman3.views.profile import delete_account, user_profile


urlpatterns = [
    re_path(r'^user-profile/delete$', delete_account,
            name='mm_user_account_delete'),
    re_path(r'^user-profile/$', user_profile, name='mm_user_profile'),
    ]
