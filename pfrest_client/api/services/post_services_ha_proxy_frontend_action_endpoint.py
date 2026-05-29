from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_frontend_action_endpoint_data_body import (
    PostServicesHAProxyFrontendActionEndpointDataBody,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_json_body import (
    PostServicesHAProxyFrontendActionEndpointJsonBody,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_400 import (
    PostServicesHAProxyFrontendActionEndpointResponse400,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_401 import (
    PostServicesHAProxyFrontendActionEndpointResponse401,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_403 import (
    PostServicesHAProxyFrontendActionEndpointResponse403,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_404 import (
    PostServicesHAProxyFrontendActionEndpointResponse404,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_405 import (
    PostServicesHAProxyFrontendActionEndpointResponse405,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_406 import (
    PostServicesHAProxyFrontendActionEndpointResponse406,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_409 import (
    PostServicesHAProxyFrontendActionEndpointResponse409,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_415 import (
    PostServicesHAProxyFrontendActionEndpointResponse415,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_422 import (
    PostServicesHAProxyFrontendActionEndpointResponse422,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_424 import (
    PostServicesHAProxyFrontendActionEndpointResponse424,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_500 import (
    PostServicesHAProxyFrontendActionEndpointResponse500,
)
from ...models.post_services_ha_proxy_frontend_action_endpoint_response_503 import (
    PostServicesHAProxyFrontendActionEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxyFrontendActionEndpointJsonBody
    | PostServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/frontend/action",
    }

    if isinstance(body, PostServicesHAProxyFrontendActionEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxyFrontendActionEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxyFrontendActionEndpointResponse400
    | PostServicesHAProxyFrontendActionEndpointResponse401
    | PostServicesHAProxyFrontendActionEndpointResponse403
    | PostServicesHAProxyFrontendActionEndpointResponse404
    | PostServicesHAProxyFrontendActionEndpointResponse405
    | PostServicesHAProxyFrontendActionEndpointResponse406
    | PostServicesHAProxyFrontendActionEndpointResponse409
    | PostServicesHAProxyFrontendActionEndpointResponse415
    | PostServicesHAProxyFrontendActionEndpointResponse422
    | PostServicesHAProxyFrontendActionEndpointResponse424
    | PostServicesHAProxyFrontendActionEndpointResponse500
    | PostServicesHAProxyFrontendActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxyFrontendActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxyFrontendActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxyFrontendActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxyFrontendActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxyFrontendActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxyFrontendActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxyFrontendActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxyFrontendActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxyFrontendActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxyFrontendActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxyFrontendActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxyFrontendActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxyFrontendActionEndpointResponse400
    | PostServicesHAProxyFrontendActionEndpointResponse401
    | PostServicesHAProxyFrontendActionEndpointResponse403
    | PostServicesHAProxyFrontendActionEndpointResponse404
    | PostServicesHAProxyFrontendActionEndpointResponse405
    | PostServicesHAProxyFrontendActionEndpointResponse406
    | PostServicesHAProxyFrontendActionEndpointResponse409
    | PostServicesHAProxyFrontendActionEndpointResponse415
    | PostServicesHAProxyFrontendActionEndpointResponse422
    | PostServicesHAProxyFrontendActionEndpointResponse424
    | PostServicesHAProxyFrontendActionEndpointResponse500
    | PostServicesHAProxyFrontendActionEndpointResponse503
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
    body: PostServicesHAProxyFrontendActionEndpointJsonBody
    | PostServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyFrontendActionEndpointResponse400
    | PostServicesHAProxyFrontendActionEndpointResponse401
    | PostServicesHAProxyFrontendActionEndpointResponse403
    | PostServicesHAProxyFrontendActionEndpointResponse404
    | PostServicesHAProxyFrontendActionEndpointResponse405
    | PostServicesHAProxyFrontendActionEndpointResponse406
    | PostServicesHAProxyFrontendActionEndpointResponse409
    | PostServicesHAProxyFrontendActionEndpointResponse415
    | PostServicesHAProxyFrontendActionEndpointResponse422
    | PostServicesHAProxyFrontendActionEndpointResponse424
    | PostServicesHAProxyFrontendActionEndpointResponse500
    | PostServicesHAProxyFrontendActionEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Frontend Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontendAction<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-action-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendActionEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyFrontendActionEndpointResponse400 | PostServicesHAProxyFrontendActionEndpointResponse401 | PostServicesHAProxyFrontendActionEndpointResponse403 | PostServicesHAProxyFrontendActionEndpointResponse404 | PostServicesHAProxyFrontendActionEndpointResponse405 | PostServicesHAProxyFrontendActionEndpointResponse406 | PostServicesHAProxyFrontendActionEndpointResponse409 | PostServicesHAProxyFrontendActionEndpointResponse415 | PostServicesHAProxyFrontendActionEndpointResponse422 | PostServicesHAProxyFrontendActionEndpointResponse424 | PostServicesHAProxyFrontendActionEndpointResponse500 | PostServicesHAProxyFrontendActionEndpointResponse503]
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
    body: PostServicesHAProxyFrontendActionEndpointJsonBody
    | PostServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyFrontendActionEndpointResponse400
    | PostServicesHAProxyFrontendActionEndpointResponse401
    | PostServicesHAProxyFrontendActionEndpointResponse403
    | PostServicesHAProxyFrontendActionEndpointResponse404
    | PostServicesHAProxyFrontendActionEndpointResponse405
    | PostServicesHAProxyFrontendActionEndpointResponse406
    | PostServicesHAProxyFrontendActionEndpointResponse409
    | PostServicesHAProxyFrontendActionEndpointResponse415
    | PostServicesHAProxyFrontendActionEndpointResponse422
    | PostServicesHAProxyFrontendActionEndpointResponse424
    | PostServicesHAProxyFrontendActionEndpointResponse500
    | PostServicesHAProxyFrontendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Frontend Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontendAction<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-action-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendActionEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyFrontendActionEndpointResponse400 | PostServicesHAProxyFrontendActionEndpointResponse401 | PostServicesHAProxyFrontendActionEndpointResponse403 | PostServicesHAProxyFrontendActionEndpointResponse404 | PostServicesHAProxyFrontendActionEndpointResponse405 | PostServicesHAProxyFrontendActionEndpointResponse406 | PostServicesHAProxyFrontendActionEndpointResponse409 | PostServicesHAProxyFrontendActionEndpointResponse415 | PostServicesHAProxyFrontendActionEndpointResponse422 | PostServicesHAProxyFrontendActionEndpointResponse424 | PostServicesHAProxyFrontendActionEndpointResponse500 | PostServicesHAProxyFrontendActionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyFrontendActionEndpointJsonBody
    | PostServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxyFrontendActionEndpointResponse400
    | PostServicesHAProxyFrontendActionEndpointResponse401
    | PostServicesHAProxyFrontendActionEndpointResponse403
    | PostServicesHAProxyFrontendActionEndpointResponse404
    | PostServicesHAProxyFrontendActionEndpointResponse405
    | PostServicesHAProxyFrontendActionEndpointResponse406
    | PostServicesHAProxyFrontendActionEndpointResponse409
    | PostServicesHAProxyFrontendActionEndpointResponse415
    | PostServicesHAProxyFrontendActionEndpointResponse422
    | PostServicesHAProxyFrontendActionEndpointResponse424
    | PostServicesHAProxyFrontendActionEndpointResponse500
    | PostServicesHAProxyFrontendActionEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Frontend Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontendAction<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-action-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendActionEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxyFrontendActionEndpointResponse400 | PostServicesHAProxyFrontendActionEndpointResponse401 | PostServicesHAProxyFrontendActionEndpointResponse403 | PostServicesHAProxyFrontendActionEndpointResponse404 | PostServicesHAProxyFrontendActionEndpointResponse405 | PostServicesHAProxyFrontendActionEndpointResponse406 | PostServicesHAProxyFrontendActionEndpointResponse409 | PostServicesHAProxyFrontendActionEndpointResponse415 | PostServicesHAProxyFrontendActionEndpointResponse422 | PostServicesHAProxyFrontendActionEndpointResponse424 | PostServicesHAProxyFrontendActionEndpointResponse500 | PostServicesHAProxyFrontendActionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxyFrontendActionEndpointJsonBody
    | PostServicesHAProxyFrontendActionEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxyFrontendActionEndpointResponse400
    | PostServicesHAProxyFrontendActionEndpointResponse401
    | PostServicesHAProxyFrontendActionEndpointResponse403
    | PostServicesHAProxyFrontendActionEndpointResponse404
    | PostServicesHAProxyFrontendActionEndpointResponse405
    | PostServicesHAProxyFrontendActionEndpointResponse406
    | PostServicesHAProxyFrontendActionEndpointResponse409
    | PostServicesHAProxyFrontendActionEndpointResponse415
    | PostServicesHAProxyFrontendActionEndpointResponse422
    | PostServicesHAProxyFrontendActionEndpointResponse424
    | PostServicesHAProxyFrontendActionEndpointResponse500
    | PostServicesHAProxyFrontendActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Frontend Action.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyFrontendAction<br>**Parent model**:
    HAProxyFrontend<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    frontend-action-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies immediately**:
    No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxyFrontendActionEndpointJsonBody | Unset):
        body (PostServicesHAProxyFrontendActionEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxyFrontendActionEndpointResponse400 | PostServicesHAProxyFrontendActionEndpointResponse401 | PostServicesHAProxyFrontendActionEndpointResponse403 | PostServicesHAProxyFrontendActionEndpointResponse404 | PostServicesHAProxyFrontendActionEndpointResponse405 | PostServicesHAProxyFrontendActionEndpointResponse406 | PostServicesHAProxyFrontendActionEndpointResponse409 | PostServicesHAProxyFrontendActionEndpointResponse415 | PostServicesHAProxyFrontendActionEndpointResponse422 | PostServicesHAProxyFrontendActionEndpointResponse424 | PostServicesHAProxyFrontendActionEndpointResponse500 | PostServicesHAProxyFrontendActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
