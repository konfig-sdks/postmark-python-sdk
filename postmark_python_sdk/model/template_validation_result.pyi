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


class TemplateValidationResult(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            ContentIsValid = schemas.BoolSchema
            RenderedContent = schemas.StrSchema
            
            
            class ValidationErrors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TemplateValidationError']:
                        return TemplateValidationError
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TemplateValidationError'], typing.List['TemplateValidationError']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ValidationErrors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TemplateValidationError':
                    return super().__getitem__(i)
            __annotations__ = {
                "ContentIsValid": ContentIsValid,
                "RenderedContent": RenderedContent,
                "ValidationErrors": ValidationErrors,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ContentIsValid"]) -> MetaOapg.properties.ContentIsValid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RenderedContent"]) -> MetaOapg.properties.RenderedContent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ValidationErrors"]) -> MetaOapg.properties.ValidationErrors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ContentIsValid", "RenderedContent", "ValidationErrors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ContentIsValid"]) -> typing.Union[MetaOapg.properties.ContentIsValid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RenderedContent"]) -> typing.Union[MetaOapg.properties.RenderedContent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ValidationErrors"]) -> typing.Union[MetaOapg.properties.ValidationErrors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ContentIsValid", "RenderedContent", "ValidationErrors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        ContentIsValid: typing.Union[MetaOapg.properties.ContentIsValid, bool, schemas.Unset] = schemas.unset,
        RenderedContent: typing.Union[MetaOapg.properties.RenderedContent, str, schemas.Unset] = schemas.unset,
        ValidationErrors: typing.Union[MetaOapg.properties.ValidationErrors, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateValidationResult':
        return super().__new__(
            cls,
            *args,
            ContentIsValid=ContentIsValid,
            RenderedContent=RenderedContent,
            ValidationErrors=ValidationErrors,
            _configuration=_configuration,
            **kwargs,
        )

from postmark_python_sdk.model.template_validation_error import TemplateValidationError
