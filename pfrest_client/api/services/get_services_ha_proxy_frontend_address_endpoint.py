from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_400 import (
    GetServicesHAProxyFrontendAddressEndpointResponse400,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_401 import (
    GetServicesHAProxyFrontendAddressEndpointResponse401,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_403 import (
    GetServicesHAProxyFrontendAddressEndpointResponse403,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_404 import (
    GetServicesHAProxyFrontendAddressEndpointResponse404,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_405 import (
    GetServicesHAProxyFrontendAddressEndpointResponse405,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_406 import (
    GetServicesHAProxyFrontendAddressEndpointResponse406,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_409 import (
    GetServicesHAProxyFrontendAddressEndpointResponse409,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_415 import (
    GetServicesHAProxyFrontendAddressEndpointResponse415,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_422 import (
    GetServicesHAProxyFrontendAddressEndpointResponse422,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_424 import (
    GetServicesHAProxyFrontendAddressEndpointResponse424,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_500 import (
    GetServicesHAProxyFrontendAddressEndpointResponse500,
)
from ...models.get_services_ha_proxy_frontend_address_endpoint_response_503 import (
    GetServicesHAProxyFrontendAddressEndpointResponse503,
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
        "url": "/api/v2/services/haproxy/frontend/address",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesHAProxyFrontendAddressEndpointResponse400
    | GetServicesHAProxyFrontendAddressEndpointResponse401
    | GetServicesHAProxyFrontendAddressEndpointResponse403
    | GetServicesHAProxyFrontendAddressEndpointResponse404
    | GetServicesHAProxyFrontendAddressEndpointResponse405
    | GetServicesHAProxyFrontendAddressEndpointResponse406
    | GetServicesHAProxyFrontendAddressEndpointResponse409
    | GetServicesHAProxyFrontendAddressEndpointResponse415
    | GetServicesHAProxyFrontendAddressEndpointResponse422
    | GetServicesHAProxyFrontendAddressEndpointResponse424
    | GetServicesHAProxyFrontendAddressEndpointResponse500
    | GetServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesHAProxyFrontendAddressEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesHAProxyFrontendAddressEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesHAProxyFrontendAddressEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesHAProxyFrontendAddressEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesHAProxyFrontendAddressEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesHAProxyFrontendAddressEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesHAProxyFrontendAddressEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesHAProxyFrontendAddressEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesHAProxyFrontendAddressEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesHAProxyFrontendAddressEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesHAProxyFrontendAddressEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesHAProxyFrontendAddressEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesHAProxyFrontendAddressEndpointResponse400
    | GetServicesHAProxyFrontendAddressEndpointResponse401
    | GetServicesHAProxyFrontendAddressEndpointResponse403
    | GetServicesHAProxyFrontendAddressEndpointResponse404
    | GetServicesHAProxyFrontendAddressEndpointResponse405
    | GetServicesHAProxyFrontendAddressEndpointResponse406
    | GetServicesHAProxyFrontendAddressEndpointResponse409
    | GetServicesHAProxyFrontendAddressEndpointResponse415
    | GetServicesHAProxyFrontendAddressEndpointResponse422
    | GetServicesHAProxyFrontendAddressEndpointResponse424
    | GetServicesHAProxyFrontendAddressEndpointResponse500
    | GetServicesHAProxyFrontendAddressEndpointResponse503
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
    GetServicesHAProxyFrontendAddressEndpointResponse400
    | GetServicesHAProxyFrontendAddressEndpointResponse401
    | GetServicesHAProxyFrontendAddressEndpointResponse403
    | GetServicesHAProxyFrontendAddressEndpointResponse404
    | GetServicesHAProxyFrontendAddressEndpointResponse405
    | GetServicesHAProxyFrontendAddressEndpointResponse406
    | GetServicesHAProxyFrontendAddressEndpointResponse409
    | GetServicesHAProxyFrontendAddressEndpointResponse415
    | GetServicesHAProxyFrontendAddressEndpointResponse422
    | GetServicesHAProxyFrontendAddressEndpointResponse424
    | GetServicesHAProxyFrontendAddressEndpointResponse500
    | GetServicesHAProxyFrontendAddressEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyFrontendAddressEndpointResponse400 | GetServicesHAProxyFrontendAddressEndpointResponse401 | GetServicesHAProxyFrontendAddressEndpointResponse403 | GetServicesHAProxyFrontendAddressEndpointResponse404 | GetServicesHAProxyFrontendAddressEndpointResponse405 | GetServicesHAProxyFrontendAddressEndpointResponse406 | GetServicesHAProxyFrontendAddressEndpointResponse409 | GetServicesHAProxyFrontendAddressEndpointResponse415 | GetServicesHAProxyFrontendAddressEndpointResponse422 | GetServicesHAProxyFrontendAddressEndpointResponse424 | GetServicesHAProxyFrontendAddressEndpointResponse500 | GetServicesHAProxyFrontendAddressEndpointResponse503]
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
    GetServicesHAProxyFrontendAddressEndpointResponse400
    | GetServicesHAProxyFrontendAddressEndpointResponse401
    | GetServicesHAProxyFrontendAddressEndpointResponse403
    | GetServicesHAProxyFrontendAddressEndpointResponse404
    | GetServicesHAProxyFrontendAddressEndpointResponse405
    | GetServicesHAProxyFrontendAddressEndpointResponse406
    | GetServicesHAProxyFrontendAddressEndpointResponse409
    | GetServicesHAProxyFrontendAddressEndpointResponse415
    | GetServicesHAProxyFrontendAddressEndpointResponse422
    | GetServicesHAProxyFrontendAddressEndpointResponse424
    | GetServicesHAProxyFrontendAddressEndpointResponse500
    | GetServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyFrontendAddressEndpointResponse400 | GetServicesHAProxyFrontendAddressEndpointResponse401 | GetServicesHAProxyFrontendAddressEndpointResponse403 | GetServicesHAProxyFrontendAddressEndpointResponse404 | GetServicesHAProxyFrontendAddressEndpointResponse405 | GetServicesHAProxyFrontendAddressEndpointResponse406 | GetServicesHAProxyFrontendAddressEndpointResponse409 | GetServicesHAProxyFrontendAddressEndpointResponse415 | GetServicesHAProxyFrontendAddressEndpointResponse422 | GetServicesHAProxyFrontendAddressEndpointResponse424 | GetServicesHAProxyFrontendAddressEndpointResponse500 | GetServicesHAProxyFrontendAddressEndpointResponse503
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
    GetServicesHAProxyFrontendAddressEndpointResponse400
    | GetServicesHAProxyFrontendAddressEndpointResponse401
    | GetServicesHAProxyFrontendAddressEndpointResponse403
    | GetServicesHAProxyFrontendAddressEndpointResponse404
    | GetServicesHAProxyFrontendAddressEndpointResponse405
    | GetServicesHAProxyFrontendAddressEndpointResponse406
    | GetServicesHAProxyFrontendAddressEndpointResponse409
    | GetServicesHAProxyFrontendAddressEndpointResponse415
    | GetServicesHAProxyFrontendAddressEndpointResponse422
    | GetServicesHAProxyFrontendAddressEndpointResponse424
    | GetServicesHAProxyFrontendAddressEndpointResponse500
    | GetServicesHAProxyFrontendAddressEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyFrontendAddressEndpointResponse400 | GetServicesHAProxyFrontendAddressEndpointResponse401 | GetServicesHAProxyFrontendAddressEndpointResponse403 | GetServicesHAProxyFrontendAddressEndpointResponse404 | GetServicesHAProxyFrontendAddressEndpointResponse405 | GetServicesHAProxyFrontendAddressEndpointResponse406 | GetServicesHAProxyFrontendAddressEndpointResponse409 | GetServicesHAProxyFrontendAddressEndpointResponse415 | GetServicesHAProxyFrontendAddressEndpointResponse422 | GetServicesHAProxyFrontendAddressEndpointResponse424 | GetServicesHAProxyFrontendAddressEndpointResponse500 | GetServicesHAProxyFrontendAddressEndpointResponse503]
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
    GetServicesHAProxyFrontendAddressEndpointResponse400
    | GetServicesHAProxyFrontendAddressEndpointResponse401
    | GetServicesHAProxyFrontendAddressEndpointResponse403
    | GetServicesHAProxyFrontendAddressEndpointResponse404
    | GetServicesHAProxyFrontendAddressEndpointResponse405
    | GetServicesHAProxyFrontendAddressEndpointResponse406
    | GetServicesHAProxyFrontendAddressEndpointResponse409
    | GetServicesHAProxyFrontendAddressEndpointResponse415
    | GetServicesHAProxyFrontendAddressEndpointResponse422
    | GetServicesHAProxyFrontendAddressEndpointResponse424
    | GetServicesHAProxyFrontendAddressEndpointResponse500
    | GetServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-get ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyFrontendAddressEndpointResponse400 | GetServicesHAProxyFrontendAddressEndpointResponse401 | GetServicesHAProxyFrontendAddressEndpointResponse403 | GetServicesHAProxyFrontendAddressEndpointResponse404 | GetServicesHAProxyFrontendAddressEndpointResponse405 | GetServicesHAProxyFrontendAddressEndpointResponse406 | GetServicesHAProxyFrontendAddressEndpointResponse409 | GetServicesHAProxyFrontendAddressEndpointResponse415 | GetServicesHAProxyFrontendAddressEndpointResponse422 | GetServicesHAProxyFrontendAddressEndpointResponse424 | GetServicesHAProxyFrontendAddressEndpointResponse500 | GetServicesHAProxyFrontendAddressEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
