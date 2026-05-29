from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_firewall_schedule_endpoint_data_body import PatchFirewallScheduleEndpointDataBody
from ...models.patch_firewall_schedule_endpoint_json_body import PatchFirewallScheduleEndpointJsonBody
from ...models.patch_firewall_schedule_endpoint_response_400 import PatchFirewallScheduleEndpointResponse400
from ...models.patch_firewall_schedule_endpoint_response_401 import PatchFirewallScheduleEndpointResponse401
from ...models.patch_firewall_schedule_endpoint_response_403 import PatchFirewallScheduleEndpointResponse403
from ...models.patch_firewall_schedule_endpoint_response_404 import PatchFirewallScheduleEndpointResponse404
from ...models.patch_firewall_schedule_endpoint_response_405 import PatchFirewallScheduleEndpointResponse405
from ...models.patch_firewall_schedule_endpoint_response_406 import PatchFirewallScheduleEndpointResponse406
from ...models.patch_firewall_schedule_endpoint_response_409 import PatchFirewallScheduleEndpointResponse409
from ...models.patch_firewall_schedule_endpoint_response_415 import PatchFirewallScheduleEndpointResponse415
from ...models.patch_firewall_schedule_endpoint_response_422 import PatchFirewallScheduleEndpointResponse422
from ...models.patch_firewall_schedule_endpoint_response_424 import PatchFirewallScheduleEndpointResponse424
from ...models.patch_firewall_schedule_endpoint_response_500 import PatchFirewallScheduleEndpointResponse500
from ...models.patch_firewall_schedule_endpoint_response_503 import PatchFirewallScheduleEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchFirewallScheduleEndpointJsonBody | PatchFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/firewall/schedule",
    }

    if isinstance(body, PatchFirewallScheduleEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchFirewallScheduleEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchFirewallScheduleEndpointResponse400
    | PatchFirewallScheduleEndpointResponse401
    | PatchFirewallScheduleEndpointResponse403
    | PatchFirewallScheduleEndpointResponse404
    | PatchFirewallScheduleEndpointResponse405
    | PatchFirewallScheduleEndpointResponse406
    | PatchFirewallScheduleEndpointResponse409
    | PatchFirewallScheduleEndpointResponse415
    | PatchFirewallScheduleEndpointResponse422
    | PatchFirewallScheduleEndpointResponse424
    | PatchFirewallScheduleEndpointResponse500
    | PatchFirewallScheduleEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchFirewallScheduleEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchFirewallScheduleEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchFirewallScheduleEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchFirewallScheduleEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchFirewallScheduleEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchFirewallScheduleEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchFirewallScheduleEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchFirewallScheduleEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchFirewallScheduleEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchFirewallScheduleEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchFirewallScheduleEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchFirewallScheduleEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchFirewallScheduleEndpointResponse400
    | PatchFirewallScheduleEndpointResponse401
    | PatchFirewallScheduleEndpointResponse403
    | PatchFirewallScheduleEndpointResponse404
    | PatchFirewallScheduleEndpointResponse405
    | PatchFirewallScheduleEndpointResponse406
    | PatchFirewallScheduleEndpointResponse409
    | PatchFirewallScheduleEndpointResponse415
    | PatchFirewallScheduleEndpointResponse422
    | PatchFirewallScheduleEndpointResponse424
    | PatchFirewallScheduleEndpointResponse500
    | PatchFirewallScheduleEndpointResponse503
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
    body: PatchFirewallScheduleEndpointJsonBody | PatchFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallScheduleEndpointResponse400
    | PatchFirewallScheduleEndpointResponse401
    | PatchFirewallScheduleEndpointResponse403
    | PatchFirewallScheduleEndpointResponse404
    | PatchFirewallScheduleEndpointResponse405
    | PatchFirewallScheduleEndpointResponse406
    | PatchFirewallScheduleEndpointResponse409
    | PatchFirewallScheduleEndpointResponse415
    | PatchFirewallScheduleEndpointResponse422
    | PatchFirewallScheduleEndpointResponse424
    | PatchFirewallScheduleEndpointResponse500
    | PatchFirewallScheduleEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Firewall Schedule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedule-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallScheduleEndpointJsonBody | Unset):
        body (PatchFirewallScheduleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallScheduleEndpointResponse400 | PatchFirewallScheduleEndpointResponse401 | PatchFirewallScheduleEndpointResponse403 | PatchFirewallScheduleEndpointResponse404 | PatchFirewallScheduleEndpointResponse405 | PatchFirewallScheduleEndpointResponse406 | PatchFirewallScheduleEndpointResponse409 | PatchFirewallScheduleEndpointResponse415 | PatchFirewallScheduleEndpointResponse422 | PatchFirewallScheduleEndpointResponse424 | PatchFirewallScheduleEndpointResponse500 | PatchFirewallScheduleEndpointResponse503]
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
    body: PatchFirewallScheduleEndpointJsonBody | PatchFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallScheduleEndpointResponse400
    | PatchFirewallScheduleEndpointResponse401
    | PatchFirewallScheduleEndpointResponse403
    | PatchFirewallScheduleEndpointResponse404
    | PatchFirewallScheduleEndpointResponse405
    | PatchFirewallScheduleEndpointResponse406
    | PatchFirewallScheduleEndpointResponse409
    | PatchFirewallScheduleEndpointResponse415
    | PatchFirewallScheduleEndpointResponse422
    | PatchFirewallScheduleEndpointResponse424
    | PatchFirewallScheduleEndpointResponse500
    | PatchFirewallScheduleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Firewall Schedule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedule-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallScheduleEndpointJsonBody | Unset):
        body (PatchFirewallScheduleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallScheduleEndpointResponse400 | PatchFirewallScheduleEndpointResponse401 | PatchFirewallScheduleEndpointResponse403 | PatchFirewallScheduleEndpointResponse404 | PatchFirewallScheduleEndpointResponse405 | PatchFirewallScheduleEndpointResponse406 | PatchFirewallScheduleEndpointResponse409 | PatchFirewallScheduleEndpointResponse415 | PatchFirewallScheduleEndpointResponse422 | PatchFirewallScheduleEndpointResponse424 | PatchFirewallScheduleEndpointResponse500 | PatchFirewallScheduleEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallScheduleEndpointJsonBody | PatchFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchFirewallScheduleEndpointResponse400
    | PatchFirewallScheduleEndpointResponse401
    | PatchFirewallScheduleEndpointResponse403
    | PatchFirewallScheduleEndpointResponse404
    | PatchFirewallScheduleEndpointResponse405
    | PatchFirewallScheduleEndpointResponse406
    | PatchFirewallScheduleEndpointResponse409
    | PatchFirewallScheduleEndpointResponse415
    | PatchFirewallScheduleEndpointResponse422
    | PatchFirewallScheduleEndpointResponse424
    | PatchFirewallScheduleEndpointResponse500
    | PatchFirewallScheduleEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing Firewall Schedule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedule-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallScheduleEndpointJsonBody | Unset):
        body (PatchFirewallScheduleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchFirewallScheduleEndpointResponse400 | PatchFirewallScheduleEndpointResponse401 | PatchFirewallScheduleEndpointResponse403 | PatchFirewallScheduleEndpointResponse404 | PatchFirewallScheduleEndpointResponse405 | PatchFirewallScheduleEndpointResponse406 | PatchFirewallScheduleEndpointResponse409 | PatchFirewallScheduleEndpointResponse415 | PatchFirewallScheduleEndpointResponse422 | PatchFirewallScheduleEndpointResponse424 | PatchFirewallScheduleEndpointResponse500 | PatchFirewallScheduleEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchFirewallScheduleEndpointJsonBody | PatchFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> (
    PatchFirewallScheduleEndpointResponse400
    | PatchFirewallScheduleEndpointResponse401
    | PatchFirewallScheduleEndpointResponse403
    | PatchFirewallScheduleEndpointResponse404
    | PatchFirewallScheduleEndpointResponse405
    | PatchFirewallScheduleEndpointResponse406
    | PatchFirewallScheduleEndpointResponse409
    | PatchFirewallScheduleEndpointResponse415
    | PatchFirewallScheduleEndpointResponse422
    | PatchFirewallScheduleEndpointResponse424
    | PatchFirewallScheduleEndpointResponse500
    | PatchFirewallScheduleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing Firewall Schedule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedule-patch ]<br>**Required packages**:
    [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchFirewallScheduleEndpointJsonBody | Unset):
        body (PatchFirewallScheduleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchFirewallScheduleEndpointResponse400 | PatchFirewallScheduleEndpointResponse401 | PatchFirewallScheduleEndpointResponse403 | PatchFirewallScheduleEndpointResponse404 | PatchFirewallScheduleEndpointResponse405 | PatchFirewallScheduleEndpointResponse406 | PatchFirewallScheduleEndpointResponse409 | PatchFirewallScheduleEndpointResponse415 | PatchFirewallScheduleEndpointResponse422 | PatchFirewallScheduleEndpointResponse424 | PatchFirewallScheduleEndpointResponse500 | PatchFirewallScheduleEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
