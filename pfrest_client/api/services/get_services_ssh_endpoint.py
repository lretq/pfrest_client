from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_ssh_endpoint_response_400 import GetServicesSSHEndpointResponse400
from ...models.get_services_ssh_endpoint_response_401 import GetServicesSSHEndpointResponse401
from ...models.get_services_ssh_endpoint_response_403 import GetServicesSSHEndpointResponse403
from ...models.get_services_ssh_endpoint_response_404 import GetServicesSSHEndpointResponse404
from ...models.get_services_ssh_endpoint_response_405 import GetServicesSSHEndpointResponse405
from ...models.get_services_ssh_endpoint_response_406 import GetServicesSSHEndpointResponse406
from ...models.get_services_ssh_endpoint_response_409 import GetServicesSSHEndpointResponse409
from ...models.get_services_ssh_endpoint_response_415 import GetServicesSSHEndpointResponse415
from ...models.get_services_ssh_endpoint_response_422 import GetServicesSSHEndpointResponse422
from ...models.get_services_ssh_endpoint_response_424 import GetServicesSSHEndpointResponse424
from ...models.get_services_ssh_endpoint_response_500 import GetServicesSSHEndpointResponse500
from ...models.get_services_ssh_endpoint_response_503 import GetServicesSSHEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/ssh",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesSSHEndpointResponse400
    | GetServicesSSHEndpointResponse401
    | GetServicesSSHEndpointResponse403
    | GetServicesSSHEndpointResponse404
    | GetServicesSSHEndpointResponse405
    | GetServicesSSHEndpointResponse406
    | GetServicesSSHEndpointResponse409
    | GetServicesSSHEndpointResponse415
    | GetServicesSSHEndpointResponse422
    | GetServicesSSHEndpointResponse424
    | GetServicesSSHEndpointResponse500
    | GetServicesSSHEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesSSHEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesSSHEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesSSHEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesSSHEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesSSHEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesSSHEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesSSHEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesSSHEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesSSHEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesSSHEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesSSHEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesSSHEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesSSHEndpointResponse400
    | GetServicesSSHEndpointResponse401
    | GetServicesSSHEndpointResponse403
    | GetServicesSSHEndpointResponse404
    | GetServicesSSHEndpointResponse405
    | GetServicesSSHEndpointResponse406
    | GetServicesSSHEndpointResponse409
    | GetServicesSSHEndpointResponse415
    | GetServicesSSHEndpointResponse422
    | GetServicesSSHEndpointResponse424
    | GetServicesSSHEndpointResponse500
    | GetServicesSSHEndpointResponse503
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
    GetServicesSSHEndpointResponse400
    | GetServicesSSHEndpointResponse401
    | GetServicesSSHEndpointResponse403
    | GetServicesSSHEndpointResponse404
    | GetServicesSSHEndpointResponse405
    | GetServicesSSHEndpointResponse406
    | GetServicesSSHEndpointResponse409
    | GetServicesSSHEndpointResponse415
    | GetServicesSSHEndpointResponse422
    | GetServicesSSHEndpointResponse424
    | GetServicesSSHEndpointResponse500
    | GetServicesSSHEndpointResponse503
]:
    """<h3>Description:</h3>Reads the current SSH server settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SSH<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-ssh-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesSSHEndpointResponse400 | GetServicesSSHEndpointResponse401 | GetServicesSSHEndpointResponse403 | GetServicesSSHEndpointResponse404 | GetServicesSSHEndpointResponse405 | GetServicesSSHEndpointResponse406 | GetServicesSSHEndpointResponse409 | GetServicesSSHEndpointResponse415 | GetServicesSSHEndpointResponse422 | GetServicesSSHEndpointResponse424 | GetServicesSSHEndpointResponse500 | GetServicesSSHEndpointResponse503]
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
    GetServicesSSHEndpointResponse400
    | GetServicesSSHEndpointResponse401
    | GetServicesSSHEndpointResponse403
    | GetServicesSSHEndpointResponse404
    | GetServicesSSHEndpointResponse405
    | GetServicesSSHEndpointResponse406
    | GetServicesSSHEndpointResponse409
    | GetServicesSSHEndpointResponse415
    | GetServicesSSHEndpointResponse422
    | GetServicesSSHEndpointResponse424
    | GetServicesSSHEndpointResponse500
    | GetServicesSSHEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads the current SSH server settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SSH<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-ssh-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesSSHEndpointResponse400 | GetServicesSSHEndpointResponse401 | GetServicesSSHEndpointResponse403 | GetServicesSSHEndpointResponse404 | GetServicesSSHEndpointResponse405 | GetServicesSSHEndpointResponse406 | GetServicesSSHEndpointResponse409 | GetServicesSSHEndpointResponse415 | GetServicesSSHEndpointResponse422 | GetServicesSSHEndpointResponse424 | GetServicesSSHEndpointResponse500 | GetServicesSSHEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesSSHEndpointResponse400
    | GetServicesSSHEndpointResponse401
    | GetServicesSSHEndpointResponse403
    | GetServicesSSHEndpointResponse404
    | GetServicesSSHEndpointResponse405
    | GetServicesSSHEndpointResponse406
    | GetServicesSSHEndpointResponse409
    | GetServicesSSHEndpointResponse415
    | GetServicesSSHEndpointResponse422
    | GetServicesSSHEndpointResponse424
    | GetServicesSSHEndpointResponse500
    | GetServicesSSHEndpointResponse503
]:
    """<h3>Description:</h3>Reads the current SSH server settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SSH<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-ssh-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesSSHEndpointResponse400 | GetServicesSSHEndpointResponse401 | GetServicesSSHEndpointResponse403 | GetServicesSSHEndpointResponse404 | GetServicesSSHEndpointResponse405 | GetServicesSSHEndpointResponse406 | GetServicesSSHEndpointResponse409 | GetServicesSSHEndpointResponse415 | GetServicesSSHEndpointResponse422 | GetServicesSSHEndpointResponse424 | GetServicesSSHEndpointResponse500 | GetServicesSSHEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesSSHEndpointResponse400
    | GetServicesSSHEndpointResponse401
    | GetServicesSSHEndpointResponse403
    | GetServicesSSHEndpointResponse404
    | GetServicesSSHEndpointResponse405
    | GetServicesSSHEndpointResponse406
    | GetServicesSSHEndpointResponse409
    | GetServicesSSHEndpointResponse415
    | GetServicesSSHEndpointResponse422
    | GetServicesSSHEndpointResponse424
    | GetServicesSSHEndpointResponse500
    | GetServicesSSHEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads the current SSH server settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SSH<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-ssh-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesSSHEndpointResponse400 | GetServicesSSHEndpointResponse401 | GetServicesSSHEndpointResponse403 | GetServicesSSHEndpointResponse404 | GetServicesSSHEndpointResponse405 | GetServicesSSHEndpointResponse406 | GetServicesSSHEndpointResponse409 | GetServicesSSHEndpointResponse415 | GetServicesSSHEndpointResponse422 | GetServicesSSHEndpointResponse424 | GetServicesSSHEndpointResponse500 | GetServicesSSHEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
