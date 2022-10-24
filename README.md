# bmlt-root-server-client
BMLT Admin API Documentation

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/bmlt-enabled/bmlt-root-server-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/bmlt-enabled/bmlt-root-server-python-client.git`)

Then import the package:
```python
import bmlt_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bmlt_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import bmlt_client
from pprint import pprint
from bmlt_client.apis.tags import root_server_api
from bmlt_client.model.error_incorrect_credentials import ErrorIncorrectCredentials
from bmlt_client.model.error_unauthenticated import ErrorUnauthenticated
from bmlt_client.model.error_unauthorized import ErrorUnauthorized
from bmlt_client.model.format import Format
from bmlt_client.model.format_collection import FormatCollection
from bmlt_client.model.format_create import FormatCreate
from bmlt_client.model.format_partial_update import FormatPartialUpdate
from bmlt_client.model.format_update import FormatUpdate
from bmlt_client.model.meeting import Meeting
from bmlt_client.model.meeting_collection import MeetingCollection
from bmlt_client.model.meeting_create import MeetingCreate
from bmlt_client.model.meeting_partial_update import MeetingPartialUpdate
from bmlt_client.model.meeting_update import MeetingUpdate
from bmlt_client.model.no_format_exists import NoFormatExists
from bmlt_client.model.no_meeting_exists import NoMeetingExists
from bmlt_client.model.no_service_body_exists import NoServiceBodyExists
from bmlt_client.model.no_user_exists import NoUserExists
from bmlt_client.model.service_body import ServiceBody
from bmlt_client.model.service_body_collection import ServiceBodyCollection
from bmlt_client.model.service_body_create import ServiceBodyCreate
from bmlt_client.model.service_body_partial_update import ServiceBodyPartialUpdate
from bmlt_client.model.service_body_update import ServiceBodyUpdate
from bmlt_client.model.token import Token
from bmlt_client.model.token_credentials import TokenCredentials
from bmlt_client.model.user import User
from bmlt_client.model.user_collection import UserCollection
from bmlt_client.model.user_create import UserCreate
from bmlt_client.model.user_partial_update import UserPartialUpdate
from bmlt_client.model.user_update import UserUpdate
from bmlt_client.model.validation_error import ValidationError
# Defining the host is optional and defaults to http://localhost:8000/main_server
# See configuration.py for a list of all supported configuration parameters.
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: bmltToken
configuration = bmlt_client.Configuration(
    host = "http://localhost:8000/main_server"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bmlt_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = root_server_api.RootServerApi(api_client)
    
    try:
        # Revokes a token
        api_instance.auth_logout()
    except bmlt_client.ApiException as e:
        print("Exception when calling RootServerApi->auth_logout: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8000/main_server*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RootServerApi* | [**auth_logout**](docs/apis/tags/RootServerApi.md#auth_logout) | **post** /api/v1/auth/logout | Revokes a token
*RootServerApi* | [**auth_refresh**](docs/apis/tags/RootServerApi.md#auth_refresh) | **post** /api/v1/auth/refresh | Revokes and issues a new token
*RootServerApi* | [**auth_token**](docs/apis/tags/RootServerApi.md#auth_token) | **post** /api/v1/auth/token | Creates a token
*RootServerApi* | [**create_format**](docs/apis/tags/RootServerApi.md#create_format) | **post** /api/v1/formats | Creates a format
*RootServerApi* | [**create_meeting**](docs/apis/tags/RootServerApi.md#create_meeting) | **post** /api/v1/meetings | Creates a meeting
*RootServerApi* | [**create_service_body**](docs/apis/tags/RootServerApi.md#create_service_body) | **post** /api/v1/servicebodies | Creates a service body
*RootServerApi* | [**create_user**](docs/apis/tags/RootServerApi.md#create_user) | **post** /api/v1/users | Creates a user
*RootServerApi* | [**delete_format**](docs/apis/tags/RootServerApi.md#delete_format) | **delete** /api/v1/formats/{formatId} | Deletes a format
*RootServerApi* | [**delete_meeting**](docs/apis/tags/RootServerApi.md#delete_meeting) | **delete** /api/v1/meetings/{meetingId} | Deletes a meeting
*RootServerApi* | [**delete_service_body**](docs/apis/tags/RootServerApi.md#delete_service_body) | **delete** /api/v1/servicebodies/{serviceBodyId} | Deletes a service body
*RootServerApi* | [**delete_user**](docs/apis/tags/RootServerApi.md#delete_user) | **delete** /api/v1/users/{userId} | Deletes a user
*RootServerApi* | [**get_format**](docs/apis/tags/RootServerApi.md#get_format) | **get** /api/v1/formats/{formatId} | Retrieves a format
*RootServerApi* | [**get_formats**](docs/apis/tags/RootServerApi.md#get_formats) | **get** /api/v1/formats | Retrieves formats
*RootServerApi* | [**get_meeting**](docs/apis/tags/RootServerApi.md#get_meeting) | **get** /api/v1/meetings/{meetingId} | Retrieves a meeting
*RootServerApi* | [**get_meetings**](docs/apis/tags/RootServerApi.md#get_meetings) | **get** /api/v1/meetings | Retrieves meetings
*RootServerApi* | [**get_service_bodies**](docs/apis/tags/RootServerApi.md#get_service_bodies) | **get** /api/v1/servicebodies | Retrieves service bodies
*RootServerApi* | [**get_service_body**](docs/apis/tags/RootServerApi.md#get_service_body) | **get** /api/v1/servicebodies/{serviceBodyId} | Retrieves a service body
*RootServerApi* | [**get_user**](docs/apis/tags/RootServerApi.md#get_user) | **get** /api/v1/users/{userId} | Retrieves a single user
*RootServerApi* | [**get_users**](docs/apis/tags/RootServerApi.md#get_users) | **get** /api/v1/users | Retrieves users
*RootServerApi* | [**partial_update_user**](docs/apis/tags/RootServerApi.md#partial_update_user) | **patch** /api/v1/users/{userId} | Patches a user
*RootServerApi* | [**patch_format**](docs/apis/tags/RootServerApi.md#patch_format) | **patch** /api/v1/formats/{formatId} | Patches a format
*RootServerApi* | [**patch_meeting**](docs/apis/tags/RootServerApi.md#patch_meeting) | **patch** /api/v1/meetings/{meetingId} | Patches a meeting
*RootServerApi* | [**patch_service_body**](docs/apis/tags/RootServerApi.md#patch_service_body) | **patch** /api/v1/servicebodies/{serviceBodyId} | Patches a service body
*RootServerApi* | [**update_format**](docs/apis/tags/RootServerApi.md#update_format) | **put** /api/v1/formats/{formatId} | Updates a format
*RootServerApi* | [**update_meeting**](docs/apis/tags/RootServerApi.md#update_meeting) | **put** /api/v1/meetings/{meetingId} | Updates a meeting
*RootServerApi* | [**update_service_body**](docs/apis/tags/RootServerApi.md#update_service_body) | **put** /api/v1/servicebodies/{serviceBodyId} | Updates a Service Body
*RootServerApi* | [**update_user**](docs/apis/tags/RootServerApi.md#update_user) | **put** /api/v1/users/{userId} | Update single user

## Documentation For Models

 - [ErrorIncorrectCredentials](docs/models/ErrorIncorrectCredentials.md)
 - [ErrorUnauthenticated](docs/models/ErrorUnauthenticated.md)
 - [ErrorUnauthorized](docs/models/ErrorUnauthorized.md)
 - [Format](docs/models/Format.md)
 - [FormatBase](docs/models/FormatBase.md)
 - [FormatCollection](docs/models/FormatCollection.md)
 - [FormatCreate](docs/models/FormatCreate.md)
 - [FormatPartialUpdate](docs/models/FormatPartialUpdate.md)
 - [FormatTranslation](docs/models/FormatTranslation.md)
 - [FormatUpdate](docs/models/FormatUpdate.md)
 - [Meeting](docs/models/Meeting.md)
 - [MeetingBase](docs/models/MeetingBase.md)
 - [MeetingCollection](docs/models/MeetingCollection.md)
 - [MeetingCreate](docs/models/MeetingCreate.md)
 - [MeetingPartialUpdate](docs/models/MeetingPartialUpdate.md)
 - [MeetingUpdate](docs/models/MeetingUpdate.md)
 - [NoFormatExists](docs/models/NoFormatExists.md)
 - [NoMeetingExists](docs/models/NoMeetingExists.md)
 - [NoServiceBodyExists](docs/models/NoServiceBodyExists.md)
 - [NoUserExists](docs/models/NoUserExists.md)
 - [ServiceBody](docs/models/ServiceBody.md)
 - [ServiceBodyBase](docs/models/ServiceBodyBase.md)
 - [ServiceBodyCollection](docs/models/ServiceBodyCollection.md)
 - [ServiceBodyCreate](docs/models/ServiceBodyCreate.md)
 - [ServiceBodyPartialUpdate](docs/models/ServiceBodyPartialUpdate.md)
 - [ServiceBodyUpdate](docs/models/ServiceBodyUpdate.md)
 - [Token](docs/models/Token.md)
 - [TokenCredentials](docs/models/TokenCredentials.md)
 - [User](docs/models/User.md)
 - [UserBase](docs/models/UserBase.md)
 - [UserCollection](docs/models/UserCollection.md)
 - [UserCreate](docs/models/UserCreate.md)
 - [UserPartialUpdate](docs/models/UserPartialUpdate.md)
 - [UserUpdate](docs/models/UserUpdate.md)
 - [ValidationError](docs/models/ValidationError.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## bmltToken

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author



## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in bmlt_client.apis and bmlt_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from bmlt_client.apis.default_api import DefaultApi`
- `from bmlt_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import bmlt_client
from bmlt_client.apis import *
from bmlt_client.models import *
```