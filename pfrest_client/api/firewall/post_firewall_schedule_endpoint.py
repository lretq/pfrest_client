from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_firewall_schedule_endpoint_data_body import PostFirewallScheduleEndpointDataBody
from ...models.post_firewall_schedule_endpoint_json_body import PostFirewallScheduleEndpointJsonBody
from ...models.post_firewall_schedule_endpoint_response_400 import PostFirewallScheduleEndpointResponse400
from ...models.post_firewall_schedule_endpoint_response_401 import PostFirewallScheduleEndpointResponse401
from ...models.post_firewall_schedule_endpoint_response_403 import PostFirewallScheduleEndpointResponse403
from ...models.post_firewall_schedule_endpoint_response_404 import PostFirewallScheduleEndpointResponse404
from ...models.post_firewall_schedule_endpoint_response_405 import PostFirewallScheduleEndpointResponse405
from ...models.post_firewall_schedule_endpoint_response_406 import PostFirewallScheduleEndpointResponse406
from ...models.post_firewall_schedule_endpoint_response_409 import PostFirewallScheduleEndpointResponse409
from ...models.post_firewall_schedule_endpoint_response_415 import PostFirewallScheduleEndpointResponse415
from ...models.post_firewall_schedule_endpoint_response_422 import PostFirewallScheduleEndpointResponse422
from ...models.post_firewall_schedule_endpoint_response_424 import PostFirewallScheduleEndpointResponse424
from ...models.post_firewall_schedule_endpoint_response_500 import PostFirewallScheduleEndpointResponse500
from ...models.post_firewall_schedule_endpoint_response_503 import PostFirewallScheduleEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostFirewallScheduleEndpointJsonBody | PostFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/firewall/schedule",
    }

    if isinstance(body, PostFirewallScheduleEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFirewallScheduleEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostFirewallScheduleEndpointResponse400
    | PostFirewallScheduleEndpointResponse401
    | PostFirewallScheduleEndpointResponse403
    | PostFirewallScheduleEndpointResponse404
    | PostFirewallScheduleEndpointResponse405
    | PostFirewallScheduleEndpointResponse406
    | PostFirewallScheduleEndpointResponse409
    | PostFirewallScheduleEndpointResponse415
    | PostFirewallScheduleEndpointResponse422
    | PostFirewallScheduleEndpointResponse424
    | PostFirewallScheduleEndpointResponse500
    | PostFirewallScheduleEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostFirewallScheduleEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostFirewallScheduleEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostFirewallScheduleEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostFirewallScheduleEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostFirewallScheduleEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostFirewallScheduleEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostFirewallScheduleEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostFirewallScheduleEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostFirewallScheduleEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostFirewallScheduleEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostFirewallScheduleEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostFirewallScheduleEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostFirewallScheduleEndpointResponse400
    | PostFirewallScheduleEndpointResponse401
    | PostFirewallScheduleEndpointResponse403
    | PostFirewallScheduleEndpointResponse404
    | PostFirewallScheduleEndpointResponse405
    | PostFirewallScheduleEndpointResponse406
    | PostFirewallScheduleEndpointResponse409
    | PostFirewallScheduleEndpointResponse415
    | PostFirewallScheduleEndpointResponse422
    | PostFirewallScheduleEndpointResponse424
    | PostFirewallScheduleEndpointResponse500
    | PostFirewallScheduleEndpointResponse503
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
    body: PostFirewallScheduleEndpointJsonBody | PostFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallScheduleEndpointResponse400
    | PostFirewallScheduleEndpointResponse401
    | PostFirewallScheduleEndpointResponse403
    | PostFirewallScheduleEndpointResponse404
    | PostFirewallScheduleEndpointResponse405
    | PostFirewallScheduleEndpointResponse406
    | PostFirewallScheduleEndpointResponse409
    | PostFirewallScheduleEndpointResponse415
    | PostFirewallScheduleEndpointResponse422
    | PostFirewallScheduleEndpointResponse424
    | PostFirewallScheduleEndpointResponse500
    | PostFirewallScheduleEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Firewall Schedule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedule-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostFirewallScheduleEndpointJsonBody | Unset):
        body (PostFirewallScheduleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallScheduleEndpointResponse400 | PostFirewallScheduleEndpointResponse401 | PostFirewallScheduleEndpointResponse403 | PostFirewallScheduleEndpointResponse404 | PostFirewallScheduleEndpointResponse405 | PostFirewallScheduleEndpointResponse406 | PostFirewallScheduleEndpointResponse409 | PostFirewallScheduleEndpointResponse415 | PostFirewallScheduleEndpointResponse422 | PostFirewallScheduleEndpointResponse424 | PostFirewallScheduleEndpointResponse500 | PostFirewallScheduleEndpointResponse503]
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
    body: PostFirewallScheduleEndpointJsonBody | PostFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallScheduleEndpointResponse400
    | PostFirewallScheduleEndpointResponse401
    | PostFirewallScheduleEndpointResponse403
    | PostFirewallScheduleEndpointResponse404
    | PostFirewallScheduleEndpointResponse405
    | PostFirewallScheduleEndpointResponse406
    | PostFirewallScheduleEndpointResponse409
    | PostFirewallScheduleEndpointResponse415
    | PostFirewallScheduleEndpointResponse422
    | PostFirewallScheduleEndpointResponse424
    | PostFirewallScheduleEndpointResponse500
    | PostFirewallScheduleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Firewall Schedule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedule-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostFirewallScheduleEndpointJsonBody | Unset):
        body (PostFirewallScheduleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallScheduleEndpointResponse400 | PostFirewallScheduleEndpointResponse401 | PostFirewallScheduleEndpointResponse403 | PostFirewallScheduleEndpointResponse404 | PostFirewallScheduleEndpointResponse405 | PostFirewallScheduleEndpointResponse406 | PostFirewallScheduleEndpointResponse409 | PostFirewallScheduleEndpointResponse415 | PostFirewallScheduleEndpointResponse422 | PostFirewallScheduleEndpointResponse424 | PostFirewallScheduleEndpointResponse500 | PostFirewallScheduleEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallScheduleEndpointJsonBody | PostFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> Response[
    PostFirewallScheduleEndpointResponse400
    | PostFirewallScheduleEndpointResponse401
    | PostFirewallScheduleEndpointResponse403
    | PostFirewallScheduleEndpointResponse404
    | PostFirewallScheduleEndpointResponse405
    | PostFirewallScheduleEndpointResponse406
    | PostFirewallScheduleEndpointResponse409
    | PostFirewallScheduleEndpointResponse415
    | PostFirewallScheduleEndpointResponse422
    | PostFirewallScheduleEndpointResponse424
    | PostFirewallScheduleEndpointResponse500
    | PostFirewallScheduleEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Firewall Schedule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedule-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostFirewallScheduleEndpointJsonBody | Unset):
        body (PostFirewallScheduleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFirewallScheduleEndpointResponse400 | PostFirewallScheduleEndpointResponse401 | PostFirewallScheduleEndpointResponse403 | PostFirewallScheduleEndpointResponse404 | PostFirewallScheduleEndpointResponse405 | PostFirewallScheduleEndpointResponse406 | PostFirewallScheduleEndpointResponse409 | PostFirewallScheduleEndpointResponse415 | PostFirewallScheduleEndpointResponse422 | PostFirewallScheduleEndpointResponse424 | PostFirewallScheduleEndpointResponse500 | PostFirewallScheduleEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostFirewallScheduleEndpointJsonBody | PostFirewallScheduleEndpointDataBody | Unset = UNSET,
) -> (
    PostFirewallScheduleEndpointResponse400
    | PostFirewallScheduleEndpointResponse401
    | PostFirewallScheduleEndpointResponse403
    | PostFirewallScheduleEndpointResponse404
    | PostFirewallScheduleEndpointResponse405
    | PostFirewallScheduleEndpointResponse406
    | PostFirewallScheduleEndpointResponse409
    | PostFirewallScheduleEndpointResponse415
    | PostFirewallScheduleEndpointResponse422
    | PostFirewallScheduleEndpointResponse424
    | PostFirewallScheduleEndpointResponse500
    | PostFirewallScheduleEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Firewall Schedule.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FirewallSchedule<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-firewall-schedule-post ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PostFirewallScheduleEndpointJsonBody | Unset):
        body (PostFirewallScheduleEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFirewallScheduleEndpointResponse400 | PostFirewallScheduleEndpointResponse401 | PostFirewallScheduleEndpointResponse403 | PostFirewallScheduleEndpointResponse404 | PostFirewallScheduleEndpointResponse405 | PostFirewallScheduleEndpointResponse406 | PostFirewallScheduleEndpointResponse409 | PostFirewallScheduleEndpointResponse415 | PostFirewallScheduleEndpointResponse422 | PostFirewallScheduleEndpointResponse424 | PostFirewallScheduleEndpointResponse500 | PostFirewallScheduleEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
