from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_restapi_access_list_entry_endpoint_data_body import (
    PatchSystemRESTAPIAccessListEntryEndpointDataBody,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_json_body import (
    PatchSystemRESTAPIAccessListEntryEndpointJsonBody,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_400 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse400,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_401 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse401,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_403 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse403,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_404 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse404,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_405 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse405,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_406 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse406,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_409 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse409,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_415 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse415,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_422 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse422,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_424 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse424,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_500 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse500,
)
from ...models.patch_system_restapi_access_list_entry_endpoint_response_503 import (
    PatchSystemRESTAPIAccessListEntryEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemRESTAPIAccessListEntryEndpointJsonBody
    | PatchSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/restapi/access_list/entry",
    }

    if isinstance(body, PatchSystemRESTAPIAccessListEntryEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemRESTAPIAccessListEntryEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemRESTAPIAccessListEntryEndpointResponse400
    | PatchSystemRESTAPIAccessListEntryEndpointResponse401
    | PatchSystemRESTAPIAccessListEntryEndpointResponse403
    | PatchSystemRESTAPIAccessListEntryEndpointResponse404
    | PatchSystemRESTAPIAccessListEntryEndpointResponse405
    | PatchSystemRESTAPIAccessListEntryEndpointResponse406
    | PatchSystemRESTAPIAccessListEntryEndpointResponse409
    | PatchSystemRESTAPIAccessListEntryEndpointResponse415
    | PatchSystemRESTAPIAccessListEntryEndpointResponse422
    | PatchSystemRESTAPIAccessListEntryEndpointResponse424
    | PatchSystemRESTAPIAccessListEntryEndpointResponse500
    | PatchSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemRESTAPIAccessListEntryEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemRESTAPIAccessListEntryEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemRESTAPIAccessListEntryEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemRESTAPIAccessListEntryEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemRESTAPIAccessListEntryEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemRESTAPIAccessListEntryEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemRESTAPIAccessListEntryEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemRESTAPIAccessListEntryEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemRESTAPIAccessListEntryEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemRESTAPIAccessListEntryEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemRESTAPIAccessListEntryEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemRESTAPIAccessListEntryEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemRESTAPIAccessListEntryEndpointResponse400
    | PatchSystemRESTAPIAccessListEntryEndpointResponse401
    | PatchSystemRESTAPIAccessListEntryEndpointResponse403
    | PatchSystemRESTAPIAccessListEntryEndpointResponse404
    | PatchSystemRESTAPIAccessListEntryEndpointResponse405
    | PatchSystemRESTAPIAccessListEntryEndpointResponse406
    | PatchSystemRESTAPIAccessListEntryEndpointResponse409
    | PatchSystemRESTAPIAccessListEntryEndpointResponse415
    | PatchSystemRESTAPIAccessListEntryEndpointResponse422
    | PatchSystemRESTAPIAccessListEntryEndpointResponse424
    | PatchSystemRESTAPIAccessListEntryEndpointResponse500
    | PatchSystemRESTAPIAccessListEntryEndpointResponse503
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
    body: PatchSystemRESTAPIAccessListEntryEndpointJsonBody
    | PatchSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchSystemRESTAPIAccessListEntryEndpointResponse400
    | PatchSystemRESTAPIAccessListEntryEndpointResponse401
    | PatchSystemRESTAPIAccessListEntryEndpointResponse403
    | PatchSystemRESTAPIAccessListEntryEndpointResponse404
    | PatchSystemRESTAPIAccessListEntryEndpointResponse405
    | PatchSystemRESTAPIAccessListEntryEndpointResponse406
    | PatchSystemRESTAPIAccessListEntryEndpointResponse409
    | PatchSystemRESTAPIAccessListEntryEndpointResponse415
    | PatchSystemRESTAPIAccessListEntryEndpointResponse422
    | PatchSystemRESTAPIAccessListEntryEndpointResponse424
    | PatchSystemRESTAPIAccessListEntryEndpointResponse500
    | PatchSystemRESTAPIAccessListEntryEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchSystemRESTAPIAccessListEntryEndpointJsonBody | Unset):
        body (PatchSystemRESTAPIAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemRESTAPIAccessListEntryEndpointResponse400 | PatchSystemRESTAPIAccessListEntryEndpointResponse401 | PatchSystemRESTAPIAccessListEntryEndpointResponse403 | PatchSystemRESTAPIAccessListEntryEndpointResponse404 | PatchSystemRESTAPIAccessListEntryEndpointResponse405 | PatchSystemRESTAPIAccessListEntryEndpointResponse406 | PatchSystemRESTAPIAccessListEntryEndpointResponse409 | PatchSystemRESTAPIAccessListEntryEndpointResponse415 | PatchSystemRESTAPIAccessListEntryEndpointResponse422 | PatchSystemRESTAPIAccessListEntryEndpointResponse424 | PatchSystemRESTAPIAccessListEntryEndpointResponse500 | PatchSystemRESTAPIAccessListEntryEndpointResponse503]
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
    body: PatchSystemRESTAPIAccessListEntryEndpointJsonBody
    | PatchSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchSystemRESTAPIAccessListEntryEndpointResponse400
    | PatchSystemRESTAPIAccessListEntryEndpointResponse401
    | PatchSystemRESTAPIAccessListEntryEndpointResponse403
    | PatchSystemRESTAPIAccessListEntryEndpointResponse404
    | PatchSystemRESTAPIAccessListEntryEndpointResponse405
    | PatchSystemRESTAPIAccessListEntryEndpointResponse406
    | PatchSystemRESTAPIAccessListEntryEndpointResponse409
    | PatchSystemRESTAPIAccessListEntryEndpointResponse415
    | PatchSystemRESTAPIAccessListEntryEndpointResponse422
    | PatchSystemRESTAPIAccessListEntryEndpointResponse424
    | PatchSystemRESTAPIAccessListEntryEndpointResponse500
    | PatchSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchSystemRESTAPIAccessListEntryEndpointJsonBody | Unset):
        body (PatchSystemRESTAPIAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemRESTAPIAccessListEntryEndpointResponse400 | PatchSystemRESTAPIAccessListEntryEndpointResponse401 | PatchSystemRESTAPIAccessListEntryEndpointResponse403 | PatchSystemRESTAPIAccessListEntryEndpointResponse404 | PatchSystemRESTAPIAccessListEntryEndpointResponse405 | PatchSystemRESTAPIAccessListEntryEndpointResponse406 | PatchSystemRESTAPIAccessListEntryEndpointResponse409 | PatchSystemRESTAPIAccessListEntryEndpointResponse415 | PatchSystemRESTAPIAccessListEntryEndpointResponse422 | PatchSystemRESTAPIAccessListEntryEndpointResponse424 | PatchSystemRESTAPIAccessListEntryEndpointResponse500 | PatchSystemRESTAPIAccessListEntryEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemRESTAPIAccessListEntryEndpointJsonBody
    | PatchSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchSystemRESTAPIAccessListEntryEndpointResponse400
    | PatchSystemRESTAPIAccessListEntryEndpointResponse401
    | PatchSystemRESTAPIAccessListEntryEndpointResponse403
    | PatchSystemRESTAPIAccessListEntryEndpointResponse404
    | PatchSystemRESTAPIAccessListEntryEndpointResponse405
    | PatchSystemRESTAPIAccessListEntryEndpointResponse406
    | PatchSystemRESTAPIAccessListEntryEndpointResponse409
    | PatchSystemRESTAPIAccessListEntryEndpointResponse415
    | PatchSystemRESTAPIAccessListEntryEndpointResponse422
    | PatchSystemRESTAPIAccessListEntryEndpointResponse424
    | PatchSystemRESTAPIAccessListEntryEndpointResponse500
    | PatchSystemRESTAPIAccessListEntryEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchSystemRESTAPIAccessListEntryEndpointJsonBody | Unset):
        body (PatchSystemRESTAPIAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemRESTAPIAccessListEntryEndpointResponse400 | PatchSystemRESTAPIAccessListEntryEndpointResponse401 | PatchSystemRESTAPIAccessListEntryEndpointResponse403 | PatchSystemRESTAPIAccessListEntryEndpointResponse404 | PatchSystemRESTAPIAccessListEntryEndpointResponse405 | PatchSystemRESTAPIAccessListEntryEndpointResponse406 | PatchSystemRESTAPIAccessListEntryEndpointResponse409 | PatchSystemRESTAPIAccessListEntryEndpointResponse415 | PatchSystemRESTAPIAccessListEntryEndpointResponse422 | PatchSystemRESTAPIAccessListEntryEndpointResponse424 | PatchSystemRESTAPIAccessListEntryEndpointResponse500 | PatchSystemRESTAPIAccessListEntryEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemRESTAPIAccessListEntryEndpointJsonBody
    | PatchSystemRESTAPIAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchSystemRESTAPIAccessListEntryEndpointResponse400
    | PatchSystemRESTAPIAccessListEntryEndpointResponse401
    | PatchSystemRESTAPIAccessListEntryEndpointResponse403
    | PatchSystemRESTAPIAccessListEntryEndpointResponse404
    | PatchSystemRESTAPIAccessListEntryEndpointResponse405
    | PatchSystemRESTAPIAccessListEntryEndpointResponse406
    | PatchSystemRESTAPIAccessListEntryEndpointResponse409
    | PatchSystemRESTAPIAccessListEntryEndpointResponse415
    | PatchSystemRESTAPIAccessListEntryEndpointResponse422
    | PatchSystemRESTAPIAccessListEntryEndpointResponse424
    | PatchSystemRESTAPIAccessListEntryEndpointResponse500
    | PatchSystemRESTAPIAccessListEntryEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing RESTAPI Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: RESTAPIAccessListEntry<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-restapi-access-list-entry-
    patch ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**:
    None

    Args:
        body (PatchSystemRESTAPIAccessListEntryEndpointJsonBody | Unset):
        body (PatchSystemRESTAPIAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemRESTAPIAccessListEntryEndpointResponse400 | PatchSystemRESTAPIAccessListEntryEndpointResponse401 | PatchSystemRESTAPIAccessListEntryEndpointResponse403 | PatchSystemRESTAPIAccessListEntryEndpointResponse404 | PatchSystemRESTAPIAccessListEntryEndpointResponse405 | PatchSystemRESTAPIAccessListEntryEndpointResponse406 | PatchSystemRESTAPIAccessListEntryEndpointResponse409 | PatchSystemRESTAPIAccessListEntryEndpointResponse415 | PatchSystemRESTAPIAccessListEntryEndpointResponse422 | PatchSystemRESTAPIAccessListEntryEndpointResponse424 | PatchSystemRESTAPIAccessListEntryEndpointResponse500 | PatchSystemRESTAPIAccessListEntryEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
