from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_bind_sync_remote_hosts_endpoint_query import GetServicesBINDSyncRemoteHostsEndpointQuery
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_400 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse400,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_401 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse401,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_403 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse403,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_404 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse404,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_405 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse405,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_406 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse406,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_409 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse409,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_415 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse415,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_422 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse422,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_424 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse424,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_500 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse500,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_response_503 import (
    GetServicesBINDSyncRemoteHostsEndpointResponse503,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_sort_flags import (
    GetServicesBINDSyncRemoteHostsEndpointSortFlags,
)
from ...models.get_services_bind_sync_remote_hosts_endpoint_sort_order import (
    GetServicesBINDSyncRemoteHostsEndpointSortOrder,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset = UNSET,
    query: GetServicesBINDSyncRemoteHostsEndpointQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_sort_by: list[str] | None | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    elif isinstance(sort_by, list):
        json_sort_by = sort_by

    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    json_sort_flags: str | Unset = UNSET
    if not isinstance(sort_flags, Unset):
        json_sort_flags = sort_flags.value

    params["sort_flags"] = json_sort_flags

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/bind/sync/remote_hosts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesBINDSyncRemoteHostsEndpointResponse400
    | GetServicesBINDSyncRemoteHostsEndpointResponse401
    | GetServicesBINDSyncRemoteHostsEndpointResponse403
    | GetServicesBINDSyncRemoteHostsEndpointResponse404
    | GetServicesBINDSyncRemoteHostsEndpointResponse405
    | GetServicesBINDSyncRemoteHostsEndpointResponse406
    | GetServicesBINDSyncRemoteHostsEndpointResponse409
    | GetServicesBINDSyncRemoteHostsEndpointResponse415
    | GetServicesBINDSyncRemoteHostsEndpointResponse422
    | GetServicesBINDSyncRemoteHostsEndpointResponse424
    | GetServicesBINDSyncRemoteHostsEndpointResponse500
    | GetServicesBINDSyncRemoteHostsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesBINDSyncRemoteHostsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesBINDSyncRemoteHostsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesBINDSyncRemoteHostsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesBINDSyncRemoteHostsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesBINDSyncRemoteHostsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesBINDSyncRemoteHostsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesBINDSyncRemoteHostsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesBINDSyncRemoteHostsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesBINDSyncRemoteHostsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesBINDSyncRemoteHostsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesBINDSyncRemoteHostsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesBINDSyncRemoteHostsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesBINDSyncRemoteHostsEndpointResponse400
    | GetServicesBINDSyncRemoteHostsEndpointResponse401
    | GetServicesBINDSyncRemoteHostsEndpointResponse403
    | GetServicesBINDSyncRemoteHostsEndpointResponse404
    | GetServicesBINDSyncRemoteHostsEndpointResponse405
    | GetServicesBINDSyncRemoteHostsEndpointResponse406
    | GetServicesBINDSyncRemoteHostsEndpointResponse409
    | GetServicesBINDSyncRemoteHostsEndpointResponse415
    | GetServicesBINDSyncRemoteHostsEndpointResponse422
    | GetServicesBINDSyncRemoteHostsEndpointResponse424
    | GetServicesBINDSyncRemoteHostsEndpointResponse500
    | GetServicesBINDSyncRemoteHostsEndpointResponse503
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
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset = UNSET,
    query: GetServicesBINDSyncRemoteHostsEndpointQuery | Unset = UNSET,
) -> Response[
    GetServicesBINDSyncRemoteHostsEndpointResponse400
    | GetServicesBINDSyncRemoteHostsEndpointResponse401
    | GetServicesBINDSyncRemoteHostsEndpointResponse403
    | GetServicesBINDSyncRemoteHostsEndpointResponse404
    | GetServicesBINDSyncRemoteHostsEndpointResponse405
    | GetServicesBINDSyncRemoteHostsEndpointResponse406
    | GetServicesBINDSyncRemoteHostsEndpointResponse409
    | GetServicesBINDSyncRemoteHostsEndpointResponse415
    | GetServicesBINDSyncRemoteHostsEndpointResponse422
    | GetServicesBINDSyncRemoteHostsEndpointResponse424
    | GetServicesBINDSyncRemoteHostsEndpointResponse500
    | GetServicesBINDSyncRemoteHostsEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing BIND Sync Remote Hosts.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-hosts-get ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset):
        sort_flags (GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset):
        query (GetServicesBINDSyncRemoteHostsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesBINDSyncRemoteHostsEndpointResponse400 | GetServicesBINDSyncRemoteHostsEndpointResponse401 | GetServicesBINDSyncRemoteHostsEndpointResponse403 | GetServicesBINDSyncRemoteHostsEndpointResponse404 | GetServicesBINDSyncRemoteHostsEndpointResponse405 | GetServicesBINDSyncRemoteHostsEndpointResponse406 | GetServicesBINDSyncRemoteHostsEndpointResponse409 | GetServicesBINDSyncRemoteHostsEndpointResponse415 | GetServicesBINDSyncRemoteHostsEndpointResponse422 | GetServicesBINDSyncRemoteHostsEndpointResponse424 | GetServicesBINDSyncRemoteHostsEndpointResponse500 | GetServicesBINDSyncRemoteHostsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset = UNSET,
    query: GetServicesBINDSyncRemoteHostsEndpointQuery | Unset = UNSET,
) -> (
    GetServicesBINDSyncRemoteHostsEndpointResponse400
    | GetServicesBINDSyncRemoteHostsEndpointResponse401
    | GetServicesBINDSyncRemoteHostsEndpointResponse403
    | GetServicesBINDSyncRemoteHostsEndpointResponse404
    | GetServicesBINDSyncRemoteHostsEndpointResponse405
    | GetServicesBINDSyncRemoteHostsEndpointResponse406
    | GetServicesBINDSyncRemoteHostsEndpointResponse409
    | GetServicesBINDSyncRemoteHostsEndpointResponse415
    | GetServicesBINDSyncRemoteHostsEndpointResponse422
    | GetServicesBINDSyncRemoteHostsEndpointResponse424
    | GetServicesBINDSyncRemoteHostsEndpointResponse500
    | GetServicesBINDSyncRemoteHostsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing BIND Sync Remote Hosts.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-hosts-get ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset):
        sort_flags (GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset):
        query (GetServicesBINDSyncRemoteHostsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesBINDSyncRemoteHostsEndpointResponse400 | GetServicesBINDSyncRemoteHostsEndpointResponse401 | GetServicesBINDSyncRemoteHostsEndpointResponse403 | GetServicesBINDSyncRemoteHostsEndpointResponse404 | GetServicesBINDSyncRemoteHostsEndpointResponse405 | GetServicesBINDSyncRemoteHostsEndpointResponse406 | GetServicesBINDSyncRemoteHostsEndpointResponse409 | GetServicesBINDSyncRemoteHostsEndpointResponse415 | GetServicesBINDSyncRemoteHostsEndpointResponse422 | GetServicesBINDSyncRemoteHostsEndpointResponse424 | GetServicesBINDSyncRemoteHostsEndpointResponse500 | GetServicesBINDSyncRemoteHostsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset = UNSET,
    query: GetServicesBINDSyncRemoteHostsEndpointQuery | Unset = UNSET,
) -> Response[
    GetServicesBINDSyncRemoteHostsEndpointResponse400
    | GetServicesBINDSyncRemoteHostsEndpointResponse401
    | GetServicesBINDSyncRemoteHostsEndpointResponse403
    | GetServicesBINDSyncRemoteHostsEndpointResponse404
    | GetServicesBINDSyncRemoteHostsEndpointResponse405
    | GetServicesBINDSyncRemoteHostsEndpointResponse406
    | GetServicesBINDSyncRemoteHostsEndpointResponse409
    | GetServicesBINDSyncRemoteHostsEndpointResponse415
    | GetServicesBINDSyncRemoteHostsEndpointResponse422
    | GetServicesBINDSyncRemoteHostsEndpointResponse424
    | GetServicesBINDSyncRemoteHostsEndpointResponse500
    | GetServicesBINDSyncRemoteHostsEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing BIND Sync Remote Hosts.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-hosts-get ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset):
        sort_flags (GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset):
        query (GetServicesBINDSyncRemoteHostsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesBINDSyncRemoteHostsEndpointResponse400 | GetServicesBINDSyncRemoteHostsEndpointResponse401 | GetServicesBINDSyncRemoteHostsEndpointResponse403 | GetServicesBINDSyncRemoteHostsEndpointResponse404 | GetServicesBINDSyncRemoteHostsEndpointResponse405 | GetServicesBINDSyncRemoteHostsEndpointResponse406 | GetServicesBINDSyncRemoteHostsEndpointResponse409 | GetServicesBINDSyncRemoteHostsEndpointResponse415 | GetServicesBINDSyncRemoteHostsEndpointResponse422 | GetServicesBINDSyncRemoteHostsEndpointResponse424 | GetServicesBINDSyncRemoteHostsEndpointResponse500 | GetServicesBINDSyncRemoteHostsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset = UNSET,
    query: GetServicesBINDSyncRemoteHostsEndpointQuery | Unset = UNSET,
) -> (
    GetServicesBINDSyncRemoteHostsEndpointResponse400
    | GetServicesBINDSyncRemoteHostsEndpointResponse401
    | GetServicesBINDSyncRemoteHostsEndpointResponse403
    | GetServicesBINDSyncRemoteHostsEndpointResponse404
    | GetServicesBINDSyncRemoteHostsEndpointResponse405
    | GetServicesBINDSyncRemoteHostsEndpointResponse406
    | GetServicesBINDSyncRemoteHostsEndpointResponse409
    | GetServicesBINDSyncRemoteHostsEndpointResponse415
    | GetServicesBINDSyncRemoteHostsEndpointResponse422
    | GetServicesBINDSyncRemoteHostsEndpointResponse424
    | GetServicesBINDSyncRemoteHostsEndpointResponse500
    | GetServicesBINDSyncRemoteHostsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing BIND Sync Remote Hosts.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: BINDSyncRemoteHost<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-sync-remote-hosts-get ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesBINDSyncRemoteHostsEndpointSortOrder | Unset):
        sort_flags (GetServicesBINDSyncRemoteHostsEndpointSortFlags | Unset):
        query (GetServicesBINDSyncRemoteHostsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesBINDSyncRemoteHostsEndpointResponse400 | GetServicesBINDSyncRemoteHostsEndpointResponse401 | GetServicesBINDSyncRemoteHostsEndpointResponse403 | GetServicesBINDSyncRemoteHostsEndpointResponse404 | GetServicesBINDSyncRemoteHostsEndpointResponse405 | GetServicesBINDSyncRemoteHostsEndpointResponse406 | GetServicesBINDSyncRemoteHostsEndpointResponse409 | GetServicesBINDSyncRemoteHostsEndpointResponse415 | GetServicesBINDSyncRemoteHostsEndpointResponse422 | GetServicesBINDSyncRemoteHostsEndpointResponse424 | GetServicesBINDSyncRemoteHostsEndpointResponse500 | GetServicesBINDSyncRemoteHostsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            sort_flags=sort_flags,
            query=query,
        )
    ).parsed
