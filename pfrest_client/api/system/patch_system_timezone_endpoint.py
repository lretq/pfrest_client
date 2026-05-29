from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_timezone_endpoint_data_body import PatchSystemTimezoneEndpointDataBody
from ...models.patch_system_timezone_endpoint_json_body import PatchSystemTimezoneEndpointJsonBody
from ...models.patch_system_timezone_endpoint_response_400 import PatchSystemTimezoneEndpointResponse400
from ...models.patch_system_timezone_endpoint_response_401 import PatchSystemTimezoneEndpointResponse401
from ...models.patch_system_timezone_endpoint_response_403 import PatchSystemTimezoneEndpointResponse403
from ...models.patch_system_timezone_endpoint_response_404 import PatchSystemTimezoneEndpointResponse404
from ...models.patch_system_timezone_endpoint_response_405 import PatchSystemTimezoneEndpointResponse405
from ...models.patch_system_timezone_endpoint_response_406 import PatchSystemTimezoneEndpointResponse406
from ...models.patch_system_timezone_endpoint_response_409 import PatchSystemTimezoneEndpointResponse409
from ...models.patch_system_timezone_endpoint_response_415 import PatchSystemTimezoneEndpointResponse415
from ...models.patch_system_timezone_endpoint_response_422 import PatchSystemTimezoneEndpointResponse422
from ...models.patch_system_timezone_endpoint_response_424 import PatchSystemTimezoneEndpointResponse424
from ...models.patch_system_timezone_endpoint_response_500 import PatchSystemTimezoneEndpointResponse500
from ...models.patch_system_timezone_endpoint_response_503 import PatchSystemTimezoneEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemTimezoneEndpointJsonBody | PatchSystemTimezoneEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/timezone",
    }

    if isinstance(body, PatchSystemTimezoneEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemTimezoneEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemTimezoneEndpointResponse400
    | PatchSystemTimezoneEndpointResponse401
    | PatchSystemTimezoneEndpointResponse403
    | PatchSystemTimezoneEndpointResponse404
    | PatchSystemTimezoneEndpointResponse405
    | PatchSystemTimezoneEndpointResponse406
    | PatchSystemTimezoneEndpointResponse409
    | PatchSystemTimezoneEndpointResponse415
    | PatchSystemTimezoneEndpointResponse422
    | PatchSystemTimezoneEndpointResponse424
    | PatchSystemTimezoneEndpointResponse500
    | PatchSystemTimezoneEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemTimezoneEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemTimezoneEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemTimezoneEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemTimezoneEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemTimezoneEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemTimezoneEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemTimezoneEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemTimezoneEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemTimezoneEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemTimezoneEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemTimezoneEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemTimezoneEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemTimezoneEndpointResponse400
    | PatchSystemTimezoneEndpointResponse401
    | PatchSystemTimezoneEndpointResponse403
    | PatchSystemTimezoneEndpointResponse404
    | PatchSystemTimezoneEndpointResponse405
    | PatchSystemTimezoneEndpointResponse406
    | PatchSystemTimezoneEndpointResponse409
    | PatchSystemTimezoneEndpointResponse415
    | PatchSystemTimezoneEndpointResponse422
    | PatchSystemTimezoneEndpointResponse424
    | PatchSystemTimezoneEndpointResponse500
    | PatchSystemTimezoneEndpointResponse503
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
    body: PatchSystemTimezoneEndpointJsonBody | PatchSystemTimezoneEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemTimezoneEndpointResponse400
    | PatchSystemTimezoneEndpointResponse401
    | PatchSystemTimezoneEndpointResponse403
    | PatchSystemTimezoneEndpointResponse404
    | PatchSystemTimezoneEndpointResponse405
    | PatchSystemTimezoneEndpointResponse406
    | PatchSystemTimezoneEndpointResponse409
    | PatchSystemTimezoneEndpointResponse415
    | PatchSystemTimezoneEndpointResponse422
    | PatchSystemTimezoneEndpointResponse424
    | PatchSystemTimezoneEndpointResponse500
    | PatchSystemTimezoneEndpointResponse503
]:
    """<h3>Description:</h3>Updates the system timezone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTimezone<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-timezone-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemTimezoneEndpointJsonBody | Unset):
        body (PatchSystemTimezoneEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemTimezoneEndpointResponse400 | PatchSystemTimezoneEndpointResponse401 | PatchSystemTimezoneEndpointResponse403 | PatchSystemTimezoneEndpointResponse404 | PatchSystemTimezoneEndpointResponse405 | PatchSystemTimezoneEndpointResponse406 | PatchSystemTimezoneEndpointResponse409 | PatchSystemTimezoneEndpointResponse415 | PatchSystemTimezoneEndpointResponse422 | PatchSystemTimezoneEndpointResponse424 | PatchSystemTimezoneEndpointResponse500 | PatchSystemTimezoneEndpointResponse503]
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
    body: PatchSystemTimezoneEndpointJsonBody | PatchSystemTimezoneEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemTimezoneEndpointResponse400
    | PatchSystemTimezoneEndpointResponse401
    | PatchSystemTimezoneEndpointResponse403
    | PatchSystemTimezoneEndpointResponse404
    | PatchSystemTimezoneEndpointResponse405
    | PatchSystemTimezoneEndpointResponse406
    | PatchSystemTimezoneEndpointResponse409
    | PatchSystemTimezoneEndpointResponse415
    | PatchSystemTimezoneEndpointResponse422
    | PatchSystemTimezoneEndpointResponse424
    | PatchSystemTimezoneEndpointResponse500
    | PatchSystemTimezoneEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates the system timezone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTimezone<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-timezone-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemTimezoneEndpointJsonBody | Unset):
        body (PatchSystemTimezoneEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemTimezoneEndpointResponse400 | PatchSystemTimezoneEndpointResponse401 | PatchSystemTimezoneEndpointResponse403 | PatchSystemTimezoneEndpointResponse404 | PatchSystemTimezoneEndpointResponse405 | PatchSystemTimezoneEndpointResponse406 | PatchSystemTimezoneEndpointResponse409 | PatchSystemTimezoneEndpointResponse415 | PatchSystemTimezoneEndpointResponse422 | PatchSystemTimezoneEndpointResponse424 | PatchSystemTimezoneEndpointResponse500 | PatchSystemTimezoneEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemTimezoneEndpointJsonBody | PatchSystemTimezoneEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemTimezoneEndpointResponse400
    | PatchSystemTimezoneEndpointResponse401
    | PatchSystemTimezoneEndpointResponse403
    | PatchSystemTimezoneEndpointResponse404
    | PatchSystemTimezoneEndpointResponse405
    | PatchSystemTimezoneEndpointResponse406
    | PatchSystemTimezoneEndpointResponse409
    | PatchSystemTimezoneEndpointResponse415
    | PatchSystemTimezoneEndpointResponse422
    | PatchSystemTimezoneEndpointResponse424
    | PatchSystemTimezoneEndpointResponse500
    | PatchSystemTimezoneEndpointResponse503
]:
    """<h3>Description:</h3>Updates the system timezone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTimezone<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-timezone-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemTimezoneEndpointJsonBody | Unset):
        body (PatchSystemTimezoneEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemTimezoneEndpointResponse400 | PatchSystemTimezoneEndpointResponse401 | PatchSystemTimezoneEndpointResponse403 | PatchSystemTimezoneEndpointResponse404 | PatchSystemTimezoneEndpointResponse405 | PatchSystemTimezoneEndpointResponse406 | PatchSystemTimezoneEndpointResponse409 | PatchSystemTimezoneEndpointResponse415 | PatchSystemTimezoneEndpointResponse422 | PatchSystemTimezoneEndpointResponse424 | PatchSystemTimezoneEndpointResponse500 | PatchSystemTimezoneEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemTimezoneEndpointJsonBody | PatchSystemTimezoneEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemTimezoneEndpointResponse400
    | PatchSystemTimezoneEndpointResponse401
    | PatchSystemTimezoneEndpointResponse403
    | PatchSystemTimezoneEndpointResponse404
    | PatchSystemTimezoneEndpointResponse405
    | PatchSystemTimezoneEndpointResponse406
    | PatchSystemTimezoneEndpointResponse409
    | PatchSystemTimezoneEndpointResponse415
    | PatchSystemTimezoneEndpointResponse422
    | PatchSystemTimezoneEndpointResponse424
    | PatchSystemTimezoneEndpointResponse500
    | PatchSystemTimezoneEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates the system timezone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemTimezone<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-timezone-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemTimezoneEndpointJsonBody | Unset):
        body (PatchSystemTimezoneEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemTimezoneEndpointResponse400 | PatchSystemTimezoneEndpointResponse401 | PatchSystemTimezoneEndpointResponse403 | PatchSystemTimezoneEndpointResponse404 | PatchSystemTimezoneEndpointResponse405 | PatchSystemTimezoneEndpointResponse406 | PatchSystemTimezoneEndpointResponse409 | PatchSystemTimezoneEndpointResponse415 | PatchSystemTimezoneEndpointResponse422 | PatchSystemTimezoneEndpointResponse424 | PatchSystemTimezoneEndpointResponse500 | PatchSystemTimezoneEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
