from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_400 import (
    GetVPNWireGuardTunnelAddressEndpointResponse400,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_401 import (
    GetVPNWireGuardTunnelAddressEndpointResponse401,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_403 import (
    GetVPNWireGuardTunnelAddressEndpointResponse403,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_404 import (
    GetVPNWireGuardTunnelAddressEndpointResponse404,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_405 import (
    GetVPNWireGuardTunnelAddressEndpointResponse405,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_406 import (
    GetVPNWireGuardTunnelAddressEndpointResponse406,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_409 import (
    GetVPNWireGuardTunnelAddressEndpointResponse409,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_415 import (
    GetVPNWireGuardTunnelAddressEndpointResponse415,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_422 import (
    GetVPNWireGuardTunnelAddressEndpointResponse422,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_424 import (
    GetVPNWireGuardTunnelAddressEndpointResponse424,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_500 import (
    GetVPNWireGuardTunnelAddressEndpointResponse500,
)
from ...models.get_vpn_wire_guard_tunnel_address_endpoint_response_503 import (
    GetVPNWireGuardTunnelAddressEndpointResponse503,
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
        "url": "/api/v2/vpn/wireguard/tunnel/address",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVPNWireGuardTunnelAddressEndpointResponse400
    | GetVPNWireGuardTunnelAddressEndpointResponse401
    | GetVPNWireGuardTunnelAddressEndpointResponse403
    | GetVPNWireGuardTunnelAddressEndpointResponse404
    | GetVPNWireGuardTunnelAddressEndpointResponse405
    | GetVPNWireGuardTunnelAddressEndpointResponse406
    | GetVPNWireGuardTunnelAddressEndpointResponse409
    | GetVPNWireGuardTunnelAddressEndpointResponse415
    | GetVPNWireGuardTunnelAddressEndpointResponse422
    | GetVPNWireGuardTunnelAddressEndpointResponse424
    | GetVPNWireGuardTunnelAddressEndpointResponse500
    | GetVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetVPNWireGuardTunnelAddressEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetVPNWireGuardTunnelAddressEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVPNWireGuardTunnelAddressEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVPNWireGuardTunnelAddressEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetVPNWireGuardTunnelAddressEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetVPNWireGuardTunnelAddressEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetVPNWireGuardTunnelAddressEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetVPNWireGuardTunnelAddressEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetVPNWireGuardTunnelAddressEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetVPNWireGuardTunnelAddressEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetVPNWireGuardTunnelAddressEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetVPNWireGuardTunnelAddressEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVPNWireGuardTunnelAddressEndpointResponse400
    | GetVPNWireGuardTunnelAddressEndpointResponse401
    | GetVPNWireGuardTunnelAddressEndpointResponse403
    | GetVPNWireGuardTunnelAddressEndpointResponse404
    | GetVPNWireGuardTunnelAddressEndpointResponse405
    | GetVPNWireGuardTunnelAddressEndpointResponse406
    | GetVPNWireGuardTunnelAddressEndpointResponse409
    | GetVPNWireGuardTunnelAddressEndpointResponse415
    | GetVPNWireGuardTunnelAddressEndpointResponse422
    | GetVPNWireGuardTunnelAddressEndpointResponse424
    | GetVPNWireGuardTunnelAddressEndpointResponse500
    | GetVPNWireGuardTunnelAddressEndpointResponse503
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
    GetVPNWireGuardTunnelAddressEndpointResponse400
    | GetVPNWireGuardTunnelAddressEndpointResponse401
    | GetVPNWireGuardTunnelAddressEndpointResponse403
    | GetVPNWireGuardTunnelAddressEndpointResponse404
    | GetVPNWireGuardTunnelAddressEndpointResponse405
    | GetVPNWireGuardTunnelAddressEndpointResponse406
    | GetVPNWireGuardTunnelAddressEndpointResponse409
    | GetVPNWireGuardTunnelAddressEndpointResponse415
    | GetVPNWireGuardTunnelAddressEndpointResponse422
    | GetVPNWireGuardTunnelAddressEndpointResponse424
    | GetVPNWireGuardTunnelAddressEndpointResponse500
    | GetVPNWireGuardTunnelAddressEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-get ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNWireGuardTunnelAddressEndpointResponse400 | GetVPNWireGuardTunnelAddressEndpointResponse401 | GetVPNWireGuardTunnelAddressEndpointResponse403 | GetVPNWireGuardTunnelAddressEndpointResponse404 | GetVPNWireGuardTunnelAddressEndpointResponse405 | GetVPNWireGuardTunnelAddressEndpointResponse406 | GetVPNWireGuardTunnelAddressEndpointResponse409 | GetVPNWireGuardTunnelAddressEndpointResponse415 | GetVPNWireGuardTunnelAddressEndpointResponse422 | GetVPNWireGuardTunnelAddressEndpointResponse424 | GetVPNWireGuardTunnelAddressEndpointResponse500 | GetVPNWireGuardTunnelAddressEndpointResponse503]
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
    GetVPNWireGuardTunnelAddressEndpointResponse400
    | GetVPNWireGuardTunnelAddressEndpointResponse401
    | GetVPNWireGuardTunnelAddressEndpointResponse403
    | GetVPNWireGuardTunnelAddressEndpointResponse404
    | GetVPNWireGuardTunnelAddressEndpointResponse405
    | GetVPNWireGuardTunnelAddressEndpointResponse406
    | GetVPNWireGuardTunnelAddressEndpointResponse409
    | GetVPNWireGuardTunnelAddressEndpointResponse415
    | GetVPNWireGuardTunnelAddressEndpointResponse422
    | GetVPNWireGuardTunnelAddressEndpointResponse424
    | GetVPNWireGuardTunnelAddressEndpointResponse500
    | GetVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-get ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNWireGuardTunnelAddressEndpointResponse400 | GetVPNWireGuardTunnelAddressEndpointResponse401 | GetVPNWireGuardTunnelAddressEndpointResponse403 | GetVPNWireGuardTunnelAddressEndpointResponse404 | GetVPNWireGuardTunnelAddressEndpointResponse405 | GetVPNWireGuardTunnelAddressEndpointResponse406 | GetVPNWireGuardTunnelAddressEndpointResponse409 | GetVPNWireGuardTunnelAddressEndpointResponse415 | GetVPNWireGuardTunnelAddressEndpointResponse422 | GetVPNWireGuardTunnelAddressEndpointResponse424 | GetVPNWireGuardTunnelAddressEndpointResponse500 | GetVPNWireGuardTunnelAddressEndpointResponse503
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
    GetVPNWireGuardTunnelAddressEndpointResponse400
    | GetVPNWireGuardTunnelAddressEndpointResponse401
    | GetVPNWireGuardTunnelAddressEndpointResponse403
    | GetVPNWireGuardTunnelAddressEndpointResponse404
    | GetVPNWireGuardTunnelAddressEndpointResponse405
    | GetVPNWireGuardTunnelAddressEndpointResponse406
    | GetVPNWireGuardTunnelAddressEndpointResponse409
    | GetVPNWireGuardTunnelAddressEndpointResponse415
    | GetVPNWireGuardTunnelAddressEndpointResponse422
    | GetVPNWireGuardTunnelAddressEndpointResponse424
    | GetVPNWireGuardTunnelAddressEndpointResponse500
    | GetVPNWireGuardTunnelAddressEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-get ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNWireGuardTunnelAddressEndpointResponse400 | GetVPNWireGuardTunnelAddressEndpointResponse401 | GetVPNWireGuardTunnelAddressEndpointResponse403 | GetVPNWireGuardTunnelAddressEndpointResponse404 | GetVPNWireGuardTunnelAddressEndpointResponse405 | GetVPNWireGuardTunnelAddressEndpointResponse406 | GetVPNWireGuardTunnelAddressEndpointResponse409 | GetVPNWireGuardTunnelAddressEndpointResponse415 | GetVPNWireGuardTunnelAddressEndpointResponse422 | GetVPNWireGuardTunnelAddressEndpointResponse424 | GetVPNWireGuardTunnelAddressEndpointResponse500 | GetVPNWireGuardTunnelAddressEndpointResponse503]
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
    GetVPNWireGuardTunnelAddressEndpointResponse400
    | GetVPNWireGuardTunnelAddressEndpointResponse401
    | GetVPNWireGuardTunnelAddressEndpointResponse403
    | GetVPNWireGuardTunnelAddressEndpointResponse404
    | GetVPNWireGuardTunnelAddressEndpointResponse405
    | GetVPNWireGuardTunnelAddressEndpointResponse406
    | GetVPNWireGuardTunnelAddressEndpointResponse409
    | GetVPNWireGuardTunnelAddressEndpointResponse415
    | GetVPNWireGuardTunnelAddressEndpointResponse422
    | GetVPNWireGuardTunnelAddressEndpointResponse424
    | GetVPNWireGuardTunnelAddressEndpointResponse500
    | GetVPNWireGuardTunnelAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing WireGuard Tunnel Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: WireGuardTunnelAddress<br>**Parent model**:
    WireGuardTunnel<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnel-
    address-get ]<br>**Required packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNWireGuardTunnelAddressEndpointResponse400 | GetVPNWireGuardTunnelAddressEndpointResponse401 | GetVPNWireGuardTunnelAddressEndpointResponse403 | GetVPNWireGuardTunnelAddressEndpointResponse404 | GetVPNWireGuardTunnelAddressEndpointResponse405 | GetVPNWireGuardTunnelAddressEndpointResponse406 | GetVPNWireGuardTunnelAddressEndpointResponse409 | GetVPNWireGuardTunnelAddressEndpointResponse415 | GetVPNWireGuardTunnelAddressEndpointResponse422 | GetVPNWireGuardTunnelAddressEndpointResponse424 | GetVPNWireGuardTunnelAddressEndpointResponse500 | GetVPNWireGuardTunnelAddressEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
