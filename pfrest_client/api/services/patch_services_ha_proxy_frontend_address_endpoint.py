from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_frontend_address_endpoint_data_body import (
    PatchServicesHAProxyFrontendAddressEndpointDataBody,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_json_body import (
    PatchServicesHAProxyFrontendAddressEndpointJsonBody,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_400 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse400,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_401 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse401,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_403 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse403,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_404 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse404,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_405 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse405,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_406 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse406,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_409 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse409,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_415 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse415,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_422 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse422,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_424 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse424,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_500 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse500,
)
from ...models.patch_services_ha_proxy_frontend_address_endpoint_response_503 import (
    PatchServicesHAProxyFrontendAddressEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyFrontendAddressEndpointJsonBody
    | PatchServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/frontend/address",
    }

    if isinstance(body, PatchServicesHAProxyFrontendAddressEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyFrontendAddressEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyFrontendAddressEndpointResponse400
    | PatchServicesHAProxyFrontendAddressEndpointResponse401
    | PatchServicesHAProxyFrontendAddressEndpointResponse403
    | PatchServicesHAProxyFrontendAddressEndpointResponse404
    | PatchServicesHAProxyFrontendAddressEndpointResponse405
    | PatchServicesHAProxyFrontendAddressEndpointResponse406
    | PatchServicesHAProxyFrontendAddressEndpointResponse409
    | PatchServicesHAProxyFrontendAddressEndpointResponse415
    | PatchServicesHAProxyFrontendAddressEndpointResponse422
    | PatchServicesHAProxyFrontendAddressEndpointResponse424
    | PatchServicesHAProxyFrontendAddressEndpointResponse500
    | PatchServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyFrontendAddressEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyFrontendAddressEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyFrontendAddressEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyFrontendAddressEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyFrontendAddressEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyFrontendAddressEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyFrontendAddressEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyFrontendAddressEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyFrontendAddressEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyFrontendAddressEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyFrontendAddressEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyFrontendAddressEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyFrontendAddressEndpointResponse400
    | PatchServicesHAProxyFrontendAddressEndpointResponse401
    | PatchServicesHAProxyFrontendAddressEndpointResponse403
    | PatchServicesHAProxyFrontendAddressEndpointResponse404
    | PatchServicesHAProxyFrontendAddressEndpointResponse405
    | PatchServicesHAProxyFrontendAddressEndpointResponse406
    | PatchServicesHAProxyFrontendAddressEndpointResponse409
    | PatchServicesHAProxyFrontendAddressEndpointResponse415
    | PatchServicesHAProxyFrontendAddressEndpointResponse422
    | PatchServicesHAProxyFrontendAddressEndpointResponse424
    | PatchServicesHAProxyFrontendAddressEndpointResponse500
    | PatchServicesHAProxyFrontendAddressEndpointResponse503
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
    body: PatchServicesHAProxyFrontendAddressEndpointJsonBody
    | PatchServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendAddressEndpointResponse400
    | PatchServicesHAProxyFrontendAddressEndpointResponse401
    | PatchServicesHAProxyFrontendAddressEndpointResponse403
    | PatchServicesHAProxyFrontendAddressEndpointResponse404
    | PatchServicesHAProxyFrontendAddressEndpointResponse405
    | PatchServicesHAProxyFrontendAddressEndpointResponse406
    | PatchServicesHAProxyFrontendAddressEndpointResponse409
    | PatchServicesHAProxyFrontendAddressEndpointResponse415
    | PatchServicesHAProxyFrontendAddressEndpointResponse422
    | PatchServicesHAProxyFrontendAddressEndpointResponse424
    | PatchServicesHAProxyFrontendAddressEndpointResponse500
    | PatchServicesHAProxyFrontendAddressEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendAddressEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendAddressEndpointResponse400 | PatchServicesHAProxyFrontendAddressEndpointResponse401 | PatchServicesHAProxyFrontendAddressEndpointResponse403 | PatchServicesHAProxyFrontendAddressEndpointResponse404 | PatchServicesHAProxyFrontendAddressEndpointResponse405 | PatchServicesHAProxyFrontendAddressEndpointResponse406 | PatchServicesHAProxyFrontendAddressEndpointResponse409 | PatchServicesHAProxyFrontendAddressEndpointResponse415 | PatchServicesHAProxyFrontendAddressEndpointResponse422 | PatchServicesHAProxyFrontendAddressEndpointResponse424 | PatchServicesHAProxyFrontendAddressEndpointResponse500 | PatchServicesHAProxyFrontendAddressEndpointResponse503]
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
    body: PatchServicesHAProxyFrontendAddressEndpointJsonBody
    | PatchServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendAddressEndpointResponse400
    | PatchServicesHAProxyFrontendAddressEndpointResponse401
    | PatchServicesHAProxyFrontendAddressEndpointResponse403
    | PatchServicesHAProxyFrontendAddressEndpointResponse404
    | PatchServicesHAProxyFrontendAddressEndpointResponse405
    | PatchServicesHAProxyFrontendAddressEndpointResponse406
    | PatchServicesHAProxyFrontendAddressEndpointResponse409
    | PatchServicesHAProxyFrontendAddressEndpointResponse415
    | PatchServicesHAProxyFrontendAddressEndpointResponse422
    | PatchServicesHAProxyFrontendAddressEndpointResponse424
    | PatchServicesHAProxyFrontendAddressEndpointResponse500
    | PatchServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendAddressEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendAddressEndpointResponse400 | PatchServicesHAProxyFrontendAddressEndpointResponse401 | PatchServicesHAProxyFrontendAddressEndpointResponse403 | PatchServicesHAProxyFrontendAddressEndpointResponse404 | PatchServicesHAProxyFrontendAddressEndpointResponse405 | PatchServicesHAProxyFrontendAddressEndpointResponse406 | PatchServicesHAProxyFrontendAddressEndpointResponse409 | PatchServicesHAProxyFrontendAddressEndpointResponse415 | PatchServicesHAProxyFrontendAddressEndpointResponse422 | PatchServicesHAProxyFrontendAddressEndpointResponse424 | PatchServicesHAProxyFrontendAddressEndpointResponse500 | PatchServicesHAProxyFrontendAddressEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendAddressEndpointJsonBody
    | PatchServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendAddressEndpointResponse400
    | PatchServicesHAProxyFrontendAddressEndpointResponse401
    | PatchServicesHAProxyFrontendAddressEndpointResponse403
    | PatchServicesHAProxyFrontendAddressEndpointResponse404
    | PatchServicesHAProxyFrontendAddressEndpointResponse405
    | PatchServicesHAProxyFrontendAddressEndpointResponse406
    | PatchServicesHAProxyFrontendAddressEndpointResponse409
    | PatchServicesHAProxyFrontendAddressEndpointResponse415
    | PatchServicesHAProxyFrontendAddressEndpointResponse422
    | PatchServicesHAProxyFrontendAddressEndpointResponse424
    | PatchServicesHAProxyFrontendAddressEndpointResponse500
    | PatchServicesHAProxyFrontendAddressEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendAddressEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendAddressEndpointResponse400 | PatchServicesHAProxyFrontendAddressEndpointResponse401 | PatchServicesHAProxyFrontendAddressEndpointResponse403 | PatchServicesHAProxyFrontendAddressEndpointResponse404 | PatchServicesHAProxyFrontendAddressEndpointResponse405 | PatchServicesHAProxyFrontendAddressEndpointResponse406 | PatchServicesHAProxyFrontendAddressEndpointResponse409 | PatchServicesHAProxyFrontendAddressEndpointResponse415 | PatchServicesHAProxyFrontendAddressEndpointResponse422 | PatchServicesHAProxyFrontendAddressEndpointResponse424 | PatchServicesHAProxyFrontendAddressEndpointResponse500 | PatchServicesHAProxyFrontendAddressEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendAddressEndpointJsonBody
    | PatchServicesHAProxyFrontendAddressEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendAddressEndpointResponse400
    | PatchServicesHAProxyFrontendAddressEndpointResponse401
    | PatchServicesHAProxyFrontendAddressEndpointResponse403
    | PatchServicesHAProxyFrontendAddressEndpointResponse404
    | PatchServicesHAProxyFrontendAddressEndpointResponse405
    | PatchServicesHAProxyFrontendAddressEndpointResponse406
    | PatchServicesHAProxyFrontendAddressEndpointResponse409
    | PatchServicesHAProxyFrontendAddressEndpointResponse415
    | PatchServicesHAProxyFrontendAddressEndpointResponse422
    | PatchServicesHAProxyFrontendAddressEndpointResponse424
    | PatchServicesHAProxyFrontendAddressEndpointResponse500
    | PatchServicesHAProxyFrontendAddressEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Address.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAddress<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-address-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendAddressEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendAddressEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendAddressEndpointResponse400 | PatchServicesHAProxyFrontendAddressEndpointResponse401 | PatchServicesHAProxyFrontendAddressEndpointResponse403 | PatchServicesHAProxyFrontendAddressEndpointResponse404 | PatchServicesHAProxyFrontendAddressEndpointResponse405 | PatchServicesHAProxyFrontendAddressEndpointResponse406 | PatchServicesHAProxyFrontendAddressEndpointResponse409 | PatchServicesHAProxyFrontendAddressEndpointResponse415 | PatchServicesHAProxyFrontendAddressEndpointResponse422 | PatchServicesHAProxyFrontendAddressEndpointResponse424 | PatchServicesHAProxyFrontendAddressEndpointResponse500 | PatchServicesHAProxyFrontendAddressEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
