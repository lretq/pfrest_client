from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_ntp_time_servers_endpoint_data_body_item import (
    PutServicesNTPTimeServersEndpointDataBodyItem,
)
from ...models.put_services_ntp_time_servers_endpoint_json_body_item import (
    PutServicesNTPTimeServersEndpointJsonBodyItem,
)
from ...models.put_services_ntp_time_servers_endpoint_response_400 import PutServicesNTPTimeServersEndpointResponse400
from ...models.put_services_ntp_time_servers_endpoint_response_401 import PutServicesNTPTimeServersEndpointResponse401
from ...models.put_services_ntp_time_servers_endpoint_response_403 import PutServicesNTPTimeServersEndpointResponse403
from ...models.put_services_ntp_time_servers_endpoint_response_404 import PutServicesNTPTimeServersEndpointResponse404
from ...models.put_services_ntp_time_servers_endpoint_response_405 import PutServicesNTPTimeServersEndpointResponse405
from ...models.put_services_ntp_time_servers_endpoint_response_406 import PutServicesNTPTimeServersEndpointResponse406
from ...models.put_services_ntp_time_servers_endpoint_response_409 import PutServicesNTPTimeServersEndpointResponse409
from ...models.put_services_ntp_time_servers_endpoint_response_415 import PutServicesNTPTimeServersEndpointResponse415
from ...models.put_services_ntp_time_servers_endpoint_response_422 import PutServicesNTPTimeServersEndpointResponse422
from ...models.put_services_ntp_time_servers_endpoint_response_424 import PutServicesNTPTimeServersEndpointResponse424
from ...models.put_services_ntp_time_servers_endpoint_response_500 import PutServicesNTPTimeServersEndpointResponse500
from ...models.put_services_ntp_time_servers_endpoint_response_503 import PutServicesNTPTimeServersEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesNTPTimeServersEndpointJsonBodyItem]
    | list[PutServicesNTPTimeServersEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/ntp/time_servers",
    }

    if isinstance(body, list[PutServicesNTPTimeServersEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesNTPTimeServersEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesNTPTimeServersEndpointResponse400
    | PutServicesNTPTimeServersEndpointResponse401
    | PutServicesNTPTimeServersEndpointResponse403
    | PutServicesNTPTimeServersEndpointResponse404
    | PutServicesNTPTimeServersEndpointResponse405
    | PutServicesNTPTimeServersEndpointResponse406
    | PutServicesNTPTimeServersEndpointResponse409
    | PutServicesNTPTimeServersEndpointResponse415
    | PutServicesNTPTimeServersEndpointResponse422
    | PutServicesNTPTimeServersEndpointResponse424
    | PutServicesNTPTimeServersEndpointResponse500
    | PutServicesNTPTimeServersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesNTPTimeServersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesNTPTimeServersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesNTPTimeServersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesNTPTimeServersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesNTPTimeServersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesNTPTimeServersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesNTPTimeServersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesNTPTimeServersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesNTPTimeServersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesNTPTimeServersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesNTPTimeServersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesNTPTimeServersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesNTPTimeServersEndpointResponse400
    | PutServicesNTPTimeServersEndpointResponse401
    | PutServicesNTPTimeServersEndpointResponse403
    | PutServicesNTPTimeServersEndpointResponse404
    | PutServicesNTPTimeServersEndpointResponse405
    | PutServicesNTPTimeServersEndpointResponse406
    | PutServicesNTPTimeServersEndpointResponse409
    | PutServicesNTPTimeServersEndpointResponse415
    | PutServicesNTPTimeServersEndpointResponse422
    | PutServicesNTPTimeServersEndpointResponse424
    | PutServicesNTPTimeServersEndpointResponse500
    | PutServicesNTPTimeServersEndpointResponse503
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
    body: list[PutServicesNTPTimeServersEndpointJsonBodyItem]
    | list[PutServicesNTPTimeServersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesNTPTimeServersEndpointResponse400
    | PutServicesNTPTimeServersEndpointResponse401
    | PutServicesNTPTimeServersEndpointResponse403
    | PutServicesNTPTimeServersEndpointResponse404
    | PutServicesNTPTimeServersEndpointResponse405
    | PutServicesNTPTimeServersEndpointResponse406
    | PutServicesNTPTimeServersEndpointResponse409
    | PutServicesNTPTimeServersEndpointResponse415
    | PutServicesNTPTimeServersEndpointResponse422
    | PutServicesNTPTimeServersEndpointResponse424
    | PutServicesNTPTimeServersEndpointResponse500
    | PutServicesNTPTimeServersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing NTP Time Servers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-servers-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesNTPTimeServersEndpointJsonBodyItem] | Unset):
        body (list[PutServicesNTPTimeServersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesNTPTimeServersEndpointResponse400 | PutServicesNTPTimeServersEndpointResponse401 | PutServicesNTPTimeServersEndpointResponse403 | PutServicesNTPTimeServersEndpointResponse404 | PutServicesNTPTimeServersEndpointResponse405 | PutServicesNTPTimeServersEndpointResponse406 | PutServicesNTPTimeServersEndpointResponse409 | PutServicesNTPTimeServersEndpointResponse415 | PutServicesNTPTimeServersEndpointResponse422 | PutServicesNTPTimeServersEndpointResponse424 | PutServicesNTPTimeServersEndpointResponse500 | PutServicesNTPTimeServersEndpointResponse503]
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
    body: list[PutServicesNTPTimeServersEndpointJsonBodyItem]
    | list[PutServicesNTPTimeServersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesNTPTimeServersEndpointResponse400
    | PutServicesNTPTimeServersEndpointResponse401
    | PutServicesNTPTimeServersEndpointResponse403
    | PutServicesNTPTimeServersEndpointResponse404
    | PutServicesNTPTimeServersEndpointResponse405
    | PutServicesNTPTimeServersEndpointResponse406
    | PutServicesNTPTimeServersEndpointResponse409
    | PutServicesNTPTimeServersEndpointResponse415
    | PutServicesNTPTimeServersEndpointResponse422
    | PutServicesNTPTimeServersEndpointResponse424
    | PutServicesNTPTimeServersEndpointResponse500
    | PutServicesNTPTimeServersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing NTP Time Servers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-servers-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesNTPTimeServersEndpointJsonBodyItem] | Unset):
        body (list[PutServicesNTPTimeServersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesNTPTimeServersEndpointResponse400 | PutServicesNTPTimeServersEndpointResponse401 | PutServicesNTPTimeServersEndpointResponse403 | PutServicesNTPTimeServersEndpointResponse404 | PutServicesNTPTimeServersEndpointResponse405 | PutServicesNTPTimeServersEndpointResponse406 | PutServicesNTPTimeServersEndpointResponse409 | PutServicesNTPTimeServersEndpointResponse415 | PutServicesNTPTimeServersEndpointResponse422 | PutServicesNTPTimeServersEndpointResponse424 | PutServicesNTPTimeServersEndpointResponse500 | PutServicesNTPTimeServersEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesNTPTimeServersEndpointJsonBodyItem]
    | list[PutServicesNTPTimeServersEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesNTPTimeServersEndpointResponse400
    | PutServicesNTPTimeServersEndpointResponse401
    | PutServicesNTPTimeServersEndpointResponse403
    | PutServicesNTPTimeServersEndpointResponse404
    | PutServicesNTPTimeServersEndpointResponse405
    | PutServicesNTPTimeServersEndpointResponse406
    | PutServicesNTPTimeServersEndpointResponse409
    | PutServicesNTPTimeServersEndpointResponse415
    | PutServicesNTPTimeServersEndpointResponse422
    | PutServicesNTPTimeServersEndpointResponse424
    | PutServicesNTPTimeServersEndpointResponse500
    | PutServicesNTPTimeServersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing NTP Time Servers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-servers-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesNTPTimeServersEndpointJsonBodyItem] | Unset):
        body (list[PutServicesNTPTimeServersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesNTPTimeServersEndpointResponse400 | PutServicesNTPTimeServersEndpointResponse401 | PutServicesNTPTimeServersEndpointResponse403 | PutServicesNTPTimeServersEndpointResponse404 | PutServicesNTPTimeServersEndpointResponse405 | PutServicesNTPTimeServersEndpointResponse406 | PutServicesNTPTimeServersEndpointResponse409 | PutServicesNTPTimeServersEndpointResponse415 | PutServicesNTPTimeServersEndpointResponse422 | PutServicesNTPTimeServersEndpointResponse424 | PutServicesNTPTimeServersEndpointResponse500 | PutServicesNTPTimeServersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesNTPTimeServersEndpointJsonBodyItem]
    | list[PutServicesNTPTimeServersEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesNTPTimeServersEndpointResponse400
    | PutServicesNTPTimeServersEndpointResponse401
    | PutServicesNTPTimeServersEndpointResponse403
    | PutServicesNTPTimeServersEndpointResponse404
    | PutServicesNTPTimeServersEndpointResponse405
    | PutServicesNTPTimeServersEndpointResponse406
    | PutServicesNTPTimeServersEndpointResponse409
    | PutServicesNTPTimeServersEndpointResponse415
    | PutServicesNTPTimeServersEndpointResponse422
    | PutServicesNTPTimeServersEndpointResponse424
    | PutServicesNTPTimeServersEndpointResponse500
    | PutServicesNTPTimeServersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing NTP Time Servers.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-servers-put ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesNTPTimeServersEndpointJsonBodyItem] | Unset):
        body (list[PutServicesNTPTimeServersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesNTPTimeServersEndpointResponse400 | PutServicesNTPTimeServersEndpointResponse401 | PutServicesNTPTimeServersEndpointResponse403 | PutServicesNTPTimeServersEndpointResponse404 | PutServicesNTPTimeServersEndpointResponse405 | PutServicesNTPTimeServersEndpointResponse406 | PutServicesNTPTimeServersEndpointResponse409 | PutServicesNTPTimeServersEndpointResponse415 | PutServicesNTPTimeServersEndpointResponse422 | PutServicesNTPTimeServersEndpointResponse424 | PutServicesNTPTimeServersEndpointResponse500 | PutServicesNTPTimeServersEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
