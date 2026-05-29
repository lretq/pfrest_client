from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_restapi_access_list_entry_endpoint_response_400 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse400,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_401 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse401,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_403 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse403,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_404 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse404,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_405 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse405,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_406 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse406,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_409 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse409,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_415 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse415,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_422 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse422,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_424 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse424,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_500 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse500,
)
from ...models.get_system_restapi_access_list_entry_endpoint_response_503 import (
    GetSystemRESTAPIAccessListEntryEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/restapi/access_list/entry",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemRESTAPIAccessListEntryEndpointResponse400
    | GetSystemRESTAPIAccessListEntryEndpointResponse401
    | GetSystemRESTAPIAccessListEntryEndpointResponse403
    | GetSystemRESTAPIAccessListEntryEndpointResponse404
    | GetSystemRESTAPIAccessListEntryEndpointResponse405
    | GetSystemRESTAPIAccessListEntryEndpointResponse406
    | GetSystemRESTAPIAccessListEntryEndpointResponse409
    | GetSystemRESTAPIAccessListEntryEndpointResponse415
    | GetSystemRESTAPIAccessListEntryEndpointResponse422
    | GetSystemRESTAPIAccessListEntryEndpointResponse424
    | GetSystemRESTAPIAccessListEntryEndpointResponse500
    | GetSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemRESTAPIAccessListEntryEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemRESTAPIAccessListEntryEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemRESTAPIAccessListEntryEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemRESTAPIAccessListEntryEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemRESTAPIAccessListEntryEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemRESTAPIAccessListEntryEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemRESTAPIAccessListEntryEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemRESTAPIAccessListEntryEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemRESTAPIAccessListEntryEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemRESTAPIAccessListEntryEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemRESTAPIAccessListEntryEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemRESTAPIAccessListEntryEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemRESTAPIAccessListEntryEndpointResponse400
    | GetSystemRESTAPIAccessListEntryEndpointResponse401
    | GetSystemRESTAPIAccessListEntryEndpointResponse403
    | GetSystemRESTAPIAccessListEntryEndpointResponse404
    | GetSystemRESTAPIAccessListEntryEndpointResponse405
    | GetSystemRESTAPIAccessListEntryEndpointResponse406
    | GetSystemRESTAPIAccessListEntryEndpointResponse409
    | GetSystemRESTAPIAccessListEntryEndpointResponse415
    | GetSystemRESTAPIAccessListEntryEndpointResponse422
    | GetSystemRESTAPIAccessListEntryEndpointResponse424
    | GetSystemRESTAPIAccessListEntryEndpointResponse500
    | GetSystemRESTAPIAccessListEntryEndpointResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    GetSystemRESTAPIAccessListEntryEndpointResponse400
    | GetSystemRESTAPIAccessListEntryEndpointResponse401
    | GetSystemRESTAPIAccessListEntryEndpointResponse403
    | GetSystemRESTAPIAccessListEntryEndpointResponse404
    | GetSystemRESTAPIAccessListEntryEndpointResponse405
    | GetSystemRESTAPIAccessListEntryEndpointResponse406
    | GetSystemRESTAPIAccessListEntryEndpointResponse409
    | GetSystemRESTAPIAccessListEntryEndpointResponse415
    | GetSystemRESTAPIAccessListEntryEndpointResponse422
    | GetSystemRESTAPIAccessListEntryEndpointResponse424
    | GetSystemRESTAPIAccessListEntryEndpointResponse500
    | GetSystemRESTAPIAccessListEntryEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-
    get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemRESTAPIAccessListEntryEndpointResponse400 | GetSystemRESTAPIAccessListEntryEndpointResponse401 | GetSystemRESTAPIAccessListEntryEndpointResponse403 | GetSystemRESTAPIAccessListEntryEndpointResponse404 | GetSystemRESTAPIAccessListEntryEndpointResponse405 | GetSystemRESTAPIAccessListEntryEndpointResponse406 | GetSystemRESTAPIAccessListEntryEndpointResponse409 | GetSystemRESTAPIAccessListEntryEndpointResponse415 | GetSystemRESTAPIAccessListEntryEndpointResponse422 | GetSystemRESTAPIAccessListEntryEndpointResponse424 | GetSystemRESTAPIAccessListEntryEndpointResponse500 | GetSystemRESTAPIAccessListEntryEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    GetSystemRESTAPIAccessListEntryEndpointResponse400
    | GetSystemRESTAPIAccessListEntryEndpointResponse401
    | GetSystemRESTAPIAccessListEntryEndpointResponse403
    | GetSystemRESTAPIAccessListEntryEndpointResponse404
    | GetSystemRESTAPIAccessListEntryEndpointResponse405
    | GetSystemRESTAPIAccessListEntryEndpointResponse406
    | GetSystemRESTAPIAccessListEntryEndpointResponse409
    | GetSystemRESTAPIAccessListEntryEndpointResponse415
    | GetSystemRESTAPIAccessListEntryEndpointResponse422
    | GetSystemRESTAPIAccessListEntryEndpointResponse424
    | GetSystemRESTAPIAccessListEntryEndpointResponse500
    | GetSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-
    get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemRESTAPIAccessListEntryEndpointResponse400 | GetSystemRESTAPIAccessListEntryEndpointResponse401 | GetSystemRESTAPIAccessListEntryEndpointResponse403 | GetSystemRESTAPIAccessListEntryEndpointResponse404 | GetSystemRESTAPIAccessListEntryEndpointResponse405 | GetSystemRESTAPIAccessListEntryEndpointResponse406 | GetSystemRESTAPIAccessListEntryEndpointResponse409 | GetSystemRESTAPIAccessListEntryEndpointResponse415 | GetSystemRESTAPIAccessListEntryEndpointResponse422 | GetSystemRESTAPIAccessListEntryEndpointResponse424 | GetSystemRESTAPIAccessListEntryEndpointResponse500 | GetSystemRESTAPIAccessListEntryEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    GetSystemRESTAPIAccessListEntryEndpointResponse400
    | GetSystemRESTAPIAccessListEntryEndpointResponse401
    | GetSystemRESTAPIAccessListEntryEndpointResponse403
    | GetSystemRESTAPIAccessListEntryEndpointResponse404
    | GetSystemRESTAPIAccessListEntryEndpointResponse405
    | GetSystemRESTAPIAccessListEntryEndpointResponse406
    | GetSystemRESTAPIAccessListEntryEndpointResponse409
    | GetSystemRESTAPIAccessListEntryEndpointResponse415
    | GetSystemRESTAPIAccessListEntryEndpointResponse422
    | GetSystemRESTAPIAccessListEntryEndpointResponse424
    | GetSystemRESTAPIAccessListEntryEndpointResponse500
    | GetSystemRESTAPIAccessListEntryEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-
    get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemRESTAPIAccessListEntryEndpointResponse400 | GetSystemRESTAPIAccessListEntryEndpointResponse401 | GetSystemRESTAPIAccessListEntryEndpointResponse403 | GetSystemRESTAPIAccessListEntryEndpointResponse404 | GetSystemRESTAPIAccessListEntryEndpointResponse405 | GetSystemRESTAPIAccessListEntryEndpointResponse406 | GetSystemRESTAPIAccessListEntryEndpointResponse409 | GetSystemRESTAPIAccessListEntryEndpointResponse415 | GetSystemRESTAPIAccessListEntryEndpointResponse422 | GetSystemRESTAPIAccessListEntryEndpointResponse424 | GetSystemRESTAPIAccessListEntryEndpointResponse500 | GetSystemRESTAPIAccessListEntryEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    GetSystemRESTAPIAccessListEntryEndpointResponse400
    | GetSystemRESTAPIAccessListEntryEndpointResponse401
    | GetSystemRESTAPIAccessListEntryEndpointResponse403
    | GetSystemRESTAPIAccessListEntryEndpointResponse404
    | GetSystemRESTAPIAccessListEntryEndpointResponse405
    | GetSystemRESTAPIAccessListEntryEndpointResponse406
    | GetSystemRESTAPIAccessListEntryEndpointResponse409
    | GetSystemRESTAPIAccessListEntryEndpointResponse415
    | GetSystemRESTAPIAccessListEntryEndpointResponse422
    | GetSystemRESTAPIAccessListEntryEndpointResponse424
    | GetSystemRESTAPIAccessListEntryEndpointResponse500
    | GetSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-
    get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemRESTAPIAccessListEntryEndpointResponse400 | GetSystemRESTAPIAccessListEntryEndpointResponse401 | GetSystemRESTAPIAccessListEntryEndpointResponse403 | GetSystemRESTAPIAccessListEntryEndpointResponse404 | GetSystemRESTAPIAccessListEntryEndpointResponse405 | GetSystemRESTAPIAccessListEntryEndpointResponse406 | GetSystemRESTAPIAccessListEntryEndpointResponse409 | GetSystemRESTAPIAccessListEntryEndpointResponse415 | GetSystemRESTAPIAccessListEntryEndpointResponse422 | GetSystemRESTAPIAccessListEntryEndpointResponse424 | GetSystemRESTAPIAccessListEntryEndpointResponse500 | GetSystemRESTAPIAccessListEntryEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
