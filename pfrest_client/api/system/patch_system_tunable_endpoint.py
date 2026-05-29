from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_tunable_endpoint_data_body import PatchSystemTunableEndpointDataBody
from ...models.patch_system_tunable_endpoint_json_body import PatchSystemTunableEndpointJsonBody
from ...models.patch_system_tunable_endpoint_response_400 import PatchSystemTunableEndpointResponse400
from ...models.patch_system_tunable_endpoint_response_401 import PatchSystemTunableEndpointResponse401
from ...models.patch_system_tunable_endpoint_response_403 import PatchSystemTunableEndpointResponse403
from ...models.patch_system_tunable_endpoint_response_404 import PatchSystemTunableEndpointResponse404
from ...models.patch_system_tunable_endpoint_response_405 import PatchSystemTunableEndpointResponse405
from ...models.patch_system_tunable_endpoint_response_406 import PatchSystemTunableEndpointResponse406
from ...models.patch_system_tunable_endpoint_response_409 import PatchSystemTunableEndpointResponse409
from ...models.patch_system_tunable_endpoint_response_415 import PatchSystemTunableEndpointResponse415
from ...models.patch_system_tunable_endpoint_response_422 import PatchSystemTunableEndpointResponse422
from ...models.patch_system_tunable_endpoint_response_424 import PatchSystemTunableEndpointResponse424
from ...models.patch_system_tunable_endpoint_response_500 import PatchSystemTunableEndpointResponse500
from ...models.patch_system_tunable_endpoint_response_503 import PatchSystemTunableEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemTunableEndpointJsonBody | PatchSystemTunableEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/tunable",
    }

    if isinstance(body, PatchSystemTunableEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemTunableEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemTunableEndpointResponse400
    | PatchSystemTunableEndpointResponse401
    | PatchSystemTunableEndpointResponse403
    | PatchSystemTunableEndpointResponse404
    | PatchSystemTunableEndpointResponse405
    | PatchSystemTunableEndpointResponse406
    | PatchSystemTunableEndpointResponse409
    | PatchSystemTunableEndpointResponse415
    | PatchSystemTunableEndpointResponse422
    | PatchSystemTunableEndpointResponse424
    | PatchSystemTunableEndpointResponse500
    | PatchSystemTunableEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemTunableEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemTunableEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemTunableEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemTunableEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemTunableEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemTunableEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemTunableEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemTunableEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemTunableEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemTunableEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemTunableEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemTunableEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemTunableEndpointResponse400
    | PatchSystemTunableEndpointResponse401
    | PatchSystemTunableEndpointResponse403
    | PatchSystemTunableEndpointResponse404
    | PatchSystemTunableEndpointResponse405
    | PatchSystemTunableEndpointResponse406
    | PatchSystemTunableEndpointResponse409
    | PatchSystemTunableEndpointResponse415
    | PatchSystemTunableEndpointResponse422
    | PatchSystemTunableEndpointResponse424
    | PatchSystemTunableEndpointResponse500
    | PatchSystemTunableEndpointResponse503
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
    body: PatchSystemTunableEndpointJsonBody | PatchSystemTunableEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemTunableEndpointResponse400
    | PatchSystemTunableEndpointResponse401
    | PatchSystemTunableEndpointResponse403
    | PatchSystemTunableEndpointResponse404
    | PatchSystemTunableEndpointResponse405
    | PatchSystemTunableEndpointResponse406
    | PatchSystemTunableEndpointResponse409
    | PatchSystemTunableEndpointResponse415
    | PatchSystemTunableEndpointResponse422
    | PatchSystemTunableEndpointResponse424
    | PatchSystemTunableEndpointResponse500
    | PatchSystemTunableEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing System Tunable.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunable-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchSystemTunableEndpointJsonBody | Unset):
        body (PatchSystemTunableEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemTunableEndpointResponse400 | PatchSystemTunableEndpointResponse401 | PatchSystemTunableEndpointResponse403 | PatchSystemTunableEndpointResponse404 | PatchSystemTunableEndpointResponse405 | PatchSystemTunableEndpointResponse406 | PatchSystemTunableEndpointResponse409 | PatchSystemTunableEndpointResponse415 | PatchSystemTunableEndpointResponse422 | PatchSystemTunableEndpointResponse424 | PatchSystemTunableEndpointResponse500 | PatchSystemTunableEndpointResponse503]
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
    body: PatchSystemTunableEndpointJsonBody | PatchSystemTunableEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemTunableEndpointResponse400
    | PatchSystemTunableEndpointResponse401
    | PatchSystemTunableEndpointResponse403
    | PatchSystemTunableEndpointResponse404
    | PatchSystemTunableEndpointResponse405
    | PatchSystemTunableEndpointResponse406
    | PatchSystemTunableEndpointResponse409
    | PatchSystemTunableEndpointResponse415
    | PatchSystemTunableEndpointResponse422
    | PatchSystemTunableEndpointResponse424
    | PatchSystemTunableEndpointResponse500
    | PatchSystemTunableEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing System Tunable.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunable-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchSystemTunableEndpointJsonBody | Unset):
        body (PatchSystemTunableEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemTunableEndpointResponse400 | PatchSystemTunableEndpointResponse401 | PatchSystemTunableEndpointResponse403 | PatchSystemTunableEndpointResponse404 | PatchSystemTunableEndpointResponse405 | PatchSystemTunableEndpointResponse406 | PatchSystemTunableEndpointResponse409 | PatchSystemTunableEndpointResponse415 | PatchSystemTunableEndpointResponse422 | PatchSystemTunableEndpointResponse424 | PatchSystemTunableEndpointResponse500 | PatchSystemTunableEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemTunableEndpointJsonBody | PatchSystemTunableEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemTunableEndpointResponse400
    | PatchSystemTunableEndpointResponse401
    | PatchSystemTunableEndpointResponse403
    | PatchSystemTunableEndpointResponse404
    | PatchSystemTunableEndpointResponse405
    | PatchSystemTunableEndpointResponse406
    | PatchSystemTunableEndpointResponse409
    | PatchSystemTunableEndpointResponse415
    | PatchSystemTunableEndpointResponse422
    | PatchSystemTunableEndpointResponse424
    | PatchSystemTunableEndpointResponse500
    | PatchSystemTunableEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing System Tunable.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunable-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchSystemTunableEndpointJsonBody | Unset):
        body (PatchSystemTunableEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemTunableEndpointResponse400 | PatchSystemTunableEndpointResponse401 | PatchSystemTunableEndpointResponse403 | PatchSystemTunableEndpointResponse404 | PatchSystemTunableEndpointResponse405 | PatchSystemTunableEndpointResponse406 | PatchSystemTunableEndpointResponse409 | PatchSystemTunableEndpointResponse415 | PatchSystemTunableEndpointResponse422 | PatchSystemTunableEndpointResponse424 | PatchSystemTunableEndpointResponse500 | PatchSystemTunableEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemTunableEndpointJsonBody | PatchSystemTunableEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemTunableEndpointResponse400
    | PatchSystemTunableEndpointResponse401
    | PatchSystemTunableEndpointResponse403
    | PatchSystemTunableEndpointResponse404
    | PatchSystemTunableEndpointResponse405
    | PatchSystemTunableEndpointResponse406
    | PatchSystemTunableEndpointResponse409
    | PatchSystemTunableEndpointResponse415
    | PatchSystemTunableEndpointResponse422
    | PatchSystemTunableEndpointResponse424
    | PatchSystemTunableEndpointResponse500
    | PatchSystemTunableEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing System Tunable.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTunable<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-tunable-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchSystemTunableEndpointJsonBody | Unset):
        body (PatchSystemTunableEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemTunableEndpointResponse400 | PatchSystemTunableEndpointResponse401 | PatchSystemTunableEndpointResponse403 | PatchSystemTunableEndpointResponse404 | PatchSystemTunableEndpointResponse405 | PatchSystemTunableEndpointResponse406 | PatchSystemTunableEndpointResponse409 | PatchSystemTunableEndpointResponse415 | PatchSystemTunableEndpointResponse422 | PatchSystemTunableEndpointResponse424 | PatchSystemTunableEndpointResponse500 | PatchSystemTunableEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
