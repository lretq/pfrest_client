from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_backend_acl_endpoint_data_body import (
    PostServicesHAProxyBackendACLEndpointDataBody,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_json_body import (
    PostServicesHAProxyBackendACLEndpointJsonBody,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_400 import (
    PostServicesHAProxyBackendACLEndpointResponse400,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_401 import (
    PostServicesHAProxyBackendACLEndpointResponse401,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_403 import (
    PostServicesHAProxyBackendACLEndpointResponse403,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_404 import (
    PostServicesHAProxyBackendACLEndpointResponse404,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_405 import (
    PostServicesHAProxyBackendACLEndpointResponse405,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_406 import (
    PostServicesHAProxyBackendACLEndpointResponse406,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_409 import (
    PostServicesHAProxyBackendACLEndpointResponse409,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_415 import (
    PostServicesHAProxyBackendACLEndpointResponse415,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_422 import (
    PostServicesHAProxyBackendACLEndpointResponse422,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_424 import (
    PostServicesHAProxyBackendACLEndpointResponse424,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_500 import (
    PostServicesHAProxyBackendACLEndpointResponse500,
)
from ...models.post_services_ha_proxy_backend_acl_endpoint_response_503 import (
    PostServicesHAProxyBackendACLEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyBackendACLEndpointJsonBody | PostServicesHAProxyBackendACLEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/backend/acl",
    }

    if isinstance(body, PostServicesHAProxyBackendACLEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyBackendACLEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyBackendACLEndpointResponse400
    | PostServicesHAProxyBackendACLEndpointResponse401
    | PostServicesHAProxyBackendACLEndpointResponse403
    | PostServicesHAProxyBackendACLEndpointResponse404
    | PostServicesHAProxyBackendACLEndpointResponse405
    | PostServicesHAProxyBackendACLEndpointResponse406
    | PostServicesHAProxyBackendACLEndpointResponse409
    | PostServicesHAProxyBackendACLEndpointResponse415
    | PostServicesHAProxyBackendACLEndpointResponse422
    | PostServicesHAProxyBackendACLEndpointResponse424
    | PostServicesHAProxyBackendACLEndpointResponse500
    | PostServicesHAProxyBackendACLEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyBackendACLEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyBackendACLEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyBackendACLEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyBackendACLEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyBackendACLEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyBackendACLEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyBackendACLEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyBackendACLEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyBackendACLEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyBackendACLEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyBackendACLEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyBackendACLEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyBackendACLEndpointResponse400
    | PostServicesHAProxyBackendACLEndpointResponse401
    | PostServicesHAProxyBackendACLEndpointResponse403
    | PostServicesHAProxyBackendACLEndpointResponse404
    | PostServicesHAProxyBackendACLEndpointResponse405
    | PostServicesHAProxyBackendACLEndpointResponse406
    | PostServicesHAProxyBackendACLEndpointResponse409
    | PostServicesHAProxyBackendACLEndpointResponse415
    | PostServicesHAProxyBackendACLEndpointResponse422
    | PostServicesHAProxyBackendACLEndpointResponse424
    | PostServicesHAProxyBackendACLEndpointResponse500
    | PostServicesHAProxyBackendACLEndpointResponse503
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
    body: PostServicesHAProxyBackendACLEndpointJsonBody | PostServicesHAProxyBackendACLEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendACLEndpointResponse400
    | PostServicesHAProxyBackendACLEndpointResponse401
    | PostServicesHAProxyBackendACLEndpointResponse403
    | PostServicesHAProxyBackendACLEndpointResponse404
    | PostServicesHAProxyBackendACLEndpointResponse405
    | PostServicesHAProxyBackendACLEndpointResponse406
    | PostServicesHAProxyBackendACLEndpointResponse409
    | PostServicesHAProxyBackendACLEndpointResponse415
    | PostServicesHAProxyBackendACLEndpointResponse422
    | PostServicesHAProxyBackendACLEndpointResponse424
    | PostServicesHAProxyBackendACLEndpointResponse500
    | PostServicesHAProxyBackendACLEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyBackendACL<br>**Parent model**: HAProxyBackend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-backend-acl-post ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendACLEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendACLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendACLEndpointResponse400 | PostServicesHAProxyBackendACLEndpointResponse401 | PostServicesHAProxyBackendACLEndpointResponse403 | PostServicesHAProxyBackendACLEndpointResponse404 | PostServicesHAProxyBackendACLEndpointResponse405 | PostServicesHAProxyBackendACLEndpointResponse406 | PostServicesHAProxyBackendACLEndpointResponse409 | PostServicesHAProxyBackendACLEndpointResponse415 | PostServicesHAProxyBackendACLEndpointResponse422 | PostServicesHAProxyBackendACLEndpointResponse424 | PostServicesHAProxyBackendACLEndpointResponse500 | PostServicesHAProxyBackendACLEndpointResponse503]
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
    body: PostServicesHAProxyBackendACLEndpointJsonBody | PostServicesHAProxyBackendACLEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendACLEndpointResponse400
    | PostServicesHAProxyBackendACLEndpointResponse401
    | PostServicesHAProxyBackendACLEndpointResponse403
    | PostServicesHAProxyBackendACLEndpointResponse404
    | PostServicesHAProxyBackendACLEndpointResponse405
    | PostServicesHAProxyBackendACLEndpointResponse406
    | PostServicesHAProxyBackendACLEndpointResponse409
    | PostServicesHAProxyBackendACLEndpointResponse415
    | PostServicesHAProxyBackendACLEndpointResponse422
    | PostServicesHAProxyBackendACLEndpointResponse424
    | PostServicesHAProxyBackendACLEndpointResponse500
    | PostServicesHAProxyBackendACLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyBackendACL<br>**Parent model**: HAProxyBackend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-backend-acl-post ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendACLEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendACLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendACLEndpointResponse400 | PostServicesHAProxyBackendACLEndpointResponse401 | PostServicesHAProxyBackendACLEndpointResponse403 | PostServicesHAProxyBackendACLEndpointResponse404 | PostServicesHAProxyBackendACLEndpointResponse405 | PostServicesHAProxyBackendACLEndpointResponse406 | PostServicesHAProxyBackendACLEndpointResponse409 | PostServicesHAProxyBackendACLEndpointResponse415 | PostServicesHAProxyBackendACLEndpointResponse422 | PostServicesHAProxyBackendACLEndpointResponse424 | PostServicesHAProxyBackendACLEndpointResponse500 | PostServicesHAProxyBackendACLEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendACLEndpointJsonBody | PostServicesHAProxyBackendACLEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendACLEndpointResponse400
    | PostServicesHAProxyBackendACLEndpointResponse401
    | PostServicesHAProxyBackendACLEndpointResponse403
    | PostServicesHAProxyBackendACLEndpointResponse404
    | PostServicesHAProxyBackendACLEndpointResponse405
    | PostServicesHAProxyBackendACLEndpointResponse406
    | PostServicesHAProxyBackendACLEndpointResponse409
    | PostServicesHAProxyBackendACLEndpointResponse415
    | PostServicesHAProxyBackendACLEndpointResponse422
    | PostServicesHAProxyBackendACLEndpointResponse424
    | PostServicesHAProxyBackendACLEndpointResponse500
    | PostServicesHAProxyBackendACLEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyBackendACL<br>**Parent model**: HAProxyBackend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-backend-acl-post ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendACLEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendACLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendACLEndpointResponse400 | PostServicesHAProxyBackendACLEndpointResponse401 | PostServicesHAProxyBackendACLEndpointResponse403 | PostServicesHAProxyBackendACLEndpointResponse404 | PostServicesHAProxyBackendACLEndpointResponse405 | PostServicesHAProxyBackendACLEndpointResponse406 | PostServicesHAProxyBackendACLEndpointResponse409 | PostServicesHAProxyBackendACLEndpointResponse415 | PostServicesHAProxyBackendACLEndpointResponse422 | PostServicesHAProxyBackendACLEndpointResponse424 | PostServicesHAProxyBackendACLEndpointResponse500 | PostServicesHAProxyBackendACLEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendACLEndpointJsonBody | PostServicesHAProxyBackendACLEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendACLEndpointResponse400
    | PostServicesHAProxyBackendACLEndpointResponse401
    | PostServicesHAProxyBackendACLEndpointResponse403
    | PostServicesHAProxyBackendACLEndpointResponse404
    | PostServicesHAProxyBackendACLEndpointResponse405
    | PostServicesHAProxyBackendACLEndpointResponse406
    | PostServicesHAProxyBackendACLEndpointResponse409
    | PostServicesHAProxyBackendACLEndpointResponse415
    | PostServicesHAProxyBackendACLEndpointResponse422
    | PostServicesHAProxyBackendACLEndpointResponse424
    | PostServicesHAProxyBackendACLEndpointResponse500
    | PostServicesHAProxyBackendACLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend Access Control
    List.<br><h3>Details:</h3>**Endpoint type**: Singular<br>**Associated model**:
    HAProxyBackendACL<br>**Parent model**: HAProxyBackend<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-haproxy-backend-acl-post ]<br>**Required packages**: [
    pfSense-pkg-haproxy ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendACLEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendACLEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendACLEndpointResponse400 | PostServicesHAProxyBackendACLEndpointResponse401 | PostServicesHAProxyBackendACLEndpointResponse403 | PostServicesHAProxyBackendACLEndpointResponse404 | PostServicesHAProxyBackendACLEndpointResponse405 | PostServicesHAProxyBackendACLEndpointResponse406 | PostServicesHAProxyBackendACLEndpointResponse409 | PostServicesHAProxyBackendACLEndpointResponse415 | PostServicesHAProxyBackendACLEndpointResponse422 | PostServicesHAProxyBackendACLEndpointResponse424 | PostServicesHAProxyBackendACLEndpointResponse500 | PostServicesHAProxyBackendACLEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
