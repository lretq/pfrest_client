from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_vpn_open_vpncso_endpoint_data_body import PostVPNOpenVPNCSOEndpointDataBody
from ...models.post_vpn_open_vpncso_endpoint_json_body import PostVPNOpenVPNCSOEndpointJsonBody
from ...models.post_vpn_open_vpncso_endpoint_response_400 import PostVPNOpenVPNCSOEndpointResponse400
from ...models.post_vpn_open_vpncso_endpoint_response_401 import PostVPNOpenVPNCSOEndpointResponse401
from ...models.post_vpn_open_vpncso_endpoint_response_403 import PostVPNOpenVPNCSOEndpointResponse403
from ...models.post_vpn_open_vpncso_endpoint_response_404 import PostVPNOpenVPNCSOEndpointResponse404
from ...models.post_vpn_open_vpncso_endpoint_response_405 import PostVPNOpenVPNCSOEndpointResponse405
from ...models.post_vpn_open_vpncso_endpoint_response_406 import PostVPNOpenVPNCSOEndpointResponse406
from ...models.post_vpn_open_vpncso_endpoint_response_409 import PostVPNOpenVPNCSOEndpointResponse409
from ...models.post_vpn_open_vpncso_endpoint_response_415 import PostVPNOpenVPNCSOEndpointResponse415
from ...models.post_vpn_open_vpncso_endpoint_response_422 import PostVPNOpenVPNCSOEndpointResponse422
from ...models.post_vpn_open_vpncso_endpoint_response_424 import PostVPNOpenVPNCSOEndpointResponse424
from ...models.post_vpn_open_vpncso_endpoint_response_500 import PostVPNOpenVPNCSOEndpointResponse500
from ...models.post_vpn_open_vpncso_endpoint_response_503 import PostVPNOpenVPNCSOEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostVPNOpenVPNCSOEndpointJsonBody | PostVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/vpn/openvpn/cso",
    }

    if isinstance(body, PostVPNOpenVPNCSOEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostVPNOpenVPNCSOEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostVPNOpenVPNCSOEndpointResponse400
    | PostVPNOpenVPNCSOEndpointResponse401
    | PostVPNOpenVPNCSOEndpointResponse403
    | PostVPNOpenVPNCSOEndpointResponse404
    | PostVPNOpenVPNCSOEndpointResponse405
    | PostVPNOpenVPNCSOEndpointResponse406
    | PostVPNOpenVPNCSOEndpointResponse409
    | PostVPNOpenVPNCSOEndpointResponse415
    | PostVPNOpenVPNCSOEndpointResponse422
    | PostVPNOpenVPNCSOEndpointResponse424
    | PostVPNOpenVPNCSOEndpointResponse500
    | PostVPNOpenVPNCSOEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostVPNOpenVPNCSOEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostVPNOpenVPNCSOEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostVPNOpenVPNCSOEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostVPNOpenVPNCSOEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostVPNOpenVPNCSOEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostVPNOpenVPNCSOEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostVPNOpenVPNCSOEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostVPNOpenVPNCSOEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostVPNOpenVPNCSOEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostVPNOpenVPNCSOEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostVPNOpenVPNCSOEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostVPNOpenVPNCSOEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostVPNOpenVPNCSOEndpointResponse400
    | PostVPNOpenVPNCSOEndpointResponse401
    | PostVPNOpenVPNCSOEndpointResponse403
    | PostVPNOpenVPNCSOEndpointResponse404
    | PostVPNOpenVPNCSOEndpointResponse405
    | PostVPNOpenVPNCSOEndpointResponse406
    | PostVPNOpenVPNCSOEndpointResponse409
    | PostVPNOpenVPNCSOEndpointResponse415
    | PostVPNOpenVPNCSOEndpointResponse422
    | PostVPNOpenVPNCSOEndpointResponse424
    | PostVPNOpenVPNCSOEndpointResponse500
    | PostVPNOpenVPNCSOEndpointResponse503
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
    body: PostVPNOpenVPNCSOEndpointJsonBody | PostVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNCSOEndpointResponse400
    | PostVPNOpenVPNCSOEndpointResponse401
    | PostVPNOpenVPNCSOEndpointResponse403
    | PostVPNOpenVPNCSOEndpointResponse404
    | PostVPNOpenVPNCSOEndpointResponse405
    | PostVPNOpenVPNCSOEndpointResponse406
    | PostVPNOpenVPNCSOEndpointResponse409
    | PostVPNOpenVPNCSOEndpointResponse415
    | PostVPNOpenVPNCSOEndpointResponse422
    | PostVPNOpenVPNCSOEndpointResponse424
    | PostVPNOpenVPNCSOEndpointResponse500
    | PostVPNOpenVPNCSOEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new OpenVPN Client Specific Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientSpecificOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-cso-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNCSOEndpointJsonBody | Unset):
        body (PostVPNOpenVPNCSOEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNCSOEndpointResponse400 | PostVPNOpenVPNCSOEndpointResponse401 | PostVPNOpenVPNCSOEndpointResponse403 | PostVPNOpenVPNCSOEndpointResponse404 | PostVPNOpenVPNCSOEndpointResponse405 | PostVPNOpenVPNCSOEndpointResponse406 | PostVPNOpenVPNCSOEndpointResponse409 | PostVPNOpenVPNCSOEndpointResponse415 | PostVPNOpenVPNCSOEndpointResponse422 | PostVPNOpenVPNCSOEndpointResponse424 | PostVPNOpenVPNCSOEndpointResponse500 | PostVPNOpenVPNCSOEndpointResponse503]
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
    body: PostVPNOpenVPNCSOEndpointJsonBody | PostVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNOpenVPNCSOEndpointResponse400
    | PostVPNOpenVPNCSOEndpointResponse401
    | PostVPNOpenVPNCSOEndpointResponse403
    | PostVPNOpenVPNCSOEndpointResponse404
    | PostVPNOpenVPNCSOEndpointResponse405
    | PostVPNOpenVPNCSOEndpointResponse406
    | PostVPNOpenVPNCSOEndpointResponse409
    | PostVPNOpenVPNCSOEndpointResponse415
    | PostVPNOpenVPNCSOEndpointResponse422
    | PostVPNOpenVPNCSOEndpointResponse424
    | PostVPNOpenVPNCSOEndpointResponse500
    | PostVPNOpenVPNCSOEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new OpenVPN Client Specific Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientSpecificOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-cso-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNCSOEndpointJsonBody | Unset):
        body (PostVPNOpenVPNCSOEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNCSOEndpointResponse400 | PostVPNOpenVPNCSOEndpointResponse401 | PostVPNOpenVPNCSOEndpointResponse403 | PostVPNOpenVPNCSOEndpointResponse404 | PostVPNOpenVPNCSOEndpointResponse405 | PostVPNOpenVPNCSOEndpointResponse406 | PostVPNOpenVPNCSOEndpointResponse409 | PostVPNOpenVPNCSOEndpointResponse415 | PostVPNOpenVPNCSOEndpointResponse422 | PostVPNOpenVPNCSOEndpointResponse424 | PostVPNOpenVPNCSOEndpointResponse500 | PostVPNOpenVPNCSOEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNCSOEndpointJsonBody | PostVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> Response[
    PostVPNOpenVPNCSOEndpointResponse400
    | PostVPNOpenVPNCSOEndpointResponse401
    | PostVPNOpenVPNCSOEndpointResponse403
    | PostVPNOpenVPNCSOEndpointResponse404
    | PostVPNOpenVPNCSOEndpointResponse405
    | PostVPNOpenVPNCSOEndpointResponse406
    | PostVPNOpenVPNCSOEndpointResponse409
    | PostVPNOpenVPNCSOEndpointResponse415
    | PostVPNOpenVPNCSOEndpointResponse422
    | PostVPNOpenVPNCSOEndpointResponse424
    | PostVPNOpenVPNCSOEndpointResponse500
    | PostVPNOpenVPNCSOEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new OpenVPN Client Specific Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientSpecificOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-cso-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNCSOEndpointJsonBody | Unset):
        body (PostVPNOpenVPNCSOEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostVPNOpenVPNCSOEndpointResponse400 | PostVPNOpenVPNCSOEndpointResponse401 | PostVPNOpenVPNCSOEndpointResponse403 | PostVPNOpenVPNCSOEndpointResponse404 | PostVPNOpenVPNCSOEndpointResponse405 | PostVPNOpenVPNCSOEndpointResponse406 | PostVPNOpenVPNCSOEndpointResponse409 | PostVPNOpenVPNCSOEndpointResponse415 | PostVPNOpenVPNCSOEndpointResponse422 | PostVPNOpenVPNCSOEndpointResponse424 | PostVPNOpenVPNCSOEndpointResponse500 | PostVPNOpenVPNCSOEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostVPNOpenVPNCSOEndpointJsonBody | PostVPNOpenVPNCSOEndpointDataBody | Unset = UNSET,
) -> (
    PostVPNOpenVPNCSOEndpointResponse400
    | PostVPNOpenVPNCSOEndpointResponse401
    | PostVPNOpenVPNCSOEndpointResponse403
    | PostVPNOpenVPNCSOEndpointResponse404
    | PostVPNOpenVPNCSOEndpointResponse405
    | PostVPNOpenVPNCSOEndpointResponse406
    | PostVPNOpenVPNCSOEndpointResponse409
    | PostVPNOpenVPNCSOEndpointResponse415
    | PostVPNOpenVPNCSOEndpointResponse422
    | PostVPNOpenVPNCSOEndpointResponse424
    | PostVPNOpenVPNCSOEndpointResponse500
    | PostVPNOpenVPNCSOEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new OpenVPN Client Specific Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: OpenVPNClientSpecificOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-openvpn-cso-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostVPNOpenVPNCSOEndpointJsonBody | Unset):
        body (PostVPNOpenVPNCSOEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostVPNOpenVPNCSOEndpointResponse400 | PostVPNOpenVPNCSOEndpointResponse401 | PostVPNOpenVPNCSOEndpointResponse403 | PostVPNOpenVPNCSOEndpointResponse404 | PostVPNOpenVPNCSOEndpointResponse405 | PostVPNOpenVPNCSOEndpointResponse406 | PostVPNOpenVPNCSOEndpointResponse409 | PostVPNOpenVPNCSOEndpointResponse415 | PostVPNOpenVPNCSOEndpointResponse422 | PostVPNOpenVPNCSOEndpointResponse424 | PostVPNOpenVPNCSOEndpointResponse500 | PostVPNOpenVPNCSOEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
