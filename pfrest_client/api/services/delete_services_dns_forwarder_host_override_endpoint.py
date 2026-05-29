from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_400 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse400,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_401 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse401,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_403 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse403,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_404 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse404,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_405 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse405,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_406 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse406,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_409 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse409,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_415 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse415,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_422 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse422,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_424 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse424,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_500 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse500,
)
from ...models.delete_services_dns_forwarder_host_override_endpoint_response_503 import (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | str,
    apply: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params["apply"] = apply

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/dns_forwarder/host_override",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesDNSForwarderHostOverrideEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesDNSForwarderHostOverrideEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesDNSForwarderHostOverrideEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesDNSForwarderHostOverrideEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesDNSForwarderHostOverrideEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesDNSForwarderHostOverrideEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesDNSForwarderHostOverrideEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesDNSForwarderHostOverrideEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesDNSForwarderHostOverrideEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesDNSForwarderHostOverrideEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesDNSForwarderHostOverrideEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesDNSForwarderHostOverrideEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesDNSForwarderHostOverrideEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse503
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
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDNSForwarderHostOverrideEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DNS Forwarder Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-
    override-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDNSForwarderHostOverrideEndpointResponse400 | DeleteServicesDNSForwarderHostOverrideEndpointResponse401 | DeleteServicesDNSForwarderHostOverrideEndpointResponse403 | DeleteServicesDNSForwarderHostOverrideEndpointResponse404 | DeleteServicesDNSForwarderHostOverrideEndpointResponse405 | DeleteServicesDNSForwarderHostOverrideEndpointResponse406 | DeleteServicesDNSForwarderHostOverrideEndpointResponse409 | DeleteServicesDNSForwarderHostOverrideEndpointResponse415 | DeleteServicesDNSForwarderHostOverrideEndpointResponse422 | DeleteServicesDNSForwarderHostOverrideEndpointResponse424 | DeleteServicesDNSForwarderHostOverrideEndpointResponse500 | DeleteServicesDNSForwarderHostOverrideEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
        apply=apply,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DNS Forwarder Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-
    override-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDNSForwarderHostOverrideEndpointResponse400 | DeleteServicesDNSForwarderHostOverrideEndpointResponse401 | DeleteServicesDNSForwarderHostOverrideEndpointResponse403 | DeleteServicesDNSForwarderHostOverrideEndpointResponse404 | DeleteServicesDNSForwarderHostOverrideEndpointResponse405 | DeleteServicesDNSForwarderHostOverrideEndpointResponse406 | DeleteServicesDNSForwarderHostOverrideEndpointResponse409 | DeleteServicesDNSForwarderHostOverrideEndpointResponse415 | DeleteServicesDNSForwarderHostOverrideEndpointResponse422 | DeleteServicesDNSForwarderHostOverrideEndpointResponse424 | DeleteServicesDNSForwarderHostOverrideEndpointResponse500 | DeleteServicesDNSForwarderHostOverrideEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
        apply=apply,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> Response[
    DeleteServicesDNSForwarderHostOverrideEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing DNS Forwarder Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-
    override-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesDNSForwarderHostOverrideEndpointResponse400 | DeleteServicesDNSForwarderHostOverrideEndpointResponse401 | DeleteServicesDNSForwarderHostOverrideEndpointResponse403 | DeleteServicesDNSForwarderHostOverrideEndpointResponse404 | DeleteServicesDNSForwarderHostOverrideEndpointResponse405 | DeleteServicesDNSForwarderHostOverrideEndpointResponse406 | DeleteServicesDNSForwarderHostOverrideEndpointResponse409 | DeleteServicesDNSForwarderHostOverrideEndpointResponse415 | DeleteServicesDNSForwarderHostOverrideEndpointResponse422 | DeleteServicesDNSForwarderHostOverrideEndpointResponse424 | DeleteServicesDNSForwarderHostOverrideEndpointResponse500 | DeleteServicesDNSForwarderHostOverrideEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
        apply=apply,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
    apply: bool | Unset = False,
) -> (
    DeleteServicesDNSForwarderHostOverrideEndpointResponse400
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse401
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse403
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse404
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse405
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse406
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse409
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse415
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse422
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse424
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse500
    | DeleteServicesDNSForwarderHostOverrideEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing DNS Forwarder Host Override.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: DNSForwarderHostOverride<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-dns-forwarder-host-
    override-delete ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes
    cache**: None

    Args:
        id (int | str):
        apply (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesDNSForwarderHostOverrideEndpointResponse400 | DeleteServicesDNSForwarderHostOverrideEndpointResponse401 | DeleteServicesDNSForwarderHostOverrideEndpointResponse403 | DeleteServicesDNSForwarderHostOverrideEndpointResponse404 | DeleteServicesDNSForwarderHostOverrideEndpointResponse405 | DeleteServicesDNSForwarderHostOverrideEndpointResponse406 | DeleteServicesDNSForwarderHostOverrideEndpointResponse409 | DeleteServicesDNSForwarderHostOverrideEndpointResponse415 | DeleteServicesDNSForwarderHostOverrideEndpointResponse422 | DeleteServicesDNSForwarderHostOverrideEndpointResponse424 | DeleteServicesDNSForwarderHostOverrideEndpointResponse500 | DeleteServicesDNSForwarderHostOverrideEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            apply=apply,
        )
    ).parsed
