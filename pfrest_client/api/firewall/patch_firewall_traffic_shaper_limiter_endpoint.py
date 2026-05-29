from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_data_body import (
    PatchFirewallTrafficShaperLimiterEndpointDataBody,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_json_body import (
    PatchFirewallTrafficShaperLimiterEndpointJsonBody,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_400 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse400,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_401 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse401,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_403 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse403,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_404 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse404,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_405 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse405,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_406 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse406,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_409 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse409,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_415 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse415,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_422 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse422,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_424 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse424,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_500 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse500,
)
from ...models.patch_firewall_traffic_shaper_limiter_endpoint_response_503 import (
    PatchFirewallTrafficShaperLimiterEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallTrafficShaperLimiterEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/traffic_shaper/limiter",
    }

    if isinstance(body, PatchFirewallTrafficShaperLimiterEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallTrafficShaperLimiterEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallTrafficShaperLimiterEndpointResponse400
    | PatchFirewallTrafficShaperLimiterEndpointResponse401
    | PatchFirewallTrafficShaperLimiterEndpointResponse403
    | PatchFirewallTrafficShaperLimiterEndpointResponse404
    | PatchFirewallTrafficShaperLimiterEndpointResponse405
    | PatchFirewallTrafficShaperLimiterEndpointResponse406
    | PatchFirewallTrafficShaperLimiterEndpointResponse409
    | PatchFirewallTrafficShaperLimiterEndpointResponse415
    | PatchFirewallTrafficShaperLimiterEndpointResponse422
    | PatchFirewallTrafficShaperLimiterEndpointResponse424
    | PatchFirewallTrafficShaperLimiterEndpointResponse500
    | PatchFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallTrafficShaperLimiterEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallTrafficShaperLimiterEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallTrafficShaperLimiterEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallTrafficShaperLimiterEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallTrafficShaperLimiterEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallTrafficShaperLimiterEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallTrafficShaperLimiterEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallTrafficShaperLimiterEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallTrafficShaperLimiterEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallTrafficShaperLimiterEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallTrafficShaperLimiterEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallTrafficShaperLimiterEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallTrafficShaperLimiterEndpointResponse400
    | PatchFirewallTrafficShaperLimiterEndpointResponse401
    | PatchFirewallTrafficShaperLimiterEndpointResponse403
    | PatchFirewallTrafficShaperLimiterEndpointResponse404
    | PatchFirewallTrafficShaperLimiterEndpointResponse405
    | PatchFirewallTrafficShaperLimiterEndpointResponse406
    | PatchFirewallTrafficShaperLimiterEndpointResponse409
    | PatchFirewallTrafficShaperLimiterEndpointResponse415
    | PatchFirewallTrafficShaperLimiterEndpointResponse422
    | PatchFirewallTrafficShaperLimiterEndpointResponse424
    | PatchFirewallTrafficShaperLimiterEndpointResponse500
    | PatchFirewallTrafficShaperLimiterEndpointResponse503
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
    body: PatchFirewallTrafficShaperLimiterEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperLimiterEndpointResponse400
    | PatchFirewallTrafficShaperLimiterEndpointResponse401
    | PatchFirewallTrafficShaperLimiterEndpointResponse403
    | PatchFirewallTrafficShaperLimiterEndpointResponse404
    | PatchFirewallTrafficShaperLimiterEndpointResponse405
    | PatchFirewallTrafficShaperLimiterEndpointResponse406
    | PatchFirewallTrafficShaperLimiterEndpointResponse409
    | PatchFirewallTrafficShaperLimiterEndpointResponse415
    | PatchFirewallTrafficShaperLimiterEndpointResponse422
    | PatchFirewallTrafficShaperLimiterEndpointResponse424
    | PatchFirewallTrafficShaperLimiterEndpointResponse500
    | PatchFirewallTrafficShaperLimiterEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchFirewallTrafficShaperLimiterEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperLimiterEndpointResponse400 | PatchFirewallTrafficShaperLimiterEndpointResponse401 | PatchFirewallTrafficShaperLimiterEndpointResponse403 | PatchFirewallTrafficShaperLimiterEndpointResponse404 | PatchFirewallTrafficShaperLimiterEndpointResponse405 | PatchFirewallTrafficShaperLimiterEndpointResponse406 | PatchFirewallTrafficShaperLimiterEndpointResponse409 | PatchFirewallTrafficShaperLimiterEndpointResponse415 | PatchFirewallTrafficShaperLimiterEndpointResponse422 | PatchFirewallTrafficShaperLimiterEndpointResponse424 | PatchFirewallTrafficShaperLimiterEndpointResponse500 | PatchFirewallTrafficShaperLimiterEndpointResponse503]
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
    body: PatchFirewallTrafficShaperLimiterEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperLimiterEndpointResponse400
    | PatchFirewallTrafficShaperLimiterEndpointResponse401
    | PatchFirewallTrafficShaperLimiterEndpointResponse403
    | PatchFirewallTrafficShaperLimiterEndpointResponse404
    | PatchFirewallTrafficShaperLimiterEndpointResponse405
    | PatchFirewallTrafficShaperLimiterEndpointResponse406
    | PatchFirewallTrafficShaperLimiterEndpointResponse409
    | PatchFirewallTrafficShaperLimiterEndpointResponse415
    | PatchFirewallTrafficShaperLimiterEndpointResponse422
    | PatchFirewallTrafficShaperLimiterEndpointResponse424
    | PatchFirewallTrafficShaperLimiterEndpointResponse500
    | PatchFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchFirewallTrafficShaperLimiterEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperLimiterEndpointResponse400 | PatchFirewallTrafficShaperLimiterEndpointResponse401 | PatchFirewallTrafficShaperLimiterEndpointResponse403 | PatchFirewallTrafficShaperLimiterEndpointResponse404 | PatchFirewallTrafficShaperLimiterEndpointResponse405 | PatchFirewallTrafficShaperLimiterEndpointResponse406 | PatchFirewallTrafficShaperLimiterEndpointResponse409 | PatchFirewallTrafficShaperLimiterEndpointResponse415 | PatchFirewallTrafficShaperLimiterEndpointResponse422 | PatchFirewallTrafficShaperLimiterEndpointResponse424 | PatchFirewallTrafficShaperLimiterEndpointResponse500 | PatchFirewallTrafficShaperLimiterEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperLimiterEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperLimiterEndpointResponse400
    | PatchFirewallTrafficShaperLimiterEndpointResponse401
    | PatchFirewallTrafficShaperLimiterEndpointResponse403
    | PatchFirewallTrafficShaperLimiterEndpointResponse404
    | PatchFirewallTrafficShaperLimiterEndpointResponse405
    | PatchFirewallTrafficShaperLimiterEndpointResponse406
    | PatchFirewallTrafficShaperLimiterEndpointResponse409
    | PatchFirewallTrafficShaperLimiterEndpointResponse415
    | PatchFirewallTrafficShaperLimiterEndpointResponse422
    | PatchFirewallTrafficShaperLimiterEndpointResponse424
    | PatchFirewallTrafficShaperLimiterEndpointResponse500
    | PatchFirewallTrafficShaperLimiterEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchFirewallTrafficShaperLimiterEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperLimiterEndpointResponse400 | PatchFirewallTrafficShaperLimiterEndpointResponse401 | PatchFirewallTrafficShaperLimiterEndpointResponse403 | PatchFirewallTrafficShaperLimiterEndpointResponse404 | PatchFirewallTrafficShaperLimiterEndpointResponse405 | PatchFirewallTrafficShaperLimiterEndpointResponse406 | PatchFirewallTrafficShaperLimiterEndpointResponse409 | PatchFirewallTrafficShaperLimiterEndpointResponse415 | PatchFirewallTrafficShaperLimiterEndpointResponse422 | PatchFirewallTrafficShaperLimiterEndpointResponse424 | PatchFirewallTrafficShaperLimiterEndpointResponse500 | PatchFirewallTrafficShaperLimiterEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperLimiterEndpointJsonBody
    | PatchFirewallTrafficShaperLimiterEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperLimiterEndpointResponse400
    | PatchFirewallTrafficShaperLimiterEndpointResponse401
    | PatchFirewallTrafficShaperLimiterEndpointResponse403
    | PatchFirewallTrafficShaperLimiterEndpointResponse404
    | PatchFirewallTrafficShaperLimiterEndpointResponse405
    | PatchFirewallTrafficShaperLimiterEndpointResponse406
    | PatchFirewallTrafficShaperLimiterEndpointResponse409
    | PatchFirewallTrafficShaperLimiterEndpointResponse415
    | PatchFirewallTrafficShaperLimiterEndpointResponse422
    | PatchFirewallTrafficShaperLimiterEndpointResponse424
    | PatchFirewallTrafficShaperLimiterEndpointResponse500
    | PatchFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchFirewallTrafficShaperLimiterEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperLimiterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperLimiterEndpointResponse400 | PatchFirewallTrafficShaperLimiterEndpointResponse401 | PatchFirewallTrafficShaperLimiterEndpointResponse403 | PatchFirewallTrafficShaperLimiterEndpointResponse404 | PatchFirewallTrafficShaperLimiterEndpointResponse405 | PatchFirewallTrafficShaperLimiterEndpointResponse406 | PatchFirewallTrafficShaperLimiterEndpointResponse409 | PatchFirewallTrafficShaperLimiterEndpointResponse415 | PatchFirewallTrafficShaperLimiterEndpointResponse422 | PatchFirewallTrafficShaperLimiterEndpointResponse424 | PatchFirewallTrafficShaperLimiterEndpointResponse500 | PatchFirewallTrafficShaperLimiterEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
