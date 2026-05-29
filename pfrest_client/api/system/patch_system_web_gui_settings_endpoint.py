from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_web_gui_settings_endpoint_data_body import PatchSystemWebGUISettingsEndpointDataBody
from ...models.patch_system_web_gui_settings_endpoint_json_body import PatchSystemWebGUISettingsEndpointJsonBody
from ...models.patch_system_web_gui_settings_endpoint_response_400 import PatchSystemWebGUISettingsEndpointResponse400
from ...models.patch_system_web_gui_settings_endpoint_response_401 import PatchSystemWebGUISettingsEndpointResponse401
from ...models.patch_system_web_gui_settings_endpoint_response_403 import PatchSystemWebGUISettingsEndpointResponse403
from ...models.patch_system_web_gui_settings_endpoint_response_404 import PatchSystemWebGUISettingsEndpointResponse404
from ...models.patch_system_web_gui_settings_endpoint_response_405 import PatchSystemWebGUISettingsEndpointResponse405
from ...models.patch_system_web_gui_settings_endpoint_response_406 import PatchSystemWebGUISettingsEndpointResponse406
from ...models.patch_system_web_gui_settings_endpoint_response_409 import PatchSystemWebGUISettingsEndpointResponse409
from ...models.patch_system_web_gui_settings_endpoint_response_415 import PatchSystemWebGUISettingsEndpointResponse415
from ...models.patch_system_web_gui_settings_endpoint_response_422 import PatchSystemWebGUISettingsEndpointResponse422
from ...models.patch_system_web_gui_settings_endpoint_response_424 import PatchSystemWebGUISettingsEndpointResponse424
from ...models.patch_system_web_gui_settings_endpoint_response_500 import PatchSystemWebGUISettingsEndpointResponse500
from ...models.patch_system_web_gui_settings_endpoint_response_503 import PatchSystemWebGUISettingsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemWebGUISettingsEndpointJsonBody | PatchSystemWebGUISettingsEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/webgui/settings",
    }

    if isinstance(body, PatchSystemWebGUISettingsEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemWebGUISettingsEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemWebGUISettingsEndpointResponse400
    | PatchSystemWebGUISettingsEndpointResponse401
    | PatchSystemWebGUISettingsEndpointResponse403
    | PatchSystemWebGUISettingsEndpointResponse404
    | PatchSystemWebGUISettingsEndpointResponse405
    | PatchSystemWebGUISettingsEndpointResponse406
    | PatchSystemWebGUISettingsEndpointResponse409
    | PatchSystemWebGUISettingsEndpointResponse415
    | PatchSystemWebGUISettingsEndpointResponse422
    | PatchSystemWebGUISettingsEndpointResponse424
    | PatchSystemWebGUISettingsEndpointResponse500
    | PatchSystemWebGUISettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemWebGUISettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemWebGUISettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemWebGUISettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemWebGUISettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemWebGUISettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemWebGUISettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemWebGUISettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemWebGUISettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemWebGUISettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemWebGUISettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemWebGUISettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemWebGUISettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemWebGUISettingsEndpointResponse400
    | PatchSystemWebGUISettingsEndpointResponse401
    | PatchSystemWebGUISettingsEndpointResponse403
    | PatchSystemWebGUISettingsEndpointResponse404
    | PatchSystemWebGUISettingsEndpointResponse405
    | PatchSystemWebGUISettingsEndpointResponse406
    | PatchSystemWebGUISettingsEndpointResponse409
    | PatchSystemWebGUISettingsEndpointResponse415
    | PatchSystemWebGUISettingsEndpointResponse422
    | PatchSystemWebGUISettingsEndpointResponse424
    | PatchSystemWebGUISettingsEndpointResponse500
    | PatchSystemWebGUISettingsEndpointResponse503
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
    body: PatchSystemWebGUISettingsEndpointJsonBody | PatchSystemWebGUISettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemWebGUISettingsEndpointResponse400
    | PatchSystemWebGUISettingsEndpointResponse401
    | PatchSystemWebGUISettingsEndpointResponse403
    | PatchSystemWebGUISettingsEndpointResponse404
    | PatchSystemWebGUISettingsEndpointResponse405
    | PatchSystemWebGUISettingsEndpointResponse406
    | PatchSystemWebGUISettingsEndpointResponse409
    | PatchSystemWebGUISettingsEndpointResponse415
    | PatchSystemWebGUISettingsEndpointResponse422
    | PatchSystemWebGUISettingsEndpointResponse424
    | PatchSystemWebGUISettingsEndpointResponse500
    | PatchSystemWebGUISettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Web GUI Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WebGUISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-webgui-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemWebGUISettingsEndpointJsonBody | Unset):
        body (PatchSystemWebGUISettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemWebGUISettingsEndpointResponse400 | PatchSystemWebGUISettingsEndpointResponse401 | PatchSystemWebGUISettingsEndpointResponse403 | PatchSystemWebGUISettingsEndpointResponse404 | PatchSystemWebGUISettingsEndpointResponse405 | PatchSystemWebGUISettingsEndpointResponse406 | PatchSystemWebGUISettingsEndpointResponse409 | PatchSystemWebGUISettingsEndpointResponse415 | PatchSystemWebGUISettingsEndpointResponse422 | PatchSystemWebGUISettingsEndpointResponse424 | PatchSystemWebGUISettingsEndpointResponse500 | PatchSystemWebGUISettingsEndpointResponse503]
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
    body: PatchSystemWebGUISettingsEndpointJsonBody | PatchSystemWebGUISettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemWebGUISettingsEndpointResponse400
    | PatchSystemWebGUISettingsEndpointResponse401
    | PatchSystemWebGUISettingsEndpointResponse403
    | PatchSystemWebGUISettingsEndpointResponse404
    | PatchSystemWebGUISettingsEndpointResponse405
    | PatchSystemWebGUISettingsEndpointResponse406
    | PatchSystemWebGUISettingsEndpointResponse409
    | PatchSystemWebGUISettingsEndpointResponse415
    | PatchSystemWebGUISettingsEndpointResponse422
    | PatchSystemWebGUISettingsEndpointResponse424
    | PatchSystemWebGUISettingsEndpointResponse500
    | PatchSystemWebGUISettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Web GUI Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WebGUISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-webgui-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemWebGUISettingsEndpointJsonBody | Unset):
        body (PatchSystemWebGUISettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemWebGUISettingsEndpointResponse400 | PatchSystemWebGUISettingsEndpointResponse401 | PatchSystemWebGUISettingsEndpointResponse403 | PatchSystemWebGUISettingsEndpointResponse404 | PatchSystemWebGUISettingsEndpointResponse405 | PatchSystemWebGUISettingsEndpointResponse406 | PatchSystemWebGUISettingsEndpointResponse409 | PatchSystemWebGUISettingsEndpointResponse415 | PatchSystemWebGUISettingsEndpointResponse422 | PatchSystemWebGUISettingsEndpointResponse424 | PatchSystemWebGUISettingsEndpointResponse500 | PatchSystemWebGUISettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemWebGUISettingsEndpointJsonBody | PatchSystemWebGUISettingsEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemWebGUISettingsEndpointResponse400
    | PatchSystemWebGUISettingsEndpointResponse401
    | PatchSystemWebGUISettingsEndpointResponse403
    | PatchSystemWebGUISettingsEndpointResponse404
    | PatchSystemWebGUISettingsEndpointResponse405
    | PatchSystemWebGUISettingsEndpointResponse406
    | PatchSystemWebGUISettingsEndpointResponse409
    | PatchSystemWebGUISettingsEndpointResponse415
    | PatchSystemWebGUISettingsEndpointResponse422
    | PatchSystemWebGUISettingsEndpointResponse424
    | PatchSystemWebGUISettingsEndpointResponse500
    | PatchSystemWebGUISettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Web GUI Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WebGUISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-webgui-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemWebGUISettingsEndpointJsonBody | Unset):
        body (PatchSystemWebGUISettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemWebGUISettingsEndpointResponse400 | PatchSystemWebGUISettingsEndpointResponse401 | PatchSystemWebGUISettingsEndpointResponse403 | PatchSystemWebGUISettingsEndpointResponse404 | PatchSystemWebGUISettingsEndpointResponse405 | PatchSystemWebGUISettingsEndpointResponse406 | PatchSystemWebGUISettingsEndpointResponse409 | PatchSystemWebGUISettingsEndpointResponse415 | PatchSystemWebGUISettingsEndpointResponse422 | PatchSystemWebGUISettingsEndpointResponse424 | PatchSystemWebGUISettingsEndpointResponse500 | PatchSystemWebGUISettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemWebGUISettingsEndpointJsonBody | PatchSystemWebGUISettingsEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemWebGUISettingsEndpointResponse400
    | PatchSystemWebGUISettingsEndpointResponse401
    | PatchSystemWebGUISettingsEndpointResponse403
    | PatchSystemWebGUISettingsEndpointResponse404
    | PatchSystemWebGUISettingsEndpointResponse405
    | PatchSystemWebGUISettingsEndpointResponse406
    | PatchSystemWebGUISettingsEndpointResponse409
    | PatchSystemWebGUISettingsEndpointResponse415
    | PatchSystemWebGUISettingsEndpointResponse422
    | PatchSystemWebGUISettingsEndpointResponse424
    | PatchSystemWebGUISettingsEndpointResponse500
    | PatchSystemWebGUISettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Web GUI Settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WebGUISettings<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-webgui-settings-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemWebGUISettingsEndpointJsonBody | Unset):
        body (PatchSystemWebGUISettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemWebGUISettingsEndpointResponse400 | PatchSystemWebGUISettingsEndpointResponse401 | PatchSystemWebGUISettingsEndpointResponse403 | PatchSystemWebGUISettingsEndpointResponse404 | PatchSystemWebGUISettingsEndpointResponse405 | PatchSystemWebGUISettingsEndpointResponse406 | PatchSystemWebGUISettingsEndpointResponse409 | PatchSystemWebGUISettingsEndpointResponse415 | PatchSystemWebGUISettingsEndpointResponse422 | PatchSystemWebGUISettingsEndpointResponse424 | PatchSystemWebGUISettingsEndpointResponse500 | PatchSystemWebGUISettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
