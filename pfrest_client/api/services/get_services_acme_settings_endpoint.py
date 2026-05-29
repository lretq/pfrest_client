from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_acme_settings_endpoint_response_400 import GetServicesACMESettingsEndpointResponse400
from ...models.get_services_acme_settings_endpoint_response_401 import GetServicesACMESettingsEndpointResponse401
from ...models.get_services_acme_settings_endpoint_response_403 import GetServicesACMESettingsEndpointResponse403
from ...models.get_services_acme_settings_endpoint_response_404 import GetServicesACMESettingsEndpointResponse404
from ...models.get_services_acme_settings_endpoint_response_405 import GetServicesACMESettingsEndpointResponse405
from ...models.get_services_acme_settings_endpoint_response_406 import GetServicesACMESettingsEndpointResponse406
from ...models.get_services_acme_settings_endpoint_response_409 import GetServicesACMESettingsEndpointResponse409
from ...models.get_services_acme_settings_endpoint_response_415 import GetServicesACMESettingsEndpointResponse415
from ...models.get_services_acme_settings_endpoint_response_422 import GetServicesACMESettingsEndpointResponse422
from ...models.get_services_acme_settings_endpoint_response_424 import GetServicesACMESettingsEndpointResponse424
from ...models.get_services_acme_settings_endpoint_response_500 import GetServicesACMESettingsEndpointResponse500
from ...models.get_services_acme_settings_endpoint_response_503 import GetServicesACMESettingsEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/acme/settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesACMESettingsEndpointResponse400
    | GetServicesACMESettingsEndpointResponse401
    | GetServicesACMESettingsEndpointResponse403
    | GetServicesACMESettingsEndpointResponse404
    | GetServicesACMESettingsEndpointResponse405
    | GetServicesACMESettingsEndpointResponse406
    | GetServicesACMESettingsEndpointResponse409
    | GetServicesACMESettingsEndpointResponse415
    | GetServicesACMESettingsEndpointResponse422
    | GetServicesACMESettingsEndpointResponse424
    | GetServicesACMESettingsEndpointResponse500
    | GetServicesACMESettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesACMESettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesACMESettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesACMESettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesACMESettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesACMESettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesACMESettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesACMESettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesACMESettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesACMESettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesACMESettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesACMESettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesACMESettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesACMESettingsEndpointResponse400
    | GetServicesACMESettingsEndpointResponse401
    | GetServicesACMESettingsEndpointResponse403
    | GetServicesACMESettingsEndpointResponse404
    | GetServicesACMESettingsEndpointResponse405
    | GetServicesACMESettingsEndpointResponse406
    | GetServicesACMESettingsEndpointResponse409
    | GetServicesACMESettingsEndpointResponse415
    | GetServicesACMESettingsEndpointResponse422
    | GetServicesACMESettingsEndpointResponse424
    | GetServicesACMESettingsEndpointResponse500
    | GetServicesACMESettingsEndpointResponse503
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
    GetServicesACMESettingsEndpointResponse400
    | GetServicesACMESettingsEndpointResponse401
    | GetServicesACMESettingsEndpointResponse403
    | GetServicesACMESettingsEndpointResponse404
    | GetServicesACMESettingsEndpointResponse405
    | GetServicesACMESettingsEndpointResponse406
    | GetServicesACMESettingsEndpointResponse409
    | GetServicesACMESettingsEndpointResponse415
    | GetServicesACMESettingsEndpointResponse422
    | GetServicesACMESettingsEndpointResponse424
    | GetServicesACMESettingsEndpointResponse500
    | GetServicesACMESettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current ACME Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMESettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-settings-get ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesACMESettingsEndpointResponse400 | GetServicesACMESettingsEndpointResponse401 | GetServicesACMESettingsEndpointResponse403 | GetServicesACMESettingsEndpointResponse404 | GetServicesACMESettingsEndpointResponse405 | GetServicesACMESettingsEndpointResponse406 | GetServicesACMESettingsEndpointResponse409 | GetServicesACMESettingsEndpointResponse415 | GetServicesACMESettingsEndpointResponse422 | GetServicesACMESettingsEndpointResponse424 | GetServicesACMESettingsEndpointResponse500 | GetServicesACMESettingsEndpointResponse503]
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
    GetServicesACMESettingsEndpointResponse400
    | GetServicesACMESettingsEndpointResponse401
    | GetServicesACMESettingsEndpointResponse403
    | GetServicesACMESettingsEndpointResponse404
    | GetServicesACMESettingsEndpointResponse405
    | GetServicesACMESettingsEndpointResponse406
    | GetServicesACMESettingsEndpointResponse409
    | GetServicesACMESettingsEndpointResponse415
    | GetServicesACMESettingsEndpointResponse422
    | GetServicesACMESettingsEndpointResponse424
    | GetServicesACMESettingsEndpointResponse500
    | GetServicesACMESettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current ACME Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMESettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-settings-get ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesACMESettingsEndpointResponse400 | GetServicesACMESettingsEndpointResponse401 | GetServicesACMESettingsEndpointResponse403 | GetServicesACMESettingsEndpointResponse404 | GetServicesACMESettingsEndpointResponse405 | GetServicesACMESettingsEndpointResponse406 | GetServicesACMESettingsEndpointResponse409 | GetServicesACMESettingsEndpointResponse415 | GetServicesACMESettingsEndpointResponse422 | GetServicesACMESettingsEndpointResponse424 | GetServicesACMESettingsEndpointResponse500 | GetServicesACMESettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesACMESettingsEndpointResponse400
    | GetServicesACMESettingsEndpointResponse401
    | GetServicesACMESettingsEndpointResponse403
    | GetServicesACMESettingsEndpointResponse404
    | GetServicesACMESettingsEndpointResponse405
    | GetServicesACMESettingsEndpointResponse406
    | GetServicesACMESettingsEndpointResponse409
    | GetServicesACMESettingsEndpointResponse415
    | GetServicesACMESettingsEndpointResponse422
    | GetServicesACMESettingsEndpointResponse424
    | GetServicesACMESettingsEndpointResponse500
    | GetServicesACMESettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current ACME Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMESettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-settings-get ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesACMESettingsEndpointResponse400 | GetServicesACMESettingsEndpointResponse401 | GetServicesACMESettingsEndpointResponse403 | GetServicesACMESettingsEndpointResponse404 | GetServicesACMESettingsEndpointResponse405 | GetServicesACMESettingsEndpointResponse406 | GetServicesACMESettingsEndpointResponse409 | GetServicesACMESettingsEndpointResponse415 | GetServicesACMESettingsEndpointResponse422 | GetServicesACMESettingsEndpointResponse424 | GetServicesACMESettingsEndpointResponse500 | GetServicesACMESettingsEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesACMESettingsEndpointResponse400
    | GetServicesACMESettingsEndpointResponse401
    | GetServicesACMESettingsEndpointResponse403
    | GetServicesACMESettingsEndpointResponse404
    | GetServicesACMESettingsEndpointResponse405
    | GetServicesACMESettingsEndpointResponse406
    | GetServicesACMESettingsEndpointResponse409
    | GetServicesACMESettingsEndpointResponse415
    | GetServicesACMESettingsEndpointResponse422
    | GetServicesACMESettingsEndpointResponse424
    | GetServicesACMESettingsEndpointResponse500
    | GetServicesACMESettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current ACME Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMESettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-settings-get ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesACMESettingsEndpointResponse400 | GetServicesACMESettingsEndpointResponse401 | GetServicesACMESettingsEndpointResponse403 | GetServicesACMESettingsEndpointResponse404 | GetServicesACMESettingsEndpointResponse405 | GetServicesACMESettingsEndpointResponse406 | GetServicesACMESettingsEndpointResponse409 | GetServicesACMESettingsEndpointResponse415 | GetServicesACMESettingsEndpointResponse422 | GetServicesACMESettingsEndpointResponse424 | GetServicesACMESettingsEndpointResponse500 | GetServicesACMESettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
