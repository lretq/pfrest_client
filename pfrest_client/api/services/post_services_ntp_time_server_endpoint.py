from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ntp_time_server_endpoint_data_body import PostServicesNTPTimeServerEndpointDataBody
from ...models.post_services_ntp_time_server_endpoint_json_body import PostServicesNTPTimeServerEndpointJsonBody
from ...models.post_services_ntp_time_server_endpoint_response_400 import PostServicesNTPTimeServerEndpointResponse400
from ...models.post_services_ntp_time_server_endpoint_response_401 import PostServicesNTPTimeServerEndpointResponse401
from ...models.post_services_ntp_time_server_endpoint_response_403 import PostServicesNTPTimeServerEndpointResponse403
from ...models.post_services_ntp_time_server_endpoint_response_404 import PostServicesNTPTimeServerEndpointResponse404
from ...models.post_services_ntp_time_server_endpoint_response_405 import PostServicesNTPTimeServerEndpointResponse405
from ...models.post_services_ntp_time_server_endpoint_response_406 import PostServicesNTPTimeServerEndpointResponse406
from ...models.post_services_ntp_time_server_endpoint_response_409 import PostServicesNTPTimeServerEndpointResponse409
from ...models.post_services_ntp_time_server_endpoint_response_415 import PostServicesNTPTimeServerEndpointResponse415
from ...models.post_services_ntp_time_server_endpoint_response_422 import PostServicesNTPTimeServerEndpointResponse422
from ...models.post_services_ntp_time_server_endpoint_response_424 import PostServicesNTPTimeServerEndpointResponse424
from ...models.post_services_ntp_time_server_endpoint_response_500 import PostServicesNTPTimeServerEndpointResponse500
from ...models.post_services_ntp_time_server_endpoint_response_503 import PostServicesNTPTimeServerEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesNTPTimeServerEndpointJsonBody | PostServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/ntp/time_server",
    }

    if isinstance(body, PostServicesNTPTimeServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesNTPTimeServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesNTPTimeServerEndpointResponse400
    | PostServicesNTPTimeServerEndpointResponse401
    | PostServicesNTPTimeServerEndpointResponse403
    | PostServicesNTPTimeServerEndpointResponse404
    | PostServicesNTPTimeServerEndpointResponse405
    | PostServicesNTPTimeServerEndpointResponse406
    | PostServicesNTPTimeServerEndpointResponse409
    | PostServicesNTPTimeServerEndpointResponse415
    | PostServicesNTPTimeServerEndpointResponse422
    | PostServicesNTPTimeServerEndpointResponse424
    | PostServicesNTPTimeServerEndpointResponse500
    | PostServicesNTPTimeServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesNTPTimeServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesNTPTimeServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesNTPTimeServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesNTPTimeServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesNTPTimeServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesNTPTimeServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesNTPTimeServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesNTPTimeServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesNTPTimeServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesNTPTimeServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesNTPTimeServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesNTPTimeServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesNTPTimeServerEndpointResponse400
    | PostServicesNTPTimeServerEndpointResponse401
    | PostServicesNTPTimeServerEndpointResponse403
    | PostServicesNTPTimeServerEndpointResponse404
    | PostServicesNTPTimeServerEndpointResponse405
    | PostServicesNTPTimeServerEndpointResponse406
    | PostServicesNTPTimeServerEndpointResponse409
    | PostServicesNTPTimeServerEndpointResponse415
    | PostServicesNTPTimeServerEndpointResponse422
    | PostServicesNTPTimeServerEndpointResponse424
    | PostServicesNTPTimeServerEndpointResponse500
    | PostServicesNTPTimeServerEndpointResponse503
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
    body: PostServicesNTPTimeServerEndpointJsonBody | PostServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesNTPTimeServerEndpointResponse400
    | PostServicesNTPTimeServerEndpointResponse401
    | PostServicesNTPTimeServerEndpointResponse403
    | PostServicesNTPTimeServerEndpointResponse404
    | PostServicesNTPTimeServerEndpointResponse405
    | PostServicesNTPTimeServerEndpointResponse406
    | PostServicesNTPTimeServerEndpointResponse409
    | PostServicesNTPTimeServerEndpointResponse415
    | PostServicesNTPTimeServerEndpointResponse422
    | PostServicesNTPTimeServerEndpointResponse424
    | PostServicesNTPTimeServerEndpointResponse500
    | PostServicesNTPTimeServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesNTPTimeServerEndpointJsonBody | Unset):
        body (PostServicesNTPTimeServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesNTPTimeServerEndpointResponse400 | PostServicesNTPTimeServerEndpointResponse401 | PostServicesNTPTimeServerEndpointResponse403 | PostServicesNTPTimeServerEndpointResponse404 | PostServicesNTPTimeServerEndpointResponse405 | PostServicesNTPTimeServerEndpointResponse406 | PostServicesNTPTimeServerEndpointResponse409 | PostServicesNTPTimeServerEndpointResponse415 | PostServicesNTPTimeServerEndpointResponse422 | PostServicesNTPTimeServerEndpointResponse424 | PostServicesNTPTimeServerEndpointResponse500 | PostServicesNTPTimeServerEndpointResponse503]
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
    body: PostServicesNTPTimeServerEndpointJsonBody | PostServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesNTPTimeServerEndpointResponse400
    | PostServicesNTPTimeServerEndpointResponse401
    | PostServicesNTPTimeServerEndpointResponse403
    | PostServicesNTPTimeServerEndpointResponse404
    | PostServicesNTPTimeServerEndpointResponse405
    | PostServicesNTPTimeServerEndpointResponse406
    | PostServicesNTPTimeServerEndpointResponse409
    | PostServicesNTPTimeServerEndpointResponse415
    | PostServicesNTPTimeServerEndpointResponse422
    | PostServicesNTPTimeServerEndpointResponse424
    | PostServicesNTPTimeServerEndpointResponse500
    | PostServicesNTPTimeServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesNTPTimeServerEndpointJsonBody | Unset):
        body (PostServicesNTPTimeServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesNTPTimeServerEndpointResponse400 | PostServicesNTPTimeServerEndpointResponse401 | PostServicesNTPTimeServerEndpointResponse403 | PostServicesNTPTimeServerEndpointResponse404 | PostServicesNTPTimeServerEndpointResponse405 | PostServicesNTPTimeServerEndpointResponse406 | PostServicesNTPTimeServerEndpointResponse409 | PostServicesNTPTimeServerEndpointResponse415 | PostServicesNTPTimeServerEndpointResponse422 | PostServicesNTPTimeServerEndpointResponse424 | PostServicesNTPTimeServerEndpointResponse500 | PostServicesNTPTimeServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesNTPTimeServerEndpointJsonBody | PostServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesNTPTimeServerEndpointResponse400
    | PostServicesNTPTimeServerEndpointResponse401
    | PostServicesNTPTimeServerEndpointResponse403
    | PostServicesNTPTimeServerEndpointResponse404
    | PostServicesNTPTimeServerEndpointResponse405
    | PostServicesNTPTimeServerEndpointResponse406
    | PostServicesNTPTimeServerEndpointResponse409
    | PostServicesNTPTimeServerEndpointResponse415
    | PostServicesNTPTimeServerEndpointResponse422
    | PostServicesNTPTimeServerEndpointResponse424
    | PostServicesNTPTimeServerEndpointResponse500
    | PostServicesNTPTimeServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesNTPTimeServerEndpointJsonBody | Unset):
        body (PostServicesNTPTimeServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesNTPTimeServerEndpointResponse400 | PostServicesNTPTimeServerEndpointResponse401 | PostServicesNTPTimeServerEndpointResponse403 | PostServicesNTPTimeServerEndpointResponse404 | PostServicesNTPTimeServerEndpointResponse405 | PostServicesNTPTimeServerEndpointResponse406 | PostServicesNTPTimeServerEndpointResponse409 | PostServicesNTPTimeServerEndpointResponse415 | PostServicesNTPTimeServerEndpointResponse422 | PostServicesNTPTimeServerEndpointResponse424 | PostServicesNTPTimeServerEndpointResponse500 | PostServicesNTPTimeServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesNTPTimeServerEndpointJsonBody | PostServicesNTPTimeServerEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesNTPTimeServerEndpointResponse400
    | PostServicesNTPTimeServerEndpointResponse401
    | PostServicesNTPTimeServerEndpointResponse403
    | PostServicesNTPTimeServerEndpointResponse404
    | PostServicesNTPTimeServerEndpointResponse405
    | PostServicesNTPTimeServerEndpointResponse406
    | PostServicesNTPTimeServerEndpointResponse409
    | PostServicesNTPTimeServerEndpointResponse415
    | PostServicesNTPTimeServerEndpointResponse422
    | PostServicesNTPTimeServerEndpointResponse424
    | PostServicesNTPTimeServerEndpointResponse500
    | PostServicesNTPTimeServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new NTP Time Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: NTPTimeServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-ntp-time-server-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesNTPTimeServerEndpointJsonBody | Unset):
        body (PostServicesNTPTimeServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesNTPTimeServerEndpointResponse400 | PostServicesNTPTimeServerEndpointResponse401 | PostServicesNTPTimeServerEndpointResponse403 | PostServicesNTPTimeServerEndpointResponse404 | PostServicesNTPTimeServerEndpointResponse405 | PostServicesNTPTimeServerEndpointResponse406 | PostServicesNTPTimeServerEndpointResponse409 | PostServicesNTPTimeServerEndpointResponse415 | PostServicesNTPTimeServerEndpointResponse422 | PostServicesNTPTimeServerEndpointResponse424 | PostServicesNTPTimeServerEndpointResponse500 | PostServicesNTPTimeServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
