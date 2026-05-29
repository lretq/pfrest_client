from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_traffic_shaper_limiter_endpoint_data_body import (
    PostFirewallTrafficShaperLimiterEndpointDataBody,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_json_body import (
    PostFirewallTrafficShaperLimiterEndpointJsonBody,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_400 import (
    PostFirewallTrafficShaperLimiterEndpointResponse400,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_401 import (
    PostFirewallTrafficShaperLimiterEndpointResponse401,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_403 import (
    PostFirewallTrafficShaperLimiterEndpointResponse403,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_404 import (
    PostFirewallTrafficShaperLimiterEndpointResponse404,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_405 import (
    PostFirewallTrafficShaperLimiterEndpointResponse405,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_406 import (
    PostFirewallTrafficShaperLimiterEndpointResponse406,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_409 import (
    PostFirewallTrafficShaperLimiterEndpointResponse409,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_415 import (
    PostFirewallTrafficShaperLimiterEndpointResponse415,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_422 import (
    PostFirewallTrafficShaperLimiterEndpointResponse422,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_424 import (
    PostFirewallTrafficShaperLimiterEndpointResponse424,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_500 import (
    PostFirewallTrafficShaperLimiterEndpointResponse500,
)
from ...models.post_firewall_traffic_shaper_limiter_endpoint_response_503 import (
    PostFirewallTrafficShaperLimiterEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallTrafficShaperLimiterEndpointJsonBody
    | PostFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/traffic_shaper/limiter",
    }

    if isinstance(body, PostFirewallTrafficShaperLimiterEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallTrafficShaperLimiterEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallTrafficShaperLimiterEndpointResponse400
    | PostFirewallTrafficShaperLimiterEndpointResponse401
    | PostFirewallTrafficShaperLimiterEndpointResponse403
    | PostFirewallTrafficShaperLimiterEndpointResponse404
    | PostFirewallTrafficShaperLimiterEndpointResponse405
    | PostFirewallTrafficShaperLimiterEndpointResponse406
    | PostFirewallTrafficShaperLimiterEndpointResponse409
    | PostFirewallTrafficShaperLimiterEndpointResponse415
    | PostFirewallTrafficShaperLimiterEndpointResponse422
    | PostFirewallTrafficShaperLimiterEndpointResponse424
    | PostFirewallTrafficShaperLimiterEndpointResponse500
    | PostFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallTrafficShaperLimiterEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallTrafficShaperLimiterEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallTrafficShaperLimiterEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallTrafficShaperLimiterEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallTrafficShaperLimiterEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallTrafficShaperLimiterEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallTrafficShaperLimiterEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallTrafficShaperLimiterEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallTrafficShaperLimiterEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallTrafficShaperLimiterEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallTrafficShaperLimiterEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallTrafficShaperLimiterEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallTrafficShaperLimiterEndpointResponse400
    | PostFirewallTrafficShaperLimiterEndpointResponse401
    | PostFirewallTrafficShaperLimiterEndpointResponse403
    | PostFirewallTrafficShaperLimiterEndpointResponse404
    | PostFirewallTrafficShaperLimiterEndpointResponse405
    | PostFirewallTrafficShaperLimiterEndpointResponse406
    | PostFirewallTrafficShaperLimiterEndpointResponse409
    | PostFirewallTrafficShaperLimiterEndpointResponse415
    | PostFirewallTrafficShaperLimiterEndpointResponse422
    | PostFirewallTrafficShaperLimiterEndpointResponse424
    | PostFirewallTrafficShaperLimiterEndpointResponse500
    | PostFirewallTrafficShaperLimiterEndpointResponse503
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
    body: PostFirewallTrafficShaperLimiterEndpointJsonBody
    | PostFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperLimiterEndpointResponse400
    | PostFirewallTrafficShaperLimiterEndpointResponse401
    | PostFirewallTrafficShaperLimiterEndpointResponse403
    | PostFirewallTrafficShaperLimiterEndpointResponse404
    | PostFirewallTrafficShaperLimiterEndpointResponse405
    | PostFirewallTrafficShaperLimiterEndpointResponse406
    | PostFirewallTrafficShaperLimiterEndpointResponse409
    | PostFirewallTrafficShaperLimiterEndpointResponse415
    | PostFirewallTrafficShaperLimiterEndpointResponse422
    | PostFirewallTrafficShaperLimiterEndpointResponse424
    | PostFirewallTrafficShaperLimiterEndpointResponse500
    | PostFirewallTrafficShaperLimiterEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperLimiterEndpointResponse400 | PostFirewallTrafficShaperLimiterEndpointResponse401 | PostFirewallTrafficShaperLimiterEndpointResponse403 | PostFirewallTrafficShaperLimiterEndpointResponse404 | PostFirewallTrafficShaperLimiterEndpointResponse405 | PostFirewallTrafficShaperLimiterEndpointResponse406 | PostFirewallTrafficShaperLimiterEndpointResponse409 | PostFirewallTrafficShaperLimiterEndpointResponse415 | PostFirewallTrafficShaperLimiterEndpointResponse422 | PostFirewallTrafficShaperLimiterEndpointResponse424 | PostFirewallTrafficShaperLimiterEndpointResponse500 | PostFirewallTrafficShaperLimiterEndpointResponse503]
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
    body: PostFirewallTrafficShaperLimiterEndpointJsonBody
    | PostFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperLimiterEndpointResponse400
    | PostFirewallTrafficShaperLimiterEndpointResponse401
    | PostFirewallTrafficShaperLimiterEndpointResponse403
    | PostFirewallTrafficShaperLimiterEndpointResponse404
    | PostFirewallTrafficShaperLimiterEndpointResponse405
    | PostFirewallTrafficShaperLimiterEndpointResponse406
    | PostFirewallTrafficShaperLimiterEndpointResponse409
    | PostFirewallTrafficShaperLimiterEndpointResponse415
    | PostFirewallTrafficShaperLimiterEndpointResponse422
    | PostFirewallTrafficShaperLimiterEndpointResponse424
    | PostFirewallTrafficShaperLimiterEndpointResponse500
    | PostFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperLimiterEndpointResponse400 | PostFirewallTrafficShaperLimiterEndpointResponse401 | PostFirewallTrafficShaperLimiterEndpointResponse403 | PostFirewallTrafficShaperLimiterEndpointResponse404 | PostFirewallTrafficShaperLimiterEndpointResponse405 | PostFirewallTrafficShaperLimiterEndpointResponse406 | PostFirewallTrafficShaperLimiterEndpointResponse409 | PostFirewallTrafficShaperLimiterEndpointResponse415 | PostFirewallTrafficShaperLimiterEndpointResponse422 | PostFirewallTrafficShaperLimiterEndpointResponse424 | PostFirewallTrafficShaperLimiterEndpointResponse500 | PostFirewallTrafficShaperLimiterEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperLimiterEndpointJsonBody
    | PostFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperLimiterEndpointResponse400
    | PostFirewallTrafficShaperLimiterEndpointResponse401
    | PostFirewallTrafficShaperLimiterEndpointResponse403
    | PostFirewallTrafficShaperLimiterEndpointResponse404
    | PostFirewallTrafficShaperLimiterEndpointResponse405
    | PostFirewallTrafficShaperLimiterEndpointResponse406
    | PostFirewallTrafficShaperLimiterEndpointResponse409
    | PostFirewallTrafficShaperLimiterEndpointResponse415
    | PostFirewallTrafficShaperLimiterEndpointResponse422
    | PostFirewallTrafficShaperLimiterEndpointResponse424
    | PostFirewallTrafficShaperLimiterEndpointResponse500
    | PostFirewallTrafficShaperLimiterEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperLimiterEndpointResponse400 | PostFirewallTrafficShaperLimiterEndpointResponse401 | PostFirewallTrafficShaperLimiterEndpointResponse403 | PostFirewallTrafficShaperLimiterEndpointResponse404 | PostFirewallTrafficShaperLimiterEndpointResponse405 | PostFirewallTrafficShaperLimiterEndpointResponse406 | PostFirewallTrafficShaperLimiterEndpointResponse409 | PostFirewallTrafficShaperLimiterEndpointResponse415 | PostFirewallTrafficShaperLimiterEndpointResponse422 | PostFirewallTrafficShaperLimiterEndpointResponse424 | PostFirewallTrafficShaperLimiterEndpointResponse500 | PostFirewallTrafficShaperLimiterEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperLimiterEndpointJsonBody
    | PostFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperLimiterEndpointResponse400
    | PostFirewallTrafficShaperLimiterEndpointResponse401
    | PostFirewallTrafficShaperLimiterEndpointResponse403
    | PostFirewallTrafficShaperLimiterEndpointResponse404
    | PostFirewallTrafficShaperLimiterEndpointResponse405
    | PostFirewallTrafficShaperLimiterEndpointResponse406
    | PostFirewallTrafficShaperLimiterEndpointResponse409
    | PostFirewallTrafficShaperLimiterEndpointResponse415
    | PostFirewallTrafficShaperLimiterEndpointResponse422
    | PostFirewallTrafficShaperLimiterEndpointResponse424
    | PostFirewallTrafficShaperLimiterEndpointResponse500
    | PostFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallTrafficShaperLimiterEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperLimiterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperLimiterEndpointResponse400 | PostFirewallTrafficShaperLimiterEndpointResponse401 | PostFirewallTrafficShaperLimiterEndpointResponse403 | PostFirewallTrafficShaperLimiterEndpointResponse404 | PostFirewallTrafficShaperLimiterEndpointResponse405 | PostFirewallTrafficShaperLimiterEndpointResponse406 | PostFirewallTrafficShaperLimiterEndpointResponse409 | PostFirewallTrafficShaperLimiterEndpointResponse415 | PostFirewallTrafficShaperLimiterEndpointResponse422 | PostFirewallTrafficShaperLimiterEndpointResponse424 | PostFirewallTrafficShaperLimiterEndpointResponse500 | PostFirewallTrafficShaperLimiterEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
