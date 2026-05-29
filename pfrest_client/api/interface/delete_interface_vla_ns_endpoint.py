from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_interface_vla_ns_endpoint_query import DeleteInterfaceVLANsEndpointQuery
from ...models.delete_interface_vla_ns_endpoint_response_400 import DeleteInterfaceVLANsEndpointResponse400
from ...models.delete_interface_vla_ns_endpoint_response_401 import DeleteInterfaceVLANsEndpointResponse401
from ...models.delete_interface_vla_ns_endpoint_response_403 import DeleteInterfaceVLANsEndpointResponse403
from ...models.delete_interface_vla_ns_endpoint_response_404 import DeleteInterfaceVLANsEndpointResponse404
from ...models.delete_interface_vla_ns_endpoint_response_405 import DeleteInterfaceVLANsEndpointResponse405
from ...models.delete_interface_vla_ns_endpoint_response_406 import DeleteInterfaceVLANsEndpointResponse406
from ...models.delete_interface_vla_ns_endpoint_response_409 import DeleteInterfaceVLANsEndpointResponse409
from ...models.delete_interface_vla_ns_endpoint_response_415 import DeleteInterfaceVLANsEndpointResponse415
from ...models.delete_interface_vla_ns_endpoint_response_422 import DeleteInterfaceVLANsEndpointResponse422
from ...models.delete_interface_vla_ns_endpoint_response_424 import DeleteInterfaceVLANsEndpointResponse424
from ...models.delete_interface_vla_ns_endpoint_response_500 import DeleteInterfaceVLANsEndpointResponse500
from ...models.delete_interface_vla_ns_endpoint_response_503 import DeleteInterfaceVLANsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteInterfaceVLANsEndpointQuery | Unset = UNSET,
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
        "url": "/api/v2/interface/vlans",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteInterfaceVLANsEndpointResponse400
    | DeleteInterfaceVLANsEndpointResponse401
    | DeleteInterfaceVLANsEndpointResponse403
    | DeleteInterfaceVLANsEndpointResponse404
    | DeleteInterfaceVLANsEndpointResponse405
    | DeleteInterfaceVLANsEndpointResponse406
    | DeleteInterfaceVLANsEndpointResponse409
    | DeleteInterfaceVLANsEndpointResponse415
    | DeleteInterfaceVLANsEndpointResponse422
    | DeleteInterfaceVLANsEndpointResponse424
    | DeleteInterfaceVLANsEndpointResponse500
    | DeleteInterfaceVLANsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteInterfaceVLANsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteInterfaceVLANsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteInterfaceVLANsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteInterfaceVLANsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteInterfaceVLANsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteInterfaceVLANsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteInterfaceVLANsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteInterfaceVLANsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteInterfaceVLANsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteInterfaceVLANsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteInterfaceVLANsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteInterfaceVLANsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteInterfaceVLANsEndpointResponse400
    | DeleteInterfaceVLANsEndpointResponse401
    | DeleteInterfaceVLANsEndpointResponse403
    | DeleteInterfaceVLANsEndpointResponse404
    | DeleteInterfaceVLANsEndpointResponse405
    | DeleteInterfaceVLANsEndpointResponse406
    | DeleteInterfaceVLANsEndpointResponse409
    | DeleteInterfaceVLANsEndpointResponse415
    | DeleteInterfaceVLANsEndpointResponse422
    | DeleteInterfaceVLANsEndpointResponse424
    | DeleteInterfaceVLANsEndpointResponse500
    | DeleteInterfaceVLANsEndpointResponse503
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
    query: DeleteInterfaceVLANsEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteInterfaceVLANsEndpointResponse400
    | DeleteInterfaceVLANsEndpointResponse401
    | DeleteInterfaceVLANsEndpointResponse403
    | DeleteInterfaceVLANsEndpointResponse404
    | DeleteInterfaceVLANsEndpointResponse405
    | DeleteInterfaceVLANsEndpointResponse406
    | DeleteInterfaceVLANsEndpointResponse409
    | DeleteInterfaceVLANsEndpointResponse415
    | DeleteInterfaceVLANsEndpointResponse422
    | DeleteInterfaceVLANsEndpointResponse424
    | DeleteInterfaceVLANsEndpointResponse500
    | DeleteInterfaceVLANsEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Interface VLANs using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlans-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteInterfaceVLANsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteInterfaceVLANsEndpointResponse400 | DeleteInterfaceVLANsEndpointResponse401 | DeleteInterfaceVLANsEndpointResponse403 | DeleteInterfaceVLANsEndpointResponse404 | DeleteInterfaceVLANsEndpointResponse405 | DeleteInterfaceVLANsEndpointResponse406 | DeleteInterfaceVLANsEndpointResponse409 | DeleteInterfaceVLANsEndpointResponse415 | DeleteInterfaceVLANsEndpointResponse422 | DeleteInterfaceVLANsEndpointResponse424 | DeleteInterfaceVLANsEndpointResponse500 | DeleteInterfaceVLANsEndpointResponse503]
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
    query: DeleteInterfaceVLANsEndpointQuery | Unset = UNSET,
) -> (
    DeleteInterfaceVLANsEndpointResponse400
    | DeleteInterfaceVLANsEndpointResponse401
    | DeleteInterfaceVLANsEndpointResponse403
    | DeleteInterfaceVLANsEndpointResponse404
    | DeleteInterfaceVLANsEndpointResponse405
    | DeleteInterfaceVLANsEndpointResponse406
    | DeleteInterfaceVLANsEndpointResponse409
    | DeleteInterfaceVLANsEndpointResponse415
    | DeleteInterfaceVLANsEndpointResponse422
    | DeleteInterfaceVLANsEndpointResponse424
    | DeleteInterfaceVLANsEndpointResponse500
    | DeleteInterfaceVLANsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Interface VLANs using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlans-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteInterfaceVLANsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteInterfaceVLANsEndpointResponse400 | DeleteInterfaceVLANsEndpointResponse401 | DeleteInterfaceVLANsEndpointResponse403 | DeleteInterfaceVLANsEndpointResponse404 | DeleteInterfaceVLANsEndpointResponse405 | DeleteInterfaceVLANsEndpointResponse406 | DeleteInterfaceVLANsEndpointResponse409 | DeleteInterfaceVLANsEndpointResponse415 | DeleteInterfaceVLANsEndpointResponse422 | DeleteInterfaceVLANsEndpointResponse424 | DeleteInterfaceVLANsEndpointResponse500 | DeleteInterfaceVLANsEndpointResponse503
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
    query: DeleteInterfaceVLANsEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteInterfaceVLANsEndpointResponse400
    | DeleteInterfaceVLANsEndpointResponse401
    | DeleteInterfaceVLANsEndpointResponse403
    | DeleteInterfaceVLANsEndpointResponse404
    | DeleteInterfaceVLANsEndpointResponse405
    | DeleteInterfaceVLANsEndpointResponse406
    | DeleteInterfaceVLANsEndpointResponse409
    | DeleteInterfaceVLANsEndpointResponse415
    | DeleteInterfaceVLANsEndpointResponse422
    | DeleteInterfaceVLANsEndpointResponse424
    | DeleteInterfaceVLANsEndpointResponse500
    | DeleteInterfaceVLANsEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing Interface VLANs using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlans-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteInterfaceVLANsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteInterfaceVLANsEndpointResponse400 | DeleteInterfaceVLANsEndpointResponse401 | DeleteInterfaceVLANsEndpointResponse403 | DeleteInterfaceVLANsEndpointResponse404 | DeleteInterfaceVLANsEndpointResponse405 | DeleteInterfaceVLANsEndpointResponse406 | DeleteInterfaceVLANsEndpointResponse409 | DeleteInterfaceVLANsEndpointResponse415 | DeleteInterfaceVLANsEndpointResponse422 | DeleteInterfaceVLANsEndpointResponse424 | DeleteInterfaceVLANsEndpointResponse500 | DeleteInterfaceVLANsEndpointResponse503]
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
    query: DeleteInterfaceVLANsEndpointQuery | Unset = UNSET,
) -> (
    DeleteInterfaceVLANsEndpointResponse400
    | DeleteInterfaceVLANsEndpointResponse401
    | DeleteInterfaceVLANsEndpointResponse403
    | DeleteInterfaceVLANsEndpointResponse404
    | DeleteInterfaceVLANsEndpointResponse405
    | DeleteInterfaceVLANsEndpointResponse406
    | DeleteInterfaceVLANsEndpointResponse409
    | DeleteInterfaceVLANsEndpointResponse415
    | DeleteInterfaceVLANsEndpointResponse422
    | DeleteInterfaceVLANsEndpointResponse424
    | DeleteInterfaceVLANsEndpointResponse500
    | DeleteInterfaceVLANsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing Interface VLANs using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: InterfaceVLAN<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-vlans-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteInterfaceVLANsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteInterfaceVLANsEndpointResponse400 | DeleteInterfaceVLANsEndpointResponse401 | DeleteInterfaceVLANsEndpointResponse403 | DeleteInterfaceVLANsEndpointResponse404 | DeleteInterfaceVLANsEndpointResponse405 | DeleteInterfaceVLANsEndpointResponse406 | DeleteInterfaceVLANsEndpointResponse409 | DeleteInterfaceVLANsEndpointResponse415 | DeleteInterfaceVLANsEndpointResponse422 | DeleteInterfaceVLANsEndpointResponse424 | DeleteInterfaceVLANsEndpointResponse500 | DeleteInterfaceVLANsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
