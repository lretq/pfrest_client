from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_backend_error_file_endpoint_data_body import (
    PostServicesHAProxyBackendErrorFileEndpointDataBody,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_json_body import (
    PostServicesHAProxyBackendErrorFileEndpointJsonBody,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_400 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse400,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_401 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse401,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_403 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse403,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_404 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse404,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_405 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse405,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_406 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse406,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_409 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse409,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_415 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse415,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_422 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse422,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_424 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse424,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_500 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse500,
)
from ...models.post_services_ha_proxy_backend_error_file_endpoint_response_503 import (
    PostServicesHAProxyBackendErrorFileEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyBackendErrorFileEndpointJsonBody
    | PostServicesHAProxyBackendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/backend/error_file",
    }

    if isinstance(body, PostServicesHAProxyBackendErrorFileEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyBackendErrorFileEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyBackendErrorFileEndpointResponse400
    | PostServicesHAProxyBackendErrorFileEndpointResponse401
    | PostServicesHAProxyBackendErrorFileEndpointResponse403
    | PostServicesHAProxyBackendErrorFileEndpointResponse404
    | PostServicesHAProxyBackendErrorFileEndpointResponse405
    | PostServicesHAProxyBackendErrorFileEndpointResponse406
    | PostServicesHAProxyBackendErrorFileEndpointResponse409
    | PostServicesHAProxyBackendErrorFileEndpointResponse415
    | PostServicesHAProxyBackendErrorFileEndpointResponse422
    | PostServicesHAProxyBackendErrorFileEndpointResponse424
    | PostServicesHAProxyBackendErrorFileEndpointResponse500
    | PostServicesHAProxyBackendErrorFileEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyBackendErrorFileEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyBackendErrorFileEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyBackendErrorFileEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyBackendErrorFileEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyBackendErrorFileEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyBackendErrorFileEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyBackendErrorFileEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyBackendErrorFileEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyBackendErrorFileEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyBackendErrorFileEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyBackendErrorFileEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyBackendErrorFileEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyBackendErrorFileEndpointResponse400
    | PostServicesHAProxyBackendErrorFileEndpointResponse401
    | PostServicesHAProxyBackendErrorFileEndpointResponse403
    | PostServicesHAProxyBackendErrorFileEndpointResponse404
    | PostServicesHAProxyBackendErrorFileEndpointResponse405
    | PostServicesHAProxyBackendErrorFileEndpointResponse406
    | PostServicesHAProxyBackendErrorFileEndpointResponse409
    | PostServicesHAProxyBackendErrorFileEndpointResponse415
    | PostServicesHAProxyBackendErrorFileEndpointResponse422
    | PostServicesHAProxyBackendErrorFileEndpointResponse424
    | PostServicesHAProxyBackendErrorFileEndpointResponse500
    | PostServicesHAProxyBackendErrorFileEndpointResponse503
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
    body: PostServicesHAProxyBackendErrorFileEndpointJsonBody
    | PostServicesHAProxyBackendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendErrorFileEndpointResponse400
    | PostServicesHAProxyBackendErrorFileEndpointResponse401
    | PostServicesHAProxyBackendErrorFileEndpointResponse403
    | PostServicesHAProxyBackendErrorFileEndpointResponse404
    | PostServicesHAProxyBackendErrorFileEndpointResponse405
    | PostServicesHAProxyBackendErrorFileEndpointResponse406
    | PostServicesHAProxyBackendErrorFileEndpointResponse409
    | PostServicesHAProxyBackendErrorFileEndpointResponse415
    | PostServicesHAProxyBackendErrorFileEndpointResponse422
    | PostServicesHAProxyBackendErrorFileEndpointResponse424
    | PostServicesHAProxyBackendErrorFileEndpointResponse500
    | PostServicesHAProxyBackendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendErrorFile<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-error-file-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendErrorFileEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendErrorFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendErrorFileEndpointResponse400 | PostServicesHAProxyBackendErrorFileEndpointResponse401 | PostServicesHAProxyBackendErrorFileEndpointResponse403 | PostServicesHAProxyBackendErrorFileEndpointResponse404 | PostServicesHAProxyBackendErrorFileEndpointResponse405 | PostServicesHAProxyBackendErrorFileEndpointResponse406 | PostServicesHAProxyBackendErrorFileEndpointResponse409 | PostServicesHAProxyBackendErrorFileEndpointResponse415 | PostServicesHAProxyBackendErrorFileEndpointResponse422 | PostServicesHAProxyBackendErrorFileEndpointResponse424 | PostServicesHAProxyBackendErrorFileEndpointResponse500 | PostServicesHAProxyBackendErrorFileEndpointResponse503]
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
    body: PostServicesHAProxyBackendErrorFileEndpointJsonBody
    | PostServicesHAProxyBackendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendErrorFileEndpointResponse400
    | PostServicesHAProxyBackendErrorFileEndpointResponse401
    | PostServicesHAProxyBackendErrorFileEndpointResponse403
    | PostServicesHAProxyBackendErrorFileEndpointResponse404
    | PostServicesHAProxyBackendErrorFileEndpointResponse405
    | PostServicesHAProxyBackendErrorFileEndpointResponse406
    | PostServicesHAProxyBackendErrorFileEndpointResponse409
    | PostServicesHAProxyBackendErrorFileEndpointResponse415
    | PostServicesHAProxyBackendErrorFileEndpointResponse422
    | PostServicesHAProxyBackendErrorFileEndpointResponse424
    | PostServicesHAProxyBackendErrorFileEndpointResponse500
    | PostServicesHAProxyBackendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendErrorFile<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-error-file-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendErrorFileEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendErrorFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendErrorFileEndpointResponse400 | PostServicesHAProxyBackendErrorFileEndpointResponse401 | PostServicesHAProxyBackendErrorFileEndpointResponse403 | PostServicesHAProxyBackendErrorFileEndpointResponse404 | PostServicesHAProxyBackendErrorFileEndpointResponse405 | PostServicesHAProxyBackendErrorFileEndpointResponse406 | PostServicesHAProxyBackendErrorFileEndpointResponse409 | PostServicesHAProxyBackendErrorFileEndpointResponse415 | PostServicesHAProxyBackendErrorFileEndpointResponse422 | PostServicesHAProxyBackendErrorFileEndpointResponse424 | PostServicesHAProxyBackendErrorFileEndpointResponse500 | PostServicesHAProxyBackendErrorFileEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendErrorFileEndpointJsonBody
    | PostServicesHAProxyBackendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendErrorFileEndpointResponse400
    | PostServicesHAProxyBackendErrorFileEndpointResponse401
    | PostServicesHAProxyBackendErrorFileEndpointResponse403
    | PostServicesHAProxyBackendErrorFileEndpointResponse404
    | PostServicesHAProxyBackendErrorFileEndpointResponse405
    | PostServicesHAProxyBackendErrorFileEndpointResponse406
    | PostServicesHAProxyBackendErrorFileEndpointResponse409
    | PostServicesHAProxyBackendErrorFileEndpointResponse415
    | PostServicesHAProxyBackendErrorFileEndpointResponse422
    | PostServicesHAProxyBackendErrorFileEndpointResponse424
    | PostServicesHAProxyBackendErrorFileEndpointResponse500
    | PostServicesHAProxyBackendErrorFileEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendErrorFile<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-error-file-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendErrorFileEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendErrorFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendErrorFileEndpointResponse400 | PostServicesHAProxyBackendErrorFileEndpointResponse401 | PostServicesHAProxyBackendErrorFileEndpointResponse403 | PostServicesHAProxyBackendErrorFileEndpointResponse404 | PostServicesHAProxyBackendErrorFileEndpointResponse405 | PostServicesHAProxyBackendErrorFileEndpointResponse406 | PostServicesHAProxyBackendErrorFileEndpointResponse409 | PostServicesHAProxyBackendErrorFileEndpointResponse415 | PostServicesHAProxyBackendErrorFileEndpointResponse422 | PostServicesHAProxyBackendErrorFileEndpointResponse424 | PostServicesHAProxyBackendErrorFileEndpointResponse500 | PostServicesHAProxyBackendErrorFileEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendErrorFileEndpointJsonBody
    | PostServicesHAProxyBackendErrorFileEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendErrorFileEndpointResponse400
    | PostServicesHAProxyBackendErrorFileEndpointResponse401
    | PostServicesHAProxyBackendErrorFileEndpointResponse403
    | PostServicesHAProxyBackendErrorFileEndpointResponse404
    | PostServicesHAProxyBackendErrorFileEndpointResponse405
    | PostServicesHAProxyBackendErrorFileEndpointResponse406
    | PostServicesHAProxyBackendErrorFileEndpointResponse409
    | PostServicesHAProxyBackendErrorFileEndpointResponse415
    | PostServicesHAProxyBackendErrorFileEndpointResponse422
    | PostServicesHAProxyBackendErrorFileEndpointResponse424
    | PostServicesHAProxyBackendErrorFileEndpointResponse500
    | PostServicesHAProxyBackendErrorFileEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend Error File.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: HAProxyBackendErrorFile<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-error-file-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendErrorFileEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendErrorFileEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendErrorFileEndpointResponse400 | PostServicesHAProxyBackendErrorFileEndpointResponse401 | PostServicesHAProxyBackendErrorFileEndpointResponse403 | PostServicesHAProxyBackendErrorFileEndpointResponse404 | PostServicesHAProxyBackendErrorFileEndpointResponse405 | PostServicesHAProxyBackendErrorFileEndpointResponse406 | PostServicesHAProxyBackendErrorFileEndpointResponse409 | PostServicesHAProxyBackendErrorFileEndpointResponse415 | PostServicesHAProxyBackendErrorFileEndpointResponse422 | PostServicesHAProxyBackendErrorFileEndpointResponse424 | PostServicesHAProxyBackendErrorFileEndpointResponse500 | PostServicesHAProxyBackendErrorFileEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
