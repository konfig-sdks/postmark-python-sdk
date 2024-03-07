# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from postmark_python_sdk import schemas  # noqa: F401


class TemplateValidationResponse(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            AllContentIsValid = schemas.BoolSchema
        
            @staticmethod
            def HtmlBody() -> typing.Type['TemplateValidationResult']:
                return TemplateValidationResult
        
            @staticmethod
            def Subject() -> typing.Type['TemplateValidationResult']:
                return TemplateValidationResult
            SuggestedTemplateModel = schemas.DictSchema
        
            @staticmethod
            def TextBody() -> typing.Type['TemplateValidationResult']:
                return TemplateValidationResult
            __annotations__ = {
                "AllContentIsValid": AllContentIsValid,
                "HtmlBody": HtmlBody,
                "Subject": Subject,
                "SuggestedTemplateModel": SuggestedTemplateModel,
                "TextBody": TextBody,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AllContentIsValid"]) -> MetaOapg.properties.AllContentIsValid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HtmlBody"]) -> 'TemplateValidationResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Subject"]) -> 'TemplateValidationResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SuggestedTemplateModel"]) -> MetaOapg.properties.SuggestedTemplateModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TextBody"]) -> 'TemplateValidationResult': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AllContentIsValid", "HtmlBody", "Subject", "SuggestedTemplateModel", "TextBody", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AllContentIsValid"]) -> typing.Union[MetaOapg.properties.AllContentIsValid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HtmlBody"]) -> typing.Union['TemplateValidationResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Subject"]) -> typing.Union['TemplateValidationResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SuggestedTemplateModel"]) -> typing.Union[MetaOapg.properties.SuggestedTemplateModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TextBody"]) -> typing.Union['TemplateValidationResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AllContentIsValid", "HtmlBody", "Subject", "SuggestedTemplateModel", "TextBody", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        AllContentIsValid: typing.Union[MetaOapg.properties.AllContentIsValid, bool, schemas.Unset] = schemas.unset,
        HtmlBody: typing.Union['TemplateValidationResult', schemas.Unset] = schemas.unset,
        Subject: typing.Union['TemplateValidationResult', schemas.Unset] = schemas.unset,
        SuggestedTemplateModel: typing.Union[MetaOapg.properties.SuggestedTemplateModel, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        TextBody: typing.Union['TemplateValidationResult', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateValidationResponse':
        return super().__new__(
            cls,
            *args,
            AllContentIsValid=AllContentIsValid,
            HtmlBody=HtmlBody,
            Subject=Subject,
            SuggestedTemplateModel=SuggestedTemplateModel,
            TextBody=TextBody,
            _configuration=_configuration,
            **kwargs,
        )

from postmark_python_sdk.model.template_validation_result import TemplateValidationResult