from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_status_open_vpn_server_connection_endpoint_response_400 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse400,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_401 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse401,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_403 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse403,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_404 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse404,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_405 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse405,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_406 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse406,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_409 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse409,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_415 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse415,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_422 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse422,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_424 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse424,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_500 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse500,
)
from ...models.delete_status_open_vpn_server_connection_endpoint_response_503 import (
    DeleteStatusOpenVPNServerConnectionEndpointResponse503,
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
        "method": "delete",
        "url": "/api/v2/status/openvpn/server/connection",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteStatusOpenVPNServerConnectionEndpointResponse400
    | DeleteStatusOpenVPNServerConnectionEndpointResponse401
    | DeleteStatusOpenVPNServerConnectionEndpointResponse403
    | DeleteStatusOpenVPNServerConnectionEndpointResponse404
    | DeleteStatusOpenVPNServerConnectionEndpointResponse405
    | DeleteStatusOpenVPNServerConnectionEndpointResponse406
    | DeleteStatusOpenVPNServerConnectionEndpointResponse409
    | DeleteStatusOpenVPNServerConnectionEndpointResponse415
    | DeleteStatusOpenVPNServerConnectionEndpointResponse422
    | DeleteStatusOpenVPNServerConnectionEndpointResponse424
    | DeleteStatusOpenVPNServerConnectionEndpointResponse500
    | DeleteStatusOpenVPNServerConnectionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteStatusOpenVPNServerConnectionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteStatusOpenVPNServerConnectionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteStatusOpenVPNServerConnectionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteStatusOpenVPNServerConnectionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteStatusOpenVPNServerConnectionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteStatusOpenVPNServerConnectionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteStatusOpenVPNServerConnectionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteStatusOpenVPNServerConnectionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteStatusOpenVPNServerConnectionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteStatusOpenVPNServerConnectionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteStatusOpenVPNServerConnectionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteStatusOpenVPNServerConnectionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteStatusOpenVPNServerConnectionEndpointResponse400
    | DeleteStatusOpenVPNServerConnectionEndpointResponse401
    | DeleteStatusOpenVPNServerConnectionEndpointResponse403
    | DeleteStatusOpenVPNServerConnectionEndpointResponse404
    | DeleteStatusOpenVPNServerConnectionEndpointResponse405
    | DeleteStatusOpenVPNServerConnectionEndpointResponse406
    | DeleteStatusOpenVPNServerConnectionEndpointResponse409
    | DeleteStatusOpenVPNServerConnectionEndpointResponse415
    | DeleteStatusOpenVPNServerConnectionEndpointResponse422
    | DeleteStatusOpenVPNServerConnectionEndpointResponse424
    | DeleteStatusOpenVPNServerConnectionEndpointResponse500
    | DeleteStatusOpenVPNServerConnectionEndpointResponse503
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
    DeleteStatusOpenVPNServerConnectionEndpointResponse400
    | DeleteStatusOpenVPNServerConnectionEndpointResponse401
    | DeleteStatusOpenVPNServerConnectionEndpointResponse403
    | DeleteStatusOpenVPNServerConnectionEndpointResponse404
    | DeleteStatusOpenVPNServerConnectionEndpointResponse405
    | DeleteStatusOpenVPNServerConnectionEndpointResponse406
    | DeleteStatusOpenVPNServerConnectionEndpointResponse409
    | DeleteStatusOpenVPNServerConnectionEndpointResponse415
    | DeleteStatusOpenVPNServerConnectionEndpointResponse422
    | DeleteStatusOpenVPNServerConnectionEndpointResponse424
    | DeleteStatusOpenVPNServerConnectionEndpointResponse500
    | DeleteStatusOpenVPNServerConnectionEndpointResponse503
]:
    """<h3>Description:</h3>Kills an existing OpenVPN Server Connection<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNServerConnectionStatus<br>**Parent model**:
    OpenVPNServerStatus<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-status-openvpn-server-
    connection-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteStatusOpenVPNServerConnectionEndpointResponse400 | DeleteStatusOpenVPNServerConnectionEndpointResponse401 | DeleteStatusOpenVPNServerConnectionEndpointResponse403 | DeleteStatusOpenVPNServerConnectionEndpointResponse404 | DeleteStatusOpenVPNServerConnectionEndpointResponse405 | DeleteStatusOpenVPNServerConnectionEndpointResponse406 | DeleteStatusOpenVPNServerConnectionEndpointResponse409 | DeleteStatusOpenVPNServerConnectionEndpointResponse415 | DeleteStatusOpenVPNServerConnectionEndpointResponse422 | DeleteStatusOpenVPNServerConnectionEndpointResponse424 | DeleteStatusOpenVPNServerConnectionEndpointResponse500 | DeleteStatusOpenVPNServerConnectionEndpointResponse503]
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
    DeleteStatusOpenVPNServerConnectionEndpointResponse400
    | DeleteStatusOpenVPNServerConnectionEndpointResponse401
    | DeleteStatusOpenVPNServerConnectionEndpointResponse403
    | DeleteStatusOpenVPNServerConnectionEndpointResponse404
    | DeleteStatusOpenVPNServerConnectionEndpointResponse405
    | DeleteStatusOpenVPNServerConnectionEndpointResponse406
    | DeleteStatusOpenVPNServerConnectionEndpointResponse409
    | DeleteStatusOpenVPNServerConnectionEndpointResponse415
    | DeleteStatusOpenVPNServerConnectionEndpointResponse422
    | DeleteStatusOpenVPNServerConnectionEndpointResponse424
    | DeleteStatusOpenVPNServerConnectionEndpointResponse500
    | DeleteStatusOpenVPNServerConnectionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Kills an existing OpenVPN Server Connection<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNServerConnectionStatus<br>**Parent model**:
    OpenVPNServerStatus<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-status-openvpn-server-
    connection-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteStatusOpenVPNServerConnectionEndpointResponse400 | DeleteStatusOpenVPNServerConnectionEndpointResponse401 | DeleteStatusOpenVPNServerConnectionEndpointResponse403 | DeleteStatusOpenVPNServerConnectionEndpointResponse404 | DeleteStatusOpenVPNServerConnectionEndpointResponse405 | DeleteStatusOpenVPNServerConnectionEndpointResponse406 | DeleteStatusOpenVPNServerConnectionEndpointResponse409 | DeleteStatusOpenVPNServerConnectionEndpointResponse415 | DeleteStatusOpenVPNServerConnectionEndpointResponse422 | DeleteStatusOpenVPNServerConnectionEndpointResponse424 | DeleteStatusOpenVPNServerConnectionEndpointResponse500 | DeleteStatusOpenVPNServerConnectionEndpointResponse503
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
    DeleteStatusOpenVPNServerConnectionEndpointResponse400
    | DeleteStatusOpenVPNServerConnectionEndpointResponse401
    | DeleteStatusOpenVPNServerConnectionEndpointResponse403
    | DeleteStatusOpenVPNServerConnectionEndpointResponse404
    | DeleteStatusOpenVPNServerConnectionEndpointResponse405
    | DeleteStatusOpenVPNServerConnectionEndpointResponse406
    | DeleteStatusOpenVPNServerConnectionEndpointResponse409
    | DeleteStatusOpenVPNServerConnectionEndpointResponse415
    | DeleteStatusOpenVPNServerConnectionEndpointResponse422
    | DeleteStatusOpenVPNServerConnectionEndpointResponse424
    | DeleteStatusOpenVPNServerConnectionEndpointResponse500
    | DeleteStatusOpenVPNServerConnectionEndpointResponse503
]:
    """<h3>Description:</h3>Kills an existing OpenVPN Server Connection<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNServerConnectionStatus<br>**Parent model**:
    OpenVPNServerStatus<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-status-openvpn-server-
    connection-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteStatusOpenVPNServerConnectionEndpointResponse400 | DeleteStatusOpenVPNServerConnectionEndpointResponse401 | DeleteStatusOpenVPNServerConnectionEndpointResponse403 | DeleteStatusOpenVPNServerConnectionEndpointResponse404 | DeleteStatusOpenVPNServerConnectionEndpointResponse405 | DeleteStatusOpenVPNServerConnectionEndpointResponse406 | DeleteStatusOpenVPNServerConnectionEndpointResponse409 | DeleteStatusOpenVPNServerConnectionEndpointResponse415 | DeleteStatusOpenVPNServerConnectionEndpointResponse422 | DeleteStatusOpenVPNServerConnectionEndpointResponse424 | DeleteStatusOpenVPNServerConnectionEndpointResponse500 | DeleteStatusOpenVPNServerConnectionEndpointResponse503]
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
    DeleteStatusOpenVPNServerConnectionEndpointResponse400
    | DeleteStatusOpenVPNServerConnectionEndpointResponse401
    | DeleteStatusOpenVPNServerConnectionEndpointResponse403
    | DeleteStatusOpenVPNServerConnectionEndpointResponse404
    | DeleteStatusOpenVPNServerConnectionEndpointResponse405
    | DeleteStatusOpenVPNServerConnectionEndpointResponse406
    | DeleteStatusOpenVPNServerConnectionEndpointResponse409
    | DeleteStatusOpenVPNServerConnectionEndpointResponse415
    | DeleteStatusOpenVPNServerConnectionEndpointResponse422
    | DeleteStatusOpenVPNServerConnectionEndpointResponse424
    | DeleteStatusOpenVPNServerConnectionEndpointResponse500
    | DeleteStatusOpenVPNServerConnectionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Kills an existing OpenVPN Server Connection<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNServerConnectionStatus<br>**Parent model**:
    OpenVPNServerStatus<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-status-openvpn-server-
    connection-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteStatusOpenVPNServerConnectionEndpointResponse400 | DeleteStatusOpenVPNServerConnectionEndpointResponse401 | DeleteStatusOpenVPNServerConnectionEndpointResponse403 | DeleteStatusOpenVPNServerConnectionEndpointResponse404 | DeleteStatusOpenVPNServerConnectionEndpointResponse405 | DeleteStatusOpenVPNServerConnectionEndpointResponse406 | DeleteStatusOpenVPNServerConnectionEndpointResponse409 | DeleteStatusOpenVPNServerConnectionEndpointResponse415 | DeleteStatusOpenVPNServerConnectionEndpointResponse422 | DeleteStatusOpenVPNServerConnectionEndpointResponse424 | DeleteStatusOpenVPNServerConnectionEndpointResponse500 | DeleteStatusOpenVPNServerConnectionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
