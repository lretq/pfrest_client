from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_bind_access_list_entry_endpoint_data_body import (
    PatchServicesBINDAccessListEntryEndpointDataBody,
)
from ...models.patch_services_bind_access_list_entry_endpoint_json_body import (
    PatchServicesBINDAccessListEntryEndpointJsonBody,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_400 import (
    PatchServicesBINDAccessListEntryEndpointResponse400,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_401 import (
    PatchServicesBINDAccessListEntryEndpointResponse401,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_403 import (
    PatchServicesBINDAccessListEntryEndpointResponse403,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_404 import (
    PatchServicesBINDAccessListEntryEndpointResponse404,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_405 import (
    PatchServicesBINDAccessListEntryEndpointResponse405,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_406 import (
    PatchServicesBINDAccessListEntryEndpointResponse406,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_409 import (
    PatchServicesBINDAccessListEntryEndpointResponse409,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_415 import (
    PatchServicesBINDAccessListEntryEndpointResponse415,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_422 import (
    PatchServicesBINDAccessListEntryEndpointResponse422,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_424 import (
    PatchServicesBINDAccessListEntryEndpointResponse424,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_500 import (
    PatchServicesBINDAccessListEntryEndpointResponse500,
)
from ...models.patch_services_bind_access_list_entry_endpoint_response_503 import (
    PatchServicesBINDAccessListEntryEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesBINDAccessListEntryEndpointJsonBody
    | PatchServicesBINDAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/bind/access_list/entry",
    }

    if isinstance(body, PatchServicesBINDAccessListEntryEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesBINDAccessListEntryEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesBINDAccessListEntryEndpointResponse400
    | PatchServicesBINDAccessListEntryEndpointResponse401
    | PatchServicesBINDAccessListEntryEndpointResponse403
    | PatchServicesBINDAccessListEntryEndpointResponse404
    | PatchServicesBINDAccessListEntryEndpointResponse405
    | PatchServicesBINDAccessListEntryEndpointResponse406
    | PatchServicesBINDAccessListEntryEndpointResponse409
    | PatchServicesBINDAccessListEntryEndpointResponse415
    | PatchServicesBINDAccessListEntryEndpointResponse422
    | PatchServicesBINDAccessListEntryEndpointResponse424
    | PatchServicesBINDAccessListEntryEndpointResponse500
    | PatchServicesBINDAccessListEntryEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesBINDAccessListEntryEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesBINDAccessListEntryEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesBINDAccessListEntryEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesBINDAccessListEntryEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesBINDAccessListEntryEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesBINDAccessListEntryEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesBINDAccessListEntryEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesBINDAccessListEntryEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesBINDAccessListEntryEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesBINDAccessListEntryEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesBINDAccessListEntryEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesBINDAccessListEntryEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesBINDAccessListEntryEndpointResponse400
    | PatchServicesBINDAccessListEntryEndpointResponse401
    | PatchServicesBINDAccessListEntryEndpointResponse403
    | PatchServicesBINDAccessListEntryEndpointResponse404
    | PatchServicesBINDAccessListEntryEndpointResponse405
    | PatchServicesBINDAccessListEntryEndpointResponse406
    | PatchServicesBINDAccessListEntryEndpointResponse409
    | PatchServicesBINDAccessListEntryEndpointResponse415
    | PatchServicesBINDAccessListEntryEndpointResponse422
    | PatchServicesBINDAccessListEntryEndpointResponse424
    | PatchServicesBINDAccessListEntryEndpointResponse500
    | PatchServicesBINDAccessListEntryEndpointResponse503
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
    body: PatchServicesBINDAccessListEntryEndpointJsonBody
    | PatchServicesBINDAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesBINDAccessListEntryEndpointResponse400
    | PatchServicesBINDAccessListEntryEndpointResponse401
    | PatchServicesBINDAccessListEntryEndpointResponse403
    | PatchServicesBINDAccessListEntryEndpointResponse404
    | PatchServicesBINDAccessListEntryEndpointResponse405
    | PatchServicesBINDAccessListEntryEndpointResponse406
    | PatchServicesBINDAccessListEntryEndpointResponse409
    | PatchServicesBINDAccessListEntryEndpointResponse415
    | PatchServicesBINDAccessListEntryEndpointResponse422
    | PatchServicesBINDAccessListEntryEndpointResponse424
    | PatchServicesBINDAccessListEntryEndpointResponse500
    | PatchServicesBINDAccessListEntryEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing BIND Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: BINDAccessListEntry<br>**Parent model**:
    BINDAccessList<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-
    list-entry-patch ]<br>**Required packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDAccessListEntryEndpointJsonBody | Unset):
        body (PatchServicesBINDAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesBINDAccessListEntryEndpointResponse400 | PatchServicesBINDAccessListEntryEndpointResponse401 | PatchServicesBINDAccessListEntryEndpointResponse403 | PatchServicesBINDAccessListEntryEndpointResponse404 | PatchServicesBINDAccessListEntryEndpointResponse405 | PatchServicesBINDAccessListEntryEndpointResponse406 | PatchServicesBINDAccessListEntryEndpointResponse409 | PatchServicesBINDAccessListEntryEndpointResponse415 | PatchServicesBINDAccessListEntryEndpointResponse422 | PatchServicesBINDAccessListEntryEndpointResponse424 | PatchServicesBINDAccessListEntryEndpointResponse500 | PatchServicesBINDAccessListEntryEndpointResponse503]
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
    body: PatchServicesBINDAccessListEntryEndpointJsonBody
    | PatchServicesBINDAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesBINDAccessListEntryEndpointResponse400
    | PatchServicesBINDAccessListEntryEndpointResponse401
    | PatchServicesBINDAccessListEntryEndpointResponse403
    | PatchServicesBINDAccessListEntryEndpointResponse404
    | PatchServicesBINDAccessListEntryEndpointResponse405
    | PatchServicesBINDAccessListEntryEndpointResponse406
    | PatchServicesBINDAccessListEntryEndpointResponse409
    | PatchServicesBINDAccessListEntryEndpointResponse415
    | PatchServicesBINDAccessListEntryEndpointResponse422
    | PatchServicesBINDAccessListEntryEndpointResponse424
    | PatchServicesBINDAccessListEntryEndpointResponse500
    | PatchServicesBINDAccessListEntryEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing BIND Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: BINDAccessListEntry<br>**Parent model**:
    BINDAccessList<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-
    list-entry-patch ]<br>**Required packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDAccessListEntryEndpointJsonBody | Unset):
        body (PatchServicesBINDAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesBINDAccessListEntryEndpointResponse400 | PatchServicesBINDAccessListEntryEndpointResponse401 | PatchServicesBINDAccessListEntryEndpointResponse403 | PatchServicesBINDAccessListEntryEndpointResponse404 | PatchServicesBINDAccessListEntryEndpointResponse405 | PatchServicesBINDAccessListEntryEndpointResponse406 | PatchServicesBINDAccessListEntryEndpointResponse409 | PatchServicesBINDAccessListEntryEndpointResponse415 | PatchServicesBINDAccessListEntryEndpointResponse422 | PatchServicesBINDAccessListEntryEndpointResponse424 | PatchServicesBINDAccessListEntryEndpointResponse500 | PatchServicesBINDAccessListEntryEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesBINDAccessListEntryEndpointJsonBody
    | PatchServicesBINDAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PatchServicesBINDAccessListEntryEndpointResponse400
    | PatchServicesBINDAccessListEntryEndpointResponse401
    | PatchServicesBINDAccessListEntryEndpointResponse403
    | PatchServicesBINDAccessListEntryEndpointResponse404
    | PatchServicesBINDAccessListEntryEndpointResponse405
    | PatchServicesBINDAccessListEntryEndpointResponse406
    | PatchServicesBINDAccessListEntryEndpointResponse409
    | PatchServicesBINDAccessListEntryEndpointResponse415
    | PatchServicesBINDAccessListEntryEndpointResponse422
    | PatchServicesBINDAccessListEntryEndpointResponse424
    | PatchServicesBINDAccessListEntryEndpointResponse500
    | PatchServicesBINDAccessListEntryEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing BIND Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: BINDAccessListEntry<br>**Parent model**:
    BINDAccessList<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-
    list-entry-patch ]<br>**Required packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDAccessListEntryEndpointJsonBody | Unset):
        body (PatchServicesBINDAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesBINDAccessListEntryEndpointResponse400 | PatchServicesBINDAccessListEntryEndpointResponse401 | PatchServicesBINDAccessListEntryEndpointResponse403 | PatchServicesBINDAccessListEntryEndpointResponse404 | PatchServicesBINDAccessListEntryEndpointResponse405 | PatchServicesBINDAccessListEntryEndpointResponse406 | PatchServicesBINDAccessListEntryEndpointResponse409 | PatchServicesBINDAccessListEntryEndpointResponse415 | PatchServicesBINDAccessListEntryEndpointResponse422 | PatchServicesBINDAccessListEntryEndpointResponse424 | PatchServicesBINDAccessListEntryEndpointResponse500 | PatchServicesBINDAccessListEntryEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesBINDAccessListEntryEndpointJsonBody
    | PatchServicesBINDAccessListEntryEndpointDataBody
    | Unset = UNSET,
) -> (
    PatchServicesBINDAccessListEntryEndpointResponse400
    | PatchServicesBINDAccessListEntryEndpointResponse401
    | PatchServicesBINDAccessListEntryEndpointResponse403
    | PatchServicesBINDAccessListEntryEndpointResponse404
    | PatchServicesBINDAccessListEntryEndpointResponse405
    | PatchServicesBINDAccessListEntryEndpointResponse406
    | PatchServicesBINDAccessListEntryEndpointResponse409
    | PatchServicesBINDAccessListEntryEndpointResponse415
    | PatchServicesBINDAccessListEntryEndpointResponse422
    | PatchServicesBINDAccessListEntryEndpointResponse424
    | PatchServicesBINDAccessListEntryEndpointResponse500
    | PatchServicesBINDAccessListEntryEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing BIND Access List Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: BINDAccessListEntry<br>**Parent model**:
    BINDAccessList<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-
    list-entry-patch ]<br>**Required packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDAccessListEntryEndpointJsonBody | Unset):
        body (PatchServicesBINDAccessListEntryEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesBINDAccessListEntryEndpointResponse400 | PatchServicesBINDAccessListEntryEndpointResponse401 | PatchServicesBINDAccessListEntryEndpointResponse403 | PatchServicesBINDAccessListEntryEndpointResponse404 | PatchServicesBINDAccessListEntryEndpointResponse405 | PatchServicesBINDAccessListEntryEndpointResponse406 | PatchServicesBINDAccessListEntryEndpointResponse409 | PatchServicesBINDAccessListEntryEndpointResponse415 | PatchServicesBINDAccessListEntryEndpointResponse422 | PatchServicesBINDAccessListEntryEndpointResponse424 | PatchServicesBINDAccessListEntryEndpointResponse500 | PatchServicesBINDAccessListEntryEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
