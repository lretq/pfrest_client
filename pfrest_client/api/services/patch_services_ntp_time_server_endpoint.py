from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ntp_time_server_endpoint_data_body import PatchServicesNTPTimeServerEndpointDataBody
from ...models.patch_services_ntp_time_server_endpoint_json_body import PatchServicesNTPTimeServerEndpointJsonBody
from ...models.patch_services_ntp_time_server_endpoint_response_400 import PatchServicesNTPTimeServerEndpointResponse400
from ...models.patch_services_ntp_time_server_endpoint_response_401 import PatchServicesNTPTimeServerEndpointResponse401
from ...models.patch_services_ntp_time_server_endpoint_response_403 import PatchServicesNTPTimeServerEndpointResponse403
from ...models.patch_services_ntp_time_server_endpoint_response_404 import PatchServicesNTPTimeServerEndpointResponse404
from ...models.patch_services_ntp_time_server_endpoint_response_405 import PatchServicesNTPTimeServerEndpointResponse405
from ...models.patch_services_ntp_time_server_endpoint_response_406 import PatchServicesNTPTimeServerEndpointResponse406
from ...models.patch_services_ntp_time_server_endpoint_response_409 import PatchServicesNTPTimeServerEndpointResponse409
from ...models.patch_services_ntp_time_server_endpoint_response_415 import PatchServicesNTPTimeServerEndpointResponse415
from ...models.patch_services_ntp_time_server_endpoint_response_422 import PatchServicesNTPTimeServerEndpointResponse422
from ...models.patch_services_ntp_time_server_endpoint_response_424 import PatchServicesNTPTimeServerEndpointResponse424
from ...models.patch_services_ntp_time_server_endpoint_response_500 import PatchServicesNTPTimeServerEndpointResponse500
from ...models.patch_services_ntp_time_server_endpoint_response_503 import PatchServicesNTPTimeServerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesNTPTimeServerEndpointJsonBody | PatchServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/ntp/time_server",
    }

    if isinstance(body, PatchServicesNTPTimeServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesNTPTimeServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesNTPTimeServerEndpointResponse400
    | PatchServicesNTPTimeServerEndpointResponse401
    | PatchServicesNTPTimeServerEndpointResponse403
    | PatchServicesNTPTimeServerEndpointResponse404
    | PatchServicesNTPTimeServerEndpointResponse405
    | PatchServicesNTPTimeServerEndpointResponse406
    | PatchServicesNTPTimeServerEndpointResponse409
    | PatchServicesNTPTimeServerEndpointResponse415
    | PatchServicesNTPTimeServerEndpointResponse422
    | PatchServicesNTPTimeServerEndpointResponse424
    | PatchServicesNTPTimeServerEndpointResponse500
    | PatchServicesNTPTimeServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesNTPTimeServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesNTPTimeServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesNTPTimeServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesNTPTimeServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesNTPTimeServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesNTPTimeServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesNTPTimeServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesNTPTimeServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesNTPTimeServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesNTPTimeServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesNTPTimeServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesNTPTimeServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesNTPTimeServerEndpointResponse400
    | PatchServicesNTPTimeServerEndpointResponse401
    | PatchServicesNTPTimeServerEndpointResponse403
    | PatchServicesNTPTimeServerEndpointResponse404
    | PatchServicesNTPTimeServerEndpointResponse405
    | PatchServicesNTPTimeServerEndpointResponse406
    | PatchServicesNTPTimeServerEndpointResponse409
    | PatchServicesNTPTimeServerEndpointResponse415
    | PatchServicesNTPTimeServerEndpointResponse422
    | PatchServicesNTPTimeServerEndpointResponse424
    | PatchServicesNTPTimeServerEndpointResponse500
    | PatchServicesNTPTimeServerEndpointResponse503
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
    body: PatchServicesNTPTimeServerEndpointJsonBody | PatchServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesNTPTimeServerEndpointResponse400
    | PatchServicesNTPTimeServerEndpointResponse401
    | PatchServicesNTPTimeServerEndpointResponse403
    | PatchServicesNTPTimeServerEndpointResponse404
    | PatchServicesNTPTimeServerEndpointResponse405
    | PatchServicesNTPTimeServerEndpointResponse406
    | PatchServicesNTPTimeServerEndpointResponse409
    | PatchServicesNTPTimeServerEndpointResponse415
    | PatchServicesNTPTimeServerEndpointResponse422
    | PatchServicesNTPTimeServerEndpointResponse424
    | PatchServicesNTPTimeServerEndpointResponse500
    | PatchServicesNTPTimeServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PatchServicesNTPTimeServerEndpointJsonBody | Unset):
        body (PatchServicesNTPTimeServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesNTPTimeServerEndpointResponse400 | PatchServicesNTPTimeServerEndpointResponse401 | PatchServicesNTPTimeServerEndpointResponse403 | PatchServicesNTPTimeServerEndpointResponse404 | PatchServicesNTPTimeServerEndpointResponse405 | PatchServicesNTPTimeServerEndpointResponse406 | PatchServicesNTPTimeServerEndpointResponse409 | PatchServicesNTPTimeServerEndpointResponse415 | PatchServicesNTPTimeServerEndpointResponse422 | PatchServicesNTPTimeServerEndpointResponse424 | PatchServicesNTPTimeServerEndpointResponse500 | PatchServicesNTPTimeServerEndpointResponse503]
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
    body: PatchServicesNTPTimeServerEndpointJsonBody | PatchServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesNTPTimeServerEndpointResponse400
    | PatchServicesNTPTimeServerEndpointResponse401
    | PatchServicesNTPTimeServerEndpointResponse403
    | PatchServicesNTPTimeServerEndpointResponse404
    | PatchServicesNTPTimeServerEndpointResponse405
    | PatchServicesNTPTimeServerEndpointResponse406
    | PatchServicesNTPTimeServerEndpointResponse409
    | PatchServicesNTPTimeServerEndpointResponse415
    | PatchServicesNTPTimeServerEndpointResponse422
    | PatchServicesNTPTimeServerEndpointResponse424
    | PatchServicesNTPTimeServerEndpointResponse500
    | PatchServicesNTPTimeServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PatchServicesNTPTimeServerEndpointJsonBody | Unset):
        body (PatchServicesNTPTimeServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesNTPTimeServerEndpointResponse400 | PatchServicesNTPTimeServerEndpointResponse401 | PatchServicesNTPTimeServerEndpointResponse403 | PatchServicesNTPTimeServerEndpointResponse404 | PatchServicesNTPTimeServerEndpointResponse405 | PatchServicesNTPTimeServerEndpointResponse406 | PatchServicesNTPTimeServerEndpointResponse409 | PatchServicesNTPTimeServerEndpointResponse415 | PatchServicesNTPTimeServerEndpointResponse422 | PatchServicesNTPTimeServerEndpointResponse424 | PatchServicesNTPTimeServerEndpointResponse500 | PatchServicesNTPTimeServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesNTPTimeServerEndpointJsonBody | PatchServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesNTPTimeServerEndpointResponse400
    | PatchServicesNTPTimeServerEndpointResponse401
    | PatchServicesNTPTimeServerEndpointResponse403
    | PatchServicesNTPTimeServerEndpointResponse404
    | PatchServicesNTPTimeServerEndpointResponse405
    | PatchServicesNTPTimeServerEndpointResponse406
    | PatchServicesNTPTimeServerEndpointResponse409
    | PatchServicesNTPTimeServerEndpointResponse415
    | PatchServicesNTPTimeServerEndpointResponse422
    | PatchServicesNTPTimeServerEndpointResponse424
    | PatchServicesNTPTimeServerEndpointResponse500
    | PatchServicesNTPTimeServerEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PatchServicesNTPTimeServerEndpointJsonBody | Unset):
        body (PatchServicesNTPTimeServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesNTPTimeServerEndpointResponse400 | PatchServicesNTPTimeServerEndpointResponse401 | PatchServicesNTPTimeServerEndpointResponse403 | PatchServicesNTPTimeServerEndpointResponse404 | PatchServicesNTPTimeServerEndpointResponse405 | PatchServicesNTPTimeServerEndpointResponse406 | PatchServicesNTPTimeServerEndpointResponse409 | PatchServicesNTPTimeServerEndpointResponse415 | PatchServicesNTPTimeServerEndpointResponse422 | PatchServicesNTPTimeServerEndpointResponse424 | PatchServicesNTPTimeServerEndpointResponse500 | PatchServicesNTPTimeServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesNTPTimeServerEndpointJsonBody | PatchServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesNTPTimeServerEndpointResponse400
    | PatchServicesNTPTimeServerEndpointResponse401
    | PatchServicesNTPTimeServerEndpointResponse403
    | PatchServicesNTPTimeServerEndpointResponse404
    | PatchServicesNTPTimeServerEndpointResponse405
    | PatchServicesNTPTimeServerEndpointResponse406
    | PatchServicesNTPTimeServerEndpointResponse409
    | PatchServicesNTPTimeServerEndpointResponse415
    | PatchServicesNTPTimeServerEndpointResponse422
    | PatchServicesNTPTimeServerEndpointResponse424
    | PatchServicesNTPTimeServerEndpointResponse500
    | PatchServicesNTPTimeServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-patch ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PatchServicesNTPTimeServerEndpointJsonBody | Unset):
        body (PatchServicesNTPTimeServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesNTPTimeServerEndpointResponse400 | PatchServicesNTPTimeServerEndpointResponse401 | PatchServicesNTPTimeServerEndpointResponse403 | PatchServicesNTPTimeServerEndpointResponse404 | PatchServicesNTPTimeServerEndpointResponse405 | PatchServicesNTPTimeServerEndpointResponse406 | PatchServicesNTPTimeServerEndpointResponse409 | PatchServicesNTPTimeServerEndpointResponse415 | PatchServicesNTPTimeServerEndpointResponse422 | PatchServicesNTPTimeServerEndpointResponse424 | PatchServicesNTPTimeServerEndpointResponse500 | PatchServicesNTPTimeServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
