from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_ha_proxy_frontend_endpoint_response_400 import (
    DeleteServicesHAProxyFrontendEndpointResponse400,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_401 import (
    DeleteServicesHAProxyFrontendEndpointResponse401,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_403 import (
    DeleteServicesHAProxyFrontendEndpointResponse403,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_404 import (
    DeleteServicesHAProxyFrontendEndpointResponse404,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_405 import (
    DeleteServicesHAProxyFrontendEndpointResponse405,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_406 import (
    DeleteServicesHAProxyFrontendEndpointResponse406,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_409 import (
    DeleteServicesHAProxyFrontendEndpointResponse409,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_415 import (
    DeleteServicesHAProxyFrontendEndpointResponse415,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_422 import (
    DeleteServicesHAProxyFrontendEndpointResponse422,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_424 import (
    DeleteServicesHAProxyFrontendEndpointResponse424,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_500 import (
    DeleteServicesHAProxyFrontendEndpointResponse500,
)
from ...models.delete_services_ha_proxy_frontend_endpoint_response_503 import (
    DeleteServicesHAProxyFrontendEndpointResponse503,
)
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
        "url": "/api/v2/services/haproxy/frontend",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesHAProxyFrontendEndpointResponse400
    | DeleteServicesHAProxyFrontendEndpointResponse401
    | DeleteServicesHAProxyFrontendEndpointResponse403
    | DeleteServicesHAProxyFrontendEndpointResponse404
    | DeleteServicesHAProxyFrontendEndpointResponse405
    | DeleteServicesHAProxyFrontendEndpointResponse406
    | DeleteServicesHAProxyFrontendEndpointResponse409
    | DeleteServicesHAProxyFrontendEndpointResponse415
    | DeleteServicesHAProxyFrontendEndpointResponse422
    | DeleteServicesHAProxyFrontendEndpointResponse424
    | DeleteServicesHAProxyFrontendEndpointResponse500
    | DeleteServicesHAProxyFrontendEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesHAProxyFrontendEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesHAProxyFrontendEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesHAProxyFrontendEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesHAProxyFrontendEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesHAProxyFrontendEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesHAProxyFrontendEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesHAProxyFrontendEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesHAProxyFrontendEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesHAProxyFrontendEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesHAProxyFrontendEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesHAProxyFrontendEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesHAProxyFrontendEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesHAProxyFrontendEndpointResponse400
    | DeleteServicesHAProxyFrontendEndpointResponse401
    | DeleteServicesHAProxyFrontendEndpointResponse403
    | DeleteServicesHAProxyFrontendEndpointResponse404
    | DeleteServicesHAProxyFrontendEndpointResponse405
    | DeleteServicesHAProxyFrontendEndpointResponse406
    | DeleteServicesHAProxyFrontendEndpointResponse409
    | DeleteServicesHAProxyFrontendEndpointResponse415
    | DeleteServicesHAProxyFrontendEndpointResponse422
    | DeleteServicesHAProxyFrontendEndpointResponse424
    | DeleteServicesHAProxyFrontendEndpointResponse500
    | DeleteServicesHAProxyFrontendEndpointResponse503
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
    DeleteServicesHAProxyFrontendEndpointResponse400
    | DeleteServicesHAProxyFrontendEndpointResponse401
    | DeleteServicesHAProxyFrontendEndpointResponse403
    | DeleteServicesHAProxyFrontendEndpointResponse404
    | DeleteServicesHAProxyFrontendEndpointResponse405
    | DeleteServicesHAProxyFrontendEndpointResponse406
    | DeleteServicesHAProxyFrontendEndpointResponse409
    | DeleteServicesHAProxyFrontendEndpointResponse415
    | DeleteServicesHAProxyFrontendEndpointResponse422
    | DeleteServicesHAProxyFrontendEndpointResponse424
    | DeleteServicesHAProxyFrontendEndpointResponse500
    | DeleteServicesHAProxyFrontendEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-delete ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyFrontendEndpointResponse400 | DeleteServicesHAProxyFrontendEndpointResponse401 | DeleteServicesHAProxyFrontendEndpointResponse403 | DeleteServicesHAProxyFrontendEndpointResponse404 | DeleteServicesHAProxyFrontendEndpointResponse405 | DeleteServicesHAProxyFrontendEndpointResponse406 | DeleteServicesHAProxyFrontendEndpointResponse409 | DeleteServicesHAProxyFrontendEndpointResponse415 | DeleteServicesHAProxyFrontendEndpointResponse422 | DeleteServicesHAProxyFrontendEndpointResponse424 | DeleteServicesHAProxyFrontendEndpointResponse500 | DeleteServicesHAProxyFrontendEndpointResponse503]
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
    DeleteServicesHAProxyFrontendEndpointResponse400
    | DeleteServicesHAProxyFrontendEndpointResponse401
    | DeleteServicesHAProxyFrontendEndpointResponse403
    | DeleteServicesHAProxyFrontendEndpointResponse404
    | DeleteServicesHAProxyFrontendEndpointResponse405
    | DeleteServicesHAProxyFrontendEndpointResponse406
    | DeleteServicesHAProxyFrontendEndpointResponse409
    | DeleteServicesHAProxyFrontendEndpointResponse415
    | DeleteServicesHAProxyFrontendEndpointResponse422
    | DeleteServicesHAProxyFrontendEndpointResponse424
    | DeleteServicesHAProxyFrontendEndpointResponse500
    | DeleteServicesHAProxyFrontendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-delete ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyFrontendEndpointResponse400 | DeleteServicesHAProxyFrontendEndpointResponse401 | DeleteServicesHAProxyFrontendEndpointResponse403 | DeleteServicesHAProxyFrontendEndpointResponse404 | DeleteServicesHAProxyFrontendEndpointResponse405 | DeleteServicesHAProxyFrontendEndpointResponse406 | DeleteServicesHAProxyFrontendEndpointResponse409 | DeleteServicesHAProxyFrontendEndpointResponse415 | DeleteServicesHAProxyFrontendEndpointResponse422 | DeleteServicesHAProxyFrontendEndpointResponse424 | DeleteServicesHAProxyFrontendEndpointResponse500 | DeleteServicesHAProxyFrontendEndpointResponse503
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
    DeleteServicesHAProxyFrontendEndpointResponse400
    | DeleteServicesHAProxyFrontendEndpointResponse401
    | DeleteServicesHAProxyFrontendEndpointResponse403
    | DeleteServicesHAProxyFrontendEndpointResponse404
    | DeleteServicesHAProxyFrontendEndpointResponse405
    | DeleteServicesHAProxyFrontendEndpointResponse406
    | DeleteServicesHAProxyFrontendEndpointResponse409
    | DeleteServicesHAProxyFrontendEndpointResponse415
    | DeleteServicesHAProxyFrontendEndpointResponse422
    | DeleteServicesHAProxyFrontendEndpointResponse424
    | DeleteServicesHAProxyFrontendEndpointResponse500
    | DeleteServicesHAProxyFrontendEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-delete ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesHAProxyFrontendEndpointResponse400 | DeleteServicesHAProxyFrontendEndpointResponse401 | DeleteServicesHAProxyFrontendEndpointResponse403 | DeleteServicesHAProxyFrontendEndpointResponse404 | DeleteServicesHAProxyFrontendEndpointResponse405 | DeleteServicesHAProxyFrontendEndpointResponse406 | DeleteServicesHAProxyFrontendEndpointResponse409 | DeleteServicesHAProxyFrontendEndpointResponse415 | DeleteServicesHAProxyFrontendEndpointResponse422 | DeleteServicesHAProxyFrontendEndpointResponse424 | DeleteServicesHAProxyFrontendEndpointResponse500 | DeleteServicesHAProxyFrontendEndpointResponse503]
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
    DeleteServicesHAProxyFrontendEndpointResponse400
    | DeleteServicesHAProxyFrontendEndpointResponse401
    | DeleteServicesHAProxyFrontendEndpointResponse403
    | DeleteServicesHAProxyFrontendEndpointResponse404
    | DeleteServicesHAProxyFrontendEndpointResponse405
    | DeleteServicesHAProxyFrontendEndpointResponse406
    | DeleteServicesHAProxyFrontendEndpointResponse409
    | DeleteServicesHAProxyFrontendEndpointResponse415
    | DeleteServicesHAProxyFrontendEndpointResponse422
    | DeleteServicesHAProxyFrontendEndpointResponse424
    | DeleteServicesHAProxyFrontendEndpointResponse500
    | DeleteServicesHAProxyFrontendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-delete ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesHAProxyFrontendEndpointResponse400 | DeleteServicesHAProxyFrontendEndpointResponse401 | DeleteServicesHAProxyFrontendEndpointResponse403 | DeleteServicesHAProxyFrontendEndpointResponse404 | DeleteServicesHAProxyFrontendEndpointResponse405 | DeleteServicesHAProxyFrontendEndpointResponse406 | DeleteServicesHAProxyFrontendEndpointResponse409 | DeleteServicesHAProxyFrontendEndpointResponse415 | DeleteServicesHAProxyFrontendEndpointResponse422 | DeleteServicesHAProxyFrontendEndpointResponse424 | DeleteServicesHAProxyFrontendEndpointResponse500 | DeleteServicesHAProxyFrontendEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
