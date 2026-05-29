from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_bind_access_list_endpoint_data_body import PatchServicesBINDAccessListEndpointDataBody
from ...models.patch_services_bind_access_list_endpoint_json_body import PatchServicesBINDAccessListEndpointJsonBody
from ...models.patch_services_bind_access_list_endpoint_response_400 import (
    PatchServicesBINDAccessListEndpointResponse400,
)
from ...models.patch_services_bind_access_list_endpoint_response_401 import (
    PatchServicesBINDAccessListEndpointResponse401,
)
from ...models.patch_services_bind_access_list_endpoint_response_403 import (
    PatchServicesBINDAccessListEndpointResponse403,
)
from ...models.patch_services_bind_access_list_endpoint_response_404 import (
    PatchServicesBINDAccessListEndpointResponse404,
)
from ...models.patch_services_bind_access_list_endpoint_response_405 import (
    PatchServicesBINDAccessListEndpointResponse405,
)
from ...models.patch_services_bind_access_list_endpoint_response_406 import (
    PatchServicesBINDAccessListEndpointResponse406,
)
from ...models.patch_services_bind_access_list_endpoint_response_409 import (
    PatchServicesBINDAccessListEndpointResponse409,
)
from ...models.patch_services_bind_access_list_endpoint_response_415 import (
    PatchServicesBINDAccessListEndpointResponse415,
)
from ...models.patch_services_bind_access_list_endpoint_response_422 import (
    PatchServicesBINDAccessListEndpointResponse422,
)
from ...models.patch_services_bind_access_list_endpoint_response_424 import (
    PatchServicesBINDAccessListEndpointResponse424,
)
from ...models.patch_services_bind_access_list_endpoint_response_500 import (
    PatchServicesBINDAccessListEndpointResponse500,
)
from ...models.patch_services_bind_access_list_endpoint_response_503 import (
    PatchServicesBINDAccessListEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesBINDAccessListEndpointJsonBody | PatchServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/bind/access_list",
    }

    if isinstance(body, PatchServicesBINDAccessListEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesBINDAccessListEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesBINDAccessListEndpointResponse400
    | PatchServicesBINDAccessListEndpointResponse401
    | PatchServicesBINDAccessListEndpointResponse403
    | PatchServicesBINDAccessListEndpointResponse404
    | PatchServicesBINDAccessListEndpointResponse405
    | PatchServicesBINDAccessListEndpointResponse406
    | PatchServicesBINDAccessListEndpointResponse409
    | PatchServicesBINDAccessListEndpointResponse415
    | PatchServicesBINDAccessListEndpointResponse422
    | PatchServicesBINDAccessListEndpointResponse424
    | PatchServicesBINDAccessListEndpointResponse500
    | PatchServicesBINDAccessListEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesBINDAccessListEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesBINDAccessListEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesBINDAccessListEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesBINDAccessListEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesBINDAccessListEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesBINDAccessListEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesBINDAccessListEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesBINDAccessListEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesBINDAccessListEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesBINDAccessListEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesBINDAccessListEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesBINDAccessListEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesBINDAccessListEndpointResponse400
    | PatchServicesBINDAccessListEndpointResponse401
    | PatchServicesBINDAccessListEndpointResponse403
    | PatchServicesBINDAccessListEndpointResponse404
    | PatchServicesBINDAccessListEndpointResponse405
    | PatchServicesBINDAccessListEndpointResponse406
    | PatchServicesBINDAccessListEndpointResponse409
    | PatchServicesBINDAccessListEndpointResponse415
    | PatchServicesBINDAccessListEndpointResponse422
    | PatchServicesBINDAccessListEndpointResponse424
    | PatchServicesBINDAccessListEndpointResponse500
    | PatchServicesBINDAccessListEndpointResponse503
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
    body: PatchServicesBINDAccessListEndpointJsonBody | PatchServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesBINDAccessListEndpointResponse400
    | PatchServicesBINDAccessListEndpointResponse401
    | PatchServicesBINDAccessListEndpointResponse403
    | PatchServicesBINDAccessListEndpointResponse404
    | PatchServicesBINDAccessListEndpointResponse405
    | PatchServicesBINDAccessListEndpointResponse406
    | PatchServicesBINDAccessListEndpointResponse409
    | PatchServicesBINDAccessListEndpointResponse415
    | PatchServicesBINDAccessListEndpointResponse422
    | PatchServicesBINDAccessListEndpointResponse424
    | PatchServicesBINDAccessListEndpointResponse500
    | PatchServicesBINDAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing BIND Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-list-patch ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDAccessListEndpointJsonBody | Unset):
        body (PatchServicesBINDAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesBINDAccessListEndpointResponse400 | PatchServicesBINDAccessListEndpointResponse401 | PatchServicesBINDAccessListEndpointResponse403 | PatchServicesBINDAccessListEndpointResponse404 | PatchServicesBINDAccessListEndpointResponse405 | PatchServicesBINDAccessListEndpointResponse406 | PatchServicesBINDAccessListEndpointResponse409 | PatchServicesBINDAccessListEndpointResponse415 | PatchServicesBINDAccessListEndpointResponse422 | PatchServicesBINDAccessListEndpointResponse424 | PatchServicesBINDAccessListEndpointResponse500 | PatchServicesBINDAccessListEndpointResponse503]
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
    body: PatchServicesBINDAccessListEndpointJsonBody | PatchServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesBINDAccessListEndpointResponse400
    | PatchServicesBINDAccessListEndpointResponse401
    | PatchServicesBINDAccessListEndpointResponse403
    | PatchServicesBINDAccessListEndpointResponse404
    | PatchServicesBINDAccessListEndpointResponse405
    | PatchServicesBINDAccessListEndpointResponse406
    | PatchServicesBINDAccessListEndpointResponse409
    | PatchServicesBINDAccessListEndpointResponse415
    | PatchServicesBINDAccessListEndpointResponse422
    | PatchServicesBINDAccessListEndpointResponse424
    | PatchServicesBINDAccessListEndpointResponse500
    | PatchServicesBINDAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing BIND Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-list-patch ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDAccessListEndpointJsonBody | Unset):
        body (PatchServicesBINDAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesBINDAccessListEndpointResponse400 | PatchServicesBINDAccessListEndpointResponse401 | PatchServicesBINDAccessListEndpointResponse403 | PatchServicesBINDAccessListEndpointResponse404 | PatchServicesBINDAccessListEndpointResponse405 | PatchServicesBINDAccessListEndpointResponse406 | PatchServicesBINDAccessListEndpointResponse409 | PatchServicesBINDAccessListEndpointResponse415 | PatchServicesBINDAccessListEndpointResponse422 | PatchServicesBINDAccessListEndpointResponse424 | PatchServicesBINDAccessListEndpointResponse500 | PatchServicesBINDAccessListEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesBINDAccessListEndpointJsonBody | PatchServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesBINDAccessListEndpointResponse400
    | PatchServicesBINDAccessListEndpointResponse401
    | PatchServicesBINDAccessListEndpointResponse403
    | PatchServicesBINDAccessListEndpointResponse404
    | PatchServicesBINDAccessListEndpointResponse405
    | PatchServicesBINDAccessListEndpointResponse406
    | PatchServicesBINDAccessListEndpointResponse409
    | PatchServicesBINDAccessListEndpointResponse415
    | PatchServicesBINDAccessListEndpointResponse422
    | PatchServicesBINDAccessListEndpointResponse424
    | PatchServicesBINDAccessListEndpointResponse500
    | PatchServicesBINDAccessListEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing BIND Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-list-patch ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDAccessListEndpointJsonBody | Unset):
        body (PatchServicesBINDAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesBINDAccessListEndpointResponse400 | PatchServicesBINDAccessListEndpointResponse401 | PatchServicesBINDAccessListEndpointResponse403 | PatchServicesBINDAccessListEndpointResponse404 | PatchServicesBINDAccessListEndpointResponse405 | PatchServicesBINDAccessListEndpointResponse406 | PatchServicesBINDAccessListEndpointResponse409 | PatchServicesBINDAccessListEndpointResponse415 | PatchServicesBINDAccessListEndpointResponse422 | PatchServicesBINDAccessListEndpointResponse424 | PatchServicesBINDAccessListEndpointResponse500 | PatchServicesBINDAccessListEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesBINDAccessListEndpointJsonBody | PatchServicesBINDAccessListEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesBINDAccessListEndpointResponse400
    | PatchServicesBINDAccessListEndpointResponse401
    | PatchServicesBINDAccessListEndpointResponse403
    | PatchServicesBINDAccessListEndpointResponse404
    | PatchServicesBINDAccessListEndpointResponse405
    | PatchServicesBINDAccessListEndpointResponse406
    | PatchServicesBINDAccessListEndpointResponse409
    | PatchServicesBINDAccessListEndpointResponse415
    | PatchServicesBINDAccessListEndpointResponse422
    | PatchServicesBINDAccessListEndpointResponse424
    | PatchServicesBINDAccessListEndpointResponse500
    | PatchServicesBINDAccessListEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing BIND Access List.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: BINDAccessList<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-bind-access-list-patch ]<br>**Required
    packages**: [ pfSense-pkg-bind ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesBINDAccessListEndpointJsonBody | Unset):
        body (PatchServicesBINDAccessListEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesBINDAccessListEndpointResponse400 | PatchServicesBINDAccessListEndpointResponse401 | PatchServicesBINDAccessListEndpointResponse403 | PatchServicesBINDAccessListEndpointResponse404 | PatchServicesBINDAccessListEndpointResponse405 | PatchServicesBINDAccessListEndpointResponse406 | PatchServicesBINDAccessListEndpointResponse409 | PatchServicesBINDAccessListEndpointResponse415 | PatchServicesBINDAccessListEndpointResponse422 | PatchServicesBINDAccessListEndpointResponse424 | PatchServicesBINDAccessListEndpointResponse500 | PatchServicesBINDAccessListEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
