from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_ssh_endpoint_data_body import PatchServicesSSHEndpointDataBody
from ...models.patch_services_ssh_endpoint_json_body import PatchServicesSSHEndpointJsonBody
from ...models.patch_services_ssh_endpoint_response_400 import PatchServicesSSHEndpointResponse400
from ...models.patch_services_ssh_endpoint_response_401 import PatchServicesSSHEndpointResponse401
from ...models.patch_services_ssh_endpoint_response_403 import PatchServicesSSHEndpointResponse403
from ...models.patch_services_ssh_endpoint_response_404 import PatchServicesSSHEndpointResponse404
from ...models.patch_services_ssh_endpoint_response_405 import PatchServicesSSHEndpointResponse405
from ...models.patch_services_ssh_endpoint_response_406 import PatchServicesSSHEndpointResponse406
from ...models.patch_services_ssh_endpoint_response_409 import PatchServicesSSHEndpointResponse409
from ...models.patch_services_ssh_endpoint_response_415 import PatchServicesSSHEndpointResponse415
from ...models.patch_services_ssh_endpoint_response_422 import PatchServicesSSHEndpointResponse422
from ...models.patch_services_ssh_endpoint_response_424 import PatchServicesSSHEndpointResponse424
from ...models.patch_services_ssh_endpoint_response_500 import PatchServicesSSHEndpointResponse500
from ...models.patch_services_ssh_endpoint_response_503 import PatchServicesSSHEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesSSHEndpointJsonBody | PatchServicesSSHEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/ssh",
    }

    if isinstance(body, PatchServicesSSHEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesSSHEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesSSHEndpointResponse400
    | PatchServicesSSHEndpointResponse401
    | PatchServicesSSHEndpointResponse403
    | PatchServicesSSHEndpointResponse404
    | PatchServicesSSHEndpointResponse405
    | PatchServicesSSHEndpointResponse406
    | PatchServicesSSHEndpointResponse409
    | PatchServicesSSHEndpointResponse415
    | PatchServicesSSHEndpointResponse422
    | PatchServicesSSHEndpointResponse424
    | PatchServicesSSHEndpointResponse500
    | PatchServicesSSHEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesSSHEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesSSHEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesSSHEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesSSHEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesSSHEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesSSHEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesSSHEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesSSHEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesSSHEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesSSHEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesSSHEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesSSHEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesSSHEndpointResponse400
    | PatchServicesSSHEndpointResponse401
    | PatchServicesSSHEndpointResponse403
    | PatchServicesSSHEndpointResponse404
    | PatchServicesSSHEndpointResponse405
    | PatchServicesSSHEndpointResponse406
    | PatchServicesSSHEndpointResponse409
    | PatchServicesSSHEndpointResponse415
    | PatchServicesSSHEndpointResponse422
    | PatchServicesSSHEndpointResponse424
    | PatchServicesSSHEndpointResponse500
    | PatchServicesSSHEndpointResponse503
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
    body: PatchServicesSSHEndpointJsonBody | PatchServicesSSHEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesSSHEndpointResponse400
    | PatchServicesSSHEndpointResponse401
    | PatchServicesSSHEndpointResponse403
    | PatchServicesSSHEndpointResponse404
    | PatchServicesSSHEndpointResponse405
    | PatchServicesSSHEndpointResponse406
    | PatchServicesSSHEndpointResponse409
    | PatchServicesSSHEndpointResponse415
    | PatchServicesSSHEndpointResponse422
    | PatchServicesSSHEndpointResponse424
    | PatchServicesSSHEndpointResponse500
    | PatchServicesSSHEndpointResponse503
]:
    """<h3>Description:</h3>Updates the current SSH server settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SSH<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-ssh-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesSSHEndpointJsonBody | Unset):
        body (PatchServicesSSHEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesSSHEndpointResponse400 | PatchServicesSSHEndpointResponse401 | PatchServicesSSHEndpointResponse403 | PatchServicesSSHEndpointResponse404 | PatchServicesSSHEndpointResponse405 | PatchServicesSSHEndpointResponse406 | PatchServicesSSHEndpointResponse409 | PatchServicesSSHEndpointResponse415 | PatchServicesSSHEndpointResponse422 | PatchServicesSSHEndpointResponse424 | PatchServicesSSHEndpointResponse500 | PatchServicesSSHEndpointResponse503]
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
    body: PatchServicesSSHEndpointJsonBody | PatchServicesSSHEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesSSHEndpointResponse400
    | PatchServicesSSHEndpointResponse401
    | PatchServicesSSHEndpointResponse403
    | PatchServicesSSHEndpointResponse404
    | PatchServicesSSHEndpointResponse405
    | PatchServicesSSHEndpointResponse406
    | PatchServicesSSHEndpointResponse409
    | PatchServicesSSHEndpointResponse415
    | PatchServicesSSHEndpointResponse422
    | PatchServicesSSHEndpointResponse424
    | PatchServicesSSHEndpointResponse500
    | PatchServicesSSHEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates the current SSH server settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SSH<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-ssh-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesSSHEndpointJsonBody | Unset):
        body (PatchServicesSSHEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesSSHEndpointResponse400 | PatchServicesSSHEndpointResponse401 | PatchServicesSSHEndpointResponse403 | PatchServicesSSHEndpointResponse404 | PatchServicesSSHEndpointResponse405 | PatchServicesSSHEndpointResponse406 | PatchServicesSSHEndpointResponse409 | PatchServicesSSHEndpointResponse415 | PatchServicesSSHEndpointResponse422 | PatchServicesSSHEndpointResponse424 | PatchServicesSSHEndpointResponse500 | PatchServicesSSHEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesSSHEndpointJsonBody | PatchServicesSSHEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesSSHEndpointResponse400
    | PatchServicesSSHEndpointResponse401
    | PatchServicesSSHEndpointResponse403
    | PatchServicesSSHEndpointResponse404
    | PatchServicesSSHEndpointResponse405
    | PatchServicesSSHEndpointResponse406
    | PatchServicesSSHEndpointResponse409
    | PatchServicesSSHEndpointResponse415
    | PatchServicesSSHEndpointResponse422
    | PatchServicesSSHEndpointResponse424
    | PatchServicesSSHEndpointResponse500
    | PatchServicesSSHEndpointResponse503
]:
    """<h3>Description:</h3>Updates the current SSH server settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SSH<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-ssh-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesSSHEndpointJsonBody | Unset):
        body (PatchServicesSSHEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesSSHEndpointResponse400 | PatchServicesSSHEndpointResponse401 | PatchServicesSSHEndpointResponse403 | PatchServicesSSHEndpointResponse404 | PatchServicesSSHEndpointResponse405 | PatchServicesSSHEndpointResponse406 | PatchServicesSSHEndpointResponse409 | PatchServicesSSHEndpointResponse415 | PatchServicesSSHEndpointResponse422 | PatchServicesSSHEndpointResponse424 | PatchServicesSSHEndpointResponse500 | PatchServicesSSHEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesSSHEndpointJsonBody | PatchServicesSSHEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesSSHEndpointResponse400
    | PatchServicesSSHEndpointResponse401
    | PatchServicesSSHEndpointResponse403
    | PatchServicesSSHEndpointResponse404
    | PatchServicesSSHEndpointResponse405
    | PatchServicesSSHEndpointResponse406
    | PatchServicesSSHEndpointResponse409
    | PatchServicesSSHEndpointResponse415
    | PatchServicesSSHEndpointResponse422
    | PatchServicesSSHEndpointResponse424
    | PatchServicesSSHEndpointResponse500
    | PatchServicesSSHEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates the current SSH server settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SSH<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-services-ssh-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesSSHEndpointJsonBody | Unset):
        body (PatchServicesSSHEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesSSHEndpointResponse400 | PatchServicesSSHEndpointResponse401 | PatchServicesSSHEndpointResponse403 | PatchServicesSSHEndpointResponse404 | PatchServicesSSHEndpointResponse405 | PatchServicesSSHEndpointResponse406 | PatchServicesSSHEndpointResponse409 | PatchServicesSSHEndpointResponse415 | PatchServicesSSHEndpointResponse422 | PatchServicesSSHEndpointResponse424 | PatchServicesSSHEndpointResponse500 | PatchServicesSSHEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
