from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_firewall_state_endpoint_response_400 import DeleteFirewallStateEndpointResponse400
from ...models.delete_firewall_state_endpoint_response_401 import DeleteFirewallStateEndpointResponse401
from ...models.delete_firewall_state_endpoint_response_403 import DeleteFirewallStateEndpointResponse403
from ...models.delete_firewall_state_endpoint_response_404 import DeleteFirewallStateEndpointResponse404
from ...models.delete_firewall_state_endpoint_response_405 import DeleteFirewallStateEndpointResponse405
from ...models.delete_firewall_state_endpoint_response_406 import DeleteFirewallStateEndpointResponse406
from ...models.delete_firewall_state_endpoint_response_409 import DeleteFirewallStateEndpointResponse409
from ...models.delete_firewall_state_endpoint_response_415 import DeleteFirewallStateEndpointResponse415
from ...models.delete_firewall_state_endpoint_response_422 import DeleteFirewallStateEndpointResponse422
from ...models.delete_firewall_state_endpoint_response_424 import DeleteFirewallStateEndpointResponse424
from ...models.delete_firewall_state_endpoint_response_500 import DeleteFirewallStateEndpointResponse500
from ...models.delete_firewall_state_endpoint_response_503 import DeleteFirewallStateEndpointResponse503
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
        "url": "/api/v2/firewall/state",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteFirewallStateEndpointResponse400
    | DeleteFirewallStateEndpointResponse401
    | DeleteFirewallStateEndpointResponse403
    | DeleteFirewallStateEndpointResponse404
    | DeleteFirewallStateEndpointResponse405
    | DeleteFirewallStateEndpointResponse406
    | DeleteFirewallStateEndpointResponse409
    | DeleteFirewallStateEndpointResponse415
    | DeleteFirewallStateEndpointResponse422
    | DeleteFirewallStateEndpointResponse424
    | DeleteFirewallStateEndpointResponse500
    | DeleteFirewallStateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteFirewallStateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteFirewallStateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteFirewallStateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteFirewallStateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteFirewallStateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteFirewallStateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteFirewallStateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteFirewallStateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteFirewallStateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteFirewallStateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteFirewallStateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteFirewallStateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteFirewallStateEndpointResponse400
    | DeleteFirewallStateEndpointResponse401
    | DeleteFirewallStateEndpointResponse403
    | DeleteFirewallStateEndpointResponse404
    | DeleteFirewallStateEndpointResponse405
    | DeleteFirewallStateEndpointResponse406
    | DeleteFirewallStateEndpointResponse409
    | DeleteFirewallStateEndpointResponse415
    | DeleteFirewallStateEndpointResponse422
    | DeleteFirewallStateEndpointResponse424
    | DeleteFirewallStateEndpointResponse500
    | DeleteFirewallStateEndpointResponse503
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
    DeleteFirewallStateEndpointResponse400
    | DeleteFirewallStateEndpointResponse401
    | DeleteFirewallStateEndpointResponse403
    | DeleteFirewallStateEndpointResponse404
    | DeleteFirewallStateEndpointResponse405
    | DeleteFirewallStateEndpointResponse406
    | DeleteFirewallStateEndpointResponse409
    | DeleteFirewallStateEndpointResponse415
    | DeleteFirewallStateEndpointResponse422
    | DeleteFirewallStateEndpointResponse424
    | DeleteFirewallStateEndpointResponse500
    | DeleteFirewallStateEndpointResponse503
]:
    """<h3>Description:</h3>Please use the /api/v2/firewall/states endpoint with a query to kill the state
    you are looking for.<br><br>Kills an existing Firewall State. Please note that the firewall state
    table changes very quickly which may result in the state's `id` suddenly changing. Use caution when
    deleting states.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallState<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported
    authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all,
    api-v2-firewall-state-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallStateEndpointResponse400 | DeleteFirewallStateEndpointResponse401 | DeleteFirewallStateEndpointResponse403 | DeleteFirewallStateEndpointResponse404 | DeleteFirewallStateEndpointResponse405 | DeleteFirewallStateEndpointResponse406 | DeleteFirewallStateEndpointResponse409 | DeleteFirewallStateEndpointResponse415 | DeleteFirewallStateEndpointResponse422 | DeleteFirewallStateEndpointResponse424 | DeleteFirewallStateEndpointResponse500 | DeleteFirewallStateEndpointResponse503]
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
    DeleteFirewallStateEndpointResponse400
    | DeleteFirewallStateEndpointResponse401
    | DeleteFirewallStateEndpointResponse403
    | DeleteFirewallStateEndpointResponse404
    | DeleteFirewallStateEndpointResponse405
    | DeleteFirewallStateEndpointResponse406
    | DeleteFirewallStateEndpointResponse409
    | DeleteFirewallStateEndpointResponse415
    | DeleteFirewallStateEndpointResponse422
    | DeleteFirewallStateEndpointResponse424
    | DeleteFirewallStateEndpointResponse500
    | DeleteFirewallStateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Please use the /api/v2/firewall/states endpoint with a query to kill the state
    you are looking for.<br><br>Kills an existing Firewall State. Please note that the firewall state
    table changes very quickly which may result in the state's `id` suddenly changing. Use caution when
    deleting states.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallState<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported
    authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all,
    api-v2-firewall-state-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallStateEndpointResponse400 | DeleteFirewallStateEndpointResponse401 | DeleteFirewallStateEndpointResponse403 | DeleteFirewallStateEndpointResponse404 | DeleteFirewallStateEndpointResponse405 | DeleteFirewallStateEndpointResponse406 | DeleteFirewallStateEndpointResponse409 | DeleteFirewallStateEndpointResponse415 | DeleteFirewallStateEndpointResponse422 | DeleteFirewallStateEndpointResponse424 | DeleteFirewallStateEndpointResponse500 | DeleteFirewallStateEndpointResponse503
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
    DeleteFirewallStateEndpointResponse400
    | DeleteFirewallStateEndpointResponse401
    | DeleteFirewallStateEndpointResponse403
    | DeleteFirewallStateEndpointResponse404
    | DeleteFirewallStateEndpointResponse405
    | DeleteFirewallStateEndpointResponse406
    | DeleteFirewallStateEndpointResponse409
    | DeleteFirewallStateEndpointResponse415
    | DeleteFirewallStateEndpointResponse422
    | DeleteFirewallStateEndpointResponse424
    | DeleteFirewallStateEndpointResponse500
    | DeleteFirewallStateEndpointResponse503
]:
    """<h3>Description:</h3>Please use the /api/v2/firewall/states endpoint with a query to kill the state
    you are looking for.<br><br>Kills an existing Firewall State. Please note that the firewall state
    table changes very quickly which may result in the state's `id` suddenly changing. Use caution when
    deleting states.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallState<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported
    authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all,
    api-v2-firewall-state-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallStateEndpointResponse400 | DeleteFirewallStateEndpointResponse401 | DeleteFirewallStateEndpointResponse403 | DeleteFirewallStateEndpointResponse404 | DeleteFirewallStateEndpointResponse405 | DeleteFirewallStateEndpointResponse406 | DeleteFirewallStateEndpointResponse409 | DeleteFirewallStateEndpointResponse415 | DeleteFirewallStateEndpointResponse422 | DeleteFirewallStateEndpointResponse424 | DeleteFirewallStateEndpointResponse500 | DeleteFirewallStateEndpointResponse503]
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
    DeleteFirewallStateEndpointResponse400
    | DeleteFirewallStateEndpointResponse401
    | DeleteFirewallStateEndpointResponse403
    | DeleteFirewallStateEndpointResponse404
    | DeleteFirewallStateEndpointResponse405
    | DeleteFirewallStateEndpointResponse406
    | DeleteFirewallStateEndpointResponse409
    | DeleteFirewallStateEndpointResponse415
    | DeleteFirewallStateEndpointResponse422
    | DeleteFirewallStateEndpointResponse424
    | DeleteFirewallStateEndpointResponse500
    | DeleteFirewallStateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Please use the /api/v2/firewall/states endpoint with a query to kill the state
    you are looking for.<br><br>Kills an existing Firewall State. Please note that the firewall state
    table changes very quickly which may result in the state's `id` suddenly changing. Use caution when
    deleting states.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallState<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported
    authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all,
    api-v2-firewall-state-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallStateEndpointResponse400 | DeleteFirewallStateEndpointResponse401 | DeleteFirewallStateEndpointResponse403 | DeleteFirewallStateEndpointResponse404 | DeleteFirewallStateEndpointResponse405 | DeleteFirewallStateEndpointResponse406 | DeleteFirewallStateEndpointResponse409 | DeleteFirewallStateEndpointResponse415 | DeleteFirewallStateEndpointResponse422 | DeleteFirewallStateEndpointResponse424 | DeleteFirewallStateEndpointResponse500 | DeleteFirewallStateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
