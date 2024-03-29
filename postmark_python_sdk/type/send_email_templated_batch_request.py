# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from postmark_python_sdk.type.email_with_template_request import EmailWithTemplateRequest

class RequiredSendEmailTemplatedBatchRequest(TypedDict):
    pass

class OptionalSendEmailTemplatedBatchRequest(TypedDict, total=False):
    Messages: typing.List[EmailWithTemplateRequest]

class SendEmailTemplatedBatchRequest(RequiredSendEmailTemplatedBatchRequest, OptionalSendEmailTemplatedBatchRequest):
    pass
