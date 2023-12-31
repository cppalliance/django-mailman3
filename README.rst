==============================
Django library for Mailman UIs
==============================

This package contains libraries and templates for Django-based interfaces
interacting with Mailman.

To use this application, add ``django_mailman3`` to the ``INSTALLED_APPS`` list
in your Django server's settings file.


NEWS
====

1.3.11 (2023-10-22)
-------------------

* Added a migration to clear the django_sessions table to avoid Mailman Web
  #16.  This will remove user's login data and require them to log in again.
  (See !195)


1.3.10 (2023-10-21)
-------------------

Configuration
-------------

* **BREAKING CHANGE**: ``django_mailman3`` now requires django_allauth>=0.56.
  This requires the addition of ``allauth.account.middleware.AccountMiddleware``
  to ``MIDDLEWARE`` in your Django settings.  If your installation uses settings
  from ``mailman-web`` as `here <https://docs.mailman3.org/en/latest/install/virtualenv.html#initial-configuration>`_,
  upgrading mailman-web to 0.0.7 will do this.

Other Changes
-------------

* Add support for Django 4.2
* Migrate to Bootstrap 5. (See !188)
* A11y: Group related radio buttons and Multi-CheckboxInput. (Fixes #65)
* Add social account buttons to the Sign Up page. (Fixes #67)
* Remove real name requirement from user profile (Fixes #51)



1.3.9 (2022-01-04)
------------------

* Add support for Python 3.11.

1.3.8 (2022-10-22)
------------------
* Add support for Django 4.0 and 4.1 (Fixes #55)
* Add support for Python 3.10 (See !153)
* Fix the Fedora socialaccount provider. (Fixes #50)
* Add pagination only when there are more than one pages. (Fixes #58)
* Use Pytest as the test runner.

1.3.7 (2021-09-02)
------------------

* Set the minimum required version of ``mailmanclient`` in setup.py.
  (Fixes #46)

1.3.6 (2021-08-31)
------------------
* ``django_mailman3.lib.mailman.get_mailman_client()`` now supports
  Mailmanclient request hooks to be added using a new
  ``@mailmanclient_request_hook`` decorator.
* Scrubber now removes null bytes from the scrubbed message body.
* Update the Display Name of a user and it's associated addresses in Mailman
  when the display name is updated in Django.
* Sync a Django user's email address to Core even if it is not verified.
* Add an allauth account adapter to disable signups.
* Add support for Django 3.2.

1.3.5 (2021-01-15)
------------------
* Add a new method get_django_user to return Django User model. (See !99)
* Add ``delete_archives`` field to ``mailinglist_deleted`` Signal.
* Replaced deprecated ``ugettexy_lazy`` with ``gettext_lazy``. (Closes #37)


1.3.4 (2020-06-05)
------------------
* Fix a bug caused by bumping to Mailman API 3.1 in version 1.3.3 which
  resulted in 404 errors for some users. (Closes #35)


1.3.3 (2020-06-01)
------------------

- Hide "Account Connections" tab in accounts if no social account providers are
  installed. (See !54)
- Use bold font for form labels (See !82)
- Update a user's preferred_address in Mailman Core when a user updates their
  primary address in Profile. (Closes #32)
- Use Mailman's API version 3.1 to get Hex UUIDs instead of integer.
- Caught a LookupError when scrubbing an attachment with an unknown charset.
  (Closes #12)
- Properly scrub the content of message/rfc822 parts.  (Closes #34)

License
=======

Django-mailman is licensed under the
`GPL v3.0 <http://www.gnu.org/licenses/gpl-3.0.html>`_

Copyright (C) 2017-2020 by the Free Software Foundation, Inc.
