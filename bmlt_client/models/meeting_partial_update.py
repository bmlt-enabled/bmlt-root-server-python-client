# coding: utf-8

"""
    BMLT

    BMLT Admin API Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist

class MeetingPartialUpdate(BaseModel):
    """
    MeetingPartialUpdate
    """
    service_body_id: StrictInt = Field(..., alias="serviceBodyId")
    format_ids: conlist(StrictInt) = Field(..., alias="formatIds")
    venue_type: StrictInt = Field(..., alias="venueType")
    temporarily_virtual: Optional[StrictBool] = Field(None, alias="temporarilyVirtual")
    day: StrictInt = Field(...)
    start_time: StrictStr = Field(..., alias="startTime")
    duration: StrictStr = Field(...)
    time_zone: Optional[StrictStr] = Field(None, alias="timeZone")
    latitude: Union[StrictFloat, StrictInt] = Field(...)
    longitude: Union[StrictFloat, StrictInt] = Field(...)
    published: StrictBool = Field(...)
    email: Optional[StrictStr] = None
    world_id: Optional[StrictStr] = Field(None, alias="worldId")
    name: StrictStr = Field(...)
    location_text: Optional[StrictStr] = None
    location_info: Optional[StrictStr] = None
    location_street: Optional[StrictStr] = None
    location_neighborhood: Optional[StrictStr] = None
    location_city_subsection: Optional[StrictStr] = None
    location_municipality: Optional[StrictStr] = None
    location_sub_province: Optional[StrictStr] = None
    location_province: Optional[StrictStr] = None
    location_postal_code_1: Optional[StrictStr] = None
    location_nation: Optional[StrictStr] = None
    phone_meeting_number: Optional[StrictStr] = None
    virtual_meeting_link: Optional[StrictStr] = None
    virtual_meeting_additional_info: Optional[StrictStr] = None
    contact_name_1: Optional[StrictStr] = None
    contact_name_2: Optional[StrictStr] = None
    contact_phone_1: Optional[StrictStr] = None
    contact_phone_2: Optional[StrictStr] = None
    contact_email_1: Optional[StrictStr] = None
    contact_email_2: Optional[StrictStr] = None
    bus_lines: Optional[StrictStr] = None
    train_line: Optional[StrictStr] = None
    comments: Optional[StrictStr] = None
    __properties = ["serviceBodyId", "formatIds", "venueType", "temporarilyVirtual", "day", "startTime", "duration", "timeZone", "latitude", "longitude", "published", "email", "worldId", "name", "location_text", "location_info", "location_street", "location_neighborhood", "location_city_subsection", "location_municipality", "location_sub_province", "location_province", "location_postal_code_1", "location_nation", "phone_meeting_number", "virtual_meeting_link", "virtual_meeting_additional_info", "contact_name_1", "contact_name_2", "contact_phone_1", "contact_phone_2", "contact_email_1", "contact_email_2", "bus_lines", "train_line", "comments"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MeetingPartialUpdate:
        """Create an instance of MeetingPartialUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MeetingPartialUpdate:
        """Create an instance of MeetingPartialUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MeetingPartialUpdate.parse_obj(obj)

        _obj = MeetingPartialUpdate.parse_obj({
            "service_body_id": obj.get("serviceBodyId"),
            "format_ids": obj.get("formatIds"),
            "venue_type": obj.get("venueType"),
            "temporarily_virtual": obj.get("temporarilyVirtual"),
            "day": obj.get("day"),
            "start_time": obj.get("startTime"),
            "duration": obj.get("duration"),
            "time_zone": obj.get("timeZone"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "published": obj.get("published"),
            "email": obj.get("email"),
            "world_id": obj.get("worldId"),
            "name": obj.get("name"),
            "location_text": obj.get("location_text"),
            "location_info": obj.get("location_info"),
            "location_street": obj.get("location_street"),
            "location_neighborhood": obj.get("location_neighborhood"),
            "location_city_subsection": obj.get("location_city_subsection"),
            "location_municipality": obj.get("location_municipality"),
            "location_sub_province": obj.get("location_sub_province"),
            "location_province": obj.get("location_province"),
            "location_postal_code_1": obj.get("location_postal_code_1"),
            "location_nation": obj.get("location_nation"),
            "phone_meeting_number": obj.get("phone_meeting_number"),
            "virtual_meeting_link": obj.get("virtual_meeting_link"),
            "virtual_meeting_additional_info": obj.get("virtual_meeting_additional_info"),
            "contact_name_1": obj.get("contact_name_1"),
            "contact_name_2": obj.get("contact_name_2"),
            "contact_phone_1": obj.get("contact_phone_1"),
            "contact_phone_2": obj.get("contact_phone_2"),
            "contact_email_1": obj.get("contact_email_1"),
            "contact_email_2": obj.get("contact_email_2"),
            "bus_lines": obj.get("bus_lines"),
            "train_line": obj.get("train_line"),
            "comments": obj.get("comments")
        })
        return _obj


