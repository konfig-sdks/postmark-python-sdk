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
from pydantic import BaseModel, Field, RootModel


class SendEmailResponse(BaseModel):
    error_code: typing.Optional[int] = Field(None, alias='ErrorCode')

    message: typing.Optional[str] = Field(None, alias='Message')

    message_i_d: typing.Optional[str] = Field(None, alias='MessageID')

    submitted_at: typing.Optional[datetime] = Field(None, alias='SubmittedAt')

    to: typing.Optional[str] = Field(None, alias='To')
    class Config:
        arbitrary_types_allowed = True
