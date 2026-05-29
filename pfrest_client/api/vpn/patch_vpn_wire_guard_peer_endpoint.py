from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_vpn_wire_guard_peer_endpoint_data_body import PatchVPNWireGuardPeerEndpointDataBody
from ...models.patch_vpn_wire_guard_peer_endpoint_json_body import PatchVPNWireGuardPeerEndpointJsonBody
from ...models.patch_vpn_wire_guard_peer_endpoint_response_400 import PatchVPNWireGuardPeerEndpointResponse400
from ...models.patch_vpn_wire_guard_peer_endpoint_response_401 import PatchVPNWireGuardPeerEndpointResponse401
from ...models.patch_vpn_wire_guard_peer_endpoint_response_403 import PatchVPNWireGuardPeerEndpointResponse403
from ...models.patch_vpn_wire_guard_peer_endpoint_response_404 import PatchVPNWireGuardPeerEndpointResponse404
from ...models.patch_vpn_wire_guard_peer_endpoint_response_405 import PatchVPNWireGuardPeerEndpointResponse405
from ...models.patch_vpn_wire_guard_peer_endpoint_response_406 import PatchVPNWireGuardPeerEndpointResponse406
from ...models.patch_vpn_wire_guard_peer_endpoint_response_409 import PatchVPNWireGuardPeerEndpointResponse409
from ...models.patch_vpn_wire_guard_peer_endpoint_response_415 import PatchVPNWireGuardPeerEndpointResponse415
from ...models.patch_vpn_wire_guard_peer_endpoint_response_422 import PatchVPNWireGuardPeerEndpointResponse422
from ...models.patch_vpn_wire_guard_peer_endpoint_response_424 import PatchVPNWireGuardPeerEndpointResponse424
from ...models.patch_vpn_wire_guard_peer_endpoint_response_500 import PatchVPNWireGuardPeerEndpointResponse500
from ...models.patch_vpn_wire_guard_peer_endpoint_response_503 import PatchVPNWireGuardPeerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchVPNWireGuardPeerEndpointJsonBody | PatchVPNWireGuardPeerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/vpn/wireguard/peer",
    }

    if isinstance(body, PatchVPNWireGuardPeerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchVPNWireGuardPeerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchVPNWireGuardPeerEndpointResponse400
    | PatchVPNWireGuardPeerEndpointResponse401
    | PatchVPNWireGuardPeerEndpointResponse403
    | PatchVPNWireGuardPeerEndpointResponse404
    | PatchVPNWireGuardPeerEndpointResponse405
    | PatchVPNWireGuardPeerEndpointResponse406
    | PatchVPNWireGuardPeerEndpointResponse409
    | PatchVPNWireGuardPeerEndpointResponse415
    | PatchVPNWireGuardPeerEndpointResponse422
    | PatchVPNWireGuardPeerEndpointResponse424
    | PatchVPNWireGuardPeerEndpointResponse500
    | PatchVPNWireGuardPeerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchVPNWireGuardPeerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchVPNWireGuardPeerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchVPNWireGuardPeerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchVPNWireGuardPeerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchVPNWireGuardPeerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchVPNWireGuardPeerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchVPNWireGuardPeerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchVPNWireGuardPeerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchVPNWireGuardPeerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchVPNWireGuardPeerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchVPNWireGuardPeerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchVPNWireGuardPeerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchVPNWireGuardPeerEndpointResponse400
    | PatchVPNWireGuardPeerEndpointResponse401
    | PatchVPNWireGuardPeerEndpointResponse403
    | PatchVPNWireGuardPeerEndpointResponse404
    | PatchVPNWireGuardPeerEndpointResponse405
    | PatchVPNWireGuardPeerEndpointResponse406
    | PatchVPNWireGuardPeerEndpointResponse409
    | PatchVPNWireGuardPeerEndpointResponse415
    | PatchVPNWireGuardPeerEndpointResponse422
    | PatchVPNWireGuardPeerEndpointResponse424
    | PatchVPNWireGuardPeerEndpointResponse500
    | PatchVPNWireGuardPeerEndpointResponse503
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
    body: PatchVPNWireGuardPeerEndpointJsonBody | PatchVPNWireGuardPeerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNWireGuardPeerEndpointResponse400
    | PatchVPNWireGuardPeerEndpointResponse401
    | PatchVPNWireGuardPeerEndpointResponse403
    | PatchVPNWireGuardPeerEndpointResponse404
    | PatchVPNWireGuardPeerEndpointResponse405
    | PatchVPNWireGuardPeerEndpointResponse406
    | PatchVPNWireGuardPeerEndpointResponse409
    | PatchVPNWireGuardPeerEndpointResponse415
    | PatchVPNWireGuardPeerEndpointResponse422
    | PatchVPNWireGuardPeerEndpointResponse424
    | PatchVPNWireGuardPeerEndpointResponse500
    | PatchVPNWireGuardPeerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing WireGuard Peer.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peer-patch ]<br>**Required packages**:
    [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardPeerEndpointJsonBody | Unset):
        body (PatchVPNWireGuardPeerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNWireGuardPeerEndpointResponse400 | PatchVPNWireGuardPeerEndpointResponse401 | PatchVPNWireGuardPeerEndpointResponse403 | PatchVPNWireGuardPeerEndpointResponse404 | PatchVPNWireGuardPeerEndpointResponse405 | PatchVPNWireGuardPeerEndpointResponse406 | PatchVPNWireGuardPeerEndpointResponse409 | PatchVPNWireGuardPeerEndpointResponse415 | PatchVPNWireGuardPeerEndpointResponse422 | PatchVPNWireGuardPeerEndpointResponse424 | PatchVPNWireGuardPeerEndpointResponse500 | PatchVPNWireGuardPeerEndpointResponse503]
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
    body: PatchVPNWireGuardPeerEndpointJsonBody | PatchVPNWireGuardPeerEndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNWireGuardPeerEndpointResponse400
    | PatchVPNWireGuardPeerEndpointResponse401
    | PatchVPNWireGuardPeerEndpointResponse403
    | PatchVPNWireGuardPeerEndpointResponse404
    | PatchVPNWireGuardPeerEndpointResponse405
    | PatchVPNWireGuardPeerEndpointResponse406
    | PatchVPNWireGuardPeerEndpointResponse409
    | PatchVPNWireGuardPeerEndpointResponse415
    | PatchVPNWireGuardPeerEndpointResponse422
    | PatchVPNWireGuardPeerEndpointResponse424
    | PatchVPNWireGuardPeerEndpointResponse500
    | PatchVPNWireGuardPeerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing WireGuard Peer.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peer-patch ]<br>**Required packages**:
    [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardPeerEndpointJsonBody | Unset):
        body (PatchVPNWireGuardPeerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNWireGuardPeerEndpointResponse400 | PatchVPNWireGuardPeerEndpointResponse401 | PatchVPNWireGuardPeerEndpointResponse403 | PatchVPNWireGuardPeerEndpointResponse404 | PatchVPNWireGuardPeerEndpointResponse405 | PatchVPNWireGuardPeerEndpointResponse406 | PatchVPNWireGuardPeerEndpointResponse409 | PatchVPNWireGuardPeerEndpointResponse415 | PatchVPNWireGuardPeerEndpointResponse422 | PatchVPNWireGuardPeerEndpointResponse424 | PatchVPNWireGuardPeerEndpointResponse500 | PatchVPNWireGuardPeerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNWireGuardPeerEndpointJsonBody | PatchVPNWireGuardPeerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNWireGuardPeerEndpointResponse400
    | PatchVPNWireGuardPeerEndpointResponse401
    | PatchVPNWireGuardPeerEndpointResponse403
    | PatchVPNWireGuardPeerEndpointResponse404
    | PatchVPNWireGuardPeerEndpointResponse405
    | PatchVPNWireGuardPeerEndpointResponse406
    | PatchVPNWireGuardPeerEndpointResponse409
    | PatchVPNWireGuardPeerEndpointResponse415
    | PatchVPNWireGuardPeerEndpointResponse422
    | PatchVPNWireGuardPeerEndpointResponse424
    | PatchVPNWireGuardPeerEndpointResponse500
    | PatchVPNWireGuardPeerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing WireGuard Peer.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peer-patch ]<br>**Required packages**:
    [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardPeerEndpointJsonBody | Unset):
        body (PatchVPNWireGuardPeerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNWireGuardPeerEndpointResponse400 | PatchVPNWireGuardPeerEndpointResponse401 | PatchVPNWireGuardPeerEndpointResponse403 | PatchVPNWireGuardPeerEndpointResponse404 | PatchVPNWireGuardPeerEndpointResponse405 | PatchVPNWireGuardPeerEndpointResponse406 | PatchVPNWireGuardPeerEndpointResponse409 | PatchVPNWireGuardPeerEndpointResponse415 | PatchVPNWireGuardPeerEndpointResponse422 | PatchVPNWireGuardPeerEndpointResponse424 | PatchVPNWireGuardPeerEndpointResponse500 | PatchVPNWireGuardPeerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNWireGuardPeerEndpointJsonBody | PatchVPNWireGuardPeerEndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNWireGuardPeerEndpointResponse400
    | PatchVPNWireGuardPeerEndpointResponse401
    | PatchVPNWireGuardPeerEndpointResponse403
    | PatchVPNWireGuardPeerEndpointResponse404
    | PatchVPNWireGuardPeerEndpointResponse405
    | PatchVPNWireGuardPeerEndpointResponse406
    | PatchVPNWireGuardPeerEndpointResponse409
    | PatchVPNWireGuardPeerEndpointResponse415
    | PatchVPNWireGuardPeerEndpointResponse422
    | PatchVPNWireGuardPeerEndpointResponse424
    | PatchVPNWireGuardPeerEndpointResponse500
    | PatchVPNWireGuardPeerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing WireGuard Peer.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peer-patch ]<br>**Required packages**:
    [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchVPNWireGuardPeerEndpointJsonBody | Unset):
        body (PatchVPNWireGuardPeerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNWireGuardPeerEndpointResponse400 | PatchVPNWireGuardPeerEndpointResponse401 | PatchVPNWireGuardPeerEndpointResponse403 | PatchVPNWireGuardPeerEndpointResponse404 | PatchVPNWireGuardPeerEndpointResponse405 | PatchVPNWireGuardPeerEndpointResponse406 | PatchVPNWireGuardPeerEndpointResponse409 | PatchVPNWireGuardPeerEndpointResponse415 | PatchVPNWireGuardPeerEndpointResponse422 | PatchVPNWireGuardPeerEndpointResponse424 | PatchVPNWireGuardPeerEndpointResponse500 | PatchVPNWireGuardPeerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
