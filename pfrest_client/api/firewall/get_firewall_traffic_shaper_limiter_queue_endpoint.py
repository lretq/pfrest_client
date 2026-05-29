from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_400 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse400,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_401 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse401,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_403 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse403,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_404 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse404,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_405 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse405,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_406 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse406,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_409 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse409,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_415 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse415,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_422 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse422,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_424 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse424,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_500 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse500,
)
from ...models.get_firewall_traffic_shaper_limiter_queue_endpoint_response_503 import (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse503,
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
        "method": "get",
        "url": "/api/v2/firewall/traffic_shaper/limiter/queue",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFirewallTrafficShaperLimiterQueueEndpointResponse400
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse401
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse403
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse404
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse405
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse406
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse409
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse415
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse422
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse424
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse500
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetFirewallTrafficShaperLimiterQueueEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFirewallTrafficShaperLimiterQueueEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFirewallTrafficShaperLimiterQueueEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFirewallTrafficShaperLimiterQueueEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetFirewallTrafficShaperLimiterQueueEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetFirewallTrafficShaperLimiterQueueEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetFirewallTrafficShaperLimiterQueueEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetFirewallTrafficShaperLimiterQueueEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetFirewallTrafficShaperLimiterQueueEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetFirewallTrafficShaperLimiterQueueEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetFirewallTrafficShaperLimiterQueueEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetFirewallTrafficShaperLimiterQueueEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFirewallTrafficShaperLimiterQueueEndpointResponse400
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse401
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse403
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse404
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse405
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse406
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse409
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse415
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse422
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse424
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse500
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse503
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
    GetFirewallTrafficShaperLimiterQueueEndpointResponse400
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse401
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse403
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse404
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse405
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse406
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse409
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse415
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse422
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse424
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse500
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Traffic Shaper Limiter Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterQueue<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-queue-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallTrafficShaperLimiterQueueEndpointResponse400 | GetFirewallTrafficShaperLimiterQueueEndpointResponse401 | GetFirewallTrafficShaperLimiterQueueEndpointResponse403 | GetFirewallTrafficShaperLimiterQueueEndpointResponse404 | GetFirewallTrafficShaperLimiterQueueEndpointResponse405 | GetFirewallTrafficShaperLimiterQueueEndpointResponse406 | GetFirewallTrafficShaperLimiterQueueEndpointResponse409 | GetFirewallTrafficShaperLimiterQueueEndpointResponse415 | GetFirewallTrafficShaperLimiterQueueEndpointResponse422 | GetFirewallTrafficShaperLimiterQueueEndpointResponse424 | GetFirewallTrafficShaperLimiterQueueEndpointResponse500 | GetFirewallTrafficShaperLimiterQueueEndpointResponse503]
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
    GetFirewallTrafficShaperLimiterQueueEndpointResponse400
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse401
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse403
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse404
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse405
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse406
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse409
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse415
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse422
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse424
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse500
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Traffic Shaper Limiter Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterQueue<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-queue-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallTrafficShaperLimiterQueueEndpointResponse400 | GetFirewallTrafficShaperLimiterQueueEndpointResponse401 | GetFirewallTrafficShaperLimiterQueueEndpointResponse403 | GetFirewallTrafficShaperLimiterQueueEndpointResponse404 | GetFirewallTrafficShaperLimiterQueueEndpointResponse405 | GetFirewallTrafficShaperLimiterQueueEndpointResponse406 | GetFirewallTrafficShaperLimiterQueueEndpointResponse409 | GetFirewallTrafficShaperLimiterQueueEndpointResponse415 | GetFirewallTrafficShaperLimiterQueueEndpointResponse422 | GetFirewallTrafficShaperLimiterQueueEndpointResponse424 | GetFirewallTrafficShaperLimiterQueueEndpointResponse500 | GetFirewallTrafficShaperLimiterQueueEndpointResponse503
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
    GetFirewallTrafficShaperLimiterQueueEndpointResponse400
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse401
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse403
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse404
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse405
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse406
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse409
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse415
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse422
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse424
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse500
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Traffic Shaper Limiter Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterQueue<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-queue-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallTrafficShaperLimiterQueueEndpointResponse400 | GetFirewallTrafficShaperLimiterQueueEndpointResponse401 | GetFirewallTrafficShaperLimiterQueueEndpointResponse403 | GetFirewallTrafficShaperLimiterQueueEndpointResponse404 | GetFirewallTrafficShaperLimiterQueueEndpointResponse405 | GetFirewallTrafficShaperLimiterQueueEndpointResponse406 | GetFirewallTrafficShaperLimiterQueueEndpointResponse409 | GetFirewallTrafficShaperLimiterQueueEndpointResponse415 | GetFirewallTrafficShaperLimiterQueueEndpointResponse422 | GetFirewallTrafficShaperLimiterQueueEndpointResponse424 | GetFirewallTrafficShaperLimiterQueueEndpointResponse500 | GetFirewallTrafficShaperLimiterQueueEndpointResponse503]
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
    GetFirewallTrafficShaperLimiterQueueEndpointResponse400
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse401
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse403
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse404
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse405
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse406
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse409
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse415
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse422
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse424
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse500
    | GetFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Traffic Shaper Limiter Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiterQueue<br>**Parent model**:
    TrafficShaperLimiter<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    limiter-queue-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallTrafficShaperLimiterQueueEndpointResponse400 | GetFirewallTrafficShaperLimiterQueueEndpointResponse401 | GetFirewallTrafficShaperLimiterQueueEndpointResponse403 | GetFirewallTrafficShaperLimiterQueueEndpointResponse404 | GetFirewallTrafficShaperLimiterQueueEndpointResponse405 | GetFirewallTrafficShaperLimiterQueueEndpointResponse406 | GetFirewallTrafficShaperLimiterQueueEndpointResponse409 | GetFirewallTrafficShaperLimiterQueueEndpointResponse415 | GetFirewallTrafficShaperLimiterQueueEndpointResponse422 | GetFirewallTrafficShaperLimiterQueueEndpointResponse424 | GetFirewallTrafficShaperLimiterQueueEndpointResponse500 | GetFirewallTrafficShaperLimiterQueueEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
