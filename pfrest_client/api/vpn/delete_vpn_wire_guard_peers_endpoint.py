from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_vpn_wire_guard_peers_endpoint_query import DeleteVPNWireGuardPeersEndpointQuery
from ...models.delete_vpn_wire_guard_peers_endpoint_response_400 import DeleteVPNWireGuardPeersEndpointResponse400
from ...models.delete_vpn_wire_guard_peers_endpoint_response_401 import DeleteVPNWireGuardPeersEndpointResponse401
from ...models.delete_vpn_wire_guard_peers_endpoint_response_403 import DeleteVPNWireGuardPeersEndpointResponse403
from ...models.delete_vpn_wire_guard_peers_endpoint_response_404 import DeleteVPNWireGuardPeersEndpointResponse404
from ...models.delete_vpn_wire_guard_peers_endpoint_response_405 import DeleteVPNWireGuardPeersEndpointResponse405
from ...models.delete_vpn_wire_guard_peers_endpoint_response_406 import DeleteVPNWireGuardPeersEndpointResponse406
from ...models.delete_vpn_wire_guard_peers_endpoint_response_409 import DeleteVPNWireGuardPeersEndpointResponse409
from ...models.delete_vpn_wire_guard_peers_endpoint_response_415 import DeleteVPNWireGuardPeersEndpointResponse415
from ...models.delete_vpn_wire_guard_peers_endpoint_response_422 import DeleteVPNWireGuardPeersEndpointResponse422
from ...models.delete_vpn_wire_guard_peers_endpoint_response_424 import DeleteVPNWireGuardPeersEndpointResponse424
from ...models.delete_vpn_wire_guard_peers_endpoint_response_500 import DeleteVPNWireGuardPeersEndpointResponse500
from ...models.delete_vpn_wire_guard_peers_endpoint_response_503 import DeleteVPNWireGuardPeersEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteVPNWireGuardPeersEndpointQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/vpn/wireguard/peers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteVPNWireGuardPeersEndpointResponse400
    | DeleteVPNWireGuardPeersEndpointResponse401
    | DeleteVPNWireGuardPeersEndpointResponse403
    | DeleteVPNWireGuardPeersEndpointResponse404
    | DeleteVPNWireGuardPeersEndpointResponse405
    | DeleteVPNWireGuardPeersEndpointResponse406
    | DeleteVPNWireGuardPeersEndpointResponse409
    | DeleteVPNWireGuardPeersEndpointResponse415
    | DeleteVPNWireGuardPeersEndpointResponse422
    | DeleteVPNWireGuardPeersEndpointResponse424
    | DeleteVPNWireGuardPeersEndpointResponse500
    | DeleteVPNWireGuardPeersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteVPNWireGuardPeersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteVPNWireGuardPeersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteVPNWireGuardPeersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteVPNWireGuardPeersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteVPNWireGuardPeersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteVPNWireGuardPeersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteVPNWireGuardPeersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteVPNWireGuardPeersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteVPNWireGuardPeersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteVPNWireGuardPeersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteVPNWireGuardPeersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteVPNWireGuardPeersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteVPNWireGuardPeersEndpointResponse400
    | DeleteVPNWireGuardPeersEndpointResponse401
    | DeleteVPNWireGuardPeersEndpointResponse403
    | DeleteVPNWireGuardPeersEndpointResponse404
    | DeleteVPNWireGuardPeersEndpointResponse405
    | DeleteVPNWireGuardPeersEndpointResponse406
    | DeleteVPNWireGuardPeersEndpointResponse409
    | DeleteVPNWireGuardPeersEndpointResponse415
    | DeleteVPNWireGuardPeersEndpointResponse422
    | DeleteVPNWireGuardPeersEndpointResponse424
    | DeleteVPNWireGuardPeersEndpointResponse500
    | DeleteVPNWireGuardPeersEndpointResponse503
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
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteVPNWireGuardPeersEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteVPNWireGuardPeersEndpointResponse400
    | DeleteVPNWireGuardPeersEndpointResponse401
    | DeleteVPNWireGuardPeersEndpointResponse403
    | DeleteVPNWireGuardPeersEndpointResponse404
    | DeleteVPNWireGuardPeersEndpointResponse405
    | DeleteVPNWireGuardPeersEndpointResponse406
    | DeleteVPNWireGuardPeersEndpointResponse409
    | DeleteVPNWireGuardPeersEndpointResponse415
    | DeleteVPNWireGuardPeersEndpointResponse422
    | DeleteVPNWireGuardPeersEndpointResponse424
    | DeleteVPNWireGuardPeersEndpointResponse500
    | DeleteVPNWireGuardPeersEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing WireGuard Peers using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peers-delete ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteVPNWireGuardPeersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVPNWireGuardPeersEndpointResponse400 | DeleteVPNWireGuardPeersEndpointResponse401 | DeleteVPNWireGuardPeersEndpointResponse403 | DeleteVPNWireGuardPeersEndpointResponse404 | DeleteVPNWireGuardPeersEndpointResponse405 | DeleteVPNWireGuardPeersEndpointResponse406 | DeleteVPNWireGuardPeersEndpointResponse409 | DeleteVPNWireGuardPeersEndpointResponse415 | DeleteVPNWireGuardPeersEndpointResponse422 | DeleteVPNWireGuardPeersEndpointResponse424 | DeleteVPNWireGuardPeersEndpointResponse500 | DeleteVPNWireGuardPeersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteVPNWireGuardPeersEndpointQuery | Unset = UNSET,
) -> (
    DeleteVPNWireGuardPeersEndpointResponse400
    | DeleteVPNWireGuardPeersEndpointResponse401
    | DeleteVPNWireGuardPeersEndpointResponse403
    | DeleteVPNWireGuardPeersEndpointResponse404
    | DeleteVPNWireGuardPeersEndpointResponse405
    | DeleteVPNWireGuardPeersEndpointResponse406
    | DeleteVPNWireGuardPeersEndpointResponse409
    | DeleteVPNWireGuardPeersEndpointResponse415
    | DeleteVPNWireGuardPeersEndpointResponse422
    | DeleteVPNWireGuardPeersEndpointResponse424
    | DeleteVPNWireGuardPeersEndpointResponse500
    | DeleteVPNWireGuardPeersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing WireGuard Peers using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peers-delete ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteVPNWireGuardPeersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVPNWireGuardPeersEndpointResponse400 | DeleteVPNWireGuardPeersEndpointResponse401 | DeleteVPNWireGuardPeersEndpointResponse403 | DeleteVPNWireGuardPeersEndpointResponse404 | DeleteVPNWireGuardPeersEndpointResponse405 | DeleteVPNWireGuardPeersEndpointResponse406 | DeleteVPNWireGuardPeersEndpointResponse409 | DeleteVPNWireGuardPeersEndpointResponse415 | DeleteVPNWireGuardPeersEndpointResponse422 | DeleteVPNWireGuardPeersEndpointResponse424 | DeleteVPNWireGuardPeersEndpointResponse500 | DeleteVPNWireGuardPeersEndpointResponse503
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteVPNWireGuardPeersEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteVPNWireGuardPeersEndpointResponse400
    | DeleteVPNWireGuardPeersEndpointResponse401
    | DeleteVPNWireGuardPeersEndpointResponse403
    | DeleteVPNWireGuardPeersEndpointResponse404
    | DeleteVPNWireGuardPeersEndpointResponse405
    | DeleteVPNWireGuardPeersEndpointResponse406
    | DeleteVPNWireGuardPeersEndpointResponse409
    | DeleteVPNWireGuardPeersEndpointResponse415
    | DeleteVPNWireGuardPeersEndpointResponse422
    | DeleteVPNWireGuardPeersEndpointResponse424
    | DeleteVPNWireGuardPeersEndpointResponse500
    | DeleteVPNWireGuardPeersEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing WireGuard Peers using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peers-delete ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteVPNWireGuardPeersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVPNWireGuardPeersEndpointResponse400 | DeleteVPNWireGuardPeersEndpointResponse401 | DeleteVPNWireGuardPeersEndpointResponse403 | DeleteVPNWireGuardPeersEndpointResponse404 | DeleteVPNWireGuardPeersEndpointResponse405 | DeleteVPNWireGuardPeersEndpointResponse406 | DeleteVPNWireGuardPeersEndpointResponse409 | DeleteVPNWireGuardPeersEndpointResponse415 | DeleteVPNWireGuardPeersEndpointResponse422 | DeleteVPNWireGuardPeersEndpointResponse424 | DeleteVPNWireGuardPeersEndpointResponse500 | DeleteVPNWireGuardPeersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteVPNWireGuardPeersEndpointQuery | Unset = UNSET,
) -> (
    DeleteVPNWireGuardPeersEndpointResponse400
    | DeleteVPNWireGuardPeersEndpointResponse401
    | DeleteVPNWireGuardPeersEndpointResponse403
    | DeleteVPNWireGuardPeersEndpointResponse404
    | DeleteVPNWireGuardPeersEndpointResponse405
    | DeleteVPNWireGuardPeersEndpointResponse406
    | DeleteVPNWireGuardPeersEndpointResponse409
    | DeleteVPNWireGuardPeersEndpointResponse415
    | DeleteVPNWireGuardPeersEndpointResponse422
    | DeleteVPNWireGuardPeersEndpointResponse424
    | DeleteVPNWireGuardPeersEndpointResponse500
    | DeleteVPNWireGuardPeersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing WireGuard Peers using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: WireGuardPeer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-wireguard-peers-delete ]<br>**Required
    packages**: [ pfSense-pkg-WireGuard ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteVPNWireGuardPeersEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVPNWireGuardPeersEndpointResponse400 | DeleteVPNWireGuardPeersEndpointResponse401 | DeleteVPNWireGuardPeersEndpointResponse403 | DeleteVPNWireGuardPeersEndpointResponse404 | DeleteVPNWireGuardPeersEndpointResponse405 | DeleteVPNWireGuardPeersEndpointResponse406 | DeleteVPNWireGuardPeersEndpointResponse409 | DeleteVPNWireGuardPeersEndpointResponse415 | DeleteVPNWireGuardPeersEndpointResponse422 | DeleteVPNWireGuardPeersEndpointResponse424 | DeleteVPNWireGuardPeersEndpointResponse500 | DeleteVPNWireGuardPeersEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
