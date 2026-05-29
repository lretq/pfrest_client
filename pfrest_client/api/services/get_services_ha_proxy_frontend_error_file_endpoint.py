from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_400 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse400,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_401 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse401,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_403 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse403,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_404 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse404,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_405 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse405,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_406 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse406,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_409 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse409,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_415 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse415,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_422 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse422,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_424 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse424,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_500 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse500,
)
from ...models.get_services_ha_proxy_frontend_error_file_endpoint_response_503 import (
    GetServicesHAProxyFrontendErrorFileEndpointResponse503,
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
        "method": "get",
        "url": "/api/v2/services/haproxy/frontend/error_file",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesHAProxyFrontendErrorFileEndpointResponse400
    | GetServicesHAProxyFrontendErrorFileEndpointResponse401
    | GetServicesHAProxyFrontendErrorFileEndpointResponse403
    | GetServicesHAProxyFrontendErrorFileEndpointResponse404
    | GetServicesHAProxyFrontendErrorFileEndpointResponse405
    | GetServicesHAProxyFrontendErrorFileEndpointResponse406
    | GetServicesHAProxyFrontendErrorFileEndpointResponse409
    | GetServicesHAProxyFrontendErrorFileEndpointResponse415
    | GetServicesHAProxyFrontendErrorFileEndpointResponse422
    | GetServicesHAProxyFrontendErrorFileEndpointResponse424
    | GetServicesHAProxyFrontendErrorFileEndpointResponse500
    | GetServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesHAProxyFrontendErrorFileEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesHAProxyFrontendErrorFileEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesHAProxyFrontendErrorFileEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesHAProxyFrontendErrorFileEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesHAProxyFrontendErrorFileEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesHAProxyFrontendErrorFileEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesHAProxyFrontendErrorFileEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesHAProxyFrontendErrorFileEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesHAProxyFrontendErrorFileEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesHAProxyFrontendErrorFileEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesHAProxyFrontendErrorFileEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesHAProxyFrontendErrorFileEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesHAProxyFrontendErrorFileEndpointResponse400
    | GetServicesHAProxyFrontendErrorFileEndpointResponse401
    | GetServicesHAProxyFrontendErrorFileEndpointResponse403
    | GetServicesHAProxyFrontendErrorFileEndpointResponse404
    | GetServicesHAProxyFrontendErrorFileEndpointResponse405
    | GetServicesHAProxyFrontendErrorFileEndpointResponse406
    | GetServicesHAProxyFrontendErrorFileEndpointResponse409
    | GetServicesHAProxyFrontendErrorFileEndpointResponse415
    | GetServicesHAProxyFrontendErrorFileEndpointResponse422
    | GetServicesHAProxyFrontendErrorFileEndpointResponse424
    | GetServicesHAProxyFrontendErrorFileEndpointResponse500
    | GetServicesHAProxyFrontendErrorFileEndpointResponse503
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
    GetServicesHAProxyFrontendErrorFileEndpointResponse400
    | GetServicesHAProxyFrontendErrorFileEndpointResponse401
    | GetServicesHAProxyFrontendErrorFileEndpointResponse403
    | GetServicesHAProxyFrontendErrorFileEndpointResponse404
    | GetServicesHAProxyFrontendErrorFileEndpointResponse405
    | GetServicesHAProxyFrontendErrorFileEndpointResponse406
    | GetServicesHAProxyFrontendErrorFileEndpointResponse409
    | GetServicesHAProxyFrontendErrorFileEndpointResponse415
    | GetServicesHAProxyFrontendErrorFileEndpointResponse422
    | GetServicesHAProxyFrontendErrorFileEndpointResponse424
    | GetServicesHAProxyFrontendErrorFileEndpointResponse500
    | GetServicesHAProxyFrontendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyFrontendErrorFileEndpointResponse400 | GetServicesHAProxyFrontendErrorFileEndpointResponse401 | GetServicesHAProxyFrontendErrorFileEndpointResponse403 | GetServicesHAProxyFrontendErrorFileEndpointResponse404 | GetServicesHAProxyFrontendErrorFileEndpointResponse405 | GetServicesHAProxyFrontendErrorFileEndpointResponse406 | GetServicesHAProxyFrontendErrorFileEndpointResponse409 | GetServicesHAProxyFrontendErrorFileEndpointResponse415 | GetServicesHAProxyFrontendErrorFileEndpointResponse422 | GetServicesHAProxyFrontendErrorFileEndpointResponse424 | GetServicesHAProxyFrontendErrorFileEndpointResponse500 | GetServicesHAProxyFrontendErrorFileEndpointResponse503]
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
    GetServicesHAProxyFrontendErrorFileEndpointResponse400
    | GetServicesHAProxyFrontendErrorFileEndpointResponse401
    | GetServicesHAProxyFrontendErrorFileEndpointResponse403
    | GetServicesHAProxyFrontendErrorFileEndpointResponse404
    | GetServicesHAProxyFrontendErrorFileEndpointResponse405
    | GetServicesHAProxyFrontendErrorFileEndpointResponse406
    | GetServicesHAProxyFrontendErrorFileEndpointResponse409
    | GetServicesHAProxyFrontendErrorFileEndpointResponse415
    | GetServicesHAProxyFrontendErrorFileEndpointResponse422
    | GetServicesHAProxyFrontendErrorFileEndpointResponse424
    | GetServicesHAProxyFrontendErrorFileEndpointResponse500
    | GetServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyFrontendErrorFileEndpointResponse400 | GetServicesHAProxyFrontendErrorFileEndpointResponse401 | GetServicesHAProxyFrontendErrorFileEndpointResponse403 | GetServicesHAProxyFrontendErrorFileEndpointResponse404 | GetServicesHAProxyFrontendErrorFileEndpointResponse405 | GetServicesHAProxyFrontendErrorFileEndpointResponse406 | GetServicesHAProxyFrontendErrorFileEndpointResponse409 | GetServicesHAProxyFrontendErrorFileEndpointResponse415 | GetServicesHAProxyFrontendErrorFileEndpointResponse422 | GetServicesHAProxyFrontendErrorFileEndpointResponse424 | GetServicesHAProxyFrontendErrorFileEndpointResponse500 | GetServicesHAProxyFrontendErrorFileEndpointResponse503
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
    GetServicesHAProxyFrontendErrorFileEndpointResponse400
    | GetServicesHAProxyFrontendErrorFileEndpointResponse401
    | GetServicesHAProxyFrontendErrorFileEndpointResponse403
    | GetServicesHAProxyFrontendErrorFileEndpointResponse404
    | GetServicesHAProxyFrontendErrorFileEndpointResponse405
    | GetServicesHAProxyFrontendErrorFileEndpointResponse406
    | GetServicesHAProxyFrontendErrorFileEndpointResponse409
    | GetServicesHAProxyFrontendErrorFileEndpointResponse415
    | GetServicesHAProxyFrontendErrorFileEndpointResponse422
    | GetServicesHAProxyFrontendErrorFileEndpointResponse424
    | GetServicesHAProxyFrontendErrorFileEndpointResponse500
    | GetServicesHAProxyFrontendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyFrontendErrorFileEndpointResponse400 | GetServicesHAProxyFrontendErrorFileEndpointResponse401 | GetServicesHAProxyFrontendErrorFileEndpointResponse403 | GetServicesHAProxyFrontendErrorFileEndpointResponse404 | GetServicesHAProxyFrontendErrorFileEndpointResponse405 | GetServicesHAProxyFrontendErrorFileEndpointResponse406 | GetServicesHAProxyFrontendErrorFileEndpointResponse409 | GetServicesHAProxyFrontendErrorFileEndpointResponse415 | GetServicesHAProxyFrontendErrorFileEndpointResponse422 | GetServicesHAProxyFrontendErrorFileEndpointResponse424 | GetServicesHAProxyFrontendErrorFileEndpointResponse500 | GetServicesHAProxyFrontendErrorFileEndpointResponse503]
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
    GetServicesHAProxyFrontendErrorFileEndpointResponse400
    | GetServicesHAProxyFrontendErrorFileEndpointResponse401
    | GetServicesHAProxyFrontendErrorFileEndpointResponse403
    | GetServicesHAProxyFrontendErrorFileEndpointResponse404
    | GetServicesHAProxyFrontendErrorFileEndpointResponse405
    | GetServicesHAProxyFrontendErrorFileEndpointResponse406
    | GetServicesHAProxyFrontendErrorFileEndpointResponse409
    | GetServicesHAProxyFrontendErrorFileEndpointResponse415
    | GetServicesHAProxyFrontendErrorFileEndpointResponse422
    | GetServicesHAProxyFrontendErrorFileEndpointResponse424
    | GetServicesHAProxyFrontendErrorFileEndpointResponse500
    | GetServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyFrontendErrorFileEndpointResponse400 | GetServicesHAProxyFrontendErrorFileEndpointResponse401 | GetServicesHAProxyFrontendErrorFileEndpointResponse403 | GetServicesHAProxyFrontendErrorFileEndpointResponse404 | GetServicesHAProxyFrontendErrorFileEndpointResponse405 | GetServicesHAProxyFrontendErrorFileEndpointResponse406 | GetServicesHAProxyFrontendErrorFileEndpointResponse409 | GetServicesHAProxyFrontendErrorFileEndpointResponse415 | GetServicesHAProxyFrontendErrorFileEndpointResponse422 | GetServicesHAProxyFrontendErrorFileEndpointResponse424 | GetServicesHAProxyFrontendErrorFileEndpointResponse500 | GetServicesHAProxyFrontendErrorFileEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
