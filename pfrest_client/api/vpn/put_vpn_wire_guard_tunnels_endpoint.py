from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_vpn_wire_guard_tunnels_endpoint_data_body_item import PutVPNWireGuardTunnelsEndpointDataBodyItem
from ...models.put_vpn_wire_guard_tunnels_endpoint_json_body_item import PutVPNWireGuardTunnelsEndpointJsonBodyItem
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_400 import PutVPNWireGuardTunnelsEndpointResponse400
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_401 import PutVPNWireGuardTunnelsEndpointResponse401
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_403 import PutVPNWireGuardTunnelsEndpointResponse403
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_404 import PutVPNWireGuardTunnelsEndpointResponse404
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_405 import PutVPNWireGuardTunnelsEndpointResponse405
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_406 import PutVPNWireGuardTunnelsEndpointResponse406
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_409 import PutVPNWireGuardTunnelsEndpointResponse409
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_415 import PutVPNWireGuardTunnelsEndpointResponse415
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_422 import PutVPNWireGuardTunnelsEndpointResponse422
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_424 import PutVPNWireGuardTunnelsEndpointResponse424
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_500 import PutVPNWireGuardTunnelsEndpointResponse500
from ...models.put_vpn_wire_guard_tunnels_endpoint_response_503 import PutVPNWireGuardTunnelsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutVPNWireGuardTunnelsEndpointJsonBodyItem]
    | list[PutVPNWireGuardTunnelsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/vpn/wireguard/tunnels",
    }

    if isinstance(body, list[PutVPNWireGuardTunnelsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutVPNWireGuardTunnelsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutVPNWireGuardTunnelsEndpointResponse400
    | PutVPNWireGuardTunnelsEndpointResponse401
    | PutVPNWireGuardTunnelsEndpointResponse403
    | PutVPNWireGuardTunnelsEndpointResponse404
    | PutVPNWireGuardTunnelsEndpointResponse405
    | PutVPNWireGuardTunnelsEndpointResponse406
    | PutVPNWireGuardTunnelsEndpointResponse409
    | PutVPNWireGuardTunnelsEndpointResponse415
    | PutVPNWireGuardTunnelsEndpointResponse422
    | PutVPNWireGuardTunnelsEndpointResponse424
    | PutVPNWireGuardTunnelsEndpointResponse500
    | PutVPNWireGuardTunnelsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutVPNWireGuardTunnelsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutVPNWireGuardTunnelsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutVPNWireGuardTunnelsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutVPNWireGuardTunnelsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutVPNWireGuardTunnelsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutVPNWireGuardTunnelsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutVPNWireGuardTunnelsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutVPNWireGuardTunnelsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutVPNWireGuardTunnelsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutVPNWireGuardTunnelsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutVPNWireGuardTunnelsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutVPNWireGuardTunnelsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutVPNWireGuardTunnelsEndpointResponse400
    | PutVPNWireGuardTunnelsEndpointResponse401
    | PutVPNWireGuardTunnelsEndpointResponse403
    | PutVPNWireGuardTunnelsEndpointResponse404
    | PutVPNWireGuardTunnelsEndpointResponse405
    | PutVPNWireGuardTunnelsEndpointResponse406
    | PutVPNWireGuardTunnelsEndpointResponse409
    | PutVPNWireGuardTunnelsEndpointResponse415
    | PutVPNWireGuardTunnelsEndpointResponse422
    | PutVPNWireGuardTunnelsEndpointResponse424
    | PutVPNWireGuardTunnelsEndpointResponse500
    | PutVPNWireGuardTunnelsEndpointResponse503
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
    body: list[PutVPNWireGuardTunnelsEndpointJsonBodyItem]
    | list[PutVPNWireGuardTunnelsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutVPNWireGuardTunnelsEndpointResponse400
    | PutVPNWireGuardTunnelsEndpointResponse401
    | PutVPNWireGuardTunnelsEndpointResponse403
    | PutVPNWireGuardTunnelsEndpointResponse404
    | PutVPNWireGuardTunnelsEndpointResponse405
    | PutVPNWireGuardTunnelsEndpointResponse406
    | PutVPNWireGuardTunnelsEndpointResponse409
    | PutVPNWireGuardTunnelsEndpointResponse415
    | PutVPNWireGuardTunnelsEndpointResponse422
    | PutVPNWireGuardTunnelsEndpointResponse424
    | PutVPNWireGuardTunnelsEndpointResponse500
    | PutVPNWireGuardTunnelsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing WireGuard Tunnels.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: WireGuardTunnel<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnels-put ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNWireGuardTunnelsEndpointJsonBodyItem] | Unset):
        body (list[PutVPNWireGuardTunnelsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutVPNWireGuardTunnelsEndpointResponse400 | PutVPNWireGuardTunnelsEndpointResponse401 | PutVPNWireGuardTunnelsEndpointResponse403 | PutVPNWireGuardTunnelsEndpointResponse404 | PutVPNWireGuardTunnelsEndpointResponse405 | PutVPNWireGuardTunnelsEndpointResponse406 | PutVPNWireGuardTunnelsEndpointResponse409 | PutVPNWireGuardTunnelsEndpointResponse415 | PutVPNWireGuardTunnelsEndpointResponse422 | PutVPNWireGuardTunnelsEndpointResponse424 | PutVPNWireGuardTunnelsEndpointResponse500 | PutVPNWireGuardTunnelsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNWireGuardTunnelsEndpointJsonBodyItem]
    | list[PutVPNWireGuardTunnelsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutVPNWireGuardTunnelsEndpointResponse400
    | PutVPNWireGuardTunnelsEndpointResponse401
    | PutVPNWireGuardTunnelsEndpointResponse403
    | PutVPNWireGuardTunnelsEndpointResponse404
    | PutVPNWireGuardTunnelsEndpointResponse405
    | PutVPNWireGuardTunnelsEndpointResponse406
    | PutVPNWireGuardTunnelsEndpointResponse409
    | PutVPNWireGuardTunnelsEndpointResponse415
    | PutVPNWireGuardTunnelsEndpointResponse422
    | PutVPNWireGuardTunnelsEndpointResponse424
    | PutVPNWireGuardTunnelsEndpointResponse500
    | PutVPNWireGuardTunnelsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing WireGuard Tunnels.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: WireGuardTunnel<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnels-put ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNWireGuardTunnelsEndpointJsonBodyItem] | Unset):
        body (list[PutVPNWireGuardTunnelsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutVPNWireGuardTunnelsEndpointResponse400 | PutVPNWireGuardTunnelsEndpointResponse401 | PutVPNWireGuardTunnelsEndpointResponse403 | PutVPNWireGuardTunnelsEndpointResponse404 | PutVPNWireGuardTunnelsEndpointResponse405 | PutVPNWireGuardTunnelsEndpointResponse406 | PutVPNWireGuardTunnelsEndpointResponse409 | PutVPNWireGuardTunnelsEndpointResponse415 | PutVPNWireGuardTunnelsEndpointResponse422 | PutVPNWireGuardTunnelsEndpointResponse424 | PutVPNWireGuardTunnelsEndpointResponse500 | PutVPNWireGuardTunnelsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNWireGuardTunnelsEndpointJsonBodyItem]
    | list[PutVPNWireGuardTunnelsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutVPNWireGuardTunnelsEndpointResponse400
    | PutVPNWireGuardTunnelsEndpointResponse401
    | PutVPNWireGuardTunnelsEndpointResponse403
    | PutVPNWireGuardTunnelsEndpointResponse404
    | PutVPNWireGuardTunnelsEndpointResponse405
    | PutVPNWireGuardTunnelsEndpointResponse406
    | PutVPNWireGuardTunnelsEndpointResponse409
    | PutVPNWireGuardTunnelsEndpointResponse415
    | PutVPNWireGuardTunnelsEndpointResponse422
    | PutVPNWireGuardTunnelsEndpointResponse424
    | PutVPNWireGuardTunnelsEndpointResponse500
    | PutVPNWireGuardTunnelsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing WireGuard Tunnels.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: WireGuardTunnel<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnels-put ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNWireGuardTunnelsEndpointJsonBodyItem] | Unset):
        body (list[PutVPNWireGuardTunnelsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutVPNWireGuardTunnelsEndpointResponse400 | PutVPNWireGuardTunnelsEndpointResponse401 | PutVPNWireGuardTunnelsEndpointResponse403 | PutVPNWireGuardTunnelsEndpointResponse404 | PutVPNWireGuardTunnelsEndpointResponse405 | PutVPNWireGuardTunnelsEndpointResponse406 | PutVPNWireGuardTunnelsEndpointResponse409 | PutVPNWireGuardTunnelsEndpointResponse415 | PutVPNWireGuardTunnelsEndpointResponse422 | PutVPNWireGuardTunnelsEndpointResponse424 | PutVPNWireGuardTunnelsEndpointResponse500 | PutVPNWireGuardTunnelsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNWireGuardTunnelsEndpointJsonBodyItem]
    | list[PutVPNWireGuardTunnelsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutVPNWireGuardTunnelsEndpointResponse400
    | PutVPNWireGuardTunnelsEndpointResponse401
    | PutVPNWireGuardTunnelsEndpointResponse403
    | PutVPNWireGuardTunnelsEndpointResponse404
    | PutVPNWireGuardTunnelsEndpointResponse405
    | PutVPNWireGuardTunnelsEndpointResponse406
    | PutVPNWireGuardTunnelsEndpointResponse409
    | PutVPNWireGuardTunnelsEndpointResponse415
    | PutVPNWireGuardTunnelsEndpointResponse422
    | PutVPNWireGuardTunnelsEndpointResponse424
    | PutVPNWireGuardTunnelsEndpointResponse500
    | PutVPNWireGuardTunnelsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing WireGuard Tunnels.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: WireGuardTunnel<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-tunnels-put ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNWireGuardTunnelsEndpointJsonBodyItem] | Unset):
        body (list[PutVPNWireGuardTunnelsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutVPNWireGuardTunnelsEndpointResponse400 | PutVPNWireGuardTunnelsEndpointResponse401 | PutVPNWireGuardTunnelsEndpointResponse403 | PutVPNWireGuardTunnelsEndpointResponse404 | PutVPNWireGuardTunnelsEndpointResponse405 | PutVPNWireGuardTunnelsEndpointResponse406 | PutVPNWireGuardTunnelsEndpointResponse409 | PutVPNWireGuardTunnelsEndpointResponse415 | PutVPNWireGuardTunnelsEndpointResponse422 | PutVPNWireGuardTunnelsEndpointResponse424 | PutVPNWireGuardTunnelsEndpointResponse500 | PutVPNWireGuardTunnelsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
