from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_firewall_traffic_shapers_endpoint_data_body_item import PutFirewallTrafficShapersEndpointDataBodyItem
from ...models.put_firewall_traffic_shapers_endpoint_json_body_item import PutFirewallTrafficShapersEndpointJsonBodyItem
from ...models.put_firewall_traffic_shapers_endpoint_response_400 import PutFirewallTrafficShapersEndpointResponse400
from ...models.put_firewall_traffic_shapers_endpoint_response_401 import PutFirewallTrafficShapersEndpointResponse401
from ...models.put_firewall_traffic_shapers_endpoint_response_403 import PutFirewallTrafficShapersEndpointResponse403
from ...models.put_firewall_traffic_shapers_endpoint_response_404 import PutFirewallTrafficShapersEndpointResponse404
from ...models.put_firewall_traffic_shapers_endpoint_response_405 import PutFirewallTrafficShapersEndpointResponse405
from ...models.put_firewall_traffic_shapers_endpoint_response_406 import PutFirewallTrafficShapersEndpointResponse406
from ...models.put_firewall_traffic_shapers_endpoint_response_409 import PutFirewallTrafficShapersEndpointResponse409
from ...models.put_firewall_traffic_shapers_endpoint_response_415 import PutFirewallTrafficShapersEndpointResponse415
from ...models.put_firewall_traffic_shapers_endpoint_response_422 import PutFirewallTrafficShapersEndpointResponse422
from ...models.put_firewall_traffic_shapers_endpoint_response_424 import PutFirewallTrafficShapersEndpointResponse424
from ...models.put_firewall_traffic_shapers_endpoint_response_500 import PutFirewallTrafficShapersEndpointResponse500
from ...models.put_firewall_traffic_shapers_endpoint_response_503 import PutFirewallTrafficShapersEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutFirewallTrafficShapersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShapersEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/firewall/traffic_shapers",
    }

    if isinstance(body, list[PutFirewallTrafficShapersEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutFirewallTrafficShapersEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutFirewallTrafficShapersEndpointResponse400
    | PutFirewallTrafficShapersEndpointResponse401
    | PutFirewallTrafficShapersEndpointResponse403
    | PutFirewallTrafficShapersEndpointResponse404
    | PutFirewallTrafficShapersEndpointResponse405
    | PutFirewallTrafficShapersEndpointResponse406
    | PutFirewallTrafficShapersEndpointResponse409
    | PutFirewallTrafficShapersEndpointResponse415
    | PutFirewallTrafficShapersEndpointResponse422
    | PutFirewallTrafficShapersEndpointResponse424
    | PutFirewallTrafficShapersEndpointResponse500
    | PutFirewallTrafficShapersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutFirewallTrafficShapersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutFirewallTrafficShapersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutFirewallTrafficShapersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutFirewallTrafficShapersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutFirewallTrafficShapersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutFirewallTrafficShapersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutFirewallTrafficShapersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutFirewallTrafficShapersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutFirewallTrafficShapersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutFirewallTrafficShapersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutFirewallTrafficShapersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutFirewallTrafficShapersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutFirewallTrafficShapersEndpointResponse400
    | PutFirewallTrafficShapersEndpointResponse401
    | PutFirewallTrafficShapersEndpointResponse403
    | PutFirewallTrafficShapersEndpointResponse404
    | PutFirewallTrafficShapersEndpointResponse405
    | PutFirewallTrafficShapersEndpointResponse406
    | PutFirewallTrafficShapersEndpointResponse409
    | PutFirewallTrafficShapersEndpointResponse415
    | PutFirewallTrafficShapersEndpointResponse422
    | PutFirewallTrafficShapersEndpointResponse424
    | PutFirewallTrafficShapersEndpointResponse500
    | PutFirewallTrafficShapersEndpointResponse503
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
    body: list[PutFirewallTrafficShapersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShapersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutFirewallTrafficShapersEndpointResponse400
    | PutFirewallTrafficShapersEndpointResponse401
    | PutFirewallTrafficShapersEndpointResponse403
    | PutFirewallTrafficShapersEndpointResponse404
    | PutFirewallTrafficShapersEndpointResponse405
    | PutFirewallTrafficShapersEndpointResponse406
    | PutFirewallTrafficShapersEndpointResponse409
    | PutFirewallTrafficShapersEndpointResponse415
    | PutFirewallTrafficShapersEndpointResponse422
    | PutFirewallTrafficShapersEndpointResponse424
    | PutFirewallTrafficShapersEndpointResponse500
    | PutFirewallTrafficShapersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Traffic Shapers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shapers-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallTrafficShapersEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallTrafficShapersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFirewallTrafficShapersEndpointResponse400 | PutFirewallTrafficShapersEndpointResponse401 | PutFirewallTrafficShapersEndpointResponse403 | PutFirewallTrafficShapersEndpointResponse404 | PutFirewallTrafficShapersEndpointResponse405 | PutFirewallTrafficShapersEndpointResponse406 | PutFirewallTrafficShapersEndpointResponse409 | PutFirewallTrafficShapersEndpointResponse415 | PutFirewallTrafficShapersEndpointResponse422 | PutFirewallTrafficShapersEndpointResponse424 | PutFirewallTrafficShapersEndpointResponse500 | PutFirewallTrafficShapersEndpointResponse503]
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
    body: list[PutFirewallTrafficShapersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShapersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutFirewallTrafficShapersEndpointResponse400
    | PutFirewallTrafficShapersEndpointResponse401
    | PutFirewallTrafficShapersEndpointResponse403
    | PutFirewallTrafficShapersEndpointResponse404
    | PutFirewallTrafficShapersEndpointResponse405
    | PutFirewallTrafficShapersEndpointResponse406
    | PutFirewallTrafficShapersEndpointResponse409
    | PutFirewallTrafficShapersEndpointResponse415
    | PutFirewallTrafficShapersEndpointResponse422
    | PutFirewallTrafficShapersEndpointResponse424
    | PutFirewallTrafficShapersEndpointResponse500
    | PutFirewallTrafficShapersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Traffic Shapers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shapers-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallTrafficShapersEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallTrafficShapersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFirewallTrafficShapersEndpointResponse400 | PutFirewallTrafficShapersEndpointResponse401 | PutFirewallTrafficShapersEndpointResponse403 | PutFirewallTrafficShapersEndpointResponse404 | PutFirewallTrafficShapersEndpointResponse405 | PutFirewallTrafficShapersEndpointResponse406 | PutFirewallTrafficShapersEndpointResponse409 | PutFirewallTrafficShapersEndpointResponse415 | PutFirewallTrafficShapersEndpointResponse422 | PutFirewallTrafficShapersEndpointResponse424 | PutFirewallTrafficShapersEndpointResponse500 | PutFirewallTrafficShapersEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutFirewallTrafficShapersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShapersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutFirewallTrafficShapersEndpointResponse400
    | PutFirewallTrafficShapersEndpointResponse401
    | PutFirewallTrafficShapersEndpointResponse403
    | PutFirewallTrafficShapersEndpointResponse404
    | PutFirewallTrafficShapersEndpointResponse405
    | PutFirewallTrafficShapersEndpointResponse406
    | PutFirewallTrafficShapersEndpointResponse409
    | PutFirewallTrafficShapersEndpointResponse415
    | PutFirewallTrafficShapersEndpointResponse422
    | PutFirewallTrafficShapersEndpointResponse424
    | PutFirewallTrafficShapersEndpointResponse500
    | PutFirewallTrafficShapersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Traffic Shapers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shapers-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallTrafficShapersEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallTrafficShapersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFirewallTrafficShapersEndpointResponse400 | PutFirewallTrafficShapersEndpointResponse401 | PutFirewallTrafficShapersEndpointResponse403 | PutFirewallTrafficShapersEndpointResponse404 | PutFirewallTrafficShapersEndpointResponse405 | PutFirewallTrafficShapersEndpointResponse406 | PutFirewallTrafficShapersEndpointResponse409 | PutFirewallTrafficShapersEndpointResponse415 | PutFirewallTrafficShapersEndpointResponse422 | PutFirewallTrafficShapersEndpointResponse424 | PutFirewallTrafficShapersEndpointResponse500 | PutFirewallTrafficShapersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutFirewallTrafficShapersEndpointJsonBodyItem]
    | list[PutFirewallTrafficShapersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutFirewallTrafficShapersEndpointResponse400
    | PutFirewallTrafficShapersEndpointResponse401
    | PutFirewallTrafficShapersEndpointResponse403
    | PutFirewallTrafficShapersEndpointResponse404
    | PutFirewallTrafficShapersEndpointResponse405
    | PutFirewallTrafficShapersEndpointResponse406
    | PutFirewallTrafficShapersEndpointResponse409
    | PutFirewallTrafficShapersEndpointResponse415
    | PutFirewallTrafficShapersEndpointResponse422
    | PutFirewallTrafficShapersEndpointResponse424
    | PutFirewallTrafficShapersEndpointResponse500
    | PutFirewallTrafficShapersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Traffic Shapers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: TrafficShaper<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-traffic-shapers-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallTrafficShapersEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallTrafficShapersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFirewallTrafficShapersEndpointResponse400 | PutFirewallTrafficShapersEndpointResponse401 | PutFirewallTrafficShapersEndpointResponse403 | PutFirewallTrafficShapersEndpointResponse404 | PutFirewallTrafficShapersEndpointResponse405 | PutFirewallTrafficShapersEndpointResponse406 | PutFirewallTrafficShapersEndpointResponse409 | PutFirewallTrafficShapersEndpointResponse415 | PutFirewallTrafficShapersEndpointResponse422 | PutFirewallTrafficShapersEndpointResponse424 | PutFirewallTrafficShapersEndpointResponse500 | PutFirewallTrafficShapersEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
