from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_routing_apply_endpoint_response_400 import GetRoutingApplyEndpointResponse400
from ...models.get_routing_apply_endpoint_response_401 import GetRoutingApplyEndpointResponse401
from ...models.get_routing_apply_endpoint_response_403 import GetRoutingApplyEndpointResponse403
from ...models.get_routing_apply_endpoint_response_404 import GetRoutingApplyEndpointResponse404
from ...models.get_routing_apply_endpoint_response_405 import GetRoutingApplyEndpointResponse405
from ...models.get_routing_apply_endpoint_response_406 import GetRoutingApplyEndpointResponse406
from ...models.get_routing_apply_endpoint_response_409 import GetRoutingApplyEndpointResponse409
from ...models.get_routing_apply_endpoint_response_415 import GetRoutingApplyEndpointResponse415
from ...models.get_routing_apply_endpoint_response_422 import GetRoutingApplyEndpointResponse422
from ...models.get_routing_apply_endpoint_response_424 import GetRoutingApplyEndpointResponse424
from ...models.get_routing_apply_endpoint_response_500 import GetRoutingApplyEndpointResponse500
from ...models.get_routing_apply_endpoint_response_503 import GetRoutingApplyEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/routing/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetRoutingApplyEndpointResponse400
    | GetRoutingApplyEndpointResponse401
    | GetRoutingApplyEndpointResponse403
    | GetRoutingApplyEndpointResponse404
    | GetRoutingApplyEndpointResponse405
    | GetRoutingApplyEndpointResponse406
    | GetRoutingApplyEndpointResponse409
    | GetRoutingApplyEndpointResponse415
    | GetRoutingApplyEndpointResponse422
    | GetRoutingApplyEndpointResponse424
    | GetRoutingApplyEndpointResponse500
    | GetRoutingApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetRoutingApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetRoutingApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetRoutingApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetRoutingApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetRoutingApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetRoutingApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetRoutingApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetRoutingApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetRoutingApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetRoutingApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetRoutingApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetRoutingApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRoutingApplyEndpointResponse400
    | GetRoutingApplyEndpointResponse401
    | GetRoutingApplyEndpointResponse403
    | GetRoutingApplyEndpointResponse404
    | GetRoutingApplyEndpointResponse405
    | GetRoutingApplyEndpointResponse406
    | GetRoutingApplyEndpointResponse409
    | GetRoutingApplyEndpointResponse415
    | GetRoutingApplyEndpointResponse422
    | GetRoutingApplyEndpointResponse424
    | GetRoutingApplyEndpointResponse500
    | GetRoutingApplyEndpointResponse503
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
) -> Response[
    GetRoutingApplyEndpointResponse400
    | GetRoutingApplyEndpointResponse401
    | GetRoutingApplyEndpointResponse403
    | GetRoutingApplyEndpointResponse404
    | GetRoutingApplyEndpointResponse405
    | GetRoutingApplyEndpointResponse406
    | GetRoutingApplyEndpointResponse409
    | GetRoutingApplyEndpointResponse415
    | GetRoutingApplyEndpointResponse422
    | GetRoutingApplyEndpointResponse424
    | GetRoutingApplyEndpointResponse500
    | GetRoutingApplyEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Routing Apply.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRoutingApplyEndpointResponse400 | GetRoutingApplyEndpointResponse401 | GetRoutingApplyEndpointResponse403 | GetRoutingApplyEndpointResponse404 | GetRoutingApplyEndpointResponse405 | GetRoutingApplyEndpointResponse406 | GetRoutingApplyEndpointResponse409 | GetRoutingApplyEndpointResponse415 | GetRoutingApplyEndpointResponse422 | GetRoutingApplyEndpointResponse424 | GetRoutingApplyEndpointResponse500 | GetRoutingApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetRoutingApplyEndpointResponse400
    | GetRoutingApplyEndpointResponse401
    | GetRoutingApplyEndpointResponse403
    | GetRoutingApplyEndpointResponse404
    | GetRoutingApplyEndpointResponse405
    | GetRoutingApplyEndpointResponse406
    | GetRoutingApplyEndpointResponse409
    | GetRoutingApplyEndpointResponse415
    | GetRoutingApplyEndpointResponse422
    | GetRoutingApplyEndpointResponse424
    | GetRoutingApplyEndpointResponse500
    | GetRoutingApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Routing Apply.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRoutingApplyEndpointResponse400 | GetRoutingApplyEndpointResponse401 | GetRoutingApplyEndpointResponse403 | GetRoutingApplyEndpointResponse404 | GetRoutingApplyEndpointResponse405 | GetRoutingApplyEndpointResponse406 | GetRoutingApplyEndpointResponse409 | GetRoutingApplyEndpointResponse415 | GetRoutingApplyEndpointResponse422 | GetRoutingApplyEndpointResponse424 | GetRoutingApplyEndpointResponse500 | GetRoutingApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetRoutingApplyEndpointResponse400
    | GetRoutingApplyEndpointResponse401
    | GetRoutingApplyEndpointResponse403
    | GetRoutingApplyEndpointResponse404
    | GetRoutingApplyEndpointResponse405
    | GetRoutingApplyEndpointResponse406
    | GetRoutingApplyEndpointResponse409
    | GetRoutingApplyEndpointResponse415
    | GetRoutingApplyEndpointResponse422
    | GetRoutingApplyEndpointResponse424
    | GetRoutingApplyEndpointResponse500
    | GetRoutingApplyEndpointResponse503
]:
    """<h3>Description:</h3>Reads current Routing Apply.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRoutingApplyEndpointResponse400 | GetRoutingApplyEndpointResponse401 | GetRoutingApplyEndpointResponse403 | GetRoutingApplyEndpointResponse404 | GetRoutingApplyEndpointResponse405 | GetRoutingApplyEndpointResponse406 | GetRoutingApplyEndpointResponse409 | GetRoutingApplyEndpointResponse415 | GetRoutingApplyEndpointResponse422 | GetRoutingApplyEndpointResponse424 | GetRoutingApplyEndpointResponse500 | GetRoutingApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetRoutingApplyEndpointResponse400
    | GetRoutingApplyEndpointResponse401
    | GetRoutingApplyEndpointResponse403
    | GetRoutingApplyEndpointResponse404
    | GetRoutingApplyEndpointResponse405
    | GetRoutingApplyEndpointResponse406
    | GetRoutingApplyEndpointResponse409
    | GetRoutingApplyEndpointResponse415
    | GetRoutingApplyEndpointResponse422
    | GetRoutingApplyEndpointResponse424
    | GetRoutingApplyEndpointResponse500
    | GetRoutingApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current Routing Apply.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RoutingApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-routing-apply-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRoutingApplyEndpointResponse400 | GetRoutingApplyEndpointResponse401 | GetRoutingApplyEndpointResponse403 | GetRoutingApplyEndpointResponse404 | GetRoutingApplyEndpointResponse405 | GetRoutingApplyEndpointResponse406 | GetRoutingApplyEndpointResponse409 | GetRoutingApplyEndpointResponse415 | GetRoutingApplyEndpointResponse422 | GetRoutingApplyEndpointResponse424 | GetRoutingApplyEndpointResponse500 | GetRoutingApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
