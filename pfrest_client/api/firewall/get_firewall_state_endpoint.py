from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_firewall_state_endpoint_response_400 import GetFirewallStateEndpointResponse400
from ...models.get_firewall_state_endpoint_response_401 import GetFirewallStateEndpointResponse401
from ...models.get_firewall_state_endpoint_response_403 import GetFirewallStateEndpointResponse403
from ...models.get_firewall_state_endpoint_response_404 import GetFirewallStateEndpointResponse404
from ...models.get_firewall_state_endpoint_response_405 import GetFirewallStateEndpointResponse405
from ...models.get_firewall_state_endpoint_response_406 import GetFirewallStateEndpointResponse406
from ...models.get_firewall_state_endpoint_response_409 import GetFirewallStateEndpointResponse409
from ...models.get_firewall_state_endpoint_response_415 import GetFirewallStateEndpointResponse415
from ...models.get_firewall_state_endpoint_response_422 import GetFirewallStateEndpointResponse422
from ...models.get_firewall_state_endpoint_response_424 import GetFirewallStateEndpointResponse424
from ...models.get_firewall_state_endpoint_response_500 import GetFirewallStateEndpointResponse500
from ...models.get_firewall_state_endpoint_response_503 import GetFirewallStateEndpointResponse503
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
        "method": "get",
        "url": "/api/v2/firewall/state",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFirewallStateEndpointResponse400
    | GetFirewallStateEndpointResponse401
    | GetFirewallStateEndpointResponse403
    | GetFirewallStateEndpointResponse404
    | GetFirewallStateEndpointResponse405
    | GetFirewallStateEndpointResponse406
    | GetFirewallStateEndpointResponse409
    | GetFirewallStateEndpointResponse415
    | GetFirewallStateEndpointResponse422
    | GetFirewallStateEndpointResponse424
    | GetFirewallStateEndpointResponse500
    | GetFirewallStateEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetFirewallStateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFirewallStateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetFirewallStateEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetFirewallStateEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetFirewallStateEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetFirewallStateEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetFirewallStateEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetFirewallStateEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetFirewallStateEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetFirewallStateEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetFirewallStateEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetFirewallStateEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFirewallStateEndpointResponse400
    | GetFirewallStateEndpointResponse401
    | GetFirewallStateEndpointResponse403
    | GetFirewallStateEndpointResponse404
    | GetFirewallStateEndpointResponse405
    | GetFirewallStateEndpointResponse406
    | GetFirewallStateEndpointResponse409
    | GetFirewallStateEndpointResponse415
    | GetFirewallStateEndpointResponse422
    | GetFirewallStateEndpointResponse424
    | GetFirewallStateEndpointResponse500
    | GetFirewallStateEndpointResponse503
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
    GetFirewallStateEndpointResponse400
    | GetFirewallStateEndpointResponse401
    | GetFirewallStateEndpointResponse403
    | GetFirewallStateEndpointResponse404
    | GetFirewallStateEndpointResponse405
    | GetFirewallStateEndpointResponse406
    | GetFirewallStateEndpointResponse409
    | GetFirewallStateEndpointResponse415
    | GetFirewallStateEndpointResponse422
    | GetFirewallStateEndpointResponse424
    | GetFirewallStateEndpointResponse500
    | GetFirewallStateEndpointResponse503
]:
    """<h3>Description:</h3>Please use the /api/v2/firewall/states endpoint with a query to find the state
    you are looking for.<br><br>Reads an existing Firewall State. Please note that the firewall state
    table changes very quickly which may result in the state's `id` suddenly changing. It is recommended
    to use the /api/v2/firewall/states endpoint with a query to find the state you are looking
    for.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallState<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported
    authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all,
    api-v2-firewall-state-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallStateEndpointResponse400 | GetFirewallStateEndpointResponse401 | GetFirewallStateEndpointResponse403 | GetFirewallStateEndpointResponse404 | GetFirewallStateEndpointResponse405 | GetFirewallStateEndpointResponse406 | GetFirewallStateEndpointResponse409 | GetFirewallStateEndpointResponse415 | GetFirewallStateEndpointResponse422 | GetFirewallStateEndpointResponse424 | GetFirewallStateEndpointResponse500 | GetFirewallStateEndpointResponse503]
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
    GetFirewallStateEndpointResponse400
    | GetFirewallStateEndpointResponse401
    | GetFirewallStateEndpointResponse403
    | GetFirewallStateEndpointResponse404
    | GetFirewallStateEndpointResponse405
    | GetFirewallStateEndpointResponse406
    | GetFirewallStateEndpointResponse409
    | GetFirewallStateEndpointResponse415
    | GetFirewallStateEndpointResponse422
    | GetFirewallStateEndpointResponse424
    | GetFirewallStateEndpointResponse500
    | GetFirewallStateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Please use the /api/v2/firewall/states endpoint with a query to find the state
    you are looking for.<br><br>Reads an existing Firewall State. Please note that the firewall state
    table changes very quickly which may result in the state's `id` suddenly changing. It is recommended
    to use the /api/v2/firewall/states endpoint with a query to find the state you are looking
    for.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallState<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported
    authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all,
    api-v2-firewall-state-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallStateEndpointResponse400 | GetFirewallStateEndpointResponse401 | GetFirewallStateEndpointResponse403 | GetFirewallStateEndpointResponse404 | GetFirewallStateEndpointResponse405 | GetFirewallStateEndpointResponse406 | GetFirewallStateEndpointResponse409 | GetFirewallStateEndpointResponse415 | GetFirewallStateEndpointResponse422 | GetFirewallStateEndpointResponse424 | GetFirewallStateEndpointResponse500 | GetFirewallStateEndpointResponse503
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
    GetFirewallStateEndpointResponse400
    | GetFirewallStateEndpointResponse401
    | GetFirewallStateEndpointResponse403
    | GetFirewallStateEndpointResponse404
    | GetFirewallStateEndpointResponse405
    | GetFirewallStateEndpointResponse406
    | GetFirewallStateEndpointResponse409
    | GetFirewallStateEndpointResponse415
    | GetFirewallStateEndpointResponse422
    | GetFirewallStateEndpointResponse424
    | GetFirewallStateEndpointResponse500
    | GetFirewallStateEndpointResponse503
]:
    """<h3>Description:</h3>Please use the /api/v2/firewall/states endpoint with a query to find the state
    you are looking for.<br><br>Reads an existing Firewall State. Please note that the firewall state
    table changes very quickly which may result in the state's `id` suddenly changing. It is recommended
    to use the /api/v2/firewall/states endpoint with a query to find the state you are looking
    for.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallState<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported
    authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all,
    api-v2-firewall-state-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFirewallStateEndpointResponse400 | GetFirewallStateEndpointResponse401 | GetFirewallStateEndpointResponse403 | GetFirewallStateEndpointResponse404 | GetFirewallStateEndpointResponse405 | GetFirewallStateEndpointResponse406 | GetFirewallStateEndpointResponse409 | GetFirewallStateEndpointResponse415 | GetFirewallStateEndpointResponse422 | GetFirewallStateEndpointResponse424 | GetFirewallStateEndpointResponse500 | GetFirewallStateEndpointResponse503]
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
    GetFirewallStateEndpointResponse400
    | GetFirewallStateEndpointResponse401
    | GetFirewallStateEndpointResponse403
    | GetFirewallStateEndpointResponse404
    | GetFirewallStateEndpointResponse405
    | GetFirewallStateEndpointResponse406
    | GetFirewallStateEndpointResponse409
    | GetFirewallStateEndpointResponse415
    | GetFirewallStateEndpointResponse422
    | GetFirewallStateEndpointResponse424
    | GetFirewallStateEndpointResponse500
    | GetFirewallStateEndpointResponse503
    | None
):
    """<h3>Description:</h3>Please use the /api/v2/firewall/states endpoint with a query to find the state
    you are looking for.<br><br>Reads an existing Firewall State. Please note that the firewall state
    table changes very quickly which may result in the state's `id` suddenly changing. It is recommended
    to use the /api/v2/firewall/states endpoint with a query to find the state you are looking
    for.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallState<br>**Parent model**: None<br>**Requires authentication**: Yes<br>**Supported
    authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all,
    api-v2-firewall-state-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFirewallStateEndpointResponse400 | GetFirewallStateEndpointResponse401 | GetFirewallStateEndpointResponse403 | GetFirewallStateEndpointResponse404 | GetFirewallStateEndpointResponse405 | GetFirewallStateEndpointResponse406 | GetFirewallStateEndpointResponse409 | GetFirewallStateEndpointResponse415 | GetFirewallStateEndpointResponse422 | GetFirewallStateEndpointResponse424 | GetFirewallStateEndpointResponse500 | GetFirewallStateEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
