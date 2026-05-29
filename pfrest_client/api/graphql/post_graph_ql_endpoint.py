from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_graph_ql_endpoint_data_body import PostGraphQLEndpointDataBody
from ...models.post_graph_ql_endpoint_json_body import PostGraphQLEndpointJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostGraphQLEndpointJsonBody | PostGraphQLEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/graphql",
    }

    if isinstance(body, PostGraphQLEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostGraphQLEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostGraphQLEndpointJsonBody | PostGraphQLEndpointDataBody | Unset = UNSET,
) -> Response[Any]:
    """<h3>Description:</h3>Execute a GraphQL query. For more information on utilizing the GraphQL API,
    please refer to https://pfrest.org/graphql.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: GraphQL<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-graphql-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostGraphQLEndpointJsonBody | Unset):
        body (PostGraphQLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostGraphQLEndpointJsonBody | PostGraphQLEndpointDataBody | Unset = UNSET,
) -> Response[Any]:
    """<h3>Description:</h3>Execute a GraphQL query. For more information on utilizing the GraphQL API,
    please refer to https://pfrest.org/graphql.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: GraphQL<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-graphql-post ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostGraphQLEndpointJsonBody | Unset):
        body (PostGraphQLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
