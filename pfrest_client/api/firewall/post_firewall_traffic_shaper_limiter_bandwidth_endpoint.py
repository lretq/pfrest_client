from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_data_body import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_json_body import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_400 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_401 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_403 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_404 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_405 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_406 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_409 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_415 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_422 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_424 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_500 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500,
)
from ...models.post_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_503 import (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/traffic_shaper/limiter/bandwidth",
    }

    if isinstance(body, PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503
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
    body: PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter Bandwidth.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterBandwidth<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-bandwidth-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503]
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
    body: PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter Bandwidth.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterBandwidth<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-bandwidth-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter Bandwidth.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterBandwidth<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-bandwidth-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter Bandwidth.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterBandwidth<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-bandwidth-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterBandwidthEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | PostFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
