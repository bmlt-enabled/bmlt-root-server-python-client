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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from bmlt_client.models.format_translation import FormatTranslation

class FormatPartialUpdate(BaseModel):
    """
    FormatPartialUpdate
    """
    world_id: Optional[StrictStr] = Field(None, alias="worldId")
    type: Optional[StrictStr] = None
    translations: Optional[conlist(FormatTranslation)] = None
    __properties = ["worldId", "type", "translations"]

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
    def from_json(cls, json_str: str) -> FormatPartialUpdate:
        """Create an instance of FormatPartialUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in translations (list)
        _items = []
        if self.translations:
            for _item in self.translations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['translations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FormatPartialUpdate:
        """Create an instance of FormatPartialUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FormatPartialUpdate.parse_obj(obj)

        _obj = FormatPartialUpdate.parse_obj({
            "world_id": obj.get("worldId"),
            "type": obj.get("type"),
            "translations": [FormatTranslation.from_dict(_item) for _item in obj.get("translations")] if obj.get("translations") is not None else None
        })
        return _obj


