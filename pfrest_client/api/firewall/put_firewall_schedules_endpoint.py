from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_firewall_schedules_endpoint_data_body_item import PutFirewallSchedulesEndpointDataBodyItem
from ...models.put_firewall_schedules_endpoint_json_body_item import PutFirewallSchedulesEndpointJsonBodyItem
from ...models.put_firewall_schedules_endpoint_response_400 import PutFirewallSchedulesEndpointResponse400
from ...models.put_firewall_schedules_endpoint_response_401 import PutFirewallSchedulesEndpointResponse401
from ...models.put_firewall_schedules_endpoint_response_403 import PutFirewallSchedulesEndpointResponse403
from ...models.put_firewall_schedules_endpoint_response_404 import PutFirewallSchedulesEndpointResponse404
from ...models.put_firewall_schedules_endpoint_response_405 import PutFirewallSchedulesEndpointResponse405
from ...models.put_firewall_schedules_endpoint_response_406 import PutFirewallSchedulesEndpointResponse406
from ...models.put_firewall_schedules_endpoint_response_409 import PutFirewallSchedulesEndpointResponse409
from ...models.put_firewall_schedules_endpoint_response_415 import PutFirewallSchedulesEndpointResponse415
from ...models.put_firewall_schedules_endpoint_response_422 import PutFirewallSchedulesEndpointResponse422
from ...models.put_firewall_schedules_endpoint_response_424 import PutFirewallSchedulesEndpointResponse424
from ...models.put_firewall_schedules_endpoint_response_500 import PutFirewallSchedulesEndpointResponse500
from ...models.put_firewall_schedules_endpoint_response_503 import PutFirewallSchedulesEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutFirewallSchedulesEndpointJsonBodyItem]
    | list[PutFirewallSchedulesEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/firewall/schedules",
    }

    if isinstance(body, list[PutFirewallSchedulesEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutFirewallSchedulesEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutFirewallSchedulesEndpointResponse400
    | PutFirewallSchedulesEndpointResponse401
    | PutFirewallSchedulesEndpointResponse403
    | PutFirewallSchedulesEndpointResponse404
    | PutFirewallSchedulesEndpointResponse405
    | PutFirewallSchedulesEndpointResponse406
    | PutFirewallSchedulesEndpointResponse409
    | PutFirewallSchedulesEndpointResponse415
    | PutFirewallSchedulesEndpointResponse422
    | PutFirewallSchedulesEndpointResponse424
    | PutFirewallSchedulesEndpointResponse500
    | PutFirewallSchedulesEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutFirewallSchedulesEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutFirewallSchedulesEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutFirewallSchedulesEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutFirewallSchedulesEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutFirewallSchedulesEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutFirewallSchedulesEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutFirewallSchedulesEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutFirewallSchedulesEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutFirewallSchedulesEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutFirewallSchedulesEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutFirewallSchedulesEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutFirewallSchedulesEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutFirewallSchedulesEndpointResponse400
    | PutFirewallSchedulesEndpointResponse401
    | PutFirewallSchedulesEndpointResponse403
    | PutFirewallSchedulesEndpointResponse404
    | PutFirewallSchedulesEndpointResponse405
    | PutFirewallSchedulesEndpointResponse406
    | PutFirewallSchedulesEndpointResponse409
    | PutFirewallSchedulesEndpointResponse415
    | PutFirewallSchedulesEndpointResponse422
    | PutFirewallSchedulesEndpointResponse424
    | PutFirewallSchedulesEndpointResponse500
    | PutFirewallSchedulesEndpointResponse503
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
    body: list[PutFirewallSchedulesEndpointJsonBodyItem]
    | list[PutFirewallSchedulesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutFirewallSchedulesEndpointResponse400
    | PutFirewallSchedulesEndpointResponse401
    | PutFirewallSchedulesEndpointResponse403
    | PutFirewallSchedulesEndpointResponse404
    | PutFirewallSchedulesEndpointResponse405
    | PutFirewallSchedulesEndpointResponse406
    | PutFirewallSchedulesEndpointResponse409
    | PutFirewallSchedulesEndpointResponse415
    | PutFirewallSchedulesEndpointResponse422
    | PutFirewallSchedulesEndpointResponse424
    | PutFirewallSchedulesEndpointResponse500
    | PutFirewallSchedulesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Firewall Schedules.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedules-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallSchedulesEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallSchedulesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFirewallSchedulesEndpointResponse400 | PutFirewallSchedulesEndpointResponse401 | PutFirewallSchedulesEndpointResponse403 | PutFirewallSchedulesEndpointResponse404 | PutFirewallSchedulesEndpointResponse405 | PutFirewallSchedulesEndpointResponse406 | PutFirewallSchedulesEndpointResponse409 | PutFirewallSchedulesEndpointResponse415 | PutFirewallSchedulesEndpointResponse422 | PutFirewallSchedulesEndpointResponse424 | PutFirewallSchedulesEndpointResponse500 | PutFirewallSchedulesEndpointResponse503]
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
    body: list[PutFirewallSchedulesEndpointJsonBodyItem]
    | list[PutFirewallSchedulesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutFirewallSchedulesEndpointResponse400
    | PutFirewallSchedulesEndpointResponse401
    | PutFirewallSchedulesEndpointResponse403
    | PutFirewallSchedulesEndpointResponse404
    | PutFirewallSchedulesEndpointResponse405
    | PutFirewallSchedulesEndpointResponse406
    | PutFirewallSchedulesEndpointResponse409
    | PutFirewallSchedulesEndpointResponse415
    | PutFirewallSchedulesEndpointResponse422
    | PutFirewallSchedulesEndpointResponse424
    | PutFirewallSchedulesEndpointResponse500
    | PutFirewallSchedulesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Firewall Schedules.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedules-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallSchedulesEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallSchedulesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFirewallSchedulesEndpointResponse400 | PutFirewallSchedulesEndpointResponse401 | PutFirewallSchedulesEndpointResponse403 | PutFirewallSchedulesEndpointResponse404 | PutFirewallSchedulesEndpointResponse405 | PutFirewallSchedulesEndpointResponse406 | PutFirewallSchedulesEndpointResponse409 | PutFirewallSchedulesEndpointResponse415 | PutFirewallSchedulesEndpointResponse422 | PutFirewallSchedulesEndpointResponse424 | PutFirewallSchedulesEndpointResponse500 | PutFirewallSchedulesEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutFirewallSchedulesEndpointJsonBodyItem]
    | list[PutFirewallSchedulesEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutFirewallSchedulesEndpointResponse400
    | PutFirewallSchedulesEndpointResponse401
    | PutFirewallSchedulesEndpointResponse403
    | PutFirewallSchedulesEndpointResponse404
    | PutFirewallSchedulesEndpointResponse405
    | PutFirewallSchedulesEndpointResponse406
    | PutFirewallSchedulesEndpointResponse409
    | PutFirewallSchedulesEndpointResponse415
    | PutFirewallSchedulesEndpointResponse422
    | PutFirewallSchedulesEndpointResponse424
    | PutFirewallSchedulesEndpointResponse500
    | PutFirewallSchedulesEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing Firewall Schedules.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedules-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallSchedulesEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallSchedulesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFirewallSchedulesEndpointResponse400 | PutFirewallSchedulesEndpointResponse401 | PutFirewallSchedulesEndpointResponse403 | PutFirewallSchedulesEndpointResponse404 | PutFirewallSchedulesEndpointResponse405 | PutFirewallSchedulesEndpointResponse406 | PutFirewallSchedulesEndpointResponse409 | PutFirewallSchedulesEndpointResponse415 | PutFirewallSchedulesEndpointResponse422 | PutFirewallSchedulesEndpointResponse424 | PutFirewallSchedulesEndpointResponse500 | PutFirewallSchedulesEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutFirewallSchedulesEndpointJsonBodyItem]
    | list[PutFirewallSchedulesEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutFirewallSchedulesEndpointResponse400
    | PutFirewallSchedulesEndpointResponse401
    | PutFirewallSchedulesEndpointResponse403
    | PutFirewallSchedulesEndpointResponse404
    | PutFirewallSchedulesEndpointResponse405
    | PutFirewallSchedulesEndpointResponse406
    | PutFirewallSchedulesEndpointResponse409
    | PutFirewallSchedulesEndpointResponse415
    | PutFirewallSchedulesEndpointResponse422
    | PutFirewallSchedulesEndpointResponse424
    | PutFirewallSchedulesEndpointResponse500
    | PutFirewallSchedulesEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing Firewall Schedules.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedules-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutFirewallSchedulesEndpointJsonBodyItem] | Unset):
        body (list[PutFirewallSchedulesEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFirewallSchedulesEndpointResponse400 | PutFirewallSchedulesEndpointResponse401 | PutFirewallSchedulesEndpointResponse403 | PutFirewallSchedulesEndpointResponse404 | PutFirewallSchedulesEndpointResponse405 | PutFirewallSchedulesEndpointResponse406 | PutFirewallSchedulesEndpointResponse409 | PutFirewallSchedulesEndpointResponse415 | PutFirewallSchedulesEndpointResponse422 | PutFirewallSchedulesEndpointResponse424 | PutFirewallSchedulesEndpointResponse500 | PutFirewallSchedulesEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
