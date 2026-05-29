from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_firewall_schedules_endpoint_query import DeleteFirewallSchedulesEndpointQuery
from ...models.delete_firewall_schedules_endpoint_response_400 import DeleteFirewallSchedulesEndpointResponse400
from ...models.delete_firewall_schedules_endpoint_response_401 import DeleteFirewallSchedulesEndpointResponse401
from ...models.delete_firewall_schedules_endpoint_response_403 import DeleteFirewallSchedulesEndpointResponse403
from ...models.delete_firewall_schedules_endpoint_response_404 import DeleteFirewallSchedulesEndpointResponse404
from ...models.delete_firewall_schedules_endpoint_response_405 import DeleteFirewallSchedulesEndpointResponse405
from ...models.delete_firewall_schedules_endpoint_response_406 import DeleteFirewallSchedulesEndpointResponse406
from ...models.delete_firewall_schedules_endpoint_response_409 import DeleteFirewallSchedulesEndpointResponse409
from ...models.delete_firewall_schedules_endpoint_response_415 import DeleteFirewallSchedulesEndpointResponse415
from ...models.delete_firewall_schedules_endpoint_response_422 import DeleteFirewallSchedulesEndpointResponse422
from ...models.delete_firewall_schedules_endpoint_response_424 import DeleteFirewallSchedulesEndpointResponse424
from ...models.delete_firewall_schedules_endpoint_response_500 import DeleteFirewallSchedulesEndpointResponse500
from ...models.delete_firewall_schedules_endpoint_response_503 import DeleteFirewallSchedulesEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteFirewallSchedulesEndpointQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/firewall/schedules",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteFirewallSchedulesEndpointResponse400
    | DeleteFirewallSchedulesEndpointResponse401
    | DeleteFirewallSchedulesEndpointResponse403
    | DeleteFirewallSchedulesEndpointResponse404
    | DeleteFirewallSchedulesEndpointResponse405
    | DeleteFirewallSchedulesEndpointResponse406
    | DeleteFirewallSchedulesEndpointResponse409
    | DeleteFirewallSchedulesEndpointResponse415
    | DeleteFirewallSchedulesEndpointResponse422
    | DeleteFirewallSchedulesEndpointResponse424
    | DeleteFirewallSchedulesEndpointResponse500
    | DeleteFirewallSchedulesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteFirewallSchedulesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteFirewallSchedulesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteFirewallSchedulesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteFirewallSchedulesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteFirewallSchedulesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteFirewallSchedulesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteFirewallSchedulesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteFirewallSchedulesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteFirewallSchedulesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteFirewallSchedulesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteFirewallSchedulesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteFirewallSchedulesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteFirewallSchedulesEndpointResponse400
    | DeleteFirewallSchedulesEndpointResponse401
    | DeleteFirewallSchedulesEndpointResponse403
    | DeleteFirewallSchedulesEndpointResponse404
    | DeleteFirewallSchedulesEndpointResponse405
    | DeleteFirewallSchedulesEndpointResponse406
    | DeleteFirewallSchedulesEndpointResponse409
    | DeleteFirewallSchedulesEndpointResponse415
    | DeleteFirewallSchedulesEndpointResponse422
    | DeleteFirewallSchedulesEndpointResponse424
    | DeleteFirewallSchedulesEndpointResponse500
    | DeleteFirewallSchedulesEndpointResponse503
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
    query: DeleteFirewallSchedulesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteFirewallSchedulesEndpointResponse400
    | DeleteFirewallSchedulesEndpointResponse401
    | DeleteFirewallSchedulesEndpointResponse403
    | DeleteFirewallSchedulesEndpointResponse404
    | DeleteFirewallSchedulesEndpointResponse405
    | DeleteFirewallSchedulesEndpointResponse406
    | DeleteFirewallSchedulesEndpointResponse409
    | DeleteFirewallSchedulesEndpointResponse415
    | DeleteFirewallSchedulesEndpointResponse422
    | DeleteFirewallSchedulesEndpointResponse424
    | DeleteFirewallSchedulesEndpointResponse500
    | DeleteFirewallSchedulesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Firewall Schedules using a query.<br><br>WARNING:
    This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedules-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteFirewallSchedulesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallSchedulesEndpointResponse400 | DeleteFirewallSchedulesEndpointResponse401 | DeleteFirewallSchedulesEndpointResponse403 | DeleteFirewallSchedulesEndpointResponse404 | DeleteFirewallSchedulesEndpointResponse405 | DeleteFirewallSchedulesEndpointResponse406 | DeleteFirewallSchedulesEndpointResponse409 | DeleteFirewallSchedulesEndpointResponse415 | DeleteFirewallSchedulesEndpointResponse422 | DeleteFirewallSchedulesEndpointResponse424 | DeleteFirewallSchedulesEndpointResponse500 | DeleteFirewallSchedulesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
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
    query: DeleteFirewallSchedulesEndpointQuery | Unset = UNSET,
) -> (
    DeleteFirewallSchedulesEndpointResponse400
    | DeleteFirewallSchedulesEndpointResponse401
    | DeleteFirewallSchedulesEndpointResponse403
    | DeleteFirewallSchedulesEndpointResponse404
    | DeleteFirewallSchedulesEndpointResponse405
    | DeleteFirewallSchedulesEndpointResponse406
    | DeleteFirewallSchedulesEndpointResponse409
    | DeleteFirewallSchedulesEndpointResponse415
    | DeleteFirewallSchedulesEndpointResponse422
    | DeleteFirewallSchedulesEndpointResponse424
    | DeleteFirewallSchedulesEndpointResponse500
    | DeleteFirewallSchedulesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Firewall Schedules using a query.<br><br>WARNING:
    This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedules-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteFirewallSchedulesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallSchedulesEndpointResponse400 | DeleteFirewallSchedulesEndpointResponse401 | DeleteFirewallSchedulesEndpointResponse403 | DeleteFirewallSchedulesEndpointResponse404 | DeleteFirewallSchedulesEndpointResponse405 | DeleteFirewallSchedulesEndpointResponse406 | DeleteFirewallSchedulesEndpointResponse409 | DeleteFirewallSchedulesEndpointResponse415 | DeleteFirewallSchedulesEndpointResponse422 | DeleteFirewallSchedulesEndpointResponse424 | DeleteFirewallSchedulesEndpointResponse500 | DeleteFirewallSchedulesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteFirewallSchedulesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteFirewallSchedulesEndpointResponse400
    | DeleteFirewallSchedulesEndpointResponse401
    | DeleteFirewallSchedulesEndpointResponse403
    | DeleteFirewallSchedulesEndpointResponse404
    | DeleteFirewallSchedulesEndpointResponse405
    | DeleteFirewallSchedulesEndpointResponse406
    | DeleteFirewallSchedulesEndpointResponse409
    | DeleteFirewallSchedulesEndpointResponse415
    | DeleteFirewallSchedulesEndpointResponse422
    | DeleteFirewallSchedulesEndpointResponse424
    | DeleteFirewallSchedulesEndpointResponse500
    | DeleteFirewallSchedulesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Firewall Schedules using a query.<br><br>WARNING:
    This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedules-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteFirewallSchedulesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallSchedulesEndpointResponse400 | DeleteFirewallSchedulesEndpointResponse401 | DeleteFirewallSchedulesEndpointResponse403 | DeleteFirewallSchedulesEndpointResponse404 | DeleteFirewallSchedulesEndpointResponse405 | DeleteFirewallSchedulesEndpointResponse406 | DeleteFirewallSchedulesEndpointResponse409 | DeleteFirewallSchedulesEndpointResponse415 | DeleteFirewallSchedulesEndpointResponse422 | DeleteFirewallSchedulesEndpointResponse424 | DeleteFirewallSchedulesEndpointResponse500 | DeleteFirewallSchedulesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteFirewallSchedulesEndpointQuery | Unset = UNSET,
) -> (
    DeleteFirewallSchedulesEndpointResponse400
    | DeleteFirewallSchedulesEndpointResponse401
    | DeleteFirewallSchedulesEndpointResponse403
    | DeleteFirewallSchedulesEndpointResponse404
    | DeleteFirewallSchedulesEndpointResponse405
    | DeleteFirewallSchedulesEndpointResponse406
    | DeleteFirewallSchedulesEndpointResponse409
    | DeleteFirewallSchedulesEndpointResponse415
    | DeleteFirewallSchedulesEndpointResponse422
    | DeleteFirewallSchedulesEndpointResponse424
    | DeleteFirewallSchedulesEndpointResponse500
    | DeleteFirewallSchedulesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Firewall Schedules using a query.<br><br>WARNING:
    This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedules-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteFirewallSchedulesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallSchedulesEndpointResponse400 | DeleteFirewallSchedulesEndpointResponse401 | DeleteFirewallSchedulesEndpointResponse403 | DeleteFirewallSchedulesEndpointResponse404 | DeleteFirewallSchedulesEndpointResponse405 | DeleteFirewallSchedulesEndpointResponse406 | DeleteFirewallSchedulesEndpointResponse409 | DeleteFirewallSchedulesEndpointResponse415 | DeleteFirewallSchedulesEndpointResponse422 | DeleteFirewallSchedulesEndpointResponse424 | DeleteFirewallSchedulesEndpointResponse500 | DeleteFirewallSchedulesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
