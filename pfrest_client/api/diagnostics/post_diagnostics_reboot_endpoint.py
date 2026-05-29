from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_diagnostics_reboot_endpoint_data_body import PostDiagnosticsRebootEndpointDataBody
from ...models.post_diagnostics_reboot_endpoint_json_body import PostDiagnosticsRebootEndpointJsonBody
from ...models.post_diagnostics_reboot_endpoint_response_400 import PostDiagnosticsRebootEndpointResponse400
from ...models.post_diagnostics_reboot_endpoint_response_401 import PostDiagnosticsRebootEndpointResponse401
from ...models.post_diagnostics_reboot_endpoint_response_403 import PostDiagnosticsRebootEndpointResponse403
from ...models.post_diagnostics_reboot_endpoint_response_404 import PostDiagnosticsRebootEndpointResponse404
from ...models.post_diagnostics_reboot_endpoint_response_405 import PostDiagnosticsRebootEndpointResponse405
from ...models.post_diagnostics_reboot_endpoint_response_406 import PostDiagnosticsRebootEndpointResponse406
from ...models.post_diagnostics_reboot_endpoint_response_409 import PostDiagnosticsRebootEndpointResponse409
from ...models.post_diagnostics_reboot_endpoint_response_415 import PostDiagnosticsRebootEndpointResponse415
from ...models.post_diagnostics_reboot_endpoint_response_422 import PostDiagnosticsRebootEndpointResponse422
from ...models.post_diagnostics_reboot_endpoint_response_424 import PostDiagnosticsRebootEndpointResponse424
from ...models.post_diagnostics_reboot_endpoint_response_500 import PostDiagnosticsRebootEndpointResponse500
from ...models.post_diagnostics_reboot_endpoint_response_503 import PostDiagnosticsRebootEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostDiagnosticsRebootEndpointJsonBody | PostDiagnosticsRebootEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/diagnostics/reboot",
    }

    if isinstance(body, PostDiagnosticsRebootEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostDiagnosticsRebootEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostDiagnosticsRebootEndpointResponse400
    | PostDiagnosticsRebootEndpointResponse401
    | PostDiagnosticsRebootEndpointResponse403
    | PostDiagnosticsRebootEndpointResponse404
    | PostDiagnosticsRebootEndpointResponse405
    | PostDiagnosticsRebootEndpointResponse406
    | PostDiagnosticsRebootEndpointResponse409
    | PostDiagnosticsRebootEndpointResponse415
    | PostDiagnosticsRebootEndpointResponse422
    | PostDiagnosticsRebootEndpointResponse424
    | PostDiagnosticsRebootEndpointResponse500
    | PostDiagnosticsRebootEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostDiagnosticsRebootEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostDiagnosticsRebootEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostDiagnosticsRebootEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostDiagnosticsRebootEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostDiagnosticsRebootEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostDiagnosticsRebootEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostDiagnosticsRebootEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostDiagnosticsRebootEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostDiagnosticsRebootEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostDiagnosticsRebootEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostDiagnosticsRebootEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostDiagnosticsRebootEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostDiagnosticsRebootEndpointResponse400
    | PostDiagnosticsRebootEndpointResponse401
    | PostDiagnosticsRebootEndpointResponse403
    | PostDiagnosticsRebootEndpointResponse404
    | PostDiagnosticsRebootEndpointResponse405
    | PostDiagnosticsRebootEndpointResponse406
    | PostDiagnosticsRebootEndpointResponse409
    | PostDiagnosticsRebootEndpointResponse415
    | PostDiagnosticsRebootEndpointResponse422
    | PostDiagnosticsRebootEndpointResponse424
    | PostDiagnosticsRebootEndpointResponse500
    | PostDiagnosticsRebootEndpointResponse503
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
    body: PostDiagnosticsRebootEndpointJsonBody | PostDiagnosticsRebootEndpointDataBody | Unset = UNSET,
) -> Response[
    PostDiagnosticsRebootEndpointResponse400
    | PostDiagnosticsRebootEndpointResponse401
    | PostDiagnosticsRebootEndpointResponse403
    | PostDiagnosticsRebootEndpointResponse404
    | PostDiagnosticsRebootEndpointResponse405
    | PostDiagnosticsRebootEndpointResponse406
    | PostDiagnosticsRebootEndpointResponse409
    | PostDiagnosticsRebootEndpointResponse415
    | PostDiagnosticsRebootEndpointResponse422
    | PostDiagnosticsRebootEndpointResponse424
    | PostDiagnosticsRebootEndpointResponse500
    | PostDiagnosticsRebootEndpointResponse503
]:
    """<h3>Description:</h3>Initiates a System Reboot.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemReboot<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-reboot-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsRebootEndpointJsonBody | Unset):
        body (PostDiagnosticsRebootEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDiagnosticsRebootEndpointResponse400 | PostDiagnosticsRebootEndpointResponse401 | PostDiagnosticsRebootEndpointResponse403 | PostDiagnosticsRebootEndpointResponse404 | PostDiagnosticsRebootEndpointResponse405 | PostDiagnosticsRebootEndpointResponse406 | PostDiagnosticsRebootEndpointResponse409 | PostDiagnosticsRebootEndpointResponse415 | PostDiagnosticsRebootEndpointResponse422 | PostDiagnosticsRebootEndpointResponse424 | PostDiagnosticsRebootEndpointResponse500 | PostDiagnosticsRebootEndpointResponse503]
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
    body: PostDiagnosticsRebootEndpointJsonBody | PostDiagnosticsRebootEndpointDataBody | Unset = UNSET,
) -> (
    PostDiagnosticsRebootEndpointResponse400
    | PostDiagnosticsRebootEndpointResponse401
    | PostDiagnosticsRebootEndpointResponse403
    | PostDiagnosticsRebootEndpointResponse404
    | PostDiagnosticsRebootEndpointResponse405
    | PostDiagnosticsRebootEndpointResponse406
    | PostDiagnosticsRebootEndpointResponse409
    | PostDiagnosticsRebootEndpointResponse415
    | PostDiagnosticsRebootEndpointResponse422
    | PostDiagnosticsRebootEndpointResponse424
    | PostDiagnosticsRebootEndpointResponse500
    | PostDiagnosticsRebootEndpointResponse503
    | None
):
    """<h3>Description:</h3>Initiates a System Reboot.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemReboot<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-reboot-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsRebootEndpointJsonBody | Unset):
        body (PostDiagnosticsRebootEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDiagnosticsRebootEndpointResponse400 | PostDiagnosticsRebootEndpointResponse401 | PostDiagnosticsRebootEndpointResponse403 | PostDiagnosticsRebootEndpointResponse404 | PostDiagnosticsRebootEndpointResponse405 | PostDiagnosticsRebootEndpointResponse406 | PostDiagnosticsRebootEndpointResponse409 | PostDiagnosticsRebootEndpointResponse415 | PostDiagnosticsRebootEndpointResponse422 | PostDiagnosticsRebootEndpointResponse424 | PostDiagnosticsRebootEndpointResponse500 | PostDiagnosticsRebootEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostDiagnosticsRebootEndpointJsonBody | PostDiagnosticsRebootEndpointDataBody | Unset = UNSET,
) -> Response[
    PostDiagnosticsRebootEndpointResponse400
    | PostDiagnosticsRebootEndpointResponse401
    | PostDiagnosticsRebootEndpointResponse403
    | PostDiagnosticsRebootEndpointResponse404
    | PostDiagnosticsRebootEndpointResponse405
    | PostDiagnosticsRebootEndpointResponse406
    | PostDiagnosticsRebootEndpointResponse409
    | PostDiagnosticsRebootEndpointResponse415
    | PostDiagnosticsRebootEndpointResponse422
    | PostDiagnosticsRebootEndpointResponse424
    | PostDiagnosticsRebootEndpointResponse500
    | PostDiagnosticsRebootEndpointResponse503
]:
    """<h3>Description:</h3>Initiates a System Reboot.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemReboot<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-reboot-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsRebootEndpointJsonBody | Unset):
        body (PostDiagnosticsRebootEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDiagnosticsRebootEndpointResponse400 | PostDiagnosticsRebootEndpointResponse401 | PostDiagnosticsRebootEndpointResponse403 | PostDiagnosticsRebootEndpointResponse404 | PostDiagnosticsRebootEndpointResponse405 | PostDiagnosticsRebootEndpointResponse406 | PostDiagnosticsRebootEndpointResponse409 | PostDiagnosticsRebootEndpointResponse415 | PostDiagnosticsRebootEndpointResponse422 | PostDiagnosticsRebootEndpointResponse424 | PostDiagnosticsRebootEndpointResponse500 | PostDiagnosticsRebootEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostDiagnosticsRebootEndpointJsonBody | PostDiagnosticsRebootEndpointDataBody | Unset = UNSET,
) -> (
    PostDiagnosticsRebootEndpointResponse400
    | PostDiagnosticsRebootEndpointResponse401
    | PostDiagnosticsRebootEndpointResponse403
    | PostDiagnosticsRebootEndpointResponse404
    | PostDiagnosticsRebootEndpointResponse405
    | PostDiagnosticsRebootEndpointResponse406
    | PostDiagnosticsRebootEndpointResponse409
    | PostDiagnosticsRebootEndpointResponse415
    | PostDiagnosticsRebootEndpointResponse422
    | PostDiagnosticsRebootEndpointResponse424
    | PostDiagnosticsRebootEndpointResponse500
    | PostDiagnosticsRebootEndpointResponse503
    | None
):
    """<h3>Description:</h3>Initiates a System Reboot.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemReboot<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-reboot-post ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostDiagnosticsRebootEndpointJsonBody | Unset):
        body (PostDiagnosticsRebootEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDiagnosticsRebootEndpointResponse400 | PostDiagnosticsRebootEndpointResponse401 | PostDiagnosticsRebootEndpointResponse403 | PostDiagnosticsRebootEndpointResponse404 | PostDiagnosticsRebootEndpointResponse405 | PostDiagnosticsRebootEndpointResponse406 | PostDiagnosticsRebootEndpointResponse409 | PostDiagnosticsRebootEndpointResponse415 | PostDiagnosticsRebootEndpointResponse422 | PostDiagnosticsRebootEndpointResponse424 | PostDiagnosticsRebootEndpointResponse500 | PostDiagnosticsRebootEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
