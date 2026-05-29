from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_400 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse400,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_401 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse401,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_403 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse403,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_404 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse404,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_405 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse405,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_406 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse406,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_409 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse409,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_415 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse415,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_422 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse422,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_424 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse424,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_500 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse500,
)
from ...models.delete_services_ha_proxy_frontend_acl_endpoint_response_503 import (
    DeleteServicesHAProxyFrontendACLEndpointResponse503,
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
        "url": "/api/v2/services/haproxy/frontend/acl",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesHAProxyFrontendACLEndpointResponse400
    | DeleteServicesHAProxyFrontendACLEndpointResponse401
    | DeleteServicesHAProxyFrontendACLEndpointResponse403
    | DeleteServicesHAProxyFrontendACLEndpointResponse404
    | DeleteServicesHAProxyFrontendACLEndpointResponse405
    | DeleteServicesHAProxyFrontendACLEndpointResponse406
    | DeleteServicesHAProxyFrontendACLEndpointResponse409
    | DeleteServicesHAProxyFrontendACLEndpointResponse415
    | DeleteServicesHAProxyFrontendACLEndpointResponse422
    | DeleteServicesHAProxyFrontendACLEndpointResponse424
    | DeleteServicesHAProxyFrontendACLEndpointResponse500
    | DeleteServicesHAProxyFrontendACLEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesHAProxyFrontendACLEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesHAProxyFrontendACLEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesHAProxyFrontendACLEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesHAProxyFrontendACLEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesHAProxyFrontendACLEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesHAProxyFrontendACLEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesHAProxyFrontendACLEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesHAProxyFrontendACLEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesHAProxyFrontendACLEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesHAProxyFrontendACLEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesHAProxyFrontendACLEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesHAProxyFrontendACLEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesHAProxyFrontendACLEndpointResponse400
    | DeleteServicesHAProxyFrontendACLEndpointResponse401
    | DeleteServicesHAProxyFrontendACLEndpointResponse403
    | DeleteServicesHAProxyFrontendACLEndpointResponse404
    | DeleteServicesHAProxyFrontendACLEndpointResponse405
    | DeleteServicesHAProxyFrontendACLEndpointResponse406
    | DeleteServicesHAProxyFrontendACLEndpointResponse409
    | DeleteServicesHAProxyFrontendACLEndpointResponse415
    | DeleteServicesHAProxyFrontendACLEndpointResponse422
    | DeleteServicesHAProxyFrontendACLEndpointResponse424
    | DeleteServicesHAProxyFrontendACLEndpointResponse500
    | DeleteServicesHAProxyFrontendACLEndpointResponse503
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
    DeleteServicesHAProxyFrontendACLEndpointResponse400
    | DeleteServicesHAProxyFrontendACLEndpointResponse401
    | DeleteServicesHAProxyFrontendACLEndpointResponse403
    | DeleteServicesHAProxyFrontendACLEndpointResponse404
    | DeleteServicesHAProxyFrontendACLEndpointResponse405
    | DeleteServicesHAProxyFrontendACLEndpointResponse406
    | DeleteServicesHAProxyFrontendACLEndpointResponse409
    | DeleteServicesHAProxyFrontendACLEndpointResponse415
    | DeleteServicesHAProxyFrontendACLEndpointResponse422
    | DeleteServicesHAProxyFrontendACLEndpointResponse424
    | DeleteServicesHAProxyFrontendACLEndpointResponse500
    | DeleteServicesHAProxyFrontendACLEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acl-delete ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyFrontendACLEndpointResponse400 | DeleteServicesHAProxyFrontendACLEndpointResponse401 | DeleteServicesHAProxyFrontendACLEndpointResponse403 | DeleteServicesHAProxyFrontendACLEndpointResponse404 | DeleteServicesHAProxyFrontendACLEndpointResponse405 | DeleteServicesHAProxyFrontendACLEndpointResponse406 | DeleteServicesHAProxyFrontendACLEndpointResponse409 | DeleteServicesHAProxyFrontendACLEndpointResponse415 | DeleteServicesHAProxyFrontendACLEndpointResponse422 | DeleteServicesHAProxyFrontendACLEndpointResponse424 | DeleteServicesHAProxyFrontendACLEndpointResponse500 | DeleteServicesHAProxyFrontendACLEndpointResponse503]
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
    DeleteServicesHAProxyFrontendACLEndpointResponse400
    | DeleteServicesHAProxyFrontendACLEndpointResponse401
    | DeleteServicesHAProxyFrontendACLEndpointResponse403
    | DeleteServicesHAProxyFrontendACLEndpointResponse404
    | DeleteServicesHAProxyFrontendACLEndpointResponse405
    | DeleteServicesHAProxyFrontendACLEndpointResponse406
    | DeleteServicesHAProxyFrontendACLEndpointResponse409
    | DeleteServicesHAProxyFrontendACLEndpointResponse415
    | DeleteServicesHAProxyFrontendACLEndpointResponse422
    | DeleteServicesHAProxyFrontendACLEndpointResponse424
    | DeleteServicesHAProxyFrontendACLEndpointResponse500
    | DeleteServicesHAProxyFrontendACLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acl-delete ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyFrontendACLEndpointResponse400 | DeleteServicesHAProxyFrontendACLEndpointResponse401 | DeleteServicesHAProxyFrontendACLEndpointResponse403 | DeleteServicesHAProxyFrontendACLEndpointResponse404 | DeleteServicesHAProxyFrontendACLEndpointResponse405 | DeleteServicesHAProxyFrontendACLEndpointResponse406 | DeleteServicesHAProxyFrontendACLEndpointResponse409 | DeleteServicesHAProxyFrontendACLEndpointResponse415 | DeleteServicesHAProxyFrontendACLEndpointResponse422 | DeleteServicesHAProxyFrontendACLEndpointResponse424 | DeleteServicesHAProxyFrontendACLEndpointResponse500 | DeleteServicesHAProxyFrontendACLEndpointResponse503
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
    DeleteServicesHAProxyFrontendACLEndpointResponse400
    | DeleteServicesHAProxyFrontendACLEndpointResponse401
    | DeleteServicesHAProxyFrontendACLEndpointResponse403
    | DeleteServicesHAProxyFrontendACLEndpointResponse404
    | DeleteServicesHAProxyFrontendACLEndpointResponse405
    | DeleteServicesHAProxyFrontendACLEndpointResponse406
    | DeleteServicesHAProxyFrontendACLEndpointResponse409
    | DeleteServicesHAProxyFrontendACLEndpointResponse415
    | DeleteServicesHAProxyFrontendACLEndpointResponse422
    | DeleteServicesHAProxyFrontendACLEndpointResponse424
    | DeleteServicesHAProxyFrontendACLEndpointResponse500
    | DeleteServicesHAProxyFrontendACLEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acl-delete ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyFrontendACLEndpointResponse400 | DeleteServicesHAProxyFrontendACLEndpointResponse401 | DeleteServicesHAProxyFrontendACLEndpointResponse403 | DeleteServicesHAProxyFrontendACLEndpointResponse404 | DeleteServicesHAProxyFrontendACLEndpointResponse405 | DeleteServicesHAProxyFrontendACLEndpointResponse406 | DeleteServicesHAProxyFrontendACLEndpointResponse409 | DeleteServicesHAProxyFrontendACLEndpointResponse415 | DeleteServicesHAProxyFrontendACLEndpointResponse422 | DeleteServicesHAProxyFrontendACLEndpointResponse424 | DeleteServicesHAProxyFrontendACLEndpointResponse500 | DeleteServicesHAProxyFrontendACLEndpointResponse503]
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
    DeleteServicesHAProxyFrontendACLEndpointResponse400
    | DeleteServicesHAProxyFrontendACLEndpointResponse401
    | DeleteServicesHAProxyFrontendACLEndpointResponse403
    | DeleteServicesHAProxyFrontendACLEndpointResponse404
    | DeleteServicesHAProxyFrontendACLEndpointResponse405
    | DeleteServicesHAProxyFrontendACLEndpointResponse406
    | DeleteServicesHAProxyFrontendACLEndpointResponse409
    | DeleteServicesHAProxyFrontendACLEndpointResponse415
    | DeleteServicesHAProxyFrontendACLEndpointResponse422
    | DeleteServicesHAProxyFrontendACLEndpointResponse424
    | DeleteServicesHAProxyFrontendACLEndpointResponse500
    | DeleteServicesHAProxyFrontendACLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acl-delete ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyFrontendACLEndpointResponse400 | DeleteServicesHAProxyFrontendACLEndpointResponse401 | DeleteServicesHAProxyFrontendACLEndpointResponse403 | DeleteServicesHAProxyFrontendACLEndpointResponse404 | DeleteServicesHAProxyFrontendACLEndpointResponse405 | DeleteServicesHAProxyFrontendACLEndpointResponse406 | DeleteServicesHAProxyFrontendACLEndpointResponse409 | DeleteServicesHAProxyFrontendACLEndpointResponse415 | DeleteServicesHAProxyFrontendACLEndpointResponse422 | DeleteServicesHAProxyFrontendACLEndpointResponse424 | DeleteServicesHAProxyFrontendACLEndpointResponse500 | DeleteServicesHAProxyFrontendACLEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
