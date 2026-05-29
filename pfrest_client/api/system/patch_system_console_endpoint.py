from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_console_endpoint_data_body import PatchSystemConsoleEndpointDataBody
from ...models.patch_system_console_endpoint_json_body import PatchSystemConsoleEndpointJsonBody
from ...models.patch_system_console_endpoint_response_400 import PatchSystemConsoleEndpointResponse400
from ...models.patch_system_console_endpoint_response_401 import PatchSystemConsoleEndpointResponse401
from ...models.patch_system_console_endpoint_response_403 import PatchSystemConsoleEndpointResponse403
from ...models.patch_system_console_endpoint_response_404 import PatchSystemConsoleEndpointResponse404
from ...models.patch_system_console_endpoint_response_405 import PatchSystemConsoleEndpointResponse405
from ...models.patch_system_console_endpoint_response_406 import PatchSystemConsoleEndpointResponse406
from ...models.patch_system_console_endpoint_response_409 import PatchSystemConsoleEndpointResponse409
from ...models.patch_system_console_endpoint_response_415 import PatchSystemConsoleEndpointResponse415
from ...models.patch_system_console_endpoint_response_422 import PatchSystemConsoleEndpointResponse422
from ...models.patch_system_console_endpoint_response_424 import PatchSystemConsoleEndpointResponse424
from ...models.patch_system_console_endpoint_response_500 import PatchSystemConsoleEndpointResponse500
from ...models.patch_system_console_endpoint_response_503 import PatchSystemConsoleEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemConsoleEndpointJsonBody | PatchSystemConsoleEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/console",
    }

    if isinstance(body, PatchSystemConsoleEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemConsoleEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemConsoleEndpointResponse400
    | PatchSystemConsoleEndpointResponse401
    | PatchSystemConsoleEndpointResponse403
    | PatchSystemConsoleEndpointResponse404
    | PatchSystemConsoleEndpointResponse405
    | PatchSystemConsoleEndpointResponse406
    | PatchSystemConsoleEndpointResponse409
    | PatchSystemConsoleEndpointResponse415
    | PatchSystemConsoleEndpointResponse422
    | PatchSystemConsoleEndpointResponse424
    | PatchSystemConsoleEndpointResponse500
    | PatchSystemConsoleEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemConsoleEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemConsoleEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemConsoleEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemConsoleEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemConsoleEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemConsoleEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemConsoleEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemConsoleEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemConsoleEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemConsoleEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemConsoleEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemConsoleEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemConsoleEndpointResponse400
    | PatchSystemConsoleEndpointResponse401
    | PatchSystemConsoleEndpointResponse403
    | PatchSystemConsoleEndpointResponse404
    | PatchSystemConsoleEndpointResponse405
    | PatchSystemConsoleEndpointResponse406
    | PatchSystemConsoleEndpointResponse409
    | PatchSystemConsoleEndpointResponse415
    | PatchSystemConsoleEndpointResponse422
    | PatchSystemConsoleEndpointResponse424
    | PatchSystemConsoleEndpointResponse500
    | PatchSystemConsoleEndpointResponse503
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
    body: PatchSystemConsoleEndpointJsonBody | PatchSystemConsoleEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemConsoleEndpointResponse400
    | PatchSystemConsoleEndpointResponse401
    | PatchSystemConsoleEndpointResponse403
    | PatchSystemConsoleEndpointResponse404
    | PatchSystemConsoleEndpointResponse405
    | PatchSystemConsoleEndpointResponse406
    | PatchSystemConsoleEndpointResponse409
    | PatchSystemConsoleEndpointResponse415
    | PatchSystemConsoleEndpointResponse422
    | PatchSystemConsoleEndpointResponse424
    | PatchSystemConsoleEndpointResponse500
    | PatchSystemConsoleEndpointResponse503
]:
    """<h3>Description:</h3>Updates current System Console.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemConsole<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-console-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemConsoleEndpointJsonBody | Unset):
        body (PatchSystemConsoleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemConsoleEndpointResponse400 | PatchSystemConsoleEndpointResponse401 | PatchSystemConsoleEndpointResponse403 | PatchSystemConsoleEndpointResponse404 | PatchSystemConsoleEndpointResponse405 | PatchSystemConsoleEndpointResponse406 | PatchSystemConsoleEndpointResponse409 | PatchSystemConsoleEndpointResponse415 | PatchSystemConsoleEndpointResponse422 | PatchSystemConsoleEndpointResponse424 | PatchSystemConsoleEndpointResponse500 | PatchSystemConsoleEndpointResponse503]
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
    body: PatchSystemConsoleEndpointJsonBody | PatchSystemConsoleEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemConsoleEndpointResponse400
    | PatchSystemConsoleEndpointResponse401
    | PatchSystemConsoleEndpointResponse403
    | PatchSystemConsoleEndpointResponse404
    | PatchSystemConsoleEndpointResponse405
    | PatchSystemConsoleEndpointResponse406
    | PatchSystemConsoleEndpointResponse409
    | PatchSystemConsoleEndpointResponse415
    | PatchSystemConsoleEndpointResponse422
    | PatchSystemConsoleEndpointResponse424
    | PatchSystemConsoleEndpointResponse500
    | PatchSystemConsoleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current System Console.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemConsole<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-console-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemConsoleEndpointJsonBody | Unset):
        body (PatchSystemConsoleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemConsoleEndpointResponse400 | PatchSystemConsoleEndpointResponse401 | PatchSystemConsoleEndpointResponse403 | PatchSystemConsoleEndpointResponse404 | PatchSystemConsoleEndpointResponse405 | PatchSystemConsoleEndpointResponse406 | PatchSystemConsoleEndpointResponse409 | PatchSystemConsoleEndpointResponse415 | PatchSystemConsoleEndpointResponse422 | PatchSystemConsoleEndpointResponse424 | PatchSystemConsoleEndpointResponse500 | PatchSystemConsoleEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemConsoleEndpointJsonBody | PatchSystemConsoleEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemConsoleEndpointResponse400
    | PatchSystemConsoleEndpointResponse401
    | PatchSystemConsoleEndpointResponse403
    | PatchSystemConsoleEndpointResponse404
    | PatchSystemConsoleEndpointResponse405
    | PatchSystemConsoleEndpointResponse406
    | PatchSystemConsoleEndpointResponse409
    | PatchSystemConsoleEndpointResponse415
    | PatchSystemConsoleEndpointResponse422
    | PatchSystemConsoleEndpointResponse424
    | PatchSystemConsoleEndpointResponse500
    | PatchSystemConsoleEndpointResponse503
]:
    """<h3>Description:</h3>Updates current System Console.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemConsole<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-console-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemConsoleEndpointJsonBody | Unset):
        body (PatchSystemConsoleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemConsoleEndpointResponse400 | PatchSystemConsoleEndpointResponse401 | PatchSystemConsoleEndpointResponse403 | PatchSystemConsoleEndpointResponse404 | PatchSystemConsoleEndpointResponse405 | PatchSystemConsoleEndpointResponse406 | PatchSystemConsoleEndpointResponse409 | PatchSystemConsoleEndpointResponse415 | PatchSystemConsoleEndpointResponse422 | PatchSystemConsoleEndpointResponse424 | PatchSystemConsoleEndpointResponse500 | PatchSystemConsoleEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemConsoleEndpointJsonBody | PatchSystemConsoleEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemConsoleEndpointResponse400
    | PatchSystemConsoleEndpointResponse401
    | PatchSystemConsoleEndpointResponse403
    | PatchSystemConsoleEndpointResponse404
    | PatchSystemConsoleEndpointResponse405
    | PatchSystemConsoleEndpointResponse406
    | PatchSystemConsoleEndpointResponse409
    | PatchSystemConsoleEndpointResponse415
    | PatchSystemConsoleEndpointResponse422
    | PatchSystemConsoleEndpointResponse424
    | PatchSystemConsoleEndpointResponse500
    | PatchSystemConsoleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current System Console.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemConsole<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-console-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemConsoleEndpointJsonBody | Unset):
        body (PatchSystemConsoleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemConsoleEndpointResponse400 | PatchSystemConsoleEndpointResponse401 | PatchSystemConsoleEndpointResponse403 | PatchSystemConsoleEndpointResponse404 | PatchSystemConsoleEndpointResponse405 | PatchSystemConsoleEndpointResponse406 | PatchSystemConsoleEndpointResponse409 | PatchSystemConsoleEndpointResponse415 | PatchSystemConsoleEndpointResponse422 | PatchSystemConsoleEndpointResponse424 | PatchSystemConsoleEndpointResponse500 | PatchSystemConsoleEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
