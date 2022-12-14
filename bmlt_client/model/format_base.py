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


class FormatBase(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            worldId = schemas.StrSchema
            type = schemas.StrSchema
            
            
            class translations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FormatTranslation']:
                        return FormatTranslation
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FormatTranslation'], typing.List['FormatTranslation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'translations':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FormatTranslation':
                    return super().__getitem__(i)
            __annotations__ = {
                "worldId": worldId,
                "type": type,
                "translations": translations,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["worldId"]) -> MetaOapg.properties.worldId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translations"]) -> MetaOapg.properties.translations: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["worldId", "type", "translations", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["worldId"]) -> typing.Union[MetaOapg.properties.worldId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translations"]) -> typing.Union[MetaOapg.properties.translations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["worldId", "type", "translations", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        worldId: typing.Union[MetaOapg.properties.worldId, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        translations: typing.Union[MetaOapg.properties.translations, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FormatBase':
        return super().__new__(
            cls,
            *args,
            worldId=worldId,
            type=type,
            translations=translations,
            _configuration=_configuration,
            **kwargs,
        )

from bmlt_client.model.format_translation import FormatTranslation
