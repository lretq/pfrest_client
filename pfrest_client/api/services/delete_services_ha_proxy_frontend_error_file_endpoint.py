from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_400 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse400,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_401 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse401,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_403 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse403,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_404 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse404,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_405 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse405,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_406 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse406,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_409 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse409,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_415 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse415,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_422 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse422,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_424 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse424,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_500 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse500,
)
from ...models.delete_services_ha_proxy_frontend_error_file_endpoint_response_503 import (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/haproxy/frontend/error_file",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse400
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesHAProxyFrontendErrorFileEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse400
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse400
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyFrontendErrorFileEndpointResponse400 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse400
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyFrontendErrorFileEndpointResponse400 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse400
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyFrontendErrorFileEndpointResponse400 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteServicesHAProxyFrontendErrorFileEndpointResponse400
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500
    | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-delete ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyFrontendErrorFileEndpointResponse400 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse401 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse403 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse404 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse405 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse406 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse409 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse415 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse422 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse424 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse500 | DeleteServicesHAProxyFrontendErrorFileEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
