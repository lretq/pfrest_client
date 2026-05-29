from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_400 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse400,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_401 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse401,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_403 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse403,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_404 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse404,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_405 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse405,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_406 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse406,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_409 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse409,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_415 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse415,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_422 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse422,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_424 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse424,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_500 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse500,
)
from ...models.delete_services_dhcp_server_static_mapping_endpoint_response_503 import (
    DeleteServicesDHCPServerStaticMappingEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params["apply"] = apply

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/dhcp_server/static_mapping",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesDHCPServerStaticMappingEndpointResponse400
    | DeleteServicesDHCPServerStaticMappingEndpointResponse401
    | DeleteServicesDHCPServerStaticMappingEndpointResponse403
    | DeleteServicesDHCPServerStaticMappingEndpointResponse404
    | DeleteServicesDHCPServerStaticMappingEndpointResponse405
    | DeleteServicesDHCPServerStaticMappingEndpointResponse406
    | DeleteServicesDHCPServerStaticMappingEndpointResponse409
    | DeleteServicesDHCPServerStaticMappingEndpointResponse415
    | DeleteServicesDHCPServerStaticMappingEndpointResponse422
    | DeleteServicesDHCPServerStaticMappingEndpointResponse424
    | DeleteServicesDHCPServerStaticMappingEndpointResponse500
    | DeleteServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesDHCPServerStaticMappingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesDHCPServerStaticMappingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesDHCPServerStaticMappingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesDHCPServerStaticMappingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesDHCPServerStaticMappingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesDHCPServerStaticMappingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesDHCPServerStaticMappingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesDHCPServerStaticMappingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesDHCPServerStaticMappingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesDHCPServerStaticMappingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesDHCPServerStaticMappingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesDHCPServerStaticMappingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesDHCPServerStaticMappingEndpointResponse400
    | DeleteServicesDHCPServerStaticMappingEndpointResponse401
    | DeleteServicesDHCPServerStaticMappingEndpointResponse403
    | DeleteServicesDHCPServerStaticMappingEndpointResponse404
    | DeleteServicesDHCPServerStaticMappingEndpointResponse405
    | DeleteServicesDHCPServerStaticMappingEndpointResponse406
    | DeleteServicesDHCPServerStaticMappingEndpointResponse409
    | DeleteServicesDHCPServerStaticMappingEndpointResponse415
    | DeleteServicesDHCPServerStaticMappingEndpointResponse422
    | DeleteServicesDHCPServerStaticMappingEndpointResponse424
    | DeleteServicesDHCPServerStaticMappingEndpointResponse500
    | DeleteServicesDHCPServerStaticMappingEndpointResponse503
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
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDHCPServerStaticMappingEndpointResponse400
    | DeleteServicesDHCPServerStaticMappingEndpointResponse401
    | DeleteServicesDHCPServerStaticMappingEndpointResponse403
    | DeleteServicesDHCPServerStaticMappingEndpointResponse404
    | DeleteServicesDHCPServerStaticMappingEndpointResponse405
    | DeleteServicesDHCPServerStaticMappingEndpointResponse406
    | DeleteServicesDHCPServerStaticMappingEndpointResponse409
    | DeleteServicesDHCPServerStaticMappingEndpointResponse415
    | DeleteServicesDHCPServerStaticMappingEndpointResponse422
    | DeleteServicesDHCPServerStaticMappingEndpointResponse424
    | DeleteServicesDHCPServerStaticMappingEndpointResponse500
    | DeleteServicesDHCPServerStaticMappingEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDHCPServerStaticMappingEndpointResponse400 | DeleteServicesDHCPServerStaticMappingEndpointResponse401 | DeleteServicesDHCPServerStaticMappingEndpointResponse403 | DeleteServicesDHCPServerStaticMappingEndpointResponse404 | DeleteServicesDHCPServerStaticMappingEndpointResponse405 | DeleteServicesDHCPServerStaticMappingEndpointResponse406 | DeleteServicesDHCPServerStaticMappingEndpointResponse409 | DeleteServicesDHCPServerStaticMappingEndpointResponse415 | DeleteServicesDHCPServerStaticMappingEndpointResponse422 | DeleteServicesDHCPServerStaticMappingEndpointResponse424 | DeleteServicesDHCPServerStaticMappingEndpointResponse500 | DeleteServicesDHCPServerStaticMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
        apply=apply,
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
    apply: bool | Unset = False,
) -> (
    DeleteServicesDHCPServerStaticMappingEndpointResponse400
    | DeleteServicesDHCPServerStaticMappingEndpointResponse401
    | DeleteServicesDHCPServerStaticMappingEndpointResponse403
    | DeleteServicesDHCPServerStaticMappingEndpointResponse404
    | DeleteServicesDHCPServerStaticMappingEndpointResponse405
    | DeleteServicesDHCPServerStaticMappingEndpointResponse406
    | DeleteServicesDHCPServerStaticMappingEndpointResponse409
    | DeleteServicesDHCPServerStaticMappingEndpointResponse415
    | DeleteServicesDHCPServerStaticMappingEndpointResponse422
    | DeleteServicesDHCPServerStaticMappingEndpointResponse424
    | DeleteServicesDHCPServerStaticMappingEndpointResponse500
    | DeleteServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDHCPServerStaticMappingEndpointResponse400 | DeleteServicesDHCPServerStaticMappingEndpointResponse401 | DeleteServicesDHCPServerStaticMappingEndpointResponse403 | DeleteServicesDHCPServerStaticMappingEndpointResponse404 | DeleteServicesDHCPServerStaticMappingEndpointResponse405 | DeleteServicesDHCPServerStaticMappingEndpointResponse406 | DeleteServicesDHCPServerStaticMappingEndpointResponse409 | DeleteServicesDHCPServerStaticMappingEndpointResponse415 | DeleteServicesDHCPServerStaticMappingEndpointResponse422 | DeleteServicesDHCPServerStaticMappingEndpointResponse424 | DeleteServicesDHCPServerStaticMappingEndpointResponse500 | DeleteServicesDHCPServerStaticMappingEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
        apply=apply,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDHCPServerStaticMappingEndpointResponse400
    | DeleteServicesDHCPServerStaticMappingEndpointResponse401
    | DeleteServicesDHCPServerStaticMappingEndpointResponse403
    | DeleteServicesDHCPServerStaticMappingEndpointResponse404
    | DeleteServicesDHCPServerStaticMappingEndpointResponse405
    | DeleteServicesDHCPServerStaticMappingEndpointResponse406
    | DeleteServicesDHCPServerStaticMappingEndpointResponse409
    | DeleteServicesDHCPServerStaticMappingEndpointResponse415
    | DeleteServicesDHCPServerStaticMappingEndpointResponse422
    | DeleteServicesDHCPServerStaticMappingEndpointResponse424
    | DeleteServicesDHCPServerStaticMappingEndpointResponse500
    | DeleteServicesDHCPServerStaticMappingEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDHCPServerStaticMappingEndpointResponse400 | DeleteServicesDHCPServerStaticMappingEndpointResponse401 | DeleteServicesDHCPServerStaticMappingEndpointResponse403 | DeleteServicesDHCPServerStaticMappingEndpointResponse404 | DeleteServicesDHCPServerStaticMappingEndpointResponse405 | DeleteServicesDHCPServerStaticMappingEndpointResponse406 | DeleteServicesDHCPServerStaticMappingEndpointResponse409 | DeleteServicesDHCPServerStaticMappingEndpointResponse415 | DeleteServicesDHCPServerStaticMappingEndpointResponse422 | DeleteServicesDHCPServerStaticMappingEndpointResponse424 | DeleteServicesDHCPServerStaticMappingEndpointResponse500 | DeleteServicesDHCPServerStaticMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
        apply=apply,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDHCPServerStaticMappingEndpointResponse400
    | DeleteServicesDHCPServerStaticMappingEndpointResponse401
    | DeleteServicesDHCPServerStaticMappingEndpointResponse403
    | DeleteServicesDHCPServerStaticMappingEndpointResponse404
    | DeleteServicesDHCPServerStaticMappingEndpointResponse405
    | DeleteServicesDHCPServerStaticMappingEndpointResponse406
    | DeleteServicesDHCPServerStaticMappingEndpointResponse409
    | DeleteServicesDHCPServerStaticMappingEndpointResponse415
    | DeleteServicesDHCPServerStaticMappingEndpointResponse422
    | DeleteServicesDHCPServerStaticMappingEndpointResponse424
    | DeleteServicesDHCPServerStaticMappingEndpointResponse500
    | DeleteServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDHCPServerStaticMappingEndpointResponse400 | DeleteServicesDHCPServerStaticMappingEndpointResponse401 | DeleteServicesDHCPServerStaticMappingEndpointResponse403 | DeleteServicesDHCPServerStaticMappingEndpointResponse404 | DeleteServicesDHCPServerStaticMappingEndpointResponse405 | DeleteServicesDHCPServerStaticMappingEndpointResponse406 | DeleteServicesDHCPServerStaticMappingEndpointResponse409 | DeleteServicesDHCPServerStaticMappingEndpointResponse415 | DeleteServicesDHCPServerStaticMappingEndpointResponse422 | DeleteServicesDHCPServerStaticMappingEndpointResponse424 | DeleteServicesDHCPServerStaticMappingEndpointResponse500 | DeleteServicesDHCPServerStaticMappingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
            apply=apply,
        )
    ).parsed
