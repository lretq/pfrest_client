from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_backend_endpoint_data_body import PatchServicesHAProxyBackendEndpointDataBody
from ...models.patch_services_ha_proxy_backend_endpoint_json_body import PatchServicesHAProxyBackendEndpointJsonBody
from ...models.patch_services_ha_proxy_backend_endpoint_response_400 import (
    PatchServicesHAProxyBackendEndpointResponse400,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_401 import (
    PatchServicesHAProxyBackendEndpointResponse401,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_403 import (
    PatchServicesHAProxyBackendEndpointResponse403,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_404 import (
    PatchServicesHAProxyBackendEndpointResponse404,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_405 import (
    PatchServicesHAProxyBackendEndpointResponse405,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_406 import (
    PatchServicesHAProxyBackendEndpointResponse406,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_409 import (
    PatchServicesHAProxyBackendEndpointResponse409,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_415 import (
    PatchServicesHAProxyBackendEndpointResponse415,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_422 import (
    PatchServicesHAProxyBackendEndpointResponse422,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_424 import (
    PatchServicesHAProxyBackendEndpointResponse424,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_500 import (
    PatchServicesHAProxyBackendEndpointResponse500,
)
from ...models.patch_services_ha_proxy_backend_endpoint_response_503 import (
    PatchServicesHAProxyBackendEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyBackendEndpointJsonBody | PatchServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/backend",
    }

    if isinstance(body, PatchServicesHAProxyBackendEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyBackendEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyBackendEndpointResponse400
    | PatchServicesHAProxyBackendEndpointResponse401
    | PatchServicesHAProxyBackendEndpointResponse403
    | PatchServicesHAProxyBackendEndpointResponse404
    | PatchServicesHAProxyBackendEndpointResponse405
    | PatchServicesHAProxyBackendEndpointResponse406
    | PatchServicesHAProxyBackendEndpointResponse409
    | PatchServicesHAProxyBackendEndpointResponse415
    | PatchServicesHAProxyBackendEndpointResponse422
    | PatchServicesHAProxyBackendEndpointResponse424
    | PatchServicesHAProxyBackendEndpointResponse500
    | PatchServicesHAProxyBackendEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyBackendEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyBackendEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyBackendEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyBackendEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyBackendEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyBackendEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyBackendEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyBackendEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyBackendEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyBackendEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyBackendEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyBackendEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyBackendEndpointResponse400
    | PatchServicesHAProxyBackendEndpointResponse401
    | PatchServicesHAProxyBackendEndpointResponse403
    | PatchServicesHAProxyBackendEndpointResponse404
    | PatchServicesHAProxyBackendEndpointResponse405
    | PatchServicesHAProxyBackendEndpointResponse406
    | PatchServicesHAProxyBackendEndpointResponse409
    | PatchServicesHAProxyBackendEndpointResponse415
    | PatchServicesHAProxyBackendEndpointResponse422
    | PatchServicesHAProxyBackendEndpointResponse424
    | PatchServicesHAProxyBackendEndpointResponse500
    | PatchServicesHAProxyBackendEndpointResponse503
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
    body: PatchServicesHAProxyBackendEndpointJsonBody | PatchServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyBackendEndpointResponse400
    | PatchServicesHAProxyBackendEndpointResponse401
    | PatchServicesHAProxyBackendEndpointResponse403
    | PatchServicesHAProxyBackendEndpointResponse404
    | PatchServicesHAProxyBackendEndpointResponse405
    | PatchServicesHAProxyBackendEndpointResponse406
    | PatchServicesHAProxyBackendEndpointResponse409
    | PatchServicesHAProxyBackendEndpointResponse415
    | PatchServicesHAProxyBackendEndpointResponse422
    | PatchServicesHAProxyBackendEndpointResponse424
    | PatchServicesHAProxyBackendEndpointResponse500
    | PatchServicesHAProxyBackendEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyBackendEndpointResponse400 | PatchServicesHAProxyBackendEndpointResponse401 | PatchServicesHAProxyBackendEndpointResponse403 | PatchServicesHAProxyBackendEndpointResponse404 | PatchServicesHAProxyBackendEndpointResponse405 | PatchServicesHAProxyBackendEndpointResponse406 | PatchServicesHAProxyBackendEndpointResponse409 | PatchServicesHAProxyBackendEndpointResponse415 | PatchServicesHAProxyBackendEndpointResponse422 | PatchServicesHAProxyBackendEndpointResponse424 | PatchServicesHAProxyBackendEndpointResponse500 | PatchServicesHAProxyBackendEndpointResponse503]
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
    body: PatchServicesHAProxyBackendEndpointJsonBody | PatchServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesHAProxyBackendEndpointResponse400
    | PatchServicesHAProxyBackendEndpointResponse401
    | PatchServicesHAProxyBackendEndpointResponse403
    | PatchServicesHAProxyBackendEndpointResponse404
    | PatchServicesHAProxyBackendEndpointResponse405
    | PatchServicesHAProxyBackendEndpointResponse406
    | PatchServicesHAProxyBackendEndpointResponse409
    | PatchServicesHAProxyBackendEndpointResponse415
    | PatchServicesHAProxyBackendEndpointResponse422
    | PatchServicesHAProxyBackendEndpointResponse424
    | PatchServicesHAProxyBackendEndpointResponse500
    | PatchServicesHAProxyBackendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyBackendEndpointResponse400 | PatchServicesHAProxyBackendEndpointResponse401 | PatchServicesHAProxyBackendEndpointResponse403 | PatchServicesHAProxyBackendEndpointResponse404 | PatchServicesHAProxyBackendEndpointResponse405 | PatchServicesHAProxyBackendEndpointResponse406 | PatchServicesHAProxyBackendEndpointResponse409 | PatchServicesHAProxyBackendEndpointResponse415 | PatchServicesHAProxyBackendEndpointResponse422 | PatchServicesHAProxyBackendEndpointResponse424 | PatchServicesHAProxyBackendEndpointResponse500 | PatchServicesHAProxyBackendEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyBackendEndpointJsonBody | PatchServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyBackendEndpointResponse400
    | PatchServicesHAProxyBackendEndpointResponse401
    | PatchServicesHAProxyBackendEndpointResponse403
    | PatchServicesHAProxyBackendEndpointResponse404
    | PatchServicesHAProxyBackendEndpointResponse405
    | PatchServicesHAProxyBackendEndpointResponse406
    | PatchServicesHAProxyBackendEndpointResponse409
    | PatchServicesHAProxyBackendEndpointResponse415
    | PatchServicesHAProxyBackendEndpointResponse422
    | PatchServicesHAProxyBackendEndpointResponse424
    | PatchServicesHAProxyBackendEndpointResponse500
    | PatchServicesHAProxyBackendEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyBackendEndpointResponse400 | PatchServicesHAProxyBackendEndpointResponse401 | PatchServicesHAProxyBackendEndpointResponse403 | PatchServicesHAProxyBackendEndpointResponse404 | PatchServicesHAProxyBackendEndpointResponse405 | PatchServicesHAProxyBackendEndpointResponse406 | PatchServicesHAProxyBackendEndpointResponse409 | PatchServicesHAProxyBackendEndpointResponse415 | PatchServicesHAProxyBackendEndpointResponse422 | PatchServicesHAProxyBackendEndpointResponse424 | PatchServicesHAProxyBackendEndpointResponse500 | PatchServicesHAProxyBackendEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyBackendEndpointJsonBody | PatchServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesHAProxyBackendEndpointResponse400
    | PatchServicesHAProxyBackendEndpointResponse401
    | PatchServicesHAProxyBackendEndpointResponse403
    | PatchServicesHAProxyBackendEndpointResponse404
    | PatchServicesHAProxyBackendEndpointResponse405
    | PatchServicesHAProxyBackendEndpointResponse406
    | PatchServicesHAProxyBackendEndpointResponse409
    | PatchServicesHAProxyBackendEndpointResponse415
    | PatchServicesHAProxyBackendEndpointResponse422
    | PatchServicesHAProxyBackendEndpointResponse424
    | PatchServicesHAProxyBackendEndpointResponse500
    | PatchServicesHAProxyBackendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyBackendEndpointJsonBody | Unset):
        body (PatchServicesHAProxyBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyBackendEndpointResponse400 | PatchServicesHAProxyBackendEndpointResponse401 | PatchServicesHAProxyBackendEndpointResponse403 | PatchServicesHAProxyBackendEndpointResponse404 | PatchServicesHAProxyBackendEndpointResponse405 | PatchServicesHAProxyBackendEndpointResponse406 | PatchServicesHAProxyBackendEndpointResponse409 | PatchServicesHAProxyBackendEndpointResponse415 | PatchServicesHAProxyBackendEndpointResponse422 | PatchServicesHAProxyBackendEndpointResponse424 | PatchServicesHAProxyBackendEndpointResponse500 | PatchServicesHAProxyBackendEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
