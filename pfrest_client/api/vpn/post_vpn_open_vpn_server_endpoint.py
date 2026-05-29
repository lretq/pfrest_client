from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpn_open_vpn_server_endpoint_data_body import PostVPNOpenVPNServerEndpointDataBody
from ...models.post_vpn_open_vpn_server_endpoint_json_body import PostVPNOpenVPNServerEndpointJsonBody
from ...models.post_vpn_open_vpn_server_endpoint_response_400 import PostVPNOpenVPNServerEndpointResponse400
from ...models.post_vpn_open_vpn_server_endpoint_response_401 import PostVPNOpenVPNServerEndpointResponse401
from ...models.post_vpn_open_vpn_server_endpoint_response_403 import PostVPNOpenVPNServerEndpointResponse403
from ...models.post_vpn_open_vpn_server_endpoint_response_404 import PostVPNOpenVPNServerEndpointResponse404
from ...models.post_vpn_open_vpn_server_endpoint_response_405 import PostVPNOpenVPNServerEndpointResponse405
from ...models.post_vpn_open_vpn_server_endpoint_response_406 import PostVPNOpenVPNServerEndpointResponse406
from ...models.post_vpn_open_vpn_server_endpoint_response_409 import PostVPNOpenVPNServerEndpointResponse409
from ...models.post_vpn_open_vpn_server_endpoint_response_415 import PostVPNOpenVPNServerEndpointResponse415
from ...models.post_vpn_open_vpn_server_endpoint_response_422 import PostVPNOpenVPNServerEndpointResponse422
from ...models.post_vpn_open_vpn_server_endpoint_response_424 import PostVPNOpenVPNServerEndpointResponse424
from ...models.post_vpn_open_vpn_server_endpoint_response_500 import PostVPNOpenVPNServerEndpointResponse500
from ...models.post_vpn_open_vpn_server_endpoint_response_503 import PostVPNOpenVPNServerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNOpenVPNServerEndpointJsonBody | PostVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/openvpn/server",
    }

    if isinstance(body, PostVPNOpenVPNServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNOpenVPNServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNOpenVPNServerEndpointResponse400
    | PostVPNOpenVPNServerEndpointResponse401
    | PostVPNOpenVPNServerEndpointResponse403
    | PostVPNOpenVPNServerEndpointResponse404
    | PostVPNOpenVPNServerEndpointResponse405
    | PostVPNOpenVPNServerEndpointResponse406
    | PostVPNOpenVPNServerEndpointResponse409
    | PostVPNOpenVPNServerEndpointResponse415
    | PostVPNOpenVPNServerEndpointResponse422
    | PostVPNOpenVPNServerEndpointResponse424
    | PostVPNOpenVPNServerEndpointResponse500
    | PostVPNOpenVPNServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNOpenVPNServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNOpenVPNServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNOpenVPNServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNOpenVPNServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNOpenVPNServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNOpenVPNServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNOpenVPNServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNOpenVPNServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNOpenVPNServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNOpenVPNServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNOpenVPNServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNOpenVPNServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNOpenVPNServerEndpointResponse400
    | PostVPNOpenVPNServerEndpointResponse401
    | PostVPNOpenVPNServerEndpointResponse403
    | PostVPNOpenVPNServerEndpointResponse404
    | PostVPNOpenVPNServerEndpointResponse405
    | PostVPNOpenVPNServerEndpointResponse406
    | PostVPNOpenVPNServerEndpointResponse409
    | PostVPNOpenVPNServerEndpointResponse415
    | PostVPNOpenVPNServerEndpointResponse422
    | PostVPNOpenVPNServerEndpointResponse424
    | PostVPNOpenVPNServerEndpointResponse500
    | PostVPNOpenVPNServerEndpointResponse503
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
    body: PostVPNOpenVPNServerEndpointJsonBody | PostVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNServerEndpointResponse400
    | PostVPNOpenVPNServerEndpointResponse401
    | PostVPNOpenVPNServerEndpointResponse403
    | PostVPNOpenVPNServerEndpointResponse404
    | PostVPNOpenVPNServerEndpointResponse405
    | PostVPNOpenVPNServerEndpointResponse406
    | PostVPNOpenVPNServerEndpointResponse409
    | PostVPNOpenVPNServerEndpointResponse415
    | PostVPNOpenVPNServerEndpointResponse422
    | PostVPNOpenVPNServerEndpointResponse424
    | PostVPNOpenVPNServerEndpointResponse500
    | PostVPNOpenVPNServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNServerEndpointJsonBody | Unset):
        body (PostVPNOpenVPNServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNServerEndpointResponse400 | PostVPNOpenVPNServerEndpointResponse401 | PostVPNOpenVPNServerEndpointResponse403 | PostVPNOpenVPNServerEndpointResponse404 | PostVPNOpenVPNServerEndpointResponse405 | PostVPNOpenVPNServerEndpointResponse406 | PostVPNOpenVPNServerEndpointResponse409 | PostVPNOpenVPNServerEndpointResponse415 | PostVPNOpenVPNServerEndpointResponse422 | PostVPNOpenVPNServerEndpointResponse424 | PostVPNOpenVPNServerEndpointResponse500 | PostVPNOpenVPNServerEndpointResponse503]
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
    body: PostVPNOpenVPNServerEndpointJsonBody | PostVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNOpenVPNServerEndpointResponse400
    | PostVPNOpenVPNServerEndpointResponse401
    | PostVPNOpenVPNServerEndpointResponse403
    | PostVPNOpenVPNServerEndpointResponse404
    | PostVPNOpenVPNServerEndpointResponse405
    | PostVPNOpenVPNServerEndpointResponse406
    | PostVPNOpenVPNServerEndpointResponse409
    | PostVPNOpenVPNServerEndpointResponse415
    | PostVPNOpenVPNServerEndpointResponse422
    | PostVPNOpenVPNServerEndpointResponse424
    | PostVPNOpenVPNServerEndpointResponse500
    | PostVPNOpenVPNServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNServerEndpointJsonBody | Unset):
        body (PostVPNOpenVPNServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNServerEndpointResponse400 | PostVPNOpenVPNServerEndpointResponse401 | PostVPNOpenVPNServerEndpointResponse403 | PostVPNOpenVPNServerEndpointResponse404 | PostVPNOpenVPNServerEndpointResponse405 | PostVPNOpenVPNServerEndpointResponse406 | PostVPNOpenVPNServerEndpointResponse409 | PostVPNOpenVPNServerEndpointResponse415 | PostVPNOpenVPNServerEndpointResponse422 | PostVPNOpenVPNServerEndpointResponse424 | PostVPNOpenVPNServerEndpointResponse500 | PostVPNOpenVPNServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNServerEndpointJsonBody | PostVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNServerEndpointResponse400
    | PostVPNOpenVPNServerEndpointResponse401
    | PostVPNOpenVPNServerEndpointResponse403
    | PostVPNOpenVPNServerEndpointResponse404
    | PostVPNOpenVPNServerEndpointResponse405
    | PostVPNOpenVPNServerEndpointResponse406
    | PostVPNOpenVPNServerEndpointResponse409
    | PostVPNOpenVPNServerEndpointResponse415
    | PostVPNOpenVPNServerEndpointResponse422
    | PostVPNOpenVPNServerEndpointResponse424
    | PostVPNOpenVPNServerEndpointResponse500
    | PostVPNOpenVPNServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNServerEndpointJsonBody | Unset):
        body (PostVPNOpenVPNServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNServerEndpointResponse400 | PostVPNOpenVPNServerEndpointResponse401 | PostVPNOpenVPNServerEndpointResponse403 | PostVPNOpenVPNServerEndpointResponse404 | PostVPNOpenVPNServerEndpointResponse405 | PostVPNOpenVPNServerEndpointResponse406 | PostVPNOpenVPNServerEndpointResponse409 | PostVPNOpenVPNServerEndpointResponse415 | PostVPNOpenVPNServerEndpointResponse422 | PostVPNOpenVPNServerEndpointResponse424 | PostVPNOpenVPNServerEndpointResponse500 | PostVPNOpenVPNServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNServerEndpointJsonBody | PostVPNOpenVPNServerEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNOpenVPNServerEndpointResponse400
    | PostVPNOpenVPNServerEndpointResponse401
    | PostVPNOpenVPNServerEndpointResponse403
    | PostVPNOpenVPNServerEndpointResponse404
    | PostVPNOpenVPNServerEndpointResponse405
    | PostVPNOpenVPNServerEndpointResponse406
    | PostVPNOpenVPNServerEndpointResponse409
    | PostVPNOpenVPNServerEndpointResponse415
    | PostVPNOpenVPNServerEndpointResponse422
    | PostVPNOpenVPNServerEndpointResponse424
    | PostVPNOpenVPNServerEndpointResponse500
    | PostVPNOpenVPNServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new OpenVPN Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-server-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNServerEndpointJsonBody | Unset):
        body (PostVPNOpenVPNServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNServerEndpointResponse400 | PostVPNOpenVPNServerEndpointResponse401 | PostVPNOpenVPNServerEndpointResponse403 | PostVPNOpenVPNServerEndpointResponse404 | PostVPNOpenVPNServerEndpointResponse405 | PostVPNOpenVPNServerEndpointResponse406 | PostVPNOpenVPNServerEndpointResponse409 | PostVPNOpenVPNServerEndpointResponse415 | PostVPNOpenVPNServerEndpointResponse422 | PostVPNOpenVPNServerEndpointResponse424 | PostVPNOpenVPNServerEndpointResponse500 | PostVPNOpenVPNServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
