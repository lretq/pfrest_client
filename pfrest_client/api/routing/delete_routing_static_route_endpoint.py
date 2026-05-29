from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_routing_static_route_endpoint_response_400 import DeleteRoutingStaticRouteEndpointResponse400
from ...models.delete_routing_static_route_endpoint_response_401 import DeleteRoutingStaticRouteEndpointResponse401
from ...models.delete_routing_static_route_endpoint_response_403 import DeleteRoutingStaticRouteEndpointResponse403
from ...models.delete_routing_static_route_endpoint_response_404 import DeleteRoutingStaticRouteEndpointResponse404
from ...models.delete_routing_static_route_endpoint_response_405 import DeleteRoutingStaticRouteEndpointResponse405
from ...models.delete_routing_static_route_endpoint_response_406 import DeleteRoutingStaticRouteEndpointResponse406
from ...models.delete_routing_static_route_endpoint_response_409 import DeleteRoutingStaticRouteEndpointResponse409
from ...models.delete_routing_static_route_endpoint_response_415 import DeleteRoutingStaticRouteEndpointResponse415
from ...models.delete_routing_static_route_endpoint_response_422 import DeleteRoutingStaticRouteEndpointResponse422
from ...models.delete_routing_static_route_endpoint_response_424 import DeleteRoutingStaticRouteEndpointResponse424
from ...models.delete_routing_static_route_endpoint_response_500 import DeleteRoutingStaticRouteEndpointResponse500
from ...models.delete_routing_static_route_endpoint_response_503 import DeleteRoutingStaticRouteEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | str,
    apply: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params["apply"] = apply

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/routing/static_route",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteRoutingStaticRouteEndpointResponse400
    | DeleteRoutingStaticRouteEndpointResponse401
    | DeleteRoutingStaticRouteEndpointResponse403
    | DeleteRoutingStaticRouteEndpointResponse404
    | DeleteRoutingStaticRouteEndpointResponse405
    | DeleteRoutingStaticRouteEndpointResponse406
    | DeleteRoutingStaticRouteEndpointResponse409
    | DeleteRoutingStaticRouteEndpointResponse415
    | DeleteRoutingStaticRouteEndpointResponse422
    | DeleteRoutingStaticRouteEndpointResponse424
    | DeleteRoutingStaticRouteEndpointResponse500
    | DeleteRoutingStaticRouteEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteRoutingStaticRouteEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteRoutingStaticRouteEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteRoutingStaticRouteEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteRoutingStaticRouteEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteRoutingStaticRouteEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteRoutingStaticRouteEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteRoutingStaticRouteEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteRoutingStaticRouteEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteRoutingStaticRouteEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteRoutingStaticRouteEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteRoutingStaticRouteEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteRoutingStaticRouteEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteRoutingStaticRouteEndpointResponse400
    | DeleteRoutingStaticRouteEndpointResponse401
    | DeleteRoutingStaticRouteEndpointResponse403
    | DeleteRoutingStaticRouteEndpointResponse404
    | DeleteRoutingStaticRouteEndpointResponse405
    | DeleteRoutingStaticRouteEndpointResponse406
    | DeleteRoutingStaticRouteEndpointResponse409
    | DeleteRoutingStaticRouteEndpointResponse415
    | DeleteRoutingStaticRouteEndpointResponse422
    | DeleteRoutingStaticRouteEndpointResponse424
    | DeleteRoutingStaticRouteEndpointResponse500
    | DeleteRoutingStaticRouteEndpointResponse503
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
    apply: bool | Unset = False,
) -> Response[
    DeleteRoutingStaticRouteEndpointResponse400
    | DeleteRoutingStaticRouteEndpointResponse401
    | DeleteRoutingStaticRouteEndpointResponse403
    | DeleteRoutingStaticRouteEndpointResponse404
    | DeleteRoutingStaticRouteEndpointResponse405
    | DeleteRoutingStaticRouteEndpointResponse406
    | DeleteRoutingStaticRouteEndpointResponse409
    | DeleteRoutingStaticRouteEndpointResponse415
    | DeleteRoutingStaticRouteEndpointResponse422
    | DeleteRoutingStaticRouteEndpointResponse424
    | DeleteRoutingStaticRouteEndpointResponse500
    | DeleteRoutingStaticRouteEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteRoutingStaticRouteEndpointResponse400 | DeleteRoutingStaticRouteEndpointResponse401 | DeleteRoutingStaticRouteEndpointResponse403 | DeleteRoutingStaticRouteEndpointResponse404 | DeleteRoutingStaticRouteEndpointResponse405 | DeleteRoutingStaticRouteEndpointResponse406 | DeleteRoutingStaticRouteEndpointResponse409 | DeleteRoutingStaticRouteEndpointResponse415 | DeleteRoutingStaticRouteEndpointResponse422 | DeleteRoutingStaticRouteEndpointResponse424 | DeleteRoutingStaticRouteEndpointResponse500 | DeleteRoutingStaticRouteEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
        apply=apply,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteRoutingStaticRouteEndpointResponse400
    | DeleteRoutingStaticRouteEndpointResponse401
    | DeleteRoutingStaticRouteEndpointResponse403
    | DeleteRoutingStaticRouteEndpointResponse404
    | DeleteRoutingStaticRouteEndpointResponse405
    | DeleteRoutingStaticRouteEndpointResponse406
    | DeleteRoutingStaticRouteEndpointResponse409
    | DeleteRoutingStaticRouteEndpointResponse415
    | DeleteRoutingStaticRouteEndpointResponse422
    | DeleteRoutingStaticRouteEndpointResponse424
    | DeleteRoutingStaticRouteEndpointResponse500
    | DeleteRoutingStaticRouteEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteRoutingStaticRouteEndpointResponse400 | DeleteRoutingStaticRouteEndpointResponse401 | DeleteRoutingStaticRouteEndpointResponse403 | DeleteRoutingStaticRouteEndpointResponse404 | DeleteRoutingStaticRouteEndpointResponse405 | DeleteRoutingStaticRouteEndpointResponse406 | DeleteRoutingStaticRouteEndpointResponse409 | DeleteRoutingStaticRouteEndpointResponse415 | DeleteRoutingStaticRouteEndpointResponse422 | DeleteRoutingStaticRouteEndpointResponse424 | DeleteRoutingStaticRouteEndpointResponse500 | DeleteRoutingStaticRouteEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
        apply=apply,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteRoutingStaticRouteEndpointResponse400
    | DeleteRoutingStaticRouteEndpointResponse401
    | DeleteRoutingStaticRouteEndpointResponse403
    | DeleteRoutingStaticRouteEndpointResponse404
    | DeleteRoutingStaticRouteEndpointResponse405
    | DeleteRoutingStaticRouteEndpointResponse406
    | DeleteRoutingStaticRouteEndpointResponse409
    | DeleteRoutingStaticRouteEndpointResponse415
    | DeleteRoutingStaticRouteEndpointResponse422
    | DeleteRoutingStaticRouteEndpointResponse424
    | DeleteRoutingStaticRouteEndpointResponse500
    | DeleteRoutingStaticRouteEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteRoutingStaticRouteEndpointResponse400 | DeleteRoutingStaticRouteEndpointResponse401 | DeleteRoutingStaticRouteEndpointResponse403 | DeleteRoutingStaticRouteEndpointResponse404 | DeleteRoutingStaticRouteEndpointResponse405 | DeleteRoutingStaticRouteEndpointResponse406 | DeleteRoutingStaticRouteEndpointResponse409 | DeleteRoutingStaticRouteEndpointResponse415 | DeleteRoutingStaticRouteEndpointResponse422 | DeleteRoutingStaticRouteEndpointResponse424 | DeleteRoutingStaticRouteEndpointResponse500 | DeleteRoutingStaticRouteEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
        apply=apply,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteRoutingStaticRouteEndpointResponse400
    | DeleteRoutingStaticRouteEndpointResponse401
    | DeleteRoutingStaticRouteEndpointResponse403
    | DeleteRoutingStaticRouteEndpointResponse404
    | DeleteRoutingStaticRouteEndpointResponse405
    | DeleteRoutingStaticRouteEndpointResponse406
    | DeleteRoutingStaticRouteEndpointResponse409
    | DeleteRoutingStaticRouteEndpointResponse415
    | DeleteRoutingStaticRouteEndpointResponse422
    | DeleteRoutingStaticRouteEndpointResponse424
    | DeleteRoutingStaticRouteEndpointResponse500
    | DeleteRoutingStaticRouteEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteRoutingStaticRouteEndpointResponse400 | DeleteRoutingStaticRouteEndpointResponse401 | DeleteRoutingStaticRouteEndpointResponse403 | DeleteRoutingStaticRouteEndpointResponse404 | DeleteRoutingStaticRouteEndpointResponse405 | DeleteRoutingStaticRouteEndpointResponse406 | DeleteRoutingStaticRouteEndpointResponse409 | DeleteRoutingStaticRouteEndpointResponse415 | DeleteRoutingStaticRouteEndpointResponse422 | DeleteRoutingStaticRouteEndpointResponse424 | DeleteRoutingStaticRouteEndpointResponse500 | DeleteRoutingStaticRouteEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            apply=apply,
        )
    ).parsed
