#!/bin/bash

set -x

# Copyright (C) 2019-2023 by the Free Software Foundation, Inc.
#
# This package is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 3 of the License.
#
# This package is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>

cd django_mailman3/

cat locale/LINGUAS | while read lingua; do

	django-admin makemessages --ignore 'tests/*' -l "${lingua}"

done
cd - 1>/dev/null
