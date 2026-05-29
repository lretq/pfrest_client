from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_diagnostics_config_history_revision_endpoint_response_400 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse400,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_401 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse401,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_403 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse403,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_404 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse404,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_405 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse405,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_406 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse406,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_409 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse409,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_415 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse415,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_422 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse422,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_424 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse424,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_500 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse500,
)
from ...models.get_diagnostics_config_history_revision_endpoint_response_503 import (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/diagnostics/config_history/revision",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse400
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse401
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse403
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse404
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse405
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse406
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse409
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse415
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse422
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse424
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse500
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetDiagnosticsConfigHistoryRevisionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetDiagnosticsConfigHistoryRevisionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetDiagnosticsConfigHistoryRevisionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDiagnosticsConfigHistoryRevisionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetDiagnosticsConfigHistoryRevisionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetDiagnosticsConfigHistoryRevisionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetDiagnosticsConfigHistoryRevisionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetDiagnosticsConfigHistoryRevisionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetDiagnosticsConfigHistoryRevisionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetDiagnosticsConfigHistoryRevisionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetDiagnosticsConfigHistoryRevisionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetDiagnosticsConfigHistoryRevisionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetDiagnosticsConfigHistoryRevisionEndpointResponse400
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse401
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse403
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse404
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse405
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse406
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse409
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse415
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse422
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse424
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse500
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse503
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
) -> Response[
    GetDiagnosticsConfigHistoryRevisionEndpointResponse400
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse401
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse403
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse404
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse405
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse406
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse409
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse415
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse422
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse424
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse500
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Configuration History Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ConfigHistoryRevision<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-config-history-
    revision-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDiagnosticsConfigHistoryRevisionEndpointResponse400 | GetDiagnosticsConfigHistoryRevisionEndpointResponse401 | GetDiagnosticsConfigHistoryRevisionEndpointResponse403 | GetDiagnosticsConfigHistoryRevisionEndpointResponse404 | GetDiagnosticsConfigHistoryRevisionEndpointResponse405 | GetDiagnosticsConfigHistoryRevisionEndpointResponse406 | GetDiagnosticsConfigHistoryRevisionEndpointResponse409 | GetDiagnosticsConfigHistoryRevisionEndpointResponse415 | GetDiagnosticsConfigHistoryRevisionEndpointResponse422 | GetDiagnosticsConfigHistoryRevisionEndpointResponse424 | GetDiagnosticsConfigHistoryRevisionEndpointResponse500 | GetDiagnosticsConfigHistoryRevisionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse400
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse401
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse403
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse404
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse405
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse406
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse409
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse415
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse422
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse424
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse500
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Configuration History Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ConfigHistoryRevision<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-config-history-
    revision-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDiagnosticsConfigHistoryRevisionEndpointResponse400 | GetDiagnosticsConfigHistoryRevisionEndpointResponse401 | GetDiagnosticsConfigHistoryRevisionEndpointResponse403 | GetDiagnosticsConfigHistoryRevisionEndpointResponse404 | GetDiagnosticsConfigHistoryRevisionEndpointResponse405 | GetDiagnosticsConfigHistoryRevisionEndpointResponse406 | GetDiagnosticsConfigHistoryRevisionEndpointResponse409 | GetDiagnosticsConfigHistoryRevisionEndpointResponse415 | GetDiagnosticsConfigHistoryRevisionEndpointResponse422 | GetDiagnosticsConfigHistoryRevisionEndpointResponse424 | GetDiagnosticsConfigHistoryRevisionEndpointResponse500 | GetDiagnosticsConfigHistoryRevisionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> Response[
    GetDiagnosticsConfigHistoryRevisionEndpointResponse400
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse401
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse403
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse404
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse405
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse406
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse409
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse415
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse422
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse424
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse500
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Configuration History Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ConfigHistoryRevision<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-config-history-
    revision-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDiagnosticsConfigHistoryRevisionEndpointResponse400 | GetDiagnosticsConfigHistoryRevisionEndpointResponse401 | GetDiagnosticsConfigHistoryRevisionEndpointResponse403 | GetDiagnosticsConfigHistoryRevisionEndpointResponse404 | GetDiagnosticsConfigHistoryRevisionEndpointResponse405 | GetDiagnosticsConfigHistoryRevisionEndpointResponse406 | GetDiagnosticsConfigHistoryRevisionEndpointResponse409 | GetDiagnosticsConfigHistoryRevisionEndpointResponse415 | GetDiagnosticsConfigHistoryRevisionEndpointResponse422 | GetDiagnosticsConfigHistoryRevisionEndpointResponse424 | GetDiagnosticsConfigHistoryRevisionEndpointResponse500 | GetDiagnosticsConfigHistoryRevisionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: int | str,
) -> (
    GetDiagnosticsConfigHistoryRevisionEndpointResponse400
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse401
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse403
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse404
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse405
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse406
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse409
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse415
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse422
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse424
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse500
    | GetDiagnosticsConfigHistoryRevisionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Configuration History Entry.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ConfigHistoryRevision<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-diagnostics-config-history-
    revision-get ]<br>**Required packages**: [ None ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDiagnosticsConfigHistoryRevisionEndpointResponse400 | GetDiagnosticsConfigHistoryRevisionEndpointResponse401 | GetDiagnosticsConfigHistoryRevisionEndpointResponse403 | GetDiagnosticsConfigHistoryRevisionEndpointResponse404 | GetDiagnosticsConfigHistoryRevisionEndpointResponse405 | GetDiagnosticsConfigHistoryRevisionEndpointResponse406 | GetDiagnosticsConfigHistoryRevisionEndpointResponse409 | GetDiagnosticsConfigHistoryRevisionEndpointResponse415 | GetDiagnosticsConfigHistoryRevisionEndpointResponse422 | GetDiagnosticsConfigHistoryRevisionEndpointResponse424 | GetDiagnosticsConfigHistoryRevisionEndpointResponse500 | GetDiagnosticsConfigHistoryRevisionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
