from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_traffic_shaper_queue_endpoint_data_body import (
    PostFirewallTrafficShaperQueueEndpointDataBody,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_json_body import (
    PostFirewallTrafficShaperQueueEndpointJsonBody,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_400 import (
    PostFirewallTrafficShaperQueueEndpointResponse400,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_401 import (
    PostFirewallTrafficShaperQueueEndpointResponse401,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_403 import (
    PostFirewallTrafficShaperQueueEndpointResponse403,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_404 import (
    PostFirewallTrafficShaperQueueEndpointResponse404,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_405 import (
    PostFirewallTrafficShaperQueueEndpointResponse405,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_406 import (
    PostFirewallTrafficShaperQueueEndpointResponse406,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_409 import (
    PostFirewallTrafficShaperQueueEndpointResponse409,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_415 import (
    PostFirewallTrafficShaperQueueEndpointResponse415,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_422 import (
    PostFirewallTrafficShaperQueueEndpointResponse422,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_424 import (
    PostFirewallTrafficShaperQueueEndpointResponse424,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_500 import (
    PostFirewallTrafficShaperQueueEndpointResponse500,
)
from ...models.post_firewall_traffic_shaper_queue_endpoint_response_503 import (
    PostFirewallTrafficShaperQueueEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallTrafficShaperQueueEndpointJsonBody
    | PostFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/traffic_shaper/queue",
    }

    if isinstance(body, PostFirewallTrafficShaperQueueEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallTrafficShaperQueueEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallTrafficShaperQueueEndpointResponse400
    | PostFirewallTrafficShaperQueueEndpointResponse401
    | PostFirewallTrafficShaperQueueEndpointResponse403
    | PostFirewallTrafficShaperQueueEndpointResponse404
    | PostFirewallTrafficShaperQueueEndpointResponse405
    | PostFirewallTrafficShaperQueueEndpointResponse406
    | PostFirewallTrafficShaperQueueEndpointResponse409
    | PostFirewallTrafficShaperQueueEndpointResponse415
    | PostFirewallTrafficShaperQueueEndpointResponse422
    | PostFirewallTrafficShaperQueueEndpointResponse424
    | PostFirewallTrafficShaperQueueEndpointResponse500
    | PostFirewallTrafficShaperQueueEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallTrafficShaperQueueEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallTrafficShaperQueueEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallTrafficShaperQueueEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallTrafficShaperQueueEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallTrafficShaperQueueEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallTrafficShaperQueueEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallTrafficShaperQueueEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallTrafficShaperQueueEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallTrafficShaperQueueEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallTrafficShaperQueueEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallTrafficShaperQueueEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallTrafficShaperQueueEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallTrafficShaperQueueEndpointResponse400
    | PostFirewallTrafficShaperQueueEndpointResponse401
    | PostFirewallTrafficShaperQueueEndpointResponse403
    | PostFirewallTrafficShaperQueueEndpointResponse404
    | PostFirewallTrafficShaperQueueEndpointResponse405
    | PostFirewallTrafficShaperQueueEndpointResponse406
    | PostFirewallTrafficShaperQueueEndpointResponse409
    | PostFirewallTrafficShaperQueueEndpointResponse415
    | PostFirewallTrafficShaperQueueEndpointResponse422
    | PostFirewallTrafficShaperQueueEndpointResponse424
    | PostFirewallTrafficShaperQueueEndpointResponse500
    | PostFirewallTrafficShaperQueueEndpointResponse503
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
    body: PostFirewallTrafficShaperQueueEndpointJsonBody
    | PostFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperQueueEndpointResponse400
    | PostFirewallTrafficShaperQueueEndpointResponse401
    | PostFirewallTrafficShaperQueueEndpointResponse403
    | PostFirewallTrafficShaperQueueEndpointResponse404
    | PostFirewallTrafficShaperQueueEndpointResponse405
    | PostFirewallTrafficShaperQueueEndpointResponse406
    | PostFirewallTrafficShaperQueueEndpointResponse409
    | PostFirewallTrafficShaperQueueEndpointResponse415
    | PostFirewallTrafficShaperQueueEndpointResponse422
    | PostFirewallTrafficShaperQueueEndpointResponse424
    | PostFirewallTrafficShaperQueueEndpointResponse500
    | PostFirewallTrafficShaperQueueEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper Queue.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaperQueue<br>**Parent model**:
    TrafficShaper<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    queue-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostFirewallTrafficShaperQueueEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperQueueEndpointResponse400 | PostFirewallTrafficShaperQueueEndpointResponse401 | PostFirewallTrafficShaperQueueEndpointResponse403 | PostFirewallTrafficShaperQueueEndpointResponse404 | PostFirewallTrafficShaperQueueEndpointResponse405 | PostFirewallTrafficShaperQueueEndpointResponse406 | PostFirewallTrafficShaperQueueEndpointResponse409 | PostFirewallTrafficShaperQueueEndpointResponse415 | PostFirewallTrafficShaperQueueEndpointResponse422 | PostFirewallTrafficShaperQueueEndpointResponse424 | PostFirewallTrafficShaperQueueEndpointResponse500 | PostFirewallTrafficShaperQueueEndpointResponse503]
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
    body: PostFirewallTrafficShaperQueueEndpointJsonBody
    | PostFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperQueueEndpointResponse400
    | PostFirewallTrafficShaperQueueEndpointResponse401
    | PostFirewallTrafficShaperQueueEndpointResponse403
    | PostFirewallTrafficShaperQueueEndpointResponse404
    | PostFirewallTrafficShaperQueueEndpointResponse405
    | PostFirewallTrafficShaperQueueEndpointResponse406
    | PostFirewallTrafficShaperQueueEndpointResponse409
    | PostFirewallTrafficShaperQueueEndpointResponse415
    | PostFirewallTrafficShaperQueueEndpointResponse422
    | PostFirewallTrafficShaperQueueEndpointResponse424
    | PostFirewallTrafficShaperQueueEndpointResponse500
    | PostFirewallTrafficShaperQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper Queue.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaperQueue<br>**Parent model**:
    TrafficShaper<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    queue-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostFirewallTrafficShaperQueueEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperQueueEndpointResponse400 | PostFirewallTrafficShaperQueueEndpointResponse401 | PostFirewallTrafficShaperQueueEndpointResponse403 | PostFirewallTrafficShaperQueueEndpointResponse404 | PostFirewallTrafficShaperQueueEndpointResponse405 | PostFirewallTrafficShaperQueueEndpointResponse406 | PostFirewallTrafficShaperQueueEndpointResponse409 | PostFirewallTrafficShaperQueueEndpointResponse415 | PostFirewallTrafficShaperQueueEndpointResponse422 | PostFirewallTrafficShaperQueueEndpointResponse424 | PostFirewallTrafficShaperQueueEndpointResponse500 | PostFirewallTrafficShaperQueueEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperQueueEndpointJsonBody
    | PostFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostFirewallTrafficShaperQueueEndpointResponse400
    | PostFirewallTrafficShaperQueueEndpointResponse401
    | PostFirewallTrafficShaperQueueEndpointResponse403
    | PostFirewallTrafficShaperQueueEndpointResponse404
    | PostFirewallTrafficShaperQueueEndpointResponse405
    | PostFirewallTrafficShaperQueueEndpointResponse406
    | PostFirewallTrafficShaperQueueEndpointResponse409
    | PostFirewallTrafficShaperQueueEndpointResponse415
    | PostFirewallTrafficShaperQueueEndpointResponse422
    | PostFirewallTrafficShaperQueueEndpointResponse424
    | PostFirewallTrafficShaperQueueEndpointResponse500
    | PostFirewallTrafficShaperQueueEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Traffic Shaper Queue.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaperQueue<br>**Parent model**:
    TrafficShaper<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    queue-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostFirewallTrafficShaperQueueEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallTrafficShaperQueueEndpointResponse400 | PostFirewallTrafficShaperQueueEndpointResponse401 | PostFirewallTrafficShaperQueueEndpointResponse403 | PostFirewallTrafficShaperQueueEndpointResponse404 | PostFirewallTrafficShaperQueueEndpointResponse405 | PostFirewallTrafficShaperQueueEndpointResponse406 | PostFirewallTrafficShaperQueueEndpointResponse409 | PostFirewallTrafficShaperQueueEndpointResponse415 | PostFirewallTrafficShaperQueueEndpointResponse422 | PostFirewallTrafficShaperQueueEndpointResponse424 | PostFirewallTrafficShaperQueueEndpointResponse500 | PostFirewallTrafficShaperQueueEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallTrafficShaperQueueEndpointJsonBody
    | PostFirewallTrafficShaperQueueEndpointDataBody
    | Unset = UNSET,
) -> (
    PostFirewallTrafficShaperQueueEndpointResponse400
    | PostFirewallTrafficShaperQueueEndpointResponse401
    | PostFirewallTrafficShaperQueueEndpointResponse403
    | PostFirewallTrafficShaperQueueEndpointResponse404
    | PostFirewallTrafficShaperQueueEndpointResponse405
    | PostFirewallTrafficShaperQueueEndpointResponse406
    | PostFirewallTrafficShaperQueueEndpointResponse409
    | PostFirewallTrafficShaperQueueEndpointResponse415
    | PostFirewallTrafficShaperQueueEndpointResponse422
    | PostFirewallTrafficShaperQueueEndpointResponse424
    | PostFirewallTrafficShaperQueueEndpointResponse500
    | PostFirewallTrafficShaperQueueEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Traffic Shaper Queue.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaperQueue<br>**Parent model**:
    TrafficShaper<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-
    queue-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostFirewallTrafficShaperQueueEndpointJsonBody | Unset):
        body (PostFirewallTrafficShaperQueueEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallTrafficShaperQueueEndpointResponse400 | PostFirewallTrafficShaperQueueEndpointResponse401 | PostFirewallTrafficShaperQueueEndpointResponse403 | PostFirewallTrafficShaperQueueEndpointResponse404 | PostFirewallTrafficShaperQueueEndpointResponse405 | PostFirewallTrafficShaperQueueEndpointResponse406 | PostFirewallTrafficShaperQueueEndpointResponse409 | PostFirewallTrafficShaperQueueEndpointResponse415 | PostFirewallTrafficShaperQueueEndpointResponse422 | PostFirewallTrafficShaperQueueEndpointResponse424 | PostFirewallTrafficShaperQueueEndpointResponse500 | PostFirewallTrafficShaperQueueEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
