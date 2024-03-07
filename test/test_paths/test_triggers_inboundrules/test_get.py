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
from postmark_python_sdk.paths.triggers_inboundrules import get
from postmark_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTriggersInboundrules(ApiTestMixin, unittest.TestCase):
    """
    TriggersInboundrules unit test stubs
        List inbound rule triggers
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
