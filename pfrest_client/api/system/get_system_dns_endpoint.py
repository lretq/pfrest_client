from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_dns_endpoint_response_400 import GetSystemDNSEndpointResponse400
from ...models.get_system_dns_endpoint_response_401 import GetSystemDNSEndpointResponse401
from ...models.get_system_dns_endpoint_response_403 import GetSystemDNSEndpointResponse403
from ...models.get_system_dns_endpoint_response_404 import GetSystemDNSEndpointResponse404
from ...models.get_system_dns_endpoint_response_405 import GetSystemDNSEndpointResponse405
from ...models.get_system_dns_endpoint_response_406 import GetSystemDNSEndpointResponse406
from ...models.get_system_dns_endpoint_response_409 import GetSystemDNSEndpointResponse409
from ...models.get_system_dns_endpoint_response_415 import GetSystemDNSEndpointResponse415
from ...models.get_system_dns_endpoint_response_422 import GetSystemDNSEndpointResponse422
from ...models.get_system_dns_endpoint_response_424 import GetSystemDNSEndpointResponse424
from ...models.get_system_dns_endpoint_response_500 import GetSystemDNSEndpointResponse500
from ...models.get_system_dns_endpoint_response_503 import GetSystemDNSEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/dns",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemDNSEndpointResponse400
    | GetSystemDNSEndpointResponse401
    | GetSystemDNSEndpointResponse403
    | GetSystemDNSEndpointResponse404
    | GetSystemDNSEndpointResponse405
    | GetSystemDNSEndpointResponse406
    | GetSystemDNSEndpointResponse409
    | GetSystemDNSEndpointResponse415
    | GetSystemDNSEndpointResponse422
    | GetSystemDNSEndpointResponse424
    | GetSystemDNSEndpointResponse500
    | GetSystemDNSEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemDNSEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemDNSEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemDNSEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemDNSEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemDNSEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemDNSEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemDNSEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemDNSEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemDNSEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemDNSEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemDNSEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemDNSEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemDNSEndpointResponse400
    | GetSystemDNSEndpointResponse401
    | GetSystemDNSEndpointResponse403
    | GetSystemDNSEndpointResponse404
    | GetSystemDNSEndpointResponse405
    | GetSystemDNSEndpointResponse406
    | GetSystemDNSEndpointResponse409
    | GetSystemDNSEndpointResponse415
    | GetSystemDNSEndpointResponse422
    | GetSystemDNSEndpointResponse424
    | GetSystemDNSEndpointResponse500
    | GetSystemDNSEndpointResponse503
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
    GetSystemDNSEndpointResponse400
    | GetSystemDNSEndpointResponse401
    | GetSystemDNSEndpointResponse403
    | GetSystemDNSEndpointResponse404
    | GetSystemDNSEndpointResponse405
    | GetSystemDNSEndpointResponse406
    | GetSystemDNSEndpointResponse409
    | GetSystemDNSEndpointResponse415
    | GetSystemDNSEndpointResponse422
    | GetSystemDNSEndpointResponse424
    | GetSystemDNSEndpointResponse500
    | GetSystemDNSEndpointResponse503
]:
    """<h3>Description:</h3>Reads the current system DNS settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemDNS<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-dns-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemDNSEndpointResponse400 | GetSystemDNSEndpointResponse401 | GetSystemDNSEndpointResponse403 | GetSystemDNSEndpointResponse404 | GetSystemDNSEndpointResponse405 | GetSystemDNSEndpointResponse406 | GetSystemDNSEndpointResponse409 | GetSystemDNSEndpointResponse415 | GetSystemDNSEndpointResponse422 | GetSystemDNSEndpointResponse424 | GetSystemDNSEndpointResponse500 | GetSystemDNSEndpointResponse503]
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
    GetSystemDNSEndpointResponse400
    | GetSystemDNSEndpointResponse401
    | GetSystemDNSEndpointResponse403
    | GetSystemDNSEndpointResponse404
    | GetSystemDNSEndpointResponse405
    | GetSystemDNSEndpointResponse406
    | GetSystemDNSEndpointResponse409
    | GetSystemDNSEndpointResponse415
    | GetSystemDNSEndpointResponse422
    | GetSystemDNSEndpointResponse424
    | GetSystemDNSEndpointResponse500
    | GetSystemDNSEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads the current system DNS settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemDNS<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-dns-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemDNSEndpointResponse400 | GetSystemDNSEndpointResponse401 | GetSystemDNSEndpointResponse403 | GetSystemDNSEndpointResponse404 | GetSystemDNSEndpointResponse405 | GetSystemDNSEndpointResponse406 | GetSystemDNSEndpointResponse409 | GetSystemDNSEndpointResponse415 | GetSystemDNSEndpointResponse422 | GetSystemDNSEndpointResponse424 | GetSystemDNSEndpointResponse500 | GetSystemDNSEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemDNSEndpointResponse400
    | GetSystemDNSEndpointResponse401
    | GetSystemDNSEndpointResponse403
    | GetSystemDNSEndpointResponse404
    | GetSystemDNSEndpointResponse405
    | GetSystemDNSEndpointResponse406
    | GetSystemDNSEndpointResponse409
    | GetSystemDNSEndpointResponse415
    | GetSystemDNSEndpointResponse422
    | GetSystemDNSEndpointResponse424
    | GetSystemDNSEndpointResponse500
    | GetSystemDNSEndpointResponse503
]:
    """<h3>Description:</h3>Reads the current system DNS settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemDNS<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-dns-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemDNSEndpointResponse400 | GetSystemDNSEndpointResponse401 | GetSystemDNSEndpointResponse403 | GetSystemDNSEndpointResponse404 | GetSystemDNSEndpointResponse405 | GetSystemDNSEndpointResponse406 | GetSystemDNSEndpointResponse409 | GetSystemDNSEndpointResponse415 | GetSystemDNSEndpointResponse422 | GetSystemDNSEndpointResponse424 | GetSystemDNSEndpointResponse500 | GetSystemDNSEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemDNSEndpointResponse400
    | GetSystemDNSEndpointResponse401
    | GetSystemDNSEndpointResponse403
    | GetSystemDNSEndpointResponse404
    | GetSystemDNSEndpointResponse405
    | GetSystemDNSEndpointResponse406
    | GetSystemDNSEndpointResponse409
    | GetSystemDNSEndpointResponse415
    | GetSystemDNSEndpointResponse422
    | GetSystemDNSEndpointResponse424
    | GetSystemDNSEndpointResponse500
    | GetSystemDNSEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads the current system DNS settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemDNS<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-dns-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemDNSEndpointResponse400 | GetSystemDNSEndpointResponse401 | GetSystemDNSEndpointResponse403 | GetSystemDNSEndpointResponse404 | GetSystemDNSEndpointResponse405 | GetSystemDNSEndpointResponse406 | GetSystemDNSEndpointResponse409 | GetSystemDNSEndpointResponse415 | GetSystemDNSEndpointResponse422 | GetSystemDNSEndpointResponse424 | GetSystemDNSEndpointResponse500 | GetSystemDNSEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
