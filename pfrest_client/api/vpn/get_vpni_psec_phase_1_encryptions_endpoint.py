from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_query import GetVPNIPsecPhase1EncryptionsEndpointQuery
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_400 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse400,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_401 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse401,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_403 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse403,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_404 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse404,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_405 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse405,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_406 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse406,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_409 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse409,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_415 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse415,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_422 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse422,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_424 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse424,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_500 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse500,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_response_503 import (
    GetVPNIPsecPhase1EncryptionsEndpointResponse503,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_sort_flags import (
    GetVPNIPsecPhase1EncryptionsEndpointSortFlags,
)
from ...models.get_vpni_psec_phase_1_encryptions_endpoint_sort_order import (
    GetVPNIPsecPhase1EncryptionsEndpointSortOrder,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset = UNSET,
    query: GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_sort_by: list[str] | None | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    elif isinstance(sort_by, list):
        json_sort_by = sort_by

    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    json_sort_flags: str | Unset = UNSET
    if not isinstance(sort_flags, Unset):
        json_sort_flags = sort_flags.value

    params["sort_flags"] = json_sort_flags

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/vpn/ipsec/phase1/encryptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetVPNIPsecPhase1EncryptionsEndpointResponse400
    | GetVPNIPsecPhase1EncryptionsEndpointResponse401
    | GetVPNIPsecPhase1EncryptionsEndpointResponse403
    | GetVPNIPsecPhase1EncryptionsEndpointResponse404
    | GetVPNIPsecPhase1EncryptionsEndpointResponse405
    | GetVPNIPsecPhase1EncryptionsEndpointResponse406
    | GetVPNIPsecPhase1EncryptionsEndpointResponse409
    | GetVPNIPsecPhase1EncryptionsEndpointResponse415
    | GetVPNIPsecPhase1EncryptionsEndpointResponse422
    | GetVPNIPsecPhase1EncryptionsEndpointResponse424
    | GetVPNIPsecPhase1EncryptionsEndpointResponse500
    | GetVPNIPsecPhase1EncryptionsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetVPNIPsecPhase1EncryptionsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetVPNIPsecPhase1EncryptionsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetVPNIPsecPhase1EncryptionsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVPNIPsecPhase1EncryptionsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetVPNIPsecPhase1EncryptionsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetVPNIPsecPhase1EncryptionsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetVPNIPsecPhase1EncryptionsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetVPNIPsecPhase1EncryptionsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetVPNIPsecPhase1EncryptionsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetVPNIPsecPhase1EncryptionsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetVPNIPsecPhase1EncryptionsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetVPNIPsecPhase1EncryptionsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetVPNIPsecPhase1EncryptionsEndpointResponse400
    | GetVPNIPsecPhase1EncryptionsEndpointResponse401
    | GetVPNIPsecPhase1EncryptionsEndpointResponse403
    | GetVPNIPsecPhase1EncryptionsEndpointResponse404
    | GetVPNIPsecPhase1EncryptionsEndpointResponse405
    | GetVPNIPsecPhase1EncryptionsEndpointResponse406
    | GetVPNIPsecPhase1EncryptionsEndpointResponse409
    | GetVPNIPsecPhase1EncryptionsEndpointResponse415
    | GetVPNIPsecPhase1EncryptionsEndpointResponse422
    | GetVPNIPsecPhase1EncryptionsEndpointResponse424
    | GetVPNIPsecPhase1EncryptionsEndpointResponse500
    | GetVPNIPsecPhase1EncryptionsEndpointResponse503
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
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset = UNSET,
    query: GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset = UNSET,
) -> Response[
    GetVPNIPsecPhase1EncryptionsEndpointResponse400
    | GetVPNIPsecPhase1EncryptionsEndpointResponse401
    | GetVPNIPsecPhase1EncryptionsEndpointResponse403
    | GetVPNIPsecPhase1EncryptionsEndpointResponse404
    | GetVPNIPsecPhase1EncryptionsEndpointResponse405
    | GetVPNIPsecPhase1EncryptionsEndpointResponse406
    | GetVPNIPsecPhase1EncryptionsEndpointResponse409
    | GetVPNIPsecPhase1EncryptionsEndpointResponse415
    | GetVPNIPsecPhase1EncryptionsEndpointResponse422
    | GetVPNIPsecPhase1EncryptionsEndpointResponse424
    | GetVPNIPsecPhase1EncryptionsEndpointResponse500
    | GetVPNIPsecPhase1EncryptionsEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing IPsec Phase 1 Encryptions.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: IPsecPhase1Encryption<br>**Parent model**:
    IPsecPhase1<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase1-encryptions-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset):
        sort_flags (GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset):
        query (GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNIPsecPhase1EncryptionsEndpointResponse400 | GetVPNIPsecPhase1EncryptionsEndpointResponse401 | GetVPNIPsecPhase1EncryptionsEndpointResponse403 | GetVPNIPsecPhase1EncryptionsEndpointResponse404 | GetVPNIPsecPhase1EncryptionsEndpointResponse405 | GetVPNIPsecPhase1EncryptionsEndpointResponse406 | GetVPNIPsecPhase1EncryptionsEndpointResponse409 | GetVPNIPsecPhase1EncryptionsEndpointResponse415 | GetVPNIPsecPhase1EncryptionsEndpointResponse422 | GetVPNIPsecPhase1EncryptionsEndpointResponse424 | GetVPNIPsecPhase1EncryptionsEndpointResponse500 | GetVPNIPsecPhase1EncryptionsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset = UNSET,
    query: GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset = UNSET,
) -> (
    GetVPNIPsecPhase1EncryptionsEndpointResponse400
    | GetVPNIPsecPhase1EncryptionsEndpointResponse401
    | GetVPNIPsecPhase1EncryptionsEndpointResponse403
    | GetVPNIPsecPhase1EncryptionsEndpointResponse404
    | GetVPNIPsecPhase1EncryptionsEndpointResponse405
    | GetVPNIPsecPhase1EncryptionsEndpointResponse406
    | GetVPNIPsecPhase1EncryptionsEndpointResponse409
    | GetVPNIPsecPhase1EncryptionsEndpointResponse415
    | GetVPNIPsecPhase1EncryptionsEndpointResponse422
    | GetVPNIPsecPhase1EncryptionsEndpointResponse424
    | GetVPNIPsecPhase1EncryptionsEndpointResponse500
    | GetVPNIPsecPhase1EncryptionsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing IPsec Phase 1 Encryptions.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: IPsecPhase1Encryption<br>**Parent model**:
    IPsecPhase1<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase1-encryptions-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset):
        sort_flags (GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset):
        query (GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNIPsecPhase1EncryptionsEndpointResponse400 | GetVPNIPsecPhase1EncryptionsEndpointResponse401 | GetVPNIPsecPhase1EncryptionsEndpointResponse403 | GetVPNIPsecPhase1EncryptionsEndpointResponse404 | GetVPNIPsecPhase1EncryptionsEndpointResponse405 | GetVPNIPsecPhase1EncryptionsEndpointResponse406 | GetVPNIPsecPhase1EncryptionsEndpointResponse409 | GetVPNIPsecPhase1EncryptionsEndpointResponse415 | GetVPNIPsecPhase1EncryptionsEndpointResponse422 | GetVPNIPsecPhase1EncryptionsEndpointResponse424 | GetVPNIPsecPhase1EncryptionsEndpointResponse500 | GetVPNIPsecPhase1EncryptionsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset = UNSET,
    query: GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset = UNSET,
) -> Response[
    GetVPNIPsecPhase1EncryptionsEndpointResponse400
    | GetVPNIPsecPhase1EncryptionsEndpointResponse401
    | GetVPNIPsecPhase1EncryptionsEndpointResponse403
    | GetVPNIPsecPhase1EncryptionsEndpointResponse404
    | GetVPNIPsecPhase1EncryptionsEndpointResponse405
    | GetVPNIPsecPhase1EncryptionsEndpointResponse406
    | GetVPNIPsecPhase1EncryptionsEndpointResponse409
    | GetVPNIPsecPhase1EncryptionsEndpointResponse415
    | GetVPNIPsecPhase1EncryptionsEndpointResponse422
    | GetVPNIPsecPhase1EncryptionsEndpointResponse424
    | GetVPNIPsecPhase1EncryptionsEndpointResponse500
    | GetVPNIPsecPhase1EncryptionsEndpointResponse503
]:
    """<h3>Description:</h3>Reads all existing IPsec Phase 1 Encryptions.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: IPsecPhase1Encryption<br>**Parent model**:
    IPsecPhase1<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase1-encryptions-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset):
        sort_flags (GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset):
        query (GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVPNIPsecPhase1EncryptionsEndpointResponse400 | GetVPNIPsecPhase1EncryptionsEndpointResponse401 | GetVPNIPsecPhase1EncryptionsEndpointResponse403 | GetVPNIPsecPhase1EncryptionsEndpointResponse404 | GetVPNIPsecPhase1EncryptionsEndpointResponse405 | GetVPNIPsecPhase1EncryptionsEndpointResponse406 | GetVPNIPsecPhase1EncryptionsEndpointResponse409 | GetVPNIPsecPhase1EncryptionsEndpointResponse415 | GetVPNIPsecPhase1EncryptionsEndpointResponse422 | GetVPNIPsecPhase1EncryptionsEndpointResponse424 | GetVPNIPsecPhase1EncryptionsEndpointResponse500 | GetVPNIPsecPhase1EncryptionsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_order=sort_order,
        sort_flags=sort_flags,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    sort_by: list[str] | None | Unset = UNSET,
    sort_order: GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset = UNSET,
    sort_flags: GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset = UNSET,
    query: GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset = UNSET,
) -> (
    GetVPNIPsecPhase1EncryptionsEndpointResponse400
    | GetVPNIPsecPhase1EncryptionsEndpointResponse401
    | GetVPNIPsecPhase1EncryptionsEndpointResponse403
    | GetVPNIPsecPhase1EncryptionsEndpointResponse404
    | GetVPNIPsecPhase1EncryptionsEndpointResponse405
    | GetVPNIPsecPhase1EncryptionsEndpointResponse406
    | GetVPNIPsecPhase1EncryptionsEndpointResponse409
    | GetVPNIPsecPhase1EncryptionsEndpointResponse415
    | GetVPNIPsecPhase1EncryptionsEndpointResponse422
    | GetVPNIPsecPhase1EncryptionsEndpointResponse424
    | GetVPNIPsecPhase1EncryptionsEndpointResponse500
    | GetVPNIPsecPhase1EncryptionsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads all existing IPsec Phase 1 Encryptions.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: IPsecPhase1Encryption<br>**Parent model**:
    IPsecPhase1<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-vpn-ipsec-phase1-encryptions-get
    ]<br>**Required packages**: [ None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        sort_by (list[str] | None | Unset):
        sort_order (GetVPNIPsecPhase1EncryptionsEndpointSortOrder | Unset):
        sort_flags (GetVPNIPsecPhase1EncryptionsEndpointSortFlags | Unset):
        query (GetVPNIPsecPhase1EncryptionsEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVPNIPsecPhase1EncryptionsEndpointResponse400 | GetVPNIPsecPhase1EncryptionsEndpointResponse401 | GetVPNIPsecPhase1EncryptionsEndpointResponse403 | GetVPNIPsecPhase1EncryptionsEndpointResponse404 | GetVPNIPsecPhase1EncryptionsEndpointResponse405 | GetVPNIPsecPhase1EncryptionsEndpointResponse406 | GetVPNIPsecPhase1EncryptionsEndpointResponse409 | GetVPNIPsecPhase1EncryptionsEndpointResponse415 | GetVPNIPsecPhase1EncryptionsEndpointResponse422 | GetVPNIPsecPhase1EncryptionsEndpointResponse424 | GetVPNIPsecPhase1EncryptionsEndpointResponse500 | GetVPNIPsecPhase1EncryptionsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            sort_flags=sort_flags,
            query=query,
        )
    ).parsed
