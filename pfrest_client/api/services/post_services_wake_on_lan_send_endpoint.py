from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_wake_on_lan_send_endpoint_data_body import PostServicesWakeOnLANSendEndpointDataBody
from ...models.post_services_wake_on_lan_send_endpoint_json_body import PostServicesWakeOnLANSendEndpointJsonBody
from ...models.post_services_wake_on_lan_send_endpoint_response_400 import PostServicesWakeOnLANSendEndpointResponse400
from ...models.post_services_wake_on_lan_send_endpoint_response_401 import PostServicesWakeOnLANSendEndpointResponse401
from ...models.post_services_wake_on_lan_send_endpoint_response_403 import PostServicesWakeOnLANSendEndpointResponse403
from ...models.post_services_wake_on_lan_send_endpoint_response_404 import PostServicesWakeOnLANSendEndpointResponse404
from ...models.post_services_wake_on_lan_send_endpoint_response_405 import PostServicesWakeOnLANSendEndpointResponse405
from ...models.post_services_wake_on_lan_send_endpoint_response_406 import PostServicesWakeOnLANSendEndpointResponse406
from ...models.post_services_wake_on_lan_send_endpoint_response_409 import PostServicesWakeOnLANSendEndpointResponse409
from ...models.post_services_wake_on_lan_send_endpoint_response_415 import PostServicesWakeOnLANSendEndpointResponse415
from ...models.post_services_wake_on_lan_send_endpoint_response_422 import PostServicesWakeOnLANSendEndpointResponse422
from ...models.post_services_wake_on_lan_send_endpoint_response_424 import PostServicesWakeOnLANSendEndpointResponse424
from ...models.post_services_wake_on_lan_send_endpoint_response_500 import PostServicesWakeOnLANSendEndpointResponse500
from ...models.post_services_wake_on_lan_send_endpoint_response_503 import PostServicesWakeOnLANSendEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesWakeOnLANSendEndpointJsonBody | PostServicesWakeOnLANSendEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/wake_on_lan/send",
    }

    if isinstance(body, PostServicesWakeOnLANSendEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesWakeOnLANSendEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesWakeOnLANSendEndpointResponse400
    | PostServicesWakeOnLANSendEndpointResponse401
    | PostServicesWakeOnLANSendEndpointResponse403
    | PostServicesWakeOnLANSendEndpointResponse404
    | PostServicesWakeOnLANSendEndpointResponse405
    | PostServicesWakeOnLANSendEndpointResponse406
    | PostServicesWakeOnLANSendEndpointResponse409
    | PostServicesWakeOnLANSendEndpointResponse415
    | PostServicesWakeOnLANSendEndpointResponse422
    | PostServicesWakeOnLANSendEndpointResponse424
    | PostServicesWakeOnLANSendEndpointResponse500
    | PostServicesWakeOnLANSendEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesWakeOnLANSendEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesWakeOnLANSendEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesWakeOnLANSendEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesWakeOnLANSendEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesWakeOnLANSendEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesWakeOnLANSendEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesWakeOnLANSendEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesWakeOnLANSendEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesWakeOnLANSendEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesWakeOnLANSendEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesWakeOnLANSendEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesWakeOnLANSendEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesWakeOnLANSendEndpointResponse400
    | PostServicesWakeOnLANSendEndpointResponse401
    | PostServicesWakeOnLANSendEndpointResponse403
    | PostServicesWakeOnLANSendEndpointResponse404
    | PostServicesWakeOnLANSendEndpointResponse405
    | PostServicesWakeOnLANSendEndpointResponse406
    | PostServicesWakeOnLANSendEndpointResponse409
    | PostServicesWakeOnLANSendEndpointResponse415
    | PostServicesWakeOnLANSendEndpointResponse422
    | PostServicesWakeOnLANSendEndpointResponse424
    | PostServicesWakeOnLANSendEndpointResponse500
    | PostServicesWakeOnLANSendEndpointResponse503
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
    body: PostServicesWakeOnLANSendEndpointJsonBody | PostServicesWakeOnLANSendEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesWakeOnLANSendEndpointResponse400
    | PostServicesWakeOnLANSendEndpointResponse401
    | PostServicesWakeOnLANSendEndpointResponse403
    | PostServicesWakeOnLANSendEndpointResponse404
    | PostServicesWakeOnLANSendEndpointResponse405
    | PostServicesWakeOnLANSendEndpointResponse406
    | PostServicesWakeOnLANSendEndpointResponse409
    | PostServicesWakeOnLANSendEndpointResponse415
    | PostServicesWakeOnLANSendEndpointResponse422
    | PostServicesWakeOnLANSendEndpointResponse424
    | PostServicesWakeOnLANSendEndpointResponse500
    | PostServicesWakeOnLANSendEndpointResponse503
]:
    """<h3>Description:</h3>Sends a Wake-on-LAN magic packet.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WakeOnLANSend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-wake-on-lan-send-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesWakeOnLANSendEndpointJsonBody | Unset):
        body (PostServicesWakeOnLANSendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesWakeOnLANSendEndpointResponse400 | PostServicesWakeOnLANSendEndpointResponse401 | PostServicesWakeOnLANSendEndpointResponse403 | PostServicesWakeOnLANSendEndpointResponse404 | PostServicesWakeOnLANSendEndpointResponse405 | PostServicesWakeOnLANSendEndpointResponse406 | PostServicesWakeOnLANSendEndpointResponse409 | PostServicesWakeOnLANSendEndpointResponse415 | PostServicesWakeOnLANSendEndpointResponse422 | PostServicesWakeOnLANSendEndpointResponse424 | PostServicesWakeOnLANSendEndpointResponse500 | PostServicesWakeOnLANSendEndpointResponse503]
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
    body: PostServicesWakeOnLANSendEndpointJsonBody | PostServicesWakeOnLANSendEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesWakeOnLANSendEndpointResponse400
    | PostServicesWakeOnLANSendEndpointResponse401
    | PostServicesWakeOnLANSendEndpointResponse403
    | PostServicesWakeOnLANSendEndpointResponse404
    | PostServicesWakeOnLANSendEndpointResponse405
    | PostServicesWakeOnLANSendEndpointResponse406
    | PostServicesWakeOnLANSendEndpointResponse409
    | PostServicesWakeOnLANSendEndpointResponse415
    | PostServicesWakeOnLANSendEndpointResponse422
    | PostServicesWakeOnLANSendEndpointResponse424
    | PostServicesWakeOnLANSendEndpointResponse500
    | PostServicesWakeOnLANSendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Sends a Wake-on-LAN magic packet.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WakeOnLANSend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-wake-on-lan-send-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesWakeOnLANSendEndpointJsonBody | Unset):
        body (PostServicesWakeOnLANSendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesWakeOnLANSendEndpointResponse400 | PostServicesWakeOnLANSendEndpointResponse401 | PostServicesWakeOnLANSendEndpointResponse403 | PostServicesWakeOnLANSendEndpointResponse404 | PostServicesWakeOnLANSendEndpointResponse405 | PostServicesWakeOnLANSendEndpointResponse406 | PostServicesWakeOnLANSendEndpointResponse409 | PostServicesWakeOnLANSendEndpointResponse415 | PostServicesWakeOnLANSendEndpointResponse422 | PostServicesWakeOnLANSendEndpointResponse424 | PostServicesWakeOnLANSendEndpointResponse500 | PostServicesWakeOnLANSendEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesWakeOnLANSendEndpointJsonBody | PostServicesWakeOnLANSendEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesWakeOnLANSendEndpointResponse400
    | PostServicesWakeOnLANSendEndpointResponse401
    | PostServicesWakeOnLANSendEndpointResponse403
    | PostServicesWakeOnLANSendEndpointResponse404
    | PostServicesWakeOnLANSendEndpointResponse405
    | PostServicesWakeOnLANSendEndpointResponse406
    | PostServicesWakeOnLANSendEndpointResponse409
    | PostServicesWakeOnLANSendEndpointResponse415
    | PostServicesWakeOnLANSendEndpointResponse422
    | PostServicesWakeOnLANSendEndpointResponse424
    | PostServicesWakeOnLANSendEndpointResponse500
    | PostServicesWakeOnLANSendEndpointResponse503
]:
    """<h3>Description:</h3>Sends a Wake-on-LAN magic packet.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WakeOnLANSend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-wake-on-lan-send-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesWakeOnLANSendEndpointJsonBody | Unset):
        body (PostServicesWakeOnLANSendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesWakeOnLANSendEndpointResponse400 | PostServicesWakeOnLANSendEndpointResponse401 | PostServicesWakeOnLANSendEndpointResponse403 | PostServicesWakeOnLANSendEndpointResponse404 | PostServicesWakeOnLANSendEndpointResponse405 | PostServicesWakeOnLANSendEndpointResponse406 | PostServicesWakeOnLANSendEndpointResponse409 | PostServicesWakeOnLANSendEndpointResponse415 | PostServicesWakeOnLANSendEndpointResponse422 | PostServicesWakeOnLANSendEndpointResponse424 | PostServicesWakeOnLANSendEndpointResponse500 | PostServicesWakeOnLANSendEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesWakeOnLANSendEndpointJsonBody | PostServicesWakeOnLANSendEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesWakeOnLANSendEndpointResponse400
    | PostServicesWakeOnLANSendEndpointResponse401
    | PostServicesWakeOnLANSendEndpointResponse403
    | PostServicesWakeOnLANSendEndpointResponse404
    | PostServicesWakeOnLANSendEndpointResponse405
    | PostServicesWakeOnLANSendEndpointResponse406
    | PostServicesWakeOnLANSendEndpointResponse409
    | PostServicesWakeOnLANSendEndpointResponse415
    | PostServicesWakeOnLANSendEndpointResponse422
    | PostServicesWakeOnLANSendEndpointResponse424
    | PostServicesWakeOnLANSendEndpointResponse500
    | PostServicesWakeOnLANSendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Sends a Wake-on-LAN magic packet.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: WakeOnLANSend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-wake-on-lan-send-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesWakeOnLANSendEndpointJsonBody | Unset):
        body (PostServicesWakeOnLANSendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesWakeOnLANSendEndpointResponse400 | PostServicesWakeOnLANSendEndpointResponse401 | PostServicesWakeOnLANSendEndpointResponse403 | PostServicesWakeOnLANSendEndpointResponse404 | PostServicesWakeOnLANSendEndpointResponse405 | PostServicesWakeOnLANSendEndpointResponse406 | PostServicesWakeOnLANSendEndpointResponse409 | PostServicesWakeOnLANSendEndpointResponse415 | PostServicesWakeOnLANSendEndpointResponse422 | PostServicesWakeOnLANSendEndpointResponse424 | PostServicesWakeOnLANSendEndpointResponse500 | PostServicesWakeOnLANSendEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
