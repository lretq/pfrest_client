from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_backend_endpoint_data_body import PostServicesHAProxyBackendEndpointDataBody
from ...models.post_services_ha_proxy_backend_endpoint_json_body import PostServicesHAProxyBackendEndpointJsonBody
from ...models.post_services_ha_proxy_backend_endpoint_response_400 import PostServicesHAProxyBackendEndpointResponse400
from ...models.post_services_ha_proxy_backend_endpoint_response_401 import PostServicesHAProxyBackendEndpointResponse401
from ...models.post_services_ha_proxy_backend_endpoint_response_403 import PostServicesHAProxyBackendEndpointResponse403
from ...models.post_services_ha_proxy_backend_endpoint_response_404 import PostServicesHAProxyBackendEndpointResponse404
from ...models.post_services_ha_proxy_backend_endpoint_response_405 import PostServicesHAProxyBackendEndpointResponse405
from ...models.post_services_ha_proxy_backend_endpoint_response_406 import PostServicesHAProxyBackendEndpointResponse406
from ...models.post_services_ha_proxy_backend_endpoint_response_409 import PostServicesHAProxyBackendEndpointResponse409
from ...models.post_services_ha_proxy_backend_endpoint_response_415 import PostServicesHAProxyBackendEndpointResponse415
from ...models.post_services_ha_proxy_backend_endpoint_response_422 import PostServicesHAProxyBackendEndpointResponse422
from ...models.post_services_ha_proxy_backend_endpoint_response_424 import PostServicesHAProxyBackendEndpointResponse424
from ...models.post_services_ha_proxy_backend_endpoint_response_500 import PostServicesHAProxyBackendEndpointResponse500
from ...models.post_services_ha_proxy_backend_endpoint_response_503 import PostServicesHAProxyBackendEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyBackendEndpointJsonBody | PostServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/backend",
    }

    if isinstance(body, PostServicesHAProxyBackendEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyBackendEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyBackendEndpointResponse400
    | PostServicesHAProxyBackendEndpointResponse401
    | PostServicesHAProxyBackendEndpointResponse403
    | PostServicesHAProxyBackendEndpointResponse404
    | PostServicesHAProxyBackendEndpointResponse405
    | PostServicesHAProxyBackendEndpointResponse406
    | PostServicesHAProxyBackendEndpointResponse409
    | PostServicesHAProxyBackendEndpointResponse415
    | PostServicesHAProxyBackendEndpointResponse422
    | PostServicesHAProxyBackendEndpointResponse424
    | PostServicesHAProxyBackendEndpointResponse500
    | PostServicesHAProxyBackendEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyBackendEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyBackendEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyBackendEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyBackendEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyBackendEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyBackendEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyBackendEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyBackendEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyBackendEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyBackendEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyBackendEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyBackendEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyBackendEndpointResponse400
    | PostServicesHAProxyBackendEndpointResponse401
    | PostServicesHAProxyBackendEndpointResponse403
    | PostServicesHAProxyBackendEndpointResponse404
    | PostServicesHAProxyBackendEndpointResponse405
    | PostServicesHAProxyBackendEndpointResponse406
    | PostServicesHAProxyBackendEndpointResponse409
    | PostServicesHAProxyBackendEndpointResponse415
    | PostServicesHAProxyBackendEndpointResponse422
    | PostServicesHAProxyBackendEndpointResponse424
    | PostServicesHAProxyBackendEndpointResponse500
    | PostServicesHAProxyBackendEndpointResponse503
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
    body: PostServicesHAProxyBackendEndpointJsonBody | PostServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendEndpointResponse400
    | PostServicesHAProxyBackendEndpointResponse401
    | PostServicesHAProxyBackendEndpointResponse403
    | PostServicesHAProxyBackendEndpointResponse404
    | PostServicesHAProxyBackendEndpointResponse405
    | PostServicesHAProxyBackendEndpointResponse406
    | PostServicesHAProxyBackendEndpointResponse409
    | PostServicesHAProxyBackendEndpointResponse415
    | PostServicesHAProxyBackendEndpointResponse422
    | PostServicesHAProxyBackendEndpointResponse424
    | PostServicesHAProxyBackendEndpointResponse500
    | PostServicesHAProxyBackendEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendEndpointResponse400 | PostServicesHAProxyBackendEndpointResponse401 | PostServicesHAProxyBackendEndpointResponse403 | PostServicesHAProxyBackendEndpointResponse404 | PostServicesHAProxyBackendEndpointResponse405 | PostServicesHAProxyBackendEndpointResponse406 | PostServicesHAProxyBackendEndpointResponse409 | PostServicesHAProxyBackendEndpointResponse415 | PostServicesHAProxyBackendEndpointResponse422 | PostServicesHAProxyBackendEndpointResponse424 | PostServicesHAProxyBackendEndpointResponse500 | PostServicesHAProxyBackendEndpointResponse503]
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
    body: PostServicesHAProxyBackendEndpointJsonBody | PostServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendEndpointResponse400
    | PostServicesHAProxyBackendEndpointResponse401
    | PostServicesHAProxyBackendEndpointResponse403
    | PostServicesHAProxyBackendEndpointResponse404
    | PostServicesHAProxyBackendEndpointResponse405
    | PostServicesHAProxyBackendEndpointResponse406
    | PostServicesHAProxyBackendEndpointResponse409
    | PostServicesHAProxyBackendEndpointResponse415
    | PostServicesHAProxyBackendEndpointResponse422
    | PostServicesHAProxyBackendEndpointResponse424
    | PostServicesHAProxyBackendEndpointResponse500
    | PostServicesHAProxyBackendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendEndpointResponse400 | PostServicesHAProxyBackendEndpointResponse401 | PostServicesHAProxyBackendEndpointResponse403 | PostServicesHAProxyBackendEndpointResponse404 | PostServicesHAProxyBackendEndpointResponse405 | PostServicesHAProxyBackendEndpointResponse406 | PostServicesHAProxyBackendEndpointResponse409 | PostServicesHAProxyBackendEndpointResponse415 | PostServicesHAProxyBackendEndpointResponse422 | PostServicesHAProxyBackendEndpointResponse424 | PostServicesHAProxyBackendEndpointResponse500 | PostServicesHAProxyBackendEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendEndpointJsonBody | PostServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendEndpointResponse400
    | PostServicesHAProxyBackendEndpointResponse401
    | PostServicesHAProxyBackendEndpointResponse403
    | PostServicesHAProxyBackendEndpointResponse404
    | PostServicesHAProxyBackendEndpointResponse405
    | PostServicesHAProxyBackendEndpointResponse406
    | PostServicesHAProxyBackendEndpointResponse409
    | PostServicesHAProxyBackendEndpointResponse415
    | PostServicesHAProxyBackendEndpointResponse422
    | PostServicesHAProxyBackendEndpointResponse424
    | PostServicesHAProxyBackendEndpointResponse500
    | PostServicesHAProxyBackendEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendEndpointResponse400 | PostServicesHAProxyBackendEndpointResponse401 | PostServicesHAProxyBackendEndpointResponse403 | PostServicesHAProxyBackendEndpointResponse404 | PostServicesHAProxyBackendEndpointResponse405 | PostServicesHAProxyBackendEndpointResponse406 | PostServicesHAProxyBackendEndpointResponse409 | PostServicesHAProxyBackendEndpointResponse415 | PostServicesHAProxyBackendEndpointResponse422 | PostServicesHAProxyBackendEndpointResponse424 | PostServicesHAProxyBackendEndpointResponse500 | PostServicesHAProxyBackendEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendEndpointJsonBody | PostServicesHAProxyBackendEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendEndpointResponse400
    | PostServicesHAProxyBackendEndpointResponse401
    | PostServicesHAProxyBackendEndpointResponse403
    | PostServicesHAProxyBackendEndpointResponse404
    | PostServicesHAProxyBackendEndpointResponse405
    | PostServicesHAProxyBackendEndpointResponse406
    | PostServicesHAProxyBackendEndpointResponse409
    | PostServicesHAProxyBackendEndpointResponse415
    | PostServicesHAProxyBackendEndpointResponse422
    | PostServicesHAProxyBackendEndpointResponse424
    | PostServicesHAProxyBackendEndpointResponse500
    | PostServicesHAProxyBackendEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackend<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-backend-post ]<br>**Required
    packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendEndpointResponse400 | PostServicesHAProxyBackendEndpointResponse401 | PostServicesHAProxyBackendEndpointResponse403 | PostServicesHAProxyBackendEndpointResponse404 | PostServicesHAProxyBackendEndpointResponse405 | PostServicesHAProxyBackendEndpointResponse406 | PostServicesHAProxyBackendEndpointResponse409 | PostServicesHAProxyBackendEndpointResponse415 | PostServicesHAProxyBackendEndpointResponse422 | PostServicesHAProxyBackendEndpointResponse424 | PostServicesHAProxyBackendEndpointResponse500 | PostServicesHAProxyBackendEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
