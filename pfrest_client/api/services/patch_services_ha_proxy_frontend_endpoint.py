from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_frontend_endpoint_data_body import PatchServicesHAProxyFrontendEndpointDataBody
from ...models.patch_services_ha_proxy_frontend_endpoint_json_body import PatchServicesHAProxyFrontendEndpointJsonBody
from ...models.patch_services_ha_proxy_frontend_endpoint_response_400 import (
    PatchServicesHAProxyFrontendEndpointResponse400,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_401 import (
    PatchServicesHAProxyFrontendEndpointResponse401,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_403 import (
    PatchServicesHAProxyFrontendEndpointResponse403,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_404 import (
    PatchServicesHAProxyFrontendEndpointResponse404,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_405 import (
    PatchServicesHAProxyFrontendEndpointResponse405,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_406 import (
    PatchServicesHAProxyFrontendEndpointResponse406,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_409 import (
    PatchServicesHAProxyFrontendEndpointResponse409,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_415 import (
    PatchServicesHAProxyFrontendEndpointResponse415,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_422 import (
    PatchServicesHAProxyFrontendEndpointResponse422,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_424 import (
    PatchServicesHAProxyFrontendEndpointResponse424,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_500 import (
    PatchServicesHAProxyFrontendEndpointResponse500,
)
from ...models.patch_services_ha_proxy_frontend_endpoint_response_503 import (
    PatchServicesHAProxyFrontendEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyFrontendEndpointJsonBody | PatchServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/frontend",
    }

    if isinstance(body, PatchServicesHAProxyFrontendEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyFrontendEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyFrontendEndpointResponse400
    | PatchServicesHAProxyFrontendEndpointResponse401
    | PatchServicesHAProxyFrontendEndpointResponse403
    | PatchServicesHAProxyFrontendEndpointResponse404
    | PatchServicesHAProxyFrontendEndpointResponse405
    | PatchServicesHAProxyFrontendEndpointResponse406
    | PatchServicesHAProxyFrontendEndpointResponse409
    | PatchServicesHAProxyFrontendEndpointResponse415
    | PatchServicesHAProxyFrontendEndpointResponse422
    | PatchServicesHAProxyFrontendEndpointResponse424
    | PatchServicesHAProxyFrontendEndpointResponse500
    | PatchServicesHAProxyFrontendEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyFrontendEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyFrontendEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyFrontendEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyFrontendEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyFrontendEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyFrontendEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyFrontendEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyFrontendEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyFrontendEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyFrontendEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyFrontendEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyFrontendEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyFrontendEndpointResponse400
    | PatchServicesHAProxyFrontendEndpointResponse401
    | PatchServicesHAProxyFrontendEndpointResponse403
    | PatchServicesHAProxyFrontendEndpointResponse404
    | PatchServicesHAProxyFrontendEndpointResponse405
    | PatchServicesHAProxyFrontendEndpointResponse406
    | PatchServicesHAProxyFrontendEndpointResponse409
    | PatchServicesHAProxyFrontendEndpointResponse415
    | PatchServicesHAProxyFrontendEndpointResponse422
    | PatchServicesHAProxyFrontendEndpointResponse424
    | PatchServicesHAProxyFrontendEndpointResponse500
    | PatchServicesHAProxyFrontendEndpointResponse503
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
    body: PatchServicesHAProxyFrontendEndpointJsonBody | PatchServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendEndpointResponse400
    | PatchServicesHAProxyFrontendEndpointResponse401
    | PatchServicesHAProxyFrontendEndpointResponse403
    | PatchServicesHAProxyFrontendEndpointResponse404
    | PatchServicesHAProxyFrontendEndpointResponse405
    | PatchServicesHAProxyFrontendEndpointResponse406
    | PatchServicesHAProxyFrontendEndpointResponse409
    | PatchServicesHAProxyFrontendEndpointResponse415
    | PatchServicesHAProxyFrontendEndpointResponse422
    | PatchServicesHAProxyFrontendEndpointResponse424
    | PatchServicesHAProxyFrontendEndpointResponse500
    | PatchServicesHAProxyFrontendEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendEndpointResponse400 | PatchServicesHAProxyFrontendEndpointResponse401 | PatchServicesHAProxyFrontendEndpointResponse403 | PatchServicesHAProxyFrontendEndpointResponse404 | PatchServicesHAProxyFrontendEndpointResponse405 | PatchServicesHAProxyFrontendEndpointResponse406 | PatchServicesHAProxyFrontendEndpointResponse409 | PatchServicesHAProxyFrontendEndpointResponse415 | PatchServicesHAProxyFrontendEndpointResponse422 | PatchServicesHAProxyFrontendEndpointResponse424 | PatchServicesHAProxyFrontendEndpointResponse500 | PatchServicesHAProxyFrontendEndpointResponse503]
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
    body: PatchServicesHAProxyFrontendEndpointJsonBody | PatchServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendEndpointResponse400
    | PatchServicesHAProxyFrontendEndpointResponse401
    | PatchServicesHAProxyFrontendEndpointResponse403
    | PatchServicesHAProxyFrontendEndpointResponse404
    | PatchServicesHAProxyFrontendEndpointResponse405
    | PatchServicesHAProxyFrontendEndpointResponse406
    | PatchServicesHAProxyFrontendEndpointResponse409
    | PatchServicesHAProxyFrontendEndpointResponse415
    | PatchServicesHAProxyFrontendEndpointResponse422
    | PatchServicesHAProxyFrontendEndpointResponse424
    | PatchServicesHAProxyFrontendEndpointResponse500
    | PatchServicesHAProxyFrontendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendEndpointResponse400 | PatchServicesHAProxyFrontendEndpointResponse401 | PatchServicesHAProxyFrontendEndpointResponse403 | PatchServicesHAProxyFrontendEndpointResponse404 | PatchServicesHAProxyFrontendEndpointResponse405 | PatchServicesHAProxyFrontendEndpointResponse406 | PatchServicesHAProxyFrontendEndpointResponse409 | PatchServicesHAProxyFrontendEndpointResponse415 | PatchServicesHAProxyFrontendEndpointResponse422 | PatchServicesHAProxyFrontendEndpointResponse424 | PatchServicesHAProxyFrontendEndpointResponse500 | PatchServicesHAProxyFrontendEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendEndpointJsonBody | PatchServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFrontendEndpointResponse400
    | PatchServicesHAProxyFrontendEndpointResponse401
    | PatchServicesHAProxyFrontendEndpointResponse403
    | PatchServicesHAProxyFrontendEndpointResponse404
    | PatchServicesHAProxyFrontendEndpointResponse405
    | PatchServicesHAProxyFrontendEndpointResponse406
    | PatchServicesHAProxyFrontendEndpointResponse409
    | PatchServicesHAProxyFrontendEndpointResponse415
    | PatchServicesHAProxyFrontendEndpointResponse422
    | PatchServicesHAProxyFrontendEndpointResponse424
    | PatchServicesHAProxyFrontendEndpointResponse500
    | PatchServicesHAProxyFrontendEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFrontendEndpointResponse400 | PatchServicesHAProxyFrontendEndpointResponse401 | PatchServicesHAProxyFrontendEndpointResponse403 | PatchServicesHAProxyFrontendEndpointResponse404 | PatchServicesHAProxyFrontendEndpointResponse405 | PatchServicesHAProxyFrontendEndpointResponse406 | PatchServicesHAProxyFrontendEndpointResponse409 | PatchServicesHAProxyFrontendEndpointResponse415 | PatchServicesHAProxyFrontendEndpointResponse422 | PatchServicesHAProxyFrontendEndpointResponse424 | PatchServicesHAProxyFrontendEndpointResponse500 | PatchServicesHAProxyFrontendEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFrontendEndpointJsonBody | PatchServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesHAProxyFrontendEndpointResponse400
    | PatchServicesHAProxyFrontendEndpointResponse401
    | PatchServicesHAProxyFrontendEndpointResponse403
    | PatchServicesHAProxyFrontendEndpointResponse404
    | PatchServicesHAProxyFrontendEndpointResponse405
    | PatchServicesHAProxyFrontendEndpointResponse406
    | PatchServicesHAProxyFrontendEndpointResponse409
    | PatchServicesHAProxyFrontendEndpointResponse415
    | PatchServicesHAProxyFrontendEndpointResponse422
    | PatchServicesHAProxyFrontendEndpointResponse424
    | PatchServicesHAProxyFrontendEndpointResponse500
    | PatchServicesHAProxyFrontendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFrontendEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFrontendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFrontendEndpointResponse400 | PatchServicesHAProxyFrontendEndpointResponse401 | PatchServicesHAProxyFrontendEndpointResponse403 | PatchServicesHAProxyFrontendEndpointResponse404 | PatchServicesHAProxyFrontendEndpointResponse405 | PatchServicesHAProxyFrontendEndpointResponse406 | PatchServicesHAProxyFrontendEndpointResponse409 | PatchServicesHAProxyFrontendEndpointResponse415 | PatchServicesHAProxyFrontendEndpointResponse422 | PatchServicesHAProxyFrontendEndpointResponse424 | PatchServicesHAProxyFrontendEndpointResponse500 | PatchServicesHAProxyFrontendEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
