from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ntp_settings_endpoint_data_body import PatchServicesNTPSettingsEndpointDataBody
from ...models.patch_services_ntp_settings_endpoint_json_body import PatchServicesNTPSettingsEndpointJsonBody
from ...models.patch_services_ntp_settings_endpoint_response_400 import PatchServicesNTPSettingsEndpointResponse400
from ...models.patch_services_ntp_settings_endpoint_response_401 import PatchServicesNTPSettingsEndpointResponse401
from ...models.patch_services_ntp_settings_endpoint_response_403 import PatchServicesNTPSettingsEndpointResponse403
from ...models.patch_services_ntp_settings_endpoint_response_404 import PatchServicesNTPSettingsEndpointResponse404
from ...models.patch_services_ntp_settings_endpoint_response_405 import PatchServicesNTPSettingsEndpointResponse405
from ...models.patch_services_ntp_settings_endpoint_response_406 import PatchServicesNTPSettingsEndpointResponse406
from ...models.patch_services_ntp_settings_endpoint_response_409 import PatchServicesNTPSettingsEndpointResponse409
from ...models.patch_services_ntp_settings_endpoint_response_415 import PatchServicesNTPSettingsEndpointResponse415
from ...models.patch_services_ntp_settings_endpoint_response_422 import PatchServicesNTPSettingsEndpointResponse422
from ...models.patch_services_ntp_settings_endpoint_response_424 import PatchServicesNTPSettingsEndpointResponse424
from ...models.patch_services_ntp_settings_endpoint_response_500 import PatchServicesNTPSettingsEndpointResponse500
from ...models.patch_services_ntp_settings_endpoint_response_503 import PatchServicesNTPSettingsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesNTPSettingsEndpointJsonBody | PatchServicesNTPSettingsEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/ntp/settings",
    }

    if isinstance(body, PatchServicesNTPSettingsEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesNTPSettingsEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesNTPSettingsEndpointResponse400
    | PatchServicesNTPSettingsEndpointResponse401
    | PatchServicesNTPSettingsEndpointResponse403
    | PatchServicesNTPSettingsEndpointResponse404
    | PatchServicesNTPSettingsEndpointResponse405
    | PatchServicesNTPSettingsEndpointResponse406
    | PatchServicesNTPSettingsEndpointResponse409
    | PatchServicesNTPSettingsEndpointResponse415
    | PatchServicesNTPSettingsEndpointResponse422
    | PatchServicesNTPSettingsEndpointResponse424
    | PatchServicesNTPSettingsEndpointResponse500
    | PatchServicesNTPSettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesNTPSettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesNTPSettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesNTPSettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesNTPSettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesNTPSettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesNTPSettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesNTPSettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesNTPSettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesNTPSettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesNTPSettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesNTPSettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesNTPSettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesNTPSettingsEndpointResponse400
    | PatchServicesNTPSettingsEndpointResponse401
    | PatchServicesNTPSettingsEndpointResponse403
    | PatchServicesNTPSettingsEndpointResponse404
    | PatchServicesNTPSettingsEndpointResponse405
    | PatchServicesNTPSettingsEndpointResponse406
    | PatchServicesNTPSettingsEndpointResponse409
    | PatchServicesNTPSettingsEndpointResponse415
    | PatchServicesNTPSettingsEndpointResponse422
    | PatchServicesNTPSettingsEndpointResponse424
    | PatchServicesNTPSettingsEndpointResponse500
    | PatchServicesNTPSettingsEndpointResponse503
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
    body: PatchServicesNTPSettingsEndpointJsonBody | PatchServicesNTPSettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesNTPSettingsEndpointResponse400
    | PatchServicesNTPSettingsEndpointResponse401
    | PatchServicesNTPSettingsEndpointResponse403
    | PatchServicesNTPSettingsEndpointResponse404
    | PatchServicesNTPSettingsEndpointResponse405
    | PatchServicesNTPSettingsEndpointResponse406
    | PatchServicesNTPSettingsEndpointResponse409
    | PatchServicesNTPSettingsEndpointResponse415
    | PatchServicesNTPSettingsEndpointResponse422
    | PatchServicesNTPSettingsEndpointResponse424
    | PatchServicesNTPSettingsEndpointResponse500
    | PatchServicesNTPSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current NTP Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesNTPSettingsEndpointJsonBody | Unset):
        body (PatchServicesNTPSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesNTPSettingsEndpointResponse400 | PatchServicesNTPSettingsEndpointResponse401 | PatchServicesNTPSettingsEndpointResponse403 | PatchServicesNTPSettingsEndpointResponse404 | PatchServicesNTPSettingsEndpointResponse405 | PatchServicesNTPSettingsEndpointResponse406 | PatchServicesNTPSettingsEndpointResponse409 | PatchServicesNTPSettingsEndpointResponse415 | PatchServicesNTPSettingsEndpointResponse422 | PatchServicesNTPSettingsEndpointResponse424 | PatchServicesNTPSettingsEndpointResponse500 | PatchServicesNTPSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesNTPSettingsEndpointJsonBody | PatchServicesNTPSettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesNTPSettingsEndpointResponse400
    | PatchServicesNTPSettingsEndpointResponse401
    | PatchServicesNTPSettingsEndpointResponse403
    | PatchServicesNTPSettingsEndpointResponse404
    | PatchServicesNTPSettingsEndpointResponse405
    | PatchServicesNTPSettingsEndpointResponse406
    | PatchServicesNTPSettingsEndpointResponse409
    | PatchServicesNTPSettingsEndpointResponse415
    | PatchServicesNTPSettingsEndpointResponse422
    | PatchServicesNTPSettingsEndpointResponse424
    | PatchServicesNTPSettingsEndpointResponse500
    | PatchServicesNTPSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current NTP Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesNTPSettingsEndpointJsonBody | Unset):
        body (PatchServicesNTPSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesNTPSettingsEndpointResponse400 | PatchServicesNTPSettingsEndpointResponse401 | PatchServicesNTPSettingsEndpointResponse403 | PatchServicesNTPSettingsEndpointResponse404 | PatchServicesNTPSettingsEndpointResponse405 | PatchServicesNTPSettingsEndpointResponse406 | PatchServicesNTPSettingsEndpointResponse409 | PatchServicesNTPSettingsEndpointResponse415 | PatchServicesNTPSettingsEndpointResponse422 | PatchServicesNTPSettingsEndpointResponse424 | PatchServicesNTPSettingsEndpointResponse500 | PatchServicesNTPSettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesNTPSettingsEndpointJsonBody | PatchServicesNTPSettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesNTPSettingsEndpointResponse400
    | PatchServicesNTPSettingsEndpointResponse401
    | PatchServicesNTPSettingsEndpointResponse403
    | PatchServicesNTPSettingsEndpointResponse404
    | PatchServicesNTPSettingsEndpointResponse405
    | PatchServicesNTPSettingsEndpointResponse406
    | PatchServicesNTPSettingsEndpointResponse409
    | PatchServicesNTPSettingsEndpointResponse415
    | PatchServicesNTPSettingsEndpointResponse422
    | PatchServicesNTPSettingsEndpointResponse424
    | PatchServicesNTPSettingsEndpointResponse500
    | PatchServicesNTPSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current NTP Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesNTPSettingsEndpointJsonBody | Unset):
        body (PatchServicesNTPSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesNTPSettingsEndpointResponse400 | PatchServicesNTPSettingsEndpointResponse401 | PatchServicesNTPSettingsEndpointResponse403 | PatchServicesNTPSettingsEndpointResponse404 | PatchServicesNTPSettingsEndpointResponse405 | PatchServicesNTPSettingsEndpointResponse406 | PatchServicesNTPSettingsEndpointResponse409 | PatchServicesNTPSettingsEndpointResponse415 | PatchServicesNTPSettingsEndpointResponse422 | PatchServicesNTPSettingsEndpointResponse424 | PatchServicesNTPSettingsEndpointResponse500 | PatchServicesNTPSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesNTPSettingsEndpointJsonBody | PatchServicesNTPSettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesNTPSettingsEndpointResponse400
    | PatchServicesNTPSettingsEndpointResponse401
    | PatchServicesNTPSettingsEndpointResponse403
    | PatchServicesNTPSettingsEndpointResponse404
    | PatchServicesNTPSettingsEndpointResponse405
    | PatchServicesNTPSettingsEndpointResponse406
    | PatchServicesNTPSettingsEndpointResponse409
    | PatchServicesNTPSettingsEndpointResponse415
    | PatchServicesNTPSettingsEndpointResponse422
    | PatchServicesNTPSettingsEndpointResponse424
    | PatchServicesNTPSettingsEndpointResponse500
    | PatchServicesNTPSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current NTP Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesNTPSettingsEndpointJsonBody | Unset):
        body (PatchServicesNTPSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesNTPSettingsEndpointResponse400 | PatchServicesNTPSettingsEndpointResponse401 | PatchServicesNTPSettingsEndpointResponse403 | PatchServicesNTPSettingsEndpointResponse404 | PatchServicesNTPSettingsEndpointResponse405 | PatchServicesNTPSettingsEndpointResponse406 | PatchServicesNTPSettingsEndpointResponse409 | PatchServicesNTPSettingsEndpointResponse415 | PatchServicesNTPSettingsEndpointResponse422 | PatchServicesNTPSettingsEndpointResponse424 | PatchServicesNTPSettingsEndpointResponse500 | PatchServicesNTPSettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
