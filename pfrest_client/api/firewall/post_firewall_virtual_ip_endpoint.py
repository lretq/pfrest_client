from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_virtual_ip_endpoint_data_body import PostFirewallVirtualIPEndpointDataBody
from ...models.post_firewall_virtual_ip_endpoint_json_body import PostFirewallVirtualIPEndpointJsonBody
from ...models.post_firewall_virtual_ip_endpoint_response_400 import PostFirewallVirtualIPEndpointResponse400
from ...models.post_firewall_virtual_ip_endpoint_response_401 import PostFirewallVirtualIPEndpointResponse401
from ...models.post_firewall_virtual_ip_endpoint_response_403 import PostFirewallVirtualIPEndpointResponse403
from ...models.post_firewall_virtual_ip_endpoint_response_404 import PostFirewallVirtualIPEndpointResponse404
from ...models.post_firewall_virtual_ip_endpoint_response_405 import PostFirewallVirtualIPEndpointResponse405
from ...models.post_firewall_virtual_ip_endpoint_response_406 import PostFirewallVirtualIPEndpointResponse406
from ...models.post_firewall_virtual_ip_endpoint_response_409 import PostFirewallVirtualIPEndpointResponse409
from ...models.post_firewall_virtual_ip_endpoint_response_415 import PostFirewallVirtualIPEndpointResponse415
from ...models.post_firewall_virtual_ip_endpoint_response_422 import PostFirewallVirtualIPEndpointResponse422
from ...models.post_firewall_virtual_ip_endpoint_response_424 import PostFirewallVirtualIPEndpointResponse424
from ...models.post_firewall_virtual_ip_endpoint_response_500 import PostFirewallVirtualIPEndpointResponse500
from ...models.post_firewall_virtual_ip_endpoint_response_503 import PostFirewallVirtualIPEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallVirtualIPEndpointJsonBody | PostFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/virtual_ip",
    }

    if isinstance(body, PostFirewallVirtualIPEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallVirtualIPEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallVirtualIPEndpointResponse400
    | PostFirewallVirtualIPEndpointResponse401
    | PostFirewallVirtualIPEndpointResponse403
    | PostFirewallVirtualIPEndpointResponse404
    | PostFirewallVirtualIPEndpointResponse405
    | PostFirewallVirtualIPEndpointResponse406
    | PostFirewallVirtualIPEndpointResponse409
    | PostFirewallVirtualIPEndpointResponse415
    | PostFirewallVirtualIPEndpointResponse422
    | PostFirewallVirtualIPEndpointResponse424
    | PostFirewallVirtualIPEndpointResponse500
    | PostFirewallVirtualIPEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallVirtualIPEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallVirtualIPEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallVirtualIPEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallVirtualIPEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallVirtualIPEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallVirtualIPEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallVirtualIPEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallVirtualIPEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallVirtualIPEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallVirtualIPEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallVirtualIPEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallVirtualIPEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallVirtualIPEndpointResponse400
    | PostFirewallVirtualIPEndpointResponse401
    | PostFirewallVirtualIPEndpointResponse403
    | PostFirewallVirtualIPEndpointResponse404
    | PostFirewallVirtualIPEndpointResponse405
    | PostFirewallVirtualIPEndpointResponse406
    | PostFirewallVirtualIPEndpointResponse409
    | PostFirewallVirtualIPEndpointResponse415
    | PostFirewallVirtualIPEndpointResponse422
    | PostFirewallVirtualIPEndpointResponse424
    | PostFirewallVirtualIPEndpointResponse500
    | PostFirewallVirtualIPEndpointResponse503
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
    body: PostFirewallVirtualIPEndpointJsonBody | PostFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallVirtualIPEndpointResponse400
    | PostFirewallVirtualIPEndpointResponse401
    | PostFirewallVirtualIPEndpointResponse403
    | PostFirewallVirtualIPEndpointResponse404
    | PostFirewallVirtualIPEndpointResponse405
    | PostFirewallVirtualIPEndpointResponse406
    | PostFirewallVirtualIPEndpointResponse409
    | PostFirewallVirtualIPEndpointResponse415
    | PostFirewallVirtualIPEndpointResponse422
    | PostFirewallVirtualIPEndpointResponse424
    | PostFirewallVirtualIPEndpointResponse500
    | PostFirewallVirtualIPEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Virtual IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallVirtualIPEndpointJsonBody | Unset):
        body (PostFirewallVirtualIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallVirtualIPEndpointResponse400 | PostFirewallVirtualIPEndpointResponse401 | PostFirewallVirtualIPEndpointResponse403 | PostFirewallVirtualIPEndpointResponse404 | PostFirewallVirtualIPEndpointResponse405 | PostFirewallVirtualIPEndpointResponse406 | PostFirewallVirtualIPEndpointResponse409 | PostFirewallVirtualIPEndpointResponse415 | PostFirewallVirtualIPEndpointResponse422 | PostFirewallVirtualIPEndpointResponse424 | PostFirewallVirtualIPEndpointResponse500 | PostFirewallVirtualIPEndpointResponse503]
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
    body: PostFirewallVirtualIPEndpointJsonBody | PostFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallVirtualIPEndpointResponse400
    | PostFirewallVirtualIPEndpointResponse401
    | PostFirewallVirtualIPEndpointResponse403
    | PostFirewallVirtualIPEndpointResponse404
    | PostFirewallVirtualIPEndpointResponse405
    | PostFirewallVirtualIPEndpointResponse406
    | PostFirewallVirtualIPEndpointResponse409
    | PostFirewallVirtualIPEndpointResponse415
    | PostFirewallVirtualIPEndpointResponse422
    | PostFirewallVirtualIPEndpointResponse424
    | PostFirewallVirtualIPEndpointResponse500
    | PostFirewallVirtualIPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Virtual IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallVirtualIPEndpointJsonBody | Unset):
        body (PostFirewallVirtualIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallVirtualIPEndpointResponse400 | PostFirewallVirtualIPEndpointResponse401 | PostFirewallVirtualIPEndpointResponse403 | PostFirewallVirtualIPEndpointResponse404 | PostFirewallVirtualIPEndpointResponse405 | PostFirewallVirtualIPEndpointResponse406 | PostFirewallVirtualIPEndpointResponse409 | PostFirewallVirtualIPEndpointResponse415 | PostFirewallVirtualIPEndpointResponse422 | PostFirewallVirtualIPEndpointResponse424 | PostFirewallVirtualIPEndpointResponse500 | PostFirewallVirtualIPEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallVirtualIPEndpointJsonBody | PostFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallVirtualIPEndpointResponse400
    | PostFirewallVirtualIPEndpointResponse401
    | PostFirewallVirtualIPEndpointResponse403
    | PostFirewallVirtualIPEndpointResponse404
    | PostFirewallVirtualIPEndpointResponse405
    | PostFirewallVirtualIPEndpointResponse406
    | PostFirewallVirtualIPEndpointResponse409
    | PostFirewallVirtualIPEndpointResponse415
    | PostFirewallVirtualIPEndpointResponse422
    | PostFirewallVirtualIPEndpointResponse424
    | PostFirewallVirtualIPEndpointResponse500
    | PostFirewallVirtualIPEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Virtual IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallVirtualIPEndpointJsonBody | Unset):
        body (PostFirewallVirtualIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallVirtualIPEndpointResponse400 | PostFirewallVirtualIPEndpointResponse401 | PostFirewallVirtualIPEndpointResponse403 | PostFirewallVirtualIPEndpointResponse404 | PostFirewallVirtualIPEndpointResponse405 | PostFirewallVirtualIPEndpointResponse406 | PostFirewallVirtualIPEndpointResponse409 | PostFirewallVirtualIPEndpointResponse415 | PostFirewallVirtualIPEndpointResponse422 | PostFirewallVirtualIPEndpointResponse424 | PostFirewallVirtualIPEndpointResponse500 | PostFirewallVirtualIPEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallVirtualIPEndpointJsonBody | PostFirewallVirtualIPEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallVirtualIPEndpointResponse400
    | PostFirewallVirtualIPEndpointResponse401
    | PostFirewallVirtualIPEndpointResponse403
    | PostFirewallVirtualIPEndpointResponse404
    | PostFirewallVirtualIPEndpointResponse405
    | PostFirewallVirtualIPEndpointResponse406
    | PostFirewallVirtualIPEndpointResponse409
    | PostFirewallVirtualIPEndpointResponse415
    | PostFirewallVirtualIPEndpointResponse422
    | PostFirewallVirtualIPEndpointResponse424
    | PostFirewallVirtualIPEndpointResponse500
    | PostFirewallVirtualIPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Virtual IP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallVirtualIPEndpointJsonBody | Unset):
        body (PostFirewallVirtualIPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallVirtualIPEndpointResponse400 | PostFirewallVirtualIPEndpointResponse401 | PostFirewallVirtualIPEndpointResponse403 | PostFirewallVirtualIPEndpointResponse404 | PostFirewallVirtualIPEndpointResponse405 | PostFirewallVirtualIPEndpointResponse406 | PostFirewallVirtualIPEndpointResponse409 | PostFirewallVirtualIPEndpointResponse415 | PostFirewallVirtualIPEndpointResponse422 | PostFirewallVirtualIPEndpointResponse424 | PostFirewallVirtualIPEndpointResponse500 | PostFirewallVirtualIPEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
