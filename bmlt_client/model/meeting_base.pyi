# coding: utf-8

"""
    BMLT

    BMLT Admin API Documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
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

from bmlt_client import schemas  # noqa: F401


class MeetingBase(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            serviceBodyId = schemas.IntSchema
            
            
            class formatIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'formatIds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            venueType = schemas.IntSchema
            temporarilyVirtual = schemas.BoolSchema
            day = schemas.IntSchema
            startTime = schemas.StrSchema
            duration = schemas.StrSchema
            timeZone = schemas.StrSchema
            latitude = schemas.Float32Schema
            longitude = schemas.Float32Schema
            published = schemas.BoolSchema
            email = schemas.StrSchema
            worldId = schemas.StrSchema
            name = schemas.StrSchema
            location_text = schemas.StrSchema
            location_info = schemas.StrSchema
            location_street = schemas.StrSchema
            location_neighborhood = schemas.StrSchema
            location_city_subsection = schemas.StrSchema
            location_municipality = schemas.StrSchema
            location_sub_province = schemas.StrSchema
            location_province = schemas.StrSchema
            location_postal_code_1 = schemas.StrSchema
            location_nation = schemas.StrSchema
            phone_meeting_number = schemas.StrSchema
            virtual_meeting_link = schemas.StrSchema
            virtual_meeting_additional_info = schemas.StrSchema
            contact_name_1 = schemas.StrSchema
            contact_name_2 = schemas.StrSchema
            contact_phone_1 = schemas.StrSchema
            contact_phone_2 = schemas.StrSchema
            contact_email_1 = schemas.StrSchema
            contact_email_2 = schemas.StrSchema
            bus_lines = schemas.StrSchema
            train_line = schemas.StrSchema
            comments = schemas.StrSchema
            __annotations__ = {
                "serviceBodyId": serviceBodyId,
                "formatIds": formatIds,
                "venueType": venueType,
                "temporarilyVirtual": temporarilyVirtual,
                "day": day,
                "startTime": startTime,
                "duration": duration,
                "timeZone": timeZone,
                "latitude": latitude,
                "longitude": longitude,
                "published": published,
                "email": email,
                "worldId": worldId,
                "name": name,
                "location_text": location_text,
                "location_info": location_info,
                "location_street": location_street,
                "location_neighborhood": location_neighborhood,
                "location_city_subsection": location_city_subsection,
                "location_municipality": location_municipality,
                "location_sub_province": location_sub_province,
                "location_province": location_province,
                "location_postal_code_1": location_postal_code_1,
                "location_nation": location_nation,
                "phone_meeting_number": phone_meeting_number,
                "virtual_meeting_link": virtual_meeting_link,
                "virtual_meeting_additional_info": virtual_meeting_additional_info,
                "contact_name_1": contact_name_1,
                "contact_name_2": contact_name_2,
                "contact_phone_1": contact_phone_1,
                "contact_phone_2": contact_phone_2,
                "contact_email_1": contact_email_1,
                "contact_email_2": contact_email_2,
                "bus_lines": bus_lines,
                "train_line": train_line,
                "comments": comments,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceBodyId"]) -> MetaOapg.properties.serviceBodyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["formatIds"]) -> MetaOapg.properties.formatIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["venueType"]) -> MetaOapg.properties.venueType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temporarilyVirtual"]) -> MetaOapg.properties.temporarilyVirtual: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["day"]) -> MetaOapg.properties.day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeZone"]) -> MetaOapg.properties.timeZone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published"]) -> MetaOapg.properties.published: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["worldId"]) -> MetaOapg.properties.worldId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_text"]) -> MetaOapg.properties.location_text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_info"]) -> MetaOapg.properties.location_info: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_street"]) -> MetaOapg.properties.location_street: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_neighborhood"]) -> MetaOapg.properties.location_neighborhood: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_city_subsection"]) -> MetaOapg.properties.location_city_subsection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_municipality"]) -> MetaOapg.properties.location_municipality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_sub_province"]) -> MetaOapg.properties.location_sub_province: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_province"]) -> MetaOapg.properties.location_province: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_postal_code_1"]) -> MetaOapg.properties.location_postal_code_1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_nation"]) -> MetaOapg.properties.location_nation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_meeting_number"]) -> MetaOapg.properties.phone_meeting_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["virtual_meeting_link"]) -> MetaOapg.properties.virtual_meeting_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["virtual_meeting_additional_info"]) -> MetaOapg.properties.virtual_meeting_additional_info: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_name_1"]) -> MetaOapg.properties.contact_name_1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_name_2"]) -> MetaOapg.properties.contact_name_2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_phone_1"]) -> MetaOapg.properties.contact_phone_1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_phone_2"]) -> MetaOapg.properties.contact_phone_2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_email_1"]) -> MetaOapg.properties.contact_email_1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_email_2"]) -> MetaOapg.properties.contact_email_2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bus_lines"]) -> MetaOapg.properties.bus_lines: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["train_line"]) -> MetaOapg.properties.train_line: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["serviceBodyId", "formatIds", "venueType", "temporarilyVirtual", "day", "startTime", "duration", "timeZone", "latitude", "longitude", "published", "email", "worldId", "name", "location_text", "location_info", "location_street", "location_neighborhood", "location_city_subsection", "location_municipality", "location_sub_province", "location_province", "location_postal_code_1", "location_nation", "phone_meeting_number", "virtual_meeting_link", "virtual_meeting_additional_info", "contact_name_1", "contact_name_2", "contact_phone_1", "contact_phone_2", "contact_email_1", "contact_email_2", "bus_lines", "train_line", "comments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceBodyId"]) -> typing.Union[MetaOapg.properties.serviceBodyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["formatIds"]) -> typing.Union[MetaOapg.properties.formatIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["venueType"]) -> typing.Union[MetaOapg.properties.venueType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temporarilyVirtual"]) -> typing.Union[MetaOapg.properties.temporarilyVirtual, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["day"]) -> typing.Union[MetaOapg.properties.day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> typing.Union[MetaOapg.properties.startTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeZone"]) -> typing.Union[MetaOapg.properties.timeZone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latitude"]) -> typing.Union[MetaOapg.properties.latitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longitude"]) -> typing.Union[MetaOapg.properties.longitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published"]) -> typing.Union[MetaOapg.properties.published, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["worldId"]) -> typing.Union[MetaOapg.properties.worldId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_text"]) -> typing.Union[MetaOapg.properties.location_text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_info"]) -> typing.Union[MetaOapg.properties.location_info, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_street"]) -> typing.Union[MetaOapg.properties.location_street, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_neighborhood"]) -> typing.Union[MetaOapg.properties.location_neighborhood, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_city_subsection"]) -> typing.Union[MetaOapg.properties.location_city_subsection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_municipality"]) -> typing.Union[MetaOapg.properties.location_municipality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_sub_province"]) -> typing.Union[MetaOapg.properties.location_sub_province, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_province"]) -> typing.Union[MetaOapg.properties.location_province, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_postal_code_1"]) -> typing.Union[MetaOapg.properties.location_postal_code_1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_nation"]) -> typing.Union[MetaOapg.properties.location_nation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_meeting_number"]) -> typing.Union[MetaOapg.properties.phone_meeting_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["virtual_meeting_link"]) -> typing.Union[MetaOapg.properties.virtual_meeting_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["virtual_meeting_additional_info"]) -> typing.Union[MetaOapg.properties.virtual_meeting_additional_info, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_name_1"]) -> typing.Union[MetaOapg.properties.contact_name_1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_name_2"]) -> typing.Union[MetaOapg.properties.contact_name_2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_phone_1"]) -> typing.Union[MetaOapg.properties.contact_phone_1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_phone_2"]) -> typing.Union[MetaOapg.properties.contact_phone_2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_email_1"]) -> typing.Union[MetaOapg.properties.contact_email_1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_email_2"]) -> typing.Union[MetaOapg.properties.contact_email_2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bus_lines"]) -> typing.Union[MetaOapg.properties.bus_lines, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["train_line"]) -> typing.Union[MetaOapg.properties.train_line, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["serviceBodyId", "formatIds", "venueType", "temporarilyVirtual", "day", "startTime", "duration", "timeZone", "latitude", "longitude", "published", "email", "worldId", "name", "location_text", "location_info", "location_street", "location_neighborhood", "location_city_subsection", "location_municipality", "location_sub_province", "location_province", "location_postal_code_1", "location_nation", "phone_meeting_number", "virtual_meeting_link", "virtual_meeting_additional_info", "contact_name_1", "contact_name_2", "contact_phone_1", "contact_phone_2", "contact_email_1", "contact_email_2", "bus_lines", "train_line", "comments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        serviceBodyId: typing.Union[MetaOapg.properties.serviceBodyId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        formatIds: typing.Union[MetaOapg.properties.formatIds, list, tuple, schemas.Unset] = schemas.unset,
        venueType: typing.Union[MetaOapg.properties.venueType, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        temporarilyVirtual: typing.Union[MetaOapg.properties.temporarilyVirtual, bool, schemas.Unset] = schemas.unset,
        day: typing.Union[MetaOapg.properties.day, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        startTime: typing.Union[MetaOapg.properties.startTime, str, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, str, schemas.Unset] = schemas.unset,
        timeZone: typing.Union[MetaOapg.properties.timeZone, str, schemas.Unset] = schemas.unset,
        latitude: typing.Union[MetaOapg.properties.latitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        longitude: typing.Union[MetaOapg.properties.longitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        published: typing.Union[MetaOapg.properties.published, bool, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        worldId: typing.Union[MetaOapg.properties.worldId, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        location_text: typing.Union[MetaOapg.properties.location_text, str, schemas.Unset] = schemas.unset,
        location_info: typing.Union[MetaOapg.properties.location_info, str, schemas.Unset] = schemas.unset,
        location_street: typing.Union[MetaOapg.properties.location_street, str, schemas.Unset] = schemas.unset,
        location_neighborhood: typing.Union[MetaOapg.properties.location_neighborhood, str, schemas.Unset] = schemas.unset,
        location_city_subsection: typing.Union[MetaOapg.properties.location_city_subsection, str, schemas.Unset] = schemas.unset,
        location_municipality: typing.Union[MetaOapg.properties.location_municipality, str, schemas.Unset] = schemas.unset,
        location_sub_province: typing.Union[MetaOapg.properties.location_sub_province, str, schemas.Unset] = schemas.unset,
        location_province: typing.Union[MetaOapg.properties.location_province, str, schemas.Unset] = schemas.unset,
        location_postal_code_1: typing.Union[MetaOapg.properties.location_postal_code_1, str, schemas.Unset] = schemas.unset,
        location_nation: typing.Union[MetaOapg.properties.location_nation, str, schemas.Unset] = schemas.unset,
        phone_meeting_number: typing.Union[MetaOapg.properties.phone_meeting_number, str, schemas.Unset] = schemas.unset,
        virtual_meeting_link: typing.Union[MetaOapg.properties.virtual_meeting_link, str, schemas.Unset] = schemas.unset,
        virtual_meeting_additional_info: typing.Union[MetaOapg.properties.virtual_meeting_additional_info, str, schemas.Unset] = schemas.unset,
        contact_name_1: typing.Union[MetaOapg.properties.contact_name_1, str, schemas.Unset] = schemas.unset,
        contact_name_2: typing.Union[MetaOapg.properties.contact_name_2, str, schemas.Unset] = schemas.unset,
        contact_phone_1: typing.Union[MetaOapg.properties.contact_phone_1, str, schemas.Unset] = schemas.unset,
        contact_phone_2: typing.Union[MetaOapg.properties.contact_phone_2, str, schemas.Unset] = schemas.unset,
        contact_email_1: typing.Union[MetaOapg.properties.contact_email_1, str, schemas.Unset] = schemas.unset,
        contact_email_2: typing.Union[MetaOapg.properties.contact_email_2, str, schemas.Unset] = schemas.unset,
        bus_lines: typing.Union[MetaOapg.properties.bus_lines, str, schemas.Unset] = schemas.unset,
        train_line: typing.Union[MetaOapg.properties.train_line, str, schemas.Unset] = schemas.unset,
        comments: typing.Union[MetaOapg.properties.comments, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingBase':
        return super().__new__(
            cls,
            *args,
            serviceBodyId=serviceBodyId,
            formatIds=formatIds,
            venueType=venueType,
            temporarilyVirtual=temporarilyVirtual,
            day=day,
            startTime=startTime,
            duration=duration,
            timeZone=timeZone,
            latitude=latitude,
            longitude=longitude,
            published=published,
            email=email,
            worldId=worldId,
            name=name,
            location_text=location_text,
            location_info=location_info,
            location_street=location_street,
            location_neighborhood=location_neighborhood,
            location_city_subsection=location_city_subsection,
            location_municipality=location_municipality,
            location_sub_province=location_sub_province,
            location_province=location_province,
            location_postal_code_1=location_postal_code_1,
            location_nation=location_nation,
            phone_meeting_number=phone_meeting_number,
            virtual_meeting_link=virtual_meeting_link,
            virtual_meeting_additional_info=virtual_meeting_additional_info,
            contact_name_1=contact_name_1,
            contact_name_2=contact_name_2,
            contact_phone_1=contact_phone_1,
            contact_phone_2=contact_phone_2,
            contact_email_1=contact_email_1,
            contact_email_2=contact_email_2,
            bus_lines=bus_lines,
            train_line=train_line,
            comments=comments,
            _configuration=_configuration,
            **kwargs,
        )
