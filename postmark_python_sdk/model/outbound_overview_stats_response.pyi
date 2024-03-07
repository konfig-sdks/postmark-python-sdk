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


class OutboundOverviewStatsResponse(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            BounceRate = schemas.IntSchema
            Bounced = schemas.IntSchema
            Opens = schemas.IntSchema
            SMTPAPIErrors = schemas.IntSchema
            Sent = schemas.IntSchema
            SpamComplaints = schemas.IntSchema
            SpamComplaintsRate = schemas.IntSchema
            TotalClicks = schemas.IntSchema
            TotalTrackedLinksSent = schemas.IntSchema
            Tracked = schemas.IntSchema
            UniqueLinksClicked = schemas.IntSchema
            UniqueOpens = schemas.IntSchema
            WithClientRecorded = schemas.IntSchema
            WithLinkTracking = schemas.IntSchema
            WithOpenTracking = schemas.IntSchema
            WithPlatformRecorded = schemas.IntSchema
            __annotations__ = {
                "BounceRate": BounceRate,
                "Bounced": Bounced,
                "Opens": Opens,
                "SMTPAPIErrors": SMTPAPIErrors,
                "Sent": Sent,
                "SpamComplaints": SpamComplaints,
                "SpamComplaintsRate": SpamComplaintsRate,
                "TotalClicks": TotalClicks,
                "TotalTrackedLinksSent": TotalTrackedLinksSent,
                "Tracked": Tracked,
                "UniqueLinksClicked": UniqueLinksClicked,
                "UniqueOpens": UniqueOpens,
                "WithClientRecorded": WithClientRecorded,
                "WithLinkTracking": WithLinkTracking,
                "WithOpenTracking": WithOpenTracking,
                "WithPlatformRecorded": WithPlatformRecorded,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BounceRate"]) -> MetaOapg.properties.BounceRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Bounced"]) -> MetaOapg.properties.Bounced: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Opens"]) -> MetaOapg.properties.Opens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SMTPAPIErrors"]) -> MetaOapg.properties.SMTPAPIErrors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Sent"]) -> MetaOapg.properties.Sent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SpamComplaints"]) -> MetaOapg.properties.SpamComplaints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SpamComplaintsRate"]) -> MetaOapg.properties.SpamComplaintsRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalClicks"]) -> MetaOapg.properties.TotalClicks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalTrackedLinksSent"]) -> MetaOapg.properties.TotalTrackedLinksSent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Tracked"]) -> MetaOapg.properties.Tracked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UniqueLinksClicked"]) -> MetaOapg.properties.UniqueLinksClicked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UniqueOpens"]) -> MetaOapg.properties.UniqueOpens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WithClientRecorded"]) -> MetaOapg.properties.WithClientRecorded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WithLinkTracking"]) -> MetaOapg.properties.WithLinkTracking: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WithOpenTracking"]) -> MetaOapg.properties.WithOpenTracking: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WithPlatformRecorded"]) -> MetaOapg.properties.WithPlatformRecorded: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["BounceRate", "Bounced", "Opens", "SMTPAPIErrors", "Sent", "SpamComplaints", "SpamComplaintsRate", "TotalClicks", "TotalTrackedLinksSent", "Tracked", "UniqueLinksClicked", "UniqueOpens", "WithClientRecorded", "WithLinkTracking", "WithOpenTracking", "WithPlatformRecorded", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BounceRate"]) -> typing.Union[MetaOapg.properties.BounceRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Bounced"]) -> typing.Union[MetaOapg.properties.Bounced, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Opens"]) -> typing.Union[MetaOapg.properties.Opens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SMTPAPIErrors"]) -> typing.Union[MetaOapg.properties.SMTPAPIErrors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Sent"]) -> typing.Union[MetaOapg.properties.Sent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SpamComplaints"]) -> typing.Union[MetaOapg.properties.SpamComplaints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SpamComplaintsRate"]) -> typing.Union[MetaOapg.properties.SpamComplaintsRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalClicks"]) -> typing.Union[MetaOapg.properties.TotalClicks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalTrackedLinksSent"]) -> typing.Union[MetaOapg.properties.TotalTrackedLinksSent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Tracked"]) -> typing.Union[MetaOapg.properties.Tracked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UniqueLinksClicked"]) -> typing.Union[MetaOapg.properties.UniqueLinksClicked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UniqueOpens"]) -> typing.Union[MetaOapg.properties.UniqueOpens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WithClientRecorded"]) -> typing.Union[MetaOapg.properties.WithClientRecorded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WithLinkTracking"]) -> typing.Union[MetaOapg.properties.WithLinkTracking, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WithOpenTracking"]) -> typing.Union[MetaOapg.properties.WithOpenTracking, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WithPlatformRecorded"]) -> typing.Union[MetaOapg.properties.WithPlatformRecorded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["BounceRate", "Bounced", "Opens", "SMTPAPIErrors", "Sent", "SpamComplaints", "SpamComplaintsRate", "TotalClicks", "TotalTrackedLinksSent", "Tracked", "UniqueLinksClicked", "UniqueOpens", "WithClientRecorded", "WithLinkTracking", "WithOpenTracking", "WithPlatformRecorded", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        BounceRate: typing.Union[MetaOapg.properties.BounceRate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Bounced: typing.Union[MetaOapg.properties.Bounced, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Opens: typing.Union[MetaOapg.properties.Opens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        SMTPAPIErrors: typing.Union[MetaOapg.properties.SMTPAPIErrors, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Sent: typing.Union[MetaOapg.properties.Sent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        SpamComplaints: typing.Union[MetaOapg.properties.SpamComplaints, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        SpamComplaintsRate: typing.Union[MetaOapg.properties.SpamComplaintsRate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TotalClicks: typing.Union[MetaOapg.properties.TotalClicks, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TotalTrackedLinksSent: typing.Union[MetaOapg.properties.TotalTrackedLinksSent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Tracked: typing.Union[MetaOapg.properties.Tracked, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        UniqueLinksClicked: typing.Union[MetaOapg.properties.UniqueLinksClicked, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        UniqueOpens: typing.Union[MetaOapg.properties.UniqueOpens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        WithClientRecorded: typing.Union[MetaOapg.properties.WithClientRecorded, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        WithLinkTracking: typing.Union[MetaOapg.properties.WithLinkTracking, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        WithOpenTracking: typing.Union[MetaOapg.properties.WithOpenTracking, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        WithPlatformRecorded: typing.Union[MetaOapg.properties.WithPlatformRecorded, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OutboundOverviewStatsResponse':
        return super().__new__(
            cls,
            *args,
            BounceRate=BounceRate,
            Bounced=Bounced,
            Opens=Opens,
            SMTPAPIErrors=SMTPAPIErrors,
            Sent=Sent,
            SpamComplaints=SpamComplaints,
            SpamComplaintsRate=SpamComplaintsRate,
            TotalClicks=TotalClicks,
            TotalTrackedLinksSent=TotalTrackedLinksSent,
            Tracked=Tracked,
            UniqueLinksClicked=UniqueLinksClicked,
            UniqueOpens=UniqueOpens,
            WithClientRecorded=WithClientRecorded,
            WithLinkTracking=WithLinkTracking,
            WithOpenTracking=WithOpenTracking,
            WithPlatformRecorded=WithPlatformRecorded,
            _configuration=_configuration,
            **kwargs,
        )
