from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_hostname_endpoint_response_400 import GetSystemHostnameEndpointResponse400
from ...models.get_system_hostname_endpoint_response_401 import GetSystemHostnameEndpointResponse401
from ...models.get_system_hostname_endpoint_response_403 import GetSystemHostnameEndpointResponse403
from ...models.get_system_hostname_endpoint_response_404 import GetSystemHostnameEndpointResponse404
from ...models.get_system_hostname_endpoint_response_405 import GetSystemHostnameEndpointResponse405
from ...models.get_system_hostname_endpoint_response_406 import GetSystemHostnameEndpointResponse406
from ...models.get_system_hostname_endpoint_response_409 import GetSystemHostnameEndpointResponse409
from ...models.get_system_hostname_endpoint_response_415 import GetSystemHostnameEndpointResponse415
from ...models.get_system_hostname_endpoint_response_422 import GetSystemHostnameEndpointResponse422
from ...models.get_system_hostname_endpoint_response_424 import GetSystemHostnameEndpointResponse424
from ...models.get_system_hostname_endpoint_response_500 import GetSystemHostnameEndpointResponse500
from ...models.get_system_hostname_endpoint_response_503 import GetSystemHostnameEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/hostname",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemHostnameEndpointResponse400
    | GetSystemHostnameEndpointResponse401
    | GetSystemHostnameEndpointResponse403
    | GetSystemHostnameEndpointResponse404
    | GetSystemHostnameEndpointResponse405
    | GetSystemHostnameEndpointResponse406
    | GetSystemHostnameEndpointResponse409
    | GetSystemHostnameEndpointResponse415
    | GetSystemHostnameEndpointResponse422
    | GetSystemHostnameEndpointResponse424
    | GetSystemHostnameEndpointResponse500
    | GetSystemHostnameEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemHostnameEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemHostnameEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemHostnameEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemHostnameEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemHostnameEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemHostnameEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemHostnameEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemHostnameEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemHostnameEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemHostnameEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemHostnameEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemHostnameEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemHostnameEndpointResponse400
    | GetSystemHostnameEndpointResponse401
    | GetSystemHostnameEndpointResponse403
    | GetSystemHostnameEndpointResponse404
    | GetSystemHostnameEndpointResponse405
    | GetSystemHostnameEndpointResponse406
    | GetSystemHostnameEndpointResponse409
    | GetSystemHostnameEndpointResponse415
    | GetSystemHostnameEndpointResponse422
    | GetSystemHostnameEndpointResponse424
    | GetSystemHostnameEndpointResponse500
    | GetSystemHostnameEndpointResponse503
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
    GetSystemHostnameEndpointResponse400
    | GetSystemHostnameEndpointResponse401
    | GetSystemHostnameEndpointResponse403
    | GetSystemHostnameEndpointResponse404
    | GetSystemHostnameEndpointResponse405
    | GetSystemHostnameEndpointResponse406
    | GetSystemHostnameEndpointResponse409
    | GetSystemHostnameEndpointResponse415
    | GetSystemHostnameEndpointResponse422
    | GetSystemHostnameEndpointResponse424
    | GetSystemHostnameEndpointResponse500
    | GetSystemHostnameEndpointResponse503
]:
    """<h3>Description:</h3>Reads the current system hostname.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemHostname<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-hostname-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemHostnameEndpointResponse400 | GetSystemHostnameEndpointResponse401 | GetSystemHostnameEndpointResponse403 | GetSystemHostnameEndpointResponse404 | GetSystemHostnameEndpointResponse405 | GetSystemHostnameEndpointResponse406 | GetSystemHostnameEndpointResponse409 | GetSystemHostnameEndpointResponse415 | GetSystemHostnameEndpointResponse422 | GetSystemHostnameEndpointResponse424 | GetSystemHostnameEndpointResponse500 | GetSystemHostnameEndpointResponse503]
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
    GetSystemHostnameEndpointResponse400
    | GetSystemHostnameEndpointResponse401
    | GetSystemHostnameEndpointResponse403
    | GetSystemHostnameEndpointResponse404
    | GetSystemHostnameEndpointResponse405
    | GetSystemHostnameEndpointResponse406
    | GetSystemHostnameEndpointResponse409
    | GetSystemHostnameEndpointResponse415
    | GetSystemHostnameEndpointResponse422
    | GetSystemHostnameEndpointResponse424
    | GetSystemHostnameEndpointResponse500
    | GetSystemHostnameEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads the current system hostname.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemHostname<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-hostname-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemHostnameEndpointResponse400 | GetSystemHostnameEndpointResponse401 | GetSystemHostnameEndpointResponse403 | GetSystemHostnameEndpointResponse404 | GetSystemHostnameEndpointResponse405 | GetSystemHostnameEndpointResponse406 | GetSystemHostnameEndpointResponse409 | GetSystemHostnameEndpointResponse415 | GetSystemHostnameEndpointResponse422 | GetSystemHostnameEndpointResponse424 | GetSystemHostnameEndpointResponse500 | GetSystemHostnameEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemHostnameEndpointResponse400
    | GetSystemHostnameEndpointResponse401
    | GetSystemHostnameEndpointResponse403
    | GetSystemHostnameEndpointResponse404
    | GetSystemHostnameEndpointResponse405
    | GetSystemHostnameEndpointResponse406
    | GetSystemHostnameEndpointResponse409
    | GetSystemHostnameEndpointResponse415
    | GetSystemHostnameEndpointResponse422
    | GetSystemHostnameEndpointResponse424
    | GetSystemHostnameEndpointResponse500
    | GetSystemHostnameEndpointResponse503
]:
    """<h3>Description:</h3>Reads the current system hostname.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemHostname<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-hostname-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemHostnameEndpointResponse400 | GetSystemHostnameEndpointResponse401 | GetSystemHostnameEndpointResponse403 | GetSystemHostnameEndpointResponse404 | GetSystemHostnameEndpointResponse405 | GetSystemHostnameEndpointResponse406 | GetSystemHostnameEndpointResponse409 | GetSystemHostnameEndpointResponse415 | GetSystemHostnameEndpointResponse422 | GetSystemHostnameEndpointResponse424 | GetSystemHostnameEndpointResponse500 | GetSystemHostnameEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemHostnameEndpointResponse400
    | GetSystemHostnameEndpointResponse401
    | GetSystemHostnameEndpointResponse403
    | GetSystemHostnameEndpointResponse404
    | GetSystemHostnameEndpointResponse405
    | GetSystemHostnameEndpointResponse406
    | GetSystemHostnameEndpointResponse409
    | GetSystemHostnameEndpointResponse415
    | GetSystemHostnameEndpointResponse422
    | GetSystemHostnameEndpointResponse424
    | GetSystemHostnameEndpointResponse500
    | GetSystemHostnameEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads the current system hostname.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemHostname<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-hostname-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemHostnameEndpointResponse400 | GetSystemHostnameEndpointResponse401 | GetSystemHostnameEndpointResponse403 | GetSystemHostnameEndpointResponse404 | GetSystemHostnameEndpointResponse405 | GetSystemHostnameEndpointResponse406 | GetSystemHostnameEndpointResponse409 | GetSystemHostnameEndpointResponse415 | GetSystemHostnameEndpointResponse422 | GetSystemHostnameEndpointResponse424 | GetSystemHostnameEndpointResponse500 | GetSystemHostnameEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
