from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_version_endpoint_response_400 import GetSystemVersionEndpointResponse400
from ...models.get_system_version_endpoint_response_401 import GetSystemVersionEndpointResponse401
from ...models.get_system_version_endpoint_response_403 import GetSystemVersionEndpointResponse403
from ...models.get_system_version_endpoint_response_404 import GetSystemVersionEndpointResponse404
from ...models.get_system_version_endpoint_response_405 import GetSystemVersionEndpointResponse405
from ...models.get_system_version_endpoint_response_406 import GetSystemVersionEndpointResponse406
from ...models.get_system_version_endpoint_response_409 import GetSystemVersionEndpointResponse409
from ...models.get_system_version_endpoint_response_415 import GetSystemVersionEndpointResponse415
from ...models.get_system_version_endpoint_response_422 import GetSystemVersionEndpointResponse422
from ...models.get_system_version_endpoint_response_424 import GetSystemVersionEndpointResponse424
from ...models.get_system_version_endpoint_response_500 import GetSystemVersionEndpointResponse500
from ...models.get_system_version_endpoint_response_503 import GetSystemVersionEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/version",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemVersionEndpointResponse400
    | GetSystemVersionEndpointResponse401
    | GetSystemVersionEndpointResponse403
    | GetSystemVersionEndpointResponse404
    | GetSystemVersionEndpointResponse405
    | GetSystemVersionEndpointResponse406
    | GetSystemVersionEndpointResponse409
    | GetSystemVersionEndpointResponse415
    | GetSystemVersionEndpointResponse422
    | GetSystemVersionEndpointResponse424
    | GetSystemVersionEndpointResponse500
    | GetSystemVersionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemVersionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemVersionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemVersionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemVersionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemVersionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemVersionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemVersionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemVersionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemVersionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemVersionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemVersionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemVersionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemVersionEndpointResponse400
    | GetSystemVersionEndpointResponse401
    | GetSystemVersionEndpointResponse403
    | GetSystemVersionEndpointResponse404
    | GetSystemVersionEndpointResponse405
    | GetSystemVersionEndpointResponse406
    | GetSystemVersionEndpointResponse409
    | GetSystemVersionEndpointResponse415
    | GetSystemVersionEndpointResponse422
    | GetSystemVersionEndpointResponse424
    | GetSystemVersionEndpointResponse500
    | GetSystemVersionEndpointResponse503
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
    GetSystemVersionEndpointResponse400
    | GetSystemVersionEndpointResponse401
    | GetSystemVersionEndpointResponse403
    | GetSystemVersionEndpointResponse404
    | GetSystemVersionEndpointResponse405
    | GetSystemVersionEndpointResponse406
    | GetSystemVersionEndpointResponse409
    | GetSystemVersionEndpointResponse415
    | GetSystemVersionEndpointResponse422
    | GetSystemVersionEndpointResponse424
    | GetSystemVersionEndpointResponse500
    | GetSystemVersionEndpointResponse503
]:
    """<h3>Description:</h3>Reads current System Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-version-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemVersionEndpointResponse400 | GetSystemVersionEndpointResponse401 | GetSystemVersionEndpointResponse403 | GetSystemVersionEndpointResponse404 | GetSystemVersionEndpointResponse405 | GetSystemVersionEndpointResponse406 | GetSystemVersionEndpointResponse409 | GetSystemVersionEndpointResponse415 | GetSystemVersionEndpointResponse422 | GetSystemVersionEndpointResponse424 | GetSystemVersionEndpointResponse500 | GetSystemVersionEndpointResponse503]
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
    GetSystemVersionEndpointResponse400
    | GetSystemVersionEndpointResponse401
    | GetSystemVersionEndpointResponse403
    | GetSystemVersionEndpointResponse404
    | GetSystemVersionEndpointResponse405
    | GetSystemVersionEndpointResponse406
    | GetSystemVersionEndpointResponse409
    | GetSystemVersionEndpointResponse415
    | GetSystemVersionEndpointResponse422
    | GetSystemVersionEndpointResponse424
    | GetSystemVersionEndpointResponse500
    | GetSystemVersionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current System Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-version-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemVersionEndpointResponse400 | GetSystemVersionEndpointResponse401 | GetSystemVersionEndpointResponse403 | GetSystemVersionEndpointResponse404 | GetSystemVersionEndpointResponse405 | GetSystemVersionEndpointResponse406 | GetSystemVersionEndpointResponse409 | GetSystemVersionEndpointResponse415 | GetSystemVersionEndpointResponse422 | GetSystemVersionEndpointResponse424 | GetSystemVersionEndpointResponse500 | GetSystemVersionEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemVersionEndpointResponse400
    | GetSystemVersionEndpointResponse401
    | GetSystemVersionEndpointResponse403
    | GetSystemVersionEndpointResponse404
    | GetSystemVersionEndpointResponse405
    | GetSystemVersionEndpointResponse406
    | GetSystemVersionEndpointResponse409
    | GetSystemVersionEndpointResponse415
    | GetSystemVersionEndpointResponse422
    | GetSystemVersionEndpointResponse424
    | GetSystemVersionEndpointResponse500
    | GetSystemVersionEndpointResponse503
]:
    """<h3>Description:</h3>Reads current System Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-version-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemVersionEndpointResponse400 | GetSystemVersionEndpointResponse401 | GetSystemVersionEndpointResponse403 | GetSystemVersionEndpointResponse404 | GetSystemVersionEndpointResponse405 | GetSystemVersionEndpointResponse406 | GetSystemVersionEndpointResponse409 | GetSystemVersionEndpointResponse415 | GetSystemVersionEndpointResponse422 | GetSystemVersionEndpointResponse424 | GetSystemVersionEndpointResponse500 | GetSystemVersionEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemVersionEndpointResponse400
    | GetSystemVersionEndpointResponse401
    | GetSystemVersionEndpointResponse403
    | GetSystemVersionEndpointResponse404
    | GetSystemVersionEndpointResponse405
    | GetSystemVersionEndpointResponse406
    | GetSystemVersionEndpointResponse409
    | GetSystemVersionEndpointResponse415
    | GetSystemVersionEndpointResponse422
    | GetSystemVersionEndpointResponse424
    | GetSystemVersionEndpointResponse500
    | GetSystemVersionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current System Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-version-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemVersionEndpointResponse400 | GetSystemVersionEndpointResponse401 | GetSystemVersionEndpointResponse403 | GetSystemVersionEndpointResponse404 | GetSystemVersionEndpointResponse405 | GetSystemVersionEndpointResponse406 | GetSystemVersionEndpointResponse409 | GetSystemVersionEndpointResponse415 | GetSystemVersionEndpointResponse422 | GetSystemVersionEndpointResponse424 | GetSystemVersionEndpointResponse500 | GetSystemVersionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
