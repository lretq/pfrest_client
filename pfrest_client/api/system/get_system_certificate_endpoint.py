from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_certificate_endpoint_response_400 import GetSystemCertificateEndpointResponse400
from ...models.get_system_certificate_endpoint_response_401 import GetSystemCertificateEndpointResponse401
from ...models.get_system_certificate_endpoint_response_403 import GetSystemCertificateEndpointResponse403
from ...models.get_system_certificate_endpoint_response_404 import GetSystemCertificateEndpointResponse404
from ...models.get_system_certificate_endpoint_response_405 import GetSystemCertificateEndpointResponse405
from ...models.get_system_certificate_endpoint_response_406 import GetSystemCertificateEndpointResponse406
from ...models.get_system_certificate_endpoint_response_409 import GetSystemCertificateEndpointResponse409
from ...models.get_system_certificate_endpoint_response_415 import GetSystemCertificateEndpointResponse415
from ...models.get_system_certificate_endpoint_response_422 import GetSystemCertificateEndpointResponse422
from ...models.get_system_certificate_endpoint_response_424 import GetSystemCertificateEndpointResponse424
from ...models.get_system_certificate_endpoint_response_500 import GetSystemCertificateEndpointResponse500
from ...models.get_system_certificate_endpoint_response_503 import GetSystemCertificateEndpointResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/certificate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemCertificateEndpointResponse400
    | GetSystemCertificateEndpointResponse401
    | GetSystemCertificateEndpointResponse403
    | GetSystemCertificateEndpointResponse404
    | GetSystemCertificateEndpointResponse405
    | GetSystemCertificateEndpointResponse406
    | GetSystemCertificateEndpointResponse409
    | GetSystemCertificateEndpointResponse415
    | GetSystemCertificateEndpointResponse422
    | GetSystemCertificateEndpointResponse424
    | GetSystemCertificateEndpointResponse500
    | GetSystemCertificateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemCertificateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemCertificateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemCertificateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemCertificateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemCertificateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemCertificateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemCertificateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemCertificateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemCertificateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemCertificateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemCertificateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemCertificateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemCertificateEndpointResponse400
    | GetSystemCertificateEndpointResponse401
    | GetSystemCertificateEndpointResponse403
    | GetSystemCertificateEndpointResponse404
    | GetSystemCertificateEndpointResponse405
    | GetSystemCertificateEndpointResponse406
    | GetSystemCertificateEndpointResponse409
    | GetSystemCertificateEndpointResponse415
    | GetSystemCertificateEndpointResponse422
    | GetSystemCertificateEndpointResponse424
    | GetSystemCertificateEndpointResponse500
    | GetSystemCertificateEndpointResponse503
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
    id: int | str,
) -> Response[
    GetSystemCertificateEndpointResponse400
    | GetSystemCertificateEndpointResponse401
    | GetSystemCertificateEndpointResponse403
    | GetSystemCertificateEndpointResponse404
    | GetSystemCertificateEndpointResponse405
    | GetSystemCertificateEndpointResponse406
    | GetSystemCertificateEndpointResponse409
    | GetSystemCertificateEndpointResponse415
    | GetSystemCertificateEndpointResponse422
    | GetSystemCertificateEndpointResponse424
    | GetSystemCertificateEndpointResponse500
    | GetSystemCertificateEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemCertificateEndpointResponse400 | GetSystemCertificateEndpointResponse401 | GetSystemCertificateEndpointResponse403 | GetSystemCertificateEndpointResponse404 | GetSystemCertificateEndpointResponse405 | GetSystemCertificateEndpointResponse406 | GetSystemCertificateEndpointResponse409 | GetSystemCertificateEndpointResponse415 | GetSystemCertificateEndpointResponse422 | GetSystemCertificateEndpointResponse424 | GetSystemCertificateEndpointResponse500 | GetSystemCertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    GetSystemCertificateEndpointResponse400
    | GetSystemCertificateEndpointResponse401
    | GetSystemCertificateEndpointResponse403
    | GetSystemCertificateEndpointResponse404
    | GetSystemCertificateEndpointResponse405
    | GetSystemCertificateEndpointResponse406
    | GetSystemCertificateEndpointResponse409
    | GetSystemCertificateEndpointResponse415
    | GetSystemCertificateEndpointResponse422
    | GetSystemCertificateEndpointResponse424
    | GetSystemCertificateEndpointResponse500
    | GetSystemCertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemCertificateEndpointResponse400 | GetSystemCertificateEndpointResponse401 | GetSystemCertificateEndpointResponse403 | GetSystemCertificateEndpointResponse404 | GetSystemCertificateEndpointResponse405 | GetSystemCertificateEndpointResponse406 | GetSystemCertificateEndpointResponse409 | GetSystemCertificateEndpointResponse415 | GetSystemCertificateEndpointResponse422 | GetSystemCertificateEndpointResponse424 | GetSystemCertificateEndpointResponse500 | GetSystemCertificateEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    GetSystemCertificateEndpointResponse400
    | GetSystemCertificateEndpointResponse401
    | GetSystemCertificateEndpointResponse403
    | GetSystemCertificateEndpointResponse404
    | GetSystemCertificateEndpointResponse405
    | GetSystemCertificateEndpointResponse406
    | GetSystemCertificateEndpointResponse409
    | GetSystemCertificateEndpointResponse415
    | GetSystemCertificateEndpointResponse422
    | GetSystemCertificateEndpointResponse424
    | GetSystemCertificateEndpointResponse500
    | GetSystemCertificateEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemCertificateEndpointResponse400 | GetSystemCertificateEndpointResponse401 | GetSystemCertificateEndpointResponse403 | GetSystemCertificateEndpointResponse404 | GetSystemCertificateEndpointResponse405 | GetSystemCertificateEndpointResponse406 | GetSystemCertificateEndpointResponse409 | GetSystemCertificateEndpointResponse415 | GetSystemCertificateEndpointResponse422 | GetSystemCertificateEndpointResponse424 | GetSystemCertificateEndpointResponse500 | GetSystemCertificateEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    GetSystemCertificateEndpointResponse400
    | GetSystemCertificateEndpointResponse401
    | GetSystemCertificateEndpointResponse403
    | GetSystemCertificateEndpointResponse404
    | GetSystemCertificateEndpointResponse405
    | GetSystemCertificateEndpointResponse406
    | GetSystemCertificateEndpointResponse409
    | GetSystemCertificateEndpointResponse415
    | GetSystemCertificateEndpointResponse422
    | GetSystemCertificateEndpointResponse424
    | GetSystemCertificateEndpointResponse500
    | GetSystemCertificateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Certificate.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Certificate<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-certificate-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemCertificateEndpointResponse400 | GetSystemCertificateEndpointResponse401 | GetSystemCertificateEndpointResponse403 | GetSystemCertificateEndpointResponse404 | GetSystemCertificateEndpointResponse405 | GetSystemCertificateEndpointResponse406 | GetSystemCertificateEndpointResponse409 | GetSystemCertificateEndpointResponse415 | GetSystemCertificateEndpointResponse422 | GetSystemCertificateEndpointResponse424 | GetSystemCertificateEndpointResponse500 | GetSystemCertificateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
