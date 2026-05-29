from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_restapi_version_endpoint_response_400 import GetSystemRESTAPIVersionEndpointResponse400
from ...models.get_system_restapi_version_endpoint_response_401 import GetSystemRESTAPIVersionEndpointResponse401
from ...models.get_system_restapi_version_endpoint_response_403 import GetSystemRESTAPIVersionEndpointResponse403
from ...models.get_system_restapi_version_endpoint_response_404 import GetSystemRESTAPIVersionEndpointResponse404
from ...models.get_system_restapi_version_endpoint_response_405 import GetSystemRESTAPIVersionEndpointResponse405
from ...models.get_system_restapi_version_endpoint_response_406 import GetSystemRESTAPIVersionEndpointResponse406
from ...models.get_system_restapi_version_endpoint_response_409 import GetSystemRESTAPIVersionEndpointResponse409
from ...models.get_system_restapi_version_endpoint_response_415 import GetSystemRESTAPIVersionEndpointResponse415
from ...models.get_system_restapi_version_endpoint_response_422 import GetSystemRESTAPIVersionEndpointResponse422
from ...models.get_system_restapi_version_endpoint_response_424 import GetSystemRESTAPIVersionEndpointResponse424
from ...models.get_system_restapi_version_endpoint_response_500 import GetSystemRESTAPIVersionEndpointResponse500
from ...models.get_system_restapi_version_endpoint_response_503 import GetSystemRESTAPIVersionEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/system/restapi/version",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSystemRESTAPIVersionEndpointResponse400
    | GetSystemRESTAPIVersionEndpointResponse401
    | GetSystemRESTAPIVersionEndpointResponse403
    | GetSystemRESTAPIVersionEndpointResponse404
    | GetSystemRESTAPIVersionEndpointResponse405
    | GetSystemRESTAPIVersionEndpointResponse406
    | GetSystemRESTAPIVersionEndpointResponse409
    | GetSystemRESTAPIVersionEndpointResponse415
    | GetSystemRESTAPIVersionEndpointResponse422
    | GetSystemRESTAPIVersionEndpointResponse424
    | GetSystemRESTAPIVersionEndpointResponse500
    | GetSystemRESTAPIVersionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetSystemRESTAPIVersionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSystemRESTAPIVersionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetSystemRESTAPIVersionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSystemRESTAPIVersionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetSystemRESTAPIVersionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetSystemRESTAPIVersionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetSystemRESTAPIVersionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetSystemRESTAPIVersionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetSystemRESTAPIVersionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetSystemRESTAPIVersionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetSystemRESTAPIVersionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetSystemRESTAPIVersionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSystemRESTAPIVersionEndpointResponse400
    | GetSystemRESTAPIVersionEndpointResponse401
    | GetSystemRESTAPIVersionEndpointResponse403
    | GetSystemRESTAPIVersionEndpointResponse404
    | GetSystemRESTAPIVersionEndpointResponse405
    | GetSystemRESTAPIVersionEndpointResponse406
    | GetSystemRESTAPIVersionEndpointResponse409
    | GetSystemRESTAPIVersionEndpointResponse415
    | GetSystemRESTAPIVersionEndpointResponse422
    | GetSystemRESTAPIVersionEndpointResponse424
    | GetSystemRESTAPIVersionEndpointResponse500
    | GetSystemRESTAPIVersionEndpointResponse503
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
    GetSystemRESTAPIVersionEndpointResponse400
    | GetSystemRESTAPIVersionEndpointResponse401
    | GetSystemRESTAPIVersionEndpointResponse403
    | GetSystemRESTAPIVersionEndpointResponse404
    | GetSystemRESTAPIVersionEndpointResponse405
    | GetSystemRESTAPIVersionEndpointResponse406
    | GetSystemRESTAPIVersionEndpointResponse409
    | GetSystemRESTAPIVersionEndpointResponse415
    | GetSystemRESTAPIVersionEndpointResponse422
    | GetSystemRESTAPIVersionEndpointResponse424
    | GetSystemRESTAPIVersionEndpointResponse500
    | GetSystemRESTAPIVersionEndpointResponse503
]:
    """<h3>Description:</h3>Reads current REST API Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-version-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    RESTAPIVersionReleasesCache

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemRESTAPIVersionEndpointResponse400 | GetSystemRESTAPIVersionEndpointResponse401 | GetSystemRESTAPIVersionEndpointResponse403 | GetSystemRESTAPIVersionEndpointResponse404 | GetSystemRESTAPIVersionEndpointResponse405 | GetSystemRESTAPIVersionEndpointResponse406 | GetSystemRESTAPIVersionEndpointResponse409 | GetSystemRESTAPIVersionEndpointResponse415 | GetSystemRESTAPIVersionEndpointResponse422 | GetSystemRESTAPIVersionEndpointResponse424 | GetSystemRESTAPIVersionEndpointResponse500 | GetSystemRESTAPIVersionEndpointResponse503]
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
    GetSystemRESTAPIVersionEndpointResponse400
    | GetSystemRESTAPIVersionEndpointResponse401
    | GetSystemRESTAPIVersionEndpointResponse403
    | GetSystemRESTAPIVersionEndpointResponse404
    | GetSystemRESTAPIVersionEndpointResponse405
    | GetSystemRESTAPIVersionEndpointResponse406
    | GetSystemRESTAPIVersionEndpointResponse409
    | GetSystemRESTAPIVersionEndpointResponse415
    | GetSystemRESTAPIVersionEndpointResponse422
    | GetSystemRESTAPIVersionEndpointResponse424
    | GetSystemRESTAPIVersionEndpointResponse500
    | GetSystemRESTAPIVersionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current REST API Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-version-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    RESTAPIVersionReleasesCache

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemRESTAPIVersionEndpointResponse400 | GetSystemRESTAPIVersionEndpointResponse401 | GetSystemRESTAPIVersionEndpointResponse403 | GetSystemRESTAPIVersionEndpointResponse404 | GetSystemRESTAPIVersionEndpointResponse405 | GetSystemRESTAPIVersionEndpointResponse406 | GetSystemRESTAPIVersionEndpointResponse409 | GetSystemRESTAPIVersionEndpointResponse415 | GetSystemRESTAPIVersionEndpointResponse422 | GetSystemRESTAPIVersionEndpointResponse424 | GetSystemRESTAPIVersionEndpointResponse500 | GetSystemRESTAPIVersionEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetSystemRESTAPIVersionEndpointResponse400
    | GetSystemRESTAPIVersionEndpointResponse401
    | GetSystemRESTAPIVersionEndpointResponse403
    | GetSystemRESTAPIVersionEndpointResponse404
    | GetSystemRESTAPIVersionEndpointResponse405
    | GetSystemRESTAPIVersionEndpointResponse406
    | GetSystemRESTAPIVersionEndpointResponse409
    | GetSystemRESTAPIVersionEndpointResponse415
    | GetSystemRESTAPIVersionEndpointResponse422
    | GetSystemRESTAPIVersionEndpointResponse424
    | GetSystemRESTAPIVersionEndpointResponse500
    | GetSystemRESTAPIVersionEndpointResponse503
]:
    """<h3>Description:</h3>Reads current REST API Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-version-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    RESTAPIVersionReleasesCache

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemRESTAPIVersionEndpointResponse400 | GetSystemRESTAPIVersionEndpointResponse401 | GetSystemRESTAPIVersionEndpointResponse403 | GetSystemRESTAPIVersionEndpointResponse404 | GetSystemRESTAPIVersionEndpointResponse405 | GetSystemRESTAPIVersionEndpointResponse406 | GetSystemRESTAPIVersionEndpointResponse409 | GetSystemRESTAPIVersionEndpointResponse415 | GetSystemRESTAPIVersionEndpointResponse422 | GetSystemRESTAPIVersionEndpointResponse424 | GetSystemRESTAPIVersionEndpointResponse500 | GetSystemRESTAPIVersionEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetSystemRESTAPIVersionEndpointResponse400
    | GetSystemRESTAPIVersionEndpointResponse401
    | GetSystemRESTAPIVersionEndpointResponse403
    | GetSystemRESTAPIVersionEndpointResponse404
    | GetSystemRESTAPIVersionEndpointResponse405
    | GetSystemRESTAPIVersionEndpointResponse406
    | GetSystemRESTAPIVersionEndpointResponse409
    | GetSystemRESTAPIVersionEndpointResponse415
    | GetSystemRESTAPIVersionEndpointResponse422
    | GetSystemRESTAPIVersionEndpointResponse424
    | GetSystemRESTAPIVersionEndpointResponse500
    | GetSystemRESTAPIVersionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current REST API Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-version-get ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    RESTAPIVersionReleasesCache

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemRESTAPIVersionEndpointResponse400 | GetSystemRESTAPIVersionEndpointResponse401 | GetSystemRESTAPIVersionEndpointResponse403 | GetSystemRESTAPIVersionEndpointResponse404 | GetSystemRESTAPIVersionEndpointResponse405 | GetSystemRESTAPIVersionEndpointResponse406 | GetSystemRESTAPIVersionEndpointResponse409 | GetSystemRESTAPIVersionEndpointResponse415 | GetSystemRESTAPIVersionEndpointResponse422 | GetSystemRESTAPIVersionEndpointResponse424 | GetSystemRESTAPIVersionEndpointResponse500 | GetSystemRESTAPIVersionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
