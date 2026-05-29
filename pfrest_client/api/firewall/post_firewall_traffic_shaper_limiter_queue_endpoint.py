from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_data_body import (
    PostFirewallTrafficShaperLimiterQueueEndpointDataBody,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_json_body import (
    PostFirewallTrafficShaperLimiterQueueEndpointJsonBody,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_400 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse400,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_401 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse401,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_403 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse403,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_404 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse404,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_405 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse405,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_406 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse406,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_409 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse409,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_415 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse415,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_422 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse422,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_424 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse424,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_500 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse500,
)
from ...models.post_firewall_traffic_shaper_limiter_queue_endpoint_response_503 import (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PostFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/traffic_shaper/limiter/queue",
    }

    if isinstance(body, PostFirewallTrafficShaperLimiterQueueEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallTrafficShaperLimiterQueueEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallTrafficShaperLimiterQueueEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallTrafficShaperLimiterQueueEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallTrafficShaperLimiterQueueEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallTrafficShaperLimiterQueueEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallTrafficShaperLimiterQueueEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallTrafficShaperLimiterQueueEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallTrafficShaperLimiterQueueEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallTrafficShaperLimiterQueueEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallTrafficShaperLimiterQueueEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallTrafficShaperLimiterQueueEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallTrafficShaperLimiterQueueEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallTrafficShaperLimiterQueueEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse503
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
    body: PostFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PostFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterQueue<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-queue-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterQueueEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperLimiterQueueEndpointResponse400 | PostFirewallTrafficShaperLimiterQueueEndpointResponse401 | PostFirewallTrafficShaperLimiterQueueEndpointResponse403 | PostFirewallTrafficShaperLimiterQueueEndpointResponse404 | PostFirewallTrafficShaperLimiterQueueEndpointResponse405 | PostFirewallTrafficShaperLimiterQueueEndpointResponse406 | PostFirewallTrafficShaperLimiterQueueEndpointResponse409 | PostFirewallTrafficShaperLimiterQueueEndpointResponse415 | PostFirewallTrafficShaperLimiterQueueEndpointResponse422 | PostFirewallTrafficShaperLimiterQueueEndpointResponse424 | PostFirewallTrafficShaperLimiterQueueEndpointResponse500 | PostFirewallTrafficShaperLimiterQueueEndpointResponse503]
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
    body: PostFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PostFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterQueue<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-queue-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterQueueEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperLimiterQueueEndpointResponse400 | PostFirewallTrafficShaperLimiterQueueEndpointResponse401 | PostFirewallTrafficShaperLimiterQueueEndpointResponse403 | PostFirewallTrafficShaperLimiterQueueEndpointResponse404 | PostFirewallTrafficShaperLimiterQueueEndpointResponse405 | PostFirewallTrafficShaperLimiterQueueEndpointResponse406 | PostFirewallTrafficShaperLimiterQueueEndpointResponse409 | PostFirewallTrafficShaperLimiterQueueEndpointResponse415 | PostFirewallTrafficShaperLimiterQueueEndpointResponse422 | PostFirewallTrafficShaperLimiterQueueEndpointResponse424 | PostFirewallTrafficShaperLimiterQueueEndpointResponse500 | PostFirewallTrafficShaperLimiterQueueEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PostFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterQueue<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-queue-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterQueueEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperLimiterQueueEndpointResponse400 | PostFirewallTrafficShaperLimiterQueueEndpointResponse401 | PostFirewallTrafficShaperLimiterQueueEndpointResponse403 | PostFirewallTrafficShaperLimiterQueueEndpointResponse404 | PostFirewallTrafficShaperLimiterQueueEndpointResponse405 | PostFirewallTrafficShaperLimiterQueueEndpointResponse406 | PostFirewallTrafficShaperLimiterQueueEndpointResponse409 | PostFirewallTrafficShaperLimiterQueueEndpointResponse415 | PostFirewallTrafficShaperLimiterQueueEndpointResponse422 | PostFirewallTrafficShaperLimiterQueueEndpointResponse424 | PostFirewallTrafficShaperLimiterQueueEndpointResponse500 | PostFirewallTrafficShaperLimiterQueueEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PostFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PostFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterQueue<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-queue-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterQueueEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperLimiterQueueEndpointResponse400 | PostFirewallTrafficShaperLimiterQueueEndpointResponse401 | PostFirewallTrafficShaperLimiterQueueEndpointResponse403 | PostFirewallTrafficShaperLimiterQueueEndpointResponse404 | PostFirewallTrafficShaperLimiterQueueEndpointResponse405 | PostFirewallTrafficShaperLimiterQueueEndpointResponse406 | PostFirewallTrafficShaperLimiterQueueEndpointResponse409 | PostFirewallTrafficShaperLimiterQueueEndpointResponse415 | PostFirewallTrafficShaperLimiterQueueEndpointResponse422 | PostFirewallTrafficShaperLimiterQueueEndpointResponse424 | PostFirewallTrafficShaperLimiterQueueEndpointResponse500 | PostFirewallTrafficShaperLimiterQueueEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
