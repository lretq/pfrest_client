from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_vpn_wire_guard_peers_endpoint_data_body_item import PutVPNWireGuardPeersEndpointDataBodyItem
from ...models.put_vpn_wire_guard_peers_endpoint_json_body_item import PutVPNWireGuardPeersEndpointJsonBodyItem
from ...models.put_vpn_wire_guard_peers_endpoint_response_400 import PutVPNWireGuardPeersEndpointResponse400
from ...models.put_vpn_wire_guard_peers_endpoint_response_401 import PutVPNWireGuardPeersEndpointResponse401
from ...models.put_vpn_wire_guard_peers_endpoint_response_403 import PutVPNWireGuardPeersEndpointResponse403
from ...models.put_vpn_wire_guard_peers_endpoint_response_404 import PutVPNWireGuardPeersEndpointResponse404
from ...models.put_vpn_wire_guard_peers_endpoint_response_405 import PutVPNWireGuardPeersEndpointResponse405
from ...models.put_vpn_wire_guard_peers_endpoint_response_406 import PutVPNWireGuardPeersEndpointResponse406
from ...models.put_vpn_wire_guard_peers_endpoint_response_409 import PutVPNWireGuardPeersEndpointResponse409
from ...models.put_vpn_wire_guard_peers_endpoint_response_415 import PutVPNWireGuardPeersEndpointResponse415
from ...models.put_vpn_wire_guard_peers_endpoint_response_422 import PutVPNWireGuardPeersEndpointResponse422
from ...models.put_vpn_wire_guard_peers_endpoint_response_424 import PutVPNWireGuardPeersEndpointResponse424
from ...models.put_vpn_wire_guard_peers_endpoint_response_500 import PutVPNWireGuardPeersEndpointResponse500
from ...models.put_vpn_wire_guard_peers_endpoint_response_503 import PutVPNWireGuardPeersEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutVPNWireGuardPeersEndpointJsonBodyItem]
    | list[PutVPNWireGuardPeersEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/vpn/wireguard/peers",
    }

    if isinstance(body, list[PutVPNWireGuardPeersEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutVPNWireGuardPeersEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutVPNWireGuardPeersEndpointResponse400
    | PutVPNWireGuardPeersEndpointResponse401
    | PutVPNWireGuardPeersEndpointResponse403
    | PutVPNWireGuardPeersEndpointResponse404
    | PutVPNWireGuardPeersEndpointResponse405
    | PutVPNWireGuardPeersEndpointResponse406
    | PutVPNWireGuardPeersEndpointResponse409
    | PutVPNWireGuardPeersEndpointResponse415
    | PutVPNWireGuardPeersEndpointResponse422
    | PutVPNWireGuardPeersEndpointResponse424
    | PutVPNWireGuardPeersEndpointResponse500
    | PutVPNWireGuardPeersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutVPNWireGuardPeersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutVPNWireGuardPeersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutVPNWireGuardPeersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutVPNWireGuardPeersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutVPNWireGuardPeersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutVPNWireGuardPeersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutVPNWireGuardPeersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutVPNWireGuardPeersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutVPNWireGuardPeersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutVPNWireGuardPeersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutVPNWireGuardPeersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutVPNWireGuardPeersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutVPNWireGuardPeersEndpointResponse400
    | PutVPNWireGuardPeersEndpointResponse401
    | PutVPNWireGuardPeersEndpointResponse403
    | PutVPNWireGuardPeersEndpointResponse404
    | PutVPNWireGuardPeersEndpointResponse405
    | PutVPNWireGuardPeersEndpointResponse406
    | PutVPNWireGuardPeersEndpointResponse409
    | PutVPNWireGuardPeersEndpointResponse415
    | PutVPNWireGuardPeersEndpointResponse422
    | PutVPNWireGuardPeersEndpointResponse424
    | PutVPNWireGuardPeersEndpointResponse500
    | PutVPNWireGuardPeersEndpointResponse503
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
    body: list[PutVPNWireGuardPeersEndpointJsonBodyItem]
    | list[PutVPNWireGuardPeersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutVPNWireGuardPeersEndpointResponse400
    | PutVPNWireGuardPeersEndpointResponse401
    | PutVPNWireGuardPeersEndpointResponse403
    | PutVPNWireGuardPeersEndpointResponse404
    | PutVPNWireGuardPeersEndpointResponse405
    | PutVPNWireGuardPeersEndpointResponse406
    | PutVPNWireGuardPeersEndpointResponse409
    | PutVPNWireGuardPeersEndpointResponse415
    | PutVPNWireGuardPeersEndpointResponse422
    | PutVPNWireGuardPeersEndpointResponse424
    | PutVPNWireGuardPeersEndpointResponse500
    | PutVPNWireGuardPeersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing WireGuard Peers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peers-put ]<br>**Required packages**:
    [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNWireGuardPeersEndpointJsonBodyItem] | Unset):
        body (list[PutVPNWireGuardPeersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutVPNWireGuardPeersEndpointResponse400 | PutVPNWireGuardPeersEndpointResponse401 | PutVPNWireGuardPeersEndpointResponse403 | PutVPNWireGuardPeersEndpointResponse404 | PutVPNWireGuardPeersEndpointResponse405 | PutVPNWireGuardPeersEndpointResponse406 | PutVPNWireGuardPeersEndpointResponse409 | PutVPNWireGuardPeersEndpointResponse415 | PutVPNWireGuardPeersEndpointResponse422 | PutVPNWireGuardPeersEndpointResponse424 | PutVPNWireGuardPeersEndpointResponse500 | PutVPNWireGuardPeersEndpointResponse503]
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
    body: list[PutVPNWireGuardPeersEndpointJsonBodyItem]
    | list[PutVPNWireGuardPeersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutVPNWireGuardPeersEndpointResponse400
    | PutVPNWireGuardPeersEndpointResponse401
    | PutVPNWireGuardPeersEndpointResponse403
    | PutVPNWireGuardPeersEndpointResponse404
    | PutVPNWireGuardPeersEndpointResponse405
    | PutVPNWireGuardPeersEndpointResponse406
    | PutVPNWireGuardPeersEndpointResponse409
    | PutVPNWireGuardPeersEndpointResponse415
    | PutVPNWireGuardPeersEndpointResponse422
    | PutVPNWireGuardPeersEndpointResponse424
    | PutVPNWireGuardPeersEndpointResponse500
    | PutVPNWireGuardPeersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing WireGuard Peers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peers-put ]<br>**Required packages**:
    [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNWireGuardPeersEndpointJsonBodyItem] | Unset):
        body (list[PutVPNWireGuardPeersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutVPNWireGuardPeersEndpointResponse400 | PutVPNWireGuardPeersEndpointResponse401 | PutVPNWireGuardPeersEndpointResponse403 | PutVPNWireGuardPeersEndpointResponse404 | PutVPNWireGuardPeersEndpointResponse405 | PutVPNWireGuardPeersEndpointResponse406 | PutVPNWireGuardPeersEndpointResponse409 | PutVPNWireGuardPeersEndpointResponse415 | PutVPNWireGuardPeersEndpointResponse422 | PutVPNWireGuardPeersEndpointResponse424 | PutVPNWireGuardPeersEndpointResponse500 | PutVPNWireGuardPeersEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNWireGuardPeersEndpointJsonBodyItem]
    | list[PutVPNWireGuardPeersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutVPNWireGuardPeersEndpointResponse400
    | PutVPNWireGuardPeersEndpointResponse401
    | PutVPNWireGuardPeersEndpointResponse403
    | PutVPNWireGuardPeersEndpointResponse404
    | PutVPNWireGuardPeersEndpointResponse405
    | PutVPNWireGuardPeersEndpointResponse406
    | PutVPNWireGuardPeersEndpointResponse409
    | PutVPNWireGuardPeersEndpointResponse415
    | PutVPNWireGuardPeersEndpointResponse422
    | PutVPNWireGuardPeersEndpointResponse424
    | PutVPNWireGuardPeersEndpointResponse500
    | PutVPNWireGuardPeersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing WireGuard Peers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peers-put ]<br>**Required packages**:
    [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNWireGuardPeersEndpointJsonBodyItem] | Unset):
        body (list[PutVPNWireGuardPeersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutVPNWireGuardPeersEndpointResponse400 | PutVPNWireGuardPeersEndpointResponse401 | PutVPNWireGuardPeersEndpointResponse403 | PutVPNWireGuardPeersEndpointResponse404 | PutVPNWireGuardPeersEndpointResponse405 | PutVPNWireGuardPeersEndpointResponse406 | PutVPNWireGuardPeersEndpointResponse409 | PutVPNWireGuardPeersEndpointResponse415 | PutVPNWireGuardPeersEndpointResponse422 | PutVPNWireGuardPeersEndpointResponse424 | PutVPNWireGuardPeersEndpointResponse500 | PutVPNWireGuardPeersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutVPNWireGuardPeersEndpointJsonBodyItem]
    | list[PutVPNWireGuardPeersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutVPNWireGuardPeersEndpointResponse400
    | PutVPNWireGuardPeersEndpointResponse401
    | PutVPNWireGuardPeersEndpointResponse403
    | PutVPNWireGuardPeersEndpointResponse404
    | PutVPNWireGuardPeersEndpointResponse405
    | PutVPNWireGuardPeersEndpointResponse406
    | PutVPNWireGuardPeersEndpointResponse409
    | PutVPNWireGuardPeersEndpointResponse415
    | PutVPNWireGuardPeersEndpointResponse422
    | PutVPNWireGuardPeersEndpointResponse424
    | PutVPNWireGuardPeersEndpointResponse500
    | PutVPNWireGuardPeersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing WireGuard Peers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peers-put ]<br>**Required packages**:
    [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutVPNWireGuardPeersEndpointJsonBodyItem] | Unset):
        body (list[PutVPNWireGuardPeersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutVPNWireGuardPeersEndpointResponse400 | PutVPNWireGuardPeersEndpointResponse401 | PutVPNWireGuardPeersEndpointResponse403 | PutVPNWireGuardPeersEndpointResponse404 | PutVPNWireGuardPeersEndpointResponse405 | PutVPNWireGuardPeersEndpointResponse406 | PutVPNWireGuardPeersEndpointResponse409 | PutVPNWireGuardPeersEndpointResponse415 | PutVPNWireGuardPeersEndpointResponse422 | PutVPNWireGuardPeersEndpointResponse424 | PutVPNWireGuardPeersEndpointResponse500 | PutVPNWireGuardPeersEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
