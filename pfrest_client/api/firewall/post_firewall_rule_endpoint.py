from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_rule_endpoint_data_body import PostFirewallRuleEndpointDataBody
from ...models.post_firewall_rule_endpoint_json_body import PostFirewallRuleEndpointJsonBody
from ...models.post_firewall_rule_endpoint_response_400 import PostFirewallRuleEndpointResponse400
from ...models.post_firewall_rule_endpoint_response_401 import PostFirewallRuleEndpointResponse401
from ...models.post_firewall_rule_endpoint_response_403 import PostFirewallRuleEndpointResponse403
from ...models.post_firewall_rule_endpoint_response_404 import PostFirewallRuleEndpointResponse404
from ...models.post_firewall_rule_endpoint_response_405 import PostFirewallRuleEndpointResponse405
from ...models.post_firewall_rule_endpoint_response_406 import PostFirewallRuleEndpointResponse406
from ...models.post_firewall_rule_endpoint_response_409 import PostFirewallRuleEndpointResponse409
from ...models.post_firewall_rule_endpoint_response_415 import PostFirewallRuleEndpointResponse415
from ...models.post_firewall_rule_endpoint_response_422 import PostFirewallRuleEndpointResponse422
from ...models.post_firewall_rule_endpoint_response_424 import PostFirewallRuleEndpointResponse424
from ...models.post_firewall_rule_endpoint_response_500 import PostFirewallRuleEndpointResponse500
from ...models.post_firewall_rule_endpoint_response_503 import PostFirewallRuleEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallRuleEndpointJsonBody | PostFirewallRuleEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/rule",
    }

    if isinstance(body, PostFirewallRuleEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallRuleEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallRuleEndpointResponse400
    | PostFirewallRuleEndpointResponse401
    | PostFirewallRuleEndpointResponse403
    | PostFirewallRuleEndpointResponse404
    | PostFirewallRuleEndpointResponse405
    | PostFirewallRuleEndpointResponse406
    | PostFirewallRuleEndpointResponse409
    | PostFirewallRuleEndpointResponse415
    | PostFirewallRuleEndpointResponse422
    | PostFirewallRuleEndpointResponse424
    | PostFirewallRuleEndpointResponse500
    | PostFirewallRuleEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallRuleEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallRuleEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallRuleEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallRuleEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallRuleEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallRuleEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallRuleEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallRuleEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallRuleEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallRuleEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallRuleEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallRuleEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallRuleEndpointResponse400
    | PostFirewallRuleEndpointResponse401
    | PostFirewallRuleEndpointResponse403
    | PostFirewallRuleEndpointResponse404
    | PostFirewallRuleEndpointResponse405
    | PostFirewallRuleEndpointResponse406
    | PostFirewallRuleEndpointResponse409
    | PostFirewallRuleEndpointResponse415
    | PostFirewallRuleEndpointResponse422
    | PostFirewallRuleEndpointResponse424
    | PostFirewallRuleEndpointResponse500
    | PostFirewallRuleEndpointResponse503
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
    body: PostFirewallRuleEndpointJsonBody | PostFirewallRuleEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallRuleEndpointResponse400
    | PostFirewallRuleEndpointResponse401
    | PostFirewallRuleEndpointResponse403
    | PostFirewallRuleEndpointResponse404
    | PostFirewallRuleEndpointResponse405
    | PostFirewallRuleEndpointResponse406
    | PostFirewallRuleEndpointResponse409
    | PostFirewallRuleEndpointResponse415
    | PostFirewallRuleEndpointResponse422
    | PostFirewallRuleEndpointResponse424
    | PostFirewallRuleEndpointResponse500
    | PostFirewallRuleEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallRuleEndpointJsonBody | Unset):
        body (PostFirewallRuleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallRuleEndpointResponse400 | PostFirewallRuleEndpointResponse401 | PostFirewallRuleEndpointResponse403 | PostFirewallRuleEndpointResponse404 | PostFirewallRuleEndpointResponse405 | PostFirewallRuleEndpointResponse406 | PostFirewallRuleEndpointResponse409 | PostFirewallRuleEndpointResponse415 | PostFirewallRuleEndpointResponse422 | PostFirewallRuleEndpointResponse424 | PostFirewallRuleEndpointResponse500 | PostFirewallRuleEndpointResponse503]
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
    body: PostFirewallRuleEndpointJsonBody | PostFirewallRuleEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallRuleEndpointResponse400
    | PostFirewallRuleEndpointResponse401
    | PostFirewallRuleEndpointResponse403
    | PostFirewallRuleEndpointResponse404
    | PostFirewallRuleEndpointResponse405
    | PostFirewallRuleEndpointResponse406
    | PostFirewallRuleEndpointResponse409
    | PostFirewallRuleEndpointResponse415
    | PostFirewallRuleEndpointResponse422
    | PostFirewallRuleEndpointResponse424
    | PostFirewallRuleEndpointResponse500
    | PostFirewallRuleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallRuleEndpointJsonBody | Unset):
        body (PostFirewallRuleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallRuleEndpointResponse400 | PostFirewallRuleEndpointResponse401 | PostFirewallRuleEndpointResponse403 | PostFirewallRuleEndpointResponse404 | PostFirewallRuleEndpointResponse405 | PostFirewallRuleEndpointResponse406 | PostFirewallRuleEndpointResponse409 | PostFirewallRuleEndpointResponse415 | PostFirewallRuleEndpointResponse422 | PostFirewallRuleEndpointResponse424 | PostFirewallRuleEndpointResponse500 | PostFirewallRuleEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallRuleEndpointJsonBody | PostFirewallRuleEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallRuleEndpointResponse400
    | PostFirewallRuleEndpointResponse401
    | PostFirewallRuleEndpointResponse403
    | PostFirewallRuleEndpointResponse404
    | PostFirewallRuleEndpointResponse405
    | PostFirewallRuleEndpointResponse406
    | PostFirewallRuleEndpointResponse409
    | PostFirewallRuleEndpointResponse415
    | PostFirewallRuleEndpointResponse422
    | PostFirewallRuleEndpointResponse424
    | PostFirewallRuleEndpointResponse500
    | PostFirewallRuleEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallRuleEndpointJsonBody | Unset):
        body (PostFirewallRuleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallRuleEndpointResponse400 | PostFirewallRuleEndpointResponse401 | PostFirewallRuleEndpointResponse403 | PostFirewallRuleEndpointResponse404 | PostFirewallRuleEndpointResponse405 | PostFirewallRuleEndpointResponse406 | PostFirewallRuleEndpointResponse409 | PostFirewallRuleEndpointResponse415 | PostFirewallRuleEndpointResponse422 | PostFirewallRuleEndpointResponse424 | PostFirewallRuleEndpointResponse500 | PostFirewallRuleEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallRuleEndpointJsonBody | PostFirewallRuleEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallRuleEndpointResponse400
    | PostFirewallRuleEndpointResponse401
    | PostFirewallRuleEndpointResponse403
    | PostFirewallRuleEndpointResponse404
    | PostFirewallRuleEndpointResponse405
    | PostFirewallRuleEndpointResponse406
    | PostFirewallRuleEndpointResponse409
    | PostFirewallRuleEndpointResponse415
    | PostFirewallRuleEndpointResponse422
    | PostFirewallRuleEndpointResponse424
    | PostFirewallRuleEndpointResponse500
    | PostFirewallRuleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Firewall Rule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallRule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-rule-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallRuleEndpointJsonBody | Unset):
        body (PostFirewallRuleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallRuleEndpointResponse400 | PostFirewallRuleEndpointResponse401 | PostFirewallRuleEndpointResponse403 | PostFirewallRuleEndpointResponse404 | PostFirewallRuleEndpointResponse405 | PostFirewallRuleEndpointResponse406 | PostFirewallRuleEndpointResponse409 | PostFirewallRuleEndpointResponse415 | PostFirewallRuleEndpointResponse422 | PostFirewallRuleEndpointResponse424 | PostFirewallRuleEndpointResponse500 | PostFirewallRuleEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
