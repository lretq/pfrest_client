from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_400 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_401 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_403 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_404 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_405 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_406 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_409 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_415 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_422 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_424 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_500 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500,
)
from ...models.delete_firewall_traffic_shaper_limiter_bandwidth_endpoint_response_503 import (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/firewall/traffic_shaper/limiter/bandwidth",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Traffic Shaper Limiter
    Bandwidth.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterBandwidth<br>**Parent model**: TrafficShaperLimiter<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-bandwidth-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Traffic Shaper Limiter
    Bandwidth.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterBandwidth<br>**Parent model**: TrafficShaperLimiter<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-bandwidth-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Traffic Shaper Limiter
    Bandwidth.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterBandwidth<br>**Parent model**: TrafficShaperLimiter<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-bandwidth-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Traffic Shaper Limiter
    Bandwidth.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterBandwidth<br>**Parent model**: TrafficShaperLimiter<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-bandwidth-delete
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse400 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse401 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse403 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse404 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse405 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse406 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse409 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse415 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse422 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse424 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse500 | DeleteFirewallTrafficShaperLimiterBandwidthEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
