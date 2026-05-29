from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_routing_gateway_group_priority_endpoint_data_body import (
    PatchRoutingGatewayGroupPriorityEndpointDataBody,
)
from ...models.patch_routing_gateway_group_priority_endpoint_json_body import (
    PatchRoutingGatewayGroupPriorityEndpointJsonBody,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_400 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse400,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_401 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse401,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_403 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse403,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_404 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse404,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_405 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse405,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_406 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse406,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_409 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse409,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_415 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse415,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_422 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse422,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_424 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse424,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_500 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse500,
)
from ...models.patch_routing_gateway_group_priority_endpoint_response_503 import (
    PatchRoutingGatewayGroupPriorityEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchRoutingGatewayGroupPriorityEndpointJsonBody
    | PatchRoutingGatewayGroupPriorityEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/routing/gateway/group/priority",
    }

    if isinstance(body, PatchRoutingGatewayGroupPriorityEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchRoutingGatewayGroupPriorityEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchRoutingGatewayGroupPriorityEndpointResponse400
    | PatchRoutingGatewayGroupPriorityEndpointResponse401
    | PatchRoutingGatewayGroupPriorityEndpointResponse403
    | PatchRoutingGatewayGroupPriorityEndpointResponse404
    | PatchRoutingGatewayGroupPriorityEndpointResponse405
    | PatchRoutingGatewayGroupPriorityEndpointResponse406
    | PatchRoutingGatewayGroupPriorityEndpointResponse409
    | PatchRoutingGatewayGroupPriorityEndpointResponse415
    | PatchRoutingGatewayGroupPriorityEndpointResponse422
    | PatchRoutingGatewayGroupPriorityEndpointResponse424
    | PatchRoutingGatewayGroupPriorityEndpointResponse500
    | PatchRoutingGatewayGroupPriorityEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchRoutingGatewayGroupPriorityEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchRoutingGatewayGroupPriorityEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchRoutingGatewayGroupPriorityEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchRoutingGatewayGroupPriorityEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchRoutingGatewayGroupPriorityEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchRoutingGatewayGroupPriorityEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchRoutingGatewayGroupPriorityEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchRoutingGatewayGroupPriorityEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchRoutingGatewayGroupPriorityEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchRoutingGatewayGroupPriorityEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchRoutingGatewayGroupPriorityEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchRoutingGatewayGroupPriorityEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchRoutingGatewayGroupPriorityEndpointResponse400
    | PatchRoutingGatewayGroupPriorityEndpointResponse401
    | PatchRoutingGatewayGroupPriorityEndpointResponse403
    | PatchRoutingGatewayGroupPriorityEndpointResponse404
    | PatchRoutingGatewayGroupPriorityEndpointResponse405
    | PatchRoutingGatewayGroupPriorityEndpointResponse406
    | PatchRoutingGatewayGroupPriorityEndpointResponse409
    | PatchRoutingGatewayGroupPriorityEndpointResponse415
    | PatchRoutingGatewayGroupPriorityEndpointResponse422
    | PatchRoutingGatewayGroupPriorityEndpointResponse424
    | PatchRoutingGatewayGroupPriorityEndpointResponse500
    | PatchRoutingGatewayGroupPriorityEndpointResponse503
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
    body: PatchRoutingGatewayGroupPriorityEndpointJsonBody
    | PatchRoutingGatewayGroupPriorityEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchRoutingGatewayGroupPriorityEndpointResponse400
    | PatchRoutingGatewayGroupPriorityEndpointResponse401
    | PatchRoutingGatewayGroupPriorityEndpointResponse403
    | PatchRoutingGatewayGroupPriorityEndpointResponse404
    | PatchRoutingGatewayGroupPriorityEndpointResponse405
    | PatchRoutingGatewayGroupPriorityEndpointResponse406
    | PatchRoutingGatewayGroupPriorityEndpointResponse409
    | PatchRoutingGatewayGroupPriorityEndpointResponse415
    | PatchRoutingGatewayGroupPriorityEndpointResponse422
    | PatchRoutingGatewayGroupPriorityEndpointResponse424
    | PatchRoutingGatewayGroupPriorityEndpointResponse500
    | PatchRoutingGatewayGroupPriorityEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Routing Gateway Group
    Priority.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-routing-gateway-group-priority-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayGroupPriorityEndpointJsonBody | Unset):
        body (PatchRoutingGatewayGroupPriorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchRoutingGatewayGroupPriorityEndpointResponse400 | PatchRoutingGatewayGroupPriorityEndpointResponse401 | PatchRoutingGatewayGroupPriorityEndpointResponse403 | PatchRoutingGatewayGroupPriorityEndpointResponse404 | PatchRoutingGatewayGroupPriorityEndpointResponse405 | PatchRoutingGatewayGroupPriorityEndpointResponse406 | PatchRoutingGatewayGroupPriorityEndpointResponse409 | PatchRoutingGatewayGroupPriorityEndpointResponse415 | PatchRoutingGatewayGroupPriorityEndpointResponse422 | PatchRoutingGatewayGroupPriorityEndpointResponse424 | PatchRoutingGatewayGroupPriorityEndpointResponse500 | PatchRoutingGatewayGroupPriorityEndpointResponse503]
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
    body: PatchRoutingGatewayGroupPriorityEndpointJsonBody
    | PatchRoutingGatewayGroupPriorityEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchRoutingGatewayGroupPriorityEndpointResponse400
    | PatchRoutingGatewayGroupPriorityEndpointResponse401
    | PatchRoutingGatewayGroupPriorityEndpointResponse403
    | PatchRoutingGatewayGroupPriorityEndpointResponse404
    | PatchRoutingGatewayGroupPriorityEndpointResponse405
    | PatchRoutingGatewayGroupPriorityEndpointResponse406
    | PatchRoutingGatewayGroupPriorityEndpointResponse409
    | PatchRoutingGatewayGroupPriorityEndpointResponse415
    | PatchRoutingGatewayGroupPriorityEndpointResponse422
    | PatchRoutingGatewayGroupPriorityEndpointResponse424
    | PatchRoutingGatewayGroupPriorityEndpointResponse500
    | PatchRoutingGatewayGroupPriorityEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Routing Gateway Group
    Priority.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-routing-gateway-group-priority-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayGroupPriorityEndpointJsonBody | Unset):
        body (PatchRoutingGatewayGroupPriorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchRoutingGatewayGroupPriorityEndpointResponse400 | PatchRoutingGatewayGroupPriorityEndpointResponse401 | PatchRoutingGatewayGroupPriorityEndpointResponse403 | PatchRoutingGatewayGroupPriorityEndpointResponse404 | PatchRoutingGatewayGroupPriorityEndpointResponse405 | PatchRoutingGatewayGroupPriorityEndpointResponse406 | PatchRoutingGatewayGroupPriorityEndpointResponse409 | PatchRoutingGatewayGroupPriorityEndpointResponse415 | PatchRoutingGatewayGroupPriorityEndpointResponse422 | PatchRoutingGatewayGroupPriorityEndpointResponse424 | PatchRoutingGatewayGroupPriorityEndpointResponse500 | PatchRoutingGatewayGroupPriorityEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingGatewayGroupPriorityEndpointJsonBody
    | PatchRoutingGatewayGroupPriorityEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchRoutingGatewayGroupPriorityEndpointResponse400
    | PatchRoutingGatewayGroupPriorityEndpointResponse401
    | PatchRoutingGatewayGroupPriorityEndpointResponse403
    | PatchRoutingGatewayGroupPriorityEndpointResponse404
    | PatchRoutingGatewayGroupPriorityEndpointResponse405
    | PatchRoutingGatewayGroupPriorityEndpointResponse406
    | PatchRoutingGatewayGroupPriorityEndpointResponse409
    | PatchRoutingGatewayGroupPriorityEndpointResponse415
    | PatchRoutingGatewayGroupPriorityEndpointResponse422
    | PatchRoutingGatewayGroupPriorityEndpointResponse424
    | PatchRoutingGatewayGroupPriorityEndpointResponse500
    | PatchRoutingGatewayGroupPriorityEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Routing Gateway Group
    Priority.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-routing-gateway-group-priority-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayGroupPriorityEndpointJsonBody | Unset):
        body (PatchRoutingGatewayGroupPriorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchRoutingGatewayGroupPriorityEndpointResponse400 | PatchRoutingGatewayGroupPriorityEndpointResponse401 | PatchRoutingGatewayGroupPriorityEndpointResponse403 | PatchRoutingGatewayGroupPriorityEndpointResponse404 | PatchRoutingGatewayGroupPriorityEndpointResponse405 | PatchRoutingGatewayGroupPriorityEndpointResponse406 | PatchRoutingGatewayGroupPriorityEndpointResponse409 | PatchRoutingGatewayGroupPriorityEndpointResponse415 | PatchRoutingGatewayGroupPriorityEndpointResponse422 | PatchRoutingGatewayGroupPriorityEndpointResponse424 | PatchRoutingGatewayGroupPriorityEndpointResponse500 | PatchRoutingGatewayGroupPriorityEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchRoutingGatewayGroupPriorityEndpointJsonBody
    | PatchRoutingGatewayGroupPriorityEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchRoutingGatewayGroupPriorityEndpointResponse400
    | PatchRoutingGatewayGroupPriorityEndpointResponse401
    | PatchRoutingGatewayGroupPriorityEndpointResponse403
    | PatchRoutingGatewayGroupPriorityEndpointResponse404
    | PatchRoutingGatewayGroupPriorityEndpointResponse405
    | PatchRoutingGatewayGroupPriorityEndpointResponse406
    | PatchRoutingGatewayGroupPriorityEndpointResponse409
    | PatchRoutingGatewayGroupPriorityEndpointResponse415
    | PatchRoutingGatewayGroupPriorityEndpointResponse422
    | PatchRoutingGatewayGroupPriorityEndpointResponse424
    | PatchRoutingGatewayGroupPriorityEndpointResponse500
    | PatchRoutingGatewayGroupPriorityEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Routing Gateway Group
    Priority.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    RoutingGatewayGroupPriority<br>**Parent model**: RoutingGatewayGroup<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-routing-gateway-group-priority-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchRoutingGatewayGroupPriorityEndpointJsonBody | Unset):
        body (PatchRoutingGatewayGroupPriorityEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchRoutingGatewayGroupPriorityEndpointResponse400 | PatchRoutingGatewayGroupPriorityEndpointResponse401 | PatchRoutingGatewayGroupPriorityEndpointResponse403 | PatchRoutingGatewayGroupPriorityEndpointResponse404 | PatchRoutingGatewayGroupPriorityEndpointResponse405 | PatchRoutingGatewayGroupPriorityEndpointResponse406 | PatchRoutingGatewayGroupPriorityEndpointResponse409 | PatchRoutingGatewayGroupPriorityEndpointResponse415 | PatchRoutingGatewayGroupPriorityEndpointResponse422 | PatchRoutingGatewayGroupPriorityEndpointResponse424 | PatchRoutingGatewayGroupPriorityEndpointResponse500 | PatchRoutingGatewayGroupPriorityEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
