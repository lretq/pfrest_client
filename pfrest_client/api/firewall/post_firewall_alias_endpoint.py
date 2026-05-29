from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_alias_endpoint_data_body import PostFirewallAliasEndpointDataBody
from ...models.post_firewall_alias_endpoint_json_body import PostFirewallAliasEndpointJsonBody
from ...models.post_firewall_alias_endpoint_response_400 import PostFirewallAliasEndpointResponse400
from ...models.post_firewall_alias_endpoint_response_401 import PostFirewallAliasEndpointResponse401
from ...models.post_firewall_alias_endpoint_response_403 import PostFirewallAliasEndpointResponse403
from ...models.post_firewall_alias_endpoint_response_404 import PostFirewallAliasEndpointResponse404
from ...models.post_firewall_alias_endpoint_response_405 import PostFirewallAliasEndpointResponse405
from ...models.post_firewall_alias_endpoint_response_406 import PostFirewallAliasEndpointResponse406
from ...models.post_firewall_alias_endpoint_response_409 import PostFirewallAliasEndpointResponse409
from ...models.post_firewall_alias_endpoint_response_415 import PostFirewallAliasEndpointResponse415
from ...models.post_firewall_alias_endpoint_response_422 import PostFirewallAliasEndpointResponse422
from ...models.post_firewall_alias_endpoint_response_424 import PostFirewallAliasEndpointResponse424
from ...models.post_firewall_alias_endpoint_response_500 import PostFirewallAliasEndpointResponse500
from ...models.post_firewall_alias_endpoint_response_503 import PostFirewallAliasEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallAliasEndpointJsonBody | PostFirewallAliasEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/alias",
    }

    if isinstance(body, PostFirewallAliasEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallAliasEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallAliasEndpointResponse400
    | PostFirewallAliasEndpointResponse401
    | PostFirewallAliasEndpointResponse403
    | PostFirewallAliasEndpointResponse404
    | PostFirewallAliasEndpointResponse405
    | PostFirewallAliasEndpointResponse406
    | PostFirewallAliasEndpointResponse409
    | PostFirewallAliasEndpointResponse415
    | PostFirewallAliasEndpointResponse422
    | PostFirewallAliasEndpointResponse424
    | PostFirewallAliasEndpointResponse500
    | PostFirewallAliasEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallAliasEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallAliasEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallAliasEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallAliasEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallAliasEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallAliasEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallAliasEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallAliasEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallAliasEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallAliasEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallAliasEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallAliasEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallAliasEndpointResponse400
    | PostFirewallAliasEndpointResponse401
    | PostFirewallAliasEndpointResponse403
    | PostFirewallAliasEndpointResponse404
    | PostFirewallAliasEndpointResponse405
    | PostFirewallAliasEndpointResponse406
    | PostFirewallAliasEndpointResponse409
    | PostFirewallAliasEndpointResponse415
    | PostFirewallAliasEndpointResponse422
    | PostFirewallAliasEndpointResponse424
    | PostFirewallAliasEndpointResponse500
    | PostFirewallAliasEndpointResponse503
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
    body: PostFirewallAliasEndpointJsonBody | PostFirewallAliasEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallAliasEndpointResponse400
    | PostFirewallAliasEndpointResponse401
    | PostFirewallAliasEndpointResponse403
    | PostFirewallAliasEndpointResponse404
    | PostFirewallAliasEndpointResponse405
    | PostFirewallAliasEndpointResponse406
    | PostFirewallAliasEndpointResponse409
    | PostFirewallAliasEndpointResponse415
    | PostFirewallAliasEndpointResponse422
    | PostFirewallAliasEndpointResponse424
    | PostFirewallAliasEndpointResponse500
    | PostFirewallAliasEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Firewall Alias.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallAlias<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-alias-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallAliasEndpointJsonBody | Unset):
        body (PostFirewallAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallAliasEndpointResponse400 | PostFirewallAliasEndpointResponse401 | PostFirewallAliasEndpointResponse403 | PostFirewallAliasEndpointResponse404 | PostFirewallAliasEndpointResponse405 | PostFirewallAliasEndpointResponse406 | PostFirewallAliasEndpointResponse409 | PostFirewallAliasEndpointResponse415 | PostFirewallAliasEndpointResponse422 | PostFirewallAliasEndpointResponse424 | PostFirewallAliasEndpointResponse500 | PostFirewallAliasEndpointResponse503]
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
    body: PostFirewallAliasEndpointJsonBody | PostFirewallAliasEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallAliasEndpointResponse400
    | PostFirewallAliasEndpointResponse401
    | PostFirewallAliasEndpointResponse403
    | PostFirewallAliasEndpointResponse404
    | PostFirewallAliasEndpointResponse405
    | PostFirewallAliasEndpointResponse406
    | PostFirewallAliasEndpointResponse409
    | PostFirewallAliasEndpointResponse415
    | PostFirewallAliasEndpointResponse422
    | PostFirewallAliasEndpointResponse424
    | PostFirewallAliasEndpointResponse500
    | PostFirewallAliasEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Firewall Alias.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallAlias<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-alias-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallAliasEndpointJsonBody | Unset):
        body (PostFirewallAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallAliasEndpointResponse400 | PostFirewallAliasEndpointResponse401 | PostFirewallAliasEndpointResponse403 | PostFirewallAliasEndpointResponse404 | PostFirewallAliasEndpointResponse405 | PostFirewallAliasEndpointResponse406 | PostFirewallAliasEndpointResponse409 | PostFirewallAliasEndpointResponse415 | PostFirewallAliasEndpointResponse422 | PostFirewallAliasEndpointResponse424 | PostFirewallAliasEndpointResponse500 | PostFirewallAliasEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallAliasEndpointJsonBody | PostFirewallAliasEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallAliasEndpointResponse400
    | PostFirewallAliasEndpointResponse401
    | PostFirewallAliasEndpointResponse403
    | PostFirewallAliasEndpointResponse404
    | PostFirewallAliasEndpointResponse405
    | PostFirewallAliasEndpointResponse406
    | PostFirewallAliasEndpointResponse409
    | PostFirewallAliasEndpointResponse415
    | PostFirewallAliasEndpointResponse422
    | PostFirewallAliasEndpointResponse424
    | PostFirewallAliasEndpointResponse500
    | PostFirewallAliasEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Firewall Alias.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallAlias<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-alias-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallAliasEndpointJsonBody | Unset):
        body (PostFirewallAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallAliasEndpointResponse400 | PostFirewallAliasEndpointResponse401 | PostFirewallAliasEndpointResponse403 | PostFirewallAliasEndpointResponse404 | PostFirewallAliasEndpointResponse405 | PostFirewallAliasEndpointResponse406 | PostFirewallAliasEndpointResponse409 | PostFirewallAliasEndpointResponse415 | PostFirewallAliasEndpointResponse422 | PostFirewallAliasEndpointResponse424 | PostFirewallAliasEndpointResponse500 | PostFirewallAliasEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallAliasEndpointJsonBody | PostFirewallAliasEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallAliasEndpointResponse400
    | PostFirewallAliasEndpointResponse401
    | PostFirewallAliasEndpointResponse403
    | PostFirewallAliasEndpointResponse404
    | PostFirewallAliasEndpointResponse405
    | PostFirewallAliasEndpointResponse406
    | PostFirewallAliasEndpointResponse409
    | PostFirewallAliasEndpointResponse415
    | PostFirewallAliasEndpointResponse422
    | PostFirewallAliasEndpointResponse424
    | PostFirewallAliasEndpointResponse500
    | PostFirewallAliasEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Firewall Alias.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallAlias<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-alias-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostFirewallAliasEndpointJsonBody | Unset):
        body (PostFirewallAliasEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallAliasEndpointResponse400 | PostFirewallAliasEndpointResponse401 | PostFirewallAliasEndpointResponse403 | PostFirewallAliasEndpointResponse404 | PostFirewallAliasEndpointResponse405 | PostFirewallAliasEndpointResponse406 | PostFirewallAliasEndpointResponse409 | PostFirewallAliasEndpointResponse415 | PostFirewallAliasEndpointResponse422 | PostFirewallAliasEndpointResponse424 | PostFirewallAliasEndpointResponse500 | PostFirewallAliasEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
