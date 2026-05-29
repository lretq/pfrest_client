from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_free_radius_client_endpoint_data_body import PatchServicesFreeRADIUSClientEndpointDataBody
from ...models.patch_services_free_radius_client_endpoint_json_body import PatchServicesFreeRADIUSClientEndpointJsonBody
from ...models.patch_services_free_radius_client_endpoint_response_400 import (
    PatchServicesFreeRADIUSClientEndpointResponse400,
)
from ...models.patch_services_free_radius_client_endpoint_response_401 import (
    PatchServicesFreeRADIUSClientEndpointResponse401,
)
from ...models.patch_services_free_radius_client_endpoint_response_403 import (
    PatchServicesFreeRADIUSClientEndpointResponse403,
)
from ...models.patch_services_free_radius_client_endpoint_response_404 import (
    PatchServicesFreeRADIUSClientEndpointResponse404,
)
from ...models.patch_services_free_radius_client_endpoint_response_405 import (
    PatchServicesFreeRADIUSClientEndpointResponse405,
)
from ...models.patch_services_free_radius_client_endpoint_response_406 import (
    PatchServicesFreeRADIUSClientEndpointResponse406,
)
from ...models.patch_services_free_radius_client_endpoint_response_409 import (
    PatchServicesFreeRADIUSClientEndpointResponse409,
)
from ...models.patch_services_free_radius_client_endpoint_response_415 import (
    PatchServicesFreeRADIUSClientEndpointResponse415,
)
from ...models.patch_services_free_radius_client_endpoint_response_422 import (
    PatchServicesFreeRADIUSClientEndpointResponse422,
)
from ...models.patch_services_free_radius_client_endpoint_response_424 import (
    PatchServicesFreeRADIUSClientEndpointResponse424,
)
from ...models.patch_services_free_radius_client_endpoint_response_500 import (
    PatchServicesFreeRADIUSClientEndpointResponse500,
)
from ...models.patch_services_free_radius_client_endpoint_response_503 import (
    PatchServicesFreeRADIUSClientEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesFreeRADIUSClientEndpointJsonBody | PatchServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/freeradius/client",
    }

    if isinstance(body, PatchServicesFreeRADIUSClientEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesFreeRADIUSClientEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesFreeRADIUSClientEndpointResponse400
    | PatchServicesFreeRADIUSClientEndpointResponse401
    | PatchServicesFreeRADIUSClientEndpointResponse403
    | PatchServicesFreeRADIUSClientEndpointResponse404
    | PatchServicesFreeRADIUSClientEndpointResponse405
    | PatchServicesFreeRADIUSClientEndpointResponse406
    | PatchServicesFreeRADIUSClientEndpointResponse409
    | PatchServicesFreeRADIUSClientEndpointResponse415
    | PatchServicesFreeRADIUSClientEndpointResponse422
    | PatchServicesFreeRADIUSClientEndpointResponse424
    | PatchServicesFreeRADIUSClientEndpointResponse500
    | PatchServicesFreeRADIUSClientEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesFreeRADIUSClientEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesFreeRADIUSClientEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesFreeRADIUSClientEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesFreeRADIUSClientEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesFreeRADIUSClientEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesFreeRADIUSClientEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesFreeRADIUSClientEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesFreeRADIUSClientEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesFreeRADIUSClientEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesFreeRADIUSClientEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesFreeRADIUSClientEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesFreeRADIUSClientEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesFreeRADIUSClientEndpointResponse400
    | PatchServicesFreeRADIUSClientEndpointResponse401
    | PatchServicesFreeRADIUSClientEndpointResponse403
    | PatchServicesFreeRADIUSClientEndpointResponse404
    | PatchServicesFreeRADIUSClientEndpointResponse405
    | PatchServicesFreeRADIUSClientEndpointResponse406
    | PatchServicesFreeRADIUSClientEndpointResponse409
    | PatchServicesFreeRADIUSClientEndpointResponse415
    | PatchServicesFreeRADIUSClientEndpointResponse422
    | PatchServicesFreeRADIUSClientEndpointResponse424
    | PatchServicesFreeRADIUSClientEndpointResponse500
    | PatchServicesFreeRADIUSClientEndpointResponse503
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
    body: PatchServicesFreeRADIUSClientEndpointJsonBody | PatchServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesFreeRADIUSClientEndpointResponse400
    | PatchServicesFreeRADIUSClientEndpointResponse401
    | PatchServicesFreeRADIUSClientEndpointResponse403
    | PatchServicesFreeRADIUSClientEndpointResponse404
    | PatchServicesFreeRADIUSClientEndpointResponse405
    | PatchServicesFreeRADIUSClientEndpointResponse406
    | PatchServicesFreeRADIUSClientEndpointResponse409
    | PatchServicesFreeRADIUSClientEndpointResponse415
    | PatchServicesFreeRADIUSClientEndpointResponse422
    | PatchServicesFreeRADIUSClientEndpointResponse424
    | PatchServicesFreeRADIUSClientEndpointResponse500
    | PatchServicesFreeRADIUSClientEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing FreeRADIUS Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-client-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSClientEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesFreeRADIUSClientEndpointResponse400 | PatchServicesFreeRADIUSClientEndpointResponse401 | PatchServicesFreeRADIUSClientEndpointResponse403 | PatchServicesFreeRADIUSClientEndpointResponse404 | PatchServicesFreeRADIUSClientEndpointResponse405 | PatchServicesFreeRADIUSClientEndpointResponse406 | PatchServicesFreeRADIUSClientEndpointResponse409 | PatchServicesFreeRADIUSClientEndpointResponse415 | PatchServicesFreeRADIUSClientEndpointResponse422 | PatchServicesFreeRADIUSClientEndpointResponse424 | PatchServicesFreeRADIUSClientEndpointResponse500 | PatchServicesFreeRADIUSClientEndpointResponse503]
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
    body: PatchServicesFreeRADIUSClientEndpointJsonBody | PatchServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesFreeRADIUSClientEndpointResponse400
    | PatchServicesFreeRADIUSClientEndpointResponse401
    | PatchServicesFreeRADIUSClientEndpointResponse403
    | PatchServicesFreeRADIUSClientEndpointResponse404
    | PatchServicesFreeRADIUSClientEndpointResponse405
    | PatchServicesFreeRADIUSClientEndpointResponse406
    | PatchServicesFreeRADIUSClientEndpointResponse409
    | PatchServicesFreeRADIUSClientEndpointResponse415
    | PatchServicesFreeRADIUSClientEndpointResponse422
    | PatchServicesFreeRADIUSClientEndpointResponse424
    | PatchServicesFreeRADIUSClientEndpointResponse500
    | PatchServicesFreeRADIUSClientEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing FreeRADIUS Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-client-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSClientEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesFreeRADIUSClientEndpointResponse400 | PatchServicesFreeRADIUSClientEndpointResponse401 | PatchServicesFreeRADIUSClientEndpointResponse403 | PatchServicesFreeRADIUSClientEndpointResponse404 | PatchServicesFreeRADIUSClientEndpointResponse405 | PatchServicesFreeRADIUSClientEndpointResponse406 | PatchServicesFreeRADIUSClientEndpointResponse409 | PatchServicesFreeRADIUSClientEndpointResponse415 | PatchServicesFreeRADIUSClientEndpointResponse422 | PatchServicesFreeRADIUSClientEndpointResponse424 | PatchServicesFreeRADIUSClientEndpointResponse500 | PatchServicesFreeRADIUSClientEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesFreeRADIUSClientEndpointJsonBody | PatchServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesFreeRADIUSClientEndpointResponse400
    | PatchServicesFreeRADIUSClientEndpointResponse401
    | PatchServicesFreeRADIUSClientEndpointResponse403
    | PatchServicesFreeRADIUSClientEndpointResponse404
    | PatchServicesFreeRADIUSClientEndpointResponse405
    | PatchServicesFreeRADIUSClientEndpointResponse406
    | PatchServicesFreeRADIUSClientEndpointResponse409
    | PatchServicesFreeRADIUSClientEndpointResponse415
    | PatchServicesFreeRADIUSClientEndpointResponse422
    | PatchServicesFreeRADIUSClientEndpointResponse424
    | PatchServicesFreeRADIUSClientEndpointResponse500
    | PatchServicesFreeRADIUSClientEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing FreeRADIUS Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-client-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSClientEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesFreeRADIUSClientEndpointResponse400 | PatchServicesFreeRADIUSClientEndpointResponse401 | PatchServicesFreeRADIUSClientEndpointResponse403 | PatchServicesFreeRADIUSClientEndpointResponse404 | PatchServicesFreeRADIUSClientEndpointResponse405 | PatchServicesFreeRADIUSClientEndpointResponse406 | PatchServicesFreeRADIUSClientEndpointResponse409 | PatchServicesFreeRADIUSClientEndpointResponse415 | PatchServicesFreeRADIUSClientEndpointResponse422 | PatchServicesFreeRADIUSClientEndpointResponse424 | PatchServicesFreeRADIUSClientEndpointResponse500 | PatchServicesFreeRADIUSClientEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesFreeRADIUSClientEndpointJsonBody | PatchServicesFreeRADIUSClientEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesFreeRADIUSClientEndpointResponse400
    | PatchServicesFreeRADIUSClientEndpointResponse401
    | PatchServicesFreeRADIUSClientEndpointResponse403
    | PatchServicesFreeRADIUSClientEndpointResponse404
    | PatchServicesFreeRADIUSClientEndpointResponse405
    | PatchServicesFreeRADIUSClientEndpointResponse406
    | PatchServicesFreeRADIUSClientEndpointResponse409
    | PatchServicesFreeRADIUSClientEndpointResponse415
    | PatchServicesFreeRADIUSClientEndpointResponse422
    | PatchServicesFreeRADIUSClientEndpointResponse424
    | PatchServicesFreeRADIUSClientEndpointResponse500
    | PatchServicesFreeRADIUSClientEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing FreeRADIUS Client.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSClient<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-client-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSClientEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSClientEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesFreeRADIUSClientEndpointResponse400 | PatchServicesFreeRADIUSClientEndpointResponse401 | PatchServicesFreeRADIUSClientEndpointResponse403 | PatchServicesFreeRADIUSClientEndpointResponse404 | PatchServicesFreeRADIUSClientEndpointResponse405 | PatchServicesFreeRADIUSClientEndpointResponse406 | PatchServicesFreeRADIUSClientEndpointResponse409 | PatchServicesFreeRADIUSClientEndpointResponse415 | PatchServicesFreeRADIUSClientEndpointResponse422 | PatchServicesFreeRADIUSClientEndpointResponse424 | PatchServicesFreeRADIUSClientEndpointResponse500 | PatchServicesFreeRADIUSClientEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
