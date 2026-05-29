from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_network_interfaces_endpoint_query import DeleteNetworkInterfacesEndpointQuery
from ...models.delete_network_interfaces_endpoint_response_400 import DeleteNetworkInterfacesEndpointResponse400
from ...models.delete_network_interfaces_endpoint_response_401 import DeleteNetworkInterfacesEndpointResponse401
from ...models.delete_network_interfaces_endpoint_response_403 import DeleteNetworkInterfacesEndpointResponse403
from ...models.delete_network_interfaces_endpoint_response_404 import DeleteNetworkInterfacesEndpointResponse404
from ...models.delete_network_interfaces_endpoint_response_405 import DeleteNetworkInterfacesEndpointResponse405
from ...models.delete_network_interfaces_endpoint_response_406 import DeleteNetworkInterfacesEndpointResponse406
from ...models.delete_network_interfaces_endpoint_response_409 import DeleteNetworkInterfacesEndpointResponse409
from ...models.delete_network_interfaces_endpoint_response_415 import DeleteNetworkInterfacesEndpointResponse415
from ...models.delete_network_interfaces_endpoint_response_422 import DeleteNetworkInterfacesEndpointResponse422
from ...models.delete_network_interfaces_endpoint_response_424 import DeleteNetworkInterfacesEndpointResponse424
from ...models.delete_network_interfaces_endpoint_response_500 import DeleteNetworkInterfacesEndpointResponse500
from ...models.delete_network_interfaces_endpoint_response_503 import DeleteNetworkInterfacesEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteNetworkInterfacesEndpointQuery | Unset = UNSET,
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
        "url": "/api/v2/interfaces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteNetworkInterfacesEndpointResponse400
    | DeleteNetworkInterfacesEndpointResponse401
    | DeleteNetworkInterfacesEndpointResponse403
    | DeleteNetworkInterfacesEndpointResponse404
    | DeleteNetworkInterfacesEndpointResponse405
    | DeleteNetworkInterfacesEndpointResponse406
    | DeleteNetworkInterfacesEndpointResponse409
    | DeleteNetworkInterfacesEndpointResponse415
    | DeleteNetworkInterfacesEndpointResponse422
    | DeleteNetworkInterfacesEndpointResponse424
    | DeleteNetworkInterfacesEndpointResponse500
    | DeleteNetworkInterfacesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteNetworkInterfacesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteNetworkInterfacesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteNetworkInterfacesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteNetworkInterfacesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteNetworkInterfacesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteNetworkInterfacesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteNetworkInterfacesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteNetworkInterfacesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteNetworkInterfacesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteNetworkInterfacesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteNetworkInterfacesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteNetworkInterfacesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteNetworkInterfacesEndpointResponse400
    | DeleteNetworkInterfacesEndpointResponse401
    | DeleteNetworkInterfacesEndpointResponse403
    | DeleteNetworkInterfacesEndpointResponse404
    | DeleteNetworkInterfacesEndpointResponse405
    | DeleteNetworkInterfacesEndpointResponse406
    | DeleteNetworkInterfacesEndpointResponse409
    | DeleteNetworkInterfacesEndpointResponse415
    | DeleteNetworkInterfacesEndpointResponse422
    | DeleteNetworkInterfacesEndpointResponse424
    | DeleteNetworkInterfacesEndpointResponse500
    | DeleteNetworkInterfacesEndpointResponse503
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
    query: DeleteNetworkInterfacesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteNetworkInterfacesEndpointResponse400
    | DeleteNetworkInterfacesEndpointResponse401
    | DeleteNetworkInterfacesEndpointResponse403
    | DeleteNetworkInterfacesEndpointResponse404
    | DeleteNetworkInterfacesEndpointResponse405
    | DeleteNetworkInterfacesEndpointResponse406
    | DeleteNetworkInterfacesEndpointResponse409
    | DeleteNetworkInterfacesEndpointResponse415
    | DeleteNetworkInterfacesEndpointResponse422
    | DeleteNetworkInterfacesEndpointResponse424
    | DeleteNetworkInterfacesEndpointResponse500
    | DeleteNetworkInterfacesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Network Interfaces using a query.<br><br>WARNING:
    This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interfaces-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteNetworkInterfacesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteNetworkInterfacesEndpointResponse400 | DeleteNetworkInterfacesEndpointResponse401 | DeleteNetworkInterfacesEndpointResponse403 | DeleteNetworkInterfacesEndpointResponse404 | DeleteNetworkInterfacesEndpointResponse405 | DeleteNetworkInterfacesEndpointResponse406 | DeleteNetworkInterfacesEndpointResponse409 | DeleteNetworkInterfacesEndpointResponse415 | DeleteNetworkInterfacesEndpointResponse422 | DeleteNetworkInterfacesEndpointResponse424 | DeleteNetworkInterfacesEndpointResponse500 | DeleteNetworkInterfacesEndpointResponse503]
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
    query: DeleteNetworkInterfacesEndpointQuery | Unset = UNSET,
) -> (
    DeleteNetworkInterfacesEndpointResponse400
    | DeleteNetworkInterfacesEndpointResponse401
    | DeleteNetworkInterfacesEndpointResponse403
    | DeleteNetworkInterfacesEndpointResponse404
    | DeleteNetworkInterfacesEndpointResponse405
    | DeleteNetworkInterfacesEndpointResponse406
    | DeleteNetworkInterfacesEndpointResponse409
    | DeleteNetworkInterfacesEndpointResponse415
    | DeleteNetworkInterfacesEndpointResponse422
    | DeleteNetworkInterfacesEndpointResponse424
    | DeleteNetworkInterfacesEndpointResponse500
    | DeleteNetworkInterfacesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Network Interfaces using a query.<br><br>WARNING:
    This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interfaces-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteNetworkInterfacesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteNetworkInterfacesEndpointResponse400 | DeleteNetworkInterfacesEndpointResponse401 | DeleteNetworkInterfacesEndpointResponse403 | DeleteNetworkInterfacesEndpointResponse404 | DeleteNetworkInterfacesEndpointResponse405 | DeleteNetworkInterfacesEndpointResponse406 | DeleteNetworkInterfacesEndpointResponse409 | DeleteNetworkInterfacesEndpointResponse415 | DeleteNetworkInterfacesEndpointResponse422 | DeleteNetworkInterfacesEndpointResponse424 | DeleteNetworkInterfacesEndpointResponse500 | DeleteNetworkInterfacesEndpointResponse503
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
    query: DeleteNetworkInterfacesEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteNetworkInterfacesEndpointResponse400
    | DeleteNetworkInterfacesEndpointResponse401
    | DeleteNetworkInterfacesEndpointResponse403
    | DeleteNetworkInterfacesEndpointResponse404
    | DeleteNetworkInterfacesEndpointResponse405
    | DeleteNetworkInterfacesEndpointResponse406
    | DeleteNetworkInterfacesEndpointResponse409
    | DeleteNetworkInterfacesEndpointResponse415
    | DeleteNetworkInterfacesEndpointResponse422
    | DeleteNetworkInterfacesEndpointResponse424
    | DeleteNetworkInterfacesEndpointResponse500
    | DeleteNetworkInterfacesEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Network Interfaces using a query.<br><br>WARNING:
    This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interfaces-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteNetworkInterfacesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteNetworkInterfacesEndpointResponse400 | DeleteNetworkInterfacesEndpointResponse401 | DeleteNetworkInterfacesEndpointResponse403 | DeleteNetworkInterfacesEndpointResponse404 | DeleteNetworkInterfacesEndpointResponse405 | DeleteNetworkInterfacesEndpointResponse406 | DeleteNetworkInterfacesEndpointResponse409 | DeleteNetworkInterfacesEndpointResponse415 | DeleteNetworkInterfacesEndpointResponse422 | DeleteNetworkInterfacesEndpointResponse424 | DeleteNetworkInterfacesEndpointResponse500 | DeleteNetworkInterfacesEndpointResponse503]
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
    query: DeleteNetworkInterfacesEndpointQuery | Unset = UNSET,
) -> (
    DeleteNetworkInterfacesEndpointResponse400
    | DeleteNetworkInterfacesEndpointResponse401
    | DeleteNetworkInterfacesEndpointResponse403
    | DeleteNetworkInterfacesEndpointResponse404
    | DeleteNetworkInterfacesEndpointResponse405
    | DeleteNetworkInterfacesEndpointResponse406
    | DeleteNetworkInterfacesEndpointResponse409
    | DeleteNetworkInterfacesEndpointResponse415
    | DeleteNetworkInterfacesEndpointResponse422
    | DeleteNetworkInterfacesEndpointResponse424
    | DeleteNetworkInterfacesEndpointResponse500
    | DeleteNetworkInterfacesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Network Interfaces using a query.<br><br>WARNING:
    This will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: NetworkInterface<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interfaces-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteNetworkInterfacesEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteNetworkInterfacesEndpointResponse400 | DeleteNetworkInterfacesEndpointResponse401 | DeleteNetworkInterfacesEndpointResponse403 | DeleteNetworkInterfacesEndpointResponse404 | DeleteNetworkInterfacesEndpointResponse405 | DeleteNetworkInterfacesEndpointResponse406 | DeleteNetworkInterfacesEndpointResponse409 | DeleteNetworkInterfacesEndpointResponse415 | DeleteNetworkInterfacesEndpointResponse422 | DeleteNetworkInterfacesEndpointResponse424 | DeleteNetworkInterfacesEndpointResponse500 | DeleteNetworkInterfacesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
