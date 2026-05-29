from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_backend_action_endpoint_data_body import (
    PatchServicesHAProxyBackendActionEndpointDataBody,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_json_body import (
    PatchServicesHAProxyBackendActionEndpointJsonBody,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_400 import (
    PatchServicesHAProxyBackendActionEndpointResponse400,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_401 import (
    PatchServicesHAProxyBackendActionEndpointResponse401,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_403 import (
    PatchServicesHAProxyBackendActionEndpointResponse403,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_404 import (
    PatchServicesHAProxyBackendActionEndpointResponse404,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_405 import (
    PatchServicesHAProxyBackendActionEndpointResponse405,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_406 import (
    PatchServicesHAProxyBackendActionEndpointResponse406,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_409 import (
    PatchServicesHAProxyBackendActionEndpointResponse409,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_415 import (
    PatchServicesHAProxyBackendActionEndpointResponse415,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_422 import (
    PatchServicesHAProxyBackendActionEndpointResponse422,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_424 import (
    PatchServicesHAProxyBackendActionEndpointResponse424,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_500 import (
    PatchServicesHAProxyBackendActionEndpointResponse500,
)
from ...models.patch_services_ha_proxy_backend_action_endpoint_response_503 import (
    PatchServicesHAProxyBackendActionEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyBackendActionEndpointJsonBody
    | PatchServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/backend/action",
    }

    if isinstance(body, PatchServicesHAProxyBackendActionEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyBackendActionEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyBackendActionEndpointResponse400
    | PatchServicesHAProxyBackendActionEndpointResponse401
    | PatchServicesHAProxyBackendActionEndpointResponse403
    | PatchServicesHAProxyBackendActionEndpointResponse404
    | PatchServicesHAProxyBackendActionEndpointResponse405
    | PatchServicesHAProxyBackendActionEndpointResponse406
    | PatchServicesHAProxyBackendActionEndpointResponse409
    | PatchServicesHAProxyBackendActionEndpointResponse415
    | PatchServicesHAProxyBackendActionEndpointResponse422
    | PatchServicesHAProxyBackendActionEndpointResponse424
    | PatchServicesHAProxyBackendActionEndpointResponse500
    | PatchServicesHAProxyBackendActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyBackendActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyBackendActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyBackendActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyBackendActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyBackendActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyBackendActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyBackendActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyBackendActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyBackendActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyBackendActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyBackendActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyBackendActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyBackendActionEndpointResponse400
    | PatchServicesHAProxyBackendActionEndpointResponse401
    | PatchServicesHAProxyBackendActionEndpointResponse403
    | PatchServicesHAProxyBackendActionEndpointResponse404
    | PatchServicesHAProxyBackendActionEndpointResponse405
    | PatchServicesHAProxyBackendActionEndpointResponse406
    | PatchServicesHAProxyBackendActionEndpointResponse409
    | PatchServicesHAProxyBackendActionEndpointResponse415
    | PatchServicesHAProxyBackendActionEndpointResponse422
    | PatchServicesHAProxyBackendActionEndpointResponse424
    | PatchServicesHAProxyBackendActionEndpointResponse500
    | PatchServicesHAProxyBackendActionEndpointResponse503
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
    body: PatchServicesHAProxyBackendActionEndpointJsonBody
    | PatchServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyBackendActionEndpointResponse400
    | PatchServicesHAProxyBackendActionEndpointResponse401
    | PatchServicesHAProxyBackendActionEndpointResponse403
    | PatchServicesHAProxyBackendActionEndpointResponse404
    | PatchServicesHAProxyBackendActionEndpointResponse405
    | PatchServicesHAProxyBackendActionEndpointResponse406
    | PatchServicesHAProxyBackendActionEndpointResponse409
    | PatchServicesHAProxyBackendActionEndpointResponse415
    | PatchServicesHAProxyBackendActionEndpointResponse422
    | PatchServicesHAProxyBackendActionEndpointResponse424
    | PatchServicesHAProxyBackendActionEndpointResponse500
    | PatchServicesHAProxyBackendActionEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendActionEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyBackendActionEndpointResponse400 | PatchServicesHAProxyBackendActionEndpointResponse401 | PatchServicesHAProxyBackendActionEndpointResponse403 | PatchServicesHAProxyBackendActionEndpointResponse404 | PatchServicesHAProxyBackendActionEndpointResponse405 | PatchServicesHAProxyBackendActionEndpointResponse406 | PatchServicesHAProxyBackendActionEndpointResponse409 | PatchServicesHAProxyBackendActionEndpointResponse415 | PatchServicesHAProxyBackendActionEndpointResponse422 | PatchServicesHAProxyBackendActionEndpointResponse424 | PatchServicesHAProxyBackendActionEndpointResponse500 | PatchServicesHAProxyBackendActionEndpointResponse503]
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
    body: PatchServicesHAProxyBackendActionEndpointJsonBody
    | PatchServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyBackendActionEndpointResponse400
    | PatchServicesHAProxyBackendActionEndpointResponse401
    | PatchServicesHAProxyBackendActionEndpointResponse403
    | PatchServicesHAProxyBackendActionEndpointResponse404
    | PatchServicesHAProxyBackendActionEndpointResponse405
    | PatchServicesHAProxyBackendActionEndpointResponse406
    | PatchServicesHAProxyBackendActionEndpointResponse409
    | PatchServicesHAProxyBackendActionEndpointResponse415
    | PatchServicesHAProxyBackendActionEndpointResponse422
    | PatchServicesHAProxyBackendActionEndpointResponse424
    | PatchServicesHAProxyBackendActionEndpointResponse500
    | PatchServicesHAProxyBackendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendActionEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyBackendActionEndpointResponse400 | PatchServicesHAProxyBackendActionEndpointResponse401 | PatchServicesHAProxyBackendActionEndpointResponse403 | PatchServicesHAProxyBackendActionEndpointResponse404 | PatchServicesHAProxyBackendActionEndpointResponse405 | PatchServicesHAProxyBackendActionEndpointResponse406 | PatchServicesHAProxyBackendActionEndpointResponse409 | PatchServicesHAProxyBackendActionEndpointResponse415 | PatchServicesHAProxyBackendActionEndpointResponse422 | PatchServicesHAProxyBackendActionEndpointResponse424 | PatchServicesHAProxyBackendActionEndpointResponse500 | PatchServicesHAProxyBackendActionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyBackendActionEndpointJsonBody
    | PatchServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyBackendActionEndpointResponse400
    | PatchServicesHAProxyBackendActionEndpointResponse401
    | PatchServicesHAProxyBackendActionEndpointResponse403
    | PatchServicesHAProxyBackendActionEndpointResponse404
    | PatchServicesHAProxyBackendActionEndpointResponse405
    | PatchServicesHAProxyBackendActionEndpointResponse406
    | PatchServicesHAProxyBackendActionEndpointResponse409
    | PatchServicesHAProxyBackendActionEndpointResponse415
    | PatchServicesHAProxyBackendActionEndpointResponse422
    | PatchServicesHAProxyBackendActionEndpointResponse424
    | PatchServicesHAProxyBackendActionEndpointResponse500
    | PatchServicesHAProxyBackendActionEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendActionEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyBackendActionEndpointResponse400 | PatchServicesHAProxyBackendActionEndpointResponse401 | PatchServicesHAProxyBackendActionEndpointResponse403 | PatchServicesHAProxyBackendActionEndpointResponse404 | PatchServicesHAProxyBackendActionEndpointResponse405 | PatchServicesHAProxyBackendActionEndpointResponse406 | PatchServicesHAProxyBackendActionEndpointResponse409 | PatchServicesHAProxyBackendActionEndpointResponse415 | PatchServicesHAProxyBackendActionEndpointResponse422 | PatchServicesHAProxyBackendActionEndpointResponse424 | PatchServicesHAProxyBackendActionEndpointResponse500 | PatchServicesHAProxyBackendActionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyBackendActionEndpointJsonBody
    | PatchServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyBackendActionEndpointResponse400
    | PatchServicesHAProxyBackendActionEndpointResponse401
    | PatchServicesHAProxyBackendActionEndpointResponse403
    | PatchServicesHAProxyBackendActionEndpointResponse404
    | PatchServicesHAProxyBackendActionEndpointResponse405
    | PatchServicesHAProxyBackendActionEndpointResponse406
    | PatchServicesHAProxyBackendActionEndpointResponse409
    | PatchServicesHAProxyBackendActionEndpointResponse415
    | PatchServicesHAProxyBackendActionEndpointResponse422
    | PatchServicesHAProxyBackendActionEndpointResponse424
    | PatchServicesHAProxyBackendActionEndpointResponse500
    | PatchServicesHAProxyBackendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendActionEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyBackendActionEndpointResponse400 | PatchServicesHAProxyBackendActionEndpointResponse401 | PatchServicesHAProxyBackendActionEndpointResponse403 | PatchServicesHAProxyBackendActionEndpointResponse404 | PatchServicesHAProxyBackendActionEndpointResponse405 | PatchServicesHAProxyBackendActionEndpointResponse406 | PatchServicesHAProxyBackendActionEndpointResponse409 | PatchServicesHAProxyBackendActionEndpointResponse415 | PatchServicesHAProxyBackendActionEndpointResponse422 | PatchServicesHAProxyBackendActionEndpointResponse424 | PatchServicesHAProxyBackendActionEndpointResponse500 | PatchServicesHAProxyBackendActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
