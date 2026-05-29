from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_system_package_endpoint_response_400 import DeleteSystemPackageEndpointResponse400
from ...models.delete_system_package_endpoint_response_401 import DeleteSystemPackageEndpointResponse401
from ...models.delete_system_package_endpoint_response_403 import DeleteSystemPackageEndpointResponse403
from ...models.delete_system_package_endpoint_response_404 import DeleteSystemPackageEndpointResponse404
from ...models.delete_system_package_endpoint_response_405 import DeleteSystemPackageEndpointResponse405
from ...models.delete_system_package_endpoint_response_406 import DeleteSystemPackageEndpointResponse406
from ...models.delete_system_package_endpoint_response_409 import DeleteSystemPackageEndpointResponse409
from ...models.delete_system_package_endpoint_response_415 import DeleteSystemPackageEndpointResponse415
from ...models.delete_system_package_endpoint_response_422 import DeleteSystemPackageEndpointResponse422
from ...models.delete_system_package_endpoint_response_424 import DeleteSystemPackageEndpointResponse424
from ...models.delete_system_package_endpoint_response_500 import DeleteSystemPackageEndpointResponse500
from ...models.delete_system_package_endpoint_response_503 import DeleteSystemPackageEndpointResponse503
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/system/package",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteSystemPackageEndpointResponse400
    | DeleteSystemPackageEndpointResponse401
    | DeleteSystemPackageEndpointResponse403
    | DeleteSystemPackageEndpointResponse404
    | DeleteSystemPackageEndpointResponse405
    | DeleteSystemPackageEndpointResponse406
    | DeleteSystemPackageEndpointResponse409
    | DeleteSystemPackageEndpointResponse415
    | DeleteSystemPackageEndpointResponse422
    | DeleteSystemPackageEndpointResponse424
    | DeleteSystemPackageEndpointResponse500
    | DeleteSystemPackageEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteSystemPackageEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteSystemPackageEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteSystemPackageEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteSystemPackageEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteSystemPackageEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteSystemPackageEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteSystemPackageEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteSystemPackageEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteSystemPackageEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteSystemPackageEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteSystemPackageEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteSystemPackageEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteSystemPackageEndpointResponse400
    | DeleteSystemPackageEndpointResponse401
    | DeleteSystemPackageEndpointResponse403
    | DeleteSystemPackageEndpointResponse404
    | DeleteSystemPackageEndpointResponse405
    | DeleteSystemPackageEndpointResponse406
    | DeleteSystemPackageEndpointResponse409
    | DeleteSystemPackageEndpointResponse415
    | DeleteSystemPackageEndpointResponse422
    | DeleteSystemPackageEndpointResponse424
    | DeleteSystemPackageEndpointResponse500
    | DeleteSystemPackageEndpointResponse503
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
    id: int | str,
) -> Response[
    DeleteSystemPackageEndpointResponse400
    | DeleteSystemPackageEndpointResponse401
    | DeleteSystemPackageEndpointResponse403
    | DeleteSystemPackageEndpointResponse404
    | DeleteSystemPackageEndpointResponse405
    | DeleteSystemPackageEndpointResponse406
    | DeleteSystemPackageEndpointResponse409
    | DeleteSystemPackageEndpointResponse415
    | DeleteSystemPackageEndpointResponse422
    | DeleteSystemPackageEndpointResponse424
    | DeleteSystemPackageEndpointResponse500
    | DeleteSystemPackageEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Package.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Package<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-package-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSystemPackageEndpointResponse400 | DeleteSystemPackageEndpointResponse401 | DeleteSystemPackageEndpointResponse403 | DeleteSystemPackageEndpointResponse404 | DeleteSystemPackageEndpointResponse405 | DeleteSystemPackageEndpointResponse406 | DeleteSystemPackageEndpointResponse409 | DeleteSystemPackageEndpointResponse415 | DeleteSystemPackageEndpointResponse422 | DeleteSystemPackageEndpointResponse424 | DeleteSystemPackageEndpointResponse500 | DeleteSystemPackageEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteSystemPackageEndpointResponse400
    | DeleteSystemPackageEndpointResponse401
    | DeleteSystemPackageEndpointResponse403
    | DeleteSystemPackageEndpointResponse404
    | DeleteSystemPackageEndpointResponse405
    | DeleteSystemPackageEndpointResponse406
    | DeleteSystemPackageEndpointResponse409
    | DeleteSystemPackageEndpointResponse415
    | DeleteSystemPackageEndpointResponse422
    | DeleteSystemPackageEndpointResponse424
    | DeleteSystemPackageEndpointResponse500
    | DeleteSystemPackageEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Package.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Package<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-package-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSystemPackageEndpointResponse400 | DeleteSystemPackageEndpointResponse401 | DeleteSystemPackageEndpointResponse403 | DeleteSystemPackageEndpointResponse404 | DeleteSystemPackageEndpointResponse405 | DeleteSystemPackageEndpointResponse406 | DeleteSystemPackageEndpointResponse409 | DeleteSystemPackageEndpointResponse415 | DeleteSystemPackageEndpointResponse422 | DeleteSystemPackageEndpointResponse424 | DeleteSystemPackageEndpointResponse500 | DeleteSystemPackageEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    DeleteSystemPackageEndpointResponse400
    | DeleteSystemPackageEndpointResponse401
    | DeleteSystemPackageEndpointResponse403
    | DeleteSystemPackageEndpointResponse404
    | DeleteSystemPackageEndpointResponse405
    | DeleteSystemPackageEndpointResponse406
    | DeleteSystemPackageEndpointResponse409
    | DeleteSystemPackageEndpointResponse415
    | DeleteSystemPackageEndpointResponse422
    | DeleteSystemPackageEndpointResponse424
    | DeleteSystemPackageEndpointResponse500
    | DeleteSystemPackageEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Package.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Package<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-package-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSystemPackageEndpointResponse400 | DeleteSystemPackageEndpointResponse401 | DeleteSystemPackageEndpointResponse403 | DeleteSystemPackageEndpointResponse404 | DeleteSystemPackageEndpointResponse405 | DeleteSystemPackageEndpointResponse406 | DeleteSystemPackageEndpointResponse409 | DeleteSystemPackageEndpointResponse415 | DeleteSystemPackageEndpointResponse422 | DeleteSystemPackageEndpointResponse424 | DeleteSystemPackageEndpointResponse500 | DeleteSystemPackageEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteSystemPackageEndpointResponse400
    | DeleteSystemPackageEndpointResponse401
    | DeleteSystemPackageEndpointResponse403
    | DeleteSystemPackageEndpointResponse404
    | DeleteSystemPackageEndpointResponse405
    | DeleteSystemPackageEndpointResponse406
    | DeleteSystemPackageEndpointResponse409
    | DeleteSystemPackageEndpointResponse415
    | DeleteSystemPackageEndpointResponse422
    | DeleteSystemPackageEndpointResponse424
    | DeleteSystemPackageEndpointResponse500
    | DeleteSystemPackageEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Package.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: Package<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-system-package-delete ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSystemPackageEndpointResponse400 | DeleteSystemPackageEndpointResponse401 | DeleteSystemPackageEndpointResponse403 | DeleteSystemPackageEndpointResponse404 | DeleteSystemPackageEndpointResponse405 | DeleteSystemPackageEndpointResponse406 | DeleteSystemPackageEndpointResponse409 | DeleteSystemPackageEndpointResponse415 | DeleteSystemPackageEndpointResponse422 | DeleteSystemPackageEndpointResponse424 | DeleteSystemPackageEndpointResponse500 | DeleteSystemPackageEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
