from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_restapi_version_endpoint_data_body import PatchSystemRESTAPIVersionEndpointDataBody
from ...models.patch_system_restapi_version_endpoint_json_body import PatchSystemRESTAPIVersionEndpointJsonBody
from ...models.patch_system_restapi_version_endpoint_response_400 import PatchSystemRESTAPIVersionEndpointResponse400
from ...models.patch_system_restapi_version_endpoint_response_401 import PatchSystemRESTAPIVersionEndpointResponse401
from ...models.patch_system_restapi_version_endpoint_response_403 import PatchSystemRESTAPIVersionEndpointResponse403
from ...models.patch_system_restapi_version_endpoint_response_404 import PatchSystemRESTAPIVersionEndpointResponse404
from ...models.patch_system_restapi_version_endpoint_response_405 import PatchSystemRESTAPIVersionEndpointResponse405
from ...models.patch_system_restapi_version_endpoint_response_406 import PatchSystemRESTAPIVersionEndpointResponse406
from ...models.patch_system_restapi_version_endpoint_response_409 import PatchSystemRESTAPIVersionEndpointResponse409
from ...models.patch_system_restapi_version_endpoint_response_415 import PatchSystemRESTAPIVersionEndpointResponse415
from ...models.patch_system_restapi_version_endpoint_response_422 import PatchSystemRESTAPIVersionEndpointResponse422
from ...models.patch_system_restapi_version_endpoint_response_424 import PatchSystemRESTAPIVersionEndpointResponse424
from ...models.patch_system_restapi_version_endpoint_response_500 import PatchSystemRESTAPIVersionEndpointResponse500
from ...models.patch_system_restapi_version_endpoint_response_503 import PatchSystemRESTAPIVersionEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemRESTAPIVersionEndpointJsonBody | PatchSystemRESTAPIVersionEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/restapi/version",
    }

    if isinstance(body, PatchSystemRESTAPIVersionEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemRESTAPIVersionEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemRESTAPIVersionEndpointResponse400
    | PatchSystemRESTAPIVersionEndpointResponse401
    | PatchSystemRESTAPIVersionEndpointResponse403
    | PatchSystemRESTAPIVersionEndpointResponse404
    | PatchSystemRESTAPIVersionEndpointResponse405
    | PatchSystemRESTAPIVersionEndpointResponse406
    | PatchSystemRESTAPIVersionEndpointResponse409
    | PatchSystemRESTAPIVersionEndpointResponse415
    | PatchSystemRESTAPIVersionEndpointResponse422
    | PatchSystemRESTAPIVersionEndpointResponse424
    | PatchSystemRESTAPIVersionEndpointResponse500
    | PatchSystemRESTAPIVersionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemRESTAPIVersionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemRESTAPIVersionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemRESTAPIVersionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemRESTAPIVersionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemRESTAPIVersionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemRESTAPIVersionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemRESTAPIVersionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemRESTAPIVersionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemRESTAPIVersionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemRESTAPIVersionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemRESTAPIVersionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemRESTAPIVersionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemRESTAPIVersionEndpointResponse400
    | PatchSystemRESTAPIVersionEndpointResponse401
    | PatchSystemRESTAPIVersionEndpointResponse403
    | PatchSystemRESTAPIVersionEndpointResponse404
    | PatchSystemRESTAPIVersionEndpointResponse405
    | PatchSystemRESTAPIVersionEndpointResponse406
    | PatchSystemRESTAPIVersionEndpointResponse409
    | PatchSystemRESTAPIVersionEndpointResponse415
    | PatchSystemRESTAPIVersionEndpointResponse422
    | PatchSystemRESTAPIVersionEndpointResponse424
    | PatchSystemRESTAPIVersionEndpointResponse500
    | PatchSystemRESTAPIVersionEndpointResponse503
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
    body: PatchSystemRESTAPIVersionEndpointJsonBody | PatchSystemRESTAPIVersionEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemRESTAPIVersionEndpointResponse400
    | PatchSystemRESTAPIVersionEndpointResponse401
    | PatchSystemRESTAPIVersionEndpointResponse403
    | PatchSystemRESTAPIVersionEndpointResponse404
    | PatchSystemRESTAPIVersionEndpointResponse405
    | PatchSystemRESTAPIVersionEndpointResponse406
    | PatchSystemRESTAPIVersionEndpointResponse409
    | PatchSystemRESTAPIVersionEndpointResponse415
    | PatchSystemRESTAPIVersionEndpointResponse422
    | PatchSystemRESTAPIVersionEndpointResponse424
    | PatchSystemRESTAPIVersionEndpointResponse500
    | PatchSystemRESTAPIVersionEndpointResponse503
]:
    """<h3>Description:</h3>Updates current REST API Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-version-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    RESTAPIVersionReleasesCache

    Args:
        body (PatchSystemRESTAPIVersionEndpointJsonBody | Unset):
        body (PatchSystemRESTAPIVersionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemRESTAPIVersionEndpointResponse400 | PatchSystemRESTAPIVersionEndpointResponse401 | PatchSystemRESTAPIVersionEndpointResponse403 | PatchSystemRESTAPIVersionEndpointResponse404 | PatchSystemRESTAPIVersionEndpointResponse405 | PatchSystemRESTAPIVersionEndpointResponse406 | PatchSystemRESTAPIVersionEndpointResponse409 | PatchSystemRESTAPIVersionEndpointResponse415 | PatchSystemRESTAPIVersionEndpointResponse422 | PatchSystemRESTAPIVersionEndpointResponse424 | PatchSystemRESTAPIVersionEndpointResponse500 | PatchSystemRESTAPIVersionEndpointResponse503]
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
    body: PatchSystemRESTAPIVersionEndpointJsonBody | PatchSystemRESTAPIVersionEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemRESTAPIVersionEndpointResponse400
    | PatchSystemRESTAPIVersionEndpointResponse401
    | PatchSystemRESTAPIVersionEndpointResponse403
    | PatchSystemRESTAPIVersionEndpointResponse404
    | PatchSystemRESTAPIVersionEndpointResponse405
    | PatchSystemRESTAPIVersionEndpointResponse406
    | PatchSystemRESTAPIVersionEndpointResponse409
    | PatchSystemRESTAPIVersionEndpointResponse415
    | PatchSystemRESTAPIVersionEndpointResponse422
    | PatchSystemRESTAPIVersionEndpointResponse424
    | PatchSystemRESTAPIVersionEndpointResponse500
    | PatchSystemRESTAPIVersionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current REST API Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-version-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    RESTAPIVersionReleasesCache

    Args:
        body (PatchSystemRESTAPIVersionEndpointJsonBody | Unset):
        body (PatchSystemRESTAPIVersionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemRESTAPIVersionEndpointResponse400 | PatchSystemRESTAPIVersionEndpointResponse401 | PatchSystemRESTAPIVersionEndpointResponse403 | PatchSystemRESTAPIVersionEndpointResponse404 | PatchSystemRESTAPIVersionEndpointResponse405 | PatchSystemRESTAPIVersionEndpointResponse406 | PatchSystemRESTAPIVersionEndpointResponse409 | PatchSystemRESTAPIVersionEndpointResponse415 | PatchSystemRESTAPIVersionEndpointResponse422 | PatchSystemRESTAPIVersionEndpointResponse424 | PatchSystemRESTAPIVersionEndpointResponse500 | PatchSystemRESTAPIVersionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemRESTAPIVersionEndpointJsonBody | PatchSystemRESTAPIVersionEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemRESTAPIVersionEndpointResponse400
    | PatchSystemRESTAPIVersionEndpointResponse401
    | PatchSystemRESTAPIVersionEndpointResponse403
    | PatchSystemRESTAPIVersionEndpointResponse404
    | PatchSystemRESTAPIVersionEndpointResponse405
    | PatchSystemRESTAPIVersionEndpointResponse406
    | PatchSystemRESTAPIVersionEndpointResponse409
    | PatchSystemRESTAPIVersionEndpointResponse415
    | PatchSystemRESTAPIVersionEndpointResponse422
    | PatchSystemRESTAPIVersionEndpointResponse424
    | PatchSystemRESTAPIVersionEndpointResponse500
    | PatchSystemRESTAPIVersionEndpointResponse503
]:
    """<h3>Description:</h3>Updates current REST API Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-version-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    RESTAPIVersionReleasesCache

    Args:
        body (PatchSystemRESTAPIVersionEndpointJsonBody | Unset):
        body (PatchSystemRESTAPIVersionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemRESTAPIVersionEndpointResponse400 | PatchSystemRESTAPIVersionEndpointResponse401 | PatchSystemRESTAPIVersionEndpointResponse403 | PatchSystemRESTAPIVersionEndpointResponse404 | PatchSystemRESTAPIVersionEndpointResponse405 | PatchSystemRESTAPIVersionEndpointResponse406 | PatchSystemRESTAPIVersionEndpointResponse409 | PatchSystemRESTAPIVersionEndpointResponse415 | PatchSystemRESTAPIVersionEndpointResponse422 | PatchSystemRESTAPIVersionEndpointResponse424 | PatchSystemRESTAPIVersionEndpointResponse500 | PatchSystemRESTAPIVersionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemRESTAPIVersionEndpointJsonBody | PatchSystemRESTAPIVersionEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemRESTAPIVersionEndpointResponse400
    | PatchSystemRESTAPIVersionEndpointResponse401
    | PatchSystemRESTAPIVersionEndpointResponse403
    | PatchSystemRESTAPIVersionEndpointResponse404
    | PatchSystemRESTAPIVersionEndpointResponse405
    | PatchSystemRESTAPIVersionEndpointResponse406
    | PatchSystemRESTAPIVersionEndpointResponse409
    | PatchSystemRESTAPIVersionEndpointResponse415
    | PatchSystemRESTAPIVersionEndpointResponse422
    | PatchSystemRESTAPIVersionEndpointResponse424
    | PatchSystemRESTAPIVersionEndpointResponse500
    | PatchSystemRESTAPIVersionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current REST API Version.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIVersion<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-version-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**:
    RESTAPIVersionReleasesCache

    Args:
        body (PatchSystemRESTAPIVersionEndpointJsonBody | Unset):
        body (PatchSystemRESTAPIVersionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemRESTAPIVersionEndpointResponse400 | PatchSystemRESTAPIVersionEndpointResponse401 | PatchSystemRESTAPIVersionEndpointResponse403 | PatchSystemRESTAPIVersionEndpointResponse404 | PatchSystemRESTAPIVersionEndpointResponse405 | PatchSystemRESTAPIVersionEndpointResponse406 | PatchSystemRESTAPIVersionEndpointResponse409 | PatchSystemRESTAPIVersionEndpointResponse415 | PatchSystemRESTAPIVersionEndpointResponse422 | PatchSystemRESTAPIVersionEndpointResponse424 | PatchSystemRESTAPIVersionEndpointResponse500 | PatchSystemRESTAPIVersionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
