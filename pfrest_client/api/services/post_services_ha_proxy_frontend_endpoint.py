from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_frontend_endpoint_data_body import PostServicesHAProxyFrontendEndpointDataBody
from ...models.post_services_ha_proxy_frontend_endpoint_json_body import PostServicesHAProxyFrontendEndpointJsonBody
from ...models.post_services_ha_proxy_frontend_endpoint_response_400 import (
    PostServicesHAProxyFrontendEndpointResponse400,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_401 import (
    PostServicesHAProxyFrontendEndpointResponse401,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_403 import (
    PostServicesHAProxyFrontendEndpointResponse403,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_404 import (
    PostServicesHAProxyFrontendEndpointResponse404,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_405 import (
    PostServicesHAProxyFrontendEndpointResponse405,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_406 import (
    PostServicesHAProxyFrontendEndpointResponse406,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_409 import (
    PostServicesHAProxyFrontendEndpointResponse409,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_415 import (
    PostServicesHAProxyFrontendEndpointResponse415,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_422 import (
    PostServicesHAProxyFrontendEndpointResponse422,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_424 import (
    PostServicesHAProxyFrontendEndpointResponse424,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_500 import (
    PostServicesHAProxyFrontendEndpointResponse500,
)
from ...models.post_services_ha_proxy_frontend_endpoint_response_503 import (
    PostServicesHAProxyFrontendEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyFrontendEndpointJsonBody | PostServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/frontend",
    }

    if isinstance(body, PostServicesHAProxyFrontendEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyFrontendEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyFrontendEndpointResponse400
    | PostServicesHAProxyFrontendEndpointResponse401
    | PostServicesHAProxyFrontendEndpointResponse403
    | PostServicesHAProxyFrontendEndpointResponse404
    | PostServicesHAProxyFrontendEndpointResponse405
    | PostServicesHAProxyFrontendEndpointResponse406
    | PostServicesHAProxyFrontendEndpointResponse409
    | PostServicesHAProxyFrontendEndpointResponse415
    | PostServicesHAProxyFrontendEndpointResponse422
    | PostServicesHAProxyFrontendEndpointResponse424
    | PostServicesHAProxyFrontendEndpointResponse500
    | PostServicesHAProxyFrontendEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyFrontendEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyFrontendEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyFrontendEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyFrontendEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyFrontendEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyFrontendEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyFrontendEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyFrontendEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyFrontendEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyFrontendEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyFrontendEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyFrontendEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyFrontendEndpointResponse400
    | PostServicesHAProxyFrontendEndpointResponse401
    | PostServicesHAProxyFrontendEndpointResponse403
    | PostServicesHAProxyFrontendEndpointResponse404
    | PostServicesHAProxyFrontendEndpointResponse405
    | PostServicesHAProxyFrontendEndpointResponse406
    | PostServicesHAProxyFrontendEndpointResponse409
    | PostServicesHAProxyFrontendEndpointResponse415
    | PostServicesHAProxyFrontendEndpointResponse422
    | PostServicesHAProxyFrontendEndpointResponse424
    | PostServicesHAProxyFrontendEndpointResponse500
    | PostServicesHAProxyFrontendEndpointResponse503
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
    body: PostServicesHAProxyFrontendEndpointJsonBody | PostServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesHAProxyFrontendEndpointResponse400
    | PostServicesHAProxyFrontendEndpointResponse401
    | PostServicesHAProxyFrontendEndpointResponse403
    | PostServicesHAProxyFrontendEndpointResponse404
    | PostServicesHAProxyFrontendEndpointResponse405
    | PostServicesHAProxyFrontendEndpointResponse406
    | PostServicesHAProxyFrontendEndpointResponse409
    | PostServicesHAProxyFrontendEndpointResponse415
    | PostServicesHAProxyFrontendEndpointResponse422
    | PostServicesHAProxyFrontendEndpointResponse424
    | PostServicesHAProxyFrontendEndpointResponse500
    | PostServicesHAProxyFrontendEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyFrontendEndpointResponse400 | PostServicesHAProxyFrontendEndpointResponse401 | PostServicesHAProxyFrontendEndpointResponse403 | PostServicesHAProxyFrontendEndpointResponse404 | PostServicesHAProxyFrontendEndpointResponse405 | PostServicesHAProxyFrontendEndpointResponse406 | PostServicesHAProxyFrontendEndpointResponse409 | PostServicesHAProxyFrontendEndpointResponse415 | PostServicesHAProxyFrontendEndpointResponse422 | PostServicesHAProxyFrontendEndpointResponse424 | PostServicesHAProxyFrontendEndpointResponse500 | PostServicesHAProxyFrontendEndpointResponse503]
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
    body: PostServicesHAProxyFrontendEndpointJsonBody | PostServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesHAProxyFrontendEndpointResponse400
    | PostServicesHAProxyFrontendEndpointResponse401
    | PostServicesHAProxyFrontendEndpointResponse403
    | PostServicesHAProxyFrontendEndpointResponse404
    | PostServicesHAProxyFrontendEndpointResponse405
    | PostServicesHAProxyFrontendEndpointResponse406
    | PostServicesHAProxyFrontendEndpointResponse409
    | PostServicesHAProxyFrontendEndpointResponse415
    | PostServicesHAProxyFrontendEndpointResponse422
    | PostServicesHAProxyFrontendEndpointResponse424
    | PostServicesHAProxyFrontendEndpointResponse500
    | PostServicesHAProxyFrontendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyFrontendEndpointResponse400 | PostServicesHAProxyFrontendEndpointResponse401 | PostServicesHAProxyFrontendEndpointResponse403 | PostServicesHAProxyFrontendEndpointResponse404 | PostServicesHAProxyFrontendEndpointResponse405 | PostServicesHAProxyFrontendEndpointResponse406 | PostServicesHAProxyFrontendEndpointResponse409 | PostServicesHAProxyFrontendEndpointResponse415 | PostServicesHAProxyFrontendEndpointResponse422 | PostServicesHAProxyFrontendEndpointResponse424 | PostServicesHAProxyFrontendEndpointResponse500 | PostServicesHAProxyFrontendEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyFrontendEndpointJsonBody | PostServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesHAProxyFrontendEndpointResponse400
    | PostServicesHAProxyFrontendEndpointResponse401
    | PostServicesHAProxyFrontendEndpointResponse403
    | PostServicesHAProxyFrontendEndpointResponse404
    | PostServicesHAProxyFrontendEndpointResponse405
    | PostServicesHAProxyFrontendEndpointResponse406
    | PostServicesHAProxyFrontendEndpointResponse409
    | PostServicesHAProxyFrontendEndpointResponse415
    | PostServicesHAProxyFrontendEndpointResponse422
    | PostServicesHAProxyFrontendEndpointResponse424
    | PostServicesHAProxyFrontendEndpointResponse500
    | PostServicesHAProxyFrontendEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyFrontendEndpointResponse400 | PostServicesHAProxyFrontendEndpointResponse401 | PostServicesHAProxyFrontendEndpointResponse403 | PostServicesHAProxyFrontendEndpointResponse404 | PostServicesHAProxyFrontendEndpointResponse405 | PostServicesHAProxyFrontendEndpointResponse406 | PostServicesHAProxyFrontendEndpointResponse409 | PostServicesHAProxyFrontendEndpointResponse415 | PostServicesHAProxyFrontendEndpointResponse422 | PostServicesHAProxyFrontendEndpointResponse424 | PostServicesHAProxyFrontendEndpointResponse500 | PostServicesHAProxyFrontendEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyFrontendEndpointJsonBody | PostServicesHAProxyFrontendEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesHAProxyFrontendEndpointResponse400
    | PostServicesHAProxyFrontendEndpointResponse401
    | PostServicesHAProxyFrontendEndpointResponse403
    | PostServicesHAProxyFrontendEndpointResponse404
    | PostServicesHAProxyFrontendEndpointResponse405
    | PostServicesHAProxyFrontendEndpointResponse406
    | PostServicesHAProxyFrontendEndpointResponse409
    | PostServicesHAProxyFrontendEndpointResponse415
    | PostServicesHAProxyFrontendEndpointResponse422
    | PostServicesHAProxyFrontendEndpointResponse424
    | PostServicesHAProxyFrontendEndpointResponse500
    | PostServicesHAProxyFrontendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Frontend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-frontend-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyFrontendEndpointResponse400 | PostServicesHAProxyFrontendEndpointResponse401 | PostServicesHAProxyFrontendEndpointResponse403 | PostServicesHAProxyFrontendEndpointResponse404 | PostServicesHAProxyFrontendEndpointResponse405 | PostServicesHAProxyFrontendEndpointResponse406 | PostServicesHAProxyFrontendEndpointResponse409 | PostServicesHAProxyFrontendEndpointResponse415 | PostServicesHAProxyFrontendEndpointResponse422 | PostServicesHAProxyFrontendEndpointResponse424 | PostServicesHAProxyFrontendEndpointResponse500 | PostServicesHAProxyFrontendEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
