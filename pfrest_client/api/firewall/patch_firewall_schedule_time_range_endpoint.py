from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_schedule_time_range_endpoint_data_body import (
    PatchFirewallScheduleTimeRangeEndpointDataBody,
)
from ...models.patch_firewall_schedule_time_range_endpoint_json_body import (
    PatchFirewallScheduleTimeRangeEndpointJsonBody,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_400 import (
    PatchFirewallScheduleTimeRangeEndpointResponse400,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_401 import (
    PatchFirewallScheduleTimeRangeEndpointResponse401,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_403 import (
    PatchFirewallScheduleTimeRangeEndpointResponse403,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_404 import (
    PatchFirewallScheduleTimeRangeEndpointResponse404,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_405 import (
    PatchFirewallScheduleTimeRangeEndpointResponse405,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_406 import (
    PatchFirewallScheduleTimeRangeEndpointResponse406,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_409 import (
    PatchFirewallScheduleTimeRangeEndpointResponse409,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_415 import (
    PatchFirewallScheduleTimeRangeEndpointResponse415,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_422 import (
    PatchFirewallScheduleTimeRangeEndpointResponse422,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_424 import (
    PatchFirewallScheduleTimeRangeEndpointResponse424,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_500 import (
    PatchFirewallScheduleTimeRangeEndpointResponse500,
)
from ...models.patch_firewall_schedule_time_range_endpoint_response_503 import (
    PatchFirewallScheduleTimeRangeEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallScheduleTimeRangeEndpointJsonBody
    | PatchFirewallScheduleTimeRangeEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/schedule/time_range",
    }

    if isinstance(body, PatchFirewallScheduleTimeRangeEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallScheduleTimeRangeEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallScheduleTimeRangeEndpointResponse400
    | PatchFirewallScheduleTimeRangeEndpointResponse401
    | PatchFirewallScheduleTimeRangeEndpointResponse403
    | PatchFirewallScheduleTimeRangeEndpointResponse404
    | PatchFirewallScheduleTimeRangeEndpointResponse405
    | PatchFirewallScheduleTimeRangeEndpointResponse406
    | PatchFirewallScheduleTimeRangeEndpointResponse409
    | PatchFirewallScheduleTimeRangeEndpointResponse415
    | PatchFirewallScheduleTimeRangeEndpointResponse422
    | PatchFirewallScheduleTimeRangeEndpointResponse424
    | PatchFirewallScheduleTimeRangeEndpointResponse500
    | PatchFirewallScheduleTimeRangeEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallScheduleTimeRangeEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallScheduleTimeRangeEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallScheduleTimeRangeEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallScheduleTimeRangeEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallScheduleTimeRangeEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallScheduleTimeRangeEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallScheduleTimeRangeEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallScheduleTimeRangeEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallScheduleTimeRangeEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallScheduleTimeRangeEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallScheduleTimeRangeEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallScheduleTimeRangeEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallScheduleTimeRangeEndpointResponse400
    | PatchFirewallScheduleTimeRangeEndpointResponse401
    | PatchFirewallScheduleTimeRangeEndpointResponse403
    | PatchFirewallScheduleTimeRangeEndpointResponse404
    | PatchFirewallScheduleTimeRangeEndpointResponse405
    | PatchFirewallScheduleTimeRangeEndpointResponse406
    | PatchFirewallScheduleTimeRangeEndpointResponse409
    | PatchFirewallScheduleTimeRangeEndpointResponse415
    | PatchFirewallScheduleTimeRangeEndpointResponse422
    | PatchFirewallScheduleTimeRangeEndpointResponse424
    | PatchFirewallScheduleTimeRangeEndpointResponse500
    | PatchFirewallScheduleTimeRangeEndpointResponse503
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
    body: PatchFirewallScheduleTimeRangeEndpointJsonBody
    | PatchFirewallScheduleTimeRangeEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallScheduleTimeRangeEndpointResponse400
    | PatchFirewallScheduleTimeRangeEndpointResponse401
    | PatchFirewallScheduleTimeRangeEndpointResponse403
    | PatchFirewallScheduleTimeRangeEndpointResponse404
    | PatchFirewallScheduleTimeRangeEndpointResponse405
    | PatchFirewallScheduleTimeRangeEndpointResponse406
    | PatchFirewallScheduleTimeRangeEndpointResponse409
    | PatchFirewallScheduleTimeRangeEndpointResponse415
    | PatchFirewallScheduleTimeRangeEndpointResponse422
    | PatchFirewallScheduleTimeRangeEndpointResponse424
    | PatchFirewallScheduleTimeRangeEndpointResponse500
    | PatchFirewallScheduleTimeRangeEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Firewall Schedule Time
    Range.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallScheduleTimeRange<br>**Parent model**: FirewallSchedule<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-schedule-time-range-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallScheduleTimeRangeEndpointJsonBody | Unset):
        body (PatchFirewallScheduleTimeRangeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallScheduleTimeRangeEndpointResponse400 | PatchFirewallScheduleTimeRangeEndpointResponse401 | PatchFirewallScheduleTimeRangeEndpointResponse403 | PatchFirewallScheduleTimeRangeEndpointResponse404 | PatchFirewallScheduleTimeRangeEndpointResponse405 | PatchFirewallScheduleTimeRangeEndpointResponse406 | PatchFirewallScheduleTimeRangeEndpointResponse409 | PatchFirewallScheduleTimeRangeEndpointResponse415 | PatchFirewallScheduleTimeRangeEndpointResponse422 | PatchFirewallScheduleTimeRangeEndpointResponse424 | PatchFirewallScheduleTimeRangeEndpointResponse500 | PatchFirewallScheduleTimeRangeEndpointResponse503]
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
    body: PatchFirewallScheduleTimeRangeEndpointJsonBody
    | PatchFirewallScheduleTimeRangeEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallScheduleTimeRangeEndpointResponse400
    | PatchFirewallScheduleTimeRangeEndpointResponse401
    | PatchFirewallScheduleTimeRangeEndpointResponse403
    | PatchFirewallScheduleTimeRangeEndpointResponse404
    | PatchFirewallScheduleTimeRangeEndpointResponse405
    | PatchFirewallScheduleTimeRangeEndpointResponse406
    | PatchFirewallScheduleTimeRangeEndpointResponse409
    | PatchFirewallScheduleTimeRangeEndpointResponse415
    | PatchFirewallScheduleTimeRangeEndpointResponse422
    | PatchFirewallScheduleTimeRangeEndpointResponse424
    | PatchFirewallScheduleTimeRangeEndpointResponse500
    | PatchFirewallScheduleTimeRangeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Firewall Schedule Time
    Range.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallScheduleTimeRange<br>**Parent model**: FirewallSchedule<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-schedule-time-range-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallScheduleTimeRangeEndpointJsonBody | Unset):
        body (PatchFirewallScheduleTimeRangeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallScheduleTimeRangeEndpointResponse400 | PatchFirewallScheduleTimeRangeEndpointResponse401 | PatchFirewallScheduleTimeRangeEndpointResponse403 | PatchFirewallScheduleTimeRangeEndpointResponse404 | PatchFirewallScheduleTimeRangeEndpointResponse405 | PatchFirewallScheduleTimeRangeEndpointResponse406 | PatchFirewallScheduleTimeRangeEndpointResponse409 | PatchFirewallScheduleTimeRangeEndpointResponse415 | PatchFirewallScheduleTimeRangeEndpointResponse422 | PatchFirewallScheduleTimeRangeEndpointResponse424 | PatchFirewallScheduleTimeRangeEndpointResponse500 | PatchFirewallScheduleTimeRangeEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallScheduleTimeRangeEndpointJsonBody
    | PatchFirewallScheduleTimeRangeEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchFirewallScheduleTimeRangeEndpointResponse400
    | PatchFirewallScheduleTimeRangeEndpointResponse401
    | PatchFirewallScheduleTimeRangeEndpointResponse403
    | PatchFirewallScheduleTimeRangeEndpointResponse404
    | PatchFirewallScheduleTimeRangeEndpointResponse405
    | PatchFirewallScheduleTimeRangeEndpointResponse406
    | PatchFirewallScheduleTimeRangeEndpointResponse409
    | PatchFirewallScheduleTimeRangeEndpointResponse415
    | PatchFirewallScheduleTimeRangeEndpointResponse422
    | PatchFirewallScheduleTimeRangeEndpointResponse424
    | PatchFirewallScheduleTimeRangeEndpointResponse500
    | PatchFirewallScheduleTimeRangeEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Firewall Schedule Time
    Range.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallScheduleTimeRange<br>**Parent model**: FirewallSchedule<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-schedule-time-range-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallScheduleTimeRangeEndpointJsonBody | Unset):
        body (PatchFirewallScheduleTimeRangeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallScheduleTimeRangeEndpointResponse400 | PatchFirewallScheduleTimeRangeEndpointResponse401 | PatchFirewallScheduleTimeRangeEndpointResponse403 | PatchFirewallScheduleTimeRangeEndpointResponse404 | PatchFirewallScheduleTimeRangeEndpointResponse405 | PatchFirewallScheduleTimeRangeEndpointResponse406 | PatchFirewallScheduleTimeRangeEndpointResponse409 | PatchFirewallScheduleTimeRangeEndpointResponse415 | PatchFirewallScheduleTimeRangeEndpointResponse422 | PatchFirewallScheduleTimeRangeEndpointResponse424 | PatchFirewallScheduleTimeRangeEndpointResponse500 | PatchFirewallScheduleTimeRangeEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallScheduleTimeRangeEndpointJsonBody
    | PatchFirewallScheduleTimeRangeEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchFirewallScheduleTimeRangeEndpointResponse400
    | PatchFirewallScheduleTimeRangeEndpointResponse401
    | PatchFirewallScheduleTimeRangeEndpointResponse403
    | PatchFirewallScheduleTimeRangeEndpointResponse404
    | PatchFirewallScheduleTimeRangeEndpointResponse405
    | PatchFirewallScheduleTimeRangeEndpointResponse406
    | PatchFirewallScheduleTimeRangeEndpointResponse409
    | PatchFirewallScheduleTimeRangeEndpointResponse415
    | PatchFirewallScheduleTimeRangeEndpointResponse422
    | PatchFirewallScheduleTimeRangeEndpointResponse424
    | PatchFirewallScheduleTimeRangeEndpointResponse500
    | PatchFirewallScheduleTimeRangeEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Firewall Schedule Time
    Range.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    FirewallScheduleTimeRange<br>**Parent model**: FirewallSchedule<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-firewall-schedule-time-range-patch ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallScheduleTimeRangeEndpointJsonBody | Unset):
        body (PatchFirewallScheduleTimeRangeEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallScheduleTimeRangeEndpointResponse400 | PatchFirewallScheduleTimeRangeEndpointResponse401 | PatchFirewallScheduleTimeRangeEndpointResponse403 | PatchFirewallScheduleTimeRangeEndpointResponse404 | PatchFirewallScheduleTimeRangeEndpointResponse405 | PatchFirewallScheduleTimeRangeEndpointResponse406 | PatchFirewallScheduleTimeRangeEndpointResponse409 | PatchFirewallScheduleTimeRangeEndpointResponse415 | PatchFirewallScheduleTimeRangeEndpointResponse422 | PatchFirewallScheduleTimeRangeEndpointResponse424 | PatchFirewallScheduleTimeRangeEndpointResponse500 | PatchFirewallScheduleTimeRangeEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
