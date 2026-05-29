from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_status_carp_endpoint_response_400 import GetStatusCARPEndpointResponse400
from ...models.get_status_carp_endpoint_response_401 import GetStatusCARPEndpointResponse401
from ...models.get_status_carp_endpoint_response_403 import GetStatusCARPEndpointResponse403
from ...models.get_status_carp_endpoint_response_404 import GetStatusCARPEndpointResponse404
from ...models.get_status_carp_endpoint_response_405 import GetStatusCARPEndpointResponse405
from ...models.get_status_carp_endpoint_response_406 import GetStatusCARPEndpointResponse406
from ...models.get_status_carp_endpoint_response_409 import GetStatusCARPEndpointResponse409
from ...models.get_status_carp_endpoint_response_415 import GetStatusCARPEndpointResponse415
from ...models.get_status_carp_endpoint_response_422 import GetStatusCARPEndpointResponse422
from ...models.get_status_carp_endpoint_response_424 import GetStatusCARPEndpointResponse424
from ...models.get_status_carp_endpoint_response_500 import GetStatusCARPEndpointResponse500
from ...models.get_status_carp_endpoint_response_503 import GetStatusCARPEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/status/carp",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetStatusCARPEndpointResponse400
    | GetStatusCARPEndpointResponse401
    | GetStatusCARPEndpointResponse403
    | GetStatusCARPEndpointResponse404
    | GetStatusCARPEndpointResponse405
    | GetStatusCARPEndpointResponse406
    | GetStatusCARPEndpointResponse409
    | GetStatusCARPEndpointResponse415
    | GetStatusCARPEndpointResponse422
    | GetStatusCARPEndpointResponse424
    | GetStatusCARPEndpointResponse500
    | GetStatusCARPEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetStatusCARPEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetStatusCARPEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetStatusCARPEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetStatusCARPEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetStatusCARPEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetStatusCARPEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetStatusCARPEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetStatusCARPEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetStatusCARPEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetStatusCARPEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetStatusCARPEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetStatusCARPEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetStatusCARPEndpointResponse400
    | GetStatusCARPEndpointResponse401
    | GetStatusCARPEndpointResponse403
    | GetStatusCARPEndpointResponse404
    | GetStatusCARPEndpointResponse405
    | GetStatusCARPEndpointResponse406
    | GetStatusCARPEndpointResponse409
    | GetStatusCARPEndpointResponse415
    | GetStatusCARPEndpointResponse422
    | GetStatusCARPEndpointResponse424
    | GetStatusCARPEndpointResponse500
    | GetStatusCARPEndpointResponse503
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
    GetStatusCARPEndpointResponse400
    | GetStatusCARPEndpointResponse401
    | GetStatusCARPEndpointResponse403
    | GetStatusCARPEndpointResponse404
    | GetStatusCARPEndpointResponse405
    | GetStatusCARPEndpointResponse406
    | GetStatusCARPEndpointResponse409
    | GetStatusCARPEndpointResponse415
    | GetStatusCARPEndpointResponse422
    | GetStatusCARPEndpointResponse424
    | GetStatusCARPEndpointResponse500
    | GetStatusCARPEndpointResponse503
]:
    """<h3>Description:</h3>Reads current CARP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CARP<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-status-carp-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatusCARPEndpointResponse400 | GetStatusCARPEndpointResponse401 | GetStatusCARPEndpointResponse403 | GetStatusCARPEndpointResponse404 | GetStatusCARPEndpointResponse405 | GetStatusCARPEndpointResponse406 | GetStatusCARPEndpointResponse409 | GetStatusCARPEndpointResponse415 | GetStatusCARPEndpointResponse422 | GetStatusCARPEndpointResponse424 | GetStatusCARPEndpointResponse500 | GetStatusCARPEndpointResponse503]
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
    GetStatusCARPEndpointResponse400
    | GetStatusCARPEndpointResponse401
    | GetStatusCARPEndpointResponse403
    | GetStatusCARPEndpointResponse404
    | GetStatusCARPEndpointResponse405
    | GetStatusCARPEndpointResponse406
    | GetStatusCARPEndpointResponse409
    | GetStatusCARPEndpointResponse415
    | GetStatusCARPEndpointResponse422
    | GetStatusCARPEndpointResponse424
    | GetStatusCARPEndpointResponse500
    | GetStatusCARPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current CARP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CARP<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-status-carp-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatusCARPEndpointResponse400 | GetStatusCARPEndpointResponse401 | GetStatusCARPEndpointResponse403 | GetStatusCARPEndpointResponse404 | GetStatusCARPEndpointResponse405 | GetStatusCARPEndpointResponse406 | GetStatusCARPEndpointResponse409 | GetStatusCARPEndpointResponse415 | GetStatusCARPEndpointResponse422 | GetStatusCARPEndpointResponse424 | GetStatusCARPEndpointResponse500 | GetStatusCARPEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetStatusCARPEndpointResponse400
    | GetStatusCARPEndpointResponse401
    | GetStatusCARPEndpointResponse403
    | GetStatusCARPEndpointResponse404
    | GetStatusCARPEndpointResponse405
    | GetStatusCARPEndpointResponse406
    | GetStatusCARPEndpointResponse409
    | GetStatusCARPEndpointResponse415
    | GetStatusCARPEndpointResponse422
    | GetStatusCARPEndpointResponse424
    | GetStatusCARPEndpointResponse500
    | GetStatusCARPEndpointResponse503
]:
    """<h3>Description:</h3>Reads current CARP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CARP<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-status-carp-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatusCARPEndpointResponse400 | GetStatusCARPEndpointResponse401 | GetStatusCARPEndpointResponse403 | GetStatusCARPEndpointResponse404 | GetStatusCARPEndpointResponse405 | GetStatusCARPEndpointResponse406 | GetStatusCARPEndpointResponse409 | GetStatusCARPEndpointResponse415 | GetStatusCARPEndpointResponse422 | GetStatusCARPEndpointResponse424 | GetStatusCARPEndpointResponse500 | GetStatusCARPEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetStatusCARPEndpointResponse400
    | GetStatusCARPEndpointResponse401
    | GetStatusCARPEndpointResponse403
    | GetStatusCARPEndpointResponse404
    | GetStatusCARPEndpointResponse405
    | GetStatusCARPEndpointResponse406
    | GetStatusCARPEndpointResponse409
    | GetStatusCARPEndpointResponse415
    | GetStatusCARPEndpointResponse422
    | GetStatusCARPEndpointResponse424
    | GetStatusCARPEndpointResponse500
    | GetStatusCARPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current CARP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CARP<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-status-carp-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatusCARPEndpointResponse400 | GetStatusCARPEndpointResponse401 | GetStatusCARPEndpointResponse403 | GetStatusCARPEndpointResponse404 | GetStatusCARPEndpointResponse405 | GetStatusCARPEndpointResponse406 | GetStatusCARPEndpointResponse409 | GetStatusCARPEndpointResponse415 | GetStatusCARPEndpointResponse422 | GetStatusCARPEndpointResponse424 | GetStatusCARPEndpointResponse500 | GetStatusCARPEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
