from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_service_watchdog_endpoint_data_body import PatchServicesServiceWatchdogEndpointDataBody
from ...models.patch_services_service_watchdog_endpoint_json_body import PatchServicesServiceWatchdogEndpointJsonBody
from ...models.patch_services_service_watchdog_endpoint_response_400 import (
    PatchServicesServiceWatchdogEndpointResponse400,
)
from ...models.patch_services_service_watchdog_endpoint_response_401 import (
    PatchServicesServiceWatchdogEndpointResponse401,
)
from ...models.patch_services_service_watchdog_endpoint_response_403 import (
    PatchServicesServiceWatchdogEndpointResponse403,
)
from ...models.patch_services_service_watchdog_endpoint_response_404 import (
    PatchServicesServiceWatchdogEndpointResponse404,
)
from ...models.patch_services_service_watchdog_endpoint_response_405 import (
    PatchServicesServiceWatchdogEndpointResponse405,
)
from ...models.patch_services_service_watchdog_endpoint_response_406 import (
    PatchServicesServiceWatchdogEndpointResponse406,
)
from ...models.patch_services_service_watchdog_endpoint_response_409 import (
    PatchServicesServiceWatchdogEndpointResponse409,
)
from ...models.patch_services_service_watchdog_endpoint_response_415 import (
    PatchServicesServiceWatchdogEndpointResponse415,
)
from ...models.patch_services_service_watchdog_endpoint_response_422 import (
    PatchServicesServiceWatchdogEndpointResponse422,
)
from ...models.patch_services_service_watchdog_endpoint_response_424 import (
    PatchServicesServiceWatchdogEndpointResponse424,
)
from ...models.patch_services_service_watchdog_endpoint_response_500 import (
    PatchServicesServiceWatchdogEndpointResponse500,
)
from ...models.patch_services_service_watchdog_endpoint_response_503 import (
    PatchServicesServiceWatchdogEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesServiceWatchdogEndpointJsonBody | PatchServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/service_watchdog",
    }

    if isinstance(body, PatchServicesServiceWatchdogEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesServiceWatchdogEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesServiceWatchdogEndpointResponse400
    | PatchServicesServiceWatchdogEndpointResponse401
    | PatchServicesServiceWatchdogEndpointResponse403
    | PatchServicesServiceWatchdogEndpointResponse404
    | PatchServicesServiceWatchdogEndpointResponse405
    | PatchServicesServiceWatchdogEndpointResponse406
    | PatchServicesServiceWatchdogEndpointResponse409
    | PatchServicesServiceWatchdogEndpointResponse415
    | PatchServicesServiceWatchdogEndpointResponse422
    | PatchServicesServiceWatchdogEndpointResponse424
    | PatchServicesServiceWatchdogEndpointResponse500
    | PatchServicesServiceWatchdogEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesServiceWatchdogEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesServiceWatchdogEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesServiceWatchdogEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesServiceWatchdogEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesServiceWatchdogEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesServiceWatchdogEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesServiceWatchdogEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesServiceWatchdogEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesServiceWatchdogEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesServiceWatchdogEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesServiceWatchdogEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesServiceWatchdogEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesServiceWatchdogEndpointResponse400
    | PatchServicesServiceWatchdogEndpointResponse401
    | PatchServicesServiceWatchdogEndpointResponse403
    | PatchServicesServiceWatchdogEndpointResponse404
    | PatchServicesServiceWatchdogEndpointResponse405
    | PatchServicesServiceWatchdogEndpointResponse406
    | PatchServicesServiceWatchdogEndpointResponse409
    | PatchServicesServiceWatchdogEndpointResponse415
    | PatchServicesServiceWatchdogEndpointResponse422
    | PatchServicesServiceWatchdogEndpointResponse424
    | PatchServicesServiceWatchdogEndpointResponse500
    | PatchServicesServiceWatchdogEndpointResponse503
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
    body: PatchServicesServiceWatchdogEndpointJsonBody | PatchServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesServiceWatchdogEndpointResponse400
    | PatchServicesServiceWatchdogEndpointResponse401
    | PatchServicesServiceWatchdogEndpointResponse403
    | PatchServicesServiceWatchdogEndpointResponse404
    | PatchServicesServiceWatchdogEndpointResponse405
    | PatchServicesServiceWatchdogEndpointResponse406
    | PatchServicesServiceWatchdogEndpointResponse409
    | PatchServicesServiceWatchdogEndpointResponse415
    | PatchServicesServiceWatchdogEndpointResponse422
    | PatchServicesServiceWatchdogEndpointResponse424
    | PatchServicesServiceWatchdogEndpointResponse500
    | PatchServicesServiceWatchdogEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-patch ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesServiceWatchdogEndpointJsonBody | Unset):
        body (PatchServicesServiceWatchdogEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesServiceWatchdogEndpointResponse400 | PatchServicesServiceWatchdogEndpointResponse401 | PatchServicesServiceWatchdogEndpointResponse403 | PatchServicesServiceWatchdogEndpointResponse404 | PatchServicesServiceWatchdogEndpointResponse405 | PatchServicesServiceWatchdogEndpointResponse406 | PatchServicesServiceWatchdogEndpointResponse409 | PatchServicesServiceWatchdogEndpointResponse415 | PatchServicesServiceWatchdogEndpointResponse422 | PatchServicesServiceWatchdogEndpointResponse424 | PatchServicesServiceWatchdogEndpointResponse500 | PatchServicesServiceWatchdogEndpointResponse503]
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
    body: PatchServicesServiceWatchdogEndpointJsonBody | PatchServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesServiceWatchdogEndpointResponse400
    | PatchServicesServiceWatchdogEndpointResponse401
    | PatchServicesServiceWatchdogEndpointResponse403
    | PatchServicesServiceWatchdogEndpointResponse404
    | PatchServicesServiceWatchdogEndpointResponse405
    | PatchServicesServiceWatchdogEndpointResponse406
    | PatchServicesServiceWatchdogEndpointResponse409
    | PatchServicesServiceWatchdogEndpointResponse415
    | PatchServicesServiceWatchdogEndpointResponse422
    | PatchServicesServiceWatchdogEndpointResponse424
    | PatchServicesServiceWatchdogEndpointResponse500
    | PatchServicesServiceWatchdogEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-patch ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesServiceWatchdogEndpointJsonBody | Unset):
        body (PatchServicesServiceWatchdogEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesServiceWatchdogEndpointResponse400 | PatchServicesServiceWatchdogEndpointResponse401 | PatchServicesServiceWatchdogEndpointResponse403 | PatchServicesServiceWatchdogEndpointResponse404 | PatchServicesServiceWatchdogEndpointResponse405 | PatchServicesServiceWatchdogEndpointResponse406 | PatchServicesServiceWatchdogEndpointResponse409 | PatchServicesServiceWatchdogEndpointResponse415 | PatchServicesServiceWatchdogEndpointResponse422 | PatchServicesServiceWatchdogEndpointResponse424 | PatchServicesServiceWatchdogEndpointResponse500 | PatchServicesServiceWatchdogEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesServiceWatchdogEndpointJsonBody | PatchServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesServiceWatchdogEndpointResponse400
    | PatchServicesServiceWatchdogEndpointResponse401
    | PatchServicesServiceWatchdogEndpointResponse403
    | PatchServicesServiceWatchdogEndpointResponse404
    | PatchServicesServiceWatchdogEndpointResponse405
    | PatchServicesServiceWatchdogEndpointResponse406
    | PatchServicesServiceWatchdogEndpointResponse409
    | PatchServicesServiceWatchdogEndpointResponse415
    | PatchServicesServiceWatchdogEndpointResponse422
    | PatchServicesServiceWatchdogEndpointResponse424
    | PatchServicesServiceWatchdogEndpointResponse500
    | PatchServicesServiceWatchdogEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-patch ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesServiceWatchdogEndpointJsonBody | Unset):
        body (PatchServicesServiceWatchdogEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesServiceWatchdogEndpointResponse400 | PatchServicesServiceWatchdogEndpointResponse401 | PatchServicesServiceWatchdogEndpointResponse403 | PatchServicesServiceWatchdogEndpointResponse404 | PatchServicesServiceWatchdogEndpointResponse405 | PatchServicesServiceWatchdogEndpointResponse406 | PatchServicesServiceWatchdogEndpointResponse409 | PatchServicesServiceWatchdogEndpointResponse415 | PatchServicesServiceWatchdogEndpointResponse422 | PatchServicesServiceWatchdogEndpointResponse424 | PatchServicesServiceWatchdogEndpointResponse500 | PatchServicesServiceWatchdogEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesServiceWatchdogEndpointJsonBody | PatchServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesServiceWatchdogEndpointResponse400
    | PatchServicesServiceWatchdogEndpointResponse401
    | PatchServicesServiceWatchdogEndpointResponse403
    | PatchServicesServiceWatchdogEndpointResponse404
    | PatchServicesServiceWatchdogEndpointResponse405
    | PatchServicesServiceWatchdogEndpointResponse406
    | PatchServicesServiceWatchdogEndpointResponse409
    | PatchServicesServiceWatchdogEndpointResponse415
    | PatchServicesServiceWatchdogEndpointResponse422
    | PatchServicesServiceWatchdogEndpointResponse424
    | PatchServicesServiceWatchdogEndpointResponse500
    | PatchServicesServiceWatchdogEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-patch ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PatchServicesServiceWatchdogEndpointJsonBody | Unset):
        body (PatchServicesServiceWatchdogEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesServiceWatchdogEndpointResponse400 | PatchServicesServiceWatchdogEndpointResponse401 | PatchServicesServiceWatchdogEndpointResponse403 | PatchServicesServiceWatchdogEndpointResponse404 | PatchServicesServiceWatchdogEndpointResponse405 | PatchServicesServiceWatchdogEndpointResponse406 | PatchServicesServiceWatchdogEndpointResponse409 | PatchServicesServiceWatchdogEndpointResponse415 | PatchServicesServiceWatchdogEndpointResponse422 | PatchServicesServiceWatchdogEndpointResponse424 | PatchServicesServiceWatchdogEndpointResponse500 | PatchServicesServiceWatchdogEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
