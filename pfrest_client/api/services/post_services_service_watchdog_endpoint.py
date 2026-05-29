from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_service_watchdog_endpoint_data_body import PostServicesServiceWatchdogEndpointDataBody
from ...models.post_services_service_watchdog_endpoint_json_body import PostServicesServiceWatchdogEndpointJsonBody
from ...models.post_services_service_watchdog_endpoint_response_400 import (
    PostServicesServiceWatchdogEndpointResponse400,
)
from ...models.post_services_service_watchdog_endpoint_response_401 import (
    PostServicesServiceWatchdogEndpointResponse401,
)
from ...models.post_services_service_watchdog_endpoint_response_403 import (
    PostServicesServiceWatchdogEndpointResponse403,
)
from ...models.post_services_service_watchdog_endpoint_response_404 import (
    PostServicesServiceWatchdogEndpointResponse404,
)
from ...models.post_services_service_watchdog_endpoint_response_405 import (
    PostServicesServiceWatchdogEndpointResponse405,
)
from ...models.post_services_service_watchdog_endpoint_response_406 import (
    PostServicesServiceWatchdogEndpointResponse406,
)
from ...models.post_services_service_watchdog_endpoint_response_409 import (
    PostServicesServiceWatchdogEndpointResponse409,
)
from ...models.post_services_service_watchdog_endpoint_response_415 import (
    PostServicesServiceWatchdogEndpointResponse415,
)
from ...models.post_services_service_watchdog_endpoint_response_422 import (
    PostServicesServiceWatchdogEndpointResponse422,
)
from ...models.post_services_service_watchdog_endpoint_response_424 import (
    PostServicesServiceWatchdogEndpointResponse424,
)
from ...models.post_services_service_watchdog_endpoint_response_500 import (
    PostServicesServiceWatchdogEndpointResponse500,
)
from ...models.post_services_service_watchdog_endpoint_response_503 import (
    PostServicesServiceWatchdogEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesServiceWatchdogEndpointJsonBody | PostServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/service_watchdog",
    }

    if isinstance(body, PostServicesServiceWatchdogEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesServiceWatchdogEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesServiceWatchdogEndpointResponse400
    | PostServicesServiceWatchdogEndpointResponse401
    | PostServicesServiceWatchdogEndpointResponse403
    | PostServicesServiceWatchdogEndpointResponse404
    | PostServicesServiceWatchdogEndpointResponse405
    | PostServicesServiceWatchdogEndpointResponse406
    | PostServicesServiceWatchdogEndpointResponse409
    | PostServicesServiceWatchdogEndpointResponse415
    | PostServicesServiceWatchdogEndpointResponse422
    | PostServicesServiceWatchdogEndpointResponse424
    | PostServicesServiceWatchdogEndpointResponse500
    | PostServicesServiceWatchdogEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesServiceWatchdogEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesServiceWatchdogEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesServiceWatchdogEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesServiceWatchdogEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesServiceWatchdogEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesServiceWatchdogEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesServiceWatchdogEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesServiceWatchdogEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesServiceWatchdogEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesServiceWatchdogEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesServiceWatchdogEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesServiceWatchdogEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesServiceWatchdogEndpointResponse400
    | PostServicesServiceWatchdogEndpointResponse401
    | PostServicesServiceWatchdogEndpointResponse403
    | PostServicesServiceWatchdogEndpointResponse404
    | PostServicesServiceWatchdogEndpointResponse405
    | PostServicesServiceWatchdogEndpointResponse406
    | PostServicesServiceWatchdogEndpointResponse409
    | PostServicesServiceWatchdogEndpointResponse415
    | PostServicesServiceWatchdogEndpointResponse422
    | PostServicesServiceWatchdogEndpointResponse424
    | PostServicesServiceWatchdogEndpointResponse500
    | PostServicesServiceWatchdogEndpointResponse503
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
    body: PostServicesServiceWatchdogEndpointJsonBody | PostServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesServiceWatchdogEndpointResponse400
    | PostServicesServiceWatchdogEndpointResponse401
    | PostServicesServiceWatchdogEndpointResponse403
    | PostServicesServiceWatchdogEndpointResponse404
    | PostServicesServiceWatchdogEndpointResponse405
    | PostServicesServiceWatchdogEndpointResponse406
    | PostServicesServiceWatchdogEndpointResponse409
    | PostServicesServiceWatchdogEndpointResponse415
    | PostServicesServiceWatchdogEndpointResponse422
    | PostServicesServiceWatchdogEndpointResponse424
    | PostServicesServiceWatchdogEndpointResponse500
    | PostServicesServiceWatchdogEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-post ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PostServicesServiceWatchdogEndpointJsonBody | Unset):
        body (PostServicesServiceWatchdogEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesServiceWatchdogEndpointResponse400 | PostServicesServiceWatchdogEndpointResponse401 | PostServicesServiceWatchdogEndpointResponse403 | PostServicesServiceWatchdogEndpointResponse404 | PostServicesServiceWatchdogEndpointResponse405 | PostServicesServiceWatchdogEndpointResponse406 | PostServicesServiceWatchdogEndpointResponse409 | PostServicesServiceWatchdogEndpointResponse415 | PostServicesServiceWatchdogEndpointResponse422 | PostServicesServiceWatchdogEndpointResponse424 | PostServicesServiceWatchdogEndpointResponse500 | PostServicesServiceWatchdogEndpointResponse503]
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
    body: PostServicesServiceWatchdogEndpointJsonBody | PostServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesServiceWatchdogEndpointResponse400
    | PostServicesServiceWatchdogEndpointResponse401
    | PostServicesServiceWatchdogEndpointResponse403
    | PostServicesServiceWatchdogEndpointResponse404
    | PostServicesServiceWatchdogEndpointResponse405
    | PostServicesServiceWatchdogEndpointResponse406
    | PostServicesServiceWatchdogEndpointResponse409
    | PostServicesServiceWatchdogEndpointResponse415
    | PostServicesServiceWatchdogEndpointResponse422
    | PostServicesServiceWatchdogEndpointResponse424
    | PostServicesServiceWatchdogEndpointResponse500
    | PostServicesServiceWatchdogEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-post ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PostServicesServiceWatchdogEndpointJsonBody | Unset):
        body (PostServicesServiceWatchdogEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesServiceWatchdogEndpointResponse400 | PostServicesServiceWatchdogEndpointResponse401 | PostServicesServiceWatchdogEndpointResponse403 | PostServicesServiceWatchdogEndpointResponse404 | PostServicesServiceWatchdogEndpointResponse405 | PostServicesServiceWatchdogEndpointResponse406 | PostServicesServiceWatchdogEndpointResponse409 | PostServicesServiceWatchdogEndpointResponse415 | PostServicesServiceWatchdogEndpointResponse422 | PostServicesServiceWatchdogEndpointResponse424 | PostServicesServiceWatchdogEndpointResponse500 | PostServicesServiceWatchdogEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesServiceWatchdogEndpointJsonBody | PostServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesServiceWatchdogEndpointResponse400
    | PostServicesServiceWatchdogEndpointResponse401
    | PostServicesServiceWatchdogEndpointResponse403
    | PostServicesServiceWatchdogEndpointResponse404
    | PostServicesServiceWatchdogEndpointResponse405
    | PostServicesServiceWatchdogEndpointResponse406
    | PostServicesServiceWatchdogEndpointResponse409
    | PostServicesServiceWatchdogEndpointResponse415
    | PostServicesServiceWatchdogEndpointResponse422
    | PostServicesServiceWatchdogEndpointResponse424
    | PostServicesServiceWatchdogEndpointResponse500
    | PostServicesServiceWatchdogEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-post ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PostServicesServiceWatchdogEndpointJsonBody | Unset):
        body (PostServicesServiceWatchdogEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesServiceWatchdogEndpointResponse400 | PostServicesServiceWatchdogEndpointResponse401 | PostServicesServiceWatchdogEndpointResponse403 | PostServicesServiceWatchdogEndpointResponse404 | PostServicesServiceWatchdogEndpointResponse405 | PostServicesServiceWatchdogEndpointResponse406 | PostServicesServiceWatchdogEndpointResponse409 | PostServicesServiceWatchdogEndpointResponse415 | PostServicesServiceWatchdogEndpointResponse422 | PostServicesServiceWatchdogEndpointResponse424 | PostServicesServiceWatchdogEndpointResponse500 | PostServicesServiceWatchdogEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesServiceWatchdogEndpointJsonBody | PostServicesServiceWatchdogEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesServiceWatchdogEndpointResponse400
    | PostServicesServiceWatchdogEndpointResponse401
    | PostServicesServiceWatchdogEndpointResponse403
    | PostServicesServiceWatchdogEndpointResponse404
    | PostServicesServiceWatchdogEndpointResponse405
    | PostServicesServiceWatchdogEndpointResponse406
    | PostServicesServiceWatchdogEndpointResponse409
    | PostServicesServiceWatchdogEndpointResponse415
    | PostServicesServiceWatchdogEndpointResponse422
    | PostServicesServiceWatchdogEndpointResponse424
    | PostServicesServiceWatchdogEndpointResponse500
    | PostServicesServiceWatchdogEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new Service Watchdog.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ServiceWatchdog<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-service-watchdog-post ]<br>**Required
    packages**: [ pfSense-pkg-Service_Watchdog ]<br>**Applies immediately**: Yes<br>**Utilizes cache**:
    None

    Args:
        body (PostServicesServiceWatchdogEndpointJsonBody | Unset):
        body (PostServicesServiceWatchdogEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesServiceWatchdogEndpointResponse400 | PostServicesServiceWatchdogEndpointResponse401 | PostServicesServiceWatchdogEndpointResponse403 | PostServicesServiceWatchdogEndpointResponse404 | PostServicesServiceWatchdogEndpointResponse405 | PostServicesServiceWatchdogEndpointResponse406 | PostServicesServiceWatchdogEndpointResponse409 | PostServicesServiceWatchdogEndpointResponse415 | PostServicesServiceWatchdogEndpointResponse422 | PostServicesServiceWatchdogEndpointResponse424 | PostServicesServiceWatchdogEndpointResponse500 | PostServicesServiceWatchdogEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
