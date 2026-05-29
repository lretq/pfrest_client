from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_routing_static_route_endpoint_data_body import PatchRoutingStaticRouteEndpointDataBody
from ...models.patch_routing_static_route_endpoint_json_body import PatchRoutingStaticRouteEndpointJsonBody
from ...models.patch_routing_static_route_endpoint_response_400 import PatchRoutingStaticRouteEndpointResponse400
from ...models.patch_routing_static_route_endpoint_response_401 import PatchRoutingStaticRouteEndpointResponse401
from ...models.patch_routing_static_route_endpoint_response_403 import PatchRoutingStaticRouteEndpointResponse403
from ...models.patch_routing_static_route_endpoint_response_404 import PatchRoutingStaticRouteEndpointResponse404
from ...models.patch_routing_static_route_endpoint_response_405 import PatchRoutingStaticRouteEndpointResponse405
from ...models.patch_routing_static_route_endpoint_response_406 import PatchRoutingStaticRouteEndpointResponse406
from ...models.patch_routing_static_route_endpoint_response_409 import PatchRoutingStaticRouteEndpointResponse409
from ...models.patch_routing_static_route_endpoint_response_415 import PatchRoutingStaticRouteEndpointResponse415
from ...models.patch_routing_static_route_endpoint_response_422 import PatchRoutingStaticRouteEndpointResponse422
from ...models.patch_routing_static_route_endpoint_response_424 import PatchRoutingStaticRouteEndpointResponse424
from ...models.patch_routing_static_route_endpoint_response_500 import PatchRoutingStaticRouteEndpointResponse500
from ...models.patch_routing_static_route_endpoint_response_503 import PatchRoutingStaticRouteEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchRoutingStaticRouteEndpointJsonBody | PatchRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/routing/static_route",
    }

    if isinstance(body, PatchRoutingStaticRouteEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchRoutingStaticRouteEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchRoutingStaticRouteEndpointResponse400
    | PatchRoutingStaticRouteEndpointResponse401
    | PatchRoutingStaticRouteEndpointResponse403
    | PatchRoutingStaticRouteEndpointResponse404
    | PatchRoutingStaticRouteEndpointResponse405
    | PatchRoutingStaticRouteEndpointResponse406
    | PatchRoutingStaticRouteEndpointResponse409
    | PatchRoutingStaticRouteEndpointResponse415
    | PatchRoutingStaticRouteEndpointResponse422
    | PatchRoutingStaticRouteEndpointResponse424
    | PatchRoutingStaticRouteEndpointResponse500
    | PatchRoutingStaticRouteEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchRoutingStaticRouteEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchRoutingStaticRouteEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchRoutingStaticRouteEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchRoutingStaticRouteEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchRoutingStaticRouteEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchRoutingStaticRouteEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchRoutingStaticRouteEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchRoutingStaticRouteEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchRoutingStaticRouteEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchRoutingStaticRouteEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchRoutingStaticRouteEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchRoutingStaticRouteEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchRoutingStaticRouteEndpointResponse400
    | PatchRoutingStaticRouteEndpointResponse401
    | PatchRoutingStaticRouteEndpointResponse403
    | PatchRoutingStaticRouteEndpointResponse404
    | PatchRoutingStaticRouteEndpointResponse405
    | PatchRoutingStaticRouteEndpointResponse406
    | PatchRoutingStaticRouteEndpointResponse409
    | PatchRoutingStaticRouteEndpointResponse415
    | PatchRoutingStaticRouteEndpointResponse422
    | PatchRoutingStaticRouteEndpointResponse424
    | PatchRoutingStaticRouteEndpointResponse500
    | PatchRoutingStaticRouteEndpointResponse503
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
    body: PatchRoutingStaticRouteEndpointJsonBody | PatchRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchRoutingStaticRouteEndpointResponse400
    | PatchRoutingStaticRouteEndpointResponse401
    | PatchRoutingStaticRouteEndpointResponse403
    | PatchRoutingStaticRouteEndpointResponse404
    | PatchRoutingStaticRouteEndpointResponse405
    | PatchRoutingStaticRouteEndpointResponse406
    | PatchRoutingStaticRouteEndpointResponse409
    | PatchRoutingStaticRouteEndpointResponse415
    | PatchRoutingStaticRouteEndpointResponse422
    | PatchRoutingStaticRouteEndpointResponse424
    | PatchRoutingStaticRouteEndpointResponse500
    | PatchRoutingStaticRouteEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingStaticRouteEndpointJsonBody | Unset):
        body (PatchRoutingStaticRouteEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchRoutingStaticRouteEndpointResponse400 | PatchRoutingStaticRouteEndpointResponse401 | PatchRoutingStaticRouteEndpointResponse403 | PatchRoutingStaticRouteEndpointResponse404 | PatchRoutingStaticRouteEndpointResponse405 | PatchRoutingStaticRouteEndpointResponse406 | PatchRoutingStaticRouteEndpointResponse409 | PatchRoutingStaticRouteEndpointResponse415 | PatchRoutingStaticRouteEndpointResponse422 | PatchRoutingStaticRouteEndpointResponse424 | PatchRoutingStaticRouteEndpointResponse500 | PatchRoutingStaticRouteEndpointResponse503]
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
    body: PatchRoutingStaticRouteEndpointJsonBody | PatchRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> (
    PatchRoutingStaticRouteEndpointResponse400
    | PatchRoutingStaticRouteEndpointResponse401
    | PatchRoutingStaticRouteEndpointResponse403
    | PatchRoutingStaticRouteEndpointResponse404
    | PatchRoutingStaticRouteEndpointResponse405
    | PatchRoutingStaticRouteEndpointResponse406
    | PatchRoutingStaticRouteEndpointResponse409
    | PatchRoutingStaticRouteEndpointResponse415
    | PatchRoutingStaticRouteEndpointResponse422
    | PatchRoutingStaticRouteEndpointResponse424
    | PatchRoutingStaticRouteEndpointResponse500
    | PatchRoutingStaticRouteEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingStaticRouteEndpointJsonBody | Unset):
        body (PatchRoutingStaticRouteEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchRoutingStaticRouteEndpointResponse400 | PatchRoutingStaticRouteEndpointResponse401 | PatchRoutingStaticRouteEndpointResponse403 | PatchRoutingStaticRouteEndpointResponse404 | PatchRoutingStaticRouteEndpointResponse405 | PatchRoutingStaticRouteEndpointResponse406 | PatchRoutingStaticRouteEndpointResponse409 | PatchRoutingStaticRouteEndpointResponse415 | PatchRoutingStaticRouteEndpointResponse422 | PatchRoutingStaticRouteEndpointResponse424 | PatchRoutingStaticRouteEndpointResponse500 | PatchRoutingStaticRouteEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingStaticRouteEndpointJsonBody | PatchRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchRoutingStaticRouteEndpointResponse400
    | PatchRoutingStaticRouteEndpointResponse401
    | PatchRoutingStaticRouteEndpointResponse403
    | PatchRoutingStaticRouteEndpointResponse404
    | PatchRoutingStaticRouteEndpointResponse405
    | PatchRoutingStaticRouteEndpointResponse406
    | PatchRoutingStaticRouteEndpointResponse409
    | PatchRoutingStaticRouteEndpointResponse415
    | PatchRoutingStaticRouteEndpointResponse422
    | PatchRoutingStaticRouteEndpointResponse424
    | PatchRoutingStaticRouteEndpointResponse500
    | PatchRoutingStaticRouteEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingStaticRouteEndpointJsonBody | Unset):
        body (PatchRoutingStaticRouteEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchRoutingStaticRouteEndpointResponse400 | PatchRoutingStaticRouteEndpointResponse401 | PatchRoutingStaticRouteEndpointResponse403 | PatchRoutingStaticRouteEndpointResponse404 | PatchRoutingStaticRouteEndpointResponse405 | PatchRoutingStaticRouteEndpointResponse406 | PatchRoutingStaticRouteEndpointResponse409 | PatchRoutingStaticRouteEndpointResponse415 | PatchRoutingStaticRouteEndpointResponse422 | PatchRoutingStaticRouteEndpointResponse424 | PatchRoutingStaticRouteEndpointResponse500 | PatchRoutingStaticRouteEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingStaticRouteEndpointJsonBody | PatchRoutingStaticRouteEndpointDataBody | Unset = UNSET,
) -> (
    PatchRoutingStaticRouteEndpointResponse400
    | PatchRoutingStaticRouteEndpointResponse401
    | PatchRoutingStaticRouteEndpointResponse403
    | PatchRoutingStaticRouteEndpointResponse404
    | PatchRoutingStaticRouteEndpointResponse405
    | PatchRoutingStaticRouteEndpointResponse406
    | PatchRoutingStaticRouteEndpointResponse409
    | PatchRoutingStaticRouteEndpointResponse415
    | PatchRoutingStaticRouteEndpointResponse422
    | PatchRoutingStaticRouteEndpointResponse424
    | PatchRoutingStaticRouteEndpointResponse500
    | PatchRoutingStaticRouteEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Static Route.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: StaticRoute<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-static-route-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingStaticRouteEndpointJsonBody | Unset):
        body (PatchRoutingStaticRouteEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchRoutingStaticRouteEndpointResponse400 | PatchRoutingStaticRouteEndpointResponse401 | PatchRoutingStaticRouteEndpointResponse403 | PatchRoutingStaticRouteEndpointResponse404 | PatchRoutingStaticRouteEndpointResponse405 | PatchRoutingStaticRouteEndpointResponse406 | PatchRoutingStaticRouteEndpointResponse409 | PatchRoutingStaticRouteEndpointResponse415 | PatchRoutingStaticRouteEndpointResponse422 | PatchRoutingStaticRouteEndpointResponse424 | PatchRoutingStaticRouteEndpointResponse500 | PatchRoutingStaticRouteEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
