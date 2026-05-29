from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ha_proxy_file_endpoint_data_body import PatchServicesHAProxyFileEndpointDataBody
from ...models.patch_services_ha_proxy_file_endpoint_json_body import PatchServicesHAProxyFileEndpointJsonBody
from ...models.patch_services_ha_proxy_file_endpoint_response_400 import PatchServicesHAProxyFileEndpointResponse400
from ...models.patch_services_ha_proxy_file_endpoint_response_401 import PatchServicesHAProxyFileEndpointResponse401
from ...models.patch_services_ha_proxy_file_endpoint_response_403 import PatchServicesHAProxyFileEndpointResponse403
from ...models.patch_services_ha_proxy_file_endpoint_response_404 import PatchServicesHAProxyFileEndpointResponse404
from ...models.patch_services_ha_proxy_file_endpoint_response_405 import PatchServicesHAProxyFileEndpointResponse405
from ...models.patch_services_ha_proxy_file_endpoint_response_406 import PatchServicesHAProxyFileEndpointResponse406
from ...models.patch_services_ha_proxy_file_endpoint_response_409 import PatchServicesHAProxyFileEndpointResponse409
from ...models.patch_services_ha_proxy_file_endpoint_response_415 import PatchServicesHAProxyFileEndpointResponse415
from ...models.patch_services_ha_proxy_file_endpoint_response_422 import PatchServicesHAProxyFileEndpointResponse422
from ...models.patch_services_ha_proxy_file_endpoint_response_424 import PatchServicesHAProxyFileEndpointResponse424
from ...models.patch_services_ha_proxy_file_endpoint_response_500 import PatchServicesHAProxyFileEndpointResponse500
from ...models.patch_services_ha_proxy_file_endpoint_response_503 import PatchServicesHAProxyFileEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesHAProxyFileEndpointJsonBody | PatchServicesHAProxyFileEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/haproxy/file",
    }

    if isinstance(body, PatchServicesHAProxyFileEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesHAProxyFileEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesHAProxyFileEndpointResponse400
    | PatchServicesHAProxyFileEndpointResponse401
    | PatchServicesHAProxyFileEndpointResponse403
    | PatchServicesHAProxyFileEndpointResponse404
    | PatchServicesHAProxyFileEndpointResponse405
    | PatchServicesHAProxyFileEndpointResponse406
    | PatchServicesHAProxyFileEndpointResponse409
    | PatchServicesHAProxyFileEndpointResponse415
    | PatchServicesHAProxyFileEndpointResponse422
    | PatchServicesHAProxyFileEndpointResponse424
    | PatchServicesHAProxyFileEndpointResponse500
    | PatchServicesHAProxyFileEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesHAProxyFileEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesHAProxyFileEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesHAProxyFileEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesHAProxyFileEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesHAProxyFileEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesHAProxyFileEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesHAProxyFileEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesHAProxyFileEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesHAProxyFileEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesHAProxyFileEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesHAProxyFileEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesHAProxyFileEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesHAProxyFileEndpointResponse400
    | PatchServicesHAProxyFileEndpointResponse401
    | PatchServicesHAProxyFileEndpointResponse403
    | PatchServicesHAProxyFileEndpointResponse404
    | PatchServicesHAProxyFileEndpointResponse405
    | PatchServicesHAProxyFileEndpointResponse406
    | PatchServicesHAProxyFileEndpointResponse409
    | PatchServicesHAProxyFileEndpointResponse415
    | PatchServicesHAProxyFileEndpointResponse422
    | PatchServicesHAProxyFileEndpointResponse424
    | PatchServicesHAProxyFileEndpointResponse500
    | PatchServicesHAProxyFileEndpointResponse503
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
    body: PatchServicesHAProxyFileEndpointJsonBody | PatchServicesHAProxyFileEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFileEndpointResponse400
    | PatchServicesHAProxyFileEndpointResponse401
    | PatchServicesHAProxyFileEndpointResponse403
    | PatchServicesHAProxyFileEndpointResponse404
    | PatchServicesHAProxyFileEndpointResponse405
    | PatchServicesHAProxyFileEndpointResponse406
    | PatchServicesHAProxyFileEndpointResponse409
    | PatchServicesHAProxyFileEndpointResponse415
    | PatchServicesHAProxyFileEndpointResponse422
    | PatchServicesHAProxyFileEndpointResponse424
    | PatchServicesHAProxyFileEndpointResponse500
    | PatchServicesHAProxyFileEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy File.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-file-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFileEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFileEndpointResponse400 | PatchServicesHAProxyFileEndpointResponse401 | PatchServicesHAProxyFileEndpointResponse403 | PatchServicesHAProxyFileEndpointResponse404 | PatchServicesHAProxyFileEndpointResponse405 | PatchServicesHAProxyFileEndpointResponse406 | PatchServicesHAProxyFileEndpointResponse409 | PatchServicesHAProxyFileEndpointResponse415 | PatchServicesHAProxyFileEndpointResponse422 | PatchServicesHAProxyFileEndpointResponse424 | PatchServicesHAProxyFileEndpointResponse500 | PatchServicesHAProxyFileEndpointResponse503]
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
    body: PatchServicesHAProxyFileEndpointJsonBody | PatchServicesHAProxyFileEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesHAProxyFileEndpointResponse400
    | PatchServicesHAProxyFileEndpointResponse401
    | PatchServicesHAProxyFileEndpointResponse403
    | PatchServicesHAProxyFileEndpointResponse404
    | PatchServicesHAProxyFileEndpointResponse405
    | PatchServicesHAProxyFileEndpointResponse406
    | PatchServicesHAProxyFileEndpointResponse409
    | PatchServicesHAProxyFileEndpointResponse415
    | PatchServicesHAProxyFileEndpointResponse422
    | PatchServicesHAProxyFileEndpointResponse424
    | PatchServicesHAProxyFileEndpointResponse500
    | PatchServicesHAProxyFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy File.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-file-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFileEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFileEndpointResponse400 | PatchServicesHAProxyFileEndpointResponse401 | PatchServicesHAProxyFileEndpointResponse403 | PatchServicesHAProxyFileEndpointResponse404 | PatchServicesHAProxyFileEndpointResponse405 | PatchServicesHAProxyFileEndpointResponse406 | PatchServicesHAProxyFileEndpointResponse409 | PatchServicesHAProxyFileEndpointResponse415 | PatchServicesHAProxyFileEndpointResponse422 | PatchServicesHAProxyFileEndpointResponse424 | PatchServicesHAProxyFileEndpointResponse500 | PatchServicesHAProxyFileEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFileEndpointJsonBody | PatchServicesHAProxyFileEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesHAProxyFileEndpointResponse400
    | PatchServicesHAProxyFileEndpointResponse401
    | PatchServicesHAProxyFileEndpointResponse403
    | PatchServicesHAProxyFileEndpointResponse404
    | PatchServicesHAProxyFileEndpointResponse405
    | PatchServicesHAProxyFileEndpointResponse406
    | PatchServicesHAProxyFileEndpointResponse409
    | PatchServicesHAProxyFileEndpointResponse415
    | PatchServicesHAProxyFileEndpointResponse422
    | PatchServicesHAProxyFileEndpointResponse424
    | PatchServicesHAProxyFileEndpointResponse500
    | PatchServicesHAProxyFileEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing HAProxy File.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-file-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFileEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesHAProxyFileEndpointResponse400 | PatchServicesHAProxyFileEndpointResponse401 | PatchServicesHAProxyFileEndpointResponse403 | PatchServicesHAProxyFileEndpointResponse404 | PatchServicesHAProxyFileEndpointResponse405 | PatchServicesHAProxyFileEndpointResponse406 | PatchServicesHAProxyFileEndpointResponse409 | PatchServicesHAProxyFileEndpointResponse415 | PatchServicesHAProxyFileEndpointResponse422 | PatchServicesHAProxyFileEndpointResponse424 | PatchServicesHAProxyFileEndpointResponse500 | PatchServicesHAProxyFileEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesHAProxyFileEndpointJsonBody | PatchServicesHAProxyFileEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesHAProxyFileEndpointResponse400
    | PatchServicesHAProxyFileEndpointResponse401
    | PatchServicesHAProxyFileEndpointResponse403
    | PatchServicesHAProxyFileEndpointResponse404
    | PatchServicesHAProxyFileEndpointResponse405
    | PatchServicesHAProxyFileEndpointResponse406
    | PatchServicesHAProxyFileEndpointResponse409
    | PatchServicesHAProxyFileEndpointResponse415
    | PatchServicesHAProxyFileEndpointResponse422
    | PatchServicesHAProxyFileEndpointResponse424
    | PatchServicesHAProxyFileEndpointResponse500
    | PatchServicesHAProxyFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing HAProxy File.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFile<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-file-patch ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PatchServicesHAProxyFileEndpointJsonBody | Unset):
        body (PatchServicesHAProxyFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesHAProxyFileEndpointResponse400 | PatchServicesHAProxyFileEndpointResponse401 | PatchServicesHAProxyFileEndpointResponse403 | PatchServicesHAProxyFileEndpointResponse404 | PatchServicesHAProxyFileEndpointResponse405 | PatchServicesHAProxyFileEndpointResponse406 | PatchServicesHAProxyFileEndpointResponse409 | PatchServicesHAProxyFileEndpointResponse415 | PatchServicesHAProxyFileEndpointResponse422 | PatchServicesHAProxyFileEndpointResponse424 | PatchServicesHAProxyFileEndpointResponse500 | PatchServicesHAProxyFileEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
