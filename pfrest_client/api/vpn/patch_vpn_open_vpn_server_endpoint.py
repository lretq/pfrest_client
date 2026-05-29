from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_vpn_open_vpn_server_endpoint_data_body import PatchVPNOpenVPNServerEndpointDataBody
from ...models.patch_vpn_open_vpn_server_endpoint_json_body import PatchVPNOpenVPNServerEndpointJsonBody
from ...models.patch_vpn_open_vpn_server_endpoint_response_400 import PatchVPNOpenVPNServerEndpointResponse400
from ...models.patch_vpn_open_vpn_server_endpoint_response_401 import PatchVPNOpenVPNServerEndpointResponse401
from ...models.patch_vpn_open_vpn_server_endpoint_response_403 import PatchVPNOpenVPNServerEndpointResponse403
from ...models.patch_vpn_open_vpn_server_endpoint_response_404 import PatchVPNOpenVPNServerEndpointResponse404
from ...models.patch_vpn_open_vpn_server_endpoint_response_405 import PatchVPNOpenVPNServerEndpointResponse405
from ...models.patch_vpn_open_vpn_server_endpoint_response_406 import PatchVPNOpenVPNServerEndpointResponse406
from ...models.patch_vpn_open_vpn_server_endpoint_response_409 import PatchVPNOpenVPNServerEndpointResponse409
from ...models.patch_vpn_open_vpn_server_endpoint_response_415 import PatchVPNOpenVPNServerEndpointResponse415
from ...models.patch_vpn_open_vpn_server_endpoint_response_422 import PatchVPNOpenVPNServerEndpointResponse422
from ...models.patch_vpn_open_vpn_server_endpoint_response_424 import PatchVPNOpenVPNServerEndpointResponse424
from ...models.patch_vpn_open_vpn_server_endpoint_response_500 import PatchVPNOpenVPNServerEndpointResponse500
from ...models.patch_vpn_open_vpn_server_endpoint_response_503 import PatchVPNOpenVPNServerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchVPNOpenVPNServerEndpointJsonBody | PatchVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/vpn/openvpn/server",
    }

    if isinstance(body, PatchVPNOpenVPNServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchVPNOpenVPNServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchVPNOpenVPNServerEndpointResponse400
    | PatchVPNOpenVPNServerEndpointResponse401
    | PatchVPNOpenVPNServerEndpointResponse403
    | PatchVPNOpenVPNServerEndpointResponse404
    | PatchVPNOpenVPNServerEndpointResponse405
    | PatchVPNOpenVPNServerEndpointResponse406
    | PatchVPNOpenVPNServerEndpointResponse409
    | PatchVPNOpenVPNServerEndpointResponse415
    | PatchVPNOpenVPNServerEndpointResponse422
    | PatchVPNOpenVPNServerEndpointResponse424
    | PatchVPNOpenVPNServerEndpointResponse500
    | PatchVPNOpenVPNServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchVPNOpenVPNServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchVPNOpenVPNServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchVPNOpenVPNServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchVPNOpenVPNServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchVPNOpenVPNServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchVPNOpenVPNServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchVPNOpenVPNServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchVPNOpenVPNServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchVPNOpenVPNServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchVPNOpenVPNServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchVPNOpenVPNServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchVPNOpenVPNServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchVPNOpenVPNServerEndpointResponse400
    | PatchVPNOpenVPNServerEndpointResponse401
    | PatchVPNOpenVPNServerEndpointResponse403
    | PatchVPNOpenVPNServerEndpointResponse404
    | PatchVPNOpenVPNServerEndpointResponse405
    | PatchVPNOpenVPNServerEndpointResponse406
    | PatchVPNOpenVPNServerEndpointResponse409
    | PatchVPNOpenVPNServerEndpointResponse415
    | PatchVPNOpenVPNServerEndpointResponse422
    | PatchVPNOpenVPNServerEndpointResponse424
    | PatchVPNOpenVPNServerEndpointResponse500
    | PatchVPNOpenVPNServerEndpointResponse503
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
    body: PatchVPNOpenVPNServerEndpointJsonBody | PatchVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNOpenVPNServerEndpointResponse400
    | PatchVPNOpenVPNServerEndpointResponse401
    | PatchVPNOpenVPNServerEndpointResponse403
    | PatchVPNOpenVPNServerEndpointResponse404
    | PatchVPNOpenVPNServerEndpointResponse405
    | PatchVPNOpenVPNServerEndpointResponse406
    | PatchVPNOpenVPNServerEndpointResponse409
    | PatchVPNOpenVPNServerEndpointResponse415
    | PatchVPNOpenVPNServerEndpointResponse422
    | PatchVPNOpenVPNServerEndpointResponse424
    | PatchVPNOpenVPNServerEndpointResponse500
    | PatchVPNOpenVPNServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNServerEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNOpenVPNServerEndpointResponse400 | PatchVPNOpenVPNServerEndpointResponse401 | PatchVPNOpenVPNServerEndpointResponse403 | PatchVPNOpenVPNServerEndpointResponse404 | PatchVPNOpenVPNServerEndpointResponse405 | PatchVPNOpenVPNServerEndpointResponse406 | PatchVPNOpenVPNServerEndpointResponse409 | PatchVPNOpenVPNServerEndpointResponse415 | PatchVPNOpenVPNServerEndpointResponse422 | PatchVPNOpenVPNServerEndpointResponse424 | PatchVPNOpenVPNServerEndpointResponse500 | PatchVPNOpenVPNServerEndpointResponse503]
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
    body: PatchVPNOpenVPNServerEndpointJsonBody | PatchVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNOpenVPNServerEndpointResponse400
    | PatchVPNOpenVPNServerEndpointResponse401
    | PatchVPNOpenVPNServerEndpointResponse403
    | PatchVPNOpenVPNServerEndpointResponse404
    | PatchVPNOpenVPNServerEndpointResponse405
    | PatchVPNOpenVPNServerEndpointResponse406
    | PatchVPNOpenVPNServerEndpointResponse409
    | PatchVPNOpenVPNServerEndpointResponse415
    | PatchVPNOpenVPNServerEndpointResponse422
    | PatchVPNOpenVPNServerEndpointResponse424
    | PatchVPNOpenVPNServerEndpointResponse500
    | PatchVPNOpenVPNServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNServerEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNOpenVPNServerEndpointResponse400 | PatchVPNOpenVPNServerEndpointResponse401 | PatchVPNOpenVPNServerEndpointResponse403 | PatchVPNOpenVPNServerEndpointResponse404 | PatchVPNOpenVPNServerEndpointResponse405 | PatchVPNOpenVPNServerEndpointResponse406 | PatchVPNOpenVPNServerEndpointResponse409 | PatchVPNOpenVPNServerEndpointResponse415 | PatchVPNOpenVPNServerEndpointResponse422 | PatchVPNOpenVPNServerEndpointResponse424 | PatchVPNOpenVPNServerEndpointResponse500 | PatchVPNOpenVPNServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNOpenVPNServerEndpointJsonBody | PatchVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchVPNOpenVPNServerEndpointResponse400
    | PatchVPNOpenVPNServerEndpointResponse401
    | PatchVPNOpenVPNServerEndpointResponse403
    | PatchVPNOpenVPNServerEndpointResponse404
    | PatchVPNOpenVPNServerEndpointResponse405
    | PatchVPNOpenVPNServerEndpointResponse406
    | PatchVPNOpenVPNServerEndpointResponse409
    | PatchVPNOpenVPNServerEndpointResponse415
    | PatchVPNOpenVPNServerEndpointResponse422
    | PatchVPNOpenVPNServerEndpointResponse424
    | PatchVPNOpenVPNServerEndpointResponse500
    | PatchVPNOpenVPNServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNServerEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchVPNOpenVPNServerEndpointResponse400 | PatchVPNOpenVPNServerEndpointResponse401 | PatchVPNOpenVPNServerEndpointResponse403 | PatchVPNOpenVPNServerEndpointResponse404 | PatchVPNOpenVPNServerEndpointResponse405 | PatchVPNOpenVPNServerEndpointResponse406 | PatchVPNOpenVPNServerEndpointResponse409 | PatchVPNOpenVPNServerEndpointResponse415 | PatchVPNOpenVPNServerEndpointResponse422 | PatchVPNOpenVPNServerEndpointResponse424 | PatchVPNOpenVPNServerEndpointResponse500 | PatchVPNOpenVPNServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchVPNOpenVPNServerEndpointJsonBody | PatchVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> (
    PatchVPNOpenVPNServerEndpointResponse400
    | PatchVPNOpenVPNServerEndpointResponse401
    | PatchVPNOpenVPNServerEndpointResponse403
    | PatchVPNOpenVPNServerEndpointResponse404
    | PatchVPNOpenVPNServerEndpointResponse405
    | PatchVPNOpenVPNServerEndpointResponse406
    | PatchVPNOpenVPNServerEndpointResponse409
    | PatchVPNOpenVPNServerEndpointResponse415
    | PatchVPNOpenVPNServerEndpointResponse422
    | PatchVPNOpenVPNServerEndpointResponse424
    | PatchVPNOpenVPNServerEndpointResponse500
    | PatchVPNOpenVPNServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchVPNOpenVPNServerEndpointJsonBody | Unset):
        body (PatchVPNOpenVPNServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchVPNOpenVPNServerEndpointResponse400 | PatchVPNOpenVPNServerEndpointResponse401 | PatchVPNOpenVPNServerEndpointResponse403 | PatchVPNOpenVPNServerEndpointResponse404 | PatchVPNOpenVPNServerEndpointResponse405 | PatchVPNOpenVPNServerEndpointResponse406 | PatchVPNOpenVPNServerEndpointResponse409 | PatchVPNOpenVPNServerEndpointResponse415 | PatchVPNOpenVPNServerEndpointResponse422 | PatchVPNOpenVPNServerEndpointResponse424 | PatchVPNOpenVPNServerEndpointResponse500 | PatchVPNOpenVPNServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
