from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_backend_action_endpoint_data_body import (
    PostServicesHAProxyBackendActionEndpointDataBody,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_json_body import (
    PostServicesHAProxyBackendActionEndpointJsonBody,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_400 import (
    PostServicesHAProxyBackendActionEndpointResponse400,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_401 import (
    PostServicesHAProxyBackendActionEndpointResponse401,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_403 import (
    PostServicesHAProxyBackendActionEndpointResponse403,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_404 import (
    PostServicesHAProxyBackendActionEndpointResponse404,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_405 import (
    PostServicesHAProxyBackendActionEndpointResponse405,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_406 import (
    PostServicesHAProxyBackendActionEndpointResponse406,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_409 import (
    PostServicesHAProxyBackendActionEndpointResponse409,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_415 import (
    PostServicesHAProxyBackendActionEndpointResponse415,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_422 import (
    PostServicesHAProxyBackendActionEndpointResponse422,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_424 import (
    PostServicesHAProxyBackendActionEndpointResponse424,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_500 import (
    PostServicesHAProxyBackendActionEndpointResponse500,
)
from ...models.post_services_ha_proxy_backend_action_endpoint_response_503 import (
    PostServicesHAProxyBackendActionEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyBackendActionEndpointJsonBody
    | PostServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/backend/action",
    }

    if isinstance(body, PostServicesHAProxyBackendActionEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyBackendActionEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyBackendActionEndpointResponse400
    | PostServicesHAProxyBackendActionEndpointResponse401
    | PostServicesHAProxyBackendActionEndpointResponse403
    | PostServicesHAProxyBackendActionEndpointResponse404
    | PostServicesHAProxyBackendActionEndpointResponse405
    | PostServicesHAProxyBackendActionEndpointResponse406
    | PostServicesHAProxyBackendActionEndpointResponse409
    | PostServicesHAProxyBackendActionEndpointResponse415
    | PostServicesHAProxyBackendActionEndpointResponse422
    | PostServicesHAProxyBackendActionEndpointResponse424
    | PostServicesHAProxyBackendActionEndpointResponse500
    | PostServicesHAProxyBackendActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyBackendActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyBackendActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyBackendActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyBackendActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyBackendActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyBackendActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyBackendActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyBackendActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyBackendActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyBackendActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyBackendActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyBackendActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyBackendActionEndpointResponse400
    | PostServicesHAProxyBackendActionEndpointResponse401
    | PostServicesHAProxyBackendActionEndpointResponse403
    | PostServicesHAProxyBackendActionEndpointResponse404
    | PostServicesHAProxyBackendActionEndpointResponse405
    | PostServicesHAProxyBackendActionEndpointResponse406
    | PostServicesHAProxyBackendActionEndpointResponse409
    | PostServicesHAProxyBackendActionEndpointResponse415
    | PostServicesHAProxyBackendActionEndpointResponse422
    | PostServicesHAProxyBackendActionEndpointResponse424
    | PostServicesHAProxyBackendActionEndpointResponse500
    | PostServicesHAProxyBackendActionEndpointResponse503
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
    body: PostServicesHAProxyBackendActionEndpointJsonBody
    | PostServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendActionEndpointResponse400
    | PostServicesHAProxyBackendActionEndpointResponse401
    | PostServicesHAProxyBackendActionEndpointResponse403
    | PostServicesHAProxyBackendActionEndpointResponse404
    | PostServicesHAProxyBackendActionEndpointResponse405
    | PostServicesHAProxyBackendActionEndpointResponse406
    | PostServicesHAProxyBackendActionEndpointResponse409
    | PostServicesHAProxyBackendActionEndpointResponse415
    | PostServicesHAProxyBackendActionEndpointResponse422
    | PostServicesHAProxyBackendActionEndpointResponse424
    | PostServicesHAProxyBackendActionEndpointResponse500
    | PostServicesHAProxyBackendActionEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendActionEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendActionEndpointResponse400 | PostServicesHAProxyBackendActionEndpointResponse401 | PostServicesHAProxyBackendActionEndpointResponse403 | PostServicesHAProxyBackendActionEndpointResponse404 | PostServicesHAProxyBackendActionEndpointResponse405 | PostServicesHAProxyBackendActionEndpointResponse406 | PostServicesHAProxyBackendActionEndpointResponse409 | PostServicesHAProxyBackendActionEndpointResponse415 | PostServicesHAProxyBackendActionEndpointResponse422 | PostServicesHAProxyBackendActionEndpointResponse424 | PostServicesHAProxyBackendActionEndpointResponse500 | PostServicesHAProxyBackendActionEndpointResponse503]
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
    body: PostServicesHAProxyBackendActionEndpointJsonBody
    | PostServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendActionEndpointResponse400
    | PostServicesHAProxyBackendActionEndpointResponse401
    | PostServicesHAProxyBackendActionEndpointResponse403
    | PostServicesHAProxyBackendActionEndpointResponse404
    | PostServicesHAProxyBackendActionEndpointResponse405
    | PostServicesHAProxyBackendActionEndpointResponse406
    | PostServicesHAProxyBackendActionEndpointResponse409
    | PostServicesHAProxyBackendActionEndpointResponse415
    | PostServicesHAProxyBackendActionEndpointResponse422
    | PostServicesHAProxyBackendActionEndpointResponse424
    | PostServicesHAProxyBackendActionEndpointResponse500
    | PostServicesHAProxyBackendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendActionEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendActionEndpointResponse400 | PostServicesHAProxyBackendActionEndpointResponse401 | PostServicesHAProxyBackendActionEndpointResponse403 | PostServicesHAProxyBackendActionEndpointResponse404 | PostServicesHAProxyBackendActionEndpointResponse405 | PostServicesHAProxyBackendActionEndpointResponse406 | PostServicesHAProxyBackendActionEndpointResponse409 | PostServicesHAProxyBackendActionEndpointResponse415 | PostServicesHAProxyBackendActionEndpointResponse422 | PostServicesHAProxyBackendActionEndpointResponse424 | PostServicesHAProxyBackendActionEndpointResponse500 | PostServicesHAProxyBackendActionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendActionEndpointJsonBody
    | PostServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyBackendActionEndpointResponse400
    | PostServicesHAProxyBackendActionEndpointResponse401
    | PostServicesHAProxyBackendActionEndpointResponse403
    | PostServicesHAProxyBackendActionEndpointResponse404
    | PostServicesHAProxyBackendActionEndpointResponse405
    | PostServicesHAProxyBackendActionEndpointResponse406
    | PostServicesHAProxyBackendActionEndpointResponse409
    | PostServicesHAProxyBackendActionEndpointResponse415
    | PostServicesHAProxyBackendActionEndpointResponse422
    | PostServicesHAProxyBackendActionEndpointResponse424
    | PostServicesHAProxyBackendActionEndpointResponse500
    | PostServicesHAProxyBackendActionEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendActionEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyBackendActionEndpointResponse400 | PostServicesHAProxyBackendActionEndpointResponse401 | PostServicesHAProxyBackendActionEndpointResponse403 | PostServicesHAProxyBackendActionEndpointResponse404 | PostServicesHAProxyBackendActionEndpointResponse405 | PostServicesHAProxyBackendActionEndpointResponse406 | PostServicesHAProxyBackendActionEndpointResponse409 | PostServicesHAProxyBackendActionEndpointResponse415 | PostServicesHAProxyBackendActionEndpointResponse422 | PostServicesHAProxyBackendActionEndpointResponse424 | PostServicesHAProxyBackendActionEndpointResponse500 | PostServicesHAProxyBackendActionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyBackendActionEndpointJsonBody
    | PostServicesHAProxyBackendActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyBackendActionEndpointResponse400
    | PostServicesHAProxyBackendActionEndpointResponse401
    | PostServicesHAProxyBackendActionEndpointResponse403
    | PostServicesHAProxyBackendActionEndpointResponse404
    | PostServicesHAProxyBackendActionEndpointResponse405
    | PostServicesHAProxyBackendActionEndpointResponse406
    | PostServicesHAProxyBackendActionEndpointResponse409
    | PostServicesHAProxyBackendActionEndpointResponse415
    | PostServicesHAProxyBackendActionEndpointResponse422
    | PostServicesHAProxyBackendActionEndpointResponse424
    | PostServicesHAProxyBackendActionEndpointResponse500
    | PostServicesHAProxyBackendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Backend Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyBackendAction<br>**Parent model**:
    HAProxyBackend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    backend-action-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyBackendActionEndpointJsonBody | Unset):
        body (PostServicesHAProxyBackendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyBackendActionEndpointResponse400 | PostServicesHAProxyBackendActionEndpointResponse401 | PostServicesHAProxyBackendActionEndpointResponse403 | PostServicesHAProxyBackendActionEndpointResponse404 | PostServicesHAProxyBackendActionEndpointResponse405 | PostServicesHAProxyBackendActionEndpointResponse406 | PostServicesHAProxyBackendActionEndpointResponse409 | PostServicesHAProxyBackendActionEndpointResponse415 | PostServicesHAProxyBackendActionEndpointResponse422 | PostServicesHAProxyBackendActionEndpointResponse424 | PostServicesHAProxyBackendActionEndpointResponse500 | PostServicesHAProxyBackendActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
