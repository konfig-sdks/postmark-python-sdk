# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from postmark_python_sdk.paths.triggers_inboundrules.post import CreateTrigger
from postmark_python_sdk.paths.triggers_inboundrules_triggerid.delete import DeleteSingleTrigger
from postmark_python_sdk.paths.triggers_inboundrules.get import ListTriggers
from postmark_python_sdk.apis.tags.inbound_rules_api_api_raw import InboundRulesAPIApiRaw


class InboundRulesAPIApi(
    CreateTrigger,
    DeleteSingleTrigger,
    ListTriggers,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: InboundRulesAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = InboundRulesAPIApiRaw(api_client)