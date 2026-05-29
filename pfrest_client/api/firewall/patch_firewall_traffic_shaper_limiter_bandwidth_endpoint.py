from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_data_body import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_json_body import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_400 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_401 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_403 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_404 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_405 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_406 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_409 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_415 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_422 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_424 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_500 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500,
)
from ...models.patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_503 import (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/traffic_shaper/limiter/bandwidth",
    }

    if isinstance(body, PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503
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
    body: PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter
    Bandwidth.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterBandwidth<br>**Parent model**: TrafficShaperLimiter<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-bandwidth-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503]
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
    body: PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter
    Bandwidth.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterBandwidth<br>**Parent model**: TrafficShaperLimiter<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-bandwidth-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter
    Bandwidth.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterBandwidth<br>**Parent model**: TrafficShaperLimiter<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-bandwidth-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter
    Bandwidth.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterBandwidth<br>**Parent model**: TrafficShaperLimiter<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-bandwidth-patch
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperLimiterBandwidthEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | PatchFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
