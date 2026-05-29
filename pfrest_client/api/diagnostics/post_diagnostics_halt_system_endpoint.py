from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_diagnostics_halt_system_endpoint_data_body import PostDiagnosticsHaltSystemEndpointDataBody
from ...models.post_diagnostics_halt_system_endpoint_json_body import PostDiagnosticsHaltSystemEndpointJsonBody
from ...models.post_diagnostics_halt_system_endpoint_response_400 import PostDiagnosticsHaltSystemEndpointResponse400
from ...models.post_diagnostics_halt_system_endpoint_response_401 import PostDiagnosticsHaltSystemEndpointResponse401
from ...models.post_diagnostics_halt_system_endpoint_response_403 import PostDiagnosticsHaltSystemEndpointResponse403
from ...models.post_diagnostics_halt_system_endpoint_response_404 import PostDiagnosticsHaltSystemEndpointResponse404
from ...models.post_diagnostics_halt_system_endpoint_response_405 import PostDiagnosticsHaltSystemEndpointResponse405
from ...models.post_diagnostics_halt_system_endpoint_response_406 import PostDiagnosticsHaltSystemEndpointResponse406
from ...models.post_diagnostics_halt_system_endpoint_response_409 import PostDiagnosticsHaltSystemEndpointResponse409
from ...models.post_diagnostics_halt_system_endpoint_response_415 import PostDiagnosticsHaltSystemEndpointResponse415
from ...models.post_diagnostics_halt_system_endpoint_response_422 import PostDiagnosticsHaltSystemEndpointResponse422
from ...models.post_diagnostics_halt_system_endpoint_response_424 import PostDiagnosticsHaltSystemEndpointResponse424
from ...models.post_diagnostics_halt_system_endpoint_response_500 import PostDiagnosticsHaltSystemEndpointResponse500
from ...models.post_diagnostics_halt_system_endpoint_response_503 import PostDiagnosticsHaltSystemEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostDiagnosticsHaltSystemEndpointJsonBody | PostDiagnosticsHaltSystemEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/diagnostics/halt_system",
    }

    if isinstance(body, PostDiagnosticsHaltSystemEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostDiagnosticsHaltSystemEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostDiagnosticsHaltSystemEndpointResponse400
    | PostDiagnosticsHaltSystemEndpointResponse401
    | PostDiagnosticsHaltSystemEndpointResponse403
    | PostDiagnosticsHaltSystemEndpointResponse404
    | PostDiagnosticsHaltSystemEndpointResponse405
    | PostDiagnosticsHaltSystemEndpointResponse406
    | PostDiagnosticsHaltSystemEndpointResponse409
    | PostDiagnosticsHaltSystemEndpointResponse415
    | PostDiagnosticsHaltSystemEndpointResponse422
    | PostDiagnosticsHaltSystemEndpointResponse424
    | PostDiagnosticsHaltSystemEndpointResponse500
    | PostDiagnosticsHaltSystemEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostDiagnosticsHaltSystemEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostDiagnosticsHaltSystemEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostDiagnosticsHaltSystemEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostDiagnosticsHaltSystemEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostDiagnosticsHaltSystemEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostDiagnosticsHaltSystemEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostDiagnosticsHaltSystemEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostDiagnosticsHaltSystemEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostDiagnosticsHaltSystemEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostDiagnosticsHaltSystemEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostDiagnosticsHaltSystemEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostDiagnosticsHaltSystemEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostDiagnosticsHaltSystemEndpointResponse400
    | PostDiagnosticsHaltSystemEndpointResponse401
    | PostDiagnosticsHaltSystemEndpointResponse403
    | PostDiagnosticsHaltSystemEndpointResponse404
    | PostDiagnosticsHaltSystemEndpointResponse405
    | PostDiagnosticsHaltSystemEndpointResponse406
    | PostDiagnosticsHaltSystemEndpointResponse409
    | PostDiagnosticsHaltSystemEndpointResponse415
    | PostDiagnosticsHaltSystemEndpointResponse422
    | PostDiagnosticsHaltSystemEndpointResponse424
    | PostDiagnosticsHaltSystemEndpointResponse500
    | PostDiagnosticsHaltSystemEndpointResponse503
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
    body: PostDiagnosticsHaltSystemEndpointJsonBody | PostDiagnosticsHaltSystemEndpointDataBody | Unset = UNSET,
) -> Response[
    PostDiagnosticsHaltSystemEndpointResponse400
    | PostDiagnosticsHaltSystemEndpointResponse401
    | PostDiagnosticsHaltSystemEndpointResponse403
    | PostDiagnosticsHaltSystemEndpointResponse404
    | PostDiagnosticsHaltSystemEndpointResponse405
    | PostDiagnosticsHaltSystemEndpointResponse406
    | PostDiagnosticsHaltSystemEndpointResponse409
    | PostDiagnosticsHaltSystemEndpointResponse415
    | PostDiagnosticsHaltSystemEndpointResponse422
    | PostDiagnosticsHaltSystemEndpointResponse424
    | PostDiagnosticsHaltSystemEndpointResponse500
    | PostDiagnosticsHaltSystemEndpointResponse503
]:
    """<h3>Description:</h3>Initiates a System Halt.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemHalt<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-halt-system-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsHaltSystemEndpointJsonBody | Unset):
        body (PostDiagnosticsHaltSystemEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDiagnosticsHaltSystemEndpointResponse400 | PostDiagnosticsHaltSystemEndpointResponse401 | PostDiagnosticsHaltSystemEndpointResponse403 | PostDiagnosticsHaltSystemEndpointResponse404 | PostDiagnosticsHaltSystemEndpointResponse405 | PostDiagnosticsHaltSystemEndpointResponse406 | PostDiagnosticsHaltSystemEndpointResponse409 | PostDiagnosticsHaltSystemEndpointResponse415 | PostDiagnosticsHaltSystemEndpointResponse422 | PostDiagnosticsHaltSystemEndpointResponse424 | PostDiagnosticsHaltSystemEndpointResponse500 | PostDiagnosticsHaltSystemEndpointResponse503]
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
    body: PostDiagnosticsHaltSystemEndpointJsonBody | PostDiagnosticsHaltSystemEndpointDataBody | Unset = UNSET,
) -> (
    PostDiagnosticsHaltSystemEndpointResponse400
    | PostDiagnosticsHaltSystemEndpointResponse401
    | PostDiagnosticsHaltSystemEndpointResponse403
    | PostDiagnosticsHaltSystemEndpointResponse404
    | PostDiagnosticsHaltSystemEndpointResponse405
    | PostDiagnosticsHaltSystemEndpointResponse406
    | PostDiagnosticsHaltSystemEndpointResponse409
    | PostDiagnosticsHaltSystemEndpointResponse415
    | PostDiagnosticsHaltSystemEndpointResponse422
    | PostDiagnosticsHaltSystemEndpointResponse424
    | PostDiagnosticsHaltSystemEndpointResponse500
    | PostDiagnosticsHaltSystemEndpointResponse503
    | None
):
    """<h3>Description:</h3>Initiates a System Halt.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemHalt<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-halt-system-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsHaltSystemEndpointJsonBody | Unset):
        body (PostDiagnosticsHaltSystemEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDiagnosticsHaltSystemEndpointResponse400 | PostDiagnosticsHaltSystemEndpointResponse401 | PostDiagnosticsHaltSystemEndpointResponse403 | PostDiagnosticsHaltSystemEndpointResponse404 | PostDiagnosticsHaltSystemEndpointResponse405 | PostDiagnosticsHaltSystemEndpointResponse406 | PostDiagnosticsHaltSystemEndpointResponse409 | PostDiagnosticsHaltSystemEndpointResponse415 | PostDiagnosticsHaltSystemEndpointResponse422 | PostDiagnosticsHaltSystemEndpointResponse424 | PostDiagnosticsHaltSystemEndpointResponse500 | PostDiagnosticsHaltSystemEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostDiagnosticsHaltSystemEndpointJsonBody | PostDiagnosticsHaltSystemEndpointDataBody | Unset = UNSET,
) -> Response[
    PostDiagnosticsHaltSystemEndpointResponse400
    | PostDiagnosticsHaltSystemEndpointResponse401
    | PostDiagnosticsHaltSystemEndpointResponse403
    | PostDiagnosticsHaltSystemEndpointResponse404
    | PostDiagnosticsHaltSystemEndpointResponse405
    | PostDiagnosticsHaltSystemEndpointResponse406
    | PostDiagnosticsHaltSystemEndpointResponse409
    | PostDiagnosticsHaltSystemEndpointResponse415
    | PostDiagnosticsHaltSystemEndpointResponse422
    | PostDiagnosticsHaltSystemEndpointResponse424
    | PostDiagnosticsHaltSystemEndpointResponse500
    | PostDiagnosticsHaltSystemEndpointResponse503
]:
    """<h3>Description:</h3>Initiates a System Halt.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemHalt<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-halt-system-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsHaltSystemEndpointJsonBody | Unset):
        body (PostDiagnosticsHaltSystemEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDiagnosticsHaltSystemEndpointResponse400 | PostDiagnosticsHaltSystemEndpointResponse401 | PostDiagnosticsHaltSystemEndpointResponse403 | PostDiagnosticsHaltSystemEndpointResponse404 | PostDiagnosticsHaltSystemEndpointResponse405 | PostDiagnosticsHaltSystemEndpointResponse406 | PostDiagnosticsHaltSystemEndpointResponse409 | PostDiagnosticsHaltSystemEndpointResponse415 | PostDiagnosticsHaltSystemEndpointResponse422 | PostDiagnosticsHaltSystemEndpointResponse424 | PostDiagnosticsHaltSystemEndpointResponse500 | PostDiagnosticsHaltSystemEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostDiagnosticsHaltSystemEndpointJsonBody | PostDiagnosticsHaltSystemEndpointDataBody | Unset = UNSET,
) -> (
    PostDiagnosticsHaltSystemEndpointResponse400
    | PostDiagnosticsHaltSystemEndpointResponse401
    | PostDiagnosticsHaltSystemEndpointResponse403
    | PostDiagnosticsHaltSystemEndpointResponse404
    | PostDiagnosticsHaltSystemEndpointResponse405
    | PostDiagnosticsHaltSystemEndpointResponse406
    | PostDiagnosticsHaltSystemEndpointResponse409
    | PostDiagnosticsHaltSystemEndpointResponse415
    | PostDiagnosticsHaltSystemEndpointResponse422
    | PostDiagnosticsHaltSystemEndpointResponse424
    | PostDiagnosticsHaltSystemEndpointResponse500
    | PostDiagnosticsHaltSystemEndpointResponse503
    | None
):
    """<h3>Description:</h3>Initiates a System Halt.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemHalt<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-halt-system-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsHaltSystemEndpointJsonBody | Unset):
        body (PostDiagnosticsHaltSystemEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDiagnosticsHaltSystemEndpointResponse400 | PostDiagnosticsHaltSystemEndpointResponse401 | PostDiagnosticsHaltSystemEndpointResponse403 | PostDiagnosticsHaltSystemEndpointResponse404 | PostDiagnosticsHaltSystemEndpointResponse405 | PostDiagnosticsHaltSystemEndpointResponse406 | PostDiagnosticsHaltSystemEndpointResponse409 | PostDiagnosticsHaltSystemEndpointResponse415 | PostDiagnosticsHaltSystemEndpointResponse422 | PostDiagnosticsHaltSystemEndpointResponse424 | PostDiagnosticsHaltSystemEndpointResponse500 | PostDiagnosticsHaltSystemEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
