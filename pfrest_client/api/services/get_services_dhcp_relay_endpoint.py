from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_dhcp_relay_endpoint_response_400 import GetServicesDHCPRelayEndpointResponse400
from ...models.get_services_dhcp_relay_endpoint_response_401 import GetServicesDHCPRelayEndpointResponse401
from ...models.get_services_dhcp_relay_endpoint_response_403 import GetServicesDHCPRelayEndpointResponse403
from ...models.get_services_dhcp_relay_endpoint_response_404 import GetServicesDHCPRelayEndpointResponse404
from ...models.get_services_dhcp_relay_endpoint_response_405 import GetServicesDHCPRelayEndpointResponse405
from ...models.get_services_dhcp_relay_endpoint_response_406 import GetServicesDHCPRelayEndpointResponse406
from ...models.get_services_dhcp_relay_endpoint_response_409 import GetServicesDHCPRelayEndpointResponse409
from ...models.get_services_dhcp_relay_endpoint_response_415 import GetServicesDHCPRelayEndpointResponse415
from ...models.get_services_dhcp_relay_endpoint_response_422 import GetServicesDHCPRelayEndpointResponse422
from ...models.get_services_dhcp_relay_endpoint_response_424 import GetServicesDHCPRelayEndpointResponse424
from ...models.get_services_dhcp_relay_endpoint_response_500 import GetServicesDHCPRelayEndpointResponse500
from ...models.get_services_dhcp_relay_endpoint_response_503 import GetServicesDHCPRelayEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/dhcp_relay",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesDHCPRelayEndpointResponse400
    | GetServicesDHCPRelayEndpointResponse401
    | GetServicesDHCPRelayEndpointResponse403
    | GetServicesDHCPRelayEndpointResponse404
    | GetServicesDHCPRelayEndpointResponse405
    | GetServicesDHCPRelayEndpointResponse406
    | GetServicesDHCPRelayEndpointResponse409
    | GetServicesDHCPRelayEndpointResponse415
    | GetServicesDHCPRelayEndpointResponse422
    | GetServicesDHCPRelayEndpointResponse424
    | GetServicesDHCPRelayEndpointResponse500
    | GetServicesDHCPRelayEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesDHCPRelayEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesDHCPRelayEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesDHCPRelayEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesDHCPRelayEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesDHCPRelayEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesDHCPRelayEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesDHCPRelayEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesDHCPRelayEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesDHCPRelayEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesDHCPRelayEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesDHCPRelayEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesDHCPRelayEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesDHCPRelayEndpointResponse400
    | GetServicesDHCPRelayEndpointResponse401
    | GetServicesDHCPRelayEndpointResponse403
    | GetServicesDHCPRelayEndpointResponse404
    | GetServicesDHCPRelayEndpointResponse405
    | GetServicesDHCPRelayEndpointResponse406
    | GetServicesDHCPRelayEndpointResponse409
    | GetServicesDHCPRelayEndpointResponse415
    | GetServicesDHCPRelayEndpointResponse422
    | GetServicesDHCPRelayEndpointResponse424
    | GetServicesDHCPRelayEndpointResponse500
    | GetServicesDHCPRelayEndpointResponse503
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
    GetServicesDHCPRelayEndpointResponse400
    | GetServicesDHCPRelayEndpointResponse401
    | GetServicesDHCPRelayEndpointResponse403
    | GetServicesDHCPRelayEndpointResponse404
    | GetServicesDHCPRelayEndpointResponse405
    | GetServicesDHCPRelayEndpointResponse406
    | GetServicesDHCPRelayEndpointResponse409
    | GetServicesDHCPRelayEndpointResponse415
    | GetServicesDHCPRelayEndpointResponse422
    | GetServicesDHCPRelayEndpointResponse424
    | GetServicesDHCPRelayEndpointResponse500
    | GetServicesDHCPRelayEndpointResponse503
]:
    """<h3>Description:</h3>Reads current DHCP Relay.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPRelay<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-relay-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDHCPRelayEndpointResponse400 | GetServicesDHCPRelayEndpointResponse401 | GetServicesDHCPRelayEndpointResponse403 | GetServicesDHCPRelayEndpointResponse404 | GetServicesDHCPRelayEndpointResponse405 | GetServicesDHCPRelayEndpointResponse406 | GetServicesDHCPRelayEndpointResponse409 | GetServicesDHCPRelayEndpointResponse415 | GetServicesDHCPRelayEndpointResponse422 | GetServicesDHCPRelayEndpointResponse424 | GetServicesDHCPRelayEndpointResponse500 | GetServicesDHCPRelayEndpointResponse503]
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
    GetServicesDHCPRelayEndpointResponse400
    | GetServicesDHCPRelayEndpointResponse401
    | GetServicesDHCPRelayEndpointResponse403
    | GetServicesDHCPRelayEndpointResponse404
    | GetServicesDHCPRelayEndpointResponse405
    | GetServicesDHCPRelayEndpointResponse406
    | GetServicesDHCPRelayEndpointResponse409
    | GetServicesDHCPRelayEndpointResponse415
    | GetServicesDHCPRelayEndpointResponse422
    | GetServicesDHCPRelayEndpointResponse424
    | GetServicesDHCPRelayEndpointResponse500
    | GetServicesDHCPRelayEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current DHCP Relay.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPRelay<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-relay-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDHCPRelayEndpointResponse400 | GetServicesDHCPRelayEndpointResponse401 | GetServicesDHCPRelayEndpointResponse403 | GetServicesDHCPRelayEndpointResponse404 | GetServicesDHCPRelayEndpointResponse405 | GetServicesDHCPRelayEndpointResponse406 | GetServicesDHCPRelayEndpointResponse409 | GetServicesDHCPRelayEndpointResponse415 | GetServicesDHCPRelayEndpointResponse422 | GetServicesDHCPRelayEndpointResponse424 | GetServicesDHCPRelayEndpointResponse500 | GetServicesDHCPRelayEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesDHCPRelayEndpointResponse400
    | GetServicesDHCPRelayEndpointResponse401
    | GetServicesDHCPRelayEndpointResponse403
    | GetServicesDHCPRelayEndpointResponse404
    | GetServicesDHCPRelayEndpointResponse405
    | GetServicesDHCPRelayEndpointResponse406
    | GetServicesDHCPRelayEndpointResponse409
    | GetServicesDHCPRelayEndpointResponse415
    | GetServicesDHCPRelayEndpointResponse422
    | GetServicesDHCPRelayEndpointResponse424
    | GetServicesDHCPRelayEndpointResponse500
    | GetServicesDHCPRelayEndpointResponse503
]:
    """<h3>Description:</h3>Reads current DHCP Relay.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPRelay<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-relay-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDHCPRelayEndpointResponse400 | GetServicesDHCPRelayEndpointResponse401 | GetServicesDHCPRelayEndpointResponse403 | GetServicesDHCPRelayEndpointResponse404 | GetServicesDHCPRelayEndpointResponse405 | GetServicesDHCPRelayEndpointResponse406 | GetServicesDHCPRelayEndpointResponse409 | GetServicesDHCPRelayEndpointResponse415 | GetServicesDHCPRelayEndpointResponse422 | GetServicesDHCPRelayEndpointResponse424 | GetServicesDHCPRelayEndpointResponse500 | GetServicesDHCPRelayEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesDHCPRelayEndpointResponse400
    | GetServicesDHCPRelayEndpointResponse401
    | GetServicesDHCPRelayEndpointResponse403
    | GetServicesDHCPRelayEndpointResponse404
    | GetServicesDHCPRelayEndpointResponse405
    | GetServicesDHCPRelayEndpointResponse406
    | GetServicesDHCPRelayEndpointResponse409
    | GetServicesDHCPRelayEndpointResponse415
    | GetServicesDHCPRelayEndpointResponse422
    | GetServicesDHCPRelayEndpointResponse424
    | GetServicesDHCPRelayEndpointResponse500
    | GetServicesDHCPRelayEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current DHCP Relay.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPRelay<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-relay-get ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDHCPRelayEndpointResponse400 | GetServicesDHCPRelayEndpointResponse401 | GetServicesDHCPRelayEndpointResponse403 | GetServicesDHCPRelayEndpointResponse404 | GetServicesDHCPRelayEndpointResponse405 | GetServicesDHCPRelayEndpointResponse406 | GetServicesDHCPRelayEndpointResponse409 | GetServicesDHCPRelayEndpointResponse415 | GetServicesDHCPRelayEndpointResponse422 | GetServicesDHCPRelayEndpointResponse424 | GetServicesDHCPRelayEndpointResponse500 | GetServicesDHCPRelayEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
