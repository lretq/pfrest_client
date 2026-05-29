from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_backend_server_endpoint_data_body import (
    PatchServicesHAProxyBackendServerEndpointDataBody,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_json_body import (
    PatchServicesHAProxyBackendServerEndpointJsonBody,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_400 import (
    PatchServicesHAProxyBackendServerEndpointResponse400,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_401 import (
    PatchServicesHAProxyBackendServerEndpointResponse401,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_403 import (
    PatchServicesHAProxyBackendServerEndpointResponse403,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_404 import (
    PatchServicesHAProxyBackendServerEndpointResponse404,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_405 import (
    PatchServicesHAProxyBackendServerEndpointResponse405,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_406 import (
    PatchServicesHAProxyBackendServerEndpointResponse406,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_409 import (
    PatchServicesHAProxyBackendServerEndpointResponse409,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_415 import (
    PatchServicesHAProxyBackendServerEndpointResponse415,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_422 import (
    PatchServicesHAProxyBackendServerEndpointResponse422,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_424 import (
    PatchServicesHAProxyBackendServerEndpointResponse424,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_500 import (
    PatchServicesHAProxyBackendServerEndpointResponse500,
)
from ...models.patch_services_ha_proxy_backend_server_endpoint_response_503 import (
    PatchServicesHAProxyBackendServerEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyBackendServerEndpointJsonBody
    | PatchServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/backend/server",
    }

    if isinstance(body, PatchServicesHAProxyBackendServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyBackendServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyBackendServerEndpointResponse400
    | PatchServicesHAProxyBackendServerEndpointResponse401
    | PatchServicesHAProxyBackendServerEndpointResponse403
    | PatchServicesHAProxyBackendServerEndpointResponse404
    | PatchServicesHAProxyBackendServerEndpointResponse405
    | PatchServicesHAProxyBackendServerEndpointResponse406
    | PatchServicesHAProxyBackendServerEndpointResponse409
    | PatchServicesHAProxyBackendServerEndpointResponse415
    | PatchServicesHAProxyBackendServerEndpointResponse422
    | PatchServicesHAProxyBackendServerEndpointResponse424
    | PatchServicesHAProxyBackendServerEndpointResponse500
    | PatchServicesHAProxyBackendServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyBackendServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyBackendServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyBackendServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyBackendServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyBackendServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyBackendServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyBackendServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyBackendServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyBackendServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyBackendServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyBackendServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyBackendServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyBackendServerEndpointResponse400
    | PatchServicesHAProxyBackendServerEndpointResponse401
    | PatchServicesHAProxyBackendServerEndpointResponse403
    | PatchServicesHAProxyBackendServerEndpointResponse404
    | PatchServicesHAProxyBackendServerEndpointResponse405
    | PatchServicesHAProxyBackendServerEndpointResponse406
    | PatchServicesHAProxyBackendServerEndpointResponse409
    | PatchServicesHAProxyBackendServerEndpointResponse415
    | PatchServicesHAProxyBackendServerEndpointResponse422
    | PatchServicesHAProxyBackendServerEndpointResponse424
    | PatchServicesHAProxyBackendServerEndpointResponse500
    | PatchServicesHAProxyBackendServerEndpointResponse503
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
    body: PatchServicesHAProxyBackendServerEndpointJsonBody
    | PatchServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyBackendServerEndpointResponse400
    | PatchServicesHAProxyBackendServerEndpointResponse401
    | PatchServicesHAProxyBackendServerEndpointResponse403
    | PatchServicesHAProxyBackendServerEndpointResponse404
    | PatchServicesHAProxyBackendServerEndpointResponse405
    | PatchServicesHAProxyBackendServerEndpointResponse406
    | PatchServicesHAProxyBackendServerEndpointResponse409
    | PatchServicesHAProxyBackendServerEndpointResponse415
    | PatchServicesHAProxyBackendServerEndpointResponse422
    | PatchServicesHAProxyBackendServerEndpointResponse424
    | PatchServicesHAProxyBackendServerEndpointResponse500
    | PatchServicesHAProxyBackendServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendServerEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyBackendServerEndpointResponse400 | PatchServicesHAProxyBackendServerEndpointResponse401 | PatchServicesHAProxyBackendServerEndpointResponse403 | PatchServicesHAProxyBackendServerEndpointResponse404 | PatchServicesHAProxyBackendServerEndpointResponse405 | PatchServicesHAProxyBackendServerEndpointResponse406 | PatchServicesHAProxyBackendServerEndpointResponse409 | PatchServicesHAProxyBackendServerEndpointResponse415 | PatchServicesHAProxyBackendServerEndpointResponse422 | PatchServicesHAProxyBackendServerEndpointResponse424 | PatchServicesHAProxyBackendServerEndpointResponse500 | PatchServicesHAProxyBackendServerEndpointResponse503]
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
    body: PatchServicesHAProxyBackendServerEndpointJsonBody
    | PatchServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyBackendServerEndpointResponse400
    | PatchServicesHAProxyBackendServerEndpointResponse401
    | PatchServicesHAProxyBackendServerEndpointResponse403
    | PatchServicesHAProxyBackendServerEndpointResponse404
    | PatchServicesHAProxyBackendServerEndpointResponse405
    | PatchServicesHAProxyBackendServerEndpointResponse406
    | PatchServicesHAProxyBackendServerEndpointResponse409
    | PatchServicesHAProxyBackendServerEndpointResponse415
    | PatchServicesHAProxyBackendServerEndpointResponse422
    | PatchServicesHAProxyBackendServerEndpointResponse424
    | PatchServicesHAProxyBackendServerEndpointResponse500
    | PatchServicesHAProxyBackendServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendServerEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyBackendServerEndpointResponse400 | PatchServicesHAProxyBackendServerEndpointResponse401 | PatchServicesHAProxyBackendServerEndpointResponse403 | PatchServicesHAProxyBackendServerEndpointResponse404 | PatchServicesHAProxyBackendServerEndpointResponse405 | PatchServicesHAProxyBackendServerEndpointResponse406 | PatchServicesHAProxyBackendServerEndpointResponse409 | PatchServicesHAProxyBackendServerEndpointResponse415 | PatchServicesHAProxyBackendServerEndpointResponse422 | PatchServicesHAProxyBackendServerEndpointResponse424 | PatchServicesHAProxyBackendServerEndpointResponse500 | PatchServicesHAProxyBackendServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyBackendServerEndpointJsonBody
    | PatchServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyBackendServerEndpointResponse400
    | PatchServicesHAProxyBackendServerEndpointResponse401
    | PatchServicesHAProxyBackendServerEndpointResponse403
    | PatchServicesHAProxyBackendServerEndpointResponse404
    | PatchServicesHAProxyBackendServerEndpointResponse405
    | PatchServicesHAProxyBackendServerEndpointResponse406
    | PatchServicesHAProxyBackendServerEndpointResponse409
    | PatchServicesHAProxyBackendServerEndpointResponse415
    | PatchServicesHAProxyBackendServerEndpointResponse422
    | PatchServicesHAProxyBackendServerEndpointResponse424
    | PatchServicesHAProxyBackendServerEndpointResponse500
    | PatchServicesHAProxyBackendServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendServerEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyBackendServerEndpointResponse400 | PatchServicesHAProxyBackendServerEndpointResponse401 | PatchServicesHAProxyBackendServerEndpointResponse403 | PatchServicesHAProxyBackendServerEndpointResponse404 | PatchServicesHAProxyBackendServerEndpointResponse405 | PatchServicesHAProxyBackendServerEndpointResponse406 | PatchServicesHAProxyBackendServerEndpointResponse409 | PatchServicesHAProxyBackendServerEndpointResponse415 | PatchServicesHAProxyBackendServerEndpointResponse422 | PatchServicesHAProxyBackendServerEndpointResponse424 | PatchServicesHAProxyBackendServerEndpointResponse500 | PatchServicesHAProxyBackendServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyBackendServerEndpointJsonBody
    | PatchServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyBackendServerEndpointResponse400
    | PatchServicesHAProxyBackendServerEndpointResponse401
    | PatchServicesHAProxyBackendServerEndpointResponse403
    | PatchServicesHAProxyBackendServerEndpointResponse404
    | PatchServicesHAProxyBackendServerEndpointResponse405
    | PatchServicesHAProxyBackendServerEndpointResponse406
    | PatchServicesHAProxyBackendServerEndpointResponse409
    | PatchServicesHAProxyBackendServerEndpointResponse415
    | PatchServicesHAProxyBackendServerEndpointResponse422
    | PatchServicesHAProxyBackendServerEndpointResponse424
    | PatchServicesHAProxyBackendServerEndpointResponse500
    | PatchServicesHAProxyBackendServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendServerEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyBackendServerEndpointResponse400 | PatchServicesHAProxyBackendServerEndpointResponse401 | PatchServicesHAProxyBackendServerEndpointResponse403 | PatchServicesHAProxyBackendServerEndpointResponse404 | PatchServicesHAProxyBackendServerEndpointResponse405 | PatchServicesHAProxyBackendServerEndpointResponse406 | PatchServicesHAProxyBackendServerEndpointResponse409 | PatchServicesHAProxyBackendServerEndpointResponse415 | PatchServicesHAProxyBackendServerEndpointResponse422 | PatchServicesHAProxyBackendServerEndpointResponse424 | PatchServicesHAProxyBackendServerEndpointResponse500 | PatchServicesHAProxyBackendServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
