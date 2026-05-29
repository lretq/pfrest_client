from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_400 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse400,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_401 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse401,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_403 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse403,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_404 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse404,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_405 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse405,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_406 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse406,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_409 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse409,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_415 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse415,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_422 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse422,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_424 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse424,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_500 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse500,
)
from ...models.delete_firewall_traffic_shaper_limiter_endpoint_response_503 import (
    DeleteFirewallTrafficShaperLimiterEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | str,
    apply: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params["apply"] = apply

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/firewall/traffic_shaper/limiter",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteFirewallTrafficShaperLimiterEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteFirewallTrafficShaperLimiterEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteFirewallTrafficShaperLimiterEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteFirewallTrafficShaperLimiterEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteFirewallTrafficShaperLimiterEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteFirewallTrafficShaperLimiterEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteFirewallTrafficShaperLimiterEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteFirewallTrafficShaperLimiterEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteFirewallTrafficShaperLimiterEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteFirewallTrafficShaperLimiterEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteFirewallTrafficShaperLimiterEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteFirewallTrafficShaperLimiterEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteFirewallTrafficShaperLimiterEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteFirewallTrafficShaperLimiterEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterEndpointResponse503
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
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteFirewallTrafficShaperLimiterEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-
    delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallTrafficShaperLimiterEndpointResponse400 | DeleteFirewallTrafficShaperLimiterEndpointResponse401 | DeleteFirewallTrafficShaperLimiterEndpointResponse403 | DeleteFirewallTrafficShaperLimiterEndpointResponse404 | DeleteFirewallTrafficShaperLimiterEndpointResponse405 | DeleteFirewallTrafficShaperLimiterEndpointResponse406 | DeleteFirewallTrafficShaperLimiterEndpointResponse409 | DeleteFirewallTrafficShaperLimiterEndpointResponse415 | DeleteFirewallTrafficShaperLimiterEndpointResponse422 | DeleteFirewallTrafficShaperLimiterEndpointResponse424 | DeleteFirewallTrafficShaperLimiterEndpointResponse500 | DeleteFirewallTrafficShaperLimiterEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
        apply=apply,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteFirewallTrafficShaperLimiterEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-
    delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallTrafficShaperLimiterEndpointResponse400 | DeleteFirewallTrafficShaperLimiterEndpointResponse401 | DeleteFirewallTrafficShaperLimiterEndpointResponse403 | DeleteFirewallTrafficShaperLimiterEndpointResponse404 | DeleteFirewallTrafficShaperLimiterEndpointResponse405 | DeleteFirewallTrafficShaperLimiterEndpointResponse406 | DeleteFirewallTrafficShaperLimiterEndpointResponse409 | DeleteFirewallTrafficShaperLimiterEndpointResponse415 | DeleteFirewallTrafficShaperLimiterEndpointResponse422 | DeleteFirewallTrafficShaperLimiterEndpointResponse424 | DeleteFirewallTrafficShaperLimiterEndpointResponse500 | DeleteFirewallTrafficShaperLimiterEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
        apply=apply,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteFirewallTrafficShaperLimiterEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-
    delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallTrafficShaperLimiterEndpointResponse400 | DeleteFirewallTrafficShaperLimiterEndpointResponse401 | DeleteFirewallTrafficShaperLimiterEndpointResponse403 | DeleteFirewallTrafficShaperLimiterEndpointResponse404 | DeleteFirewallTrafficShaperLimiterEndpointResponse405 | DeleteFirewallTrafficShaperLimiterEndpointResponse406 | DeleteFirewallTrafficShaperLimiterEndpointResponse409 | DeleteFirewallTrafficShaperLimiterEndpointResponse415 | DeleteFirewallTrafficShaperLimiterEndpointResponse422 | DeleteFirewallTrafficShaperLimiterEndpointResponse424 | DeleteFirewallTrafficShaperLimiterEndpointResponse500 | DeleteFirewallTrafficShaperLimiterEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
        apply=apply,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteFirewallTrafficShaperLimiterEndpointResponse400
    | DeleteFirewallTrafficShaperLimiterEndpointResponse401
    | DeleteFirewallTrafficShaperLimiterEndpointResponse403
    | DeleteFirewallTrafficShaperLimiterEndpointResponse404
    | DeleteFirewallTrafficShaperLimiterEndpointResponse405
    | DeleteFirewallTrafficShaperLimiterEndpointResponse406
    | DeleteFirewallTrafficShaperLimiterEndpointResponse409
    | DeleteFirewallTrafficShaperLimiterEndpointResponse415
    | DeleteFirewallTrafficShaperLimiterEndpointResponse422
    | DeleteFirewallTrafficShaperLimiterEndpointResponse424
    | DeleteFirewallTrafficShaperLimiterEndpointResponse500
    | DeleteFirewallTrafficShaperLimiterEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Traffic Shaper Limiter.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiter-
    delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallTrafficShaperLimiterEndpointResponse400 | DeleteFirewallTrafficShaperLimiterEndpointResponse401 | DeleteFirewallTrafficShaperLimiterEndpointResponse403 | DeleteFirewallTrafficShaperLimiterEndpointResponse404 | DeleteFirewallTrafficShaperLimiterEndpointResponse405 | DeleteFirewallTrafficShaperLimiterEndpointResponse406 | DeleteFirewallTrafficShaperLimiterEndpointResponse409 | DeleteFirewallTrafficShaperLimiterEndpointResponse415 | DeleteFirewallTrafficShaperLimiterEndpointResponse422 | DeleteFirewallTrafficShaperLimiterEndpointResponse424 | DeleteFirewallTrafficShaperLimiterEndpointResponse500 | DeleteFirewallTrafficShaperLimiterEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            apply=apply,
        )
    ).parsed
