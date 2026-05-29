from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_console_endpoint_response_400 import GetSystemConsoleEndpointResponse400
from ...models.get_system_console_endpoint_response_401 import GetSystemConsoleEndpointResponse401
from ...models.get_system_console_endpoint_response_403 import GetSystemConsoleEndpointResponse403
from ...models.get_system_console_endpoint_response_404 import GetSystemConsoleEndpointResponse404
from ...models.get_system_console_endpoint_response_405 import GetSystemConsoleEndpointResponse405
from ...models.get_system_console_endpoint_response_406 import GetSystemConsoleEndpointResponse406
from ...models.get_system_console_endpoint_response_409 import GetSystemConsoleEndpointResponse409
from ...models.get_system_console_endpoint_response_415 import GetSystemConsoleEndpointResponse415
from ...models.get_system_console_endpoint_response_422 import GetSystemConsoleEndpointResponse422
from ...models.get_system_console_endpoint_response_424 import GetSystemConsoleEndpointResponse424
from ...models.get_system_console_endpoint_response_500 import GetSystemConsoleEndpointResponse500
from ...models.get_system_console_endpoint_response_503 import GetSystemConsoleEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/console",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemConsoleEndpointResponse400
    | GetSystemConsoleEndpointResponse401
    | GetSystemConsoleEndpointResponse403
    | GetSystemConsoleEndpointResponse404
    | GetSystemConsoleEndpointResponse405
    | GetSystemConsoleEndpointResponse406
    | GetSystemConsoleEndpointResponse409
    | GetSystemConsoleEndpointResponse415
    | GetSystemConsoleEndpointResponse422
    | GetSystemConsoleEndpointResponse424
    | GetSystemConsoleEndpointResponse500
    | GetSystemConsoleEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemConsoleEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemConsoleEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemConsoleEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemConsoleEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemConsoleEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemConsoleEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemConsoleEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemConsoleEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemConsoleEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemConsoleEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemConsoleEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemConsoleEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemConsoleEndpointResponse400
    | GetSystemConsoleEndpointResponse401
    | GetSystemConsoleEndpointResponse403
    | GetSystemConsoleEndpointResponse404
    | GetSystemConsoleEndpointResponse405
    | GetSystemConsoleEndpointResponse406
    | GetSystemConsoleEndpointResponse409
    | GetSystemConsoleEndpointResponse415
    | GetSystemConsoleEndpointResponse422
    | GetSystemConsoleEndpointResponse424
    | GetSystemConsoleEndpointResponse500
    | GetSystemConsoleEndpointResponse503
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
    GetSystemConsoleEndpointResponse400
    | GetSystemConsoleEndpointResponse401
    | GetSystemConsoleEndpointResponse403
    | GetSystemConsoleEndpointResponse404
    | GetSystemConsoleEndpointResponse405
    | GetSystemConsoleEndpointResponse406
    | GetSystemConsoleEndpointResponse409
    | GetSystemConsoleEndpointResponse415
    | GetSystemConsoleEndpointResponse422
    | GetSystemConsoleEndpointResponse424
    | GetSystemConsoleEndpointResponse500
    | GetSystemConsoleEndpointResponse503
]:
    """<h3>Description:</h3>Reads current System Console.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemConsole<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-console-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemConsoleEndpointResponse400 | GetSystemConsoleEndpointResponse401 | GetSystemConsoleEndpointResponse403 | GetSystemConsoleEndpointResponse404 | GetSystemConsoleEndpointResponse405 | GetSystemConsoleEndpointResponse406 | GetSystemConsoleEndpointResponse409 | GetSystemConsoleEndpointResponse415 | GetSystemConsoleEndpointResponse422 | GetSystemConsoleEndpointResponse424 | GetSystemConsoleEndpointResponse500 | GetSystemConsoleEndpointResponse503]
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
    GetSystemConsoleEndpointResponse400
    | GetSystemConsoleEndpointResponse401
    | GetSystemConsoleEndpointResponse403
    | GetSystemConsoleEndpointResponse404
    | GetSystemConsoleEndpointResponse405
    | GetSystemConsoleEndpointResponse406
    | GetSystemConsoleEndpointResponse409
    | GetSystemConsoleEndpointResponse415
    | GetSystemConsoleEndpointResponse422
    | GetSystemConsoleEndpointResponse424
    | GetSystemConsoleEndpointResponse500
    | GetSystemConsoleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current System Console.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemConsole<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-console-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemConsoleEndpointResponse400 | GetSystemConsoleEndpointResponse401 | GetSystemConsoleEndpointResponse403 | GetSystemConsoleEndpointResponse404 | GetSystemConsoleEndpointResponse405 | GetSystemConsoleEndpointResponse406 | GetSystemConsoleEndpointResponse409 | GetSystemConsoleEndpointResponse415 | GetSystemConsoleEndpointResponse422 | GetSystemConsoleEndpointResponse424 | GetSystemConsoleEndpointResponse500 | GetSystemConsoleEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemConsoleEndpointResponse400
    | GetSystemConsoleEndpointResponse401
    | GetSystemConsoleEndpointResponse403
    | GetSystemConsoleEndpointResponse404
    | GetSystemConsoleEndpointResponse405
    | GetSystemConsoleEndpointResponse406
    | GetSystemConsoleEndpointResponse409
    | GetSystemConsoleEndpointResponse415
    | GetSystemConsoleEndpointResponse422
    | GetSystemConsoleEndpointResponse424
    | GetSystemConsoleEndpointResponse500
    | GetSystemConsoleEndpointResponse503
]:
    """<h3>Description:</h3>Reads current System Console.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemConsole<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-console-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemConsoleEndpointResponse400 | GetSystemConsoleEndpointResponse401 | GetSystemConsoleEndpointResponse403 | GetSystemConsoleEndpointResponse404 | GetSystemConsoleEndpointResponse405 | GetSystemConsoleEndpointResponse406 | GetSystemConsoleEndpointResponse409 | GetSystemConsoleEndpointResponse415 | GetSystemConsoleEndpointResponse422 | GetSystemConsoleEndpointResponse424 | GetSystemConsoleEndpointResponse500 | GetSystemConsoleEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemConsoleEndpointResponse400
    | GetSystemConsoleEndpointResponse401
    | GetSystemConsoleEndpointResponse403
    | GetSystemConsoleEndpointResponse404
    | GetSystemConsoleEndpointResponse405
    | GetSystemConsoleEndpointResponse406
    | GetSystemConsoleEndpointResponse409
    | GetSystemConsoleEndpointResponse415
    | GetSystemConsoleEndpointResponse422
    | GetSystemConsoleEndpointResponse424
    | GetSystemConsoleEndpointResponse500
    | GetSystemConsoleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current System Console.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemConsole<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-console-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemConsoleEndpointResponse400 | GetSystemConsoleEndpointResponse401 | GetSystemConsoleEndpointResponse403 | GetSystemConsoleEndpointResponse404 | GetSystemConsoleEndpointResponse405 | GetSystemConsoleEndpointResponse406 | GetSystemConsoleEndpointResponse409 | GetSystemConsoleEndpointResponse415 | GetSystemConsoleEndpointResponse422 | GetSystemConsoleEndpointResponse424 | GetSystemConsoleEndpointResponse500 | GetSystemConsoleEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
