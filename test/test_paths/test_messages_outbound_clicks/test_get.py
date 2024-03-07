# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import postmark_python_sdk
from postmark_python_sdk.paths.messages_outbound_clicks import get
from postmark_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestMessagesOutboundClicks(ApiTestMixin, unittest.TestCase):
    """
    MessagesOutboundClicks unit test stubs
        Clicks for a all messages
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
