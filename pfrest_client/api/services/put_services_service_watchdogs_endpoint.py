from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_service_watchdogs_endpoint_data_body_item import (
    PutServicesServiceWatchdogsEndpointDataBodyItem,
)
from ...models.put_services_service_watchdogs_endpoint_json_body_item import (
    PutServicesServiceWatchdogsEndpointJsonBodyItem,
)
from ...models.put_services_service_watchdogs_endpoint_response_400 import (
    PutServicesServiceWatchdogsEndpointResponse400,
)
from ...models.put_services_service_watchdogs_endpoint_response_401 import (
    PutServicesServiceWatchdogsEndpointResponse401,
)
from ...models.put_services_service_watchdogs_endpoint_response_403 import (
    PutServicesServiceWatchdogsEndpointResponse403,
)
from ...models.put_services_service_watchdogs_endpoint_response_404 import (
    PutServicesServiceWatchdogsEndpointResponse404,
)
from ...models.put_services_service_watchdogs_endpoint_response_405 import (
    PutServicesServiceWatchdogsEndpointResponse405,
)
from ...models.put_services_service_watchdogs_endpoint_response_406 import (
    PutServicesServiceWatchdogsEndpointResponse406,
)
from ...models.put_services_service_watchdogs_endpoint_response_409 import (
    PutServicesServiceWatchdogsEndpointResponse409,
)
from ...models.put_services_service_watchdogs_endpoint_response_415 import (
    PutServicesServiceWatchdogsEndpointResponse415,
)
from ...models.put_services_service_watchdogs_endpoint_response_422 import (
    PutServicesServiceWatchdogsEndpointResponse422,
)
from ...models.put_services_service_watchdogs_endpoint_response_424 import (
    PutServicesServiceWatchdogsEndpointResponse424,
)
from ...models.put_services_service_watchdogs_endpoint_response_500 import (
    PutServicesServiceWatchdogsEndpointResponse500,
)
from ...models.put_services_service_watchdogs_endpoint_response_503 import (
    PutServicesServiceWatchdogsEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesServiceWatchdogsEndpointJsonBodyItem]
    | list[PutServicesServiceWatchdogsEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/service_watchdogs",
    }

    if isinstance(body, list[PutServicesServiceWatchdogsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesServiceWatchdogsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesServiceWatchdogsEndpointResponse400
    | PutServicesServiceWatchdogsEndpointResponse401
    | PutServicesServiceWatchdogsEndpointResponse403
    | PutServicesServiceWatchdogsEndpointResponse404
    | PutServicesServiceWatchdogsEndpointResponse405
    | PutServicesServiceWatchdogsEndpointResponse406
    | PutServicesServiceWatchdogsEndpointResponse409
    | PutServicesServiceWatchdogsEndpointResponse415
    | PutServicesServiceWatchdogsEndpointResponse422
    | PutServicesServiceWatchdogsEndpointResponse424
    | PutServicesServiceWatchdogsEndpointResponse500
    | PutServicesServiceWatchdogsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesServiceWatchdogsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesServiceWatchdogsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesServiceWatchdogsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesServiceWatchdogsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesServiceWatchdogsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesServiceWatchdogsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesServiceWatchdogsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesServiceWatchdogsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesServiceWatchdogsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesServiceWatchdogsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesServiceWatchdogsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesServiceWatchdogsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesServiceWatchdogsEndpointResponse400
    | PutServicesServiceWatchdogsEndpointResponse401
    | PutServicesServiceWatchdogsEndpointResponse403
    | PutServicesServiceWatchdogsEndpointResponse404
    | PutServicesServiceWatchdogsEndpointResponse405
    | PutServicesServiceWatchdogsEndpointResponse406
    | PutServicesServiceWatchdogsEndpointResponse409
    | PutServicesServiceWatchdogsEndpointResponse415
    | PutServicesServiceWatchdogsEndpointResponse422
    | PutServicesServiceWatchdogsEndpointResponse424
    | PutServicesServiceWatchdogsEndpointResponse500
    | PutServicesServiceWatchdogsEndpointResponse503
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
    body: list[PutServicesServiceWatchdogsEndpointJsonBodyItem]
    | list[PutServicesServiceWatchdogsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesServiceWatchdogsEndpointResponse400
    | PutServicesServiceWatchdogsEndpointResponse401
    | PutServicesServiceWatchdogsEndpointResponse403
    | PutServicesServiceWatchdogsEndpointResponse404
    | PutServicesServiceWatchdogsEndpointResponse405
    | PutServicesServiceWatchdogsEndpointResponse406
    | PutServicesServiceWatchdogsEndpointResponse409
    | PutServicesServiceWatchdogsEndpointResponse415
    | PutServicesServiceWatchdogsEndpointResponse422
    | PutServicesServiceWatchdogsEndpointResponse424
    | PutServicesServiceWatchdogsEndpointResponse500
    | PutServicesServiceWatchdogsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Service Watchdogs.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdogs-put ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (list[PutServicesServiceWatchdogsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesServiceWatchdogsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesServiceWatchdogsEndpointResponse400 | PutServicesServiceWatchdogsEndpointResponse401 | PutServicesServiceWatchdogsEndpointResponse403 | PutServicesServiceWatchdogsEndpointResponse404 | PutServicesServiceWatchdogsEndpointResponse405 | PutServicesServiceWatchdogsEndpointResponse406 | PutServicesServiceWatchdogsEndpointResponse409 | PutServicesServiceWatchdogsEndpointResponse415 | PutServicesServiceWatchdogsEndpointResponse422 | PutServicesServiceWatchdogsEndpointResponse424 | PutServicesServiceWatchdogsEndpointResponse500 | PutServicesServiceWatchdogsEndpointResponse503]
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
    body: list[PutServicesServiceWatchdogsEndpointJsonBodyItem]
    | list[PutServicesServiceWatchdogsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesServiceWatchdogsEndpointResponse400
    | PutServicesServiceWatchdogsEndpointResponse401
    | PutServicesServiceWatchdogsEndpointResponse403
    | PutServicesServiceWatchdogsEndpointResponse404
    | PutServicesServiceWatchdogsEndpointResponse405
    | PutServicesServiceWatchdogsEndpointResponse406
    | PutServicesServiceWatchdogsEndpointResponse409
    | PutServicesServiceWatchdogsEndpointResponse415
    | PutServicesServiceWatchdogsEndpointResponse422
    | PutServicesServiceWatchdogsEndpointResponse424
    | PutServicesServiceWatchdogsEndpointResponse500
    | PutServicesServiceWatchdogsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Service Watchdogs.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdogs-put ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (list[PutServicesServiceWatchdogsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesServiceWatchdogsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesServiceWatchdogsEndpointResponse400 | PutServicesServiceWatchdogsEndpointResponse401 | PutServicesServiceWatchdogsEndpointResponse403 | PutServicesServiceWatchdogsEndpointResponse404 | PutServicesServiceWatchdogsEndpointResponse405 | PutServicesServiceWatchdogsEndpointResponse406 | PutServicesServiceWatchdogsEndpointResponse409 | PutServicesServiceWatchdogsEndpointResponse415 | PutServicesServiceWatchdogsEndpointResponse422 | PutServicesServiceWatchdogsEndpointResponse424 | PutServicesServiceWatchdogsEndpointResponse500 | PutServicesServiceWatchdogsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesServiceWatchdogsEndpointJsonBodyItem]
    | list[PutServicesServiceWatchdogsEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesServiceWatchdogsEndpointResponse400
    | PutServicesServiceWatchdogsEndpointResponse401
    | PutServicesServiceWatchdogsEndpointResponse403
    | PutServicesServiceWatchdogsEndpointResponse404
    | PutServicesServiceWatchdogsEndpointResponse405
    | PutServicesServiceWatchdogsEndpointResponse406
    | PutServicesServiceWatchdogsEndpointResponse409
    | PutServicesServiceWatchdogsEndpointResponse415
    | PutServicesServiceWatchdogsEndpointResponse422
    | PutServicesServiceWatchdogsEndpointResponse424
    | PutServicesServiceWatchdogsEndpointResponse500
    | PutServicesServiceWatchdogsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Service Watchdogs.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdogs-put ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (list[PutServicesServiceWatchdogsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesServiceWatchdogsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesServiceWatchdogsEndpointResponse400 | PutServicesServiceWatchdogsEndpointResponse401 | PutServicesServiceWatchdogsEndpointResponse403 | PutServicesServiceWatchdogsEndpointResponse404 | PutServicesServiceWatchdogsEndpointResponse405 | PutServicesServiceWatchdogsEndpointResponse406 | PutServicesServiceWatchdogsEndpointResponse409 | PutServicesServiceWatchdogsEndpointResponse415 | PutServicesServiceWatchdogsEndpointResponse422 | PutServicesServiceWatchdogsEndpointResponse424 | PutServicesServiceWatchdogsEndpointResponse500 | PutServicesServiceWatchdogsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesServiceWatchdogsEndpointJsonBodyItem]
    | list[PutServicesServiceWatchdogsEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesServiceWatchdogsEndpointResponse400
    | PutServicesServiceWatchdogsEndpointResponse401
    | PutServicesServiceWatchdogsEndpointResponse403
    | PutServicesServiceWatchdogsEndpointResponse404
    | PutServicesServiceWatchdogsEndpointResponse405
    | PutServicesServiceWatchdogsEndpointResponse406
    | PutServicesServiceWatchdogsEndpointResponse409
    | PutServicesServiceWatchdogsEndpointResponse415
    | PutServicesServiceWatchdogsEndpointResponse422
    | PutServicesServiceWatchdogsEndpointResponse424
    | PutServicesServiceWatchdogsEndpointResponse500
    | PutServicesServiceWatchdogsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Service Watchdogs.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdogs-put ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (list[PutServicesServiceWatchdogsEndpointJsonBodyItem] | Unset):
        body (list[PutServicesServiceWatchdogsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesServiceWatchdogsEndpointResponse400 | PutServicesServiceWatchdogsEndpointResponse401 | PutServicesServiceWatchdogsEndpointResponse403 | PutServicesServiceWatchdogsEndpointResponse404 | PutServicesServiceWatchdogsEndpointResponse405 | PutServicesServiceWatchdogsEndpointResponse406 | PutServicesServiceWatchdogsEndpointResponse409 | PutServicesServiceWatchdogsEndpointResponse415 | PutServicesServiceWatchdogsEndpointResponse422 | PutServicesServiceWatchdogsEndpointResponse424 | PutServicesServiceWatchdogsEndpointResponse500 | PutServicesServiceWatchdogsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
