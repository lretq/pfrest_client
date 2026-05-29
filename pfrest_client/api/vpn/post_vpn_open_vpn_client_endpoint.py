from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpn_open_vpn_client_endpoint_data_body import PostVPNOpenVPNClientEndpointDataBody
from ...models.post_vpn_open_vpn_client_endpoint_json_body import PostVPNOpenVPNClientEndpointJsonBody
from ...models.post_vpn_open_vpn_client_endpoint_response_400 import PostVPNOpenVPNClientEndpointResponse400
from ...models.post_vpn_open_vpn_client_endpoint_response_401 import PostVPNOpenVPNClientEndpointResponse401
from ...models.post_vpn_open_vpn_client_endpoint_response_403 import PostVPNOpenVPNClientEndpointResponse403
from ...models.post_vpn_open_vpn_client_endpoint_response_404 import PostVPNOpenVPNClientEndpointResponse404
from ...models.post_vpn_open_vpn_client_endpoint_response_405 import PostVPNOpenVPNClientEndpointResponse405
from ...models.post_vpn_open_vpn_client_endpoint_response_406 import PostVPNOpenVPNClientEndpointResponse406
from ...models.post_vpn_open_vpn_client_endpoint_response_409 import PostVPNOpenVPNClientEndpointResponse409
from ...models.post_vpn_open_vpn_client_endpoint_response_415 import PostVPNOpenVPNClientEndpointResponse415
from ...models.post_vpn_open_vpn_client_endpoint_response_422 import PostVPNOpenVPNClientEndpointResponse422
from ...models.post_vpn_open_vpn_client_endpoint_response_424 import PostVPNOpenVPNClientEndpointResponse424
from ...models.post_vpn_open_vpn_client_endpoint_response_500 import PostVPNOpenVPNClientEndpointResponse500
from ...models.post_vpn_open_vpn_client_endpoint_response_503 import PostVPNOpenVPNClientEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNOpenVPNClientEndpointJsonBody | PostVPNOpenVPNClientEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/openvpn/client",
    }

    if isinstance(body, PostVPNOpenVPNClientEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNOpenVPNClientEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNOpenVPNClientEndpointResponse400
    | PostVPNOpenVPNClientEndpointResponse401
    | PostVPNOpenVPNClientEndpointResponse403
    | PostVPNOpenVPNClientEndpointResponse404
    | PostVPNOpenVPNClientEndpointResponse405
    | PostVPNOpenVPNClientEndpointResponse406
    | PostVPNOpenVPNClientEndpointResponse409
    | PostVPNOpenVPNClientEndpointResponse415
    | PostVPNOpenVPNClientEndpointResponse422
    | PostVPNOpenVPNClientEndpointResponse424
    | PostVPNOpenVPNClientEndpointResponse500
    | PostVPNOpenVPNClientEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNOpenVPNClientEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNOpenVPNClientEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNOpenVPNClientEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNOpenVPNClientEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNOpenVPNClientEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNOpenVPNClientEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNOpenVPNClientEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNOpenVPNClientEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNOpenVPNClientEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNOpenVPNClientEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNOpenVPNClientEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNOpenVPNClientEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNOpenVPNClientEndpointResponse400
    | PostVPNOpenVPNClientEndpointResponse401
    | PostVPNOpenVPNClientEndpointResponse403
    | PostVPNOpenVPNClientEndpointResponse404
    | PostVPNOpenVPNClientEndpointResponse405
    | PostVPNOpenVPNClientEndpointResponse406
    | PostVPNOpenVPNClientEndpointResponse409
    | PostVPNOpenVPNClientEndpointResponse415
    | PostVPNOpenVPNClientEndpointResponse422
    | PostVPNOpenVPNClientEndpointResponse424
    | PostVPNOpenVPNClientEndpointResponse500
    | PostVPNOpenVPNClientEndpointResponse503
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
    body: PostVPNOpenVPNClientEndpointJsonBody | PostVPNOpenVPNClientEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNClientEndpointResponse400
    | PostVPNOpenVPNClientEndpointResponse401
    | PostVPNOpenVPNClientEndpointResponse403
    | PostVPNOpenVPNClientEndpointResponse404
    | PostVPNOpenVPNClientEndpointResponse405
    | PostVPNOpenVPNClientEndpointResponse406
    | PostVPNOpenVPNClientEndpointResponse409
    | PostVPNOpenVPNClientEndpointResponse415
    | PostVPNOpenVPNClientEndpointResponse422
    | PostVPNOpenVPNClientEndpointResponse424
    | PostVPNOpenVPNClientEndpointResponse500
    | PostVPNOpenVPNClientEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new OpenVPN Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNClientEndpointResponse400 | PostVPNOpenVPNClientEndpointResponse401 | PostVPNOpenVPNClientEndpointResponse403 | PostVPNOpenVPNClientEndpointResponse404 | PostVPNOpenVPNClientEndpointResponse405 | PostVPNOpenVPNClientEndpointResponse406 | PostVPNOpenVPNClientEndpointResponse409 | PostVPNOpenVPNClientEndpointResponse415 | PostVPNOpenVPNClientEndpointResponse422 | PostVPNOpenVPNClientEndpointResponse424 | PostVPNOpenVPNClientEndpointResponse500 | PostVPNOpenVPNClientEndpointResponse503]
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
    body: PostVPNOpenVPNClientEndpointJsonBody | PostVPNOpenVPNClientEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNOpenVPNClientEndpointResponse400
    | PostVPNOpenVPNClientEndpointResponse401
    | PostVPNOpenVPNClientEndpointResponse403
    | PostVPNOpenVPNClientEndpointResponse404
    | PostVPNOpenVPNClientEndpointResponse405
    | PostVPNOpenVPNClientEndpointResponse406
    | PostVPNOpenVPNClientEndpointResponse409
    | PostVPNOpenVPNClientEndpointResponse415
    | PostVPNOpenVPNClientEndpointResponse422
    | PostVPNOpenVPNClientEndpointResponse424
    | PostVPNOpenVPNClientEndpointResponse500
    | PostVPNOpenVPNClientEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new OpenVPN Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNClientEndpointResponse400 | PostVPNOpenVPNClientEndpointResponse401 | PostVPNOpenVPNClientEndpointResponse403 | PostVPNOpenVPNClientEndpointResponse404 | PostVPNOpenVPNClientEndpointResponse405 | PostVPNOpenVPNClientEndpointResponse406 | PostVPNOpenVPNClientEndpointResponse409 | PostVPNOpenVPNClientEndpointResponse415 | PostVPNOpenVPNClientEndpointResponse422 | PostVPNOpenVPNClientEndpointResponse424 | PostVPNOpenVPNClientEndpointResponse500 | PostVPNOpenVPNClientEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNClientEndpointJsonBody | PostVPNOpenVPNClientEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNClientEndpointResponse400
    | PostVPNOpenVPNClientEndpointResponse401
    | PostVPNOpenVPNClientEndpointResponse403
    | PostVPNOpenVPNClientEndpointResponse404
    | PostVPNOpenVPNClientEndpointResponse405
    | PostVPNOpenVPNClientEndpointResponse406
    | PostVPNOpenVPNClientEndpointResponse409
    | PostVPNOpenVPNClientEndpointResponse415
    | PostVPNOpenVPNClientEndpointResponse422
    | PostVPNOpenVPNClientEndpointResponse424
    | PostVPNOpenVPNClientEndpointResponse500
    | PostVPNOpenVPNClientEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new OpenVPN Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNClientEndpointResponse400 | PostVPNOpenVPNClientEndpointResponse401 | PostVPNOpenVPNClientEndpointResponse403 | PostVPNOpenVPNClientEndpointResponse404 | PostVPNOpenVPNClientEndpointResponse405 | PostVPNOpenVPNClientEndpointResponse406 | PostVPNOpenVPNClientEndpointResponse409 | PostVPNOpenVPNClientEndpointResponse415 | PostVPNOpenVPNClientEndpointResponse422 | PostVPNOpenVPNClientEndpointResponse424 | PostVPNOpenVPNClientEndpointResponse500 | PostVPNOpenVPNClientEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNClientEndpointJsonBody | PostVPNOpenVPNClientEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNOpenVPNClientEndpointResponse400
    | PostVPNOpenVPNClientEndpointResponse401
    | PostVPNOpenVPNClientEndpointResponse403
    | PostVPNOpenVPNClientEndpointResponse404
    | PostVPNOpenVPNClientEndpointResponse405
    | PostVPNOpenVPNClientEndpointResponse406
    | PostVPNOpenVPNClientEndpointResponse409
    | PostVPNOpenVPNClientEndpointResponse415
    | PostVPNOpenVPNClientEndpointResponse422
    | PostVPNOpenVPNClientEndpointResponse424
    | PostVPNOpenVPNClientEndpointResponse500
    | PostVPNOpenVPNClientEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new OpenVPN Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: OpenVPNClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-client-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNClientEndpointJsonBody | Unset):
        body (PostVPNOpenVPNClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNClientEndpointResponse400 | PostVPNOpenVPNClientEndpointResponse401 | PostVPNOpenVPNClientEndpointResponse403 | PostVPNOpenVPNClientEndpointResponse404 | PostVPNOpenVPNClientEndpointResponse405 | PostVPNOpenVPNClientEndpointResponse406 | PostVPNOpenVPNClientEndpointResponse409 | PostVPNOpenVPNClientEndpointResponse415 | PostVPNOpenVPNClientEndpointResponse422 | PostVPNOpenVPNClientEndpointResponse424 | PostVPNOpenVPNClientEndpointResponse500 | PostVPNOpenVPNClientEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
