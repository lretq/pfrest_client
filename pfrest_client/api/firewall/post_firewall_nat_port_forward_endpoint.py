from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_nat_port_forward_endpoint_data_body import PostFirewallNATPortForwardEndpointDataBody
from ...models.post_firewall_nat_port_forward_endpoint_json_body import PostFirewallNATPortForwardEndpointJsonBody
from ...models.post_firewall_nat_port_forward_endpoint_response_400 import PostFirewallNATPortForwardEndpointResponse400
from ...models.post_firewall_nat_port_forward_endpoint_response_401 import PostFirewallNATPortForwardEndpointResponse401
from ...models.post_firewall_nat_port_forward_endpoint_response_403 import PostFirewallNATPortForwardEndpointResponse403
from ...models.post_firewall_nat_port_forward_endpoint_response_404 import PostFirewallNATPortForwardEndpointResponse404
from ...models.post_firewall_nat_port_forward_endpoint_response_405 import PostFirewallNATPortForwardEndpointResponse405
from ...models.post_firewall_nat_port_forward_endpoint_response_406 import PostFirewallNATPortForwardEndpointResponse406
from ...models.post_firewall_nat_port_forward_endpoint_response_409 import PostFirewallNATPortForwardEndpointResponse409
from ...models.post_firewall_nat_port_forward_endpoint_response_415 import PostFirewallNATPortForwardEndpointResponse415
from ...models.post_firewall_nat_port_forward_endpoint_response_422 import PostFirewallNATPortForwardEndpointResponse422
from ...models.post_firewall_nat_port_forward_endpoint_response_424 import PostFirewallNATPortForwardEndpointResponse424
from ...models.post_firewall_nat_port_forward_endpoint_response_500 import PostFirewallNATPortForwardEndpointResponse500
from ...models.post_firewall_nat_port_forward_endpoint_response_503 import PostFirewallNATPortForwardEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallNATPortForwardEndpointJsonBody | PostFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/nat/port_forward",
    }

    if isinstance(body, PostFirewallNATPortForwardEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallNATPortForwardEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallNATPortForwardEndpointResponse400
    | PostFirewallNATPortForwardEndpointResponse401
    | PostFirewallNATPortForwardEndpointResponse403
    | PostFirewallNATPortForwardEndpointResponse404
    | PostFirewallNATPortForwardEndpointResponse405
    | PostFirewallNATPortForwardEndpointResponse406
    | PostFirewallNATPortForwardEndpointResponse409
    | PostFirewallNATPortForwardEndpointResponse415
    | PostFirewallNATPortForwardEndpointResponse422
    | PostFirewallNATPortForwardEndpointResponse424
    | PostFirewallNATPortForwardEndpointResponse500
    | PostFirewallNATPortForwardEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallNATPortForwardEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallNATPortForwardEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallNATPortForwardEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallNATPortForwardEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallNATPortForwardEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallNATPortForwardEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallNATPortForwardEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallNATPortForwardEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallNATPortForwardEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallNATPortForwardEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallNATPortForwardEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallNATPortForwardEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallNATPortForwardEndpointResponse400
    | PostFirewallNATPortForwardEndpointResponse401
    | PostFirewallNATPortForwardEndpointResponse403
    | PostFirewallNATPortForwardEndpointResponse404
    | PostFirewallNATPortForwardEndpointResponse405
    | PostFirewallNATPortForwardEndpointResponse406
    | PostFirewallNATPortForwardEndpointResponse409
    | PostFirewallNATPortForwardEndpointResponse415
    | PostFirewallNATPortForwardEndpointResponse422
    | PostFirewallNATPortForwardEndpointResponse424
    | PostFirewallNATPortForwardEndpointResponse500
    | PostFirewallNATPortForwardEndpointResponse503
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
    body: PostFirewallNATPortForwardEndpointJsonBody | PostFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallNATPortForwardEndpointResponse400
    | PostFirewallNATPortForwardEndpointResponse401
    | PostFirewallNATPortForwardEndpointResponse403
    | PostFirewallNATPortForwardEndpointResponse404
    | PostFirewallNATPortForwardEndpointResponse405
    | PostFirewallNATPortForwardEndpointResponse406
    | PostFirewallNATPortForwardEndpointResponse409
    | PostFirewallNATPortForwardEndpointResponse415
    | PostFirewallNATPortForwardEndpointResponse422
    | PostFirewallNATPortForwardEndpointResponse424
    | PostFirewallNATPortForwardEndpointResponse500
    | PostFirewallNATPortForwardEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Port Forward.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forward-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallNATPortForwardEndpointJsonBody | Unset):
        body (PostFirewallNATPortForwardEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallNATPortForwardEndpointResponse400 | PostFirewallNATPortForwardEndpointResponse401 | PostFirewallNATPortForwardEndpointResponse403 | PostFirewallNATPortForwardEndpointResponse404 | PostFirewallNATPortForwardEndpointResponse405 | PostFirewallNATPortForwardEndpointResponse406 | PostFirewallNATPortForwardEndpointResponse409 | PostFirewallNATPortForwardEndpointResponse415 | PostFirewallNATPortForwardEndpointResponse422 | PostFirewallNATPortForwardEndpointResponse424 | PostFirewallNATPortForwardEndpointResponse500 | PostFirewallNATPortForwardEndpointResponse503]
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
    body: PostFirewallNATPortForwardEndpointJsonBody | PostFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallNATPortForwardEndpointResponse400
    | PostFirewallNATPortForwardEndpointResponse401
    | PostFirewallNATPortForwardEndpointResponse403
    | PostFirewallNATPortForwardEndpointResponse404
    | PostFirewallNATPortForwardEndpointResponse405
    | PostFirewallNATPortForwardEndpointResponse406
    | PostFirewallNATPortForwardEndpointResponse409
    | PostFirewallNATPortForwardEndpointResponse415
    | PostFirewallNATPortForwardEndpointResponse422
    | PostFirewallNATPortForwardEndpointResponse424
    | PostFirewallNATPortForwardEndpointResponse500
    | PostFirewallNATPortForwardEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Port Forward.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forward-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallNATPortForwardEndpointJsonBody | Unset):
        body (PostFirewallNATPortForwardEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallNATPortForwardEndpointResponse400 | PostFirewallNATPortForwardEndpointResponse401 | PostFirewallNATPortForwardEndpointResponse403 | PostFirewallNATPortForwardEndpointResponse404 | PostFirewallNATPortForwardEndpointResponse405 | PostFirewallNATPortForwardEndpointResponse406 | PostFirewallNATPortForwardEndpointResponse409 | PostFirewallNATPortForwardEndpointResponse415 | PostFirewallNATPortForwardEndpointResponse422 | PostFirewallNATPortForwardEndpointResponse424 | PostFirewallNATPortForwardEndpointResponse500 | PostFirewallNATPortForwardEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallNATPortForwardEndpointJsonBody | PostFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallNATPortForwardEndpointResponse400
    | PostFirewallNATPortForwardEndpointResponse401
    | PostFirewallNATPortForwardEndpointResponse403
    | PostFirewallNATPortForwardEndpointResponse404
    | PostFirewallNATPortForwardEndpointResponse405
    | PostFirewallNATPortForwardEndpointResponse406
    | PostFirewallNATPortForwardEndpointResponse409
    | PostFirewallNATPortForwardEndpointResponse415
    | PostFirewallNATPortForwardEndpointResponse422
    | PostFirewallNATPortForwardEndpointResponse424
    | PostFirewallNATPortForwardEndpointResponse500
    | PostFirewallNATPortForwardEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Port Forward.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forward-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallNATPortForwardEndpointJsonBody | Unset):
        body (PostFirewallNATPortForwardEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallNATPortForwardEndpointResponse400 | PostFirewallNATPortForwardEndpointResponse401 | PostFirewallNATPortForwardEndpointResponse403 | PostFirewallNATPortForwardEndpointResponse404 | PostFirewallNATPortForwardEndpointResponse405 | PostFirewallNATPortForwardEndpointResponse406 | PostFirewallNATPortForwardEndpointResponse409 | PostFirewallNATPortForwardEndpointResponse415 | PostFirewallNATPortForwardEndpointResponse422 | PostFirewallNATPortForwardEndpointResponse424 | PostFirewallNATPortForwardEndpointResponse500 | PostFirewallNATPortForwardEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallNATPortForwardEndpointJsonBody | PostFirewallNATPortForwardEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallNATPortForwardEndpointResponse400
    | PostFirewallNATPortForwardEndpointResponse401
    | PostFirewallNATPortForwardEndpointResponse403
    | PostFirewallNATPortForwardEndpointResponse404
    | PostFirewallNATPortForwardEndpointResponse405
    | PostFirewallNATPortForwardEndpointResponse406
    | PostFirewallNATPortForwardEndpointResponse409
    | PostFirewallNATPortForwardEndpointResponse415
    | PostFirewallNATPortForwardEndpointResponse422
    | PostFirewallNATPortForwardEndpointResponse424
    | PostFirewallNATPortForwardEndpointResponse500
    | PostFirewallNATPortForwardEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Port Forward.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forward-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallNATPortForwardEndpointJsonBody | Unset):
        body (PostFirewallNATPortForwardEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallNATPortForwardEndpointResponse400 | PostFirewallNATPortForwardEndpointResponse401 | PostFirewallNATPortForwardEndpointResponse403 | PostFirewallNATPortForwardEndpointResponse404 | PostFirewallNATPortForwardEndpointResponse405 | PostFirewallNATPortForwardEndpointResponse406 | PostFirewallNATPortForwardEndpointResponse409 | PostFirewallNATPortForwardEndpointResponse415 | PostFirewallNATPortForwardEndpointResponse422 | PostFirewallNATPortForwardEndpointResponse424 | PostFirewallNATPortForwardEndpointResponse500 | PostFirewallNATPortForwardEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
