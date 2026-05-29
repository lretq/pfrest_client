from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_restapi_settings_endpoint_data_body import PatchSystemRESTAPISettingsEndpointDataBody
from ...models.patch_system_restapi_settings_endpoint_json_body import PatchSystemRESTAPISettingsEndpointJsonBody
from ...models.patch_system_restapi_settings_endpoint_response_400 import PatchSystemRESTAPISettingsEndpointResponse400
from ...models.patch_system_restapi_settings_endpoint_response_401 import PatchSystemRESTAPISettingsEndpointResponse401
from ...models.patch_system_restapi_settings_endpoint_response_403 import PatchSystemRESTAPISettingsEndpointResponse403
from ...models.patch_system_restapi_settings_endpoint_response_404 import PatchSystemRESTAPISettingsEndpointResponse404
from ...models.patch_system_restapi_settings_endpoint_response_405 import PatchSystemRESTAPISettingsEndpointResponse405
from ...models.patch_system_restapi_settings_endpoint_response_406 import PatchSystemRESTAPISettingsEndpointResponse406
from ...models.patch_system_restapi_settings_endpoint_response_409 import PatchSystemRESTAPISettingsEndpointResponse409
from ...models.patch_system_restapi_settings_endpoint_response_415 import PatchSystemRESTAPISettingsEndpointResponse415
from ...models.patch_system_restapi_settings_endpoint_response_422 import PatchSystemRESTAPISettingsEndpointResponse422
from ...models.patch_system_restapi_settings_endpoint_response_424 import PatchSystemRESTAPISettingsEndpointResponse424
from ...models.patch_system_restapi_settings_endpoint_response_500 import PatchSystemRESTAPISettingsEndpointResponse500
from ...models.patch_system_restapi_settings_endpoint_response_503 import PatchSystemRESTAPISettingsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemRESTAPISettingsEndpointJsonBody | PatchSystemRESTAPISettingsEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/restapi/settings",
    }

    if isinstance(body, PatchSystemRESTAPISettingsEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemRESTAPISettingsEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemRESTAPISettingsEndpointResponse400
    | PatchSystemRESTAPISettingsEndpointResponse401
    | PatchSystemRESTAPISettingsEndpointResponse403
    | PatchSystemRESTAPISettingsEndpointResponse404
    | PatchSystemRESTAPISettingsEndpointResponse405
    | PatchSystemRESTAPISettingsEndpointResponse406
    | PatchSystemRESTAPISettingsEndpointResponse409
    | PatchSystemRESTAPISettingsEndpointResponse415
    | PatchSystemRESTAPISettingsEndpointResponse422
    | PatchSystemRESTAPISettingsEndpointResponse424
    | PatchSystemRESTAPISettingsEndpointResponse500
    | PatchSystemRESTAPISettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemRESTAPISettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemRESTAPISettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemRESTAPISettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemRESTAPISettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemRESTAPISettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemRESTAPISettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemRESTAPISettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemRESTAPISettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemRESTAPISettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemRESTAPISettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemRESTAPISettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemRESTAPISettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemRESTAPISettingsEndpointResponse400
    | PatchSystemRESTAPISettingsEndpointResponse401
    | PatchSystemRESTAPISettingsEndpointResponse403
    | PatchSystemRESTAPISettingsEndpointResponse404
    | PatchSystemRESTAPISettingsEndpointResponse405
    | PatchSystemRESTAPISettingsEndpointResponse406
    | PatchSystemRESTAPISettingsEndpointResponse409
    | PatchSystemRESTAPISettingsEndpointResponse415
    | PatchSystemRESTAPISettingsEndpointResponse422
    | PatchSystemRESTAPISettingsEndpointResponse424
    | PatchSystemRESTAPISettingsEndpointResponse500
    | PatchSystemRESTAPISettingsEndpointResponse503
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
    body: PatchSystemRESTAPISettingsEndpointJsonBody | PatchSystemRESTAPISettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemRESTAPISettingsEndpointResponse400
    | PatchSystemRESTAPISettingsEndpointResponse401
    | PatchSystemRESTAPISettingsEndpointResponse403
    | PatchSystemRESTAPISettingsEndpointResponse404
    | PatchSystemRESTAPISettingsEndpointResponse405
    | PatchSystemRESTAPISettingsEndpointResponse406
    | PatchSystemRESTAPISettingsEndpointResponse409
    | PatchSystemRESTAPISettingsEndpointResponse415
    | PatchSystemRESTAPISettingsEndpointResponse422
    | PatchSystemRESTAPISettingsEndpointResponse424
    | PatchSystemRESTAPISettingsEndpointResponse500
    | PatchSystemRESTAPISettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current REST API Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemRESTAPISettingsEndpointJsonBody | Unset):
        body (PatchSystemRESTAPISettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemRESTAPISettingsEndpointResponse400 | PatchSystemRESTAPISettingsEndpointResponse401 | PatchSystemRESTAPISettingsEndpointResponse403 | PatchSystemRESTAPISettingsEndpointResponse404 | PatchSystemRESTAPISettingsEndpointResponse405 | PatchSystemRESTAPISettingsEndpointResponse406 | PatchSystemRESTAPISettingsEndpointResponse409 | PatchSystemRESTAPISettingsEndpointResponse415 | PatchSystemRESTAPISettingsEndpointResponse422 | PatchSystemRESTAPISettingsEndpointResponse424 | PatchSystemRESTAPISettingsEndpointResponse500 | PatchSystemRESTAPISettingsEndpointResponse503]
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
    body: PatchSystemRESTAPISettingsEndpointJsonBody | PatchSystemRESTAPISettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemRESTAPISettingsEndpointResponse400
    | PatchSystemRESTAPISettingsEndpointResponse401
    | PatchSystemRESTAPISettingsEndpointResponse403
    | PatchSystemRESTAPISettingsEndpointResponse404
    | PatchSystemRESTAPISettingsEndpointResponse405
    | PatchSystemRESTAPISettingsEndpointResponse406
    | PatchSystemRESTAPISettingsEndpointResponse409
    | PatchSystemRESTAPISettingsEndpointResponse415
    | PatchSystemRESTAPISettingsEndpointResponse422
    | PatchSystemRESTAPISettingsEndpointResponse424
    | PatchSystemRESTAPISettingsEndpointResponse500
    | PatchSystemRESTAPISettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current REST API Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemRESTAPISettingsEndpointJsonBody | Unset):
        body (PatchSystemRESTAPISettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemRESTAPISettingsEndpointResponse400 | PatchSystemRESTAPISettingsEndpointResponse401 | PatchSystemRESTAPISettingsEndpointResponse403 | PatchSystemRESTAPISettingsEndpointResponse404 | PatchSystemRESTAPISettingsEndpointResponse405 | PatchSystemRESTAPISettingsEndpointResponse406 | PatchSystemRESTAPISettingsEndpointResponse409 | PatchSystemRESTAPISettingsEndpointResponse415 | PatchSystemRESTAPISettingsEndpointResponse422 | PatchSystemRESTAPISettingsEndpointResponse424 | PatchSystemRESTAPISettingsEndpointResponse500 | PatchSystemRESTAPISettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemRESTAPISettingsEndpointJsonBody | PatchSystemRESTAPISettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemRESTAPISettingsEndpointResponse400
    | PatchSystemRESTAPISettingsEndpointResponse401
    | PatchSystemRESTAPISettingsEndpointResponse403
    | PatchSystemRESTAPISettingsEndpointResponse404
    | PatchSystemRESTAPISettingsEndpointResponse405
    | PatchSystemRESTAPISettingsEndpointResponse406
    | PatchSystemRESTAPISettingsEndpointResponse409
    | PatchSystemRESTAPISettingsEndpointResponse415
    | PatchSystemRESTAPISettingsEndpointResponse422
    | PatchSystemRESTAPISettingsEndpointResponse424
    | PatchSystemRESTAPISettingsEndpointResponse500
    | PatchSystemRESTAPISettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current REST API Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemRESTAPISettingsEndpointJsonBody | Unset):
        body (PatchSystemRESTAPISettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemRESTAPISettingsEndpointResponse400 | PatchSystemRESTAPISettingsEndpointResponse401 | PatchSystemRESTAPISettingsEndpointResponse403 | PatchSystemRESTAPISettingsEndpointResponse404 | PatchSystemRESTAPISettingsEndpointResponse405 | PatchSystemRESTAPISettingsEndpointResponse406 | PatchSystemRESTAPISettingsEndpointResponse409 | PatchSystemRESTAPISettingsEndpointResponse415 | PatchSystemRESTAPISettingsEndpointResponse422 | PatchSystemRESTAPISettingsEndpointResponse424 | PatchSystemRESTAPISettingsEndpointResponse500 | PatchSystemRESTAPISettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemRESTAPISettingsEndpointJsonBody | PatchSystemRESTAPISettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemRESTAPISettingsEndpointResponse400
    | PatchSystemRESTAPISettingsEndpointResponse401
    | PatchSystemRESTAPISettingsEndpointResponse403
    | PatchSystemRESTAPISettingsEndpointResponse404
    | PatchSystemRESTAPISettingsEndpointResponse405
    | PatchSystemRESTAPISettingsEndpointResponse406
    | PatchSystemRESTAPISettingsEndpointResponse409
    | PatchSystemRESTAPISettingsEndpointResponse415
    | PatchSystemRESTAPISettingsEndpointResponse422
    | PatchSystemRESTAPISettingsEndpointResponse424
    | PatchSystemRESTAPISettingsEndpointResponse500
    | PatchSystemRESTAPISettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current REST API Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemRESTAPISettingsEndpointJsonBody | Unset):
        body (PatchSystemRESTAPISettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemRESTAPISettingsEndpointResponse400 | PatchSystemRESTAPISettingsEndpointResponse401 | PatchSystemRESTAPISettingsEndpointResponse403 | PatchSystemRESTAPISettingsEndpointResponse404 | PatchSystemRESTAPISettingsEndpointResponse405 | PatchSystemRESTAPISettingsEndpointResponse406 | PatchSystemRESTAPISettingsEndpointResponse409 | PatchSystemRESTAPISettingsEndpointResponse415 | PatchSystemRESTAPISettingsEndpointResponse422 | PatchSystemRESTAPISettingsEndpointResponse424 | PatchSystemRESTAPISettingsEndpointResponse500 | PatchSystemRESTAPISettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
