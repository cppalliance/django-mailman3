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

from unittest import TestCase
from django_mailman3.lib.paginator import paginate


class PaginateTestCase(TestCase):

    def test_page_range(self):
        objects = range(1000)
        self.assertEqual(paginate(objects, 1).page_range,
                         [1, 2, 3, 4, '...', 50])
        self.assertEqual(paginate(objects, 2).page_range,
                         [1, 2, 3, 4, 5, '...', 50])
        self.assertEqual(paginate(objects, 3).page_range,
                         [1, 2, 3, 4, 5, 6, '...', 50])
        self.assertEqual(paginate(objects, 4).page_range,
                         [1, 2, 3, 4, 5, 6, 7, '...', 50])
        self.assertEqual(paginate(objects, 5).page_range,
                         [1, 2, 3, 4, 5, 6, 7, 8, '...', 50])
        self.assertEqual(paginate(objects, 6).page_range,
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, '...', 50])
        self.assertEqual(paginate(objects, 7).page_range,
                         [1, '...', 4, 5, 6, 7, 8, 9, 10, '...', 50])
        self.assertEqual(paginate(objects, 8).page_range,
                         [1, '...', 5, 6, 7, 8, 9, 10, 11, '...', 50])
        self.assertEqual(paginate(objects, 9).page_range,
                         [1, '...', 6, 7, 8, 9, 10, 11, 12, '...', 50])
        self.assertEqual(paginate(objects, 10).page_range,
                         [1, '...', 7, 8, 9, 10, 11, 12, 13, '...', 50])
        self.assertEqual(paginate(objects, 30).page_range,
                         [1, '...', 27, 28, 29, 30, 31, 32, 33, '...', 50])
        self.assertEqual(paginate(objects, 40).page_range,
                         [1, '...', 37, 38, 39, 40, 41, 42, 43, '...', 50])
        self.assertEqual(paginate(objects, 41).page_range,
                         [1, '...', 38, 39, 40, 41, 42, 43, 44, '...', 50])
        self.assertEqual(paginate(objects, 42).page_range,
                         [1, '...', 39, 40, 41, 42, 43, 44, 45, '...', 50])
        self.assertEqual(paginate(objects, 43).page_range,
                         [1, '...', 40, 41, 42, 43, 44, 45, 46, '...', 50])
        self.assertEqual(paginate(objects, 44).page_range,
                         [1, '...', 41, 42, 43, 44, 45, 46, 47, '...', 50])
        self.assertEqual(paginate(objects, 45).page_range,
                         [1, '...', 42, 43, 44, 45, 46, 47, 48, 49, 50])
        self.assertEqual(paginate(objects, 46).page_range,
                         [1, '...', 43, 44, 45, 46, 47, 48, 49, 50])
        self.assertEqual(paginate(objects, 47).page_range,
                         [1, '...', 44, 45, 46, 47, 48, 49, 50])
        self.assertEqual(paginate(objects, 48).page_range,
                         [1, '...', 45, 46, 47, 48, 49, 50])
        self.assertEqual(paginate(objects, 49).page_range,
                         [1, '...', 46, 47, 48, 49, 50])
        self.assertEqual(paginate(objects, 50).page_range,
                         [1, '...', 47, 48, 49, 50])

    def test_default_page(self):
        self.assertEqual(paginate(range(100), None).number, 1)

    def test_last_page(self):
        self.assertEqual(paginate(range(100), 1000).number, 5)
