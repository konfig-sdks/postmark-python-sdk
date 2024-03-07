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

from postmark_python_sdk.pydantic.template_validation_result import TemplateValidationResult

class TemplateValidationResponse(BaseModel):
    all_content_is_valid: typing.Optional[bool] = Field(None, alias='AllContentIsValid')

    html_body: typing.Optional[TemplateValidationResult] = Field(None, alias='HtmlBody')

    subject: typing.Optional[TemplateValidationResult] = Field(None, alias='Subject')

    suggested_template_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='SuggestedTemplateModel')

    text_body: typing.Optional[TemplateValidationResult] = Field(None, alias='TextBody')
    class Config:
        arbitrary_types_allowed = True