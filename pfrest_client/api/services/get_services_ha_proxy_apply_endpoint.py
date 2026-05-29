from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_ha_proxy_apply_endpoint_response_400 import GetServicesHAProxyApplyEndpointResponse400
from ...models.get_services_ha_proxy_apply_endpoint_response_401 import GetServicesHAProxyApplyEndpointResponse401
from ...models.get_services_ha_proxy_apply_endpoint_response_403 import GetServicesHAProxyApplyEndpointResponse403
from ...models.get_services_ha_proxy_apply_endpoint_response_404 import GetServicesHAProxyApplyEndpointResponse404
from ...models.get_services_ha_proxy_apply_endpoint_response_405 import GetServicesHAProxyApplyEndpointResponse405
from ...models.get_services_ha_proxy_apply_endpoint_response_406 import GetServicesHAProxyApplyEndpointResponse406
from ...models.get_services_ha_proxy_apply_endpoint_response_409 import GetServicesHAProxyApplyEndpointResponse409
from ...models.get_services_ha_proxy_apply_endpoint_response_415 import GetServicesHAProxyApplyEndpointResponse415
from ...models.get_services_ha_proxy_apply_endpoint_response_422 import GetServicesHAProxyApplyEndpointResponse422
from ...models.get_services_ha_proxy_apply_endpoint_response_424 import GetServicesHAProxyApplyEndpointResponse424
from ...models.get_services_ha_proxy_apply_endpoint_response_500 import GetServicesHAProxyApplyEndpointResponse500
from ...models.get_services_ha_proxy_apply_endpoint_response_503 import GetServicesHAProxyApplyEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/haproxy/apply",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesHAProxyApplyEndpointResponse400
    | GetServicesHAProxyApplyEndpointResponse401
    | GetServicesHAProxyApplyEndpointResponse403
    | GetServicesHAProxyApplyEndpointResponse404
    | GetServicesHAProxyApplyEndpointResponse405
    | GetServicesHAProxyApplyEndpointResponse406
    | GetServicesHAProxyApplyEndpointResponse409
    | GetServicesHAProxyApplyEndpointResponse415
    | GetServicesHAProxyApplyEndpointResponse422
    | GetServicesHAProxyApplyEndpointResponse424
    | GetServicesHAProxyApplyEndpointResponse500
    | GetServicesHAProxyApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesHAProxyApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesHAProxyApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesHAProxyApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesHAProxyApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesHAProxyApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesHAProxyApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesHAProxyApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesHAProxyApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesHAProxyApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesHAProxyApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesHAProxyApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesHAProxyApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesHAProxyApplyEndpointResponse400
    | GetServicesHAProxyApplyEndpointResponse401
    | GetServicesHAProxyApplyEndpointResponse403
    | GetServicesHAProxyApplyEndpointResponse404
    | GetServicesHAProxyApplyEndpointResponse405
    | GetServicesHAProxyApplyEndpointResponse406
    | GetServicesHAProxyApplyEndpointResponse409
    | GetServicesHAProxyApplyEndpointResponse415
    | GetServicesHAProxyApplyEndpointResponse422
    | GetServicesHAProxyApplyEndpointResponse424
    | GetServicesHAProxyApplyEndpointResponse500
    | GetServicesHAProxyApplyEndpointResponse503
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
) -> Response[
    GetServicesHAProxyApplyEndpointResponse400
    | GetServicesHAProxyApplyEndpointResponse401
    | GetServicesHAProxyApplyEndpointResponse403
    | GetServicesHAProxyApplyEndpointResponse404
    | GetServicesHAProxyApplyEndpointResponse405
    | GetServicesHAProxyApplyEndpointResponse406
    | GetServicesHAProxyApplyEndpointResponse409
    | GetServicesHAProxyApplyEndpointResponse415
    | GetServicesHAProxyApplyEndpointResponse422
    | GetServicesHAProxyApplyEndpointResponse424
    | GetServicesHAProxyApplyEndpointResponse500
    | GetServicesHAProxyApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending HAProxy change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-apply-get ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyApplyEndpointResponse400 | GetServicesHAProxyApplyEndpointResponse401 | GetServicesHAProxyApplyEndpointResponse403 | GetServicesHAProxyApplyEndpointResponse404 | GetServicesHAProxyApplyEndpointResponse405 | GetServicesHAProxyApplyEndpointResponse406 | GetServicesHAProxyApplyEndpointResponse409 | GetServicesHAProxyApplyEndpointResponse415 | GetServicesHAProxyApplyEndpointResponse422 | GetServicesHAProxyApplyEndpointResponse424 | GetServicesHAProxyApplyEndpointResponse500 | GetServicesHAProxyApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesHAProxyApplyEndpointResponse400
    | GetServicesHAProxyApplyEndpointResponse401
    | GetServicesHAProxyApplyEndpointResponse403
    | GetServicesHAProxyApplyEndpointResponse404
    | GetServicesHAProxyApplyEndpointResponse405
    | GetServicesHAProxyApplyEndpointResponse406
    | GetServicesHAProxyApplyEndpointResponse409
    | GetServicesHAProxyApplyEndpointResponse415
    | GetServicesHAProxyApplyEndpointResponse422
    | GetServicesHAProxyApplyEndpointResponse424
    | GetServicesHAProxyApplyEndpointResponse500
    | GetServicesHAProxyApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending HAProxy change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-apply-get ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyApplyEndpointResponse400 | GetServicesHAProxyApplyEndpointResponse401 | GetServicesHAProxyApplyEndpointResponse403 | GetServicesHAProxyApplyEndpointResponse404 | GetServicesHAProxyApplyEndpointResponse405 | GetServicesHAProxyApplyEndpointResponse406 | GetServicesHAProxyApplyEndpointResponse409 | GetServicesHAProxyApplyEndpointResponse415 | GetServicesHAProxyApplyEndpointResponse422 | GetServicesHAProxyApplyEndpointResponse424 | GetServicesHAProxyApplyEndpointResponse500 | GetServicesHAProxyApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesHAProxyApplyEndpointResponse400
    | GetServicesHAProxyApplyEndpointResponse401
    | GetServicesHAProxyApplyEndpointResponse403
    | GetServicesHAProxyApplyEndpointResponse404
    | GetServicesHAProxyApplyEndpointResponse405
    | GetServicesHAProxyApplyEndpointResponse406
    | GetServicesHAProxyApplyEndpointResponse409
    | GetServicesHAProxyApplyEndpointResponse415
    | GetServicesHAProxyApplyEndpointResponse422
    | GetServicesHAProxyApplyEndpointResponse424
    | GetServicesHAProxyApplyEndpointResponse500
    | GetServicesHAProxyApplyEndpointResponse503
]:
    """<h3>Description:</h3>Read pending HAProxy change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-apply-get ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesHAProxyApplyEndpointResponse400 | GetServicesHAProxyApplyEndpointResponse401 | GetServicesHAProxyApplyEndpointResponse403 | GetServicesHAProxyApplyEndpointResponse404 | GetServicesHAProxyApplyEndpointResponse405 | GetServicesHAProxyApplyEndpointResponse406 | GetServicesHAProxyApplyEndpointResponse409 | GetServicesHAProxyApplyEndpointResponse415 | GetServicesHAProxyApplyEndpointResponse422 | GetServicesHAProxyApplyEndpointResponse424 | GetServicesHAProxyApplyEndpointResponse500 | GetServicesHAProxyApplyEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesHAProxyApplyEndpointResponse400
    | GetServicesHAProxyApplyEndpointResponse401
    | GetServicesHAProxyApplyEndpointResponse403
    | GetServicesHAProxyApplyEndpointResponse404
    | GetServicesHAProxyApplyEndpointResponse405
    | GetServicesHAProxyApplyEndpointResponse406
    | GetServicesHAProxyApplyEndpointResponse409
    | GetServicesHAProxyApplyEndpointResponse415
    | GetServicesHAProxyApplyEndpointResponse422
    | GetServicesHAProxyApplyEndpointResponse424
    | GetServicesHAProxyApplyEndpointResponse500
    | GetServicesHAProxyApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Read pending HAProxy change status.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-apply-get ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: Not Applicable<br>**Utilizes
    cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesHAProxyApplyEndpointResponse400 | GetServicesHAProxyApplyEndpointResponse401 | GetServicesHAProxyApplyEndpointResponse403 | GetServicesHAProxyApplyEndpointResponse404 | GetServicesHAProxyApplyEndpointResponse405 | GetServicesHAProxyApplyEndpointResponse406 | GetServicesHAProxyApplyEndpointResponse409 | GetServicesHAProxyApplyEndpointResponse415 | GetServicesHAProxyApplyEndpointResponse422 | GetServicesHAProxyApplyEndpointResponse424 | GetServicesHAProxyApplyEndpointResponse500 | GetServicesHAProxyApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
