from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_service_watchdog_endpoint_response_400 import (
    DeleteServicesServiceWatchdogEndpointResponse400,
)
from ...models.delete_services_service_watchdog_endpoint_response_401 import (
    DeleteServicesServiceWatchdogEndpointResponse401,
)
from ...models.delete_services_service_watchdog_endpoint_response_403 import (
    DeleteServicesServiceWatchdogEndpointResponse403,
)
from ...models.delete_services_service_watchdog_endpoint_response_404 import (
    DeleteServicesServiceWatchdogEndpointResponse404,
)
from ...models.delete_services_service_watchdog_endpoint_response_405 import (
    DeleteServicesServiceWatchdogEndpointResponse405,
)
from ...models.delete_services_service_watchdog_endpoint_response_406 import (
    DeleteServicesServiceWatchdogEndpointResponse406,
)
from ...models.delete_services_service_watchdog_endpoint_response_409 import (
    DeleteServicesServiceWatchdogEndpointResponse409,
)
from ...models.delete_services_service_watchdog_endpoint_response_415 import (
    DeleteServicesServiceWatchdogEndpointResponse415,
)
from ...models.delete_services_service_watchdog_endpoint_response_422 import (
    DeleteServicesServiceWatchdogEndpointResponse422,
)
from ...models.delete_services_service_watchdog_endpoint_response_424 import (
    DeleteServicesServiceWatchdogEndpointResponse424,
)
from ...models.delete_services_service_watchdog_endpoint_response_500 import (
    DeleteServicesServiceWatchdogEndpointResponse500,
)
from ...models.delete_services_service_watchdog_endpoint_response_503 import (
    DeleteServicesServiceWatchdogEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/service_watchdog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesServiceWatchdogEndpointResponse400
    | DeleteServicesServiceWatchdogEndpointResponse401
    | DeleteServicesServiceWatchdogEndpointResponse403
    | DeleteServicesServiceWatchdogEndpointResponse404
    | DeleteServicesServiceWatchdogEndpointResponse405
    | DeleteServicesServiceWatchdogEndpointResponse406
    | DeleteServicesServiceWatchdogEndpointResponse409
    | DeleteServicesServiceWatchdogEndpointResponse415
    | DeleteServicesServiceWatchdogEndpointResponse422
    | DeleteServicesServiceWatchdogEndpointResponse424
    | DeleteServicesServiceWatchdogEndpointResponse500
    | DeleteServicesServiceWatchdogEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesServiceWatchdogEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesServiceWatchdogEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesServiceWatchdogEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesServiceWatchdogEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesServiceWatchdogEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesServiceWatchdogEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesServiceWatchdogEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesServiceWatchdogEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesServiceWatchdogEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesServiceWatchdogEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesServiceWatchdogEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesServiceWatchdogEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesServiceWatchdogEndpointResponse400
    | DeleteServicesServiceWatchdogEndpointResponse401
    | DeleteServicesServiceWatchdogEndpointResponse403
    | DeleteServicesServiceWatchdogEndpointResponse404
    | DeleteServicesServiceWatchdogEndpointResponse405
    | DeleteServicesServiceWatchdogEndpointResponse406
    | DeleteServicesServiceWatchdogEndpointResponse409
    | DeleteServicesServiceWatchdogEndpointResponse415
    | DeleteServicesServiceWatchdogEndpointResponse422
    | DeleteServicesServiceWatchdogEndpointResponse424
    | DeleteServicesServiceWatchdogEndpointResponse500
    | DeleteServicesServiceWatchdogEndpointResponse503
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
    id: int | str,
) -> Response[
    DeleteServicesServiceWatchdogEndpointResponse400
    | DeleteServicesServiceWatchdogEndpointResponse401
    | DeleteServicesServiceWatchdogEndpointResponse403
    | DeleteServicesServiceWatchdogEndpointResponse404
    | DeleteServicesServiceWatchdogEndpointResponse405
    | DeleteServicesServiceWatchdogEndpointResponse406
    | DeleteServicesServiceWatchdogEndpointResponse409
    | DeleteServicesServiceWatchdogEndpointResponse415
    | DeleteServicesServiceWatchdogEndpointResponse422
    | DeleteServicesServiceWatchdogEndpointResponse424
    | DeleteServicesServiceWatchdogEndpointResponse500
    | DeleteServicesServiceWatchdogEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-delete ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesServiceWatchdogEndpointResponse400 | DeleteServicesServiceWatchdogEndpointResponse401 | DeleteServicesServiceWatchdogEndpointResponse403 | DeleteServicesServiceWatchdogEndpointResponse404 | DeleteServicesServiceWatchdogEndpointResponse405 | DeleteServicesServiceWatchdogEndpointResponse406 | DeleteServicesServiceWatchdogEndpointResponse409 | DeleteServicesServiceWatchdogEndpointResponse415 | DeleteServicesServiceWatchdogEndpointResponse422 | DeleteServicesServiceWatchdogEndpointResponse424 | DeleteServicesServiceWatchdogEndpointResponse500 | DeleteServicesServiceWatchdogEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesServiceWatchdogEndpointResponse400
    | DeleteServicesServiceWatchdogEndpointResponse401
    | DeleteServicesServiceWatchdogEndpointResponse403
    | DeleteServicesServiceWatchdogEndpointResponse404
    | DeleteServicesServiceWatchdogEndpointResponse405
    | DeleteServicesServiceWatchdogEndpointResponse406
    | DeleteServicesServiceWatchdogEndpointResponse409
    | DeleteServicesServiceWatchdogEndpointResponse415
    | DeleteServicesServiceWatchdogEndpointResponse422
    | DeleteServicesServiceWatchdogEndpointResponse424
    | DeleteServicesServiceWatchdogEndpointResponse500
    | DeleteServicesServiceWatchdogEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-delete ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesServiceWatchdogEndpointResponse400 | DeleteServicesServiceWatchdogEndpointResponse401 | DeleteServicesServiceWatchdogEndpointResponse403 | DeleteServicesServiceWatchdogEndpointResponse404 | DeleteServicesServiceWatchdogEndpointResponse405 | DeleteServicesServiceWatchdogEndpointResponse406 | DeleteServicesServiceWatchdogEndpointResponse409 | DeleteServicesServiceWatchdogEndpointResponse415 | DeleteServicesServiceWatchdogEndpointResponse422 | DeleteServicesServiceWatchdogEndpointResponse424 | DeleteServicesServiceWatchdogEndpointResponse500 | DeleteServicesServiceWatchdogEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    DeleteServicesServiceWatchdogEndpointResponse400
    | DeleteServicesServiceWatchdogEndpointResponse401
    | DeleteServicesServiceWatchdogEndpointResponse403
    | DeleteServicesServiceWatchdogEndpointResponse404
    | DeleteServicesServiceWatchdogEndpointResponse405
    | DeleteServicesServiceWatchdogEndpointResponse406
    | DeleteServicesServiceWatchdogEndpointResponse409
    | DeleteServicesServiceWatchdogEndpointResponse415
    | DeleteServicesServiceWatchdogEndpointResponse422
    | DeleteServicesServiceWatchdogEndpointResponse424
    | DeleteServicesServiceWatchdogEndpointResponse500
    | DeleteServicesServiceWatchdogEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-delete ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesServiceWatchdogEndpointResponse400 | DeleteServicesServiceWatchdogEndpointResponse401 | DeleteServicesServiceWatchdogEndpointResponse403 | DeleteServicesServiceWatchdogEndpointResponse404 | DeleteServicesServiceWatchdogEndpointResponse405 | DeleteServicesServiceWatchdogEndpointResponse406 | DeleteServicesServiceWatchdogEndpointResponse409 | DeleteServicesServiceWatchdogEndpointResponse415 | DeleteServicesServiceWatchdogEndpointResponse422 | DeleteServicesServiceWatchdogEndpointResponse424 | DeleteServicesServiceWatchdogEndpointResponse500 | DeleteServicesServiceWatchdogEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    DeleteServicesServiceWatchdogEndpointResponse400
    | DeleteServicesServiceWatchdogEndpointResponse401
    | DeleteServicesServiceWatchdogEndpointResponse403
    | DeleteServicesServiceWatchdogEndpointResponse404
    | DeleteServicesServiceWatchdogEndpointResponse405
    | DeleteServicesServiceWatchdogEndpointResponse406
    | DeleteServicesServiceWatchdogEndpointResponse409
    | DeleteServicesServiceWatchdogEndpointResponse415
    | DeleteServicesServiceWatchdogEndpointResponse422
    | DeleteServicesServiceWatchdogEndpointResponse424
    | DeleteServicesServiceWatchdogEndpointResponse500
    | DeleteServicesServiceWatchdogEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-delete ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesServiceWatchdogEndpointResponse400 | DeleteServicesServiceWatchdogEndpointResponse401 | DeleteServicesServiceWatchdogEndpointResponse403 | DeleteServicesServiceWatchdogEndpointResponse404 | DeleteServicesServiceWatchdogEndpointResponse405 | DeleteServicesServiceWatchdogEndpointResponse406 | DeleteServicesServiceWatchdogEndpointResponse409 | DeleteServicesServiceWatchdogEndpointResponse415 | DeleteServicesServiceWatchdogEndpointResponse422 | DeleteServicesServiceWatchdogEndpointResponse424 | DeleteServicesServiceWatchdogEndpointResponse500 | DeleteServicesServiceWatchdogEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
