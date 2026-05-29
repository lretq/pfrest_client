from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_system_dns_endpoint_data_body import PatchSystemDNSEndpointDataBody
from ...models.patch_system_dns_endpoint_json_body import PatchSystemDNSEndpointJsonBody
from ...models.patch_system_dns_endpoint_response_400 import PatchSystemDNSEndpointResponse400
from ...models.patch_system_dns_endpoint_response_401 import PatchSystemDNSEndpointResponse401
from ...models.patch_system_dns_endpoint_response_403 import PatchSystemDNSEndpointResponse403
from ...models.patch_system_dns_endpoint_response_404 import PatchSystemDNSEndpointResponse404
from ...models.patch_system_dns_endpoint_response_405 import PatchSystemDNSEndpointResponse405
from ...models.patch_system_dns_endpoint_response_406 import PatchSystemDNSEndpointResponse406
from ...models.patch_system_dns_endpoint_response_409 import PatchSystemDNSEndpointResponse409
from ...models.patch_system_dns_endpoint_response_415 import PatchSystemDNSEndpointResponse415
from ...models.patch_system_dns_endpoint_response_422 import PatchSystemDNSEndpointResponse422
from ...models.patch_system_dns_endpoint_response_424 import PatchSystemDNSEndpointResponse424
from ...models.patch_system_dns_endpoint_response_500 import PatchSystemDNSEndpointResponse500
from ...models.patch_system_dns_endpoint_response_503 import PatchSystemDNSEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchSystemDNSEndpointJsonBody | PatchSystemDNSEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/system/dns",
    }

    if isinstance(body, PatchSystemDNSEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchSystemDNSEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchSystemDNSEndpointResponse400
    | PatchSystemDNSEndpointResponse401
    | PatchSystemDNSEndpointResponse403
    | PatchSystemDNSEndpointResponse404
    | PatchSystemDNSEndpointResponse405
    | PatchSystemDNSEndpointResponse406
    | PatchSystemDNSEndpointResponse409
    | PatchSystemDNSEndpointResponse415
    | PatchSystemDNSEndpointResponse422
    | PatchSystemDNSEndpointResponse424
    | PatchSystemDNSEndpointResponse500
    | PatchSystemDNSEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchSystemDNSEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchSystemDNSEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchSystemDNSEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchSystemDNSEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchSystemDNSEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchSystemDNSEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchSystemDNSEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchSystemDNSEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchSystemDNSEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchSystemDNSEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchSystemDNSEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchSystemDNSEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchSystemDNSEndpointResponse400
    | PatchSystemDNSEndpointResponse401
    | PatchSystemDNSEndpointResponse403
    | PatchSystemDNSEndpointResponse404
    | PatchSystemDNSEndpointResponse405
    | PatchSystemDNSEndpointResponse406
    | PatchSystemDNSEndpointResponse409
    | PatchSystemDNSEndpointResponse415
    | PatchSystemDNSEndpointResponse422
    | PatchSystemDNSEndpointResponse424
    | PatchSystemDNSEndpointResponse500
    | PatchSystemDNSEndpointResponse503
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
    body: PatchSystemDNSEndpointJsonBody | PatchSystemDNSEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemDNSEndpointResponse400
    | PatchSystemDNSEndpointResponse401
    | PatchSystemDNSEndpointResponse403
    | PatchSystemDNSEndpointResponse404
    | PatchSystemDNSEndpointResponse405
    | PatchSystemDNSEndpointResponse406
    | PatchSystemDNSEndpointResponse409
    | PatchSystemDNSEndpointResponse415
    | PatchSystemDNSEndpointResponse422
    | PatchSystemDNSEndpointResponse424
    | PatchSystemDNSEndpointResponse500
    | PatchSystemDNSEndpointResponse503
]:
    """<h3>Description:</h3>Updates the current system DNS settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemDNS<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-dns-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemDNSEndpointJsonBody | Unset):
        body (PatchSystemDNSEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemDNSEndpointResponse400 | PatchSystemDNSEndpointResponse401 | PatchSystemDNSEndpointResponse403 | PatchSystemDNSEndpointResponse404 | PatchSystemDNSEndpointResponse405 | PatchSystemDNSEndpointResponse406 | PatchSystemDNSEndpointResponse409 | PatchSystemDNSEndpointResponse415 | PatchSystemDNSEndpointResponse422 | PatchSystemDNSEndpointResponse424 | PatchSystemDNSEndpointResponse500 | PatchSystemDNSEndpointResponse503]
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
    body: PatchSystemDNSEndpointJsonBody | PatchSystemDNSEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemDNSEndpointResponse400
    | PatchSystemDNSEndpointResponse401
    | PatchSystemDNSEndpointResponse403
    | PatchSystemDNSEndpointResponse404
    | PatchSystemDNSEndpointResponse405
    | PatchSystemDNSEndpointResponse406
    | PatchSystemDNSEndpointResponse409
    | PatchSystemDNSEndpointResponse415
    | PatchSystemDNSEndpointResponse422
    | PatchSystemDNSEndpointResponse424
    | PatchSystemDNSEndpointResponse500
    | PatchSystemDNSEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates the current system DNS settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemDNS<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-dns-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemDNSEndpointJsonBody | Unset):
        body (PatchSystemDNSEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemDNSEndpointResponse400 | PatchSystemDNSEndpointResponse401 | PatchSystemDNSEndpointResponse403 | PatchSystemDNSEndpointResponse404 | PatchSystemDNSEndpointResponse405 | PatchSystemDNSEndpointResponse406 | PatchSystemDNSEndpointResponse409 | PatchSystemDNSEndpointResponse415 | PatchSystemDNSEndpointResponse422 | PatchSystemDNSEndpointResponse424 | PatchSystemDNSEndpointResponse500 | PatchSystemDNSEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemDNSEndpointJsonBody | PatchSystemDNSEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchSystemDNSEndpointResponse400
    | PatchSystemDNSEndpointResponse401
    | PatchSystemDNSEndpointResponse403
    | PatchSystemDNSEndpointResponse404
    | PatchSystemDNSEndpointResponse405
    | PatchSystemDNSEndpointResponse406
    | PatchSystemDNSEndpointResponse409
    | PatchSystemDNSEndpointResponse415
    | PatchSystemDNSEndpointResponse422
    | PatchSystemDNSEndpointResponse424
    | PatchSystemDNSEndpointResponse500
    | PatchSystemDNSEndpointResponse503
]:
    """<h3>Description:</h3>Updates the current system DNS settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemDNS<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-dns-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemDNSEndpointJsonBody | Unset):
        body (PatchSystemDNSEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSystemDNSEndpointResponse400 | PatchSystemDNSEndpointResponse401 | PatchSystemDNSEndpointResponse403 | PatchSystemDNSEndpointResponse404 | PatchSystemDNSEndpointResponse405 | PatchSystemDNSEndpointResponse406 | PatchSystemDNSEndpointResponse409 | PatchSystemDNSEndpointResponse415 | PatchSystemDNSEndpointResponse422 | PatchSystemDNSEndpointResponse424 | PatchSystemDNSEndpointResponse500 | PatchSystemDNSEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchSystemDNSEndpointJsonBody | PatchSystemDNSEndpointDataBody | Unset = UNSET,
) -> (
    PatchSystemDNSEndpointResponse400
    | PatchSystemDNSEndpointResponse401
    | PatchSystemDNSEndpointResponse403
    | PatchSystemDNSEndpointResponse404
    | PatchSystemDNSEndpointResponse405
    | PatchSystemDNSEndpointResponse406
    | PatchSystemDNSEndpointResponse409
    | PatchSystemDNSEndpointResponse415
    | PatchSystemDNSEndpointResponse422
    | PatchSystemDNSEndpointResponse424
    | PatchSystemDNSEndpointResponse500
    | PatchSystemDNSEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates the current system DNS settings.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: SystemDNS<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-system-dns-patch ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchSystemDNSEndpointJsonBody | Unset):
        body (PatchSystemDNSEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSystemDNSEndpointResponse400 | PatchSystemDNSEndpointResponse401 | PatchSystemDNSEndpointResponse403 | PatchSystemDNSEndpointResponse404 | PatchSystemDNSEndpointResponse405 | PatchSystemDNSEndpointResponse406 | PatchSystemDNSEndpointResponse409 | PatchSystemDNSEndpointResponse415 | PatchSystemDNSEndpointResponse422 | PatchSystemDNSEndpointResponse424 | PatchSystemDNSEndpointResponse500 | PatchSystemDNSEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
