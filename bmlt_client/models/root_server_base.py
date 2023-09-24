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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from bmlt_client.models.root_server_base_statistics import RootServerBaseStatistics

class RootServerBase(BaseModel):
    """
    RootServerBase
    """
    source_id: Optional[StrictInt] = Field(None, alias="sourceId")
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    statistics: Optional[RootServerBaseStatistics] = None
    server_info: Optional[StrictStr] = Field(None, alias="serverInfo")
    last_successful_import: Optional[datetime] = Field(None, alias="lastSuccessfulImport")
    __properties = ["sourceId", "name", "url", "statistics", "serverInfo", "lastSuccessfulImport"]

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
    def from_json(cls, json_str: str) -> RootServerBase:
        """Create an instance of RootServerBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RootServerBase:
        """Create an instance of RootServerBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RootServerBase.parse_obj(obj)

        _obj = RootServerBase.parse_obj({
            "source_id": obj.get("sourceId"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "statistics": RootServerBaseStatistics.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None,
            "server_info": obj.get("serverInfo"),
            "last_successful_import": obj.get("lastSuccessfulImport")
        })
        return _obj


