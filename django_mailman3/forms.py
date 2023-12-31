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


from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django_mailman3.models import TIMEZONES


class UserProfileForm(forms.Form):
    username = forms.CharField(required=True, label=_('Username'))
    first_name = forms.CharField(label=_('First name'), required=False)
    last_name = forms.CharField(label=_('Last name'), required=False)
    timezone = forms.ChoiceField(
        label=_('Time zone'), choices=TIMEZONES)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username != self.initial.get("username"):
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    _("A user with that username already exists."))
        return username
