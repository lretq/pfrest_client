from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_backend_server_endpoint_data_body import (
    PostServicesHAProxyBackendServerEndpointDataBody,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_json_body import (
    PostServicesHAProxyBackendServerEndpointJsonBody,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_400 import (
    PostServicesHAProxyBackendServerEndpointResponse400,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_401 import (
    PostServicesHAProxyBackendServerEndpointResponse401,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_403 import (
    PostServicesHAProxyBackendServerEndpointResponse403,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_404 import (
    PostServicesHAProxyBackendServerEndpointResponse404,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_405 import (
    PostServicesHAProxyBackendServerEndpointResponse405,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_406 import (
    PostServicesHAProxyBackendServerEndpointResponse406,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_409 import (
    PostServicesHAProxyBackendServerEndpointResponse409,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_415 import (
    PostServicesHAProxyBackendServerEndpointResponse415,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_422 import (
    PostServicesHAProxyBackendServerEndpointResponse422,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_424 import (
    PostServicesHAProxyBackendServerEndpointResponse424,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_500 import (
    PostServicesHAProxyBackendServerEndpointResponse500,
)
from ...models.post_services_ha_proxy_backend_server_endpoint_response_503 import (
    PostServicesHAProxyBackendServerEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyBackendServerEndpointJsonBody
    | PostServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/backend/server",
    }

    if isinstance(body, PostServicesHAProxyBackendServerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyBackendServerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyBackendServerEndpointResponse400
    | PostServicesHAProxyBackendServerEndpointResponse401
    | PostServicesHAProxyBackendServerEndpointResponse403
    | PostServicesHAProxyBackendServerEndpointResponse404
    | PostServicesHAProxyBackendServerEndpointResponse405
    | PostServicesHAProxyBackendServerEndpointResponse406
    | PostServicesHAProxyBackendServerEndpointResponse409
    | PostServicesHAProxyBackendServerEndpointResponse415
    | PostServicesHAProxyBackendServerEndpointResponse422
    | PostServicesHAProxyBackendServerEndpointResponse424
    | PostServicesHAProxyBackendServerEndpointResponse500
    | PostServicesHAProxyBackendServerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyBackendServerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyBackendServerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyBackendServerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyBackendServerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyBackendServerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyBackendServerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyBackendServerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyBackendServerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyBackendServerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyBackendServerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyBackendServerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyBackendServerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyBackendServerEndpointResponse400
    | PostServicesHAProxyBackendServerEndpointResponse401
    | PostServicesHAProxyBackendServerEndpointResponse403
    | PostServicesHAProxyBackendServerEndpointResponse404
    | PostServicesHAProxyBackendServerEndpointResponse405
    | PostServicesHAProxyBackendServerEndpointResponse406
    | PostServicesHAProxyBackendServerEndpointResponse409
    | PostServicesHAProxyBackendServerEndpointResponse415
    | PostServicesHAProxyBackendServerEndpointResponse422
    | PostServicesHAProxyBackendServerEndpointResponse424
    | PostServicesHAProxyBackendServerEndpointResponse500
    | PostServicesHAProxyBackendServerEndpointResponse503
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
    body: PostServicesHAProxyBackendServerEndpointJsonBody
    | PostServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendServerEndpointResponse400
    | PostServicesHAProxyBackendServerEndpointResponse401
    | PostServicesHAProxyBackendServerEndpointResponse403
    | PostServicesHAProxyBackendServerEndpointResponse404
    | PostServicesHAProxyBackendServerEndpointResponse405
    | PostServicesHAProxyBackendServerEndpointResponse406
    | PostServicesHAProxyBackendServerEndpointResponse409
    | PostServicesHAProxyBackendServerEndpointResponse415
    | PostServicesHAProxyBackendServerEndpointResponse422
    | PostServicesHAProxyBackendServerEndpointResponse424
    | PostServicesHAProxyBackendServerEndpointResponse500
    | PostServicesHAProxyBackendServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendServerEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendServerEndpointResponse400 | PostServicesHAProxyBackendServerEndpointResponse401 | PostServicesHAProxyBackendServerEndpointResponse403 | PostServicesHAProxyBackendServerEndpointResponse404 | PostServicesHAProxyBackendServerEndpointResponse405 | PostServicesHAProxyBackendServerEndpointResponse406 | PostServicesHAProxyBackendServerEndpointResponse409 | PostServicesHAProxyBackendServerEndpointResponse415 | PostServicesHAProxyBackendServerEndpointResponse422 | PostServicesHAProxyBackendServerEndpointResponse424 | PostServicesHAProxyBackendServerEndpointResponse500 | PostServicesHAProxyBackendServerEndpointResponse503]
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
    body: PostServicesHAProxyBackendServerEndpointJsonBody
    | PostServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendServerEndpointResponse400
    | PostServicesHAProxyBackendServerEndpointResponse401
    | PostServicesHAProxyBackendServerEndpointResponse403
    | PostServicesHAProxyBackendServerEndpointResponse404
    | PostServicesHAProxyBackendServerEndpointResponse405
    | PostServicesHAProxyBackendServerEndpointResponse406
    | PostServicesHAProxyBackendServerEndpointResponse409
    | PostServicesHAProxyBackendServerEndpointResponse415
    | PostServicesHAProxyBackendServerEndpointResponse422
    | PostServicesHAProxyBackendServerEndpointResponse424
    | PostServicesHAProxyBackendServerEndpointResponse500
    | PostServicesHAProxyBackendServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendServerEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendServerEndpointResponse400 | PostServicesHAProxyBackendServerEndpointResponse401 | PostServicesHAProxyBackendServerEndpointResponse403 | PostServicesHAProxyBackendServerEndpointResponse404 | PostServicesHAProxyBackendServerEndpointResponse405 | PostServicesHAProxyBackendServerEndpointResponse406 | PostServicesHAProxyBackendServerEndpointResponse409 | PostServicesHAProxyBackendServerEndpointResponse415 | PostServicesHAProxyBackendServerEndpointResponse422 | PostServicesHAProxyBackendServerEndpointResponse424 | PostServicesHAProxyBackendServerEndpointResponse500 | PostServicesHAProxyBackendServerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendServerEndpointJsonBody
    | PostServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendServerEndpointResponse400
    | PostServicesHAProxyBackendServerEndpointResponse401
    | PostServicesHAProxyBackendServerEndpointResponse403
    | PostServicesHAProxyBackendServerEndpointResponse404
    | PostServicesHAProxyBackendServerEndpointResponse405
    | PostServicesHAProxyBackendServerEndpointResponse406
    | PostServicesHAProxyBackendServerEndpointResponse409
    | PostServicesHAProxyBackendServerEndpointResponse415
    | PostServicesHAProxyBackendServerEndpointResponse422
    | PostServicesHAProxyBackendServerEndpointResponse424
    | PostServicesHAProxyBackendServerEndpointResponse500
    | PostServicesHAProxyBackendServerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendServerEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendServerEndpointResponse400 | PostServicesHAProxyBackendServerEndpointResponse401 | PostServicesHAProxyBackendServerEndpointResponse403 | PostServicesHAProxyBackendServerEndpointResponse404 | PostServicesHAProxyBackendServerEndpointResponse405 | PostServicesHAProxyBackendServerEndpointResponse406 | PostServicesHAProxyBackendServerEndpointResponse409 | PostServicesHAProxyBackendServerEndpointResponse415 | PostServicesHAProxyBackendServerEndpointResponse422 | PostServicesHAProxyBackendServerEndpointResponse424 | PostServicesHAProxyBackendServerEndpointResponse500 | PostServicesHAProxyBackendServerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendServerEndpointJsonBody
    | PostServicesHAProxyBackendServerEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendServerEndpointResponse400
    | PostServicesHAProxyBackendServerEndpointResponse401
    | PostServicesHAProxyBackendServerEndpointResponse403
    | PostServicesHAProxyBackendServerEndpointResponse404
    | PostServicesHAProxyBackendServerEndpointResponse405
    | PostServicesHAProxyBackendServerEndpointResponse406
    | PostServicesHAProxyBackendServerEndpointResponse409
    | PostServicesHAProxyBackendServerEndpointResponse415
    | PostServicesHAProxyBackendServerEndpointResponse422
    | PostServicesHAProxyBackendServerEndpointResponse424
    | PostServicesHAProxyBackendServerEndpointResponse500
    | PostServicesHAProxyBackendServerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend Server.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackendServer<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-server-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendServerEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendServerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendServerEndpointResponse400 | PostServicesHAProxyBackendServerEndpointResponse401 | PostServicesHAProxyBackendServerEndpointResponse403 | PostServicesHAProxyBackendServerEndpointResponse404 | PostServicesHAProxyBackendServerEndpointResponse405 | PostServicesHAProxyBackendServerEndpointResponse406 | PostServicesHAProxyBackendServerEndpointResponse409 | PostServicesHAProxyBackendServerEndpointResponse415 | PostServicesHAProxyBackendServerEndpointResponse422 | PostServicesHAProxyBackendServerEndpointResponse424 | PostServicesHAProxyBackendServerEndpointResponse500 | PostServicesHAProxyBackendServerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
