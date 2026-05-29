from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_service_watchdogs_endpoint_query import GetServicesServiceWatchdogsEndpointQuery
from ...models.get_services_service_watchdogs_endpoint_response_400 import (
    GetServicesServiceWatchdogsEndpointResponse400,
)
from ...models.get_services_service_watchdogs_endpoint_response_401 import (
    GetServicesServiceWatchdogsEndpointResponse401,
)
from ...models.get_services_service_watchdogs_endpoint_response_403 import (
    GetServicesServiceWatchdogsEndpointResponse403,
)
from ...models.get_services_service_watchdogs_endpoint_response_404 import (
    GetServicesServiceWatchdogsEndpointResponse404,
)
from ...models.get_services_service_watchdogs_endpoint_response_405 import (
    GetServicesServiceWatchdogsEndpointResponse405,
)
from ...models.get_services_service_watchdogs_endpoint_response_406 import (
    GetServicesServiceWatchdogsEndpointResponse406,
)
from ...models.get_services_service_watchdogs_endpoint_response_409 import (
    GetServicesServiceWatchdogsEndpointResponse409,
)
from ...models.get_services_service_watchdogs_endpoint_response_415 import (
    GetServicesServiceWatchdogsEndpointResponse415,
)
from ...models.get_services_service_watchdogs_endpoint_response_422 import (
    GetServicesServiceWatchdogsEndpointResponse422,
)
from ...models.get_services_service_watchdogs_endpoint_response_424 import (
    GetServicesServiceWatchdogsEndpointResponse424,
)
from ...models.get_services_service_watchdogs_endpoint_response_500 import (
    GetServicesServiceWatchdogsEndpointResponse500,
)
from ...models.get_services_service_watchdogs_endpoint_response_503 import (
    GetServicesServiceWatchdogsEndpointResponse503,
)
from ...models.get_services_service_watchdogs_endpoint_sort_flags import GetServicesServiceWatchdogsEndpointSortFlags
from ...models.get_services_service_watchdogs_endpoint_sort_order import GetServicesServiceWatchdogsEndpointSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetServicesServiceWatchdogsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesServiceWatchdogsEndpointSortFlags | Unset = UNSET,
    query: GetServicesServiceWatchdogsEndpointQuery | Unset = UNSET,
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
        "url": "/api/v2/services/service_watchdogs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesServiceWatchdogsEndpointResponse400
    | GetServicesServiceWatchdogsEndpointResponse401
    | GetServicesServiceWatchdogsEndpointResponse403
    | GetServicesServiceWatchdogsEndpointResponse404
    | GetServicesServiceWatchdogsEndpointResponse405
    | GetServicesServiceWatchdogsEndpointResponse406
    | GetServicesServiceWatchdogsEndpointResponse409
    | GetServicesServiceWatchdogsEndpointResponse415
    | GetServicesServiceWatchdogsEndpointResponse422
    | GetServicesServiceWatchdogsEndpointResponse424
    | GetServicesServiceWatchdogsEndpointResponse500
    | GetServicesServiceWatchdogsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesServiceWatchdogsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesServiceWatchdogsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesServiceWatchdogsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesServiceWatchdogsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesServiceWatchdogsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesServiceWatchdogsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesServiceWatchdogsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesServiceWatchdogsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesServiceWatchdogsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesServiceWatchdogsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesServiceWatchdogsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesServiceWatchdogsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesServiceWatchdogsEndpointResponse400
    | GetServicesServiceWatchdogsEndpointResponse401
    | GetServicesServiceWatchdogsEndpointResponse403
    | GetServicesServiceWatchdogsEndpointResponse404
    | GetServicesServiceWatchdogsEndpointResponse405
    | GetServicesServiceWatchdogsEndpointResponse406
    | GetServicesServiceWatchdogsEndpointResponse409
    | GetServicesServiceWatchdogsEndpointResponse415
    | GetServicesServiceWatchdogsEndpointResponse422
    | GetServicesServiceWatchdogsEndpointResponse424
    | GetServicesServiceWatchdogsEndpointResponse500
    | GetServicesServiceWatchdogsEndpointResponse503
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
    sort_order: GetServicesServiceWatchdogsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesServiceWatchdogsEndpointSortFlags | Unset = UNSET,
    query: GetServicesServiceWatchdogsEndpointQuery | Unset = UNSET,
) -> Response[
    GetServicesServiceWatchdogsEndpointResponse400
    | GetServicesServiceWatchdogsEndpointResponse401
    | GetServicesServiceWatchdogsEndpointResponse403
    | GetServicesServiceWatchdogsEndpointResponse404
    | GetServicesServiceWatchdogsEndpointResponse405
    | GetServicesServiceWatchdogsEndpointResponse406
    | GetServicesServiceWatchdogsEndpointResponse409
    | GetServicesServiceWatchdogsEndpointResponse415
    | GetServicesServiceWatchdogsEndpointResponse422
    | GetServicesServiceWatchdogsEndpointResponse424
    | GetServicesServiceWatchdogsEndpointResponse500
    | GetServicesServiceWatchdogsEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing Service Watchdogs.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdogs-get ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesServiceWatchdogsEndpointSortOrder | Unset):
        sort_flags (GetServicesServiceWatchdogsEndpointSortFlags | Unset):
        query (GetServicesServiceWatchdogsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesServiceWatchdogsEndpointResponse400 | GetServicesServiceWatchdogsEndpointResponse401 | GetServicesServiceWatchdogsEndpointResponse403 | GetServicesServiceWatchdogsEndpointResponse404 | GetServicesServiceWatchdogsEndpointResponse405 | GetServicesServiceWatchdogsEndpointResponse406 | GetServicesServiceWatchdogsEndpointResponse409 | GetServicesServiceWatchdogsEndpointResponse415 | GetServicesServiceWatchdogsEndpointResponse422 | GetServicesServiceWatchdogsEndpointResponse424 | GetServicesServiceWatchdogsEndpointResponse500 | GetServicesServiceWatchdogsEndpointResponse503]
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
    sort_order: GetServicesServiceWatchdogsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesServiceWatchdogsEndpointSortFlags | Unset = UNSET,
    query: GetServicesServiceWatchdogsEndpointQuery | Unset = UNSET,
) -> (
    GetServicesServiceWatchdogsEndpointResponse400
    | GetServicesServiceWatchdogsEndpointResponse401
    | GetServicesServiceWatchdogsEndpointResponse403
    | GetServicesServiceWatchdogsEndpointResponse404
    | GetServicesServiceWatchdogsEndpointResponse405
    | GetServicesServiceWatchdogsEndpointResponse406
    | GetServicesServiceWatchdogsEndpointResponse409
    | GetServicesServiceWatchdogsEndpointResponse415
    | GetServicesServiceWatchdogsEndpointResponse422
    | GetServicesServiceWatchdogsEndpointResponse424
    | GetServicesServiceWatchdogsEndpointResponse500
    | GetServicesServiceWatchdogsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing Service Watchdogs.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdogs-get ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesServiceWatchdogsEndpointSortOrder | Unset):
        sort_flags (GetServicesServiceWatchdogsEndpointSortFlags | Unset):
        query (GetServicesServiceWatchdogsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesServiceWatchdogsEndpointResponse400 | GetServicesServiceWatchdogsEndpointResponse401 | GetServicesServiceWatchdogsEndpointResponse403 | GetServicesServiceWatchdogsEndpointResponse404 | GetServicesServiceWatchdogsEndpointResponse405 | GetServicesServiceWatchdogsEndpointResponse406 | GetServicesServiceWatchdogsEndpointResponse409 | GetServicesServiceWatchdogsEndpointResponse415 | GetServicesServiceWatchdogsEndpointResponse422 | GetServicesServiceWatchdogsEndpointResponse424 | GetServicesServiceWatchdogsEndpointResponse500 | GetServicesServiceWatchdogsEndpointResponse503
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
    sort_order: GetServicesServiceWatchdogsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesServiceWatchdogsEndpointSortFlags | Unset = UNSET,
    query: GetServicesServiceWatchdogsEndpointQuery | Unset = UNSET,
) -> Response[
    GetServicesServiceWatchdogsEndpointResponse400
    | GetServicesServiceWatchdogsEndpointResponse401
    | GetServicesServiceWatchdogsEndpointResponse403
    | GetServicesServiceWatchdogsEndpointResponse404
    | GetServicesServiceWatchdogsEndpointResponse405
    | GetServicesServiceWatchdogsEndpointResponse406
    | GetServicesServiceWatchdogsEndpointResponse409
    | GetServicesServiceWatchdogsEndpointResponse415
    | GetServicesServiceWatchdogsEndpointResponse422
    | GetServicesServiceWatchdogsEndpointResponse424
    | GetServicesServiceWatchdogsEndpointResponse500
    | GetServicesServiceWatchdogsEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing Service Watchdogs.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdogs-get ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesServiceWatchdogsEndpointSortOrder | Unset):
        sort_flags (GetServicesServiceWatchdogsEndpointSortFlags | Unset):
        query (GetServicesServiceWatchdogsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesServiceWatchdogsEndpointResponse400 | GetServicesServiceWatchdogsEndpointResponse401 | GetServicesServiceWatchdogsEndpointResponse403 | GetServicesServiceWatchdogsEndpointResponse404 | GetServicesServiceWatchdogsEndpointResponse405 | GetServicesServiceWatchdogsEndpointResponse406 | GetServicesServiceWatchdogsEndpointResponse409 | GetServicesServiceWatchdogsEndpointResponse415 | GetServicesServiceWatchdogsEndpointResponse422 | GetServicesServiceWatchdogsEndpointResponse424 | GetServicesServiceWatchdogsEndpointResponse500 | GetServicesServiceWatchdogsEndpointResponse503]
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
    sort_order: GetServicesServiceWatchdogsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetServicesServiceWatchdogsEndpointSortFlags | Unset = UNSET,
    query: GetServicesServiceWatchdogsEndpointQuery | Unset = UNSET,
) -> (
    GetServicesServiceWatchdogsEndpointResponse400
    | GetServicesServiceWatchdogsEndpointResponse401
    | GetServicesServiceWatchdogsEndpointResponse403
    | GetServicesServiceWatchdogsEndpointResponse404
    | GetServicesServiceWatchdogsEndpointResponse405
    | GetServicesServiceWatchdogsEndpointResponse406
    | GetServicesServiceWatchdogsEndpointResponse409
    | GetServicesServiceWatchdogsEndpointResponse415
    | GetServicesServiceWatchdogsEndpointResponse422
    | GetServicesServiceWatchdogsEndpointResponse424
    | GetServicesServiceWatchdogsEndpointResponse500
    | GetServicesServiceWatchdogsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing Service Watchdogs.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdogs-get ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetServicesServiceWatchdogsEndpointSortOrder | Unset):
        sort_flags (GetServicesServiceWatchdogsEndpointSortFlags | Unset):
        query (GetServicesServiceWatchdogsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesServiceWatchdogsEndpointResponse400 | GetServicesServiceWatchdogsEndpointResponse401 | GetServicesServiceWatchdogsEndpointResponse403 | GetServicesServiceWatchdogsEndpointResponse404 | GetServicesServiceWatchdogsEndpointResponse405 | GetServicesServiceWatchdogsEndpointResponse406 | GetServicesServiceWatchdogsEndpointResponse409 | GetServicesServiceWatchdogsEndpointResponse415 | GetServicesServiceWatchdogsEndpointResponse422 | GetServicesServiceWatchdogsEndpointResponse424 | GetServicesServiceWatchdogsEndpointResponse500 | GetServicesServiceWatchdogsEndpointResponse503
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
