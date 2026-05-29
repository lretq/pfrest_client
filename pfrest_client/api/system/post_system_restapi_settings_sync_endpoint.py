from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_restapi_settings_sync_endpoint_data_body import PostSystemRESTAPISettingsSyncEndpointDataBody
from ...models.post_system_restapi_settings_sync_endpoint_json_body import PostSystemRESTAPISettingsSyncEndpointJsonBody
from ...models.post_system_restapi_settings_sync_endpoint_response_400 import (
    PostSystemRESTAPISettingsSyncEndpointResponse400,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_401 import (
    PostSystemRESTAPISettingsSyncEndpointResponse401,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_403 import (
    PostSystemRESTAPISettingsSyncEndpointResponse403,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_404 import (
    PostSystemRESTAPISettingsSyncEndpointResponse404,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_405 import (
    PostSystemRESTAPISettingsSyncEndpointResponse405,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_406 import (
    PostSystemRESTAPISettingsSyncEndpointResponse406,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_409 import (
    PostSystemRESTAPISettingsSyncEndpointResponse409,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_415 import (
    PostSystemRESTAPISettingsSyncEndpointResponse415,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_422 import (
    PostSystemRESTAPISettingsSyncEndpointResponse422,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_424 import (
    PostSystemRESTAPISettingsSyncEndpointResponse424,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_500 import (
    PostSystemRESTAPISettingsSyncEndpointResponse500,
)
from ...models.post_system_restapi_settings_sync_endpoint_response_503 import (
    PostSystemRESTAPISettingsSyncEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemRESTAPISettingsSyncEndpointJsonBody | PostSystemRESTAPISettingsSyncEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/restapi/settings/sync",
    }

    if isinstance(body, PostSystemRESTAPISettingsSyncEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemRESTAPISettingsSyncEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemRESTAPISettingsSyncEndpointResponse400
    | PostSystemRESTAPISettingsSyncEndpointResponse401
    | PostSystemRESTAPISettingsSyncEndpointResponse403
    | PostSystemRESTAPISettingsSyncEndpointResponse404
    | PostSystemRESTAPISettingsSyncEndpointResponse405
    | PostSystemRESTAPISettingsSyncEndpointResponse406
    | PostSystemRESTAPISettingsSyncEndpointResponse409
    | PostSystemRESTAPISettingsSyncEndpointResponse415
    | PostSystemRESTAPISettingsSyncEndpointResponse422
    | PostSystemRESTAPISettingsSyncEndpointResponse424
    | PostSystemRESTAPISettingsSyncEndpointResponse500
    | PostSystemRESTAPISettingsSyncEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemRESTAPISettingsSyncEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemRESTAPISettingsSyncEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemRESTAPISettingsSyncEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemRESTAPISettingsSyncEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemRESTAPISettingsSyncEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemRESTAPISettingsSyncEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemRESTAPISettingsSyncEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemRESTAPISettingsSyncEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemRESTAPISettingsSyncEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemRESTAPISettingsSyncEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemRESTAPISettingsSyncEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemRESTAPISettingsSyncEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemRESTAPISettingsSyncEndpointResponse400
    | PostSystemRESTAPISettingsSyncEndpointResponse401
    | PostSystemRESTAPISettingsSyncEndpointResponse403
    | PostSystemRESTAPISettingsSyncEndpointResponse404
    | PostSystemRESTAPISettingsSyncEndpointResponse405
    | PostSystemRESTAPISettingsSyncEndpointResponse406
    | PostSystemRESTAPISettingsSyncEndpointResponse409
    | PostSystemRESTAPISettingsSyncEndpointResponse415
    | PostSystemRESTAPISettingsSyncEndpointResponse422
    | PostSystemRESTAPISettingsSyncEndpointResponse424
    | PostSystemRESTAPISettingsSyncEndpointResponse500
    | PostSystemRESTAPISettingsSyncEndpointResponse503
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostSystemRESTAPISettingsSyncEndpointJsonBody | PostSystemRESTAPISettingsSyncEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemRESTAPISettingsSyncEndpointResponse400
    | PostSystemRESTAPISettingsSyncEndpointResponse401
    | PostSystemRESTAPISettingsSyncEndpointResponse403
    | PostSystemRESTAPISettingsSyncEndpointResponse404
    | PostSystemRESTAPISettingsSyncEndpointResponse405
    | PostSystemRESTAPISettingsSyncEndpointResponse406
    | PostSystemRESTAPISettingsSyncEndpointResponse409
    | PostSystemRESTAPISettingsSyncEndpointResponse415
    | PostSystemRESTAPISettingsSyncEndpointResponse422
    | PostSystemRESTAPISettingsSyncEndpointResponse424
    | PostSystemRESTAPISettingsSyncEndpointResponse500
    | PostSystemRESTAPISettingsSyncEndpointResponse503
]:
    """<h3>Description:</h3>Creates REST API Settings Sync.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPISettingsSync<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-restapi-settings-sync-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemRESTAPISettingsSyncEndpointJsonBody | Unset):
        body (PostSystemRESTAPISettingsSyncEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemRESTAPISettingsSyncEndpointResponse400 | PostSystemRESTAPISettingsSyncEndpointResponse401 | PostSystemRESTAPISettingsSyncEndpointResponse403 | PostSystemRESTAPISettingsSyncEndpointResponse404 | PostSystemRESTAPISettingsSyncEndpointResponse405 | PostSystemRESTAPISettingsSyncEndpointResponse406 | PostSystemRESTAPISettingsSyncEndpointResponse409 | PostSystemRESTAPISettingsSyncEndpointResponse415 | PostSystemRESTAPISettingsSyncEndpointResponse422 | PostSystemRESTAPISettingsSyncEndpointResponse424 | PostSystemRESTAPISettingsSyncEndpointResponse500 | PostSystemRESTAPISettingsSyncEndpointResponse503]
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
    client: AuthenticatedClient,
    body: PostSystemRESTAPISettingsSyncEndpointJsonBody | PostSystemRESTAPISettingsSyncEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemRESTAPISettingsSyncEndpointResponse400
    | PostSystemRESTAPISettingsSyncEndpointResponse401
    | PostSystemRESTAPISettingsSyncEndpointResponse403
    | PostSystemRESTAPISettingsSyncEndpointResponse404
    | PostSystemRESTAPISettingsSyncEndpointResponse405
    | PostSystemRESTAPISettingsSyncEndpointResponse406
    | PostSystemRESTAPISettingsSyncEndpointResponse409
    | PostSystemRESTAPISettingsSyncEndpointResponse415
    | PostSystemRESTAPISettingsSyncEndpointResponse422
    | PostSystemRESTAPISettingsSyncEndpointResponse424
    | PostSystemRESTAPISettingsSyncEndpointResponse500
    | PostSystemRESTAPISettingsSyncEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates REST API Settings Sync.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPISettingsSync<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-restapi-settings-sync-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemRESTAPISettingsSyncEndpointJsonBody | Unset):
        body (PostSystemRESTAPISettingsSyncEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemRESTAPISettingsSyncEndpointResponse400 | PostSystemRESTAPISettingsSyncEndpointResponse401 | PostSystemRESTAPISettingsSyncEndpointResponse403 | PostSystemRESTAPISettingsSyncEndpointResponse404 | PostSystemRESTAPISettingsSyncEndpointResponse405 | PostSystemRESTAPISettingsSyncEndpointResponse406 | PostSystemRESTAPISettingsSyncEndpointResponse409 | PostSystemRESTAPISettingsSyncEndpointResponse415 | PostSystemRESTAPISettingsSyncEndpointResponse422 | PostSystemRESTAPISettingsSyncEndpointResponse424 | PostSystemRESTAPISettingsSyncEndpointResponse500 | PostSystemRESTAPISettingsSyncEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostSystemRESTAPISettingsSyncEndpointJsonBody | PostSystemRESTAPISettingsSyncEndpointDataBody | Unset = UNSET,
) -> Response[
    PostSystemRESTAPISettingsSyncEndpointResponse400
    | PostSystemRESTAPISettingsSyncEndpointResponse401
    | PostSystemRESTAPISettingsSyncEndpointResponse403
    | PostSystemRESTAPISettingsSyncEndpointResponse404
    | PostSystemRESTAPISettingsSyncEndpointResponse405
    | PostSystemRESTAPISettingsSyncEndpointResponse406
    | PostSystemRESTAPISettingsSyncEndpointResponse409
    | PostSystemRESTAPISettingsSyncEndpointResponse415
    | PostSystemRESTAPISettingsSyncEndpointResponse422
    | PostSystemRESTAPISettingsSyncEndpointResponse424
    | PostSystemRESTAPISettingsSyncEndpointResponse500
    | PostSystemRESTAPISettingsSyncEndpointResponse503
]:
    """<h3>Description:</h3>Creates REST API Settings Sync.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPISettingsSync<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-restapi-settings-sync-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemRESTAPISettingsSyncEndpointJsonBody | Unset):
        body (PostSystemRESTAPISettingsSyncEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemRESTAPISettingsSyncEndpointResponse400 | PostSystemRESTAPISettingsSyncEndpointResponse401 | PostSystemRESTAPISettingsSyncEndpointResponse403 | PostSystemRESTAPISettingsSyncEndpointResponse404 | PostSystemRESTAPISettingsSyncEndpointResponse405 | PostSystemRESTAPISettingsSyncEndpointResponse406 | PostSystemRESTAPISettingsSyncEndpointResponse409 | PostSystemRESTAPISettingsSyncEndpointResponse415 | PostSystemRESTAPISettingsSyncEndpointResponse422 | PostSystemRESTAPISettingsSyncEndpointResponse424 | PostSystemRESTAPISettingsSyncEndpointResponse500 | PostSystemRESTAPISettingsSyncEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostSystemRESTAPISettingsSyncEndpointJsonBody | PostSystemRESTAPISettingsSyncEndpointDataBody | Unset = UNSET,
) -> (
    PostSystemRESTAPISettingsSyncEndpointResponse400
    | PostSystemRESTAPISettingsSyncEndpointResponse401
    | PostSystemRESTAPISettingsSyncEndpointResponse403
    | PostSystemRESTAPISettingsSyncEndpointResponse404
    | PostSystemRESTAPISettingsSyncEndpointResponse405
    | PostSystemRESTAPISettingsSyncEndpointResponse406
    | PostSystemRESTAPISettingsSyncEndpointResponse409
    | PostSystemRESTAPISettingsSyncEndpointResponse415
    | PostSystemRESTAPISettingsSyncEndpointResponse422
    | PostSystemRESTAPISettingsSyncEndpointResponse424
    | PostSystemRESTAPISettingsSyncEndpointResponse500
    | PostSystemRESTAPISettingsSyncEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates REST API Settings Sync.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPISettingsSync<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-restapi-settings-sync-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostSystemRESTAPISettingsSyncEndpointJsonBody | Unset):
        body (PostSystemRESTAPISettingsSyncEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemRESTAPISettingsSyncEndpointResponse400 | PostSystemRESTAPISettingsSyncEndpointResponse401 | PostSystemRESTAPISettingsSyncEndpointResponse403 | PostSystemRESTAPISettingsSyncEndpointResponse404 | PostSystemRESTAPISettingsSyncEndpointResponse405 | PostSystemRESTAPISettingsSyncEndpointResponse406 | PostSystemRESTAPISettingsSyncEndpointResponse409 | PostSystemRESTAPISettingsSyncEndpointResponse415 | PostSystemRESTAPISettingsSyncEndpointResponse422 | PostSystemRESTAPISettingsSyncEndpointResponse424 | PostSystemRESTAPISettingsSyncEndpointResponse500 | PostSystemRESTAPISettingsSyncEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
