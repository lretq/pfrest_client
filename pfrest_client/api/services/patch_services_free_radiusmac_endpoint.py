from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_free_radiusmac_endpoint_data_body import PatchServicesFreeRADIUSMACEndpointDataBody
from ...models.patch_services_free_radiusmac_endpoint_json_body import PatchServicesFreeRADIUSMACEndpointJsonBody
from ...models.patch_services_free_radiusmac_endpoint_response_400 import PatchServicesFreeRADIUSMACEndpointResponse400
from ...models.patch_services_free_radiusmac_endpoint_response_401 import PatchServicesFreeRADIUSMACEndpointResponse401
from ...models.patch_services_free_radiusmac_endpoint_response_403 import PatchServicesFreeRADIUSMACEndpointResponse403
from ...models.patch_services_free_radiusmac_endpoint_response_404 import PatchServicesFreeRADIUSMACEndpointResponse404
from ...models.patch_services_free_radiusmac_endpoint_response_405 import PatchServicesFreeRADIUSMACEndpointResponse405
from ...models.patch_services_free_radiusmac_endpoint_response_406 import PatchServicesFreeRADIUSMACEndpointResponse406
from ...models.patch_services_free_radiusmac_endpoint_response_409 import PatchServicesFreeRADIUSMACEndpointResponse409
from ...models.patch_services_free_radiusmac_endpoint_response_415 import PatchServicesFreeRADIUSMACEndpointResponse415
from ...models.patch_services_free_radiusmac_endpoint_response_422 import PatchServicesFreeRADIUSMACEndpointResponse422
from ...models.patch_services_free_radiusmac_endpoint_response_424 import PatchServicesFreeRADIUSMACEndpointResponse424
from ...models.patch_services_free_radiusmac_endpoint_response_500 import PatchServicesFreeRADIUSMACEndpointResponse500
from ...models.patch_services_free_radiusmac_endpoint_response_503 import PatchServicesFreeRADIUSMACEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesFreeRADIUSMACEndpointJsonBody | PatchServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/freeradius/mac",
    }

    if isinstance(body, PatchServicesFreeRADIUSMACEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesFreeRADIUSMACEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesFreeRADIUSMACEndpointResponse400
    | PatchServicesFreeRADIUSMACEndpointResponse401
    | PatchServicesFreeRADIUSMACEndpointResponse403
    | PatchServicesFreeRADIUSMACEndpointResponse404
    | PatchServicesFreeRADIUSMACEndpointResponse405
    | PatchServicesFreeRADIUSMACEndpointResponse406
    | PatchServicesFreeRADIUSMACEndpointResponse409
    | PatchServicesFreeRADIUSMACEndpointResponse415
    | PatchServicesFreeRADIUSMACEndpointResponse422
    | PatchServicesFreeRADIUSMACEndpointResponse424
    | PatchServicesFreeRADIUSMACEndpointResponse500
    | PatchServicesFreeRADIUSMACEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesFreeRADIUSMACEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesFreeRADIUSMACEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesFreeRADIUSMACEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesFreeRADIUSMACEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesFreeRADIUSMACEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesFreeRADIUSMACEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesFreeRADIUSMACEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesFreeRADIUSMACEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesFreeRADIUSMACEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesFreeRADIUSMACEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesFreeRADIUSMACEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesFreeRADIUSMACEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesFreeRADIUSMACEndpointResponse400
    | PatchServicesFreeRADIUSMACEndpointResponse401
    | PatchServicesFreeRADIUSMACEndpointResponse403
    | PatchServicesFreeRADIUSMACEndpointResponse404
    | PatchServicesFreeRADIUSMACEndpointResponse405
    | PatchServicesFreeRADIUSMACEndpointResponse406
    | PatchServicesFreeRADIUSMACEndpointResponse409
    | PatchServicesFreeRADIUSMACEndpointResponse415
    | PatchServicesFreeRADIUSMACEndpointResponse422
    | PatchServicesFreeRADIUSMACEndpointResponse424
    | PatchServicesFreeRADIUSMACEndpointResponse500
    | PatchServicesFreeRADIUSMACEndpointResponse503
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
    body: PatchServicesFreeRADIUSMACEndpointJsonBody | PatchServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesFreeRADIUSMACEndpointResponse400
    | PatchServicesFreeRADIUSMACEndpointResponse401
    | PatchServicesFreeRADIUSMACEndpointResponse403
    | PatchServicesFreeRADIUSMACEndpointResponse404
    | PatchServicesFreeRADIUSMACEndpointResponse405
    | PatchServicesFreeRADIUSMACEndpointResponse406
    | PatchServicesFreeRADIUSMACEndpointResponse409
    | PatchServicesFreeRADIUSMACEndpointResponse415
    | PatchServicesFreeRADIUSMACEndpointResponse422
    | PatchServicesFreeRADIUSMACEndpointResponse424
    | PatchServicesFreeRADIUSMACEndpointResponse500
    | PatchServicesFreeRADIUSMACEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing FreeRADIUS MAC.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSMAC<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-mac-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSMACEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSMACEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesFreeRADIUSMACEndpointResponse400 | PatchServicesFreeRADIUSMACEndpointResponse401 | PatchServicesFreeRADIUSMACEndpointResponse403 | PatchServicesFreeRADIUSMACEndpointResponse404 | PatchServicesFreeRADIUSMACEndpointResponse405 | PatchServicesFreeRADIUSMACEndpointResponse406 | PatchServicesFreeRADIUSMACEndpointResponse409 | PatchServicesFreeRADIUSMACEndpointResponse415 | PatchServicesFreeRADIUSMACEndpointResponse422 | PatchServicesFreeRADIUSMACEndpointResponse424 | PatchServicesFreeRADIUSMACEndpointResponse500 | PatchServicesFreeRADIUSMACEndpointResponse503]
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
    body: PatchServicesFreeRADIUSMACEndpointJsonBody | PatchServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesFreeRADIUSMACEndpointResponse400
    | PatchServicesFreeRADIUSMACEndpointResponse401
    | PatchServicesFreeRADIUSMACEndpointResponse403
    | PatchServicesFreeRADIUSMACEndpointResponse404
    | PatchServicesFreeRADIUSMACEndpointResponse405
    | PatchServicesFreeRADIUSMACEndpointResponse406
    | PatchServicesFreeRADIUSMACEndpointResponse409
    | PatchServicesFreeRADIUSMACEndpointResponse415
    | PatchServicesFreeRADIUSMACEndpointResponse422
    | PatchServicesFreeRADIUSMACEndpointResponse424
    | PatchServicesFreeRADIUSMACEndpointResponse500
    | PatchServicesFreeRADIUSMACEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing FreeRADIUS MAC.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSMAC<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-mac-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSMACEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSMACEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesFreeRADIUSMACEndpointResponse400 | PatchServicesFreeRADIUSMACEndpointResponse401 | PatchServicesFreeRADIUSMACEndpointResponse403 | PatchServicesFreeRADIUSMACEndpointResponse404 | PatchServicesFreeRADIUSMACEndpointResponse405 | PatchServicesFreeRADIUSMACEndpointResponse406 | PatchServicesFreeRADIUSMACEndpointResponse409 | PatchServicesFreeRADIUSMACEndpointResponse415 | PatchServicesFreeRADIUSMACEndpointResponse422 | PatchServicesFreeRADIUSMACEndpointResponse424 | PatchServicesFreeRADIUSMACEndpointResponse500 | PatchServicesFreeRADIUSMACEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesFreeRADIUSMACEndpointJsonBody | PatchServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesFreeRADIUSMACEndpointResponse400
    | PatchServicesFreeRADIUSMACEndpointResponse401
    | PatchServicesFreeRADIUSMACEndpointResponse403
    | PatchServicesFreeRADIUSMACEndpointResponse404
    | PatchServicesFreeRADIUSMACEndpointResponse405
    | PatchServicesFreeRADIUSMACEndpointResponse406
    | PatchServicesFreeRADIUSMACEndpointResponse409
    | PatchServicesFreeRADIUSMACEndpointResponse415
    | PatchServicesFreeRADIUSMACEndpointResponse422
    | PatchServicesFreeRADIUSMACEndpointResponse424
    | PatchServicesFreeRADIUSMACEndpointResponse500
    | PatchServicesFreeRADIUSMACEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing FreeRADIUS MAC.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSMAC<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-mac-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSMACEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSMACEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesFreeRADIUSMACEndpointResponse400 | PatchServicesFreeRADIUSMACEndpointResponse401 | PatchServicesFreeRADIUSMACEndpointResponse403 | PatchServicesFreeRADIUSMACEndpointResponse404 | PatchServicesFreeRADIUSMACEndpointResponse405 | PatchServicesFreeRADIUSMACEndpointResponse406 | PatchServicesFreeRADIUSMACEndpointResponse409 | PatchServicesFreeRADIUSMACEndpointResponse415 | PatchServicesFreeRADIUSMACEndpointResponse422 | PatchServicesFreeRADIUSMACEndpointResponse424 | PatchServicesFreeRADIUSMACEndpointResponse500 | PatchServicesFreeRADIUSMACEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesFreeRADIUSMACEndpointJsonBody | PatchServicesFreeRADIUSMACEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesFreeRADIUSMACEndpointResponse400
    | PatchServicesFreeRADIUSMACEndpointResponse401
    | PatchServicesFreeRADIUSMACEndpointResponse403
    | PatchServicesFreeRADIUSMACEndpointResponse404
    | PatchServicesFreeRADIUSMACEndpointResponse405
    | PatchServicesFreeRADIUSMACEndpointResponse406
    | PatchServicesFreeRADIUSMACEndpointResponse409
    | PatchServicesFreeRADIUSMACEndpointResponse415
    | PatchServicesFreeRADIUSMACEndpointResponse422
    | PatchServicesFreeRADIUSMACEndpointResponse424
    | PatchServicesFreeRADIUSMACEndpointResponse500
    | PatchServicesFreeRADIUSMACEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing FreeRADIUS MAC.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSMAC<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-mac-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSMACEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSMACEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesFreeRADIUSMACEndpointResponse400 | PatchServicesFreeRADIUSMACEndpointResponse401 | PatchServicesFreeRADIUSMACEndpointResponse403 | PatchServicesFreeRADIUSMACEndpointResponse404 | PatchServicesFreeRADIUSMACEndpointResponse405 | PatchServicesFreeRADIUSMACEndpointResponse406 | PatchServicesFreeRADIUSMACEndpointResponse409 | PatchServicesFreeRADIUSMACEndpointResponse415 | PatchServicesFreeRADIUSMACEndpointResponse422 | PatchServicesFreeRADIUSMACEndpointResponse424 | PatchServicesFreeRADIUSMACEndpointResponse500 | PatchServicesFreeRADIUSMACEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
