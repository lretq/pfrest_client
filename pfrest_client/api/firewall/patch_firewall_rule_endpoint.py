from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_rule_endpoint_data_body import PatchFirewallRuleEndpointDataBody
from ...models.patch_firewall_rule_endpoint_json_body import PatchFirewallRuleEndpointJsonBody
from ...models.patch_firewall_rule_endpoint_response_400 import PatchFirewallRuleEndpointResponse400
from ...models.patch_firewall_rule_endpoint_response_401 import PatchFirewallRuleEndpointResponse401
from ...models.patch_firewall_rule_endpoint_response_403 import PatchFirewallRuleEndpointResponse403
from ...models.patch_firewall_rule_endpoint_response_404 import PatchFirewallRuleEndpointResponse404
from ...models.patch_firewall_rule_endpoint_response_405 import PatchFirewallRuleEndpointResponse405
from ...models.patch_firewall_rule_endpoint_response_406 import PatchFirewallRuleEndpointResponse406
from ...models.patch_firewall_rule_endpoint_response_409 import PatchFirewallRuleEndpointResponse409
from ...models.patch_firewall_rule_endpoint_response_415 import PatchFirewallRuleEndpointResponse415
from ...models.patch_firewall_rule_endpoint_response_422 import PatchFirewallRuleEndpointResponse422
from ...models.patch_firewall_rule_endpoint_response_424 import PatchFirewallRuleEndpointResponse424
from ...models.patch_firewall_rule_endpoint_response_500 import PatchFirewallRuleEndpointResponse500
from ...models.patch_firewall_rule_endpoint_response_503 import PatchFirewallRuleEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallRuleEndpointJsonBody | PatchFirewallRuleEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/rule",
    }

    if isinstance(body, PatchFirewallRuleEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallRuleEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallRuleEndpointResponse400
    | PatchFirewallRuleEndpointResponse401
    | PatchFirewallRuleEndpointResponse403
    | PatchFirewallRuleEndpointResponse404
    | PatchFirewallRuleEndpointResponse405
    | PatchFirewallRuleEndpointResponse406
    | PatchFirewallRuleEndpointResponse409
    | PatchFirewallRuleEndpointResponse415
    | PatchFirewallRuleEndpointResponse422
    | PatchFirewallRuleEndpointResponse424
    | PatchFirewallRuleEndpointResponse500
    | PatchFirewallRuleEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallRuleEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallRuleEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallRuleEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallRuleEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallRuleEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallRuleEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallRuleEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallRuleEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallRuleEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallRuleEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallRuleEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallRuleEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallRuleEndpointResponse400
    | PatchFirewallRuleEndpointResponse401
    | PatchFirewallRuleEndpointResponse403
    | PatchFirewallRuleEndpointResponse404
    | PatchFirewallRuleEndpointResponse405
    | PatchFirewallRuleEndpointResponse406
    | PatchFirewallRuleEndpointResponse409
    | PatchFirewallRuleEndpointResponse415
    | PatchFirewallRuleEndpointResponse422
    | PatchFirewallRuleEndpointResponse424
    | PatchFirewallRuleEndpointResponse500
    | PatchFirewallRuleEndpointResponse503
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
    body: PatchFirewallRuleEndpointJsonBody | PatchFirewallRuleEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallRuleEndpointResponse400
    | PatchFirewallRuleEndpointResponse401
    | PatchFirewallRuleEndpointResponse403
    | PatchFirewallRuleEndpointResponse404
    | PatchFirewallRuleEndpointResponse405
    | PatchFirewallRuleEndpointResponse406
    | PatchFirewallRuleEndpointResponse409
    | PatchFirewallRuleEndpointResponse415
    | PatchFirewallRuleEndpointResponse422
    | PatchFirewallRuleEndpointResponse424
    | PatchFirewallRuleEndpointResponse500
    | PatchFirewallRuleEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallRuleEndpointJsonBody | Unset):
        body (PatchFirewallRuleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallRuleEndpointResponse400 | PatchFirewallRuleEndpointResponse401 | PatchFirewallRuleEndpointResponse403 | PatchFirewallRuleEndpointResponse404 | PatchFirewallRuleEndpointResponse405 | PatchFirewallRuleEndpointResponse406 | PatchFirewallRuleEndpointResponse409 | PatchFirewallRuleEndpointResponse415 | PatchFirewallRuleEndpointResponse422 | PatchFirewallRuleEndpointResponse424 | PatchFirewallRuleEndpointResponse500 | PatchFirewallRuleEndpointResponse503]
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
    body: PatchFirewallRuleEndpointJsonBody | PatchFirewallRuleEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallRuleEndpointResponse400
    | PatchFirewallRuleEndpointResponse401
    | PatchFirewallRuleEndpointResponse403
    | PatchFirewallRuleEndpointResponse404
    | PatchFirewallRuleEndpointResponse405
    | PatchFirewallRuleEndpointResponse406
    | PatchFirewallRuleEndpointResponse409
    | PatchFirewallRuleEndpointResponse415
    | PatchFirewallRuleEndpointResponse422
    | PatchFirewallRuleEndpointResponse424
    | PatchFirewallRuleEndpointResponse500
    | PatchFirewallRuleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallRuleEndpointJsonBody | Unset):
        body (PatchFirewallRuleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallRuleEndpointResponse400 | PatchFirewallRuleEndpointResponse401 | PatchFirewallRuleEndpointResponse403 | PatchFirewallRuleEndpointResponse404 | PatchFirewallRuleEndpointResponse405 | PatchFirewallRuleEndpointResponse406 | PatchFirewallRuleEndpointResponse409 | PatchFirewallRuleEndpointResponse415 | PatchFirewallRuleEndpointResponse422 | PatchFirewallRuleEndpointResponse424 | PatchFirewallRuleEndpointResponse500 | PatchFirewallRuleEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallRuleEndpointJsonBody | PatchFirewallRuleEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallRuleEndpointResponse400
    | PatchFirewallRuleEndpointResponse401
    | PatchFirewallRuleEndpointResponse403
    | PatchFirewallRuleEndpointResponse404
    | PatchFirewallRuleEndpointResponse405
    | PatchFirewallRuleEndpointResponse406
    | PatchFirewallRuleEndpointResponse409
    | PatchFirewallRuleEndpointResponse415
    | PatchFirewallRuleEndpointResponse422
    | PatchFirewallRuleEndpointResponse424
    | PatchFirewallRuleEndpointResponse500
    | PatchFirewallRuleEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallRuleEndpointJsonBody | Unset):
        body (PatchFirewallRuleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallRuleEndpointResponse400 | PatchFirewallRuleEndpointResponse401 | PatchFirewallRuleEndpointResponse403 | PatchFirewallRuleEndpointResponse404 | PatchFirewallRuleEndpointResponse405 | PatchFirewallRuleEndpointResponse406 | PatchFirewallRuleEndpointResponse409 | PatchFirewallRuleEndpointResponse415 | PatchFirewallRuleEndpointResponse422 | PatchFirewallRuleEndpointResponse424 | PatchFirewallRuleEndpointResponse500 | PatchFirewallRuleEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallRuleEndpointJsonBody | PatchFirewallRuleEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallRuleEndpointResponse400
    | PatchFirewallRuleEndpointResponse401
    | PatchFirewallRuleEndpointResponse403
    | PatchFirewallRuleEndpointResponse404
    | PatchFirewallRuleEndpointResponse405
    | PatchFirewallRuleEndpointResponse406
    | PatchFirewallRuleEndpointResponse409
    | PatchFirewallRuleEndpointResponse415
    | PatchFirewallRuleEndpointResponse422
    | PatchFirewallRuleEndpointResponse424
    | PatchFirewallRuleEndpointResponse500
    | PatchFirewallRuleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallRuleEndpointJsonBody | Unset):
        body (PatchFirewallRuleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallRuleEndpointResponse400 | PatchFirewallRuleEndpointResponse401 | PatchFirewallRuleEndpointResponse403 | PatchFirewallRuleEndpointResponse404 | PatchFirewallRuleEndpointResponse405 | PatchFirewallRuleEndpointResponse406 | PatchFirewallRuleEndpointResponse409 | PatchFirewallRuleEndpointResponse415 | PatchFirewallRuleEndpointResponse422 | PatchFirewallRuleEndpointResponse424 | PatchFirewallRuleEndpointResponse500 | PatchFirewallRuleEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
