from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_interface_apply_endpoint_response_400 import GetInterfaceApplyEndpointResponse400
from ...models.get_interface_apply_endpoint_response_401 import GetInterfaceApplyEndpointResponse401
from ...models.get_interface_apply_endpoint_response_403 import GetInterfaceApplyEndpointResponse403
from ...models.get_interface_apply_endpoint_response_404 import GetInterfaceApplyEndpointResponse404
from ...models.get_interface_apply_endpoint_response_405 import GetInterfaceApplyEndpointResponse405
from ...models.get_interface_apply_endpoint_response_406 import GetInterfaceApplyEndpointResponse406
from ...models.get_interface_apply_endpoint_response_409 import GetInterfaceApplyEndpointResponse409
from ...models.get_interface_apply_endpoint_response_415 import GetInterfaceApplyEndpointResponse415
from ...models.get_interface_apply_endpoint_response_422 import GetInterfaceApplyEndpointResponse422
from ...models.get_interface_apply_endpoint_response_424 import GetInterfaceApplyEndpointResponse424
from ...models.get_interface_apply_endpoint_response_500 import GetInterfaceApplyEndpointResponse500
from ...models.get_interface_apply_endpoint_response_503 import GetInterfaceApplyEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/interface/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetInterfaceApplyEndpointResponse400
    | GetInterfaceApplyEndpointResponse401
    | GetInterfaceApplyEndpointResponse403
    | GetInterfaceApplyEndpointResponse404
    | GetInterfaceApplyEndpointResponse405
    | GetInterfaceApplyEndpointResponse406
    | GetInterfaceApplyEndpointResponse409
    | GetInterfaceApplyEndpointResponse415
    | GetInterfaceApplyEndpointResponse422
    | GetInterfaceApplyEndpointResponse424
    | GetInterfaceApplyEndpointResponse500
    | GetInterfaceApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetInterfaceApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetInterfaceApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetInterfaceApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetInterfaceApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetInterfaceApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetInterfaceApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetInterfaceApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetInterfaceApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetInterfaceApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetInterfaceApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetInterfaceApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetInterfaceApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetInterfaceApplyEndpointResponse400
    | GetInterfaceApplyEndpointResponse401
    | GetInterfaceApplyEndpointResponse403
    | GetInterfaceApplyEndpointResponse404
    | GetInterfaceApplyEndpointResponse405
    | GetInterfaceApplyEndpointResponse406
    | GetInterfaceApplyEndpointResponse409
    | GetInterfaceApplyEndpointResponse415
    | GetInterfaceApplyEndpointResponse422
    | GetInterfaceApplyEndpointResponse424
    | GetInterfaceApplyEndpointResponse500
    | GetInterfaceApplyEndpointResponse503
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
) -> Response[
    GetInterfaceApplyEndpointResponse400
    | GetInterfaceApplyEndpointResponse401
    | GetInterfaceApplyEndpointResponse403
    | GetInterfaceApplyEndpointResponse404
    | GetInterfaceApplyEndpointResponse405
    | GetInterfaceApplyEndpointResponse406
    | GetInterfaceApplyEndpointResponse409
    | GetInterfaceApplyEndpointResponse415
    | GetInterfaceApplyEndpointResponse422
    | GetInterfaceApplyEndpointResponse424
    | GetInterfaceApplyEndpointResponse500
    | GetInterfaceApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending interfaces status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInterfaceApplyEndpointResponse400 | GetInterfaceApplyEndpointResponse401 | GetInterfaceApplyEndpointResponse403 | GetInterfaceApplyEndpointResponse404 | GetInterfaceApplyEndpointResponse405 | GetInterfaceApplyEndpointResponse406 | GetInterfaceApplyEndpointResponse409 | GetInterfaceApplyEndpointResponse415 | GetInterfaceApplyEndpointResponse422 | GetInterfaceApplyEndpointResponse424 | GetInterfaceApplyEndpointResponse500 | GetInterfaceApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetInterfaceApplyEndpointResponse400
    | GetInterfaceApplyEndpointResponse401
    | GetInterfaceApplyEndpointResponse403
    | GetInterfaceApplyEndpointResponse404
    | GetInterfaceApplyEndpointResponse405
    | GetInterfaceApplyEndpointResponse406
    | GetInterfaceApplyEndpointResponse409
    | GetInterfaceApplyEndpointResponse415
    | GetInterfaceApplyEndpointResponse422
    | GetInterfaceApplyEndpointResponse424
    | GetInterfaceApplyEndpointResponse500
    | GetInterfaceApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending interfaces status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInterfaceApplyEndpointResponse400 | GetInterfaceApplyEndpointResponse401 | GetInterfaceApplyEndpointResponse403 | GetInterfaceApplyEndpointResponse404 | GetInterfaceApplyEndpointResponse405 | GetInterfaceApplyEndpointResponse406 | GetInterfaceApplyEndpointResponse409 | GetInterfaceApplyEndpointResponse415 | GetInterfaceApplyEndpointResponse422 | GetInterfaceApplyEndpointResponse424 | GetInterfaceApplyEndpointResponse500 | GetInterfaceApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetInterfaceApplyEndpointResponse400
    | GetInterfaceApplyEndpointResponse401
    | GetInterfaceApplyEndpointResponse403
    | GetInterfaceApplyEndpointResponse404
    | GetInterfaceApplyEndpointResponse405
    | GetInterfaceApplyEndpointResponse406
    | GetInterfaceApplyEndpointResponse409
    | GetInterfaceApplyEndpointResponse415
    | GetInterfaceApplyEndpointResponse422
    | GetInterfaceApplyEndpointResponse424
    | GetInterfaceApplyEndpointResponse500
    | GetInterfaceApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending interfaces status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInterfaceApplyEndpointResponse400 | GetInterfaceApplyEndpointResponse401 | GetInterfaceApplyEndpointResponse403 | GetInterfaceApplyEndpointResponse404 | GetInterfaceApplyEndpointResponse405 | GetInterfaceApplyEndpointResponse406 | GetInterfaceApplyEndpointResponse409 | GetInterfaceApplyEndpointResponse415 | GetInterfaceApplyEndpointResponse422 | GetInterfaceApplyEndpointResponse424 | GetInterfaceApplyEndpointResponse500 | GetInterfaceApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetInterfaceApplyEndpointResponse400
    | GetInterfaceApplyEndpointResponse401
    | GetInterfaceApplyEndpointResponse403
    | GetInterfaceApplyEndpointResponse404
    | GetInterfaceApplyEndpointResponse405
    | GetInterfaceApplyEndpointResponse406
    | GetInterfaceApplyEndpointResponse409
    | GetInterfaceApplyEndpointResponse415
    | GetInterfaceApplyEndpointResponse422
    | GetInterfaceApplyEndpointResponse424
    | GetInterfaceApplyEndpointResponse500
    | GetInterfaceApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending interfaces status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-apply-get ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInterfaceApplyEndpointResponse400 | GetInterfaceApplyEndpointResponse401 | GetInterfaceApplyEndpointResponse403 | GetInterfaceApplyEndpointResponse404 | GetInterfaceApplyEndpointResponse405 | GetInterfaceApplyEndpointResponse406 | GetInterfaceApplyEndpointResponse409 | GetInterfaceApplyEndpointResponse415 | GetInterfaceApplyEndpointResponse422 | GetInterfaceApplyEndpointResponse424 | GetInterfaceApplyEndpointResponse500 | GetInterfaceApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
