from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_ha_proxy_file_endpoint_response_400 import DeleteServicesHAProxyFileEndpointResponse400
from ...models.delete_services_ha_proxy_file_endpoint_response_401 import DeleteServicesHAProxyFileEndpointResponse401
from ...models.delete_services_ha_proxy_file_endpoint_response_403 import DeleteServicesHAProxyFileEndpointResponse403
from ...models.delete_services_ha_proxy_file_endpoint_response_404 import DeleteServicesHAProxyFileEndpointResponse404
from ...models.delete_services_ha_proxy_file_endpoint_response_405 import DeleteServicesHAProxyFileEndpointResponse405
from ...models.delete_services_ha_proxy_file_endpoint_response_406 import DeleteServicesHAProxyFileEndpointResponse406
from ...models.delete_services_ha_proxy_file_endpoint_response_409 import DeleteServicesHAProxyFileEndpointResponse409
from ...models.delete_services_ha_proxy_file_endpoint_response_415 import DeleteServicesHAProxyFileEndpointResponse415
from ...models.delete_services_ha_proxy_file_endpoint_response_422 import DeleteServicesHAProxyFileEndpointResponse422
from ...models.delete_services_ha_proxy_file_endpoint_response_424 import DeleteServicesHAProxyFileEndpointResponse424
from ...models.delete_services_ha_proxy_file_endpoint_response_500 import DeleteServicesHAProxyFileEndpointResponse500
from ...models.delete_services_ha_proxy_file_endpoint_response_503 import DeleteServicesHAProxyFileEndpointResponse503
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
        "url": "/api/v2/services/haproxy/file",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesHAProxyFileEndpointResponse400
    | DeleteServicesHAProxyFileEndpointResponse401
    | DeleteServicesHAProxyFileEndpointResponse403
    | DeleteServicesHAProxyFileEndpointResponse404
    | DeleteServicesHAProxyFileEndpointResponse405
    | DeleteServicesHAProxyFileEndpointResponse406
    | DeleteServicesHAProxyFileEndpointResponse409
    | DeleteServicesHAProxyFileEndpointResponse415
    | DeleteServicesHAProxyFileEndpointResponse422
    | DeleteServicesHAProxyFileEndpointResponse424
    | DeleteServicesHAProxyFileEndpointResponse500
    | DeleteServicesHAProxyFileEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesHAProxyFileEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesHAProxyFileEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesHAProxyFileEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesHAProxyFileEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesHAProxyFileEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesHAProxyFileEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesHAProxyFileEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesHAProxyFileEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesHAProxyFileEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesHAProxyFileEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesHAProxyFileEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesHAProxyFileEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesHAProxyFileEndpointResponse400
    | DeleteServicesHAProxyFileEndpointResponse401
    | DeleteServicesHAProxyFileEndpointResponse403
    | DeleteServicesHAProxyFileEndpointResponse404
    | DeleteServicesHAProxyFileEndpointResponse405
    | DeleteServicesHAProxyFileEndpointResponse406
    | DeleteServicesHAProxyFileEndpointResponse409
    | DeleteServicesHAProxyFileEndpointResponse415
    | DeleteServicesHAProxyFileEndpointResponse422
    | DeleteServicesHAProxyFileEndpointResponse424
    | DeleteServicesHAProxyFileEndpointResponse500
    | DeleteServicesHAProxyFileEndpointResponse503
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
    DeleteServicesHAProxyFileEndpointResponse400
    | DeleteServicesHAProxyFileEndpointResponse401
    | DeleteServicesHAProxyFileEndpointResponse403
    | DeleteServicesHAProxyFileEndpointResponse404
    | DeleteServicesHAProxyFileEndpointResponse405
    | DeleteServicesHAProxyFileEndpointResponse406
    | DeleteServicesHAProxyFileEndpointResponse409
    | DeleteServicesHAProxyFileEndpointResponse415
    | DeleteServicesHAProxyFileEndpointResponse422
    | DeleteServicesHAProxyFileEndpointResponse424
    | DeleteServicesHAProxyFileEndpointResponse500
    | DeleteServicesHAProxyFileEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy File.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-file-delete ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyFileEndpointResponse400 | DeleteServicesHAProxyFileEndpointResponse401 | DeleteServicesHAProxyFileEndpointResponse403 | DeleteServicesHAProxyFileEndpointResponse404 | DeleteServicesHAProxyFileEndpointResponse405 | DeleteServicesHAProxyFileEndpointResponse406 | DeleteServicesHAProxyFileEndpointResponse409 | DeleteServicesHAProxyFileEndpointResponse415 | DeleteServicesHAProxyFileEndpointResponse422 | DeleteServicesHAProxyFileEndpointResponse424 | DeleteServicesHAProxyFileEndpointResponse500 | DeleteServicesHAProxyFileEndpointResponse503]
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
    DeleteServicesHAProxyFileEndpointResponse400
    | DeleteServicesHAProxyFileEndpointResponse401
    | DeleteServicesHAProxyFileEndpointResponse403
    | DeleteServicesHAProxyFileEndpointResponse404
    | DeleteServicesHAProxyFileEndpointResponse405
    | DeleteServicesHAProxyFileEndpointResponse406
    | DeleteServicesHAProxyFileEndpointResponse409
    | DeleteServicesHAProxyFileEndpointResponse415
    | DeleteServicesHAProxyFileEndpointResponse422
    | DeleteServicesHAProxyFileEndpointResponse424
    | DeleteServicesHAProxyFileEndpointResponse500
    | DeleteServicesHAProxyFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy File.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-file-delete ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyFileEndpointResponse400 | DeleteServicesHAProxyFileEndpointResponse401 | DeleteServicesHAProxyFileEndpointResponse403 | DeleteServicesHAProxyFileEndpointResponse404 | DeleteServicesHAProxyFileEndpointResponse405 | DeleteServicesHAProxyFileEndpointResponse406 | DeleteServicesHAProxyFileEndpointResponse409 | DeleteServicesHAProxyFileEndpointResponse415 | DeleteServicesHAProxyFileEndpointResponse422 | DeleteServicesHAProxyFileEndpointResponse424 | DeleteServicesHAProxyFileEndpointResponse500 | DeleteServicesHAProxyFileEndpointResponse503
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
    DeleteServicesHAProxyFileEndpointResponse400
    | DeleteServicesHAProxyFileEndpointResponse401
    | DeleteServicesHAProxyFileEndpointResponse403
    | DeleteServicesHAProxyFileEndpointResponse404
    | DeleteServicesHAProxyFileEndpointResponse405
    | DeleteServicesHAProxyFileEndpointResponse406
    | DeleteServicesHAProxyFileEndpointResponse409
    | DeleteServicesHAProxyFileEndpointResponse415
    | DeleteServicesHAProxyFileEndpointResponse422
    | DeleteServicesHAProxyFileEndpointResponse424
    | DeleteServicesHAProxyFileEndpointResponse500
    | DeleteServicesHAProxyFileEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy File.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-file-delete ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyFileEndpointResponse400 | DeleteServicesHAProxyFileEndpointResponse401 | DeleteServicesHAProxyFileEndpointResponse403 | DeleteServicesHAProxyFileEndpointResponse404 | DeleteServicesHAProxyFileEndpointResponse405 | DeleteServicesHAProxyFileEndpointResponse406 | DeleteServicesHAProxyFileEndpointResponse409 | DeleteServicesHAProxyFileEndpointResponse415 | DeleteServicesHAProxyFileEndpointResponse422 | DeleteServicesHAProxyFileEndpointResponse424 | DeleteServicesHAProxyFileEndpointResponse500 | DeleteServicesHAProxyFileEndpointResponse503]
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
    DeleteServicesHAProxyFileEndpointResponse400
    | DeleteServicesHAProxyFileEndpointResponse401
    | DeleteServicesHAProxyFileEndpointResponse403
    | DeleteServicesHAProxyFileEndpointResponse404
    | DeleteServicesHAProxyFileEndpointResponse405
    | DeleteServicesHAProxyFileEndpointResponse406
    | DeleteServicesHAProxyFileEndpointResponse409
    | DeleteServicesHAProxyFileEndpointResponse415
    | DeleteServicesHAProxyFileEndpointResponse422
    | DeleteServicesHAProxyFileEndpointResponse424
    | DeleteServicesHAProxyFileEndpointResponse500
    | DeleteServicesHAProxyFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy File.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-file-delete ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyFileEndpointResponse400 | DeleteServicesHAProxyFileEndpointResponse401 | DeleteServicesHAProxyFileEndpointResponse403 | DeleteServicesHAProxyFileEndpointResponse404 | DeleteServicesHAProxyFileEndpointResponse405 | DeleteServicesHAProxyFileEndpointResponse406 | DeleteServicesHAProxyFileEndpointResponse409 | DeleteServicesHAProxyFileEndpointResponse415 | DeleteServicesHAProxyFileEndpointResponse422 | DeleteServicesHAProxyFileEndpointResponse424 | DeleteServicesHAProxyFileEndpointResponse500 | DeleteServicesHAProxyFileEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
