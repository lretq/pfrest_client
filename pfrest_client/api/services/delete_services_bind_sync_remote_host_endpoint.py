from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_bind_sync_remote_host_endpoint_response_400 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse400,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_401 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse401,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_403 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse403,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_404 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse404,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_405 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse405,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_406 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse406,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_409 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse409,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_415 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse415,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_422 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse422,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_424 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse424,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_500 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse500,
)
from ...models.delete_services_bind_sync_remote_host_endpoint_response_503 import (
    DeleteServicesBINDSyncRemoteHostEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/bind/sync/remote_host",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesBINDSyncRemoteHostEndpointResponse400
    | DeleteServicesBINDSyncRemoteHostEndpointResponse401
    | DeleteServicesBINDSyncRemoteHostEndpointResponse403
    | DeleteServicesBINDSyncRemoteHostEndpointResponse404
    | DeleteServicesBINDSyncRemoteHostEndpointResponse405
    | DeleteServicesBINDSyncRemoteHostEndpointResponse406
    | DeleteServicesBINDSyncRemoteHostEndpointResponse409
    | DeleteServicesBINDSyncRemoteHostEndpointResponse415
    | DeleteServicesBINDSyncRemoteHostEndpointResponse422
    | DeleteServicesBINDSyncRemoteHostEndpointResponse424
    | DeleteServicesBINDSyncRemoteHostEndpointResponse500
    | DeleteServicesBINDSyncRemoteHostEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesBINDSyncRemoteHostEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesBINDSyncRemoteHostEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesBINDSyncRemoteHostEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesBINDSyncRemoteHostEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesBINDSyncRemoteHostEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesBINDSyncRemoteHostEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesBINDSyncRemoteHostEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesBINDSyncRemoteHostEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesBINDSyncRemoteHostEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesBINDSyncRemoteHostEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesBINDSyncRemoteHostEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesBINDSyncRemoteHostEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesBINDSyncRemoteHostEndpointResponse400
    | DeleteServicesBINDSyncRemoteHostEndpointResponse401
    | DeleteServicesBINDSyncRemoteHostEndpointResponse403
    | DeleteServicesBINDSyncRemoteHostEndpointResponse404
    | DeleteServicesBINDSyncRemoteHostEndpointResponse405
    | DeleteServicesBINDSyncRemoteHostEndpointResponse406
    | DeleteServicesBINDSyncRemoteHostEndpointResponse409
    | DeleteServicesBINDSyncRemoteHostEndpointResponse415
    | DeleteServicesBINDSyncRemoteHostEndpointResponse422
    | DeleteServicesBINDSyncRemoteHostEndpointResponse424
    | DeleteServicesBINDSyncRemoteHostEndpointResponse500
    | DeleteServicesBINDSyncRemoteHostEndpointResponse503
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
    id: int | str,
) -> Response[
    DeleteServicesBINDSyncRemoteHostEndpointResponse400
    | DeleteServicesBINDSyncRemoteHostEndpointResponse401
    | DeleteServicesBINDSyncRemoteHostEndpointResponse403
    | DeleteServicesBINDSyncRemoteHostEndpointResponse404
    | DeleteServicesBINDSyncRemoteHostEndpointResponse405
    | DeleteServicesBINDSyncRemoteHostEndpointResponse406
    | DeleteServicesBINDSyncRemoteHostEndpointResponse409
    | DeleteServicesBINDSyncRemoteHostEndpointResponse415
    | DeleteServicesBINDSyncRemoteHostEndpointResponse422
    | DeleteServicesBINDSyncRemoteHostEndpointResponse424
    | DeleteServicesBINDSyncRemoteHostEndpointResponse500
    | DeleteServicesBINDSyncRemoteHostEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing BIND Sync Remote Host.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-host-delete
    ]<br>**Required packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes
    cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesBINDSyncRemoteHostEndpointResponse400 | DeleteServicesBINDSyncRemoteHostEndpointResponse401 | DeleteServicesBINDSyncRemoteHostEndpointResponse403 | DeleteServicesBINDSyncRemoteHostEndpointResponse404 | DeleteServicesBINDSyncRemoteHostEndpointResponse405 | DeleteServicesBINDSyncRemoteHostEndpointResponse406 | DeleteServicesBINDSyncRemoteHostEndpointResponse409 | DeleteServicesBINDSyncRemoteHostEndpointResponse415 | DeleteServicesBINDSyncRemoteHostEndpointResponse422 | DeleteServicesBINDSyncRemoteHostEndpointResponse424 | DeleteServicesBINDSyncRemoteHostEndpointResponse500 | DeleteServicesBINDSyncRemoteHostEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesBINDSyncRemoteHostEndpointResponse400
    | DeleteServicesBINDSyncRemoteHostEndpointResponse401
    | DeleteServicesBINDSyncRemoteHostEndpointResponse403
    | DeleteServicesBINDSyncRemoteHostEndpointResponse404
    | DeleteServicesBINDSyncRemoteHostEndpointResponse405
    | DeleteServicesBINDSyncRemoteHostEndpointResponse406
    | DeleteServicesBINDSyncRemoteHostEndpointResponse409
    | DeleteServicesBINDSyncRemoteHostEndpointResponse415
    | DeleteServicesBINDSyncRemoteHostEndpointResponse422
    | DeleteServicesBINDSyncRemoteHostEndpointResponse424
    | DeleteServicesBINDSyncRemoteHostEndpointResponse500
    | DeleteServicesBINDSyncRemoteHostEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing BIND Sync Remote Host.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-host-delete
    ]<br>**Required packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes
    cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesBINDSyncRemoteHostEndpointResponse400 | DeleteServicesBINDSyncRemoteHostEndpointResponse401 | DeleteServicesBINDSyncRemoteHostEndpointResponse403 | DeleteServicesBINDSyncRemoteHostEndpointResponse404 | DeleteServicesBINDSyncRemoteHostEndpointResponse405 | DeleteServicesBINDSyncRemoteHostEndpointResponse406 | DeleteServicesBINDSyncRemoteHostEndpointResponse409 | DeleteServicesBINDSyncRemoteHostEndpointResponse415 | DeleteServicesBINDSyncRemoteHostEndpointResponse422 | DeleteServicesBINDSyncRemoteHostEndpointResponse424 | DeleteServicesBINDSyncRemoteHostEndpointResponse500 | DeleteServicesBINDSyncRemoteHostEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    DeleteServicesBINDSyncRemoteHostEndpointResponse400
    | DeleteServicesBINDSyncRemoteHostEndpointResponse401
    | DeleteServicesBINDSyncRemoteHostEndpointResponse403
    | DeleteServicesBINDSyncRemoteHostEndpointResponse404
    | DeleteServicesBINDSyncRemoteHostEndpointResponse405
    | DeleteServicesBINDSyncRemoteHostEndpointResponse406
    | DeleteServicesBINDSyncRemoteHostEndpointResponse409
    | DeleteServicesBINDSyncRemoteHostEndpointResponse415
    | DeleteServicesBINDSyncRemoteHostEndpointResponse422
    | DeleteServicesBINDSyncRemoteHostEndpointResponse424
    | DeleteServicesBINDSyncRemoteHostEndpointResponse500
    | DeleteServicesBINDSyncRemoteHostEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing BIND Sync Remote Host.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-host-delete
    ]<br>**Required packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes
    cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesBINDSyncRemoteHostEndpointResponse400 | DeleteServicesBINDSyncRemoteHostEndpointResponse401 | DeleteServicesBINDSyncRemoteHostEndpointResponse403 | DeleteServicesBINDSyncRemoteHostEndpointResponse404 | DeleteServicesBINDSyncRemoteHostEndpointResponse405 | DeleteServicesBINDSyncRemoteHostEndpointResponse406 | DeleteServicesBINDSyncRemoteHostEndpointResponse409 | DeleteServicesBINDSyncRemoteHostEndpointResponse415 | DeleteServicesBINDSyncRemoteHostEndpointResponse422 | DeleteServicesBINDSyncRemoteHostEndpointResponse424 | DeleteServicesBINDSyncRemoteHostEndpointResponse500 | DeleteServicesBINDSyncRemoteHostEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesBINDSyncRemoteHostEndpointResponse400
    | DeleteServicesBINDSyncRemoteHostEndpointResponse401
    | DeleteServicesBINDSyncRemoteHostEndpointResponse403
    | DeleteServicesBINDSyncRemoteHostEndpointResponse404
    | DeleteServicesBINDSyncRemoteHostEndpointResponse405
    | DeleteServicesBINDSyncRemoteHostEndpointResponse406
    | DeleteServicesBINDSyncRemoteHostEndpointResponse409
    | DeleteServicesBINDSyncRemoteHostEndpointResponse415
    | DeleteServicesBINDSyncRemoteHostEndpointResponse422
    | DeleteServicesBINDSyncRemoteHostEndpointResponse424
    | DeleteServicesBINDSyncRemoteHostEndpointResponse500
    | DeleteServicesBINDSyncRemoteHostEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing BIND Sync Remote Host.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-host-delete
    ]<br>**Required packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes
    cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesBINDSyncRemoteHostEndpointResponse400 | DeleteServicesBINDSyncRemoteHostEndpointResponse401 | DeleteServicesBINDSyncRemoteHostEndpointResponse403 | DeleteServicesBINDSyncRemoteHostEndpointResponse404 | DeleteServicesBINDSyncRemoteHostEndpointResponse405 | DeleteServicesBINDSyncRemoteHostEndpointResponse406 | DeleteServicesBINDSyncRemoteHostEndpointResponse409 | DeleteServicesBINDSyncRemoteHostEndpointResponse415 | DeleteServicesBINDSyncRemoteHostEndpointResponse422 | DeleteServicesBINDSyncRemoteHostEndpointResponse424 | DeleteServicesBINDSyncRemoteHostEndpointResponse500 | DeleteServicesBINDSyncRemoteHostEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
