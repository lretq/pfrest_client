from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_notifications_email_settings_endpoint_response_400 import (
    GetSystemNotificationsEmailSettingsEndpointResponse400,
)
from ...models.get_system_notifications_email_settings_endpoint_response_401 import (
    GetSystemNotificationsEmailSettingsEndpointResponse401,
)
from ...models.get_system_notifications_email_settings_endpoint_response_403 import (
    GetSystemNotificationsEmailSettingsEndpointResponse403,
)
from ...models.get_system_notifications_email_settings_endpoint_response_404 import (
    GetSystemNotificationsEmailSettingsEndpointResponse404,
)
from ...models.get_system_notifications_email_settings_endpoint_response_405 import (
    GetSystemNotificationsEmailSettingsEndpointResponse405,
)
from ...models.get_system_notifications_email_settings_endpoint_response_406 import (
    GetSystemNotificationsEmailSettingsEndpointResponse406,
)
from ...models.get_system_notifications_email_settings_endpoint_response_409 import (
    GetSystemNotificationsEmailSettingsEndpointResponse409,
)
from ...models.get_system_notifications_email_settings_endpoint_response_415 import (
    GetSystemNotificationsEmailSettingsEndpointResponse415,
)
from ...models.get_system_notifications_email_settings_endpoint_response_422 import (
    GetSystemNotificationsEmailSettingsEndpointResponse422,
)
from ...models.get_system_notifications_email_settings_endpoint_response_424 import (
    GetSystemNotificationsEmailSettingsEndpointResponse424,
)
from ...models.get_system_notifications_email_settings_endpoint_response_500 import (
    GetSystemNotificationsEmailSettingsEndpointResponse500,
)
from ...models.get_system_notifications_email_settings_endpoint_response_503 import (
    GetSystemNotificationsEmailSettingsEndpointResponse503,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/notifications/email_settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemNotificationsEmailSettingsEndpointResponse400
    | GetSystemNotificationsEmailSettingsEndpointResponse401
    | GetSystemNotificationsEmailSettingsEndpointResponse403
    | GetSystemNotificationsEmailSettingsEndpointResponse404
    | GetSystemNotificationsEmailSettingsEndpointResponse405
    | GetSystemNotificationsEmailSettingsEndpointResponse406
    | GetSystemNotificationsEmailSettingsEndpointResponse409
    | GetSystemNotificationsEmailSettingsEndpointResponse415
    | GetSystemNotificationsEmailSettingsEndpointResponse422
    | GetSystemNotificationsEmailSettingsEndpointResponse424
    | GetSystemNotificationsEmailSettingsEndpointResponse500
    | GetSystemNotificationsEmailSettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemNotificationsEmailSettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemNotificationsEmailSettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemNotificationsEmailSettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemNotificationsEmailSettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemNotificationsEmailSettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemNotificationsEmailSettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemNotificationsEmailSettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemNotificationsEmailSettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemNotificationsEmailSettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemNotificationsEmailSettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemNotificationsEmailSettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemNotificationsEmailSettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemNotificationsEmailSettingsEndpointResponse400
    | GetSystemNotificationsEmailSettingsEndpointResponse401
    | GetSystemNotificationsEmailSettingsEndpointResponse403
    | GetSystemNotificationsEmailSettingsEndpointResponse404
    | GetSystemNotificationsEmailSettingsEndpointResponse405
    | GetSystemNotificationsEmailSettingsEndpointResponse406
    | GetSystemNotificationsEmailSettingsEndpointResponse409
    | GetSystemNotificationsEmailSettingsEndpointResponse415
    | GetSystemNotificationsEmailSettingsEndpointResponse422
    | GetSystemNotificationsEmailSettingsEndpointResponse424
    | GetSystemNotificationsEmailSettingsEndpointResponse500
    | GetSystemNotificationsEmailSettingsEndpointResponse503
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
    GetSystemNotificationsEmailSettingsEndpointResponse400
    | GetSystemNotificationsEmailSettingsEndpointResponse401
    | GetSystemNotificationsEmailSettingsEndpointResponse403
    | GetSystemNotificationsEmailSettingsEndpointResponse404
    | GetSystemNotificationsEmailSettingsEndpointResponse405
    | GetSystemNotificationsEmailSettingsEndpointResponse406
    | GetSystemNotificationsEmailSettingsEndpointResponse409
    | GetSystemNotificationsEmailSettingsEndpointResponse415
    | GetSystemNotificationsEmailSettingsEndpointResponse422
    | GetSystemNotificationsEmailSettingsEndpointResponse424
    | GetSystemNotificationsEmailSettingsEndpointResponse500
    | GetSystemNotificationsEmailSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Email Notification Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: EmailNotificationSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-notifications-email-
    settings-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemNotificationsEmailSettingsEndpointResponse400 | GetSystemNotificationsEmailSettingsEndpointResponse401 | GetSystemNotificationsEmailSettingsEndpointResponse403 | GetSystemNotificationsEmailSettingsEndpointResponse404 | GetSystemNotificationsEmailSettingsEndpointResponse405 | GetSystemNotificationsEmailSettingsEndpointResponse406 | GetSystemNotificationsEmailSettingsEndpointResponse409 | GetSystemNotificationsEmailSettingsEndpointResponse415 | GetSystemNotificationsEmailSettingsEndpointResponse422 | GetSystemNotificationsEmailSettingsEndpointResponse424 | GetSystemNotificationsEmailSettingsEndpointResponse500 | GetSystemNotificationsEmailSettingsEndpointResponse503]
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
    GetSystemNotificationsEmailSettingsEndpointResponse400
    | GetSystemNotificationsEmailSettingsEndpointResponse401
    | GetSystemNotificationsEmailSettingsEndpointResponse403
    | GetSystemNotificationsEmailSettingsEndpointResponse404
    | GetSystemNotificationsEmailSettingsEndpointResponse405
    | GetSystemNotificationsEmailSettingsEndpointResponse406
    | GetSystemNotificationsEmailSettingsEndpointResponse409
    | GetSystemNotificationsEmailSettingsEndpointResponse415
    | GetSystemNotificationsEmailSettingsEndpointResponse422
    | GetSystemNotificationsEmailSettingsEndpointResponse424
    | GetSystemNotificationsEmailSettingsEndpointResponse500
    | GetSystemNotificationsEmailSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Email Notification Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: EmailNotificationSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-notifications-email-
    settings-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemNotificationsEmailSettingsEndpointResponse400 | GetSystemNotificationsEmailSettingsEndpointResponse401 | GetSystemNotificationsEmailSettingsEndpointResponse403 | GetSystemNotificationsEmailSettingsEndpointResponse404 | GetSystemNotificationsEmailSettingsEndpointResponse405 | GetSystemNotificationsEmailSettingsEndpointResponse406 | GetSystemNotificationsEmailSettingsEndpointResponse409 | GetSystemNotificationsEmailSettingsEndpointResponse415 | GetSystemNotificationsEmailSettingsEndpointResponse422 | GetSystemNotificationsEmailSettingsEndpointResponse424 | GetSystemNotificationsEmailSettingsEndpointResponse500 | GetSystemNotificationsEmailSettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemNotificationsEmailSettingsEndpointResponse400
    | GetSystemNotificationsEmailSettingsEndpointResponse401
    | GetSystemNotificationsEmailSettingsEndpointResponse403
    | GetSystemNotificationsEmailSettingsEndpointResponse404
    | GetSystemNotificationsEmailSettingsEndpointResponse405
    | GetSystemNotificationsEmailSettingsEndpointResponse406
    | GetSystemNotificationsEmailSettingsEndpointResponse409
    | GetSystemNotificationsEmailSettingsEndpointResponse415
    | GetSystemNotificationsEmailSettingsEndpointResponse422
    | GetSystemNotificationsEmailSettingsEndpointResponse424
    | GetSystemNotificationsEmailSettingsEndpointResponse500
    | GetSystemNotificationsEmailSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Email Notification Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: EmailNotificationSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-notifications-email-
    settings-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemNotificationsEmailSettingsEndpointResponse400 | GetSystemNotificationsEmailSettingsEndpointResponse401 | GetSystemNotificationsEmailSettingsEndpointResponse403 | GetSystemNotificationsEmailSettingsEndpointResponse404 | GetSystemNotificationsEmailSettingsEndpointResponse405 | GetSystemNotificationsEmailSettingsEndpointResponse406 | GetSystemNotificationsEmailSettingsEndpointResponse409 | GetSystemNotificationsEmailSettingsEndpointResponse415 | GetSystemNotificationsEmailSettingsEndpointResponse422 | GetSystemNotificationsEmailSettingsEndpointResponse424 | GetSystemNotificationsEmailSettingsEndpointResponse500 | GetSystemNotificationsEmailSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemNotificationsEmailSettingsEndpointResponse400
    | GetSystemNotificationsEmailSettingsEndpointResponse401
    | GetSystemNotificationsEmailSettingsEndpointResponse403
    | GetSystemNotificationsEmailSettingsEndpointResponse404
    | GetSystemNotificationsEmailSettingsEndpointResponse405
    | GetSystemNotificationsEmailSettingsEndpointResponse406
    | GetSystemNotificationsEmailSettingsEndpointResponse409
    | GetSystemNotificationsEmailSettingsEndpointResponse415
    | GetSystemNotificationsEmailSettingsEndpointResponse422
    | GetSystemNotificationsEmailSettingsEndpointResponse424
    | GetSystemNotificationsEmailSettingsEndpointResponse500
    | GetSystemNotificationsEmailSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Email Notification Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: EmailNotificationSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-notifications-email-
    settings-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemNotificationsEmailSettingsEndpointResponse400 | GetSystemNotificationsEmailSettingsEndpointResponse401 | GetSystemNotificationsEmailSettingsEndpointResponse403 | GetSystemNotificationsEmailSettingsEndpointResponse404 | GetSystemNotificationsEmailSettingsEndpointResponse405 | GetSystemNotificationsEmailSettingsEndpointResponse406 | GetSystemNotificationsEmailSettingsEndpointResponse409 | GetSystemNotificationsEmailSettingsEndpointResponse415 | GetSystemNotificationsEmailSettingsEndpointResponse422 | GetSystemNotificationsEmailSettingsEndpointResponse424 | GetSystemNotificationsEmailSettingsEndpointResponse500 | GetSystemNotificationsEmailSettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
