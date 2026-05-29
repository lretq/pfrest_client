from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_firewall_nat_port_forwards_endpoint_data_body_item import (
    PutFirewallNATPortForwardsEndpointDataBodyItem,
)
from ...models.put_firewall_nat_port_forwards_endpoint_json_body_item import (
    PutFirewallNATPortForwardsEndpointJsonBodyItem,
)
from ...models.put_firewall_nat_port_forwards_endpoint_response_400 import PutFirewallNATPortForwardsEndpointResponse400
from ...models.put_firewall_nat_port_forwards_endpoint_response_401 import PutFirewallNATPortForwardsEndpointResponse401
from ...models.put_firewall_nat_port_forwards_endpoint_response_403 import PutFirewallNATPortForwardsEndpointResponse403
from ...models.put_firewall_nat_port_forwards_endpoint_response_404 import PutFirewallNATPortForwardsEndpointResponse404
from ...models.put_firewall_nat_port_forwards_endpoint_response_405 import PutFirewallNATPortForwardsEndpointResponse405
from ...models.put_firewall_nat_port_forwards_endpoint_response_406 import PutFirewallNATPortForwardsEndpointResponse406
from ...models.put_firewall_nat_port_forwards_endpoint_response_409 import PutFirewallNATPortForwardsEndpointResponse409
from ...models.put_firewall_nat_port_forwards_endpoint_response_415 import PutFirewallNATPortForwardsEndpointResponse415
from ...models.put_firewall_nat_port_forwards_endpoint_response_422 import PutFirewallNATPortForwardsEndpointResponse422
from ...models.put_firewall_nat_port_forwards_endpoint_response_424 import PutFirewallNATPortForwardsEndpointResponse424
from ...models.put_firewall_nat_port_forwards_endpoint_response_500 import PutFirewallNATPortForwardsEndpointResponse500
from ...models.put_firewall_nat_port_forwards_endpoint_response_503 import PutFirewallNATPortForwardsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutFirewallNATPortForwardsEndpointJsonBodyItem]
    | list[PutFirewallNATPortForwardsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/firewall/nat/port_forwards",
    }

    if isinstance(body, list[PutFirewallNATPortForwardsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutFirewallNATPortForwardsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutFirewallNATPortForwardsEndpointResponse400
    | PutFirewallNATPortForwardsEndpointResponse401
    | PutFirewallNATPortForwardsEndpointResponse403
    | PutFirewallNATPortForwardsEndpointResponse404
    | PutFirewallNATPortForwardsEndpointResponse405
    | PutFirewallNATPortForwardsEndpointResponse406
    | PutFirewallNATPortForwardsEndpointResponse409
    | PutFirewallNATPortForwardsEndpointResponse415
    | PutFirewallNATPortForwardsEndpointResponse422
    | PutFirewallNATPortForwardsEndpointResponse424
    | PutFirewallNATPortForwardsEndpointResponse500
    | PutFirewallNATPortForwardsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutFirewallNATPortForwardsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutFirewallNATPortForwardsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutFirewallNATPortForwardsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutFirewallNATPortForwardsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutFirewallNATPortForwardsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutFirewallNATPortForwardsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutFirewallNATPortForwardsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutFirewallNATPortForwardsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutFirewallNATPortForwardsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutFirewallNATPortForwardsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutFirewallNATPortForwardsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutFirewallNATPortForwardsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutFirewallNATPortForwardsEndpointResponse400
    | PutFirewallNATPortForwardsEndpointResponse401
    | PutFirewallNATPortForwardsEndpointResponse403
    | PutFirewallNATPortForwardsEndpointResponse404
    | PutFirewallNATPortForwardsEndpointResponse405
    | PutFirewallNATPortForwardsEndpointResponse406
    | PutFirewallNATPortForwardsEndpointResponse409
    | PutFirewallNATPortForwardsEndpointResponse415
    | PutFirewallNATPortForwardsEndpointResponse422
    | PutFirewallNATPortForwardsEndpointResponse424
    | PutFirewallNATPortForwardsEndpointResponse500
    | PutFirewallNATPortForwardsEndpointResponse503
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
    body: list[PutFirewallNATPortForwardsEndpointJsonBodyItem]
    | list[PutFirewallNATPortForwardsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutFirewallNATPortForwardsEndpointResponse400
    | PutFirewallNATPortForwardsEndpointResponse401
    | PutFirewallNATPortForwardsEndpointResponse403
    | PutFirewallNATPortForwardsEndpointResponse404
    | PutFirewallNATPortForwardsEndpointResponse405
    | PutFirewallNATPortForwardsEndpointResponse406
    | PutFirewallNATPortForwardsEndpointResponse409
    | PutFirewallNATPortForwardsEndpointResponse415
    | PutFirewallNATPortForwardsEndpointResponse422
    | PutFirewallNATPortForwardsEndpointResponse424
    | PutFirewallNATPortForwardsEndpointResponse500
    | PutFirewallNATPortForwardsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Port Forwards.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forwards-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallNATPortForwardsEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallNATPortForwardsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFirewallNATPortForwardsEndpointResponse400 | PutFirewallNATPortForwardsEndpointResponse401 | PutFirewallNATPortForwardsEndpointResponse403 | PutFirewallNATPortForwardsEndpointResponse404 | PutFirewallNATPortForwardsEndpointResponse405 | PutFirewallNATPortForwardsEndpointResponse406 | PutFirewallNATPortForwardsEndpointResponse409 | PutFirewallNATPortForwardsEndpointResponse415 | PutFirewallNATPortForwardsEndpointResponse422 | PutFirewallNATPortForwardsEndpointResponse424 | PutFirewallNATPortForwardsEndpointResponse500 | PutFirewallNATPortForwardsEndpointResponse503]
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
    body: list[PutFirewallNATPortForwardsEndpointJsonBodyItem]
    | list[PutFirewallNATPortForwardsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutFirewallNATPortForwardsEndpointResponse400
    | PutFirewallNATPortForwardsEndpointResponse401
    | PutFirewallNATPortForwardsEndpointResponse403
    | PutFirewallNATPortForwardsEndpointResponse404
    | PutFirewallNATPortForwardsEndpointResponse405
    | PutFirewallNATPortForwardsEndpointResponse406
    | PutFirewallNATPortForwardsEndpointResponse409
    | PutFirewallNATPortForwardsEndpointResponse415
    | PutFirewallNATPortForwardsEndpointResponse422
    | PutFirewallNATPortForwardsEndpointResponse424
    | PutFirewallNATPortForwardsEndpointResponse500
    | PutFirewallNATPortForwardsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Port Forwards.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forwards-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallNATPortForwardsEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallNATPortForwardsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFirewallNATPortForwardsEndpointResponse400 | PutFirewallNATPortForwardsEndpointResponse401 | PutFirewallNATPortForwardsEndpointResponse403 | PutFirewallNATPortForwardsEndpointResponse404 | PutFirewallNATPortForwardsEndpointResponse405 | PutFirewallNATPortForwardsEndpointResponse406 | PutFirewallNATPortForwardsEndpointResponse409 | PutFirewallNATPortForwardsEndpointResponse415 | PutFirewallNATPortForwardsEndpointResponse422 | PutFirewallNATPortForwardsEndpointResponse424 | PutFirewallNATPortForwardsEndpointResponse500 | PutFirewallNATPortForwardsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutFirewallNATPortForwardsEndpointJsonBodyItem]
    | list[PutFirewallNATPortForwardsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutFirewallNATPortForwardsEndpointResponse400
    | PutFirewallNATPortForwardsEndpointResponse401
    | PutFirewallNATPortForwardsEndpointResponse403
    | PutFirewallNATPortForwardsEndpointResponse404
    | PutFirewallNATPortForwardsEndpointResponse405
    | PutFirewallNATPortForwardsEndpointResponse406
    | PutFirewallNATPortForwardsEndpointResponse409
    | PutFirewallNATPortForwardsEndpointResponse415
    | PutFirewallNATPortForwardsEndpointResponse422
    | PutFirewallNATPortForwardsEndpointResponse424
    | PutFirewallNATPortForwardsEndpointResponse500
    | PutFirewallNATPortForwardsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Port Forwards.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forwards-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallNATPortForwardsEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallNATPortForwardsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFirewallNATPortForwardsEndpointResponse400 | PutFirewallNATPortForwardsEndpointResponse401 | PutFirewallNATPortForwardsEndpointResponse403 | PutFirewallNATPortForwardsEndpointResponse404 | PutFirewallNATPortForwardsEndpointResponse405 | PutFirewallNATPortForwardsEndpointResponse406 | PutFirewallNATPortForwardsEndpointResponse409 | PutFirewallNATPortForwardsEndpointResponse415 | PutFirewallNATPortForwardsEndpointResponse422 | PutFirewallNATPortForwardsEndpointResponse424 | PutFirewallNATPortForwardsEndpointResponse500 | PutFirewallNATPortForwardsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutFirewallNATPortForwardsEndpointJsonBodyItem]
    | list[PutFirewallNATPortForwardsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutFirewallNATPortForwardsEndpointResponse400
    | PutFirewallNATPortForwardsEndpointResponse401
    | PutFirewallNATPortForwardsEndpointResponse403
    | PutFirewallNATPortForwardsEndpointResponse404
    | PutFirewallNATPortForwardsEndpointResponse405
    | PutFirewallNATPortForwardsEndpointResponse406
    | PutFirewallNATPortForwardsEndpointResponse409
    | PutFirewallNATPortForwardsEndpointResponse415
    | PutFirewallNATPortForwardsEndpointResponse422
    | PutFirewallNATPortForwardsEndpointResponse424
    | PutFirewallNATPortForwardsEndpointResponse500
    | PutFirewallNATPortForwardsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Port Forwards.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: PortForward<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-nat-port-forwards-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallNATPortForwardsEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallNATPortForwardsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFirewallNATPortForwardsEndpointResponse400 | PutFirewallNATPortForwardsEndpointResponse401 | PutFirewallNATPortForwardsEndpointResponse403 | PutFirewallNATPortForwardsEndpointResponse404 | PutFirewallNATPortForwardsEndpointResponse405 | PutFirewallNATPortForwardsEndpointResponse406 | PutFirewallNATPortForwardsEndpointResponse409 | PutFirewallNATPortForwardsEndpointResponse415 | PutFirewallNATPortForwardsEndpointResponse422 | PutFirewallNATPortForwardsEndpointResponse424 | PutFirewallNATPortForwardsEndpointResponse500 | PutFirewallNATPortForwardsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
