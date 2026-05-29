from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_firewall_states_size_endpoint_response_400 import GetFirewallStatesSizeEndpointResponse400
from ...models.get_firewall_states_size_endpoint_response_401 import GetFirewallStatesSizeEndpointResponse401
from ...models.get_firewall_states_size_endpoint_response_403 import GetFirewallStatesSizeEndpointResponse403
from ...models.get_firewall_states_size_endpoint_response_404 import GetFirewallStatesSizeEndpointResponse404
from ...models.get_firewall_states_size_endpoint_response_405 import GetFirewallStatesSizeEndpointResponse405
from ...models.get_firewall_states_size_endpoint_response_406 import GetFirewallStatesSizeEndpointResponse406
from ...models.get_firewall_states_size_endpoint_response_409 import GetFirewallStatesSizeEndpointResponse409
from ...models.get_firewall_states_size_endpoint_response_415 import GetFirewallStatesSizeEndpointResponse415
from ...models.get_firewall_states_size_endpoint_response_422 import GetFirewallStatesSizeEndpointResponse422
from ...models.get_firewall_states_size_endpoint_response_424 import GetFirewallStatesSizeEndpointResponse424
from ...models.get_firewall_states_size_endpoint_response_500 import GetFirewallStatesSizeEndpointResponse500
from ...models.get_firewall_states_size_endpoint_response_503 import GetFirewallStatesSizeEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/firewall/states/size",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFirewallStatesSizeEndpointResponse400
    | GetFirewallStatesSizeEndpointResponse401
    | GetFirewallStatesSizeEndpointResponse403
    | GetFirewallStatesSizeEndpointResponse404
    | GetFirewallStatesSizeEndpointResponse405
    | GetFirewallStatesSizeEndpointResponse406
    | GetFirewallStatesSizeEndpointResponse409
    | GetFirewallStatesSizeEndpointResponse415
    | GetFirewallStatesSizeEndpointResponse422
    | GetFirewallStatesSizeEndpointResponse424
    | GetFirewallStatesSizeEndpointResponse500
    | GetFirewallStatesSizeEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetFirewallStatesSizeEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFirewallStatesSizeEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFirewallStatesSizeEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFirewallStatesSizeEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetFirewallStatesSizeEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetFirewallStatesSizeEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetFirewallStatesSizeEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetFirewallStatesSizeEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetFirewallStatesSizeEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetFirewallStatesSizeEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetFirewallStatesSizeEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetFirewallStatesSizeEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFirewallStatesSizeEndpointResponse400
    | GetFirewallStatesSizeEndpointResponse401
    | GetFirewallStatesSizeEndpointResponse403
    | GetFirewallStatesSizeEndpointResponse404
    | GetFirewallStatesSizeEndpointResponse405
    | GetFirewallStatesSizeEndpointResponse406
    | GetFirewallStatesSizeEndpointResponse409
    | GetFirewallStatesSizeEndpointResponse415
    | GetFirewallStatesSizeEndpointResponse422
    | GetFirewallStatesSizeEndpointResponse424
    | GetFirewallStatesSizeEndpointResponse500
    | GetFirewallStatesSizeEndpointResponse503
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
) -> Response[
    GetFirewallStatesSizeEndpointResponse400
    | GetFirewallStatesSizeEndpointResponse401
    | GetFirewallStatesSizeEndpointResponse403
    | GetFirewallStatesSizeEndpointResponse404
    | GetFirewallStatesSizeEndpointResponse405
    | GetFirewallStatesSizeEndpointResponse406
    | GetFirewallStatesSizeEndpointResponse409
    | GetFirewallStatesSizeEndpointResponse415
    | GetFirewallStatesSizeEndpointResponse422
    | GetFirewallStatesSizeEndpointResponse424
    | GetFirewallStatesSizeEndpointResponse500
    | GetFirewallStatesSizeEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Firewall States Size.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallStatesSize<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-states-size-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallStatesSizeEndpointResponse400 | GetFirewallStatesSizeEndpointResponse401 | GetFirewallStatesSizeEndpointResponse403 | GetFirewallStatesSizeEndpointResponse404 | GetFirewallStatesSizeEndpointResponse405 | GetFirewallStatesSizeEndpointResponse406 | GetFirewallStatesSizeEndpointResponse409 | GetFirewallStatesSizeEndpointResponse415 | GetFirewallStatesSizeEndpointResponse422 | GetFirewallStatesSizeEndpointResponse424 | GetFirewallStatesSizeEndpointResponse500 | GetFirewallStatesSizeEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetFirewallStatesSizeEndpointResponse400
    | GetFirewallStatesSizeEndpointResponse401
    | GetFirewallStatesSizeEndpointResponse403
    | GetFirewallStatesSizeEndpointResponse404
    | GetFirewallStatesSizeEndpointResponse405
    | GetFirewallStatesSizeEndpointResponse406
    | GetFirewallStatesSizeEndpointResponse409
    | GetFirewallStatesSizeEndpointResponse415
    | GetFirewallStatesSizeEndpointResponse422
    | GetFirewallStatesSizeEndpointResponse424
    | GetFirewallStatesSizeEndpointResponse500
    | GetFirewallStatesSizeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Firewall States Size.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallStatesSize<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-states-size-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallStatesSizeEndpointResponse400 | GetFirewallStatesSizeEndpointResponse401 | GetFirewallStatesSizeEndpointResponse403 | GetFirewallStatesSizeEndpointResponse404 | GetFirewallStatesSizeEndpointResponse405 | GetFirewallStatesSizeEndpointResponse406 | GetFirewallStatesSizeEndpointResponse409 | GetFirewallStatesSizeEndpointResponse415 | GetFirewallStatesSizeEndpointResponse422 | GetFirewallStatesSizeEndpointResponse424 | GetFirewallStatesSizeEndpointResponse500 | GetFirewallStatesSizeEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetFirewallStatesSizeEndpointResponse400
    | GetFirewallStatesSizeEndpointResponse401
    | GetFirewallStatesSizeEndpointResponse403
    | GetFirewallStatesSizeEndpointResponse404
    | GetFirewallStatesSizeEndpointResponse405
    | GetFirewallStatesSizeEndpointResponse406
    | GetFirewallStatesSizeEndpointResponse409
    | GetFirewallStatesSizeEndpointResponse415
    | GetFirewallStatesSizeEndpointResponse422
    | GetFirewallStatesSizeEndpointResponse424
    | GetFirewallStatesSizeEndpointResponse500
    | GetFirewallStatesSizeEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Firewall States Size.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallStatesSize<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-states-size-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallStatesSizeEndpointResponse400 | GetFirewallStatesSizeEndpointResponse401 | GetFirewallStatesSizeEndpointResponse403 | GetFirewallStatesSizeEndpointResponse404 | GetFirewallStatesSizeEndpointResponse405 | GetFirewallStatesSizeEndpointResponse406 | GetFirewallStatesSizeEndpointResponse409 | GetFirewallStatesSizeEndpointResponse415 | GetFirewallStatesSizeEndpointResponse422 | GetFirewallStatesSizeEndpointResponse424 | GetFirewallStatesSizeEndpointResponse500 | GetFirewallStatesSizeEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetFirewallStatesSizeEndpointResponse400
    | GetFirewallStatesSizeEndpointResponse401
    | GetFirewallStatesSizeEndpointResponse403
    | GetFirewallStatesSizeEndpointResponse404
    | GetFirewallStatesSizeEndpointResponse405
    | GetFirewallStatesSizeEndpointResponse406
    | GetFirewallStatesSizeEndpointResponse409
    | GetFirewallStatesSizeEndpointResponse415
    | GetFirewallStatesSizeEndpointResponse422
    | GetFirewallStatesSizeEndpointResponse424
    | GetFirewallStatesSizeEndpointResponse500
    | GetFirewallStatesSizeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Firewall States Size.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallStatesSize<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-states-size-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallStatesSizeEndpointResponse400 | GetFirewallStatesSizeEndpointResponse401 | GetFirewallStatesSizeEndpointResponse403 | GetFirewallStatesSizeEndpointResponse404 | GetFirewallStatesSizeEndpointResponse405 | GetFirewallStatesSizeEndpointResponse406 | GetFirewallStatesSizeEndpointResponse409 | GetFirewallStatesSizeEndpointResponse415 | GetFirewallStatesSizeEndpointResponse422 | GetFirewallStatesSizeEndpointResponse424 | GetFirewallStatesSizeEndpointResponse500 | GetFirewallStatesSizeEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
