from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_ntp_settings_endpoint_response_400 import GetServicesNTPSettingsEndpointResponse400
from ...models.get_services_ntp_settings_endpoint_response_401 import GetServicesNTPSettingsEndpointResponse401
from ...models.get_services_ntp_settings_endpoint_response_403 import GetServicesNTPSettingsEndpointResponse403
from ...models.get_services_ntp_settings_endpoint_response_404 import GetServicesNTPSettingsEndpointResponse404
from ...models.get_services_ntp_settings_endpoint_response_405 import GetServicesNTPSettingsEndpointResponse405
from ...models.get_services_ntp_settings_endpoint_response_406 import GetServicesNTPSettingsEndpointResponse406
from ...models.get_services_ntp_settings_endpoint_response_409 import GetServicesNTPSettingsEndpointResponse409
from ...models.get_services_ntp_settings_endpoint_response_415 import GetServicesNTPSettingsEndpointResponse415
from ...models.get_services_ntp_settings_endpoint_response_422 import GetServicesNTPSettingsEndpointResponse422
from ...models.get_services_ntp_settings_endpoint_response_424 import GetServicesNTPSettingsEndpointResponse424
from ...models.get_services_ntp_settings_endpoint_response_500 import GetServicesNTPSettingsEndpointResponse500
from ...models.get_services_ntp_settings_endpoint_response_503 import GetServicesNTPSettingsEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/ntp/settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesNTPSettingsEndpointResponse400
    | GetServicesNTPSettingsEndpointResponse401
    | GetServicesNTPSettingsEndpointResponse403
    | GetServicesNTPSettingsEndpointResponse404
    | GetServicesNTPSettingsEndpointResponse405
    | GetServicesNTPSettingsEndpointResponse406
    | GetServicesNTPSettingsEndpointResponse409
    | GetServicesNTPSettingsEndpointResponse415
    | GetServicesNTPSettingsEndpointResponse422
    | GetServicesNTPSettingsEndpointResponse424
    | GetServicesNTPSettingsEndpointResponse500
    | GetServicesNTPSettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesNTPSettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesNTPSettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesNTPSettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesNTPSettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesNTPSettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesNTPSettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesNTPSettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesNTPSettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesNTPSettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesNTPSettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesNTPSettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesNTPSettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesNTPSettingsEndpointResponse400
    | GetServicesNTPSettingsEndpointResponse401
    | GetServicesNTPSettingsEndpointResponse403
    | GetServicesNTPSettingsEndpointResponse404
    | GetServicesNTPSettingsEndpointResponse405
    | GetServicesNTPSettingsEndpointResponse406
    | GetServicesNTPSettingsEndpointResponse409
    | GetServicesNTPSettingsEndpointResponse415
    | GetServicesNTPSettingsEndpointResponse422
    | GetServicesNTPSettingsEndpointResponse424
    | GetServicesNTPSettingsEndpointResponse500
    | GetServicesNTPSettingsEndpointResponse503
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
    GetServicesNTPSettingsEndpointResponse400
    | GetServicesNTPSettingsEndpointResponse401
    | GetServicesNTPSettingsEndpointResponse403
    | GetServicesNTPSettingsEndpointResponse404
    | GetServicesNTPSettingsEndpointResponse405
    | GetServicesNTPSettingsEndpointResponse406
    | GetServicesNTPSettingsEndpointResponse409
    | GetServicesNTPSettingsEndpointResponse415
    | GetServicesNTPSettingsEndpointResponse422
    | GetServicesNTPSettingsEndpointResponse424
    | GetServicesNTPSettingsEndpointResponse500
    | GetServicesNTPSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current NTP Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-settings-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesNTPSettingsEndpointResponse400 | GetServicesNTPSettingsEndpointResponse401 | GetServicesNTPSettingsEndpointResponse403 | GetServicesNTPSettingsEndpointResponse404 | GetServicesNTPSettingsEndpointResponse405 | GetServicesNTPSettingsEndpointResponse406 | GetServicesNTPSettingsEndpointResponse409 | GetServicesNTPSettingsEndpointResponse415 | GetServicesNTPSettingsEndpointResponse422 | GetServicesNTPSettingsEndpointResponse424 | GetServicesNTPSettingsEndpointResponse500 | GetServicesNTPSettingsEndpointResponse503]
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
    GetServicesNTPSettingsEndpointResponse400
    | GetServicesNTPSettingsEndpointResponse401
    | GetServicesNTPSettingsEndpointResponse403
    | GetServicesNTPSettingsEndpointResponse404
    | GetServicesNTPSettingsEndpointResponse405
    | GetServicesNTPSettingsEndpointResponse406
    | GetServicesNTPSettingsEndpointResponse409
    | GetServicesNTPSettingsEndpointResponse415
    | GetServicesNTPSettingsEndpointResponse422
    | GetServicesNTPSettingsEndpointResponse424
    | GetServicesNTPSettingsEndpointResponse500
    | GetServicesNTPSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current NTP Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-settings-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesNTPSettingsEndpointResponse400 | GetServicesNTPSettingsEndpointResponse401 | GetServicesNTPSettingsEndpointResponse403 | GetServicesNTPSettingsEndpointResponse404 | GetServicesNTPSettingsEndpointResponse405 | GetServicesNTPSettingsEndpointResponse406 | GetServicesNTPSettingsEndpointResponse409 | GetServicesNTPSettingsEndpointResponse415 | GetServicesNTPSettingsEndpointResponse422 | GetServicesNTPSettingsEndpointResponse424 | GetServicesNTPSettingsEndpointResponse500 | GetServicesNTPSettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesNTPSettingsEndpointResponse400
    | GetServicesNTPSettingsEndpointResponse401
    | GetServicesNTPSettingsEndpointResponse403
    | GetServicesNTPSettingsEndpointResponse404
    | GetServicesNTPSettingsEndpointResponse405
    | GetServicesNTPSettingsEndpointResponse406
    | GetServicesNTPSettingsEndpointResponse409
    | GetServicesNTPSettingsEndpointResponse415
    | GetServicesNTPSettingsEndpointResponse422
    | GetServicesNTPSettingsEndpointResponse424
    | GetServicesNTPSettingsEndpointResponse500
    | GetServicesNTPSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current NTP Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-settings-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesNTPSettingsEndpointResponse400 | GetServicesNTPSettingsEndpointResponse401 | GetServicesNTPSettingsEndpointResponse403 | GetServicesNTPSettingsEndpointResponse404 | GetServicesNTPSettingsEndpointResponse405 | GetServicesNTPSettingsEndpointResponse406 | GetServicesNTPSettingsEndpointResponse409 | GetServicesNTPSettingsEndpointResponse415 | GetServicesNTPSettingsEndpointResponse422 | GetServicesNTPSettingsEndpointResponse424 | GetServicesNTPSettingsEndpointResponse500 | GetServicesNTPSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesNTPSettingsEndpointResponse400
    | GetServicesNTPSettingsEndpointResponse401
    | GetServicesNTPSettingsEndpointResponse403
    | GetServicesNTPSettingsEndpointResponse404
    | GetServicesNTPSettingsEndpointResponse405
    | GetServicesNTPSettingsEndpointResponse406
    | GetServicesNTPSettingsEndpointResponse409
    | GetServicesNTPSettingsEndpointResponse415
    | GetServicesNTPSettingsEndpointResponse422
    | GetServicesNTPSettingsEndpointResponse424
    | GetServicesNTPSettingsEndpointResponse500
    | GetServicesNTPSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current NTP Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-settings-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesNTPSettingsEndpointResponse400 | GetServicesNTPSettingsEndpointResponse401 | GetServicesNTPSettingsEndpointResponse403 | GetServicesNTPSettingsEndpointResponse404 | GetServicesNTPSettingsEndpointResponse405 | GetServicesNTPSettingsEndpointResponse406 | GetServicesNTPSettingsEndpointResponse409 | GetServicesNTPSettingsEndpointResponse415 | GetServicesNTPSettingsEndpointResponse422 | GetServicesNTPSettingsEndpointResponse424 | GetServicesNTPSettingsEndpointResponse500 | GetServicesNTPSettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
