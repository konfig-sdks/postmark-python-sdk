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


class TemplateValidationRequest(BaseModel):
    # The html body content to validate. Must be specified if Subject or TextBody are not. See our template language documentation for more information on the syntax for this field. 
    html_body: typing.Optional[str] = Field(None, alias='HtmlBody')

    # When HtmlBody is specified, the test render will have style blocks inlined as style attributes on matching html elements. You may disable the css inlining behavior by passing false for this parameter. 
    inline_css_for_html_test_render: typing.Optional[bool] = Field(None, alias='InlineCssForHtmlTestRender')

    # The subject content to validate. Must be specified if HtmlBody or TextBody are not. See our template language documentation for more information on the syntax for this field. 
    subject: typing.Optional[str] = Field(None, alias='Subject')

    # The model to be used when rendering test content.
    test_render_model: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='TestRenderModel')

    # The text body content to validate. Must be specified if HtmlBody or Subject are not. See our template language documentation for more information on the syntax for this field. 
    text_body: typing.Optional[str] = Field(None, alias='TextBody')
    class Config:
        arbitrary_types_allowed = True