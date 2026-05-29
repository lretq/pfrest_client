from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_dhcp_server_apply_endpoint_response_400 import GetServicesDHCPServerApplyEndpointResponse400
from ...models.get_services_dhcp_server_apply_endpoint_response_401 import GetServicesDHCPServerApplyEndpointResponse401
from ...models.get_services_dhcp_server_apply_endpoint_response_403 import GetServicesDHCPServerApplyEndpointResponse403
from ...models.get_services_dhcp_server_apply_endpoint_response_404 import GetServicesDHCPServerApplyEndpointResponse404
from ...models.get_services_dhcp_server_apply_endpoint_response_405 import GetServicesDHCPServerApplyEndpointResponse405
from ...models.get_services_dhcp_server_apply_endpoint_response_406 import GetServicesDHCPServerApplyEndpointResponse406
from ...models.get_services_dhcp_server_apply_endpoint_response_409 import GetServicesDHCPServerApplyEndpointResponse409
from ...models.get_services_dhcp_server_apply_endpoint_response_415 import GetServicesDHCPServerApplyEndpointResponse415
from ...models.get_services_dhcp_server_apply_endpoint_response_422 import GetServicesDHCPServerApplyEndpointResponse422
from ...models.get_services_dhcp_server_apply_endpoint_response_424 import GetServicesDHCPServerApplyEndpointResponse424
from ...models.get_services_dhcp_server_apply_endpoint_response_500 import GetServicesDHCPServerApplyEndpointResponse500
from ...models.get_services_dhcp_server_apply_endpoint_response_503 import GetServicesDHCPServerApplyEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/dhcp_server/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesDHCPServerApplyEndpointResponse400
    | GetServicesDHCPServerApplyEndpointResponse401
    | GetServicesDHCPServerApplyEndpointResponse403
    | GetServicesDHCPServerApplyEndpointResponse404
    | GetServicesDHCPServerApplyEndpointResponse405
    | GetServicesDHCPServerApplyEndpointResponse406
    | GetServicesDHCPServerApplyEndpointResponse409
    | GetServicesDHCPServerApplyEndpointResponse415
    | GetServicesDHCPServerApplyEndpointResponse422
    | GetServicesDHCPServerApplyEndpointResponse424
    | GetServicesDHCPServerApplyEndpointResponse500
    | GetServicesDHCPServerApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesDHCPServerApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesDHCPServerApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesDHCPServerApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesDHCPServerApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesDHCPServerApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesDHCPServerApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesDHCPServerApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesDHCPServerApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesDHCPServerApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesDHCPServerApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesDHCPServerApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesDHCPServerApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesDHCPServerApplyEndpointResponse400
    | GetServicesDHCPServerApplyEndpointResponse401
    | GetServicesDHCPServerApplyEndpointResponse403
    | GetServicesDHCPServerApplyEndpointResponse404
    | GetServicesDHCPServerApplyEndpointResponse405
    | GetServicesDHCPServerApplyEndpointResponse406
    | GetServicesDHCPServerApplyEndpointResponse409
    | GetServicesDHCPServerApplyEndpointResponse415
    | GetServicesDHCPServerApplyEndpointResponse422
    | GetServicesDHCPServerApplyEndpointResponse424
    | GetServicesDHCPServerApplyEndpointResponse500
    | GetServicesDHCPServerApplyEndpointResponse503
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
    GetServicesDHCPServerApplyEndpointResponse400
    | GetServicesDHCPServerApplyEndpointResponse401
    | GetServicesDHCPServerApplyEndpointResponse403
    | GetServicesDHCPServerApplyEndpointResponse404
    | GetServicesDHCPServerApplyEndpointResponse405
    | GetServicesDHCPServerApplyEndpointResponse406
    | GetServicesDHCPServerApplyEndpointResponse409
    | GetServicesDHCPServerApplyEndpointResponse415
    | GetServicesDHCPServerApplyEndpointResponse422
    | GetServicesDHCPServerApplyEndpointResponse424
    | GetServicesDHCPServerApplyEndpointResponse500
    | GetServicesDHCPServerApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending DHCP Server change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDHCPServerApplyEndpointResponse400 | GetServicesDHCPServerApplyEndpointResponse401 | GetServicesDHCPServerApplyEndpointResponse403 | GetServicesDHCPServerApplyEndpointResponse404 | GetServicesDHCPServerApplyEndpointResponse405 | GetServicesDHCPServerApplyEndpointResponse406 | GetServicesDHCPServerApplyEndpointResponse409 | GetServicesDHCPServerApplyEndpointResponse415 | GetServicesDHCPServerApplyEndpointResponse422 | GetServicesDHCPServerApplyEndpointResponse424 | GetServicesDHCPServerApplyEndpointResponse500 | GetServicesDHCPServerApplyEndpointResponse503]
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
    GetServicesDHCPServerApplyEndpointResponse400
    | GetServicesDHCPServerApplyEndpointResponse401
    | GetServicesDHCPServerApplyEndpointResponse403
    | GetServicesDHCPServerApplyEndpointResponse404
    | GetServicesDHCPServerApplyEndpointResponse405
    | GetServicesDHCPServerApplyEndpointResponse406
    | GetServicesDHCPServerApplyEndpointResponse409
    | GetServicesDHCPServerApplyEndpointResponse415
    | GetServicesDHCPServerApplyEndpointResponse422
    | GetServicesDHCPServerApplyEndpointResponse424
    | GetServicesDHCPServerApplyEndpointResponse500
    | GetServicesDHCPServerApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending DHCP Server change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDHCPServerApplyEndpointResponse400 | GetServicesDHCPServerApplyEndpointResponse401 | GetServicesDHCPServerApplyEndpointResponse403 | GetServicesDHCPServerApplyEndpointResponse404 | GetServicesDHCPServerApplyEndpointResponse405 | GetServicesDHCPServerApplyEndpointResponse406 | GetServicesDHCPServerApplyEndpointResponse409 | GetServicesDHCPServerApplyEndpointResponse415 | GetServicesDHCPServerApplyEndpointResponse422 | GetServicesDHCPServerApplyEndpointResponse424 | GetServicesDHCPServerApplyEndpointResponse500 | GetServicesDHCPServerApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesDHCPServerApplyEndpointResponse400
    | GetServicesDHCPServerApplyEndpointResponse401
    | GetServicesDHCPServerApplyEndpointResponse403
    | GetServicesDHCPServerApplyEndpointResponse404
    | GetServicesDHCPServerApplyEndpointResponse405
    | GetServicesDHCPServerApplyEndpointResponse406
    | GetServicesDHCPServerApplyEndpointResponse409
    | GetServicesDHCPServerApplyEndpointResponse415
    | GetServicesDHCPServerApplyEndpointResponse422
    | GetServicesDHCPServerApplyEndpointResponse424
    | GetServicesDHCPServerApplyEndpointResponse500
    | GetServicesDHCPServerApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending DHCP Server change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesDHCPServerApplyEndpointResponse400 | GetServicesDHCPServerApplyEndpointResponse401 | GetServicesDHCPServerApplyEndpointResponse403 | GetServicesDHCPServerApplyEndpointResponse404 | GetServicesDHCPServerApplyEndpointResponse405 | GetServicesDHCPServerApplyEndpointResponse406 | GetServicesDHCPServerApplyEndpointResponse409 | GetServicesDHCPServerApplyEndpointResponse415 | GetServicesDHCPServerApplyEndpointResponse422 | GetServicesDHCPServerApplyEndpointResponse424 | GetServicesDHCPServerApplyEndpointResponse500 | GetServicesDHCPServerApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesDHCPServerApplyEndpointResponse400
    | GetServicesDHCPServerApplyEndpointResponse401
    | GetServicesDHCPServerApplyEndpointResponse403
    | GetServicesDHCPServerApplyEndpointResponse404
    | GetServicesDHCPServerApplyEndpointResponse405
    | GetServicesDHCPServerApplyEndpointResponse406
    | GetServicesDHCPServerApplyEndpointResponse409
    | GetServicesDHCPServerApplyEndpointResponse415
    | GetServicesDHCPServerApplyEndpointResponse422
    | GetServicesDHCPServerApplyEndpointResponse424
    | GetServicesDHCPServerApplyEndpointResponse500
    | GetServicesDHCPServerApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending DHCP Server change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-apply-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesDHCPServerApplyEndpointResponse400 | GetServicesDHCPServerApplyEndpointResponse401 | GetServicesDHCPServerApplyEndpointResponse403 | GetServicesDHCPServerApplyEndpointResponse404 | GetServicesDHCPServerApplyEndpointResponse405 | GetServicesDHCPServerApplyEndpointResponse406 | GetServicesDHCPServerApplyEndpointResponse409 | GetServicesDHCPServerApplyEndpointResponse415 | GetServicesDHCPServerApplyEndpointResponse422 | GetServicesDHCPServerApplyEndpointResponse424 | GetServicesDHCPServerApplyEndpointResponse500 | GetServicesDHCPServerApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
