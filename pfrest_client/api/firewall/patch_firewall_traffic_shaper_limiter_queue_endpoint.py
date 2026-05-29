from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_data_body import (
    PatchFirewallTrafficShaperLimiterQueueEndpointDataBody,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_json_body import (
    PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_400 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse400,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_401 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse401,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_403 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse403,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_404 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse404,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_405 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse405,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_406 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse406,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_409 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse409,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_415 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse415,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_422 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse422,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_424 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse424,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_500 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse500,
)
from ...models.patch_firewall_traffic_shaper_limiter_queue_endpoint_response_503 import (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/traffic_shaper/limiter/queue",
    }

    if isinstance(body, PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallTrafficShaperLimiterQueueEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallTrafficShaperLimiterQueueEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503
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
    body: PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter
    Queue.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterQueue<br>**Parent model**: TrafficShaperLimiter<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-queue-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperLimiterQueueEndpointResponse400 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503]
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
    body: PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter
    Queue.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterQueue<br>**Parent model**: TrafficShaperLimiter<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-queue-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperLimiterQueueEndpointResponse400 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter
    Queue.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterQueue<br>**Parent model**: TrafficShaperLimiter<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-queue-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperLimiterQueueEndpointResponse400 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterQueueEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperLimiterQueueEndpointResponse400
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500
    | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter
    Queue.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    TrafficShaperLimiterQueue<br>**Parent model**: TrafficShaperLimiter<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-queue-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperLimiterQueueEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperLimiterQueueEndpointResponse400 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse401 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse403 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse404 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse405 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse406 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse409 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse415 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse422 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse424 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse500 | PatchFirewallTrafficShaperLimiterQueueEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
