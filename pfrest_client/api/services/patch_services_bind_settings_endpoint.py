from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_bind_settings_endpoint_data_body import PatchServicesBINDSettingsEndpointDataBody
from ...models.patch_services_bind_settings_endpoint_json_body import PatchServicesBINDSettingsEndpointJsonBody
from ...models.patch_services_bind_settings_endpoint_response_400 import PatchServicesBINDSettingsEndpointResponse400
from ...models.patch_services_bind_settings_endpoint_response_401 import PatchServicesBINDSettingsEndpointResponse401
from ...models.patch_services_bind_settings_endpoint_response_403 import PatchServicesBINDSettingsEndpointResponse403
from ...models.patch_services_bind_settings_endpoint_response_404 import PatchServicesBINDSettingsEndpointResponse404
from ...models.patch_services_bind_settings_endpoint_response_405 import PatchServicesBINDSettingsEndpointResponse405
from ...models.patch_services_bind_settings_endpoint_response_406 import PatchServicesBINDSettingsEndpointResponse406
from ...models.patch_services_bind_settings_endpoint_response_409 import PatchServicesBINDSettingsEndpointResponse409
from ...models.patch_services_bind_settings_endpoint_response_415 import PatchServicesBINDSettingsEndpointResponse415
from ...models.patch_services_bind_settings_endpoint_response_422 import PatchServicesBINDSettingsEndpointResponse422
from ...models.patch_services_bind_settings_endpoint_response_424 import PatchServicesBINDSettingsEndpointResponse424
from ...models.patch_services_bind_settings_endpoint_response_500 import PatchServicesBINDSettingsEndpointResponse500
from ...models.patch_services_bind_settings_endpoint_response_503 import PatchServicesBINDSettingsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesBINDSettingsEndpointJsonBody | PatchServicesBINDSettingsEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/bind/settings",
    }

    if isinstance(body, PatchServicesBINDSettingsEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesBINDSettingsEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesBINDSettingsEndpointResponse400
    | PatchServicesBINDSettingsEndpointResponse401
    | PatchServicesBINDSettingsEndpointResponse403
    | PatchServicesBINDSettingsEndpointResponse404
    | PatchServicesBINDSettingsEndpointResponse405
    | PatchServicesBINDSettingsEndpointResponse406
    | PatchServicesBINDSettingsEndpointResponse409
    | PatchServicesBINDSettingsEndpointResponse415
    | PatchServicesBINDSettingsEndpointResponse422
    | PatchServicesBINDSettingsEndpointResponse424
    | PatchServicesBINDSettingsEndpointResponse500
    | PatchServicesBINDSettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesBINDSettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesBINDSettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesBINDSettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesBINDSettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesBINDSettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesBINDSettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesBINDSettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesBINDSettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesBINDSettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesBINDSettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesBINDSettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesBINDSettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesBINDSettingsEndpointResponse400
    | PatchServicesBINDSettingsEndpointResponse401
    | PatchServicesBINDSettingsEndpointResponse403
    | PatchServicesBINDSettingsEndpointResponse404
    | PatchServicesBINDSettingsEndpointResponse405
    | PatchServicesBINDSettingsEndpointResponse406
    | PatchServicesBINDSettingsEndpointResponse409
    | PatchServicesBINDSettingsEndpointResponse415
    | PatchServicesBINDSettingsEndpointResponse422
    | PatchServicesBINDSettingsEndpointResponse424
    | PatchServicesBINDSettingsEndpointResponse500
    | PatchServicesBINDSettingsEndpointResponse503
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
    body: PatchServicesBINDSettingsEndpointJsonBody | PatchServicesBINDSettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesBINDSettingsEndpointResponse400
    | PatchServicesBINDSettingsEndpointResponse401
    | PatchServicesBINDSettingsEndpointResponse403
    | PatchServicesBINDSettingsEndpointResponse404
    | PatchServicesBINDSettingsEndpointResponse405
    | PatchServicesBINDSettingsEndpointResponse406
    | PatchServicesBINDSettingsEndpointResponse409
    | PatchServicesBINDSettingsEndpointResponse415
    | PatchServicesBINDSettingsEndpointResponse422
    | PatchServicesBINDSettingsEndpointResponse424
    | PatchServicesBINDSettingsEndpointResponse500
    | PatchServicesBINDSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current BIND Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDSettingsEndpointJsonBody | Unset):
        body (PatchServicesBINDSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesBINDSettingsEndpointResponse400 | PatchServicesBINDSettingsEndpointResponse401 | PatchServicesBINDSettingsEndpointResponse403 | PatchServicesBINDSettingsEndpointResponse404 | PatchServicesBINDSettingsEndpointResponse405 | PatchServicesBINDSettingsEndpointResponse406 | PatchServicesBINDSettingsEndpointResponse409 | PatchServicesBINDSettingsEndpointResponse415 | PatchServicesBINDSettingsEndpointResponse422 | PatchServicesBINDSettingsEndpointResponse424 | PatchServicesBINDSettingsEndpointResponse500 | PatchServicesBINDSettingsEndpointResponse503]
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
    body: PatchServicesBINDSettingsEndpointJsonBody | PatchServicesBINDSettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesBINDSettingsEndpointResponse400
    | PatchServicesBINDSettingsEndpointResponse401
    | PatchServicesBINDSettingsEndpointResponse403
    | PatchServicesBINDSettingsEndpointResponse404
    | PatchServicesBINDSettingsEndpointResponse405
    | PatchServicesBINDSettingsEndpointResponse406
    | PatchServicesBINDSettingsEndpointResponse409
    | PatchServicesBINDSettingsEndpointResponse415
    | PatchServicesBINDSettingsEndpointResponse422
    | PatchServicesBINDSettingsEndpointResponse424
    | PatchServicesBINDSettingsEndpointResponse500
    | PatchServicesBINDSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current BIND Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDSettingsEndpointJsonBody | Unset):
        body (PatchServicesBINDSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesBINDSettingsEndpointResponse400 | PatchServicesBINDSettingsEndpointResponse401 | PatchServicesBINDSettingsEndpointResponse403 | PatchServicesBINDSettingsEndpointResponse404 | PatchServicesBINDSettingsEndpointResponse405 | PatchServicesBINDSettingsEndpointResponse406 | PatchServicesBINDSettingsEndpointResponse409 | PatchServicesBINDSettingsEndpointResponse415 | PatchServicesBINDSettingsEndpointResponse422 | PatchServicesBINDSettingsEndpointResponse424 | PatchServicesBINDSettingsEndpointResponse500 | PatchServicesBINDSettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesBINDSettingsEndpointJsonBody | PatchServicesBINDSettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesBINDSettingsEndpointResponse400
    | PatchServicesBINDSettingsEndpointResponse401
    | PatchServicesBINDSettingsEndpointResponse403
    | PatchServicesBINDSettingsEndpointResponse404
    | PatchServicesBINDSettingsEndpointResponse405
    | PatchServicesBINDSettingsEndpointResponse406
    | PatchServicesBINDSettingsEndpointResponse409
    | PatchServicesBINDSettingsEndpointResponse415
    | PatchServicesBINDSettingsEndpointResponse422
    | PatchServicesBINDSettingsEndpointResponse424
    | PatchServicesBINDSettingsEndpointResponse500
    | PatchServicesBINDSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current BIND Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDSettingsEndpointJsonBody | Unset):
        body (PatchServicesBINDSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesBINDSettingsEndpointResponse400 | PatchServicesBINDSettingsEndpointResponse401 | PatchServicesBINDSettingsEndpointResponse403 | PatchServicesBINDSettingsEndpointResponse404 | PatchServicesBINDSettingsEndpointResponse405 | PatchServicesBINDSettingsEndpointResponse406 | PatchServicesBINDSettingsEndpointResponse409 | PatchServicesBINDSettingsEndpointResponse415 | PatchServicesBINDSettingsEndpointResponse422 | PatchServicesBINDSettingsEndpointResponse424 | PatchServicesBINDSettingsEndpointResponse500 | PatchServicesBINDSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesBINDSettingsEndpointJsonBody | PatchServicesBINDSettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesBINDSettingsEndpointResponse400
    | PatchServicesBINDSettingsEndpointResponse401
    | PatchServicesBINDSettingsEndpointResponse403
    | PatchServicesBINDSettingsEndpointResponse404
    | PatchServicesBINDSettingsEndpointResponse405
    | PatchServicesBINDSettingsEndpointResponse406
    | PatchServicesBINDSettingsEndpointResponse409
    | PatchServicesBINDSettingsEndpointResponse415
    | PatchServicesBINDSettingsEndpointResponse422
    | PatchServicesBINDSettingsEndpointResponse424
    | PatchServicesBINDSettingsEndpointResponse500
    | PatchServicesBINDSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current BIND Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDSettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-settings-patch ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDSettingsEndpointJsonBody | Unset):
        body (PatchServicesBINDSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesBINDSettingsEndpointResponse400 | PatchServicesBINDSettingsEndpointResponse401 | PatchServicesBINDSettingsEndpointResponse403 | PatchServicesBINDSettingsEndpointResponse404 | PatchServicesBINDSettingsEndpointResponse405 | PatchServicesBINDSettingsEndpointResponse406 | PatchServicesBINDSettingsEndpointResponse409 | PatchServicesBINDSettingsEndpointResponse415 | PatchServicesBINDSettingsEndpointResponse422 | PatchServicesBINDSettingsEndpointResponse424 | PatchServicesBINDSettingsEndpointResponse500 | PatchServicesBINDSettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
