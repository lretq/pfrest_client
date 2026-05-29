from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_timezone_endpoint_response_400 import GetSystemTimezoneEndpointResponse400
from ...models.get_system_timezone_endpoint_response_401 import GetSystemTimezoneEndpointResponse401
from ...models.get_system_timezone_endpoint_response_403 import GetSystemTimezoneEndpointResponse403
from ...models.get_system_timezone_endpoint_response_404 import GetSystemTimezoneEndpointResponse404
from ...models.get_system_timezone_endpoint_response_405 import GetSystemTimezoneEndpointResponse405
from ...models.get_system_timezone_endpoint_response_406 import GetSystemTimezoneEndpointResponse406
from ...models.get_system_timezone_endpoint_response_409 import GetSystemTimezoneEndpointResponse409
from ...models.get_system_timezone_endpoint_response_415 import GetSystemTimezoneEndpointResponse415
from ...models.get_system_timezone_endpoint_response_422 import GetSystemTimezoneEndpointResponse422
from ...models.get_system_timezone_endpoint_response_424 import GetSystemTimezoneEndpointResponse424
from ...models.get_system_timezone_endpoint_response_500 import GetSystemTimezoneEndpointResponse500
from ...models.get_system_timezone_endpoint_response_503 import GetSystemTimezoneEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/timezone",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemTimezoneEndpointResponse400
    | GetSystemTimezoneEndpointResponse401
    | GetSystemTimezoneEndpointResponse403
    | GetSystemTimezoneEndpointResponse404
    | GetSystemTimezoneEndpointResponse405
    | GetSystemTimezoneEndpointResponse406
    | GetSystemTimezoneEndpointResponse409
    | GetSystemTimezoneEndpointResponse415
    | GetSystemTimezoneEndpointResponse422
    | GetSystemTimezoneEndpointResponse424
    | GetSystemTimezoneEndpointResponse500
    | GetSystemTimezoneEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemTimezoneEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemTimezoneEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemTimezoneEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemTimezoneEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemTimezoneEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemTimezoneEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemTimezoneEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemTimezoneEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemTimezoneEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemTimezoneEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemTimezoneEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemTimezoneEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemTimezoneEndpointResponse400
    | GetSystemTimezoneEndpointResponse401
    | GetSystemTimezoneEndpointResponse403
    | GetSystemTimezoneEndpointResponse404
    | GetSystemTimezoneEndpointResponse405
    | GetSystemTimezoneEndpointResponse406
    | GetSystemTimezoneEndpointResponse409
    | GetSystemTimezoneEndpointResponse415
    | GetSystemTimezoneEndpointResponse422
    | GetSystemTimezoneEndpointResponse424
    | GetSystemTimezoneEndpointResponse500
    | GetSystemTimezoneEndpointResponse503
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
    GetSystemTimezoneEndpointResponse400
    | GetSystemTimezoneEndpointResponse401
    | GetSystemTimezoneEndpointResponse403
    | GetSystemTimezoneEndpointResponse404
    | GetSystemTimezoneEndpointResponse405
    | GetSystemTimezoneEndpointResponse406
    | GetSystemTimezoneEndpointResponse409
    | GetSystemTimezoneEndpointResponse415
    | GetSystemTimezoneEndpointResponse422
    | GetSystemTimezoneEndpointResponse424
    | GetSystemTimezoneEndpointResponse500
    | GetSystemTimezoneEndpointResponse503
]:
    """<h3>Description:</h3>Reads the current system timezone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTimezone<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-timezone-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemTimezoneEndpointResponse400 | GetSystemTimezoneEndpointResponse401 | GetSystemTimezoneEndpointResponse403 | GetSystemTimezoneEndpointResponse404 | GetSystemTimezoneEndpointResponse405 | GetSystemTimezoneEndpointResponse406 | GetSystemTimezoneEndpointResponse409 | GetSystemTimezoneEndpointResponse415 | GetSystemTimezoneEndpointResponse422 | GetSystemTimezoneEndpointResponse424 | GetSystemTimezoneEndpointResponse500 | GetSystemTimezoneEndpointResponse503]
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
    GetSystemTimezoneEndpointResponse400
    | GetSystemTimezoneEndpointResponse401
    | GetSystemTimezoneEndpointResponse403
    | GetSystemTimezoneEndpointResponse404
    | GetSystemTimezoneEndpointResponse405
    | GetSystemTimezoneEndpointResponse406
    | GetSystemTimezoneEndpointResponse409
    | GetSystemTimezoneEndpointResponse415
    | GetSystemTimezoneEndpointResponse422
    | GetSystemTimezoneEndpointResponse424
    | GetSystemTimezoneEndpointResponse500
    | GetSystemTimezoneEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads the current system timezone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTimezone<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-timezone-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemTimezoneEndpointResponse400 | GetSystemTimezoneEndpointResponse401 | GetSystemTimezoneEndpointResponse403 | GetSystemTimezoneEndpointResponse404 | GetSystemTimezoneEndpointResponse405 | GetSystemTimezoneEndpointResponse406 | GetSystemTimezoneEndpointResponse409 | GetSystemTimezoneEndpointResponse415 | GetSystemTimezoneEndpointResponse422 | GetSystemTimezoneEndpointResponse424 | GetSystemTimezoneEndpointResponse500 | GetSystemTimezoneEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemTimezoneEndpointResponse400
    | GetSystemTimezoneEndpointResponse401
    | GetSystemTimezoneEndpointResponse403
    | GetSystemTimezoneEndpointResponse404
    | GetSystemTimezoneEndpointResponse405
    | GetSystemTimezoneEndpointResponse406
    | GetSystemTimezoneEndpointResponse409
    | GetSystemTimezoneEndpointResponse415
    | GetSystemTimezoneEndpointResponse422
    | GetSystemTimezoneEndpointResponse424
    | GetSystemTimezoneEndpointResponse500
    | GetSystemTimezoneEndpointResponse503
]:
    """<h3>Description:</h3>Reads the current system timezone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTimezone<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-timezone-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemTimezoneEndpointResponse400 | GetSystemTimezoneEndpointResponse401 | GetSystemTimezoneEndpointResponse403 | GetSystemTimezoneEndpointResponse404 | GetSystemTimezoneEndpointResponse405 | GetSystemTimezoneEndpointResponse406 | GetSystemTimezoneEndpointResponse409 | GetSystemTimezoneEndpointResponse415 | GetSystemTimezoneEndpointResponse422 | GetSystemTimezoneEndpointResponse424 | GetSystemTimezoneEndpointResponse500 | GetSystemTimezoneEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemTimezoneEndpointResponse400
    | GetSystemTimezoneEndpointResponse401
    | GetSystemTimezoneEndpointResponse403
    | GetSystemTimezoneEndpointResponse404
    | GetSystemTimezoneEndpointResponse405
    | GetSystemTimezoneEndpointResponse406
    | GetSystemTimezoneEndpointResponse409
    | GetSystemTimezoneEndpointResponse415
    | GetSystemTimezoneEndpointResponse422
    | GetSystemTimezoneEndpointResponse424
    | GetSystemTimezoneEndpointResponse500
    | GetSystemTimezoneEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads the current system timezone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTimezone<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-timezone-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemTimezoneEndpointResponse400 | GetSystemTimezoneEndpointResponse401 | GetSystemTimezoneEndpointResponse403 | GetSystemTimezoneEndpointResponse404 | GetSystemTimezoneEndpointResponse405 | GetSystemTimezoneEndpointResponse406 | GetSystemTimezoneEndpointResponse409 | GetSystemTimezoneEndpointResponse415 | GetSystemTimezoneEndpointResponse422 | GetSystemTimezoneEndpointResponse424 | GetSystemTimezoneEndpointResponse500 | GetSystemTimezoneEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
