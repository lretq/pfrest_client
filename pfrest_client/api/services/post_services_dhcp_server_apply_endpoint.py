from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_dhcp_server_apply_endpoint_data_body import PostServicesDHCPServerApplyEndpointDataBody
from ...models.post_services_dhcp_server_apply_endpoint_json_body import PostServicesDHCPServerApplyEndpointJsonBody
from ...models.post_services_dhcp_server_apply_endpoint_response_400 import (
    PostServicesDHCPServerApplyEndpointResponse400,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_401 import (
    PostServicesDHCPServerApplyEndpointResponse401,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_403 import (
    PostServicesDHCPServerApplyEndpointResponse403,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_404 import (
    PostServicesDHCPServerApplyEndpointResponse404,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_405 import (
    PostServicesDHCPServerApplyEndpointResponse405,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_406 import (
    PostServicesDHCPServerApplyEndpointResponse406,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_409 import (
    PostServicesDHCPServerApplyEndpointResponse409,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_415 import (
    PostServicesDHCPServerApplyEndpointResponse415,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_422 import (
    PostServicesDHCPServerApplyEndpointResponse422,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_424 import (
    PostServicesDHCPServerApplyEndpointResponse424,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_500 import (
    PostServicesDHCPServerApplyEndpointResponse500,
)
from ...models.post_services_dhcp_server_apply_endpoint_response_503 import (
    PostServicesDHCPServerApplyEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesDHCPServerApplyEndpointJsonBody | PostServicesDHCPServerApplyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/dhcp_server/apply",
    }

    if isinstance(body, PostServicesDHCPServerApplyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesDHCPServerApplyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesDHCPServerApplyEndpointResponse400
    | PostServicesDHCPServerApplyEndpointResponse401
    | PostServicesDHCPServerApplyEndpointResponse403
    | PostServicesDHCPServerApplyEndpointResponse404
    | PostServicesDHCPServerApplyEndpointResponse405
    | PostServicesDHCPServerApplyEndpointResponse406
    | PostServicesDHCPServerApplyEndpointResponse409
    | PostServicesDHCPServerApplyEndpointResponse415
    | PostServicesDHCPServerApplyEndpointResponse422
    | PostServicesDHCPServerApplyEndpointResponse424
    | PostServicesDHCPServerApplyEndpointResponse500
    | PostServicesDHCPServerApplyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesDHCPServerApplyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesDHCPServerApplyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesDHCPServerApplyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesDHCPServerApplyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesDHCPServerApplyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesDHCPServerApplyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesDHCPServerApplyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesDHCPServerApplyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesDHCPServerApplyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesDHCPServerApplyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesDHCPServerApplyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesDHCPServerApplyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesDHCPServerApplyEndpointResponse400
    | PostServicesDHCPServerApplyEndpointResponse401
    | PostServicesDHCPServerApplyEndpointResponse403
    | PostServicesDHCPServerApplyEndpointResponse404
    | PostServicesDHCPServerApplyEndpointResponse405
    | PostServicesDHCPServerApplyEndpointResponse406
    | PostServicesDHCPServerApplyEndpointResponse409
    | PostServicesDHCPServerApplyEndpointResponse415
    | PostServicesDHCPServerApplyEndpointResponse422
    | PostServicesDHCPServerApplyEndpointResponse424
    | PostServicesDHCPServerApplyEndpointResponse500
    | PostServicesDHCPServerApplyEndpointResponse503
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
    body: PostServicesDHCPServerApplyEndpointJsonBody | PostServicesDHCPServerApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesDHCPServerApplyEndpointResponse400
    | PostServicesDHCPServerApplyEndpointResponse401
    | PostServicesDHCPServerApplyEndpointResponse403
    | PostServicesDHCPServerApplyEndpointResponse404
    | PostServicesDHCPServerApplyEndpointResponse405
    | PostServicesDHCPServerApplyEndpointResponse406
    | PostServicesDHCPServerApplyEndpointResponse409
    | PostServicesDHCPServerApplyEndpointResponse415
    | PostServicesDHCPServerApplyEndpointResponse422
    | PostServicesDHCPServerApplyEndpointResponse424
    | PostServicesDHCPServerApplyEndpointResponse500
    | PostServicesDHCPServerApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending DHCP Server changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesDHCPServerApplyEndpointJsonBody | Unset):
        body (PostServicesDHCPServerApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDHCPServerApplyEndpointResponse400 | PostServicesDHCPServerApplyEndpointResponse401 | PostServicesDHCPServerApplyEndpointResponse403 | PostServicesDHCPServerApplyEndpointResponse404 | PostServicesDHCPServerApplyEndpointResponse405 | PostServicesDHCPServerApplyEndpointResponse406 | PostServicesDHCPServerApplyEndpointResponse409 | PostServicesDHCPServerApplyEndpointResponse415 | PostServicesDHCPServerApplyEndpointResponse422 | PostServicesDHCPServerApplyEndpointResponse424 | PostServicesDHCPServerApplyEndpointResponse500 | PostServicesDHCPServerApplyEndpointResponse503]
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
    body: PostServicesDHCPServerApplyEndpointJsonBody | PostServicesDHCPServerApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesDHCPServerApplyEndpointResponse400
    | PostServicesDHCPServerApplyEndpointResponse401
    | PostServicesDHCPServerApplyEndpointResponse403
    | PostServicesDHCPServerApplyEndpointResponse404
    | PostServicesDHCPServerApplyEndpointResponse405
    | PostServicesDHCPServerApplyEndpointResponse406
    | PostServicesDHCPServerApplyEndpointResponse409
    | PostServicesDHCPServerApplyEndpointResponse415
    | PostServicesDHCPServerApplyEndpointResponse422
    | PostServicesDHCPServerApplyEndpointResponse424
    | PostServicesDHCPServerApplyEndpointResponse500
    | PostServicesDHCPServerApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending DHCP Server changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesDHCPServerApplyEndpointJsonBody | Unset):
        body (PostServicesDHCPServerApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDHCPServerApplyEndpointResponse400 | PostServicesDHCPServerApplyEndpointResponse401 | PostServicesDHCPServerApplyEndpointResponse403 | PostServicesDHCPServerApplyEndpointResponse404 | PostServicesDHCPServerApplyEndpointResponse405 | PostServicesDHCPServerApplyEndpointResponse406 | PostServicesDHCPServerApplyEndpointResponse409 | PostServicesDHCPServerApplyEndpointResponse415 | PostServicesDHCPServerApplyEndpointResponse422 | PostServicesDHCPServerApplyEndpointResponse424 | PostServicesDHCPServerApplyEndpointResponse500 | PostServicesDHCPServerApplyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDHCPServerApplyEndpointJsonBody | PostServicesDHCPServerApplyEndpointDataBody | Unset = UNSET,
) -> Response[
    PostServicesDHCPServerApplyEndpointResponse400
    | PostServicesDHCPServerApplyEndpointResponse401
    | PostServicesDHCPServerApplyEndpointResponse403
    | PostServicesDHCPServerApplyEndpointResponse404
    | PostServicesDHCPServerApplyEndpointResponse405
    | PostServicesDHCPServerApplyEndpointResponse406
    | PostServicesDHCPServerApplyEndpointResponse409
    | PostServicesDHCPServerApplyEndpointResponse415
    | PostServicesDHCPServerApplyEndpointResponse422
    | PostServicesDHCPServerApplyEndpointResponse424
    | PostServicesDHCPServerApplyEndpointResponse500
    | PostServicesDHCPServerApplyEndpointResponse503
]:
    """<h3>Description:</h3>Apply pending DHCP Server changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesDHCPServerApplyEndpointJsonBody | Unset):
        body (PostServicesDHCPServerApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesDHCPServerApplyEndpointResponse400 | PostServicesDHCPServerApplyEndpointResponse401 | PostServicesDHCPServerApplyEndpointResponse403 | PostServicesDHCPServerApplyEndpointResponse404 | PostServicesDHCPServerApplyEndpointResponse405 | PostServicesDHCPServerApplyEndpointResponse406 | PostServicesDHCPServerApplyEndpointResponse409 | PostServicesDHCPServerApplyEndpointResponse415 | PostServicesDHCPServerApplyEndpointResponse422 | PostServicesDHCPServerApplyEndpointResponse424 | PostServicesDHCPServerApplyEndpointResponse500 | PostServicesDHCPServerApplyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesDHCPServerApplyEndpointJsonBody | PostServicesDHCPServerApplyEndpointDataBody | Unset = UNSET,
) -> (
    PostServicesDHCPServerApplyEndpointResponse400
    | PostServicesDHCPServerApplyEndpointResponse401
    | PostServicesDHCPServerApplyEndpointResponse403
    | PostServicesDHCPServerApplyEndpointResponse404
    | PostServicesDHCPServerApplyEndpointResponse405
    | PostServicesDHCPServerApplyEndpointResponse406
    | PostServicesDHCPServerApplyEndpointResponse409
    | PostServicesDHCPServerApplyEndpointResponse415
    | PostServicesDHCPServerApplyEndpointResponse422
    | PostServicesDHCPServerApplyEndpointResponse424
    | PostServicesDHCPServerApplyEndpointResponse500
    | PostServicesDHCPServerApplyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Apply pending DHCP Server changes.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: DHCPServerApply<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-dhcp-server-apply-post ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Not Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesDHCPServerApplyEndpointJsonBody | Unset):
        body (PostServicesDHCPServerApplyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesDHCPServerApplyEndpointResponse400 | PostServicesDHCPServerApplyEndpointResponse401 | PostServicesDHCPServerApplyEndpointResponse403 | PostServicesDHCPServerApplyEndpointResponse404 | PostServicesDHCPServerApplyEndpointResponse405 | PostServicesDHCPServerApplyEndpointResponse406 | PostServicesDHCPServerApplyEndpointResponse409 | PostServicesDHCPServerApplyEndpointResponse415 | PostServicesDHCPServerApplyEndpointResponse422 | PostServicesDHCPServerApplyEndpointResponse424 | PostServicesDHCPServerApplyEndpointResponse500 | PostServicesDHCPServerApplyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
