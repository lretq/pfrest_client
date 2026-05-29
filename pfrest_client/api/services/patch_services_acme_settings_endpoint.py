from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_acme_settings_endpoint_data_body import PatchServicesACMESettingsEndpointDataBody
from ...models.patch_services_acme_settings_endpoint_json_body import PatchServicesACMESettingsEndpointJsonBody
from ...models.patch_services_acme_settings_endpoint_response_400 import PatchServicesACMESettingsEndpointResponse400
from ...models.patch_services_acme_settings_endpoint_response_401 import PatchServicesACMESettingsEndpointResponse401
from ...models.patch_services_acme_settings_endpoint_response_403 import PatchServicesACMESettingsEndpointResponse403
from ...models.patch_services_acme_settings_endpoint_response_404 import PatchServicesACMESettingsEndpointResponse404
from ...models.patch_services_acme_settings_endpoint_response_405 import PatchServicesACMESettingsEndpointResponse405
from ...models.patch_services_acme_settings_endpoint_response_406 import PatchServicesACMESettingsEndpointResponse406
from ...models.patch_services_acme_settings_endpoint_response_409 import PatchServicesACMESettingsEndpointResponse409
from ...models.patch_services_acme_settings_endpoint_response_415 import PatchServicesACMESettingsEndpointResponse415
from ...models.patch_services_acme_settings_endpoint_response_422 import PatchServicesACMESettingsEndpointResponse422
from ...models.patch_services_acme_settings_endpoint_response_424 import PatchServicesACMESettingsEndpointResponse424
from ...models.patch_services_acme_settings_endpoint_response_500 import PatchServicesACMESettingsEndpointResponse500
from ...models.patch_services_acme_settings_endpoint_response_503 import PatchServicesACMESettingsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesACMESettingsEndpointJsonBody | PatchServicesACMESettingsEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/acme/settings",
    }

    if isinstance(body, PatchServicesACMESettingsEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesACMESettingsEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesACMESettingsEndpointResponse400
    | PatchServicesACMESettingsEndpointResponse401
    | PatchServicesACMESettingsEndpointResponse403
    | PatchServicesACMESettingsEndpointResponse404
    | PatchServicesACMESettingsEndpointResponse405
    | PatchServicesACMESettingsEndpointResponse406
    | PatchServicesACMESettingsEndpointResponse409
    | PatchServicesACMESettingsEndpointResponse415
    | PatchServicesACMESettingsEndpointResponse422
    | PatchServicesACMESettingsEndpointResponse424
    | PatchServicesACMESettingsEndpointResponse500
    | PatchServicesACMESettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesACMESettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesACMESettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesACMESettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesACMESettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesACMESettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesACMESettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesACMESettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesACMESettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesACMESettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesACMESettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesACMESettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesACMESettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesACMESettingsEndpointResponse400
    | PatchServicesACMESettingsEndpointResponse401
    | PatchServicesACMESettingsEndpointResponse403
    | PatchServicesACMESettingsEndpointResponse404
    | PatchServicesACMESettingsEndpointResponse405
    | PatchServicesACMESettingsEndpointResponse406
    | PatchServicesACMESettingsEndpointResponse409
    | PatchServicesACMESettingsEndpointResponse415
    | PatchServicesACMESettingsEndpointResponse422
    | PatchServicesACMESettingsEndpointResponse424
    | PatchServicesACMESettingsEndpointResponse500
    | PatchServicesACMESettingsEndpointResponse503
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
    body: PatchServicesACMESettingsEndpointJsonBody | PatchServicesACMESettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesACMESettingsEndpointResponse400
    | PatchServicesACMESettingsEndpointResponse401
    | PatchServicesACMESettingsEndpointResponse403
    | PatchServicesACMESettingsEndpointResponse404
    | PatchServicesACMESettingsEndpointResponse405
    | PatchServicesACMESettingsEndpointResponse406
    | PatchServicesACMESettingsEndpointResponse409
    | PatchServicesACMESettingsEndpointResponse415
    | PatchServicesACMESettingsEndpointResponse422
    | PatchServicesACMESettingsEndpointResponse424
    | PatchServicesACMESettingsEndpointResponse500
    | PatchServicesACMESettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current ACME Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMESettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMESettingsEndpointJsonBody | Unset):
        body (PatchServicesACMESettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMESettingsEndpointResponse400 | PatchServicesACMESettingsEndpointResponse401 | PatchServicesACMESettingsEndpointResponse403 | PatchServicesACMESettingsEndpointResponse404 | PatchServicesACMESettingsEndpointResponse405 | PatchServicesACMESettingsEndpointResponse406 | PatchServicesACMESettingsEndpointResponse409 | PatchServicesACMESettingsEndpointResponse415 | PatchServicesACMESettingsEndpointResponse422 | PatchServicesACMESettingsEndpointResponse424 | PatchServicesACMESettingsEndpointResponse500 | PatchServicesACMESettingsEndpointResponse503]
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
    body: PatchServicesACMESettingsEndpointJsonBody | PatchServicesACMESettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesACMESettingsEndpointResponse400
    | PatchServicesACMESettingsEndpointResponse401
    | PatchServicesACMESettingsEndpointResponse403
    | PatchServicesACMESettingsEndpointResponse404
    | PatchServicesACMESettingsEndpointResponse405
    | PatchServicesACMESettingsEndpointResponse406
    | PatchServicesACMESettingsEndpointResponse409
    | PatchServicesACMESettingsEndpointResponse415
    | PatchServicesACMESettingsEndpointResponse422
    | PatchServicesACMESettingsEndpointResponse424
    | PatchServicesACMESettingsEndpointResponse500
    | PatchServicesACMESettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current ACME Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMESettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMESettingsEndpointJsonBody | Unset):
        body (PatchServicesACMESettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMESettingsEndpointResponse400 | PatchServicesACMESettingsEndpointResponse401 | PatchServicesACMESettingsEndpointResponse403 | PatchServicesACMESettingsEndpointResponse404 | PatchServicesACMESettingsEndpointResponse405 | PatchServicesACMESettingsEndpointResponse406 | PatchServicesACMESettingsEndpointResponse409 | PatchServicesACMESettingsEndpointResponse415 | PatchServicesACMESettingsEndpointResponse422 | PatchServicesACMESettingsEndpointResponse424 | PatchServicesACMESettingsEndpointResponse500 | PatchServicesACMESettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMESettingsEndpointJsonBody | PatchServicesACMESettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesACMESettingsEndpointResponse400
    | PatchServicesACMESettingsEndpointResponse401
    | PatchServicesACMESettingsEndpointResponse403
    | PatchServicesACMESettingsEndpointResponse404
    | PatchServicesACMESettingsEndpointResponse405
    | PatchServicesACMESettingsEndpointResponse406
    | PatchServicesACMESettingsEndpointResponse409
    | PatchServicesACMESettingsEndpointResponse415
    | PatchServicesACMESettingsEndpointResponse422
    | PatchServicesACMESettingsEndpointResponse424
    | PatchServicesACMESettingsEndpointResponse500
    | PatchServicesACMESettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current ACME Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMESettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMESettingsEndpointJsonBody | Unset):
        body (PatchServicesACMESettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMESettingsEndpointResponse400 | PatchServicesACMESettingsEndpointResponse401 | PatchServicesACMESettingsEndpointResponse403 | PatchServicesACMESettingsEndpointResponse404 | PatchServicesACMESettingsEndpointResponse405 | PatchServicesACMESettingsEndpointResponse406 | PatchServicesACMESettingsEndpointResponse409 | PatchServicesACMESettingsEndpointResponse415 | PatchServicesACMESettingsEndpointResponse422 | PatchServicesACMESettingsEndpointResponse424 | PatchServicesACMESettingsEndpointResponse500 | PatchServicesACMESettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMESettingsEndpointJsonBody | PatchServicesACMESettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesACMESettingsEndpointResponse400
    | PatchServicesACMESettingsEndpointResponse401
    | PatchServicesACMESettingsEndpointResponse403
    | PatchServicesACMESettingsEndpointResponse404
    | PatchServicesACMESettingsEndpointResponse405
    | PatchServicesACMESettingsEndpointResponse406
    | PatchServicesACMESettingsEndpointResponse409
    | PatchServicesACMESettingsEndpointResponse415
    | PatchServicesACMESettingsEndpointResponse422
    | PatchServicesACMESettingsEndpointResponse424
    | PatchServicesACMESettingsEndpointResponse500
    | PatchServicesACMESettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current ACME Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMESettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMESettingsEndpointJsonBody | Unset):
        body (PatchServicesACMESettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMESettingsEndpointResponse400 | PatchServicesACMESettingsEndpointResponse401 | PatchServicesACMESettingsEndpointResponse403 | PatchServicesACMESettingsEndpointResponse404 | PatchServicesACMESettingsEndpointResponse405 | PatchServicesACMESettingsEndpointResponse406 | PatchServicesACMESettingsEndpointResponse409 | PatchServicesACMESettingsEndpointResponse415 | PatchServicesACMESettingsEndpointResponse422 | PatchServicesACMESettingsEndpointResponse424 | PatchServicesACMESettingsEndpointResponse500 | PatchServicesACMESettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
