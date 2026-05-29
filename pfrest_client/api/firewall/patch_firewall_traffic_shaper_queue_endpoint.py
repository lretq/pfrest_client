from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_traffic_shaper_queue_endpoint_data_body import (
    PatchFirewallTrafficShaperQueueEndpointDataBody,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_json_body import (
    PatchFirewallTrafficShaperQueueEndpointJsonBody,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_400 import (
    PatchFirewallTrafficShaperQueueEndpointResponse400,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_401 import (
    PatchFirewallTrafficShaperQueueEndpointResponse401,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_403 import (
    PatchFirewallTrafficShaperQueueEndpointResponse403,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_404 import (
    PatchFirewallTrafficShaperQueueEndpointResponse404,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_405 import (
    PatchFirewallTrafficShaperQueueEndpointResponse405,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_406 import (
    PatchFirewallTrafficShaperQueueEndpointResponse406,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_409 import (
    PatchFirewallTrafficShaperQueueEndpointResponse409,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_415 import (
    PatchFirewallTrafficShaperQueueEndpointResponse415,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_422 import (
    PatchFirewallTrafficShaperQueueEndpointResponse422,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_424 import (
    PatchFirewallTrafficShaperQueueEndpointResponse424,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_500 import (
    PatchFirewallTrafficShaperQueueEndpointResponse500,
)
from ...models.patch_firewall_traffic_shaper_queue_endpoint_response_503 import (
    PatchFirewallTrafficShaperQueueEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallTrafficShaperQueueEndpointJsonBody
    | PatchFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/traffic_shaper/queue",
    }

    if isinstance(body, PatchFirewallTrafficShaperQueueEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallTrafficShaperQueueEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallTrafficShaperQueueEndpointResponse400
    | PatchFirewallTrafficShaperQueueEndpointResponse401
    | PatchFirewallTrafficShaperQueueEndpointResponse403
    | PatchFirewallTrafficShaperQueueEndpointResponse404
    | PatchFirewallTrafficShaperQueueEndpointResponse405
    | PatchFirewallTrafficShaperQueueEndpointResponse406
    | PatchFirewallTrafficShaperQueueEndpointResponse409
    | PatchFirewallTrafficShaperQueueEndpointResponse415
    | PatchFirewallTrafficShaperQueueEndpointResponse422
    | PatchFirewallTrafficShaperQueueEndpointResponse424
    | PatchFirewallTrafficShaperQueueEndpointResponse500
    | PatchFirewallTrafficShaperQueueEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallTrafficShaperQueueEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallTrafficShaperQueueEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallTrafficShaperQueueEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallTrafficShaperQueueEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallTrafficShaperQueueEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallTrafficShaperQueueEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallTrafficShaperQueueEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallTrafficShaperQueueEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallTrafficShaperQueueEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallTrafficShaperQueueEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallTrafficShaperQueueEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallTrafficShaperQueueEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallTrafficShaperQueueEndpointResponse400
    | PatchFirewallTrafficShaperQueueEndpointResponse401
    | PatchFirewallTrafficShaperQueueEndpointResponse403
    | PatchFirewallTrafficShaperQueueEndpointResponse404
    | PatchFirewallTrafficShaperQueueEndpointResponse405
    | PatchFirewallTrafficShaperQueueEndpointResponse406
    | PatchFirewallTrafficShaperQueueEndpointResponse409
    | PatchFirewallTrafficShaperQueueEndpointResponse415
    | PatchFirewallTrafficShaperQueueEndpointResponse422
    | PatchFirewallTrafficShaperQueueEndpointResponse424
    | PatchFirewallTrafficShaperQueueEndpointResponse500
    | PatchFirewallTrafficShaperQueueEndpointResponse503
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
    body: PatchFirewallTrafficShaperQueueEndpointJsonBody
    | PatchFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperQueueEndpointResponse400
    | PatchFirewallTrafficShaperQueueEndpointResponse401
    | PatchFirewallTrafficShaperQueueEndpointResponse403
    | PatchFirewallTrafficShaperQueueEndpointResponse404
    | PatchFirewallTrafficShaperQueueEndpointResponse405
    | PatchFirewallTrafficShaperQueueEndpointResponse406
    | PatchFirewallTrafficShaperQueueEndpointResponse409
    | PatchFirewallTrafficShaperQueueEndpointResponse415
    | PatchFirewallTrafficShaperQueueEndpointResponse422
    | PatchFirewallTrafficShaperQueueEndpointResponse424
    | PatchFirewallTrafficShaperQueueEndpointResponse500
    | PatchFirewallTrafficShaperQueueEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperQueue<br>**Parent model**:
    TrafficShaper<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    queue-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchFirewallTrafficShaperQueueEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperQueueEndpointResponse400 | PatchFirewallTrafficShaperQueueEndpointResponse401 | PatchFirewallTrafficShaperQueueEndpointResponse403 | PatchFirewallTrafficShaperQueueEndpointResponse404 | PatchFirewallTrafficShaperQueueEndpointResponse405 | PatchFirewallTrafficShaperQueueEndpointResponse406 | PatchFirewallTrafficShaperQueueEndpointResponse409 | PatchFirewallTrafficShaperQueueEndpointResponse415 | PatchFirewallTrafficShaperQueueEndpointResponse422 | PatchFirewallTrafficShaperQueueEndpointResponse424 | PatchFirewallTrafficShaperQueueEndpointResponse500 | PatchFirewallTrafficShaperQueueEndpointResponse503]
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
    body: PatchFirewallTrafficShaperQueueEndpointJsonBody
    | PatchFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperQueueEndpointResponse400
    | PatchFirewallTrafficShaperQueueEndpointResponse401
    | PatchFirewallTrafficShaperQueueEndpointResponse403
    | PatchFirewallTrafficShaperQueueEndpointResponse404
    | PatchFirewallTrafficShaperQueueEndpointResponse405
    | PatchFirewallTrafficShaperQueueEndpointResponse406
    | PatchFirewallTrafficShaperQueueEndpointResponse409
    | PatchFirewallTrafficShaperQueueEndpointResponse415
    | PatchFirewallTrafficShaperQueueEndpointResponse422
    | PatchFirewallTrafficShaperQueueEndpointResponse424
    | PatchFirewallTrafficShaperQueueEndpointResponse500
    | PatchFirewallTrafficShaperQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperQueue<br>**Parent model**:
    TrafficShaper<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    queue-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchFirewallTrafficShaperQueueEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperQueueEndpointResponse400 | PatchFirewallTrafficShaperQueueEndpointResponse401 | PatchFirewallTrafficShaperQueueEndpointResponse403 | PatchFirewallTrafficShaperQueueEndpointResponse404 | PatchFirewallTrafficShaperQueueEndpointResponse405 | PatchFirewallTrafficShaperQueueEndpointResponse406 | PatchFirewallTrafficShaperQueueEndpointResponse409 | PatchFirewallTrafficShaperQueueEndpointResponse415 | PatchFirewallTrafficShaperQueueEndpointResponse422 | PatchFirewallTrafficShaperQueueEndpointResponse424 | PatchFirewallTrafficShaperQueueEndpointResponse500 | PatchFirewallTrafficShaperQueueEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperQueueEndpointJsonBody
    | PatchFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperQueueEndpointResponse400
    | PatchFirewallTrafficShaperQueueEndpointResponse401
    | PatchFirewallTrafficShaperQueueEndpointResponse403
    | PatchFirewallTrafficShaperQueueEndpointResponse404
    | PatchFirewallTrafficShaperQueueEndpointResponse405
    | PatchFirewallTrafficShaperQueueEndpointResponse406
    | PatchFirewallTrafficShaperQueueEndpointResponse409
    | PatchFirewallTrafficShaperQueueEndpointResponse415
    | PatchFirewallTrafficShaperQueueEndpointResponse422
    | PatchFirewallTrafficShaperQueueEndpointResponse424
    | PatchFirewallTrafficShaperQueueEndpointResponse500
    | PatchFirewallTrafficShaperQueueEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperQueue<br>**Parent model**:
    TrafficShaper<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    queue-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchFirewallTrafficShaperQueueEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperQueueEndpointResponse400 | PatchFirewallTrafficShaperQueueEndpointResponse401 | PatchFirewallTrafficShaperQueueEndpointResponse403 | PatchFirewallTrafficShaperQueueEndpointResponse404 | PatchFirewallTrafficShaperQueueEndpointResponse405 | PatchFirewallTrafficShaperQueueEndpointResponse406 | PatchFirewallTrafficShaperQueueEndpointResponse409 | PatchFirewallTrafficShaperQueueEndpointResponse415 | PatchFirewallTrafficShaperQueueEndpointResponse422 | PatchFirewallTrafficShaperQueueEndpointResponse424 | PatchFirewallTrafficShaperQueueEndpointResponse500 | PatchFirewallTrafficShaperQueueEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperQueueEndpointJsonBody
    | PatchFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperQueueEndpointResponse400
    | PatchFirewallTrafficShaperQueueEndpointResponse401
    | PatchFirewallTrafficShaperQueueEndpointResponse403
    | PatchFirewallTrafficShaperQueueEndpointResponse404
    | PatchFirewallTrafficShaperQueueEndpointResponse405
    | PatchFirewallTrafficShaperQueueEndpointResponse406
    | PatchFirewallTrafficShaperQueueEndpointResponse409
    | PatchFirewallTrafficShaperQueueEndpointResponse415
    | PatchFirewallTrafficShaperQueueEndpointResponse422
    | PatchFirewallTrafficShaperQueueEndpointResponse424
    | PatchFirewallTrafficShaperQueueEndpointResponse500
    | PatchFirewallTrafficShaperQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper Queue.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperQueue<br>**Parent model**:
    TrafficShaper<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    queue-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchFirewallTrafficShaperQueueEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperQueueEndpointResponse400 | PatchFirewallTrafficShaperQueueEndpointResponse401 | PatchFirewallTrafficShaperQueueEndpointResponse403 | PatchFirewallTrafficShaperQueueEndpointResponse404 | PatchFirewallTrafficShaperQueueEndpointResponse405 | PatchFirewallTrafficShaperQueueEndpointResponse406 | PatchFirewallTrafficShaperQueueEndpointResponse409 | PatchFirewallTrafficShaperQueueEndpointResponse415 | PatchFirewallTrafficShaperQueueEndpointResponse422 | PatchFirewallTrafficShaperQueueEndpointResponse424 | PatchFirewallTrafficShaperQueueEndpointResponse500 | PatchFirewallTrafficShaperQueueEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
