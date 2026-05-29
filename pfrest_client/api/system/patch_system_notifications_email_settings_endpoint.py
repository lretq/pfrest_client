from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_notifications_email_settings_endpoint_data_body import (
    PatchSystemNotificationsEmailSettingsEndpointDataBody,
)
from ...models.patch_system_notifications_email_settings_endpoint_json_body import (
    PatchSystemNotificationsEmailSettingsEndpointJsonBody,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_400 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse400,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_401 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse401,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_403 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse403,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_404 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse404,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_405 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse405,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_406 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse406,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_409 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse409,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_415 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse415,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_422 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse422,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_424 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse424,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_500 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse500,
)
from ...models.patch_system_notifications_email_settings_endpoint_response_503 import (
    PatchSystemNotificationsEmailSettingsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemNotificationsEmailSettingsEndpointJsonBody
    | PatchSystemNotificationsEmailSettingsEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/notifications/email_settings",
    }

    if isinstance(body, PatchSystemNotificationsEmailSettingsEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemNotificationsEmailSettingsEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemNotificationsEmailSettingsEndpointResponse400
    | PatchSystemNotificationsEmailSettingsEndpointResponse401
    | PatchSystemNotificationsEmailSettingsEndpointResponse403
    | PatchSystemNotificationsEmailSettingsEndpointResponse404
    | PatchSystemNotificationsEmailSettingsEndpointResponse405
    | PatchSystemNotificationsEmailSettingsEndpointResponse406
    | PatchSystemNotificationsEmailSettingsEndpointResponse409
    | PatchSystemNotificationsEmailSettingsEndpointResponse415
    | PatchSystemNotificationsEmailSettingsEndpointResponse422
    | PatchSystemNotificationsEmailSettingsEndpointResponse424
    | PatchSystemNotificationsEmailSettingsEndpointResponse500
    | PatchSystemNotificationsEmailSettingsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemNotificationsEmailSettingsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemNotificationsEmailSettingsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemNotificationsEmailSettingsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemNotificationsEmailSettingsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemNotificationsEmailSettingsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemNotificationsEmailSettingsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemNotificationsEmailSettingsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemNotificationsEmailSettingsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemNotificationsEmailSettingsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemNotificationsEmailSettingsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemNotificationsEmailSettingsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemNotificationsEmailSettingsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemNotificationsEmailSettingsEndpointResponse400
    | PatchSystemNotificationsEmailSettingsEndpointResponse401
    | PatchSystemNotificationsEmailSettingsEndpointResponse403
    | PatchSystemNotificationsEmailSettingsEndpointResponse404
    | PatchSystemNotificationsEmailSettingsEndpointResponse405
    | PatchSystemNotificationsEmailSettingsEndpointResponse406
    | PatchSystemNotificationsEmailSettingsEndpointResponse409
    | PatchSystemNotificationsEmailSettingsEndpointResponse415
    | PatchSystemNotificationsEmailSettingsEndpointResponse422
    | PatchSystemNotificationsEmailSettingsEndpointResponse424
    | PatchSystemNotificationsEmailSettingsEndpointResponse500
    | PatchSystemNotificationsEmailSettingsEndpointResponse503
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
    body: PatchSystemNotificationsEmailSettingsEndpointJsonBody
    | PatchSystemNotificationsEmailSettingsEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchSystemNotificationsEmailSettingsEndpointResponse400
    | PatchSystemNotificationsEmailSettingsEndpointResponse401
    | PatchSystemNotificationsEmailSettingsEndpointResponse403
    | PatchSystemNotificationsEmailSettingsEndpointResponse404
    | PatchSystemNotificationsEmailSettingsEndpointResponse405
    | PatchSystemNotificationsEmailSettingsEndpointResponse406
    | PatchSystemNotificationsEmailSettingsEndpointResponse409
    | PatchSystemNotificationsEmailSettingsEndpointResponse415
    | PatchSystemNotificationsEmailSettingsEndpointResponse422
    | PatchSystemNotificationsEmailSettingsEndpointResponse424
    | PatchSystemNotificationsEmailSettingsEndpointResponse500
    | PatchSystemNotificationsEmailSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Email Notification Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: EmailNotificationSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-notifications-email-
    settings-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchSystemNotificationsEmailSettingsEndpointJsonBody | Unset):
        body (PatchSystemNotificationsEmailSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemNotificationsEmailSettingsEndpointResponse400 | PatchSystemNotificationsEmailSettingsEndpointResponse401 | PatchSystemNotificationsEmailSettingsEndpointResponse403 | PatchSystemNotificationsEmailSettingsEndpointResponse404 | PatchSystemNotificationsEmailSettingsEndpointResponse405 | PatchSystemNotificationsEmailSettingsEndpointResponse406 | PatchSystemNotificationsEmailSettingsEndpointResponse409 | PatchSystemNotificationsEmailSettingsEndpointResponse415 | PatchSystemNotificationsEmailSettingsEndpointResponse422 | PatchSystemNotificationsEmailSettingsEndpointResponse424 | PatchSystemNotificationsEmailSettingsEndpointResponse500 | PatchSystemNotificationsEmailSettingsEndpointResponse503]
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
    body: PatchSystemNotificationsEmailSettingsEndpointJsonBody
    | PatchSystemNotificationsEmailSettingsEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchSystemNotificationsEmailSettingsEndpointResponse400
    | PatchSystemNotificationsEmailSettingsEndpointResponse401
    | PatchSystemNotificationsEmailSettingsEndpointResponse403
    | PatchSystemNotificationsEmailSettingsEndpointResponse404
    | PatchSystemNotificationsEmailSettingsEndpointResponse405
    | PatchSystemNotificationsEmailSettingsEndpointResponse406
    | PatchSystemNotificationsEmailSettingsEndpointResponse409
    | PatchSystemNotificationsEmailSettingsEndpointResponse415
    | PatchSystemNotificationsEmailSettingsEndpointResponse422
    | PatchSystemNotificationsEmailSettingsEndpointResponse424
    | PatchSystemNotificationsEmailSettingsEndpointResponse500
    | PatchSystemNotificationsEmailSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Email Notification Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: EmailNotificationSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-notifications-email-
    settings-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchSystemNotificationsEmailSettingsEndpointJsonBody | Unset):
        body (PatchSystemNotificationsEmailSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemNotificationsEmailSettingsEndpointResponse400 | PatchSystemNotificationsEmailSettingsEndpointResponse401 | PatchSystemNotificationsEmailSettingsEndpointResponse403 | PatchSystemNotificationsEmailSettingsEndpointResponse404 | PatchSystemNotificationsEmailSettingsEndpointResponse405 | PatchSystemNotificationsEmailSettingsEndpointResponse406 | PatchSystemNotificationsEmailSettingsEndpointResponse409 | PatchSystemNotificationsEmailSettingsEndpointResponse415 | PatchSystemNotificationsEmailSettingsEndpointResponse422 | PatchSystemNotificationsEmailSettingsEndpointResponse424 | PatchSystemNotificationsEmailSettingsEndpointResponse500 | PatchSystemNotificationsEmailSettingsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemNotificationsEmailSettingsEndpointJsonBody
    | PatchSystemNotificationsEmailSettingsEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchSystemNotificationsEmailSettingsEndpointResponse400
    | PatchSystemNotificationsEmailSettingsEndpointResponse401
    | PatchSystemNotificationsEmailSettingsEndpointResponse403
    | PatchSystemNotificationsEmailSettingsEndpointResponse404
    | PatchSystemNotificationsEmailSettingsEndpointResponse405
    | PatchSystemNotificationsEmailSettingsEndpointResponse406
    | PatchSystemNotificationsEmailSettingsEndpointResponse409
    | PatchSystemNotificationsEmailSettingsEndpointResponse415
    | PatchSystemNotificationsEmailSettingsEndpointResponse422
    | PatchSystemNotificationsEmailSettingsEndpointResponse424
    | PatchSystemNotificationsEmailSettingsEndpointResponse500
    | PatchSystemNotificationsEmailSettingsEndpointResponse503
]:
    """<h3>Description:</h3>Updates current Email Notification Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: EmailNotificationSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-notifications-email-
    settings-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchSystemNotificationsEmailSettingsEndpointJsonBody | Unset):
        body (PatchSystemNotificationsEmailSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemNotificationsEmailSettingsEndpointResponse400 | PatchSystemNotificationsEmailSettingsEndpointResponse401 | PatchSystemNotificationsEmailSettingsEndpointResponse403 | PatchSystemNotificationsEmailSettingsEndpointResponse404 | PatchSystemNotificationsEmailSettingsEndpointResponse405 | PatchSystemNotificationsEmailSettingsEndpointResponse406 | PatchSystemNotificationsEmailSettingsEndpointResponse409 | PatchSystemNotificationsEmailSettingsEndpointResponse415 | PatchSystemNotificationsEmailSettingsEndpointResponse422 | PatchSystemNotificationsEmailSettingsEndpointResponse424 | PatchSystemNotificationsEmailSettingsEndpointResponse500 | PatchSystemNotificationsEmailSettingsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemNotificationsEmailSettingsEndpointJsonBody
    | PatchSystemNotificationsEmailSettingsEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchSystemNotificationsEmailSettingsEndpointResponse400
    | PatchSystemNotificationsEmailSettingsEndpointResponse401
    | PatchSystemNotificationsEmailSettingsEndpointResponse403
    | PatchSystemNotificationsEmailSettingsEndpointResponse404
    | PatchSystemNotificationsEmailSettingsEndpointResponse405
    | PatchSystemNotificationsEmailSettingsEndpointResponse406
    | PatchSystemNotificationsEmailSettingsEndpointResponse409
    | PatchSystemNotificationsEmailSettingsEndpointResponse415
    | PatchSystemNotificationsEmailSettingsEndpointResponse422
    | PatchSystemNotificationsEmailSettingsEndpointResponse424
    | PatchSystemNotificationsEmailSettingsEndpointResponse500
    | PatchSystemNotificationsEmailSettingsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current Email Notification Settings.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: EmailNotificationSettings<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-notifications-email-
    settings-patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PatchSystemNotificationsEmailSettingsEndpointJsonBody | Unset):
        body (PatchSystemNotificationsEmailSettingsEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemNotificationsEmailSettingsEndpointResponse400 | PatchSystemNotificationsEmailSettingsEndpointResponse401 | PatchSystemNotificationsEmailSettingsEndpointResponse403 | PatchSystemNotificationsEmailSettingsEndpointResponse404 | PatchSystemNotificationsEmailSettingsEndpointResponse405 | PatchSystemNotificationsEmailSettingsEndpointResponse406 | PatchSystemNotificationsEmailSettingsEndpointResponse409 | PatchSystemNotificationsEmailSettingsEndpointResponse415 | PatchSystemNotificationsEmailSettingsEndpointResponse422 | PatchSystemNotificationsEmailSettingsEndpointResponse424 | PatchSystemNotificationsEmailSettingsEndpointResponse500 | PatchSystemNotificationsEmailSettingsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
