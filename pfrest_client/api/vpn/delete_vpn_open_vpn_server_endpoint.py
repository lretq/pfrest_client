from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_vpn_open_vpn_server_endpoint_response_400 import DeleteVPNOpenVPNServerEndpointResponse400
from ...models.delete_vpn_open_vpn_server_endpoint_response_401 import DeleteVPNOpenVPNServerEndpointResponse401
from ...models.delete_vpn_open_vpn_server_endpoint_response_403 import DeleteVPNOpenVPNServerEndpointResponse403
from ...models.delete_vpn_open_vpn_server_endpoint_response_404 import DeleteVPNOpenVPNServerEndpointResponse404
from ...models.delete_vpn_open_vpn_server_endpoint_response_405 import DeleteVPNOpenVPNServerEndpointResponse405
from ...models.delete_vpn_open_vpn_server_endpoint_response_406 import DeleteVPNOpenVPNServerEndpointResponse406
from ...models.delete_vpn_open_vpn_server_endpoint_response_409 import DeleteVPNOpenVPNServerEndpointResponse409
from ...models.delete_vpn_open_vpn_server_endpoint_response_415 import DeleteVPNOpenVPNServerEndpointResponse415
from ...models.delete_vpn_open_vpn_server_endpoint_response_422 import DeleteVPNOpenVPNServerEndpointResponse422
from ...models.delete_vpn_open_vpn_server_endpoint_response_424 import DeleteVPNOpenVPNServerEndpointResponse424
from ...models.delete_vpn_open_vpn_server_endpoint_response_500 import DeleteVPNOpenVPNServerEndpointResponse500
from ...models.delete_vpn_open_vpn_server_endpoint_response_503 import DeleteVPNOpenVPNServerEndpointResponse503
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
        "method": "delete",
        "url": "/api/v2/vpn/openvpn/server",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteVPNOpenVPNServerEndpointResponse400
    | DeleteVPNOpenVPNServerEndpointResponse401
    | DeleteVPNOpenVPNServerEndpointResponse403
    | DeleteVPNOpenVPNServerEndpointResponse404
    | DeleteVPNOpenVPNServerEndpointResponse405
    | DeleteVPNOpenVPNServerEndpointResponse406
    | DeleteVPNOpenVPNServerEndpointResponse409
    | DeleteVPNOpenVPNServerEndpointResponse415
    | DeleteVPNOpenVPNServerEndpointResponse422
    | DeleteVPNOpenVPNServerEndpointResponse424
    | DeleteVPNOpenVPNServerEndpointResponse500
    | DeleteVPNOpenVPNServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteVPNOpenVPNServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteVPNOpenVPNServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteVPNOpenVPNServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteVPNOpenVPNServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteVPNOpenVPNServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteVPNOpenVPNServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteVPNOpenVPNServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteVPNOpenVPNServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteVPNOpenVPNServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteVPNOpenVPNServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteVPNOpenVPNServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteVPNOpenVPNServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteVPNOpenVPNServerEndpointResponse400
    | DeleteVPNOpenVPNServerEndpointResponse401
    | DeleteVPNOpenVPNServerEndpointResponse403
    | DeleteVPNOpenVPNServerEndpointResponse404
    | DeleteVPNOpenVPNServerEndpointResponse405
    | DeleteVPNOpenVPNServerEndpointResponse406
    | DeleteVPNOpenVPNServerEndpointResponse409
    | DeleteVPNOpenVPNServerEndpointResponse415
    | DeleteVPNOpenVPNServerEndpointResponse422
    | DeleteVPNOpenVPNServerEndpointResponse424
    | DeleteVPNOpenVPNServerEndpointResponse500
    | DeleteVPNOpenVPNServerEndpointResponse503
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
    DeleteVPNOpenVPNServerEndpointResponse400
    | DeleteVPNOpenVPNServerEndpointResponse401
    | DeleteVPNOpenVPNServerEndpointResponse403
    | DeleteVPNOpenVPNServerEndpointResponse404
    | DeleteVPNOpenVPNServerEndpointResponse405
    | DeleteVPNOpenVPNServerEndpointResponse406
    | DeleteVPNOpenVPNServerEndpointResponse409
    | DeleteVPNOpenVPNServerEndpointResponse415
    | DeleteVPNOpenVPNServerEndpointResponse422
    | DeleteVPNOpenVPNServerEndpointResponse424
    | DeleteVPNOpenVPNServerEndpointResponse500
    | DeleteVPNOpenVPNServerEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVPNOpenVPNServerEndpointResponse400 | DeleteVPNOpenVPNServerEndpointResponse401 | DeleteVPNOpenVPNServerEndpointResponse403 | DeleteVPNOpenVPNServerEndpointResponse404 | DeleteVPNOpenVPNServerEndpointResponse405 | DeleteVPNOpenVPNServerEndpointResponse406 | DeleteVPNOpenVPNServerEndpointResponse409 | DeleteVPNOpenVPNServerEndpointResponse415 | DeleteVPNOpenVPNServerEndpointResponse422 | DeleteVPNOpenVPNServerEndpointResponse424 | DeleteVPNOpenVPNServerEndpointResponse500 | DeleteVPNOpenVPNServerEndpointResponse503]
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
    DeleteVPNOpenVPNServerEndpointResponse400
    | DeleteVPNOpenVPNServerEndpointResponse401
    | DeleteVPNOpenVPNServerEndpointResponse403
    | DeleteVPNOpenVPNServerEndpointResponse404
    | DeleteVPNOpenVPNServerEndpointResponse405
    | DeleteVPNOpenVPNServerEndpointResponse406
    | DeleteVPNOpenVPNServerEndpointResponse409
    | DeleteVPNOpenVPNServerEndpointResponse415
    | DeleteVPNOpenVPNServerEndpointResponse422
    | DeleteVPNOpenVPNServerEndpointResponse424
    | DeleteVPNOpenVPNServerEndpointResponse500
    | DeleteVPNOpenVPNServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVPNOpenVPNServerEndpointResponse400 | DeleteVPNOpenVPNServerEndpointResponse401 | DeleteVPNOpenVPNServerEndpointResponse403 | DeleteVPNOpenVPNServerEndpointResponse404 | DeleteVPNOpenVPNServerEndpointResponse405 | DeleteVPNOpenVPNServerEndpointResponse406 | DeleteVPNOpenVPNServerEndpointResponse409 | DeleteVPNOpenVPNServerEndpointResponse415 | DeleteVPNOpenVPNServerEndpointResponse422 | DeleteVPNOpenVPNServerEndpointResponse424 | DeleteVPNOpenVPNServerEndpointResponse500 | DeleteVPNOpenVPNServerEndpointResponse503
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
    DeleteVPNOpenVPNServerEndpointResponse400
    | DeleteVPNOpenVPNServerEndpointResponse401
    | DeleteVPNOpenVPNServerEndpointResponse403
    | DeleteVPNOpenVPNServerEndpointResponse404
    | DeleteVPNOpenVPNServerEndpointResponse405
    | DeleteVPNOpenVPNServerEndpointResponse406
    | DeleteVPNOpenVPNServerEndpointResponse409
    | DeleteVPNOpenVPNServerEndpointResponse415
    | DeleteVPNOpenVPNServerEndpointResponse422
    | DeleteVPNOpenVPNServerEndpointResponse424
    | DeleteVPNOpenVPNServerEndpointResponse500
    | DeleteVPNOpenVPNServerEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVPNOpenVPNServerEndpointResponse400 | DeleteVPNOpenVPNServerEndpointResponse401 | DeleteVPNOpenVPNServerEndpointResponse403 | DeleteVPNOpenVPNServerEndpointResponse404 | DeleteVPNOpenVPNServerEndpointResponse405 | DeleteVPNOpenVPNServerEndpointResponse406 | DeleteVPNOpenVPNServerEndpointResponse409 | DeleteVPNOpenVPNServerEndpointResponse415 | DeleteVPNOpenVPNServerEndpointResponse422 | DeleteVPNOpenVPNServerEndpointResponse424 | DeleteVPNOpenVPNServerEndpointResponse500 | DeleteVPNOpenVPNServerEndpointResponse503]
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
    DeleteVPNOpenVPNServerEndpointResponse400
    | DeleteVPNOpenVPNServerEndpointResponse401
    | DeleteVPNOpenVPNServerEndpointResponse403
    | DeleteVPNOpenVPNServerEndpointResponse404
    | DeleteVPNOpenVPNServerEndpointResponse405
    | DeleteVPNOpenVPNServerEndpointResponse406
    | DeleteVPNOpenVPNServerEndpointResponse409
    | DeleteVPNOpenVPNServerEndpointResponse415
    | DeleteVPNOpenVPNServerEndpointResponse422
    | DeleteVPNOpenVPNServerEndpointResponse424
    | DeleteVPNOpenVPNServerEndpointResponse500
    | DeleteVPNOpenVPNServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVPNOpenVPNServerEndpointResponse400 | DeleteVPNOpenVPNServerEndpointResponse401 | DeleteVPNOpenVPNServerEndpointResponse403 | DeleteVPNOpenVPNServerEndpointResponse404 | DeleteVPNOpenVPNServerEndpointResponse405 | DeleteVPNOpenVPNServerEndpointResponse406 | DeleteVPNOpenVPNServerEndpointResponse409 | DeleteVPNOpenVPNServerEndpointResponse415 | DeleteVPNOpenVPNServerEndpointResponse422 | DeleteVPNOpenVPNServerEndpointResponse424 | DeleteVPNOpenVPNServerEndpointResponse500 | DeleteVPNOpenVPNServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
