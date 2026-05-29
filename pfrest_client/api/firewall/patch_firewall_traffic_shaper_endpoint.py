from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_traffic_shaper_endpoint_data_body import PatchFirewallTrafficShaperEndpointDataBody
from ...models.patch_firewall_traffic_shaper_endpoint_json_body import PatchFirewallTrafficShaperEndpointJsonBody
from ...models.patch_firewall_traffic_shaper_endpoint_response_400 import PatchFirewallTrafficShaperEndpointResponse400
from ...models.patch_firewall_traffic_shaper_endpoint_response_401 import PatchFirewallTrafficShaperEndpointResponse401
from ...models.patch_firewall_traffic_shaper_endpoint_response_403 import PatchFirewallTrafficShaperEndpointResponse403
from ...models.patch_firewall_traffic_shaper_endpoint_response_404 import PatchFirewallTrafficShaperEndpointResponse404
from ...models.patch_firewall_traffic_shaper_endpoint_response_405 import PatchFirewallTrafficShaperEndpointResponse405
from ...models.patch_firewall_traffic_shaper_endpoint_response_406 import PatchFirewallTrafficShaperEndpointResponse406
from ...models.patch_firewall_traffic_shaper_endpoint_response_409 import PatchFirewallTrafficShaperEndpointResponse409
from ...models.patch_firewall_traffic_shaper_endpoint_response_415 import PatchFirewallTrafficShaperEndpointResponse415
from ...models.patch_firewall_traffic_shaper_endpoint_response_422 import PatchFirewallTrafficShaperEndpointResponse422
from ...models.patch_firewall_traffic_shaper_endpoint_response_424 import PatchFirewallTrafficShaperEndpointResponse424
from ...models.patch_firewall_traffic_shaper_endpoint_response_500 import PatchFirewallTrafficShaperEndpointResponse500
from ...models.patch_firewall_traffic_shaper_endpoint_response_503 import PatchFirewallTrafficShaperEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallTrafficShaperEndpointJsonBody | PatchFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/traffic_shaper",
    }

    if isinstance(body, PatchFirewallTrafficShaperEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallTrafficShaperEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallTrafficShaperEndpointResponse400
    | PatchFirewallTrafficShaperEndpointResponse401
    | PatchFirewallTrafficShaperEndpointResponse403
    | PatchFirewallTrafficShaperEndpointResponse404
    | PatchFirewallTrafficShaperEndpointResponse405
    | PatchFirewallTrafficShaperEndpointResponse406
    | PatchFirewallTrafficShaperEndpointResponse409
    | PatchFirewallTrafficShaperEndpointResponse415
    | PatchFirewallTrafficShaperEndpointResponse422
    | PatchFirewallTrafficShaperEndpointResponse424
    | PatchFirewallTrafficShaperEndpointResponse500
    | PatchFirewallTrafficShaperEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallTrafficShaperEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallTrafficShaperEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallTrafficShaperEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallTrafficShaperEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallTrafficShaperEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallTrafficShaperEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallTrafficShaperEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallTrafficShaperEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallTrafficShaperEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallTrafficShaperEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallTrafficShaperEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallTrafficShaperEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallTrafficShaperEndpointResponse400
    | PatchFirewallTrafficShaperEndpointResponse401
    | PatchFirewallTrafficShaperEndpointResponse403
    | PatchFirewallTrafficShaperEndpointResponse404
    | PatchFirewallTrafficShaperEndpointResponse405
    | PatchFirewallTrafficShaperEndpointResponse406
    | PatchFirewallTrafficShaperEndpointResponse409
    | PatchFirewallTrafficShaperEndpointResponse415
    | PatchFirewallTrafficShaperEndpointResponse422
    | PatchFirewallTrafficShaperEndpointResponse424
    | PatchFirewallTrafficShaperEndpointResponse500
    | PatchFirewallTrafficShaperEndpointResponse503
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
    body: PatchFirewallTrafficShaperEndpointJsonBody | PatchFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperEndpointResponse400
    | PatchFirewallTrafficShaperEndpointResponse401
    | PatchFirewallTrafficShaperEndpointResponse403
    | PatchFirewallTrafficShaperEndpointResponse404
    | PatchFirewallTrafficShaperEndpointResponse405
    | PatchFirewallTrafficShaperEndpointResponse406
    | PatchFirewallTrafficShaperEndpointResponse409
    | PatchFirewallTrafficShaperEndpointResponse415
    | PatchFirewallTrafficShaperEndpointResponse422
    | PatchFirewallTrafficShaperEndpointResponse424
    | PatchFirewallTrafficShaperEndpointResponse500
    | PatchFirewallTrafficShaperEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperEndpointResponse400 | PatchFirewallTrafficShaperEndpointResponse401 | PatchFirewallTrafficShaperEndpointResponse403 | PatchFirewallTrafficShaperEndpointResponse404 | PatchFirewallTrafficShaperEndpointResponse405 | PatchFirewallTrafficShaperEndpointResponse406 | PatchFirewallTrafficShaperEndpointResponse409 | PatchFirewallTrafficShaperEndpointResponse415 | PatchFirewallTrafficShaperEndpointResponse422 | PatchFirewallTrafficShaperEndpointResponse424 | PatchFirewallTrafficShaperEndpointResponse500 | PatchFirewallTrafficShaperEndpointResponse503]
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
    body: PatchFirewallTrafficShaperEndpointJsonBody | PatchFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperEndpointResponse400
    | PatchFirewallTrafficShaperEndpointResponse401
    | PatchFirewallTrafficShaperEndpointResponse403
    | PatchFirewallTrafficShaperEndpointResponse404
    | PatchFirewallTrafficShaperEndpointResponse405
    | PatchFirewallTrafficShaperEndpointResponse406
    | PatchFirewallTrafficShaperEndpointResponse409
    | PatchFirewallTrafficShaperEndpointResponse415
    | PatchFirewallTrafficShaperEndpointResponse422
    | PatchFirewallTrafficShaperEndpointResponse424
    | PatchFirewallTrafficShaperEndpointResponse500
    | PatchFirewallTrafficShaperEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperEndpointResponse400 | PatchFirewallTrafficShaperEndpointResponse401 | PatchFirewallTrafficShaperEndpointResponse403 | PatchFirewallTrafficShaperEndpointResponse404 | PatchFirewallTrafficShaperEndpointResponse405 | PatchFirewallTrafficShaperEndpointResponse406 | PatchFirewallTrafficShaperEndpointResponse409 | PatchFirewallTrafficShaperEndpointResponse415 | PatchFirewallTrafficShaperEndpointResponse422 | PatchFirewallTrafficShaperEndpointResponse424 | PatchFirewallTrafficShaperEndpointResponse500 | PatchFirewallTrafficShaperEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperEndpointJsonBody | PatchFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallTrafficShaperEndpointResponse400
    | PatchFirewallTrafficShaperEndpointResponse401
    | PatchFirewallTrafficShaperEndpointResponse403
    | PatchFirewallTrafficShaperEndpointResponse404
    | PatchFirewallTrafficShaperEndpointResponse405
    | PatchFirewallTrafficShaperEndpointResponse406
    | PatchFirewallTrafficShaperEndpointResponse409
    | PatchFirewallTrafficShaperEndpointResponse415
    | PatchFirewallTrafficShaperEndpointResponse422
    | PatchFirewallTrafficShaperEndpointResponse424
    | PatchFirewallTrafficShaperEndpointResponse500
    | PatchFirewallTrafficShaperEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Traffic Shaper.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallTrafficShaperEndpointResponse400 | PatchFirewallTrafficShaperEndpointResponse401 | PatchFirewallTrafficShaperEndpointResponse403 | PatchFirewallTrafficShaperEndpointResponse404 | PatchFirewallTrafficShaperEndpointResponse405 | PatchFirewallTrafficShaperEndpointResponse406 | PatchFirewallTrafficShaperEndpointResponse409 | PatchFirewallTrafficShaperEndpointResponse415 | PatchFirewallTrafficShaperEndpointResponse422 | PatchFirewallTrafficShaperEndpointResponse424 | PatchFirewallTrafficShaperEndpointResponse500 | PatchFirewallTrafficShaperEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallTrafficShaperEndpointJsonBody | PatchFirewallTrafficShaperEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallTrafficShaperEndpointResponse400
    | PatchFirewallTrafficShaperEndpointResponse401
    | PatchFirewallTrafficShaperEndpointResponse403
    | PatchFirewallTrafficShaperEndpointResponse404
    | PatchFirewallTrafficShaperEndpointResponse405
    | PatchFirewallTrafficShaperEndpointResponse406
    | PatchFirewallTrafficShaperEndpointResponse409
    | PatchFirewallTrafficShaperEndpointResponse415
    | PatchFirewallTrafficShaperEndpointResponse422
    | PatchFirewallTrafficShaperEndpointResponse424
    | PatchFirewallTrafficShaperEndpointResponse500
    | PatchFirewallTrafficShaperEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Traffic Shaper.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shaper-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallTrafficShaperEndpointJsonBody | Unset):
        body (PatchFirewallTrafficShaperEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallTrafficShaperEndpointResponse400 | PatchFirewallTrafficShaperEndpointResponse401 | PatchFirewallTrafficShaperEndpointResponse403 | PatchFirewallTrafficShaperEndpointResponse404 | PatchFirewallTrafficShaperEndpointResponse405 | PatchFirewallTrafficShaperEndpointResponse406 | PatchFirewallTrafficShaperEndpointResponse409 | PatchFirewallTrafficShaperEndpointResponse415 | PatchFirewallTrafficShaperEndpointResponse422 | PatchFirewallTrafficShaperEndpointResponse424 | PatchFirewallTrafficShaperEndpointResponse500 | PatchFirewallTrafficShaperEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
