from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_firewall_traffic_shaper_limiters_endpoint_data_body_item import (
    PutFirewallTrafficShaperLimitersEndpointDataBodyItem,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_json_body_item import (
    PutFirewallTrafficShaperLimitersEndpointJsonBodyItem,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_400 import (
    PutFirewallTrafficShaperLimitersEndpointResponse400,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_401 import (
    PutFirewallTrafficShaperLimitersEndpointResponse401,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_403 import (
    PutFirewallTrafficShaperLimitersEndpointResponse403,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_404 import (
    PutFirewallTrafficShaperLimitersEndpointResponse404,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_405 import (
    PutFirewallTrafficShaperLimitersEndpointResponse405,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_406 import (
    PutFirewallTrafficShaperLimitersEndpointResponse406,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_409 import (
    PutFirewallTrafficShaperLimitersEndpointResponse409,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_415 import (
    PutFirewallTrafficShaperLimitersEndpointResponse415,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_422 import (
    PutFirewallTrafficShaperLimitersEndpointResponse422,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_424 import (
    PutFirewallTrafficShaperLimitersEndpointResponse424,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_500 import (
    PutFirewallTrafficShaperLimitersEndpointResponse500,
)
from ...models.put_firewall_traffic_shaper_limiters_endpoint_response_503 import (
    PutFirewallTrafficShaperLimitersEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/firewall/traffic_shaper/limiters",
    }

    if isinstance(body, list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutFirewallTrafficShaperLimitersEndpointResponse400
    | PutFirewallTrafficShaperLimitersEndpointResponse401
    | PutFirewallTrafficShaperLimitersEndpointResponse403
    | PutFirewallTrafficShaperLimitersEndpointResponse404
    | PutFirewallTrafficShaperLimitersEndpointResponse405
    | PutFirewallTrafficShaperLimitersEndpointResponse406
    | PutFirewallTrafficShaperLimitersEndpointResponse409
    | PutFirewallTrafficShaperLimitersEndpointResponse415
    | PutFirewallTrafficShaperLimitersEndpointResponse422
    | PutFirewallTrafficShaperLimitersEndpointResponse424
    | PutFirewallTrafficShaperLimitersEndpointResponse500
    | PutFirewallTrafficShaperLimitersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutFirewallTrafficShaperLimitersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutFirewallTrafficShaperLimitersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutFirewallTrafficShaperLimitersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutFirewallTrafficShaperLimitersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutFirewallTrafficShaperLimitersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutFirewallTrafficShaperLimitersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutFirewallTrafficShaperLimitersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutFirewallTrafficShaperLimitersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutFirewallTrafficShaperLimitersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutFirewallTrafficShaperLimitersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutFirewallTrafficShaperLimitersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutFirewallTrafficShaperLimitersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutFirewallTrafficShaperLimitersEndpointResponse400
    | PutFirewallTrafficShaperLimitersEndpointResponse401
    | PutFirewallTrafficShaperLimitersEndpointResponse403
    | PutFirewallTrafficShaperLimitersEndpointResponse404
    | PutFirewallTrafficShaperLimitersEndpointResponse405
    | PutFirewallTrafficShaperLimitersEndpointResponse406
    | PutFirewallTrafficShaperLimitersEndpointResponse409
    | PutFirewallTrafficShaperLimitersEndpointResponse415
    | PutFirewallTrafficShaperLimitersEndpointResponse422
    | PutFirewallTrafficShaperLimitersEndpointResponse424
    | PutFirewallTrafficShaperLimitersEndpointResponse500
    | PutFirewallTrafficShaperLimitersEndpointResponse503
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
    body: list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutFirewallTrafficShaperLimitersEndpointResponse400
    | PutFirewallTrafficShaperLimitersEndpointResponse401
    | PutFirewallTrafficShaperLimitersEndpointResponse403
    | PutFirewallTrafficShaperLimitersEndpointResponse404
    | PutFirewallTrafficShaperLimitersEndpointResponse405
    | PutFirewallTrafficShaperLimitersEndpointResponse406
    | PutFirewallTrafficShaperLimitersEndpointResponse409
    | PutFirewallTrafficShaperLimitersEndpointResponse415
    | PutFirewallTrafficShaperLimitersEndpointResponse422
    | PutFirewallTrafficShaperLimitersEndpointResponse424
    | PutFirewallTrafficShaperLimitersEndpointResponse500
    | PutFirewallTrafficShaperLimitersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Traffic Shaper Limiters.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiters-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFirewallTrafficShaperLimitersEndpointResponse400 | PutFirewallTrafficShaperLimitersEndpointResponse401 | PutFirewallTrafficShaperLimitersEndpointResponse403 | PutFirewallTrafficShaperLimitersEndpointResponse404 | PutFirewallTrafficShaperLimitersEndpointResponse405 | PutFirewallTrafficShaperLimitersEndpointResponse406 | PutFirewallTrafficShaperLimitersEndpointResponse409 | PutFirewallTrafficShaperLimitersEndpointResponse415 | PutFirewallTrafficShaperLimitersEndpointResponse422 | PutFirewallTrafficShaperLimitersEndpointResponse424 | PutFirewallTrafficShaperLimitersEndpointResponse500 | PutFirewallTrafficShaperLimitersEndpointResponse503]
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
    body: list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutFirewallTrafficShaperLimitersEndpointResponse400
    | PutFirewallTrafficShaperLimitersEndpointResponse401
    | PutFirewallTrafficShaperLimitersEndpointResponse403
    | PutFirewallTrafficShaperLimitersEndpointResponse404
    | PutFirewallTrafficShaperLimitersEndpointResponse405
    | PutFirewallTrafficShaperLimitersEndpointResponse406
    | PutFirewallTrafficShaperLimitersEndpointResponse409
    | PutFirewallTrafficShaperLimitersEndpointResponse415
    | PutFirewallTrafficShaperLimitersEndpointResponse422
    | PutFirewallTrafficShaperLimitersEndpointResponse424
    | PutFirewallTrafficShaperLimitersEndpointResponse500
    | PutFirewallTrafficShaperLimitersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Traffic Shaper Limiters.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiters-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFirewallTrafficShaperLimitersEndpointResponse400 | PutFirewallTrafficShaperLimitersEndpointResponse401 | PutFirewallTrafficShaperLimitersEndpointResponse403 | PutFirewallTrafficShaperLimitersEndpointResponse404 | PutFirewallTrafficShaperLimitersEndpointResponse405 | PutFirewallTrafficShaperLimitersEndpointResponse406 | PutFirewallTrafficShaperLimitersEndpointResponse409 | PutFirewallTrafficShaperLimitersEndpointResponse415 | PutFirewallTrafficShaperLimitersEndpointResponse422 | PutFirewallTrafficShaperLimitersEndpointResponse424 | PutFirewallTrafficShaperLimitersEndpointResponse500 | PutFirewallTrafficShaperLimitersEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutFirewallTrafficShaperLimitersEndpointResponse400
    | PutFirewallTrafficShaperLimitersEndpointResponse401
    | PutFirewallTrafficShaperLimitersEndpointResponse403
    | PutFirewallTrafficShaperLimitersEndpointResponse404
    | PutFirewallTrafficShaperLimitersEndpointResponse405
    | PutFirewallTrafficShaperLimitersEndpointResponse406
    | PutFirewallTrafficShaperLimitersEndpointResponse409
    | PutFirewallTrafficShaperLimitersEndpointResponse415
    | PutFirewallTrafficShaperLimitersEndpointResponse422
    | PutFirewallTrafficShaperLimitersEndpointResponse424
    | PutFirewallTrafficShaperLimitersEndpointResponse500
    | PutFirewallTrafficShaperLimitersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Traffic Shaper Limiters.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiters-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFirewallTrafficShaperLimitersEndpointResponse400 | PutFirewallTrafficShaperLimitersEndpointResponse401 | PutFirewallTrafficShaperLimitersEndpointResponse403 | PutFirewallTrafficShaperLimitersEndpointResponse404 | PutFirewallTrafficShaperLimitersEndpointResponse405 | PutFirewallTrafficShaperLimitersEndpointResponse406 | PutFirewallTrafficShaperLimitersEndpointResponse409 | PutFirewallTrafficShaperLimitersEndpointResponse415 | PutFirewallTrafficShaperLimitersEndpointResponse422 | PutFirewallTrafficShaperLimitersEndpointResponse424 | PutFirewallTrafficShaperLimitersEndpointResponse500 | PutFirewallTrafficShaperLimitersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutFirewallTrafficShaperLimitersEndpointResponse400
    | PutFirewallTrafficShaperLimitersEndpointResponse401
    | PutFirewallTrafficShaperLimitersEndpointResponse403
    | PutFirewallTrafficShaperLimitersEndpointResponse404
    | PutFirewallTrafficShaperLimitersEndpointResponse405
    | PutFirewallTrafficShaperLimitersEndpointResponse406
    | PutFirewallTrafficShaperLimitersEndpointResponse409
    | PutFirewallTrafficShaperLimitersEndpointResponse415
    | PutFirewallTrafficShaperLimitersEndpointResponse422
    | PutFirewallTrafficShaperLimitersEndpointResponse424
    | PutFirewallTrafficShaperLimitersEndpointResponse500
    | PutFirewallTrafficShaperLimitersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Traffic Shaper Limiters.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: TrafficShaperLimiter<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-limiters-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallTrafficShaperLimitersEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallTrafficShaperLimitersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFirewallTrafficShaperLimitersEndpointResponse400 | PutFirewallTrafficShaperLimitersEndpointResponse401 | PutFirewallTrafficShaperLimitersEndpointResponse403 | PutFirewallTrafficShaperLimitersEndpointResponse404 | PutFirewallTrafficShaperLimitersEndpointResponse405 | PutFirewallTrafficShaperLimitersEndpointResponse406 | PutFirewallTrafficShaperLimitersEndpointResponse409 | PutFirewallTrafficShaperLimitersEndpointResponse415 | PutFirewallTrafficShaperLimitersEndpointResponse422 | PutFirewallTrafficShaperLimitersEndpointResponse424 | PutFirewallTrafficShaperLimitersEndpointResponse500 | PutFirewallTrafficShaperLimitersEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
