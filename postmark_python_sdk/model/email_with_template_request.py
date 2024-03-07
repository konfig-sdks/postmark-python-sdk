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


class EmailWithTemplateRequest(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "From",
            "TemplateModel",
            "To",
            "TemplateId",
            "TemplateAlias",
        }
        
        class properties:
            _from = schemas.StrSchema
            TemplateAlias = schemas.StrSchema
            TemplateId = schemas.IntSchema
            TemplateModel = schemas.DictSchema
            To = schemas.StrSchema
        
            @staticmethod
            def Attachments() -> typing.Type['AttachmentCollection']:
                return AttachmentCollection
            Bcc = schemas.StrSchema
            Cc = schemas.StrSchema
        
            @staticmethod
            def Headers() -> typing.Type['HeaderCollection']:
                return HeaderCollection
            InlineCss = schemas.BoolSchema
            ReplyTo = schemas.StrSchema
            Tag = schemas.StrSchema
            
            
            class TrackLinks(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "None": "NONE",
                        "HtmlAndText": "HTML_AND_TEXT",
                        "HtmlOnly": "HTML_ONLY",
                        "TextOnly": "TEXT_ONLY",
                    }
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("None")
                
                @schemas.classproperty
                def HTML_AND_TEXT(cls):
                    return cls("HtmlAndText")
                
                @schemas.classproperty
                def HTML_ONLY(cls):
                    return cls("HtmlOnly")
                
                @schemas.classproperty
                def TEXT_ONLY(cls):
                    return cls("TextOnly")
            TrackOpens = schemas.BoolSchema
            __annotations__ = {
                "From": _from,
                "TemplateAlias": TemplateAlias,
                "TemplateId": TemplateId,
                "TemplateModel": TemplateModel,
                "To": To,
                "Attachments": Attachments,
                "Bcc": Bcc,
                "Cc": Cc,
                "Headers": Headers,
                "InlineCss": InlineCss,
                "ReplyTo": ReplyTo,
                "Tag": Tag,
                "TrackLinks": TrackLinks,
                "TrackOpens": TrackOpens,
            }

    
    TemplateModel: MetaOapg.properties.TemplateModel
    To: MetaOapg.properties.To
    TemplateId: MetaOapg.properties.TemplateId
    TemplateAlias: MetaOapg.properties.TemplateAlias
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["From"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TemplateAlias"]) -> MetaOapg.properties.TemplateAlias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TemplateId"]) -> MetaOapg.properties.TemplateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TemplateModel"]) -> MetaOapg.properties.TemplateModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["To"]) -> MetaOapg.properties.To: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Attachments"]) -> 'AttachmentCollection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Bcc"]) -> MetaOapg.properties.Bcc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Cc"]) -> MetaOapg.properties.Cc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Headers"]) -> 'HeaderCollection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["InlineCss"]) -> MetaOapg.properties.InlineCss: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ReplyTo"]) -> MetaOapg.properties.ReplyTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Tag"]) -> MetaOapg.properties.Tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TrackLinks"]) -> MetaOapg.properties.TrackLinks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TrackOpens"]) -> MetaOapg.properties.TrackOpens: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["From", "TemplateAlias", "TemplateId", "TemplateModel", "To", "Attachments", "Bcc", "Cc", "Headers", "InlineCss", "ReplyTo", "Tag", "TrackLinks", "TrackOpens", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["From"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TemplateAlias"]) -> MetaOapg.properties.TemplateAlias: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TemplateId"]) -> MetaOapg.properties.TemplateId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TemplateModel"]) -> MetaOapg.properties.TemplateModel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["To"]) -> MetaOapg.properties.To: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Attachments"]) -> typing.Union['AttachmentCollection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Bcc"]) -> typing.Union[MetaOapg.properties.Bcc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Cc"]) -> typing.Union[MetaOapg.properties.Cc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Headers"]) -> typing.Union['HeaderCollection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["InlineCss"]) -> typing.Union[MetaOapg.properties.InlineCss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ReplyTo"]) -> typing.Union[MetaOapg.properties.ReplyTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Tag"]) -> typing.Union[MetaOapg.properties.Tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TrackLinks"]) -> typing.Union[MetaOapg.properties.TrackLinks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TrackOpens"]) -> typing.Union[MetaOapg.properties.TrackOpens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["From", "TemplateAlias", "TemplateId", "TemplateModel", "To", "Attachments", "Bcc", "Cc", "Headers", "InlineCss", "ReplyTo", "Tag", "TrackLinks", "TrackOpens", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        TemplateModel: typing.Union[MetaOapg.properties.TemplateModel, dict, frozendict.frozendict, ],
        To: typing.Union[MetaOapg.properties.To, str, ],
        TemplateId: typing.Union[MetaOapg.properties.TemplateId, decimal.Decimal, int, ],
        TemplateAlias: typing.Union[MetaOapg.properties.TemplateAlias, str, ],
        Attachments: typing.Union['AttachmentCollection', schemas.Unset] = schemas.unset,
        Bcc: typing.Union[MetaOapg.properties.Bcc, str, schemas.Unset] = schemas.unset,
        Cc: typing.Union[MetaOapg.properties.Cc, str, schemas.Unset] = schemas.unset,
        Headers: typing.Union['HeaderCollection', schemas.Unset] = schemas.unset,
        InlineCss: typing.Union[MetaOapg.properties.InlineCss, bool, schemas.Unset] = schemas.unset,
        ReplyTo: typing.Union[MetaOapg.properties.ReplyTo, str, schemas.Unset] = schemas.unset,
        Tag: typing.Union[MetaOapg.properties.Tag, str, schemas.Unset] = schemas.unset,
        TrackLinks: typing.Union[MetaOapg.properties.TrackLinks, str, schemas.Unset] = schemas.unset,
        TrackOpens: typing.Union[MetaOapg.properties.TrackOpens, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmailWithTemplateRequest':
        return super().__new__(
            cls,
            *args,
            TemplateModel=TemplateModel,
            To=To,
            TemplateId=TemplateId,
            TemplateAlias=TemplateAlias,
            Attachments=Attachments,
            Bcc=Bcc,
            Cc=Cc,
            Headers=Headers,
            InlineCss=InlineCss,
            ReplyTo=ReplyTo,
            Tag=Tag,
            TrackLinks=TrackLinks,
            TrackOpens=TrackOpens,
            _configuration=_configuration,
            **kwargs,
        )

from postmark_python_sdk.model.attachment_collection import AttachmentCollection
from postmark_python_sdk.model.header_collection import HeaderCollection