from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_web_gui_settings_endpoint_response_400 import GetSystemWebGUISettingsEndpointResponse400
from ...models.get_system_web_gui_settings_endpoint_response_401 import GetSystemWebGUISettingsEndpointResponse401
from ...models.get_system_web_gui_settings_endpoint_response_403 import GetSystemWebGUISettingsEndpointResponse403
from ...models.get_system_web_gui_settings_endpoint_response_404 import GetSystemWebGUISettingsEndpointResponse404
from ...models.get_system_web_gui_settings_endpoint_response_405 import GetSystemWebGUISettingsEndpointResponse405
from ...models.get_system_web_gui_settings_endpoint_response_406 import GetSystemWebGUISettingsEndpointResponse406
from ...models.get_system_web_gui_settings_endpoint_response_409 import GetSystemWebGUISettingsEndpointResponse409
from ...models.get_system_web_gui_settings_endpoint_response_415 import GetSystemWebGUISettingsEndpointResponse415
from ...models.get_system_web_gui_settings_endpoint_response_422 import GetSystemWebGUISettingsEndpointResponse422
from ...models.get_system_web_gui_settings_endpoint_response_424 import GetSystemWebGUISettingsEndpointResponse424
from ...models.get_system_web_gui_settings_endpoint_response_500 import GetSystemWebGUISettingsEndpointResponse500
from ...models.get_system_web_gui_settings_endpoint_response_503 import GetSystemWebGUISettingsEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/webgui/settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemWebGUISettingsEndpointResponse400
    | GetSystemWebGUISettingsEndpointResponse401
    | GetSystemWebGUISettingsEndpointResponse403
    | GetSystemWebGUISettingsEndpointResponse404
    | GetSystemWebGUISettingsEndpointResponse405
    | GetSystemWebGUISettingsEndpointResponse406
    | GetSystemWebGUISettingsEndpointResponse409
    | GetSystemWebGUISettingsEndpointResponse415
    | GetSystemWebGUISettingsEndpointResponse422
    | GetSystemWebGUISettingsEndpointResponse424
    | GetSystemWebGUISettingsEndpointResponse500
    | GetSystemWebGUISettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemWebGUISettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemWebGUISettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemWebGUISettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemWebGUISettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemWebGUISettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemWebGUISettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemWebGUISettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemWebGUISettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemWebGUISettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemWebGUISettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemWebGUISettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemWebGUISettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemWebGUISettingsEndpointResponse400
    | GetSystemWebGUISettingsEndpointResponse401
    | GetSystemWebGUISettingsEndpointResponse403
    | GetSystemWebGUISettingsEndpointResponse404
    | GetSystemWebGUISettingsEndpointResponse405
    | GetSystemWebGUISettingsEndpointResponse406
    | GetSystemWebGUISettingsEndpointResponse409
    | GetSystemWebGUISettingsEndpointResponse415
    | GetSystemWebGUISettingsEndpointResponse422
    | GetSystemWebGUISettingsEndpointResponse424
    | GetSystemWebGUISettingsEndpointResponse500
    | GetSystemWebGUISettingsEndpointResponse503
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
    GetSystemWebGUISettingsEndpointResponse400
    | GetSystemWebGUISettingsEndpointResponse401
    | GetSystemWebGUISettingsEndpointResponse403
    | GetSystemWebGUISettingsEndpointResponse404
    | GetSystemWebGUISettingsEndpointResponse405
    | GetSystemWebGUISettingsEndpointResponse406
    | GetSystemWebGUISettingsEndpointResponse409
    | GetSystemWebGUISettingsEndpointResponse415
    | GetSystemWebGUISettingsEndpointResponse422
    | GetSystemWebGUISettingsEndpointResponse424
    | GetSystemWebGUISettingsEndpointResponse500
    | GetSystemWebGUISettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Web GUI Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WebGUISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-webgui-settings-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemWebGUISettingsEndpointResponse400 | GetSystemWebGUISettingsEndpointResponse401 | GetSystemWebGUISettingsEndpointResponse403 | GetSystemWebGUISettingsEndpointResponse404 | GetSystemWebGUISettingsEndpointResponse405 | GetSystemWebGUISettingsEndpointResponse406 | GetSystemWebGUISettingsEndpointResponse409 | GetSystemWebGUISettingsEndpointResponse415 | GetSystemWebGUISettingsEndpointResponse422 | GetSystemWebGUISettingsEndpointResponse424 | GetSystemWebGUISettingsEndpointResponse500 | GetSystemWebGUISettingsEndpointResponse503]
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
    GetSystemWebGUISettingsEndpointResponse400
    | GetSystemWebGUISettingsEndpointResponse401
    | GetSystemWebGUISettingsEndpointResponse403
    | GetSystemWebGUISettingsEndpointResponse404
    | GetSystemWebGUISettingsEndpointResponse405
    | GetSystemWebGUISettingsEndpointResponse406
    | GetSystemWebGUISettingsEndpointResponse409
    | GetSystemWebGUISettingsEndpointResponse415
    | GetSystemWebGUISettingsEndpointResponse422
    | GetSystemWebGUISettingsEndpointResponse424
    | GetSystemWebGUISettingsEndpointResponse500
    | GetSystemWebGUISettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Web GUI Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WebGUISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-webgui-settings-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemWebGUISettingsEndpointResponse400 | GetSystemWebGUISettingsEndpointResponse401 | GetSystemWebGUISettingsEndpointResponse403 | GetSystemWebGUISettingsEndpointResponse404 | GetSystemWebGUISettingsEndpointResponse405 | GetSystemWebGUISettingsEndpointResponse406 | GetSystemWebGUISettingsEndpointResponse409 | GetSystemWebGUISettingsEndpointResponse415 | GetSystemWebGUISettingsEndpointResponse422 | GetSystemWebGUISettingsEndpointResponse424 | GetSystemWebGUISettingsEndpointResponse500 | GetSystemWebGUISettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemWebGUISettingsEndpointResponse400
    | GetSystemWebGUISettingsEndpointResponse401
    | GetSystemWebGUISettingsEndpointResponse403
    | GetSystemWebGUISettingsEndpointResponse404
    | GetSystemWebGUISettingsEndpointResponse405
    | GetSystemWebGUISettingsEndpointResponse406
    | GetSystemWebGUISettingsEndpointResponse409
    | GetSystemWebGUISettingsEndpointResponse415
    | GetSystemWebGUISettingsEndpointResponse422
    | GetSystemWebGUISettingsEndpointResponse424
    | GetSystemWebGUISettingsEndpointResponse500
    | GetSystemWebGUISettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Web GUI Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WebGUISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-webgui-settings-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemWebGUISettingsEndpointResponse400 | GetSystemWebGUISettingsEndpointResponse401 | GetSystemWebGUISettingsEndpointResponse403 | GetSystemWebGUISettingsEndpointResponse404 | GetSystemWebGUISettingsEndpointResponse405 | GetSystemWebGUISettingsEndpointResponse406 | GetSystemWebGUISettingsEndpointResponse409 | GetSystemWebGUISettingsEndpointResponse415 | GetSystemWebGUISettingsEndpointResponse422 | GetSystemWebGUISettingsEndpointResponse424 | GetSystemWebGUISettingsEndpointResponse500 | GetSystemWebGUISettingsEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemWebGUISettingsEndpointResponse400
    | GetSystemWebGUISettingsEndpointResponse401
    | GetSystemWebGUISettingsEndpointResponse403
    | GetSystemWebGUISettingsEndpointResponse404
    | GetSystemWebGUISettingsEndpointResponse405
    | GetSystemWebGUISettingsEndpointResponse406
    | GetSystemWebGUISettingsEndpointResponse409
    | GetSystemWebGUISettingsEndpointResponse415
    | GetSystemWebGUISettingsEndpointResponse422
    | GetSystemWebGUISettingsEndpointResponse424
    | GetSystemWebGUISettingsEndpointResponse500
    | GetSystemWebGUISettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Web GUI Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WebGUISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-webgui-settings-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemWebGUISettingsEndpointResponse400 | GetSystemWebGUISettingsEndpointResponse401 | GetSystemWebGUISettingsEndpointResponse403 | GetSystemWebGUISettingsEndpointResponse404 | GetSystemWebGUISettingsEndpointResponse405 | GetSystemWebGUISettingsEndpointResponse406 | GetSystemWebGUISettingsEndpointResponse409 | GetSystemWebGUISettingsEndpointResponse415 | GetSystemWebGUISettingsEndpointResponse422 | GetSystemWebGUISettingsEndpointResponse424 | GetSystemWebGUISettingsEndpointResponse500 | GetSystemWebGUISettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
