from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_traffic_shaper_endpoint_data_body import PostFirewallTrafficShaperEndpointDataBody
from ...models.post_firewall_traffic_shaper_endpoint_json_body import PostFirewallTrafficShaperEndpointJsonBody
from ...models.post_firewall_traffic_shaper_endpoint_response_400 import PostFirewallTrafficShaperEndpointResponse400
from ...models.post_firewall_traffic_shaper_endpoint_response_401 import PostFirewallTrafficShaperEndpointResponse401
from ...models.post_firewall_traffic_shaper_endpoint_response_403 import PostFirewallTrafficShaperEndpointResponse403
from ...models.post_firewall_traffic_shaper_endpoint_response_404 import PostFirewallTrafficShaperEndpointResponse404
from ...models.post_firewall_traffic_shaper_endpoint_response_405 import PostFirewallTrafficShaperEndpointResponse405
from ...models.post_firewall_traffic_shaper_endpoint_response_406 import PostFirewallTrafficShaperEndpointResponse406
from ...models.post_firewall_traffic_shaper_endpoint_response_409 import PostFirewallTrafficShaperEndpointResponse409
from ...models.post_firewall_traffic_shaper_endpoint_response_415 import PostFirewallTrafficShaperEndpointResponse415
from ...models.post_firewall_traffic_shaper_endpoint_response_422 import PostFirewallTrafficShaperEndpointResponse422
from ...models.post_firewall_traffic_shaper_endpoint_response_424 import PostFirewallTrafficShaperEndpointResponse424
from ...models.post_firewall_traffic_shaper_endpoint_response_500 import PostFirewallTrafficShaperEndpointResponse500
from ...models.post_firewall_traffic_shaper_endpoint_response_503 import PostFirewallTrafficShaperEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallTrafficShaperEndpointJsonBody | PostFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/traffic_shaper",
    }

    if isinstance(body, PostFirewallTrafficShaperEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallTrafficShaperEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallTrafficShaperEndpointResponse400
    | PostFirewallTrafficShaperEndpointResponse401
    | PostFirewallTrafficShaperEndpointResponse403
    | PostFirewallTrafficShaperEndpointResponse404
    | PostFirewallTrafficShaperEndpointResponse405
    | PostFirewallTrafficShaperEndpointResponse406
    | PostFirewallTrafficShaperEndpointResponse409
    | PostFirewallTrafficShaperEndpointResponse415
    | PostFirewallTrafficShaperEndpointResponse422
    | PostFirewallTrafficShaperEndpointResponse424
    | PostFirewallTrafficShaperEndpointResponse500
    | PostFirewallTrafficShaperEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallTrafficShaperEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallTrafficShaperEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallTrafficShaperEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallTrafficShaperEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallTrafficShaperEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallTrafficShaperEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallTrafficShaperEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallTrafficShaperEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallTrafficShaperEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallTrafficShaperEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallTrafficShaperEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallTrafficShaperEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallTrafficShaperEndpointResponse400
    | PostFirewallTrafficShaperEndpointResponse401
    | PostFirewallTrafficShaperEndpointResponse403
    | PostFirewallTrafficShaperEndpointResponse404
    | PostFirewallTrafficShaperEndpointResponse405
    | PostFirewallTrafficShaperEndpointResponse406
    | PostFirewallTrafficShaperEndpointResponse409
    | PostFirewallTrafficShaperEndpointResponse415
    | PostFirewallTrafficShaperEndpointResponse422
    | PostFirewallTrafficShaperEndpointResponse424
    | PostFirewallTrafficShaperEndpointResponse500
    | PostFirewallTrafficShaperEndpointResponse503
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
    body: PostFirewallTrafficShaperEndpointJsonBody | PostFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperEndpointResponse400
    | PostFirewallTrafficShaperEndpointResponse401
    | PostFirewallTrafficShaperEndpointResponse403
    | PostFirewallTrafficShaperEndpointResponse404
    | PostFirewallTrafficShaperEndpointResponse405
    | PostFirewallTrafficShaperEndpointResponse406
    | PostFirewallTrafficShaperEndpointResponse409
    | PostFirewallTrafficShaperEndpointResponse415
    | PostFirewallTrafficShaperEndpointResponse422
    | PostFirewallTrafficShaperEndpointResponse424
    | PostFirewallTrafficShaperEndpointResponse500
    | PostFirewallTrafficShaperEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperEndpointResponse400 | PostFirewallTrafficShaperEndpointResponse401 | PostFirewallTrafficShaperEndpointResponse403 | PostFirewallTrafficShaperEndpointResponse404 | PostFirewallTrafficShaperEndpointResponse405 | PostFirewallTrafficShaperEndpointResponse406 | PostFirewallTrafficShaperEndpointResponse409 | PostFirewallTrafficShaperEndpointResponse415 | PostFirewallTrafficShaperEndpointResponse422 | PostFirewallTrafficShaperEndpointResponse424 | PostFirewallTrafficShaperEndpointResponse500 | PostFirewallTrafficShaperEndpointResponse503]
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
    body: PostFirewallTrafficShaperEndpointJsonBody | PostFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperEndpointResponse400
    | PostFirewallTrafficShaperEndpointResponse401
    | PostFirewallTrafficShaperEndpointResponse403
    | PostFirewallTrafficShaperEndpointResponse404
    | PostFirewallTrafficShaperEndpointResponse405
    | PostFirewallTrafficShaperEndpointResponse406
    | PostFirewallTrafficShaperEndpointResponse409
    | PostFirewallTrafficShaperEndpointResponse415
    | PostFirewallTrafficShaperEndpointResponse422
    | PostFirewallTrafficShaperEndpointResponse424
    | PostFirewallTrafficShaperEndpointResponse500
    | PostFirewallTrafficShaperEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperEndpointResponse400 | PostFirewallTrafficShaperEndpointResponse401 | PostFirewallTrafficShaperEndpointResponse403 | PostFirewallTrafficShaperEndpointResponse404 | PostFirewallTrafficShaperEndpointResponse405 | PostFirewallTrafficShaperEndpointResponse406 | PostFirewallTrafficShaperEndpointResponse409 | PostFirewallTrafficShaperEndpointResponse415 | PostFirewallTrafficShaperEndpointResponse422 | PostFirewallTrafficShaperEndpointResponse424 | PostFirewallTrafficShaperEndpointResponse500 | PostFirewallTrafficShaperEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperEndpointJsonBody | PostFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperEndpointResponse400
    | PostFirewallTrafficShaperEndpointResponse401
    | PostFirewallTrafficShaperEndpointResponse403
    | PostFirewallTrafficShaperEndpointResponse404
    | PostFirewallTrafficShaperEndpointResponse405
    | PostFirewallTrafficShaperEndpointResponse406
    | PostFirewallTrafficShaperEndpointResponse409
    | PostFirewallTrafficShaperEndpointResponse415
    | PostFirewallTrafficShaperEndpointResponse422
    | PostFirewallTrafficShaperEndpointResponse424
    | PostFirewallTrafficShaperEndpointResponse500
    | PostFirewallTrafficShaperEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperEndpointResponse400 | PostFirewallTrafficShaperEndpointResponse401 | PostFirewallTrafficShaperEndpointResponse403 | PostFirewallTrafficShaperEndpointResponse404 | PostFirewallTrafficShaperEndpointResponse405 | PostFirewallTrafficShaperEndpointResponse406 | PostFirewallTrafficShaperEndpointResponse409 | PostFirewallTrafficShaperEndpointResponse415 | PostFirewallTrafficShaperEndpointResponse422 | PostFirewallTrafficShaperEndpointResponse424 | PostFirewallTrafficShaperEndpointResponse500 | PostFirewallTrafficShaperEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperEndpointJsonBody | PostFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperEndpointResponse400
    | PostFirewallTrafficShaperEndpointResponse401
    | PostFirewallTrafficShaperEndpointResponse403
    | PostFirewallTrafficShaperEndpointResponse404
    | PostFirewallTrafficShaperEndpointResponse405
    | PostFirewallTrafficShaperEndpointResponse406
    | PostFirewallTrafficShaperEndpointResponse409
    | PostFirewallTrafficShaperEndpointResponse415
    | PostFirewallTrafficShaperEndpointResponse422
    | PostFirewallTrafficShaperEndpointResponse424
    | PostFirewallTrafficShaperEndpointResponse500
    | PostFirewallTrafficShaperEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperEndpointResponse400 | PostFirewallTrafficShaperEndpointResponse401 | PostFirewallTrafficShaperEndpointResponse403 | PostFirewallTrafficShaperEndpointResponse404 | PostFirewallTrafficShaperEndpointResponse405 | PostFirewallTrafficShaperEndpointResponse406 | PostFirewallTrafficShaperEndpointResponse409 | PostFirewallTrafficShaperEndpointResponse415 | PostFirewallTrafficShaperEndpointResponse422 | PostFirewallTrafficShaperEndpointResponse424 | PostFirewallTrafficShaperEndpointResponse500 | PostFirewallTrafficShaperEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
