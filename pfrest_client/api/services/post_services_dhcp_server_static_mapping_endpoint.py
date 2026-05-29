from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dhcp_server_static_mapping_endpoint_data_body import (
    PostServicesDHCPServerStaticMappingEndpointDataBody,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_json_body import (
    PostServicesDHCPServerStaticMappingEndpointJsonBody,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_400 import (
    PostServicesDHCPServerStaticMappingEndpointResponse400,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_401 import (
    PostServicesDHCPServerStaticMappingEndpointResponse401,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_403 import (
    PostServicesDHCPServerStaticMappingEndpointResponse403,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_404 import (
    PostServicesDHCPServerStaticMappingEndpointResponse404,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_405 import (
    PostServicesDHCPServerStaticMappingEndpointResponse405,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_406 import (
    PostServicesDHCPServerStaticMappingEndpointResponse406,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_409 import (
    PostServicesDHCPServerStaticMappingEndpointResponse409,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_415 import (
    PostServicesDHCPServerStaticMappingEndpointResponse415,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_422 import (
    PostServicesDHCPServerStaticMappingEndpointResponse422,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_424 import (
    PostServicesDHCPServerStaticMappingEndpointResponse424,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_500 import (
    PostServicesDHCPServerStaticMappingEndpointResponse500,
)
from ...models.post_services_dhcp_server_static_mapping_endpoint_response_503 import (
    PostServicesDHCPServerStaticMappingEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDHCPServerStaticMappingEndpointJsonBody
    | PostServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dhcp_server/static_mapping",
    }

    if isinstance(body, PostServicesDHCPServerStaticMappingEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDHCPServerStaticMappingEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDHCPServerStaticMappingEndpointResponse400
    | PostServicesDHCPServerStaticMappingEndpointResponse401
    | PostServicesDHCPServerStaticMappingEndpointResponse403
    | PostServicesDHCPServerStaticMappingEndpointResponse404
    | PostServicesDHCPServerStaticMappingEndpointResponse405
    | PostServicesDHCPServerStaticMappingEndpointResponse406
    | PostServicesDHCPServerStaticMappingEndpointResponse409
    | PostServicesDHCPServerStaticMappingEndpointResponse415
    | PostServicesDHCPServerStaticMappingEndpointResponse422
    | PostServicesDHCPServerStaticMappingEndpointResponse424
    | PostServicesDHCPServerStaticMappingEndpointResponse500
    | PostServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDHCPServerStaticMappingEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDHCPServerStaticMappingEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDHCPServerStaticMappingEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDHCPServerStaticMappingEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDHCPServerStaticMappingEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDHCPServerStaticMappingEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDHCPServerStaticMappingEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDHCPServerStaticMappingEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDHCPServerStaticMappingEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDHCPServerStaticMappingEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDHCPServerStaticMappingEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDHCPServerStaticMappingEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDHCPServerStaticMappingEndpointResponse400
    | PostServicesDHCPServerStaticMappingEndpointResponse401
    | PostServicesDHCPServerStaticMappingEndpointResponse403
    | PostServicesDHCPServerStaticMappingEndpointResponse404
    | PostServicesDHCPServerStaticMappingEndpointResponse405
    | PostServicesDHCPServerStaticMappingEndpointResponse406
    | PostServicesDHCPServerStaticMappingEndpointResponse409
    | PostServicesDHCPServerStaticMappingEndpointResponse415
    | PostServicesDHCPServerStaticMappingEndpointResponse422
    | PostServicesDHCPServerStaticMappingEndpointResponse424
    | PostServicesDHCPServerStaticMappingEndpointResponse500
    | PostServicesDHCPServerStaticMappingEndpointResponse503
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
    body: PostServicesDHCPServerStaticMappingEndpointJsonBody
    | PostServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDHCPServerStaticMappingEndpointResponse400
    | PostServicesDHCPServerStaticMappingEndpointResponse401
    | PostServicesDHCPServerStaticMappingEndpointResponse403
    | PostServicesDHCPServerStaticMappingEndpointResponse404
    | PostServicesDHCPServerStaticMappingEndpointResponse405
    | PostServicesDHCPServerStaticMappingEndpointResponse406
    | PostServicesDHCPServerStaticMappingEndpointResponse409
    | PostServicesDHCPServerStaticMappingEndpointResponse415
    | PostServicesDHCPServerStaticMappingEndpointResponse422
    | PostServicesDHCPServerStaticMappingEndpointResponse424
    | PostServicesDHCPServerStaticMappingEndpointResponse500
    | PostServicesDHCPServerStaticMappingEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDHCPServerStaticMappingEndpointJsonBody | Unset):
        body (PostServicesDHCPServerStaticMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDHCPServerStaticMappingEndpointResponse400 | PostServicesDHCPServerStaticMappingEndpointResponse401 | PostServicesDHCPServerStaticMappingEndpointResponse403 | PostServicesDHCPServerStaticMappingEndpointResponse404 | PostServicesDHCPServerStaticMappingEndpointResponse405 | PostServicesDHCPServerStaticMappingEndpointResponse406 | PostServicesDHCPServerStaticMappingEndpointResponse409 | PostServicesDHCPServerStaticMappingEndpointResponse415 | PostServicesDHCPServerStaticMappingEndpointResponse422 | PostServicesDHCPServerStaticMappingEndpointResponse424 | PostServicesDHCPServerStaticMappingEndpointResponse500 | PostServicesDHCPServerStaticMappingEndpointResponse503]
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
    body: PostServicesDHCPServerStaticMappingEndpointJsonBody
    | PostServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDHCPServerStaticMappingEndpointResponse400
    | PostServicesDHCPServerStaticMappingEndpointResponse401
    | PostServicesDHCPServerStaticMappingEndpointResponse403
    | PostServicesDHCPServerStaticMappingEndpointResponse404
    | PostServicesDHCPServerStaticMappingEndpointResponse405
    | PostServicesDHCPServerStaticMappingEndpointResponse406
    | PostServicesDHCPServerStaticMappingEndpointResponse409
    | PostServicesDHCPServerStaticMappingEndpointResponse415
    | PostServicesDHCPServerStaticMappingEndpointResponse422
    | PostServicesDHCPServerStaticMappingEndpointResponse424
    | PostServicesDHCPServerStaticMappingEndpointResponse500
    | PostServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDHCPServerStaticMappingEndpointJsonBody | Unset):
        body (PostServicesDHCPServerStaticMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDHCPServerStaticMappingEndpointResponse400 | PostServicesDHCPServerStaticMappingEndpointResponse401 | PostServicesDHCPServerStaticMappingEndpointResponse403 | PostServicesDHCPServerStaticMappingEndpointResponse404 | PostServicesDHCPServerStaticMappingEndpointResponse405 | PostServicesDHCPServerStaticMappingEndpointResponse406 | PostServicesDHCPServerStaticMappingEndpointResponse409 | PostServicesDHCPServerStaticMappingEndpointResponse415 | PostServicesDHCPServerStaticMappingEndpointResponse422 | PostServicesDHCPServerStaticMappingEndpointResponse424 | PostServicesDHCPServerStaticMappingEndpointResponse500 | PostServicesDHCPServerStaticMappingEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDHCPServerStaticMappingEndpointJsonBody
    | PostServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesDHCPServerStaticMappingEndpointResponse400
    | PostServicesDHCPServerStaticMappingEndpointResponse401
    | PostServicesDHCPServerStaticMappingEndpointResponse403
    | PostServicesDHCPServerStaticMappingEndpointResponse404
    | PostServicesDHCPServerStaticMappingEndpointResponse405
    | PostServicesDHCPServerStaticMappingEndpointResponse406
    | PostServicesDHCPServerStaticMappingEndpointResponse409
    | PostServicesDHCPServerStaticMappingEndpointResponse415
    | PostServicesDHCPServerStaticMappingEndpointResponse422
    | PostServicesDHCPServerStaticMappingEndpointResponse424
    | PostServicesDHCPServerStaticMappingEndpointResponse500
    | PostServicesDHCPServerStaticMappingEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDHCPServerStaticMappingEndpointJsonBody | Unset):
        body (PostServicesDHCPServerStaticMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDHCPServerStaticMappingEndpointResponse400 | PostServicesDHCPServerStaticMappingEndpointResponse401 | PostServicesDHCPServerStaticMappingEndpointResponse403 | PostServicesDHCPServerStaticMappingEndpointResponse404 | PostServicesDHCPServerStaticMappingEndpointResponse405 | PostServicesDHCPServerStaticMappingEndpointResponse406 | PostServicesDHCPServerStaticMappingEndpointResponse409 | PostServicesDHCPServerStaticMappingEndpointResponse415 | PostServicesDHCPServerStaticMappingEndpointResponse422 | PostServicesDHCPServerStaticMappingEndpointResponse424 | PostServicesDHCPServerStaticMappingEndpointResponse500 | PostServicesDHCPServerStaticMappingEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDHCPServerStaticMappingEndpointJsonBody
    | PostServicesDHCPServerStaticMappingEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesDHCPServerStaticMappingEndpointResponse400
    | PostServicesDHCPServerStaticMappingEndpointResponse401
    | PostServicesDHCPServerStaticMappingEndpointResponse403
    | PostServicesDHCPServerStaticMappingEndpointResponse404
    | PostServicesDHCPServerStaticMappingEndpointResponse405
    | PostServicesDHCPServerStaticMappingEndpointResponse406
    | PostServicesDHCPServerStaticMappingEndpointResponse409
    | PostServicesDHCPServerStaticMappingEndpointResponse415
    | PostServicesDHCPServerStaticMappingEndpointResponse422
    | PostServicesDHCPServerStaticMappingEndpointResponse424
    | PostServicesDHCPServerStaticMappingEndpointResponse500
    | PostServicesDHCPServerStaticMappingEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new DHCP Server Static Mapping.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DHCPServerStaticMapping<br>**Parent model**:
    DHCPServer<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-static-
    mapping-post ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        body (PostServicesDHCPServerStaticMappingEndpointJsonBody | Unset):
        body (PostServicesDHCPServerStaticMappingEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDHCPServerStaticMappingEndpointResponse400 | PostServicesDHCPServerStaticMappingEndpointResponse401 | PostServicesDHCPServerStaticMappingEndpointResponse403 | PostServicesDHCPServerStaticMappingEndpointResponse404 | PostServicesDHCPServerStaticMappingEndpointResponse405 | PostServicesDHCPServerStaticMappingEndpointResponse406 | PostServicesDHCPServerStaticMappingEndpointResponse409 | PostServicesDHCPServerStaticMappingEndpointResponse415 | PostServicesDHCPServerStaticMappingEndpointResponse422 | PostServicesDHCPServerStaticMappingEndpointResponse424 | PostServicesDHCPServerStaticMappingEndpointResponse500 | PostServicesDHCPServerStaticMappingEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
