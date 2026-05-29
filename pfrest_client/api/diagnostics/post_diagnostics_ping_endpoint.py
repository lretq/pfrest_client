from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_diagnostics_ping_endpoint_data_body import PostDiagnosticsPingEndpointDataBody
from ...models.post_diagnostics_ping_endpoint_json_body import PostDiagnosticsPingEndpointJsonBody
from ...models.post_diagnostics_ping_endpoint_response_400 import PostDiagnosticsPingEndpointResponse400
from ...models.post_diagnostics_ping_endpoint_response_401 import PostDiagnosticsPingEndpointResponse401
from ...models.post_diagnostics_ping_endpoint_response_403 import PostDiagnosticsPingEndpointResponse403
from ...models.post_diagnostics_ping_endpoint_response_404 import PostDiagnosticsPingEndpointResponse404
from ...models.post_diagnostics_ping_endpoint_response_405 import PostDiagnosticsPingEndpointResponse405
from ...models.post_diagnostics_ping_endpoint_response_406 import PostDiagnosticsPingEndpointResponse406
from ...models.post_diagnostics_ping_endpoint_response_409 import PostDiagnosticsPingEndpointResponse409
from ...models.post_diagnostics_ping_endpoint_response_415 import PostDiagnosticsPingEndpointResponse415
from ...models.post_diagnostics_ping_endpoint_response_422 import PostDiagnosticsPingEndpointResponse422
from ...models.post_diagnostics_ping_endpoint_response_424 import PostDiagnosticsPingEndpointResponse424
from ...models.post_diagnostics_ping_endpoint_response_500 import PostDiagnosticsPingEndpointResponse500
from ...models.post_diagnostics_ping_endpoint_response_503 import PostDiagnosticsPingEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostDiagnosticsPingEndpointJsonBody | PostDiagnosticsPingEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/diagnostics/ping",
    }

    if isinstance(body, PostDiagnosticsPingEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostDiagnosticsPingEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostDiagnosticsPingEndpointResponse400
    | PostDiagnosticsPingEndpointResponse401
    | PostDiagnosticsPingEndpointResponse403
    | PostDiagnosticsPingEndpointResponse404
    | PostDiagnosticsPingEndpointResponse405
    | PostDiagnosticsPingEndpointResponse406
    | PostDiagnosticsPingEndpointResponse409
    | PostDiagnosticsPingEndpointResponse415
    | PostDiagnosticsPingEndpointResponse422
    | PostDiagnosticsPingEndpointResponse424
    | PostDiagnosticsPingEndpointResponse500
    | PostDiagnosticsPingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostDiagnosticsPingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostDiagnosticsPingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostDiagnosticsPingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostDiagnosticsPingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostDiagnosticsPingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostDiagnosticsPingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostDiagnosticsPingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostDiagnosticsPingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostDiagnosticsPingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostDiagnosticsPingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostDiagnosticsPingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostDiagnosticsPingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostDiagnosticsPingEndpointResponse400
    | PostDiagnosticsPingEndpointResponse401
    | PostDiagnosticsPingEndpointResponse403
    | PostDiagnosticsPingEndpointResponse404
    | PostDiagnosticsPingEndpointResponse405
    | PostDiagnosticsPingEndpointResponse406
    | PostDiagnosticsPingEndpointResponse409
    | PostDiagnosticsPingEndpointResponse415
    | PostDiagnosticsPingEndpointResponse422
    | PostDiagnosticsPingEndpointResponse424
    | PostDiagnosticsPingEndpointResponse500
    | PostDiagnosticsPingEndpointResponse503
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
    body: PostDiagnosticsPingEndpointJsonBody | PostDiagnosticsPingEndpointDataBody | Unset = UNSET,
) -> Response[
    PostDiagnosticsPingEndpointResponse400
    | PostDiagnosticsPingEndpointResponse401
    | PostDiagnosticsPingEndpointResponse403
    | PostDiagnosticsPingEndpointResponse404
    | PostDiagnosticsPingEndpointResponse405
    | PostDiagnosticsPingEndpointResponse406
    | PostDiagnosticsPingEndpointResponse409
    | PostDiagnosticsPingEndpointResponse415
    | PostDiagnosticsPingEndpointResponse422
    | PostDiagnosticsPingEndpointResponse424
    | PostDiagnosticsPingEndpointResponse500
    | PostDiagnosticsPingEndpointResponse503
]:
    """<h3>Description:</h3>Run a ping command from pfSense to a specified
    host.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Ping<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-ping-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostDiagnosticsPingEndpointJsonBody | Unset):
        body (PostDiagnosticsPingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDiagnosticsPingEndpointResponse400 | PostDiagnosticsPingEndpointResponse401 | PostDiagnosticsPingEndpointResponse403 | PostDiagnosticsPingEndpointResponse404 | PostDiagnosticsPingEndpointResponse405 | PostDiagnosticsPingEndpointResponse406 | PostDiagnosticsPingEndpointResponse409 | PostDiagnosticsPingEndpointResponse415 | PostDiagnosticsPingEndpointResponse422 | PostDiagnosticsPingEndpointResponse424 | PostDiagnosticsPingEndpointResponse500 | PostDiagnosticsPingEndpointResponse503]
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
    body: PostDiagnosticsPingEndpointJsonBody | PostDiagnosticsPingEndpointDataBody | Unset = UNSET,
) -> (
    PostDiagnosticsPingEndpointResponse400
    | PostDiagnosticsPingEndpointResponse401
    | PostDiagnosticsPingEndpointResponse403
    | PostDiagnosticsPingEndpointResponse404
    | PostDiagnosticsPingEndpointResponse405
    | PostDiagnosticsPingEndpointResponse406
    | PostDiagnosticsPingEndpointResponse409
    | PostDiagnosticsPingEndpointResponse415
    | PostDiagnosticsPingEndpointResponse422
    | PostDiagnosticsPingEndpointResponse424
    | PostDiagnosticsPingEndpointResponse500
    | PostDiagnosticsPingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Run a ping command from pfSense to a specified
    host.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Ping<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-ping-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostDiagnosticsPingEndpointJsonBody | Unset):
        body (PostDiagnosticsPingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDiagnosticsPingEndpointResponse400 | PostDiagnosticsPingEndpointResponse401 | PostDiagnosticsPingEndpointResponse403 | PostDiagnosticsPingEndpointResponse404 | PostDiagnosticsPingEndpointResponse405 | PostDiagnosticsPingEndpointResponse406 | PostDiagnosticsPingEndpointResponse409 | PostDiagnosticsPingEndpointResponse415 | PostDiagnosticsPingEndpointResponse422 | PostDiagnosticsPingEndpointResponse424 | PostDiagnosticsPingEndpointResponse500 | PostDiagnosticsPingEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostDiagnosticsPingEndpointJsonBody | PostDiagnosticsPingEndpointDataBody | Unset = UNSET,
) -> Response[
    PostDiagnosticsPingEndpointResponse400
    | PostDiagnosticsPingEndpointResponse401
    | PostDiagnosticsPingEndpointResponse403
    | PostDiagnosticsPingEndpointResponse404
    | PostDiagnosticsPingEndpointResponse405
    | PostDiagnosticsPingEndpointResponse406
    | PostDiagnosticsPingEndpointResponse409
    | PostDiagnosticsPingEndpointResponse415
    | PostDiagnosticsPingEndpointResponse422
    | PostDiagnosticsPingEndpointResponse424
    | PostDiagnosticsPingEndpointResponse500
    | PostDiagnosticsPingEndpointResponse503
]:
    """<h3>Description:</h3>Run a ping command from pfSense to a specified
    host.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Ping<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-ping-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostDiagnosticsPingEndpointJsonBody | Unset):
        body (PostDiagnosticsPingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDiagnosticsPingEndpointResponse400 | PostDiagnosticsPingEndpointResponse401 | PostDiagnosticsPingEndpointResponse403 | PostDiagnosticsPingEndpointResponse404 | PostDiagnosticsPingEndpointResponse405 | PostDiagnosticsPingEndpointResponse406 | PostDiagnosticsPingEndpointResponse409 | PostDiagnosticsPingEndpointResponse415 | PostDiagnosticsPingEndpointResponse422 | PostDiagnosticsPingEndpointResponse424 | PostDiagnosticsPingEndpointResponse500 | PostDiagnosticsPingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostDiagnosticsPingEndpointJsonBody | PostDiagnosticsPingEndpointDataBody | Unset = UNSET,
) -> (
    PostDiagnosticsPingEndpointResponse400
    | PostDiagnosticsPingEndpointResponse401
    | PostDiagnosticsPingEndpointResponse403
    | PostDiagnosticsPingEndpointResponse404
    | PostDiagnosticsPingEndpointResponse405
    | PostDiagnosticsPingEndpointResponse406
    | PostDiagnosticsPingEndpointResponse409
    | PostDiagnosticsPingEndpointResponse415
    | PostDiagnosticsPingEndpointResponse422
    | PostDiagnosticsPingEndpointResponse424
    | PostDiagnosticsPingEndpointResponse500
    | PostDiagnosticsPingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Run a ping command from pfSense to a specified
    host.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**: Ping<br>**Parent
    model**: None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-ping-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Args:
        body (PostDiagnosticsPingEndpointJsonBody | Unset):
        body (PostDiagnosticsPingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDiagnosticsPingEndpointResponse400 | PostDiagnosticsPingEndpointResponse401 | PostDiagnosticsPingEndpointResponse403 | PostDiagnosticsPingEndpointResponse404 | PostDiagnosticsPingEndpointResponse405 | PostDiagnosticsPingEndpointResponse406 | PostDiagnosticsPingEndpointResponse409 | PostDiagnosticsPingEndpointResponse415 | PostDiagnosticsPingEndpointResponse422 | PostDiagnosticsPingEndpointResponse424 | PostDiagnosticsPingEndpointResponse500 | PostDiagnosticsPingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
