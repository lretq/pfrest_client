from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_data_body import (
    PatchServicesHAProxyFrontendACLEndpointDataBody,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_json_body import (
    PatchServicesHAProxyFrontendACLEndpointJsonBody,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_400 import (
    PatchServicesHAProxyFrontendACLEndpointResponse400,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_401 import (
    PatchServicesHAProxyFrontendACLEndpointResponse401,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_403 import (
    PatchServicesHAProxyFrontendACLEndpointResponse403,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_404 import (
    PatchServicesHAProxyFrontendACLEndpointResponse404,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_405 import (
    PatchServicesHAProxyFrontendACLEndpointResponse405,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_406 import (
    PatchServicesHAProxyFrontendACLEndpointResponse406,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_409 import (
    PatchServicesHAProxyFrontendACLEndpointResponse409,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_415 import (
    PatchServicesHAProxyFrontendACLEndpointResponse415,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_422 import (
    PatchServicesHAProxyFrontendACLEndpointResponse422,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_424 import (
    PatchServicesHAProxyFrontendACLEndpointResponse424,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_500 import (
    PatchServicesHAProxyFrontendACLEndpointResponse500,
)
from ...models.patch_services_ha_proxy_frontend_acl_endpoint_response_503 import (
    PatchServicesHAProxyFrontendACLEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyFrontendACLEndpointJsonBody
    | PatchServicesHAProxyFrontendACLEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/frontend/acl",
    }

    if isinstance(body, PatchServicesHAProxyFrontendACLEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyFrontendACLEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyFrontendACLEndpointResponse400
    | PatchServicesHAProxyFrontendACLEndpointResponse401
    | PatchServicesHAProxyFrontendACLEndpointResponse403
    | PatchServicesHAProxyFrontendACLEndpointResponse404
    | PatchServicesHAProxyFrontendACLEndpointResponse405
    | PatchServicesHAProxyFrontendACLEndpointResponse406
    | PatchServicesHAProxyFrontendACLEndpointResponse409
    | PatchServicesHAProxyFrontendACLEndpointResponse415
    | PatchServicesHAProxyFrontendACLEndpointResponse422
    | PatchServicesHAProxyFrontendACLEndpointResponse424
    | PatchServicesHAProxyFrontendACLEndpointResponse500
    | PatchServicesHAProxyFrontendACLEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyFrontendACLEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyFrontendACLEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyFrontendACLEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyFrontendACLEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyFrontendACLEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyFrontendACLEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyFrontendACLEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyFrontendACLEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyFrontendACLEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyFrontendACLEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyFrontendACLEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyFrontendACLEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyFrontendACLEndpointResponse400
    | PatchServicesHAProxyFrontendACLEndpointResponse401
    | PatchServicesHAProxyFrontendACLEndpointResponse403
    | PatchServicesHAProxyFrontendACLEndpointResponse404
    | PatchServicesHAProxyFrontendACLEndpointResponse405
    | PatchServicesHAProxyFrontendACLEndpointResponse406
    | PatchServicesHAProxyFrontendACLEndpointResponse409
    | PatchServicesHAProxyFrontendACLEndpointResponse415
    | PatchServicesHAProxyFrontendACLEndpointResponse422
    | PatchServicesHAProxyFrontendACLEndpointResponse424
    | PatchServicesHAProxyFrontendACLEndpointResponse500
    | PatchServicesHAProxyFrontendACLEndpointResponse503
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
    body: PatchServicesHAProxyFrontendACLEndpointJsonBody
    | PatchServicesHAProxyFrontendACLEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendACLEndpointResponse400
    | PatchServicesHAProxyFrontendACLEndpointResponse401
    | PatchServicesHAProxyFrontendACLEndpointResponse403
    | PatchServicesHAProxyFrontendACLEndpointResponse404
    | PatchServicesHAProxyFrontendACLEndpointResponse405
    | PatchServicesHAProxyFrontendACLEndpointResponse406
    | PatchServicesHAProxyFrontendACLEndpointResponse409
    | PatchServicesHAProxyFrontendACLEndpointResponse415
    | PatchServicesHAProxyFrontendACLEndpointResponse422
    | PatchServicesHAProxyFrontendACLEndpointResponse424
    | PatchServicesHAProxyFrontendACLEndpointResponse500
    | PatchServicesHAProxyFrontendACLEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acl-patch ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendACLEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendACLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendACLEndpointResponse400 | PatchServicesHAProxyFrontendACLEndpointResponse401 | PatchServicesHAProxyFrontendACLEndpointResponse403 | PatchServicesHAProxyFrontendACLEndpointResponse404 | PatchServicesHAProxyFrontendACLEndpointResponse405 | PatchServicesHAProxyFrontendACLEndpointResponse406 | PatchServicesHAProxyFrontendACLEndpointResponse409 | PatchServicesHAProxyFrontendACLEndpointResponse415 | PatchServicesHAProxyFrontendACLEndpointResponse422 | PatchServicesHAProxyFrontendACLEndpointResponse424 | PatchServicesHAProxyFrontendACLEndpointResponse500 | PatchServicesHAProxyFrontendACLEndpointResponse503]
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
    body: PatchServicesHAProxyFrontendACLEndpointJsonBody
    | PatchServicesHAProxyFrontendACLEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendACLEndpointResponse400
    | PatchServicesHAProxyFrontendACLEndpointResponse401
    | PatchServicesHAProxyFrontendACLEndpointResponse403
    | PatchServicesHAProxyFrontendACLEndpointResponse404
    | PatchServicesHAProxyFrontendACLEndpointResponse405
    | PatchServicesHAProxyFrontendACLEndpointResponse406
    | PatchServicesHAProxyFrontendACLEndpointResponse409
    | PatchServicesHAProxyFrontendACLEndpointResponse415
    | PatchServicesHAProxyFrontendACLEndpointResponse422
    | PatchServicesHAProxyFrontendACLEndpointResponse424
    | PatchServicesHAProxyFrontendACLEndpointResponse500
    | PatchServicesHAProxyFrontendACLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acl-patch ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendACLEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendACLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendACLEndpointResponse400 | PatchServicesHAProxyFrontendACLEndpointResponse401 | PatchServicesHAProxyFrontendACLEndpointResponse403 | PatchServicesHAProxyFrontendACLEndpointResponse404 | PatchServicesHAProxyFrontendACLEndpointResponse405 | PatchServicesHAProxyFrontendACLEndpointResponse406 | PatchServicesHAProxyFrontendACLEndpointResponse409 | PatchServicesHAProxyFrontendACLEndpointResponse415 | PatchServicesHAProxyFrontendACLEndpointResponse422 | PatchServicesHAProxyFrontendACLEndpointResponse424 | PatchServicesHAProxyFrontendACLEndpointResponse500 | PatchServicesHAProxyFrontendACLEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendACLEndpointJsonBody
    | PatchServicesHAProxyFrontendACLEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendACLEndpointResponse400
    | PatchServicesHAProxyFrontendACLEndpointResponse401
    | PatchServicesHAProxyFrontendACLEndpointResponse403
    | PatchServicesHAProxyFrontendACLEndpointResponse404
    | PatchServicesHAProxyFrontendACLEndpointResponse405
    | PatchServicesHAProxyFrontendACLEndpointResponse406
    | PatchServicesHAProxyFrontendACLEndpointResponse409
    | PatchServicesHAProxyFrontendACLEndpointResponse415
    | PatchServicesHAProxyFrontendACLEndpointResponse422
    | PatchServicesHAProxyFrontendACLEndpointResponse424
    | PatchServicesHAProxyFrontendACLEndpointResponse500
    | PatchServicesHAProxyFrontendACLEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acl-patch ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendACLEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendACLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendACLEndpointResponse400 | PatchServicesHAProxyFrontendACLEndpointResponse401 | PatchServicesHAProxyFrontendACLEndpointResponse403 | PatchServicesHAProxyFrontendACLEndpointResponse404 | PatchServicesHAProxyFrontendACLEndpointResponse405 | PatchServicesHAProxyFrontendACLEndpointResponse406 | PatchServicesHAProxyFrontendACLEndpointResponse409 | PatchServicesHAProxyFrontendACLEndpointResponse415 | PatchServicesHAProxyFrontendACLEndpointResponse422 | PatchServicesHAProxyFrontendACLEndpointResponse424 | PatchServicesHAProxyFrontendACLEndpointResponse500 | PatchServicesHAProxyFrontendACLEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendACLEndpointJsonBody
    | PatchServicesHAProxyFrontendACLEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendACLEndpointResponse400
    | PatchServicesHAProxyFrontendACLEndpointResponse401
    | PatchServicesHAProxyFrontendACLEndpointResponse403
    | PatchServicesHAProxyFrontendACLEndpointResponse404
    | PatchServicesHAProxyFrontendACLEndpointResponse405
    | PatchServicesHAProxyFrontendACLEndpointResponse406
    | PatchServicesHAProxyFrontendACLEndpointResponse409
    | PatchServicesHAProxyFrontendACLEndpointResponse415
    | PatchServicesHAProxyFrontendACLEndpointResponse422
    | PatchServicesHAProxyFrontendACLEndpointResponse424
    | PatchServicesHAProxyFrontendACLEndpointResponse500
    | PatchServicesHAProxyFrontendACLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyFrontendACL<br>**Parent model**: HAProxyFrontend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-frontend-acl-patch ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendACLEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendACLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendACLEndpointResponse400 | PatchServicesHAProxyFrontendACLEndpointResponse401 | PatchServicesHAProxyFrontendACLEndpointResponse403 | PatchServicesHAProxyFrontendACLEndpointResponse404 | PatchServicesHAProxyFrontendACLEndpointResponse405 | PatchServicesHAProxyFrontendACLEndpointResponse406 | PatchServicesHAProxyFrontendACLEndpointResponse409 | PatchServicesHAProxyFrontendACLEndpointResponse415 | PatchServicesHAProxyFrontendACLEndpointResponse422 | PatchServicesHAProxyFrontendACLEndpointResponse424 | PatchServicesHAProxyFrontendACLEndpointResponse500 | PatchServicesHAProxyFrontendACLEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
