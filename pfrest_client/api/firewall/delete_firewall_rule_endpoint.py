from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_firewall_rule_endpoint_response_400 import DeleteFirewallRuleEndpointResponse400
from ...models.delete_firewall_rule_endpoint_response_401 import DeleteFirewallRuleEndpointResponse401
from ...models.delete_firewall_rule_endpoint_response_403 import DeleteFirewallRuleEndpointResponse403
from ...models.delete_firewall_rule_endpoint_response_404 import DeleteFirewallRuleEndpointResponse404
from ...models.delete_firewall_rule_endpoint_response_405 import DeleteFirewallRuleEndpointResponse405
from ...models.delete_firewall_rule_endpoint_response_406 import DeleteFirewallRuleEndpointResponse406
from ...models.delete_firewall_rule_endpoint_response_409 import DeleteFirewallRuleEndpointResponse409
from ...models.delete_firewall_rule_endpoint_response_415 import DeleteFirewallRuleEndpointResponse415
from ...models.delete_firewall_rule_endpoint_response_422 import DeleteFirewallRuleEndpointResponse422
from ...models.delete_firewall_rule_endpoint_response_424 import DeleteFirewallRuleEndpointResponse424
from ...models.delete_firewall_rule_endpoint_response_500 import DeleteFirewallRuleEndpointResponse500
from ...models.delete_firewall_rule_endpoint_response_503 import DeleteFirewallRuleEndpointResponse503
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
        "url": "/api/v2/firewall/rule",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteFirewallRuleEndpointResponse400
    | DeleteFirewallRuleEndpointResponse401
    | DeleteFirewallRuleEndpointResponse403
    | DeleteFirewallRuleEndpointResponse404
    | DeleteFirewallRuleEndpointResponse405
    | DeleteFirewallRuleEndpointResponse406
    | DeleteFirewallRuleEndpointResponse409
    | DeleteFirewallRuleEndpointResponse415
    | DeleteFirewallRuleEndpointResponse422
    | DeleteFirewallRuleEndpointResponse424
    | DeleteFirewallRuleEndpointResponse500
    | DeleteFirewallRuleEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteFirewallRuleEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteFirewallRuleEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteFirewallRuleEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteFirewallRuleEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteFirewallRuleEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteFirewallRuleEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteFirewallRuleEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteFirewallRuleEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteFirewallRuleEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteFirewallRuleEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteFirewallRuleEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteFirewallRuleEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteFirewallRuleEndpointResponse400
    | DeleteFirewallRuleEndpointResponse401
    | DeleteFirewallRuleEndpointResponse403
    | DeleteFirewallRuleEndpointResponse404
    | DeleteFirewallRuleEndpointResponse405
    | DeleteFirewallRuleEndpointResponse406
    | DeleteFirewallRuleEndpointResponse409
    | DeleteFirewallRuleEndpointResponse415
    | DeleteFirewallRuleEndpointResponse422
    | DeleteFirewallRuleEndpointResponse424
    | DeleteFirewallRuleEndpointResponse500
    | DeleteFirewallRuleEndpointResponse503
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
    DeleteFirewallRuleEndpointResponse400
    | DeleteFirewallRuleEndpointResponse401
    | DeleteFirewallRuleEndpointResponse403
    | DeleteFirewallRuleEndpointResponse404
    | DeleteFirewallRuleEndpointResponse405
    | DeleteFirewallRuleEndpointResponse406
    | DeleteFirewallRuleEndpointResponse409
    | DeleteFirewallRuleEndpointResponse415
    | DeleteFirewallRuleEndpointResponse422
    | DeleteFirewallRuleEndpointResponse424
    | DeleteFirewallRuleEndpointResponse500
    | DeleteFirewallRuleEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallRuleEndpointResponse400 | DeleteFirewallRuleEndpointResponse401 | DeleteFirewallRuleEndpointResponse403 | DeleteFirewallRuleEndpointResponse404 | DeleteFirewallRuleEndpointResponse405 | DeleteFirewallRuleEndpointResponse406 | DeleteFirewallRuleEndpointResponse409 | DeleteFirewallRuleEndpointResponse415 | DeleteFirewallRuleEndpointResponse422 | DeleteFirewallRuleEndpointResponse424 | DeleteFirewallRuleEndpointResponse500 | DeleteFirewallRuleEndpointResponse503]
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
    DeleteFirewallRuleEndpointResponse400
    | DeleteFirewallRuleEndpointResponse401
    | DeleteFirewallRuleEndpointResponse403
    | DeleteFirewallRuleEndpointResponse404
    | DeleteFirewallRuleEndpointResponse405
    | DeleteFirewallRuleEndpointResponse406
    | DeleteFirewallRuleEndpointResponse409
    | DeleteFirewallRuleEndpointResponse415
    | DeleteFirewallRuleEndpointResponse422
    | DeleteFirewallRuleEndpointResponse424
    | DeleteFirewallRuleEndpointResponse500
    | DeleteFirewallRuleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallRuleEndpointResponse400 | DeleteFirewallRuleEndpointResponse401 | DeleteFirewallRuleEndpointResponse403 | DeleteFirewallRuleEndpointResponse404 | DeleteFirewallRuleEndpointResponse405 | DeleteFirewallRuleEndpointResponse406 | DeleteFirewallRuleEndpointResponse409 | DeleteFirewallRuleEndpointResponse415 | DeleteFirewallRuleEndpointResponse422 | DeleteFirewallRuleEndpointResponse424 | DeleteFirewallRuleEndpointResponse500 | DeleteFirewallRuleEndpointResponse503
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
    DeleteFirewallRuleEndpointResponse400
    | DeleteFirewallRuleEndpointResponse401
    | DeleteFirewallRuleEndpointResponse403
    | DeleteFirewallRuleEndpointResponse404
    | DeleteFirewallRuleEndpointResponse405
    | DeleteFirewallRuleEndpointResponse406
    | DeleteFirewallRuleEndpointResponse409
    | DeleteFirewallRuleEndpointResponse415
    | DeleteFirewallRuleEndpointResponse422
    | DeleteFirewallRuleEndpointResponse424
    | DeleteFirewallRuleEndpointResponse500
    | DeleteFirewallRuleEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallRuleEndpointResponse400 | DeleteFirewallRuleEndpointResponse401 | DeleteFirewallRuleEndpointResponse403 | DeleteFirewallRuleEndpointResponse404 | DeleteFirewallRuleEndpointResponse405 | DeleteFirewallRuleEndpointResponse406 | DeleteFirewallRuleEndpointResponse409 | DeleteFirewallRuleEndpointResponse415 | DeleteFirewallRuleEndpointResponse422 | DeleteFirewallRuleEndpointResponse424 | DeleteFirewallRuleEndpointResponse500 | DeleteFirewallRuleEndpointResponse503]
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
    DeleteFirewallRuleEndpointResponse400
    | DeleteFirewallRuleEndpointResponse401
    | DeleteFirewallRuleEndpointResponse403
    | DeleteFirewallRuleEndpointResponse404
    | DeleteFirewallRuleEndpointResponse405
    | DeleteFirewallRuleEndpointResponse406
    | DeleteFirewallRuleEndpointResponse409
    | DeleteFirewallRuleEndpointResponse415
    | DeleteFirewallRuleEndpointResponse422
    | DeleteFirewallRuleEndpointResponse424
    | DeleteFirewallRuleEndpointResponse500
    | DeleteFirewallRuleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallRuleEndpointResponse400 | DeleteFirewallRuleEndpointResponse401 | DeleteFirewallRuleEndpointResponse403 | DeleteFirewallRuleEndpointResponse404 | DeleteFirewallRuleEndpointResponse405 | DeleteFirewallRuleEndpointResponse406 | DeleteFirewallRuleEndpointResponse409 | DeleteFirewallRuleEndpointResponse415 | DeleteFirewallRuleEndpointResponse422 | DeleteFirewallRuleEndpointResponse424 | DeleteFirewallRuleEndpointResponse500 | DeleteFirewallRuleEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
