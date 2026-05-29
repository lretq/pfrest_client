from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_bind_zone_endpoint_data_body import PatchServicesBINDZoneEndpointDataBody
from ...models.patch_services_bind_zone_endpoint_json_body import PatchServicesBINDZoneEndpointJsonBody
from ...models.patch_services_bind_zone_endpoint_response_400 import PatchServicesBINDZoneEndpointResponse400
from ...models.patch_services_bind_zone_endpoint_response_401 import PatchServicesBINDZoneEndpointResponse401
from ...models.patch_services_bind_zone_endpoint_response_403 import PatchServicesBINDZoneEndpointResponse403
from ...models.patch_services_bind_zone_endpoint_response_404 import PatchServicesBINDZoneEndpointResponse404
from ...models.patch_services_bind_zone_endpoint_response_405 import PatchServicesBINDZoneEndpointResponse405
from ...models.patch_services_bind_zone_endpoint_response_406 import PatchServicesBINDZoneEndpointResponse406
from ...models.patch_services_bind_zone_endpoint_response_409 import PatchServicesBINDZoneEndpointResponse409
from ...models.patch_services_bind_zone_endpoint_response_415 import PatchServicesBINDZoneEndpointResponse415
from ...models.patch_services_bind_zone_endpoint_response_422 import PatchServicesBINDZoneEndpointResponse422
from ...models.patch_services_bind_zone_endpoint_response_424 import PatchServicesBINDZoneEndpointResponse424
from ...models.patch_services_bind_zone_endpoint_response_500 import PatchServicesBINDZoneEndpointResponse500
from ...models.patch_services_bind_zone_endpoint_response_503 import PatchServicesBINDZoneEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesBINDZoneEndpointJsonBody | PatchServicesBINDZoneEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/bind/zone",
    }

    if isinstance(body, PatchServicesBINDZoneEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesBINDZoneEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesBINDZoneEndpointResponse400
    | PatchServicesBINDZoneEndpointResponse401
    | PatchServicesBINDZoneEndpointResponse403
    | PatchServicesBINDZoneEndpointResponse404
    | PatchServicesBINDZoneEndpointResponse405
    | PatchServicesBINDZoneEndpointResponse406
    | PatchServicesBINDZoneEndpointResponse409
    | PatchServicesBINDZoneEndpointResponse415
    | PatchServicesBINDZoneEndpointResponse422
    | PatchServicesBINDZoneEndpointResponse424
    | PatchServicesBINDZoneEndpointResponse500
    | PatchServicesBINDZoneEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesBINDZoneEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesBINDZoneEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesBINDZoneEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesBINDZoneEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesBINDZoneEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesBINDZoneEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesBINDZoneEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesBINDZoneEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesBINDZoneEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesBINDZoneEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesBINDZoneEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesBINDZoneEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesBINDZoneEndpointResponse400
    | PatchServicesBINDZoneEndpointResponse401
    | PatchServicesBINDZoneEndpointResponse403
    | PatchServicesBINDZoneEndpointResponse404
    | PatchServicesBINDZoneEndpointResponse405
    | PatchServicesBINDZoneEndpointResponse406
    | PatchServicesBINDZoneEndpointResponse409
    | PatchServicesBINDZoneEndpointResponse415
    | PatchServicesBINDZoneEndpointResponse422
    | PatchServicesBINDZoneEndpointResponse424
    | PatchServicesBINDZoneEndpointResponse500
    | PatchServicesBINDZoneEndpointResponse503
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
    body: PatchServicesBINDZoneEndpointJsonBody | PatchServicesBINDZoneEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesBINDZoneEndpointResponse400
    | PatchServicesBINDZoneEndpointResponse401
    | PatchServicesBINDZoneEndpointResponse403
    | PatchServicesBINDZoneEndpointResponse404
    | PatchServicesBINDZoneEndpointResponse405
    | PatchServicesBINDZoneEndpointResponse406
    | PatchServicesBINDZoneEndpointResponse409
    | PatchServicesBINDZoneEndpointResponse415
    | PatchServicesBINDZoneEndpointResponse422
    | PatchServicesBINDZoneEndpointResponse424
    | PatchServicesBINDZoneEndpointResponse500
    | PatchServicesBINDZoneEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing BIND Zone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDZone<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-zone-patch ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDZoneEndpointJsonBody | Unset):
        body (PatchServicesBINDZoneEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesBINDZoneEndpointResponse400 | PatchServicesBINDZoneEndpointResponse401 | PatchServicesBINDZoneEndpointResponse403 | PatchServicesBINDZoneEndpointResponse404 | PatchServicesBINDZoneEndpointResponse405 | PatchServicesBINDZoneEndpointResponse406 | PatchServicesBINDZoneEndpointResponse409 | PatchServicesBINDZoneEndpointResponse415 | PatchServicesBINDZoneEndpointResponse422 | PatchServicesBINDZoneEndpointResponse424 | PatchServicesBINDZoneEndpointResponse500 | PatchServicesBINDZoneEndpointResponse503]
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
    body: PatchServicesBINDZoneEndpointJsonBody | PatchServicesBINDZoneEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesBINDZoneEndpointResponse400
    | PatchServicesBINDZoneEndpointResponse401
    | PatchServicesBINDZoneEndpointResponse403
    | PatchServicesBINDZoneEndpointResponse404
    | PatchServicesBINDZoneEndpointResponse405
    | PatchServicesBINDZoneEndpointResponse406
    | PatchServicesBINDZoneEndpointResponse409
    | PatchServicesBINDZoneEndpointResponse415
    | PatchServicesBINDZoneEndpointResponse422
    | PatchServicesBINDZoneEndpointResponse424
    | PatchServicesBINDZoneEndpointResponse500
    | PatchServicesBINDZoneEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing BIND Zone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDZone<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-zone-patch ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDZoneEndpointJsonBody | Unset):
        body (PatchServicesBINDZoneEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesBINDZoneEndpointResponse400 | PatchServicesBINDZoneEndpointResponse401 | PatchServicesBINDZoneEndpointResponse403 | PatchServicesBINDZoneEndpointResponse404 | PatchServicesBINDZoneEndpointResponse405 | PatchServicesBINDZoneEndpointResponse406 | PatchServicesBINDZoneEndpointResponse409 | PatchServicesBINDZoneEndpointResponse415 | PatchServicesBINDZoneEndpointResponse422 | PatchServicesBINDZoneEndpointResponse424 | PatchServicesBINDZoneEndpointResponse500 | PatchServicesBINDZoneEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesBINDZoneEndpointJsonBody | PatchServicesBINDZoneEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesBINDZoneEndpointResponse400
    | PatchServicesBINDZoneEndpointResponse401
    | PatchServicesBINDZoneEndpointResponse403
    | PatchServicesBINDZoneEndpointResponse404
    | PatchServicesBINDZoneEndpointResponse405
    | PatchServicesBINDZoneEndpointResponse406
    | PatchServicesBINDZoneEndpointResponse409
    | PatchServicesBINDZoneEndpointResponse415
    | PatchServicesBINDZoneEndpointResponse422
    | PatchServicesBINDZoneEndpointResponse424
    | PatchServicesBINDZoneEndpointResponse500
    | PatchServicesBINDZoneEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing BIND Zone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDZone<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-zone-patch ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDZoneEndpointJsonBody | Unset):
        body (PatchServicesBINDZoneEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesBINDZoneEndpointResponse400 | PatchServicesBINDZoneEndpointResponse401 | PatchServicesBINDZoneEndpointResponse403 | PatchServicesBINDZoneEndpointResponse404 | PatchServicesBINDZoneEndpointResponse405 | PatchServicesBINDZoneEndpointResponse406 | PatchServicesBINDZoneEndpointResponse409 | PatchServicesBINDZoneEndpointResponse415 | PatchServicesBINDZoneEndpointResponse422 | PatchServicesBINDZoneEndpointResponse424 | PatchServicesBINDZoneEndpointResponse500 | PatchServicesBINDZoneEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesBINDZoneEndpointJsonBody | PatchServicesBINDZoneEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesBINDZoneEndpointResponse400
    | PatchServicesBINDZoneEndpointResponse401
    | PatchServicesBINDZoneEndpointResponse403
    | PatchServicesBINDZoneEndpointResponse404
    | PatchServicesBINDZoneEndpointResponse405
    | PatchServicesBINDZoneEndpointResponse406
    | PatchServicesBINDZoneEndpointResponse409
    | PatchServicesBINDZoneEndpointResponse415
    | PatchServicesBINDZoneEndpointResponse422
    | PatchServicesBINDZoneEndpointResponse424
    | PatchServicesBINDZoneEndpointResponse500
    | PatchServicesBINDZoneEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing BIND Zone.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDZone<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-bind-zone-patch ]<br>**Required packages**: [ pfSense-pkg-
    bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDZoneEndpointJsonBody | Unset):
        body (PatchServicesBINDZoneEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesBINDZoneEndpointResponse400 | PatchServicesBINDZoneEndpointResponse401 | PatchServicesBINDZoneEndpointResponse403 | PatchServicesBINDZoneEndpointResponse404 | PatchServicesBINDZoneEndpointResponse405 | PatchServicesBINDZoneEndpointResponse406 | PatchServicesBINDZoneEndpointResponse409 | PatchServicesBINDZoneEndpointResponse415 | PatchServicesBINDZoneEndpointResponse422 | PatchServicesBINDZoneEndpointResponse424 | PatchServicesBINDZoneEndpointResponse500 | PatchServicesBINDZoneEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
