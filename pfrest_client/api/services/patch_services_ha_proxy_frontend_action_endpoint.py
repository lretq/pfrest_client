from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_frontend_action_endpoint_data_body import (
    PatchServicesHAProxyFrontendActionEndpointDataBody,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_json_body import (
    PatchServicesHAProxyFrontendActionEndpointJsonBody,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_400 import (
    PatchServicesHAProxyFrontendActionEndpointResponse400,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_401 import (
    PatchServicesHAProxyFrontendActionEndpointResponse401,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_403 import (
    PatchServicesHAProxyFrontendActionEndpointResponse403,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_404 import (
    PatchServicesHAProxyFrontendActionEndpointResponse404,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_405 import (
    PatchServicesHAProxyFrontendActionEndpointResponse405,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_406 import (
    PatchServicesHAProxyFrontendActionEndpointResponse406,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_409 import (
    PatchServicesHAProxyFrontendActionEndpointResponse409,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_415 import (
    PatchServicesHAProxyFrontendActionEndpointResponse415,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_422 import (
    PatchServicesHAProxyFrontendActionEndpointResponse422,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_424 import (
    PatchServicesHAProxyFrontendActionEndpointResponse424,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_500 import (
    PatchServicesHAProxyFrontendActionEndpointResponse500,
)
from ...models.patch_services_ha_proxy_frontend_action_endpoint_response_503 import (
    PatchServicesHAProxyFrontendActionEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyFrontendActionEndpointJsonBody
    | PatchServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/frontend/action",
    }

    if isinstance(body, PatchServicesHAProxyFrontendActionEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyFrontendActionEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyFrontendActionEndpointResponse400
    | PatchServicesHAProxyFrontendActionEndpointResponse401
    | PatchServicesHAProxyFrontendActionEndpointResponse403
    | PatchServicesHAProxyFrontendActionEndpointResponse404
    | PatchServicesHAProxyFrontendActionEndpointResponse405
    | PatchServicesHAProxyFrontendActionEndpointResponse406
    | PatchServicesHAProxyFrontendActionEndpointResponse409
    | PatchServicesHAProxyFrontendActionEndpointResponse415
    | PatchServicesHAProxyFrontendActionEndpointResponse422
    | PatchServicesHAProxyFrontendActionEndpointResponse424
    | PatchServicesHAProxyFrontendActionEndpointResponse500
    | PatchServicesHAProxyFrontendActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyFrontendActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyFrontendActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyFrontendActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyFrontendActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyFrontendActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyFrontendActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyFrontendActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyFrontendActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyFrontendActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyFrontendActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyFrontendActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyFrontendActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyFrontendActionEndpointResponse400
    | PatchServicesHAProxyFrontendActionEndpointResponse401
    | PatchServicesHAProxyFrontendActionEndpointResponse403
    | PatchServicesHAProxyFrontendActionEndpointResponse404
    | PatchServicesHAProxyFrontendActionEndpointResponse405
    | PatchServicesHAProxyFrontendActionEndpointResponse406
    | PatchServicesHAProxyFrontendActionEndpointResponse409
    | PatchServicesHAProxyFrontendActionEndpointResponse415
    | PatchServicesHAProxyFrontendActionEndpointResponse422
    | PatchServicesHAProxyFrontendActionEndpointResponse424
    | PatchServicesHAProxyFrontendActionEndpointResponse500
    | PatchServicesHAProxyFrontendActionEndpointResponse503
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
    body: PatchServicesHAProxyFrontendActionEndpointJsonBody
    | PatchServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendActionEndpointResponse400
    | PatchServicesHAProxyFrontendActionEndpointResponse401
    | PatchServicesHAProxyFrontendActionEndpointResponse403
    | PatchServicesHAProxyFrontendActionEndpointResponse404
    | PatchServicesHAProxyFrontendActionEndpointResponse405
    | PatchServicesHAProxyFrontendActionEndpointResponse406
    | PatchServicesHAProxyFrontendActionEndpointResponse409
    | PatchServicesHAProxyFrontendActionEndpointResponse415
    | PatchServicesHAProxyFrontendActionEndpointResponse422
    | PatchServicesHAProxyFrontendActionEndpointResponse424
    | PatchServicesHAProxyFrontendActionEndpointResponse500
    | PatchServicesHAProxyFrontendActionEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAction<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-action-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendActionEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendActionEndpointResponse400 | PatchServicesHAProxyFrontendActionEndpointResponse401 | PatchServicesHAProxyFrontendActionEndpointResponse403 | PatchServicesHAProxyFrontendActionEndpointResponse404 | PatchServicesHAProxyFrontendActionEndpointResponse405 | PatchServicesHAProxyFrontendActionEndpointResponse406 | PatchServicesHAProxyFrontendActionEndpointResponse409 | PatchServicesHAProxyFrontendActionEndpointResponse415 | PatchServicesHAProxyFrontendActionEndpointResponse422 | PatchServicesHAProxyFrontendActionEndpointResponse424 | PatchServicesHAProxyFrontendActionEndpointResponse500 | PatchServicesHAProxyFrontendActionEndpointResponse503]
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
    body: PatchServicesHAProxyFrontendActionEndpointJsonBody
    | PatchServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendActionEndpointResponse400
    | PatchServicesHAProxyFrontendActionEndpointResponse401
    | PatchServicesHAProxyFrontendActionEndpointResponse403
    | PatchServicesHAProxyFrontendActionEndpointResponse404
    | PatchServicesHAProxyFrontendActionEndpointResponse405
    | PatchServicesHAProxyFrontendActionEndpointResponse406
    | PatchServicesHAProxyFrontendActionEndpointResponse409
    | PatchServicesHAProxyFrontendActionEndpointResponse415
    | PatchServicesHAProxyFrontendActionEndpointResponse422
    | PatchServicesHAProxyFrontendActionEndpointResponse424
    | PatchServicesHAProxyFrontendActionEndpointResponse500
    | PatchServicesHAProxyFrontendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAction<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-action-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendActionEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendActionEndpointResponse400 | PatchServicesHAProxyFrontendActionEndpointResponse401 | PatchServicesHAProxyFrontendActionEndpointResponse403 | PatchServicesHAProxyFrontendActionEndpointResponse404 | PatchServicesHAProxyFrontendActionEndpointResponse405 | PatchServicesHAProxyFrontendActionEndpointResponse406 | PatchServicesHAProxyFrontendActionEndpointResponse409 | PatchServicesHAProxyFrontendActionEndpointResponse415 | PatchServicesHAProxyFrontendActionEndpointResponse422 | PatchServicesHAProxyFrontendActionEndpointResponse424 | PatchServicesHAProxyFrontendActionEndpointResponse500 | PatchServicesHAProxyFrontendActionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendActionEndpointJsonBody
    | PatchServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendActionEndpointResponse400
    | PatchServicesHAProxyFrontendActionEndpointResponse401
    | PatchServicesHAProxyFrontendActionEndpointResponse403
    | PatchServicesHAProxyFrontendActionEndpointResponse404
    | PatchServicesHAProxyFrontendActionEndpointResponse405
    | PatchServicesHAProxyFrontendActionEndpointResponse406
    | PatchServicesHAProxyFrontendActionEndpointResponse409
    | PatchServicesHAProxyFrontendActionEndpointResponse415
    | PatchServicesHAProxyFrontendActionEndpointResponse422
    | PatchServicesHAProxyFrontendActionEndpointResponse424
    | PatchServicesHAProxyFrontendActionEndpointResponse500
    | PatchServicesHAProxyFrontendActionEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAction<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-action-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendActionEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendActionEndpointResponse400 | PatchServicesHAProxyFrontendActionEndpointResponse401 | PatchServicesHAProxyFrontendActionEndpointResponse403 | PatchServicesHAProxyFrontendActionEndpointResponse404 | PatchServicesHAProxyFrontendActionEndpointResponse405 | PatchServicesHAProxyFrontendActionEndpointResponse406 | PatchServicesHAProxyFrontendActionEndpointResponse409 | PatchServicesHAProxyFrontendActionEndpointResponse415 | PatchServicesHAProxyFrontendActionEndpointResponse422 | PatchServicesHAProxyFrontendActionEndpointResponse424 | PatchServicesHAProxyFrontendActionEndpointResponse500 | PatchServicesHAProxyFrontendActionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendActionEndpointJsonBody
    | PatchServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendActionEndpointResponse400
    | PatchServicesHAProxyFrontendActionEndpointResponse401
    | PatchServicesHAProxyFrontendActionEndpointResponse403
    | PatchServicesHAProxyFrontendActionEndpointResponse404
    | PatchServicesHAProxyFrontendActionEndpointResponse405
    | PatchServicesHAProxyFrontendActionEndpointResponse406
    | PatchServicesHAProxyFrontendActionEndpointResponse409
    | PatchServicesHAProxyFrontendActionEndpointResponse415
    | PatchServicesHAProxyFrontendActionEndpointResponse422
    | PatchServicesHAProxyFrontendActionEndpointResponse424
    | PatchServicesHAProxyFrontendActionEndpointResponse500
    | PatchServicesHAProxyFrontendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyFrontendAction<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-action-patch ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendActionEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendActionEndpointResponse400 | PatchServicesHAProxyFrontendActionEndpointResponse401 | PatchServicesHAProxyFrontendActionEndpointResponse403 | PatchServicesHAProxyFrontendActionEndpointResponse404 | PatchServicesHAProxyFrontendActionEndpointResponse405 | PatchServicesHAProxyFrontendActionEndpointResponse406 | PatchServicesHAProxyFrontendActionEndpointResponse409 | PatchServicesHAProxyFrontendActionEndpointResponse415 | PatchServicesHAProxyFrontendActionEndpointResponse422 | PatchServicesHAProxyFrontendActionEndpointResponse424 | PatchServicesHAProxyFrontendActionEndpointResponse500 | PatchServicesHAProxyFrontendActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
