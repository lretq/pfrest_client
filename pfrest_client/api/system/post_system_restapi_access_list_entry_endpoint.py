from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_system_restapi_access_list_entry_endpoint_data_body import (
    PostSystemRESTAPIAccessListEntryEndpointDataBody,
)
from ...models.post_system_restapi_access_list_entry_endpoint_json_body import (
    PostSystemRESTAPIAccessListEntryEndpointJsonBody,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_400 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse400,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_401 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse401,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_403 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse403,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_404 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse404,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_405 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse405,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_406 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse406,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_409 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse409,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_415 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse415,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_422 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse422,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_424 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse424,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_500 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse500,
)
from ...models.post_system_restapi_access_list_entry_endpoint_response_503 import (
    PostSystemRESTAPIAccessListEntryEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostSystemRESTAPIAccessListEntryEndpointJsonBody
    | PostSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/restapi/access_list/entry",
    }

    if isinstance(body, PostSystemRESTAPIAccessListEntryEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSystemRESTAPIAccessListEntryEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostSystemRESTAPIAccessListEntryEndpointResponse400
    | PostSystemRESTAPIAccessListEntryEndpointResponse401
    | PostSystemRESTAPIAccessListEntryEndpointResponse403
    | PostSystemRESTAPIAccessListEntryEndpointResponse404
    | PostSystemRESTAPIAccessListEntryEndpointResponse405
    | PostSystemRESTAPIAccessListEntryEndpointResponse406
    | PostSystemRESTAPIAccessListEntryEndpointResponse409
    | PostSystemRESTAPIAccessListEntryEndpointResponse415
    | PostSystemRESTAPIAccessListEntryEndpointResponse422
    | PostSystemRESTAPIAccessListEntryEndpointResponse424
    | PostSystemRESTAPIAccessListEntryEndpointResponse500
    | PostSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostSystemRESTAPIAccessListEntryEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostSystemRESTAPIAccessListEntryEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostSystemRESTAPIAccessListEntryEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostSystemRESTAPIAccessListEntryEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostSystemRESTAPIAccessListEntryEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostSystemRESTAPIAccessListEntryEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostSystemRESTAPIAccessListEntryEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostSystemRESTAPIAccessListEntryEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostSystemRESTAPIAccessListEntryEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostSystemRESTAPIAccessListEntryEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostSystemRESTAPIAccessListEntryEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostSystemRESTAPIAccessListEntryEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostSystemRESTAPIAccessListEntryEndpointResponse400
    | PostSystemRESTAPIAccessListEntryEndpointResponse401
    | PostSystemRESTAPIAccessListEntryEndpointResponse403
    | PostSystemRESTAPIAccessListEntryEndpointResponse404
    | PostSystemRESTAPIAccessListEntryEndpointResponse405
    | PostSystemRESTAPIAccessListEntryEndpointResponse406
    | PostSystemRESTAPIAccessListEntryEndpointResponse409
    | PostSystemRESTAPIAccessListEntryEndpointResponse415
    | PostSystemRESTAPIAccessListEntryEndpointResponse422
    | PostSystemRESTAPIAccessListEntryEndpointResponse424
    | PostSystemRESTAPIAccessListEntryEndpointResponse500
    | PostSystemRESTAPIAccessListEntryEndpointResponse503
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
    body: PostSystemRESTAPIAccessListEntryEndpointJsonBody
    | PostSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemRESTAPIAccessListEntryEndpointResponse400
    | PostSystemRESTAPIAccessListEntryEndpointResponse401
    | PostSystemRESTAPIAccessListEntryEndpointResponse403
    | PostSystemRESTAPIAccessListEntryEndpointResponse404
    | PostSystemRESTAPIAccessListEntryEndpointResponse405
    | PostSystemRESTAPIAccessListEntryEndpointResponse406
    | PostSystemRESTAPIAccessListEntryEndpointResponse409
    | PostSystemRESTAPIAccessListEntryEndpointResponse415
    | PostSystemRESTAPIAccessListEntryEndpointResponse422
    | PostSystemRESTAPIAccessListEntryEndpointResponse424
    | PostSystemRESTAPIAccessListEntryEndpointResponse500
    | PostSystemRESTAPIAccessListEntryEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemRESTAPIAccessListEntryEndpointJsonBody | Unset):
        body (PostSystemRESTAPIAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemRESTAPIAccessListEntryEndpointResponse400 | PostSystemRESTAPIAccessListEntryEndpointResponse401 | PostSystemRESTAPIAccessListEntryEndpointResponse403 | PostSystemRESTAPIAccessListEntryEndpointResponse404 | PostSystemRESTAPIAccessListEntryEndpointResponse405 | PostSystemRESTAPIAccessListEntryEndpointResponse406 | PostSystemRESTAPIAccessListEntryEndpointResponse409 | PostSystemRESTAPIAccessListEntryEndpointResponse415 | PostSystemRESTAPIAccessListEntryEndpointResponse422 | PostSystemRESTAPIAccessListEntryEndpointResponse424 | PostSystemRESTAPIAccessListEntryEndpointResponse500 | PostSystemRESTAPIAccessListEntryEndpointResponse503]
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
    body: PostSystemRESTAPIAccessListEntryEndpointJsonBody
    | PostSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemRESTAPIAccessListEntryEndpointResponse400
    | PostSystemRESTAPIAccessListEntryEndpointResponse401
    | PostSystemRESTAPIAccessListEntryEndpointResponse403
    | PostSystemRESTAPIAccessListEntryEndpointResponse404
    | PostSystemRESTAPIAccessListEntryEndpointResponse405
    | PostSystemRESTAPIAccessListEntryEndpointResponse406
    | PostSystemRESTAPIAccessListEntryEndpointResponse409
    | PostSystemRESTAPIAccessListEntryEndpointResponse415
    | PostSystemRESTAPIAccessListEntryEndpointResponse422
    | PostSystemRESTAPIAccessListEntryEndpointResponse424
    | PostSystemRESTAPIAccessListEntryEndpointResponse500
    | PostSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemRESTAPIAccessListEntryEndpointJsonBody | Unset):
        body (PostSystemRESTAPIAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemRESTAPIAccessListEntryEndpointResponse400 | PostSystemRESTAPIAccessListEntryEndpointResponse401 | PostSystemRESTAPIAccessListEntryEndpointResponse403 | PostSystemRESTAPIAccessListEntryEndpointResponse404 | PostSystemRESTAPIAccessListEntryEndpointResponse405 | PostSystemRESTAPIAccessListEntryEndpointResponse406 | PostSystemRESTAPIAccessListEntryEndpointResponse409 | PostSystemRESTAPIAccessListEntryEndpointResponse415 | PostSystemRESTAPIAccessListEntryEndpointResponse422 | PostSystemRESTAPIAccessListEntryEndpointResponse424 | PostSystemRESTAPIAccessListEntryEndpointResponse500 | PostSystemRESTAPIAccessListEntryEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemRESTAPIAccessListEntryEndpointJsonBody
    | PostSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostSystemRESTAPIAccessListEntryEndpointResponse400
    | PostSystemRESTAPIAccessListEntryEndpointResponse401
    | PostSystemRESTAPIAccessListEntryEndpointResponse403
    | PostSystemRESTAPIAccessListEntryEndpointResponse404
    | PostSystemRESTAPIAccessListEntryEndpointResponse405
    | PostSystemRESTAPIAccessListEntryEndpointResponse406
    | PostSystemRESTAPIAccessListEntryEndpointResponse409
    | PostSystemRESTAPIAccessListEntryEndpointResponse415
    | PostSystemRESTAPIAccessListEntryEndpointResponse422
    | PostSystemRESTAPIAccessListEntryEndpointResponse424
    | PostSystemRESTAPIAccessListEntryEndpointResponse500
    | PostSystemRESTAPIAccessListEntryEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemRESTAPIAccessListEntryEndpointJsonBody | Unset):
        body (PostSystemRESTAPIAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSystemRESTAPIAccessListEntryEndpointResponse400 | PostSystemRESTAPIAccessListEntryEndpointResponse401 | PostSystemRESTAPIAccessListEntryEndpointResponse403 | PostSystemRESTAPIAccessListEntryEndpointResponse404 | PostSystemRESTAPIAccessListEntryEndpointResponse405 | PostSystemRESTAPIAccessListEntryEndpointResponse406 | PostSystemRESTAPIAccessListEntryEndpointResponse409 | PostSystemRESTAPIAccessListEntryEndpointResponse415 | PostSystemRESTAPIAccessListEntryEndpointResponse422 | PostSystemRESTAPIAccessListEntryEndpointResponse424 | PostSystemRESTAPIAccessListEntryEndpointResponse500 | PostSystemRESTAPIAccessListEntryEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemRESTAPIAccessListEntryEndpointJsonBody
    | PostSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> (
    PostSystemRESTAPIAccessListEntryEndpointResponse400
    | PostSystemRESTAPIAccessListEntryEndpointResponse401
    | PostSystemRESTAPIAccessListEntryEndpointResponse403
    | PostSystemRESTAPIAccessListEntryEndpointResponse404
    | PostSystemRESTAPIAccessListEntryEndpointResponse405
    | PostSystemRESTAPIAccessListEntryEndpointResponse406
    | PostSystemRESTAPIAccessListEntryEndpointResponse409
    | PostSystemRESTAPIAccessListEntryEndpointResponse415
    | PostSystemRESTAPIAccessListEntryEndpointResponse422
    | PostSystemRESTAPIAccessListEntryEndpointResponse424
    | PostSystemRESTAPIAccessListEntryEndpointResponse500
    | PostSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-post
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostSystemRESTAPIAccessListEntryEndpointJsonBody | Unset):
        body (PostSystemRESTAPIAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSystemRESTAPIAccessListEntryEndpointResponse400 | PostSystemRESTAPIAccessListEntryEndpointResponse401 | PostSystemRESTAPIAccessListEntryEndpointResponse403 | PostSystemRESTAPIAccessListEntryEndpointResponse404 | PostSystemRESTAPIAccessListEntryEndpointResponse405 | PostSystemRESTAPIAccessListEntryEndpointResponse406 | PostSystemRESTAPIAccessListEntryEndpointResponse409 | PostSystemRESTAPIAccessListEntryEndpointResponse415 | PostSystemRESTAPIAccessListEntryEndpointResponse422 | PostSystemRESTAPIAccessListEntryEndpointResponse424 | PostSystemRESTAPIAccessListEntryEndpointResponse500 | PostSystemRESTAPIAccessListEntryEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
