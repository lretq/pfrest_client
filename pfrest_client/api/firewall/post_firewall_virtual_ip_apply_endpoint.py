from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_virtual_ip_apply_endpoint_data_body import PostFirewallVirtualIPApplyEndpointDataBody
from ...models.post_firewall_virtual_ip_apply_endpoint_json_body import PostFirewallVirtualIPApplyEndpointJsonBody
from ...models.post_firewall_virtual_ip_apply_endpoint_response_400 import PostFirewallVirtualIPApplyEndpointResponse400
from ...models.post_firewall_virtual_ip_apply_endpoint_response_401 import PostFirewallVirtualIPApplyEndpointResponse401
from ...models.post_firewall_virtual_ip_apply_endpoint_response_403 import PostFirewallVirtualIPApplyEndpointResponse403
from ...models.post_firewall_virtual_ip_apply_endpoint_response_404 import PostFirewallVirtualIPApplyEndpointResponse404
from ...models.post_firewall_virtual_ip_apply_endpoint_response_405 import PostFirewallVirtualIPApplyEndpointResponse405
from ...models.post_firewall_virtual_ip_apply_endpoint_response_406 import PostFirewallVirtualIPApplyEndpointResponse406
from ...models.post_firewall_virtual_ip_apply_endpoint_response_409 import PostFirewallVirtualIPApplyEndpointResponse409
from ...models.post_firewall_virtual_ip_apply_endpoint_response_415 import PostFirewallVirtualIPApplyEndpointResponse415
from ...models.post_firewall_virtual_ip_apply_endpoint_response_422 import PostFirewallVirtualIPApplyEndpointResponse422
from ...models.post_firewall_virtual_ip_apply_endpoint_response_424 import PostFirewallVirtualIPApplyEndpointResponse424
from ...models.post_firewall_virtual_ip_apply_endpoint_response_500 import PostFirewallVirtualIPApplyEndpointResponse500
from ...models.post_firewall_virtual_ip_apply_endpoint_response_503 import PostFirewallVirtualIPApplyEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallVirtualIPApplyEndpointJsonBody | PostFirewallVirtualIPApplyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/virtual_ip/apply",
    }

    if isinstance(body, PostFirewallVirtualIPApplyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallVirtualIPApplyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallVirtualIPApplyEndpointResponse400
    | PostFirewallVirtualIPApplyEndpointResponse401
    | PostFirewallVirtualIPApplyEndpointResponse403
    | PostFirewallVirtualIPApplyEndpointResponse404
    | PostFirewallVirtualIPApplyEndpointResponse405
    | PostFirewallVirtualIPApplyEndpointResponse406
    | PostFirewallVirtualIPApplyEndpointResponse409
    | PostFirewallVirtualIPApplyEndpointResponse415
    | PostFirewallVirtualIPApplyEndpointResponse422
    | PostFirewallVirtualIPApplyEndpointResponse424
    | PostFirewallVirtualIPApplyEndpointResponse500
    | PostFirewallVirtualIPApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallVirtualIPApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallVirtualIPApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallVirtualIPApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallVirtualIPApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallVirtualIPApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallVirtualIPApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallVirtualIPApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallVirtualIPApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallVirtualIPApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallVirtualIPApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallVirtualIPApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallVirtualIPApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallVirtualIPApplyEndpointResponse400
    | PostFirewallVirtualIPApplyEndpointResponse401
    | PostFirewallVirtualIPApplyEndpointResponse403
    | PostFirewallVirtualIPApplyEndpointResponse404
    | PostFirewallVirtualIPApplyEndpointResponse405
    | PostFirewallVirtualIPApplyEndpointResponse406
    | PostFirewallVirtualIPApplyEndpointResponse409
    | PostFirewallVirtualIPApplyEndpointResponse415
    | PostFirewallVirtualIPApplyEndpointResponse422
    | PostFirewallVirtualIPApplyEndpointResponse424
    | PostFirewallVirtualIPApplyEndpointResponse500
    | PostFirewallVirtualIPApplyEndpointResponse503
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
    body: PostFirewallVirtualIPApplyEndpointJsonBody | PostFirewallVirtualIPApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallVirtualIPApplyEndpointResponse400
    | PostFirewallVirtualIPApplyEndpointResponse401
    | PostFirewallVirtualIPApplyEndpointResponse403
    | PostFirewallVirtualIPApplyEndpointResponse404
    | PostFirewallVirtualIPApplyEndpointResponse405
    | PostFirewallVirtualIPApplyEndpointResponse406
    | PostFirewallVirtualIPApplyEndpointResponse409
    | PostFirewallVirtualIPApplyEndpointResponse415
    | PostFirewallVirtualIPApplyEndpointResponse422
    | PostFirewallVirtualIPApplyEndpointResponse424
    | PostFirewallVirtualIPApplyEndpointResponse500
    | PostFirewallVirtualIPApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending virtual IP changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIPApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostFirewallVirtualIPApplyEndpointJsonBody | Unset):
        body (PostFirewallVirtualIPApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallVirtualIPApplyEndpointResponse400 | PostFirewallVirtualIPApplyEndpointResponse401 | PostFirewallVirtualIPApplyEndpointResponse403 | PostFirewallVirtualIPApplyEndpointResponse404 | PostFirewallVirtualIPApplyEndpointResponse405 | PostFirewallVirtualIPApplyEndpointResponse406 | PostFirewallVirtualIPApplyEndpointResponse409 | PostFirewallVirtualIPApplyEndpointResponse415 | PostFirewallVirtualIPApplyEndpointResponse422 | PostFirewallVirtualIPApplyEndpointResponse424 | PostFirewallVirtualIPApplyEndpointResponse500 | PostFirewallVirtualIPApplyEndpointResponse503]
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
    body: PostFirewallVirtualIPApplyEndpointJsonBody | PostFirewallVirtualIPApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallVirtualIPApplyEndpointResponse400
    | PostFirewallVirtualIPApplyEndpointResponse401
    | PostFirewallVirtualIPApplyEndpointResponse403
    | PostFirewallVirtualIPApplyEndpointResponse404
    | PostFirewallVirtualIPApplyEndpointResponse405
    | PostFirewallVirtualIPApplyEndpointResponse406
    | PostFirewallVirtualIPApplyEndpointResponse409
    | PostFirewallVirtualIPApplyEndpointResponse415
    | PostFirewallVirtualIPApplyEndpointResponse422
    | PostFirewallVirtualIPApplyEndpointResponse424
    | PostFirewallVirtualIPApplyEndpointResponse500
    | PostFirewallVirtualIPApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending virtual IP changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIPApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostFirewallVirtualIPApplyEndpointJsonBody | Unset):
        body (PostFirewallVirtualIPApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallVirtualIPApplyEndpointResponse400 | PostFirewallVirtualIPApplyEndpointResponse401 | PostFirewallVirtualIPApplyEndpointResponse403 | PostFirewallVirtualIPApplyEndpointResponse404 | PostFirewallVirtualIPApplyEndpointResponse405 | PostFirewallVirtualIPApplyEndpointResponse406 | PostFirewallVirtualIPApplyEndpointResponse409 | PostFirewallVirtualIPApplyEndpointResponse415 | PostFirewallVirtualIPApplyEndpointResponse422 | PostFirewallVirtualIPApplyEndpointResponse424 | PostFirewallVirtualIPApplyEndpointResponse500 | PostFirewallVirtualIPApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallVirtualIPApplyEndpointJsonBody | PostFirewallVirtualIPApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallVirtualIPApplyEndpointResponse400
    | PostFirewallVirtualIPApplyEndpointResponse401
    | PostFirewallVirtualIPApplyEndpointResponse403
    | PostFirewallVirtualIPApplyEndpointResponse404
    | PostFirewallVirtualIPApplyEndpointResponse405
    | PostFirewallVirtualIPApplyEndpointResponse406
    | PostFirewallVirtualIPApplyEndpointResponse409
    | PostFirewallVirtualIPApplyEndpointResponse415
    | PostFirewallVirtualIPApplyEndpointResponse422
    | PostFirewallVirtualIPApplyEndpointResponse424
    | PostFirewallVirtualIPApplyEndpointResponse500
    | PostFirewallVirtualIPApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending virtual IP changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIPApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostFirewallVirtualIPApplyEndpointJsonBody | Unset):
        body (PostFirewallVirtualIPApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallVirtualIPApplyEndpointResponse400 | PostFirewallVirtualIPApplyEndpointResponse401 | PostFirewallVirtualIPApplyEndpointResponse403 | PostFirewallVirtualIPApplyEndpointResponse404 | PostFirewallVirtualIPApplyEndpointResponse405 | PostFirewallVirtualIPApplyEndpointResponse406 | PostFirewallVirtualIPApplyEndpointResponse409 | PostFirewallVirtualIPApplyEndpointResponse415 | PostFirewallVirtualIPApplyEndpointResponse422 | PostFirewallVirtualIPApplyEndpointResponse424 | PostFirewallVirtualIPApplyEndpointResponse500 | PostFirewallVirtualIPApplyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallVirtualIPApplyEndpointJsonBody | PostFirewallVirtualIPApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallVirtualIPApplyEndpointResponse400
    | PostFirewallVirtualIPApplyEndpointResponse401
    | PostFirewallVirtualIPApplyEndpointResponse403
    | PostFirewallVirtualIPApplyEndpointResponse404
    | PostFirewallVirtualIPApplyEndpointResponse405
    | PostFirewallVirtualIPApplyEndpointResponse406
    | PostFirewallVirtualIPApplyEndpointResponse409
    | PostFirewallVirtualIPApplyEndpointResponse415
    | PostFirewallVirtualIPApplyEndpointResponse422
    | PostFirewallVirtualIPApplyEndpointResponse424
    | PostFirewallVirtualIPApplyEndpointResponse500
    | PostFirewallVirtualIPApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending virtual IP changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: VirtualIPApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-virtual-ip-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostFirewallVirtualIPApplyEndpointJsonBody | Unset):
        body (PostFirewallVirtualIPApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallVirtualIPApplyEndpointResponse400 | PostFirewallVirtualIPApplyEndpointResponse401 | PostFirewallVirtualIPApplyEndpointResponse403 | PostFirewallVirtualIPApplyEndpointResponse404 | PostFirewallVirtualIPApplyEndpointResponse405 | PostFirewallVirtualIPApplyEndpointResponse406 | PostFirewallVirtualIPApplyEndpointResponse409 | PostFirewallVirtualIPApplyEndpointResponse415 | PostFirewallVirtualIPApplyEndpointResponse422 | PostFirewallVirtualIPApplyEndpointResponse424 | PostFirewallVirtualIPApplyEndpointResponse500 | PostFirewallVirtualIPApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
