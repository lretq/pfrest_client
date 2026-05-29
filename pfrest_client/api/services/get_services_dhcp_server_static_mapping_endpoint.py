from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_400 import (
    GetServicesDHCPServerStaticMappingEndpointResponse400,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_401 import (
    GetServicesDHCPServerStaticMappingEndpointResponse401,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_403 import (
    GetServicesDHCPServerStaticMappingEndpointResponse403,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_404 import (
    GetServicesDHCPServerStaticMappingEndpointResponse404,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_405 import (
    GetServicesDHCPServerStaticMappingEndpointResponse405,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_406 import (
    GetServicesDHCPServerStaticMappingEndpointResponse406,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_409 import (
    GetServicesDHCPServerStaticMappingEndpointResponse409,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_415 import (
    GetServicesDHCPServerStaticMappingEndpointResponse415,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_422 import (
    GetServicesDHCPServerStaticMappingEndpointResponse422,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_424 import (
    GetServicesDHCPServerStaticMappingEndpointResponse424,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_500 import (
    GetServicesDHCPServerStaticMappingEndpointResponse500,
)
from ...models.get_services_dhcp_server_static_mapping_endpoint_response_503 import (
    GetServicesDHCPServerStaticMappingEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/dhcp_server/static_mapping",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesDHCPServerStaticMappingEndpointResponse400
    | GetServicesDHCPServerStaticMappingEndpointResponse401
    | GetServicesDHCPServerStaticMappingEndpointResponse403
    | GetServicesDHCPServerStaticMappingEndpointResponse404
    | GetServicesDHCPServerStaticMappingEndpointResponse405
    | GetServicesDHCPServerStaticMappingEndpointResponse406
    | GetServicesDHCPServerStaticMappingEndpointResponse409
    | GetServicesDHCPServerStaticMappingEndpointResponse415
    | GetServicesDHCPServerStaticMappingEndpointResponse422
    | GetServicesDHCPServerStaticMappingEndpointResponse424
    | GetServicesDHCPServerStaticMappingEndpointResponse500
    | GetServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesDHCPServerStaticMappingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesDHCPServerStaticMappingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesDHCPServerStaticMappingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesDHCPServerStaticMappingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesDHCPServerStaticMappingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesDHCPServerStaticMappingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesDHCPServerStaticMappingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesDHCPServerStaticMappingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesDHCPServerStaticMappingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesDHCPServerStaticMappingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesDHCPServerStaticMappingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesDHCPServerStaticMappingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesDHCPServerStaticMappingEndpointResponse400
    | GetServicesDHCPServerStaticMappingEndpointResponse401
    | GetServicesDHCPServerStaticMappingEndpointResponse403
    | GetServicesDHCPServerStaticMappingEndpointResponse404
    | GetServicesDHCPServerStaticMappingEndpointResponse405
    | GetServicesDHCPServerStaticMappingEndpointResponse406
    | GetServicesDHCPServerStaticMappingEndpointResponse409
    | GetServicesDHCPServerStaticMappingEndpointResponse415
    | GetServicesDHCPServerStaticMappingEndpointResponse422
    | GetServicesDHCPServerStaticMappingEndpointResponse424
    | GetServicesDHCPServerStaticMappingEndpointResponse500
    | GetServicesDHCPServerStaticMappingEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
) -> Response[
    GetServicesDHCPServerStaticMappingEndpointResponse400
    | GetServicesDHCPServerStaticMappingEndpointResponse401
    | GetServicesDHCPServerStaticMappingEndpointResponse403
    | GetServicesDHCPServerStaticMappingEndpointResponse404
    | GetServicesDHCPServerStaticMappingEndpointResponse405
    | GetServicesDHCPServerStaticMappingEndpointResponse406
    | GetServicesDHCPServerStaticMappingEndpointResponse409
    | GetServicesDHCPServerStaticMappingEndpointResponse415
    | GetServicesDHCPServerStaticMappingEndpointResponse422
    | GetServicesDHCPServerStaticMappingEndpointResponse424
    | GetServicesDHCPServerStaticMappingEndpointResponse500
    | GetServicesDHCPServerStaticMappingEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDHCPServerStaticMappingEndpointResponse400 | GetServicesDHCPServerStaticMappingEndpointResponse401 | GetServicesDHCPServerStaticMappingEndpointResponse403 | GetServicesDHCPServerStaticMappingEndpointResponse404 | GetServicesDHCPServerStaticMappingEndpointResponse405 | GetServicesDHCPServerStaticMappingEndpointResponse406 | GetServicesDHCPServerStaticMappingEndpointResponse409 | GetServicesDHCPServerStaticMappingEndpointResponse415 | GetServicesDHCPServerStaticMappingEndpointResponse422 | GetServicesDHCPServerStaticMappingEndpointResponse424 | GetServicesDHCPServerStaticMappingEndpointResponse500 | GetServicesDHCPServerStaticMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    GetServicesDHCPServerStaticMappingEndpointResponse400
    | GetServicesDHCPServerStaticMappingEndpointResponse401
    | GetServicesDHCPServerStaticMappingEndpointResponse403
    | GetServicesDHCPServerStaticMappingEndpointResponse404
    | GetServicesDHCPServerStaticMappingEndpointResponse405
    | GetServicesDHCPServerStaticMappingEndpointResponse406
    | GetServicesDHCPServerStaticMappingEndpointResponse409
    | GetServicesDHCPServerStaticMappingEndpointResponse415
    | GetServicesDHCPServerStaticMappingEndpointResponse422
    | GetServicesDHCPServerStaticMappingEndpointResponse424
    | GetServicesDHCPServerStaticMappingEndpointResponse500
    | GetServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDHCPServerStaticMappingEndpointResponse400 | GetServicesDHCPServerStaticMappingEndpointResponse401 | GetServicesDHCPServerStaticMappingEndpointResponse403 | GetServicesDHCPServerStaticMappingEndpointResponse404 | GetServicesDHCPServerStaticMappingEndpointResponse405 | GetServicesDHCPServerStaticMappingEndpointResponse406 | GetServicesDHCPServerStaticMappingEndpointResponse409 | GetServicesDHCPServerStaticMappingEndpointResponse415 | GetServicesDHCPServerStaticMappingEndpointResponse422 | GetServicesDHCPServerStaticMappingEndpointResponse424 | GetServicesDHCPServerStaticMappingEndpointResponse500 | GetServicesDHCPServerStaticMappingEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    GetServicesDHCPServerStaticMappingEndpointResponse400
    | GetServicesDHCPServerStaticMappingEndpointResponse401
    | GetServicesDHCPServerStaticMappingEndpointResponse403
    | GetServicesDHCPServerStaticMappingEndpointResponse404
    | GetServicesDHCPServerStaticMappingEndpointResponse405
    | GetServicesDHCPServerStaticMappingEndpointResponse406
    | GetServicesDHCPServerStaticMappingEndpointResponse409
    | GetServicesDHCPServerStaticMappingEndpointResponse415
    | GetServicesDHCPServerStaticMappingEndpointResponse422
    | GetServicesDHCPServerStaticMappingEndpointResponse424
    | GetServicesDHCPServerStaticMappingEndpointResponse500
    | GetServicesDHCPServerStaticMappingEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDHCPServerStaticMappingEndpointResponse400 | GetServicesDHCPServerStaticMappingEndpointResponse401 | GetServicesDHCPServerStaticMappingEndpointResponse403 | GetServicesDHCPServerStaticMappingEndpointResponse404 | GetServicesDHCPServerStaticMappingEndpointResponse405 | GetServicesDHCPServerStaticMappingEndpointResponse406 | GetServicesDHCPServerStaticMappingEndpointResponse409 | GetServicesDHCPServerStaticMappingEndpointResponse415 | GetServicesDHCPServerStaticMappingEndpointResponse422 | GetServicesDHCPServerStaticMappingEndpointResponse424 | GetServicesDHCPServerStaticMappingEndpointResponse500 | GetServicesDHCPServerStaticMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    GetServicesDHCPServerStaticMappingEndpointResponse400
    | GetServicesDHCPServerStaticMappingEndpointResponse401
    | GetServicesDHCPServerStaticMappingEndpointResponse403
    | GetServicesDHCPServerStaticMappingEndpointResponse404
    | GetServicesDHCPServerStaticMappingEndpointResponse405
    | GetServicesDHCPServerStaticMappingEndpointResponse406
    | GetServicesDHCPServerStaticMappingEndpointResponse409
    | GetServicesDHCPServerStaticMappingEndpointResponse415
    | GetServicesDHCPServerStaticMappingEndpointResponse422
    | GetServicesDHCPServerStaticMappingEndpointResponse424
    | GetServicesDHCPServerStaticMappingEndpointResponse500
    | GetServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDHCPServerStaticMappingEndpointResponse400 | GetServicesDHCPServerStaticMappingEndpointResponse401 | GetServicesDHCPServerStaticMappingEndpointResponse403 | GetServicesDHCPServerStaticMappingEndpointResponse404 | GetServicesDHCPServerStaticMappingEndpointResponse405 | GetServicesDHCPServerStaticMappingEndpointResponse406 | GetServicesDHCPServerStaticMappingEndpointResponse409 | GetServicesDHCPServerStaticMappingEndpointResponse415 | GetServicesDHCPServerStaticMappingEndpointResponse422 | GetServicesDHCPServerStaticMappingEndpointResponse424 | GetServicesDHCPServerStaticMappingEndpointResponse500 | GetServicesDHCPServerStaticMappingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
