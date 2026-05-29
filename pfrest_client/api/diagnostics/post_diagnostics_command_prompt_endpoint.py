from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_diagnostics_command_prompt_endpoint_data_body import PostDiagnosticsCommandPromptEndpointDataBody
from ...models.post_diagnostics_command_prompt_endpoint_json_body import PostDiagnosticsCommandPromptEndpointJsonBody
from ...models.post_diagnostics_command_prompt_endpoint_response_400 import (
    PostDiagnosticsCommandPromptEndpointResponse400,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_401 import (
    PostDiagnosticsCommandPromptEndpointResponse401,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_403 import (
    PostDiagnosticsCommandPromptEndpointResponse403,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_404 import (
    PostDiagnosticsCommandPromptEndpointResponse404,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_405 import (
    PostDiagnosticsCommandPromptEndpointResponse405,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_406 import (
    PostDiagnosticsCommandPromptEndpointResponse406,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_409 import (
    PostDiagnosticsCommandPromptEndpointResponse409,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_415 import (
    PostDiagnosticsCommandPromptEndpointResponse415,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_422 import (
    PostDiagnosticsCommandPromptEndpointResponse422,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_424 import (
    PostDiagnosticsCommandPromptEndpointResponse424,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_500 import (
    PostDiagnosticsCommandPromptEndpointResponse500,
)
from ...models.post_diagnostics_command_prompt_endpoint_response_503 import (
    PostDiagnosticsCommandPromptEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostDiagnosticsCommandPromptEndpointJsonBody | PostDiagnosticsCommandPromptEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/diagnostics/command_prompt",
    }

    if isinstance(body, PostDiagnosticsCommandPromptEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostDiagnosticsCommandPromptEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostDiagnosticsCommandPromptEndpointResponse400
    | PostDiagnosticsCommandPromptEndpointResponse401
    | PostDiagnosticsCommandPromptEndpointResponse403
    | PostDiagnosticsCommandPromptEndpointResponse404
    | PostDiagnosticsCommandPromptEndpointResponse405
    | PostDiagnosticsCommandPromptEndpointResponse406
    | PostDiagnosticsCommandPromptEndpointResponse409
    | PostDiagnosticsCommandPromptEndpointResponse415
    | PostDiagnosticsCommandPromptEndpointResponse422
    | PostDiagnosticsCommandPromptEndpointResponse424
    | PostDiagnosticsCommandPromptEndpointResponse500
    | PostDiagnosticsCommandPromptEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostDiagnosticsCommandPromptEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostDiagnosticsCommandPromptEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostDiagnosticsCommandPromptEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostDiagnosticsCommandPromptEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostDiagnosticsCommandPromptEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostDiagnosticsCommandPromptEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostDiagnosticsCommandPromptEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostDiagnosticsCommandPromptEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostDiagnosticsCommandPromptEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostDiagnosticsCommandPromptEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostDiagnosticsCommandPromptEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostDiagnosticsCommandPromptEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostDiagnosticsCommandPromptEndpointResponse400
    | PostDiagnosticsCommandPromptEndpointResponse401
    | PostDiagnosticsCommandPromptEndpointResponse403
    | PostDiagnosticsCommandPromptEndpointResponse404
    | PostDiagnosticsCommandPromptEndpointResponse405
    | PostDiagnosticsCommandPromptEndpointResponse406
    | PostDiagnosticsCommandPromptEndpointResponse409
    | PostDiagnosticsCommandPromptEndpointResponse415
    | PostDiagnosticsCommandPromptEndpointResponse422
    | PostDiagnosticsCommandPromptEndpointResponse424
    | PostDiagnosticsCommandPromptEndpointResponse500
    | PostDiagnosticsCommandPromptEndpointResponse503
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
    body: PostDiagnosticsCommandPromptEndpointJsonBody | PostDiagnosticsCommandPromptEndpointDataBody | Unset = UNSET,
) -> Response[
    PostDiagnosticsCommandPromptEndpointResponse400
    | PostDiagnosticsCommandPromptEndpointResponse401
    | PostDiagnosticsCommandPromptEndpointResponse403
    | PostDiagnosticsCommandPromptEndpointResponse404
    | PostDiagnosticsCommandPromptEndpointResponse405
    | PostDiagnosticsCommandPromptEndpointResponse406
    | PostDiagnosticsCommandPromptEndpointResponse409
    | PostDiagnosticsCommandPromptEndpointResponse415
    | PostDiagnosticsCommandPromptEndpointResponse422
    | PostDiagnosticsCommandPromptEndpointResponse424
    | PostDiagnosticsCommandPromptEndpointResponse500
    | PostDiagnosticsCommandPromptEndpointResponse503
]:
    """<h3>Description:</h3>Executes a shell command.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CommandPrompt<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-command-prompt-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsCommandPromptEndpointJsonBody | Unset):
        body (PostDiagnosticsCommandPromptEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDiagnosticsCommandPromptEndpointResponse400 | PostDiagnosticsCommandPromptEndpointResponse401 | PostDiagnosticsCommandPromptEndpointResponse403 | PostDiagnosticsCommandPromptEndpointResponse404 | PostDiagnosticsCommandPromptEndpointResponse405 | PostDiagnosticsCommandPromptEndpointResponse406 | PostDiagnosticsCommandPromptEndpointResponse409 | PostDiagnosticsCommandPromptEndpointResponse415 | PostDiagnosticsCommandPromptEndpointResponse422 | PostDiagnosticsCommandPromptEndpointResponse424 | PostDiagnosticsCommandPromptEndpointResponse500 | PostDiagnosticsCommandPromptEndpointResponse503]
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
    body: PostDiagnosticsCommandPromptEndpointJsonBody | PostDiagnosticsCommandPromptEndpointDataBody | Unset = UNSET,
) -> (
    PostDiagnosticsCommandPromptEndpointResponse400
    | PostDiagnosticsCommandPromptEndpointResponse401
    | PostDiagnosticsCommandPromptEndpointResponse403
    | PostDiagnosticsCommandPromptEndpointResponse404
    | PostDiagnosticsCommandPromptEndpointResponse405
    | PostDiagnosticsCommandPromptEndpointResponse406
    | PostDiagnosticsCommandPromptEndpointResponse409
    | PostDiagnosticsCommandPromptEndpointResponse415
    | PostDiagnosticsCommandPromptEndpointResponse422
    | PostDiagnosticsCommandPromptEndpointResponse424
    | PostDiagnosticsCommandPromptEndpointResponse500
    | PostDiagnosticsCommandPromptEndpointResponse503
    | None
):
    """<h3>Description:</h3>Executes a shell command.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CommandPrompt<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-command-prompt-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsCommandPromptEndpointJsonBody | Unset):
        body (PostDiagnosticsCommandPromptEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDiagnosticsCommandPromptEndpointResponse400 | PostDiagnosticsCommandPromptEndpointResponse401 | PostDiagnosticsCommandPromptEndpointResponse403 | PostDiagnosticsCommandPromptEndpointResponse404 | PostDiagnosticsCommandPromptEndpointResponse405 | PostDiagnosticsCommandPromptEndpointResponse406 | PostDiagnosticsCommandPromptEndpointResponse409 | PostDiagnosticsCommandPromptEndpointResponse415 | PostDiagnosticsCommandPromptEndpointResponse422 | PostDiagnosticsCommandPromptEndpointResponse424 | PostDiagnosticsCommandPromptEndpointResponse500 | PostDiagnosticsCommandPromptEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostDiagnosticsCommandPromptEndpointJsonBody | PostDiagnosticsCommandPromptEndpointDataBody | Unset = UNSET,
) -> Response[
    PostDiagnosticsCommandPromptEndpointResponse400
    | PostDiagnosticsCommandPromptEndpointResponse401
    | PostDiagnosticsCommandPromptEndpointResponse403
    | PostDiagnosticsCommandPromptEndpointResponse404
    | PostDiagnosticsCommandPromptEndpointResponse405
    | PostDiagnosticsCommandPromptEndpointResponse406
    | PostDiagnosticsCommandPromptEndpointResponse409
    | PostDiagnosticsCommandPromptEndpointResponse415
    | PostDiagnosticsCommandPromptEndpointResponse422
    | PostDiagnosticsCommandPromptEndpointResponse424
    | PostDiagnosticsCommandPromptEndpointResponse500
    | PostDiagnosticsCommandPromptEndpointResponse503
]:
    """<h3>Description:</h3>Executes a shell command.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CommandPrompt<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-command-prompt-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsCommandPromptEndpointJsonBody | Unset):
        body (PostDiagnosticsCommandPromptEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDiagnosticsCommandPromptEndpointResponse400 | PostDiagnosticsCommandPromptEndpointResponse401 | PostDiagnosticsCommandPromptEndpointResponse403 | PostDiagnosticsCommandPromptEndpointResponse404 | PostDiagnosticsCommandPromptEndpointResponse405 | PostDiagnosticsCommandPromptEndpointResponse406 | PostDiagnosticsCommandPromptEndpointResponse409 | PostDiagnosticsCommandPromptEndpointResponse415 | PostDiagnosticsCommandPromptEndpointResponse422 | PostDiagnosticsCommandPromptEndpointResponse424 | PostDiagnosticsCommandPromptEndpointResponse500 | PostDiagnosticsCommandPromptEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostDiagnosticsCommandPromptEndpointJsonBody | PostDiagnosticsCommandPromptEndpointDataBody | Unset = UNSET,
) -> (
    PostDiagnosticsCommandPromptEndpointResponse400
    | PostDiagnosticsCommandPromptEndpointResponse401
    | PostDiagnosticsCommandPromptEndpointResponse403
    | PostDiagnosticsCommandPromptEndpointResponse404
    | PostDiagnosticsCommandPromptEndpointResponse405
    | PostDiagnosticsCommandPromptEndpointResponse406
    | PostDiagnosticsCommandPromptEndpointResponse409
    | PostDiagnosticsCommandPromptEndpointResponse415
    | PostDiagnosticsCommandPromptEndpointResponse422
    | PostDiagnosticsCommandPromptEndpointResponse424
    | PostDiagnosticsCommandPromptEndpointResponse500
    | PostDiagnosticsCommandPromptEndpointResponse503
    | None
):
    """<h3>Description:</h3>Executes a shell command.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: CommandPrompt<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-command-prompt-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsCommandPromptEndpointJsonBody | Unset):
        body (PostDiagnosticsCommandPromptEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDiagnosticsCommandPromptEndpointResponse400 | PostDiagnosticsCommandPromptEndpointResponse401 | PostDiagnosticsCommandPromptEndpointResponse403 | PostDiagnosticsCommandPromptEndpointResponse404 | PostDiagnosticsCommandPromptEndpointResponse405 | PostDiagnosticsCommandPromptEndpointResponse406 | PostDiagnosticsCommandPromptEndpointResponse409 | PostDiagnosticsCommandPromptEndpointResponse415 | PostDiagnosticsCommandPromptEndpointResponse422 | PostDiagnosticsCommandPromptEndpointResponse424 | PostDiagnosticsCommandPromptEndpointResponse500 | PostDiagnosticsCommandPromptEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
