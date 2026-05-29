from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_firewall_schedule_time_range_endpoint_response_400 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse400,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_401 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse401,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_403 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse403,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_404 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse404,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_405 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse405,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_406 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse406,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_409 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse409,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_415 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse415,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_422 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse422,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_424 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse424,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_500 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse500,
)
from ...models.delete_firewall_schedule_time_range_endpoint_response_503 import (
    DeleteFirewallScheduleTimeRangeEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/firewall/schedule/time_range",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteFirewallScheduleTimeRangeEndpointResponse400
    | DeleteFirewallScheduleTimeRangeEndpointResponse401
    | DeleteFirewallScheduleTimeRangeEndpointResponse403
    | DeleteFirewallScheduleTimeRangeEndpointResponse404
    | DeleteFirewallScheduleTimeRangeEndpointResponse405
    | DeleteFirewallScheduleTimeRangeEndpointResponse406
    | DeleteFirewallScheduleTimeRangeEndpointResponse409
    | DeleteFirewallScheduleTimeRangeEndpointResponse415
    | DeleteFirewallScheduleTimeRangeEndpointResponse422
    | DeleteFirewallScheduleTimeRangeEndpointResponse424
    | DeleteFirewallScheduleTimeRangeEndpointResponse500
    | DeleteFirewallScheduleTimeRangeEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteFirewallScheduleTimeRangeEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteFirewallScheduleTimeRangeEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteFirewallScheduleTimeRangeEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteFirewallScheduleTimeRangeEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteFirewallScheduleTimeRangeEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteFirewallScheduleTimeRangeEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteFirewallScheduleTimeRangeEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteFirewallScheduleTimeRangeEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteFirewallScheduleTimeRangeEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteFirewallScheduleTimeRangeEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteFirewallScheduleTimeRangeEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteFirewallScheduleTimeRangeEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteFirewallScheduleTimeRangeEndpointResponse400
    | DeleteFirewallScheduleTimeRangeEndpointResponse401
    | DeleteFirewallScheduleTimeRangeEndpointResponse403
    | DeleteFirewallScheduleTimeRangeEndpointResponse404
    | DeleteFirewallScheduleTimeRangeEndpointResponse405
    | DeleteFirewallScheduleTimeRangeEndpointResponse406
    | DeleteFirewallScheduleTimeRangeEndpointResponse409
    | DeleteFirewallScheduleTimeRangeEndpointResponse415
    | DeleteFirewallScheduleTimeRangeEndpointResponse422
    | DeleteFirewallScheduleTimeRangeEndpointResponse424
    | DeleteFirewallScheduleTimeRangeEndpointResponse500
    | DeleteFirewallScheduleTimeRangeEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteFirewallScheduleTimeRangeEndpointResponse400
    | DeleteFirewallScheduleTimeRangeEndpointResponse401
    | DeleteFirewallScheduleTimeRangeEndpointResponse403
    | DeleteFirewallScheduleTimeRangeEndpointResponse404
    | DeleteFirewallScheduleTimeRangeEndpointResponse405
    | DeleteFirewallScheduleTimeRangeEndpointResponse406
    | DeleteFirewallScheduleTimeRangeEndpointResponse409
    | DeleteFirewallScheduleTimeRangeEndpointResponse415
    | DeleteFirewallScheduleTimeRangeEndpointResponse422
    | DeleteFirewallScheduleTimeRangeEndpointResponse424
    | DeleteFirewallScheduleTimeRangeEndpointResponse500
    | DeleteFirewallScheduleTimeRangeEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Firewall Schedule Time
    Range.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallScheduleTimeRange<br>**Parent model**: FirewallSchedule<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-schedule-time-range-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallScheduleTimeRangeEndpointResponse400 | DeleteFirewallScheduleTimeRangeEndpointResponse401 | DeleteFirewallScheduleTimeRangeEndpointResponse403 | DeleteFirewallScheduleTimeRangeEndpointResponse404 | DeleteFirewallScheduleTimeRangeEndpointResponse405 | DeleteFirewallScheduleTimeRangeEndpointResponse406 | DeleteFirewallScheduleTimeRangeEndpointResponse409 | DeleteFirewallScheduleTimeRangeEndpointResponse415 | DeleteFirewallScheduleTimeRangeEndpointResponse422 | DeleteFirewallScheduleTimeRangeEndpointResponse424 | DeleteFirewallScheduleTimeRangeEndpointResponse500 | DeleteFirewallScheduleTimeRangeEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteFirewallScheduleTimeRangeEndpointResponse400
    | DeleteFirewallScheduleTimeRangeEndpointResponse401
    | DeleteFirewallScheduleTimeRangeEndpointResponse403
    | DeleteFirewallScheduleTimeRangeEndpointResponse404
    | DeleteFirewallScheduleTimeRangeEndpointResponse405
    | DeleteFirewallScheduleTimeRangeEndpointResponse406
    | DeleteFirewallScheduleTimeRangeEndpointResponse409
    | DeleteFirewallScheduleTimeRangeEndpointResponse415
    | DeleteFirewallScheduleTimeRangeEndpointResponse422
    | DeleteFirewallScheduleTimeRangeEndpointResponse424
    | DeleteFirewallScheduleTimeRangeEndpointResponse500
    | DeleteFirewallScheduleTimeRangeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Firewall Schedule Time
    Range.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallScheduleTimeRange<br>**Parent model**: FirewallSchedule<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-schedule-time-range-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallScheduleTimeRangeEndpointResponse400 | DeleteFirewallScheduleTimeRangeEndpointResponse401 | DeleteFirewallScheduleTimeRangeEndpointResponse403 | DeleteFirewallScheduleTimeRangeEndpointResponse404 | DeleteFirewallScheduleTimeRangeEndpointResponse405 | DeleteFirewallScheduleTimeRangeEndpointResponse406 | DeleteFirewallScheduleTimeRangeEndpointResponse409 | DeleteFirewallScheduleTimeRangeEndpointResponse415 | DeleteFirewallScheduleTimeRangeEndpointResponse422 | DeleteFirewallScheduleTimeRangeEndpointResponse424 | DeleteFirewallScheduleTimeRangeEndpointResponse500 | DeleteFirewallScheduleTimeRangeEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    DeleteFirewallScheduleTimeRangeEndpointResponse400
    | DeleteFirewallScheduleTimeRangeEndpointResponse401
    | DeleteFirewallScheduleTimeRangeEndpointResponse403
    | DeleteFirewallScheduleTimeRangeEndpointResponse404
    | DeleteFirewallScheduleTimeRangeEndpointResponse405
    | DeleteFirewallScheduleTimeRangeEndpointResponse406
    | DeleteFirewallScheduleTimeRangeEndpointResponse409
    | DeleteFirewallScheduleTimeRangeEndpointResponse415
    | DeleteFirewallScheduleTimeRangeEndpointResponse422
    | DeleteFirewallScheduleTimeRangeEndpointResponse424
    | DeleteFirewallScheduleTimeRangeEndpointResponse500
    | DeleteFirewallScheduleTimeRangeEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Firewall Schedule Time
    Range.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallScheduleTimeRange<br>**Parent model**: FirewallSchedule<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-schedule-time-range-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFirewallScheduleTimeRangeEndpointResponse400 | DeleteFirewallScheduleTimeRangeEndpointResponse401 | DeleteFirewallScheduleTimeRangeEndpointResponse403 | DeleteFirewallScheduleTimeRangeEndpointResponse404 | DeleteFirewallScheduleTimeRangeEndpointResponse405 | DeleteFirewallScheduleTimeRangeEndpointResponse406 | DeleteFirewallScheduleTimeRangeEndpointResponse409 | DeleteFirewallScheduleTimeRangeEndpointResponse415 | DeleteFirewallScheduleTimeRangeEndpointResponse422 | DeleteFirewallScheduleTimeRangeEndpointResponse424 | DeleteFirewallScheduleTimeRangeEndpointResponse500 | DeleteFirewallScheduleTimeRangeEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    DeleteFirewallScheduleTimeRangeEndpointResponse400
    | DeleteFirewallScheduleTimeRangeEndpointResponse401
    | DeleteFirewallScheduleTimeRangeEndpointResponse403
    | DeleteFirewallScheduleTimeRangeEndpointResponse404
    | DeleteFirewallScheduleTimeRangeEndpointResponse405
    | DeleteFirewallScheduleTimeRangeEndpointResponse406
    | DeleteFirewallScheduleTimeRangeEndpointResponse409
    | DeleteFirewallScheduleTimeRangeEndpointResponse415
    | DeleteFirewallScheduleTimeRangeEndpointResponse422
    | DeleteFirewallScheduleTimeRangeEndpointResponse424
    | DeleteFirewallScheduleTimeRangeEndpointResponse500
    | DeleteFirewallScheduleTimeRangeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Firewall Schedule Time
    Range.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallScheduleTimeRange<br>**Parent model**: FirewallSchedule<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-schedule-time-range-delete ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFirewallScheduleTimeRangeEndpointResponse400 | DeleteFirewallScheduleTimeRangeEndpointResponse401 | DeleteFirewallScheduleTimeRangeEndpointResponse403 | DeleteFirewallScheduleTimeRangeEndpointResponse404 | DeleteFirewallScheduleTimeRangeEndpointResponse405 | DeleteFirewallScheduleTimeRangeEndpointResponse406 | DeleteFirewallScheduleTimeRangeEndpointResponse409 | DeleteFirewallScheduleTimeRangeEndpointResponse415 | DeleteFirewallScheduleTimeRangeEndpointResponse422 | DeleteFirewallScheduleTimeRangeEndpointResponse424 | DeleteFirewallScheduleTimeRangeEndpointResponse500 | DeleteFirewallScheduleTimeRangeEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
