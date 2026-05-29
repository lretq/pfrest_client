from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_data_body import (
    PatchServicesHAProxyFrontendErrorFileEndpointDataBody,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_json_body import (
    PatchServicesHAProxyFrontendErrorFileEndpointJsonBody,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_400 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse400,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_401 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse401,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_403 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse403,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_404 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse404,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_405 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse405,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_406 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse406,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_409 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse409,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_415 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse415,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_422 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse422,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_424 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse424,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_500 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse500,
)
from ...models.patch_services_ha_proxy_frontend_error_file_endpoint_response_503 import (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyFrontendErrorFileEndpointJsonBody
    | PatchServicesHAProxyFrontendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/frontend/error_file",
    }

    if isinstance(body, PatchServicesHAProxyFrontendErrorFileEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyFrontendErrorFileEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse400
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse401
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse403
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse404
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse405
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse406
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse409
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse415
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse422
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse424
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse500
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyFrontendErrorFileEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyFrontendErrorFileEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyFrontendErrorFileEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyFrontendErrorFileEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyFrontendErrorFileEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyFrontendErrorFileEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyFrontendErrorFileEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyFrontendErrorFileEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyFrontendErrorFileEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyFrontendErrorFileEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyFrontendErrorFileEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyFrontendErrorFileEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyFrontendErrorFileEndpointResponse400
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse401
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse403
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse404
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse405
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse406
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse409
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse415
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse422
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse424
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse500
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse503
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
    body: PatchServicesHAProxyFrontendErrorFileEndpointJsonBody
    | PatchServicesHAProxyFrontendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendErrorFileEndpointResponse400
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse401
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse403
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse404
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse405
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse406
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse409
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse415
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse422
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse424
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse500
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendErrorFileEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendErrorFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendErrorFileEndpointResponse400 | PatchServicesHAProxyFrontendErrorFileEndpointResponse401 | PatchServicesHAProxyFrontendErrorFileEndpointResponse403 | PatchServicesHAProxyFrontendErrorFileEndpointResponse404 | PatchServicesHAProxyFrontendErrorFileEndpointResponse405 | PatchServicesHAProxyFrontendErrorFileEndpointResponse406 | PatchServicesHAProxyFrontendErrorFileEndpointResponse409 | PatchServicesHAProxyFrontendErrorFileEndpointResponse415 | PatchServicesHAProxyFrontendErrorFileEndpointResponse422 | PatchServicesHAProxyFrontendErrorFileEndpointResponse424 | PatchServicesHAProxyFrontendErrorFileEndpointResponse500 | PatchServicesHAProxyFrontendErrorFileEndpointResponse503]
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
    body: PatchServicesHAProxyFrontendErrorFileEndpointJsonBody
    | PatchServicesHAProxyFrontendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse400
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse401
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse403
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse404
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse405
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse406
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse409
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse415
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse422
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse424
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse500
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendErrorFileEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendErrorFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendErrorFileEndpointResponse400 | PatchServicesHAProxyFrontendErrorFileEndpointResponse401 | PatchServicesHAProxyFrontendErrorFileEndpointResponse403 | PatchServicesHAProxyFrontendErrorFileEndpointResponse404 | PatchServicesHAProxyFrontendErrorFileEndpointResponse405 | PatchServicesHAProxyFrontendErrorFileEndpointResponse406 | PatchServicesHAProxyFrontendErrorFileEndpointResponse409 | PatchServicesHAProxyFrontendErrorFileEndpointResponse415 | PatchServicesHAProxyFrontendErrorFileEndpointResponse422 | PatchServicesHAProxyFrontendErrorFileEndpointResponse424 | PatchServicesHAProxyFrontendErrorFileEndpointResponse500 | PatchServicesHAProxyFrontendErrorFileEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendErrorFileEndpointJsonBody
    | PatchServicesHAProxyFrontendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendErrorFileEndpointResponse400
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse401
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse403
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse404
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse405
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse406
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse409
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse415
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse422
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse424
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse500
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendErrorFileEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendErrorFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendErrorFileEndpointResponse400 | PatchServicesHAProxyFrontendErrorFileEndpointResponse401 | PatchServicesHAProxyFrontendErrorFileEndpointResponse403 | PatchServicesHAProxyFrontendErrorFileEndpointResponse404 | PatchServicesHAProxyFrontendErrorFileEndpointResponse405 | PatchServicesHAProxyFrontendErrorFileEndpointResponse406 | PatchServicesHAProxyFrontendErrorFileEndpointResponse409 | PatchServicesHAProxyFrontendErrorFileEndpointResponse415 | PatchServicesHAProxyFrontendErrorFileEndpointResponse422 | PatchServicesHAProxyFrontendErrorFileEndpointResponse424 | PatchServicesHAProxyFrontendErrorFileEndpointResponse500 | PatchServicesHAProxyFrontendErrorFileEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendErrorFileEndpointJsonBody
    | PatchServicesHAProxyFrontendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendErrorFileEndpointResponse400
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse401
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse403
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse404
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse405
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse406
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse409
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse415
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse422
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse424
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse500
    | PatchServicesHAProxyFrontendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendErrorFile<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-error-file-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendErrorFileEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendErrorFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendErrorFileEndpointResponse400 | PatchServicesHAProxyFrontendErrorFileEndpointResponse401 | PatchServicesHAProxyFrontendErrorFileEndpointResponse403 | PatchServicesHAProxyFrontendErrorFileEndpointResponse404 | PatchServicesHAProxyFrontendErrorFileEndpointResponse405 | PatchServicesHAProxyFrontendErrorFileEndpointResponse406 | PatchServicesHAProxyFrontendErrorFileEndpointResponse409 | PatchServicesHAProxyFrontendErrorFileEndpointResponse415 | PatchServicesHAProxyFrontendErrorFileEndpointResponse422 | PatchServicesHAProxyFrontendErrorFileEndpointResponse424 | PatchServicesHAProxyFrontendErrorFileEndpointResponse500 | PatchServicesHAProxyFrontendErrorFileEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
