from __future__ import absolute_import, print_function, unicode_literals

from django.test import RequestFactory
from django.contrib.messages.storage.cookie import CookieStorage


def get_flash_messages(response, empty=True):
    if "messages" not in response.cookies:
        return []
    # A RequestFactory will not run the messages middleware, and thus will
    # not delete the messages after retrieval.
    dummy_request = RequestFactory().get("/")
    dummy_request.COOKIES["messages"] = response.cookies["messages"].value
    msgs = list(CookieStorage(dummy_request))
    if empty:
        del response.client.cookies["messages"]
    return msgs
get_flash_messages.__test__ = False
