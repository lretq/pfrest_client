from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_interface_gre_endpoint_response_400 import GetInterfaceGREEndpointResponse400
from ...models.get_interface_gre_endpoint_response_401 import GetInterfaceGREEndpointResponse401
from ...models.get_interface_gre_endpoint_response_403 import GetInterfaceGREEndpointResponse403
from ...models.get_interface_gre_endpoint_response_404 import GetInterfaceGREEndpointResponse404
from ...models.get_interface_gre_endpoint_response_405 import GetInterfaceGREEndpointResponse405
from ...models.get_interface_gre_endpoint_response_406 import GetInterfaceGREEndpointResponse406
from ...models.get_interface_gre_endpoint_response_409 import GetInterfaceGREEndpointResponse409
from ...models.get_interface_gre_endpoint_response_415 import GetInterfaceGREEndpointResponse415
from ...models.get_interface_gre_endpoint_response_422 import GetInterfaceGREEndpointResponse422
from ...models.get_interface_gre_endpoint_response_424 import GetInterfaceGREEndpointResponse424
from ...models.get_interface_gre_endpoint_response_500 import GetInterfaceGREEndpointResponse500
from ...models.get_interface_gre_endpoint_response_503 import GetInterfaceGREEndpointResponse503
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
        "url": "/api/v2/interface/gre",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetInterfaceGREEndpointResponse400
    | GetInterfaceGREEndpointResponse401
    | GetInterfaceGREEndpointResponse403
    | GetInterfaceGREEndpointResponse404
    | GetInterfaceGREEndpointResponse405
    | GetInterfaceGREEndpointResponse406
    | GetInterfaceGREEndpointResponse409
    | GetInterfaceGREEndpointResponse415
    | GetInterfaceGREEndpointResponse422
    | GetInterfaceGREEndpointResponse424
    | GetInterfaceGREEndpointResponse500
    | GetInterfaceGREEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetInterfaceGREEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetInterfaceGREEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetInterfaceGREEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetInterfaceGREEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetInterfaceGREEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetInterfaceGREEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetInterfaceGREEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetInterfaceGREEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetInterfaceGREEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetInterfaceGREEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetInterfaceGREEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetInterfaceGREEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetInterfaceGREEndpointResponse400
    | GetInterfaceGREEndpointResponse401
    | GetInterfaceGREEndpointResponse403
    | GetInterfaceGREEndpointResponse404
    | GetInterfaceGREEndpointResponse405
    | GetInterfaceGREEndpointResponse406
    | GetInterfaceGREEndpointResponse409
    | GetInterfaceGREEndpointResponse415
    | GetInterfaceGREEndpointResponse422
    | GetInterfaceGREEndpointResponse424
    | GetInterfaceGREEndpointResponse500
    | GetInterfaceGREEndpointResponse503
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
    GetInterfaceGREEndpointResponse400
    | GetInterfaceGREEndpointResponse401
    | GetInterfaceGREEndpointResponse403
    | GetInterfaceGREEndpointResponse404
    | GetInterfaceGREEndpointResponse405
    | GetInterfaceGREEndpointResponse406
    | GetInterfaceGREEndpointResponse409
    | GetInterfaceGREEndpointResponse415
    | GetInterfaceGREEndpointResponse422
    | GetInterfaceGREEndpointResponse424
    | GetInterfaceGREEndpointResponse500
    | GetInterfaceGREEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInterfaceGREEndpointResponse400 | GetInterfaceGREEndpointResponse401 | GetInterfaceGREEndpointResponse403 | GetInterfaceGREEndpointResponse404 | GetInterfaceGREEndpointResponse405 | GetInterfaceGREEndpointResponse406 | GetInterfaceGREEndpointResponse409 | GetInterfaceGREEndpointResponse415 | GetInterfaceGREEndpointResponse422 | GetInterfaceGREEndpointResponse424 | GetInterfaceGREEndpointResponse500 | GetInterfaceGREEndpointResponse503]
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
    GetInterfaceGREEndpointResponse400
    | GetInterfaceGREEndpointResponse401
    | GetInterfaceGREEndpointResponse403
    | GetInterfaceGREEndpointResponse404
    | GetInterfaceGREEndpointResponse405
    | GetInterfaceGREEndpointResponse406
    | GetInterfaceGREEndpointResponse409
    | GetInterfaceGREEndpointResponse415
    | GetInterfaceGREEndpointResponse422
    | GetInterfaceGREEndpointResponse424
    | GetInterfaceGREEndpointResponse500
    | GetInterfaceGREEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInterfaceGREEndpointResponse400 | GetInterfaceGREEndpointResponse401 | GetInterfaceGREEndpointResponse403 | GetInterfaceGREEndpointResponse404 | GetInterfaceGREEndpointResponse405 | GetInterfaceGREEndpointResponse406 | GetInterfaceGREEndpointResponse409 | GetInterfaceGREEndpointResponse415 | GetInterfaceGREEndpointResponse422 | GetInterfaceGREEndpointResponse424 | GetInterfaceGREEndpointResponse500 | GetInterfaceGREEndpointResponse503
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
    GetInterfaceGREEndpointResponse400
    | GetInterfaceGREEndpointResponse401
    | GetInterfaceGREEndpointResponse403
    | GetInterfaceGREEndpointResponse404
    | GetInterfaceGREEndpointResponse405
    | GetInterfaceGREEndpointResponse406
    | GetInterfaceGREEndpointResponse409
    | GetInterfaceGREEndpointResponse415
    | GetInterfaceGREEndpointResponse422
    | GetInterfaceGREEndpointResponse424
    | GetInterfaceGREEndpointResponse500
    | GetInterfaceGREEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInterfaceGREEndpointResponse400 | GetInterfaceGREEndpointResponse401 | GetInterfaceGREEndpointResponse403 | GetInterfaceGREEndpointResponse404 | GetInterfaceGREEndpointResponse405 | GetInterfaceGREEndpointResponse406 | GetInterfaceGREEndpointResponse409 | GetInterfaceGREEndpointResponse415 | GetInterfaceGREEndpointResponse422 | GetInterfaceGREEndpointResponse424 | GetInterfaceGREEndpointResponse500 | GetInterfaceGREEndpointResponse503]
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
    GetInterfaceGREEndpointResponse400
    | GetInterfaceGREEndpointResponse401
    | GetInterfaceGREEndpointResponse403
    | GetInterfaceGREEndpointResponse404
    | GetInterfaceGREEndpointResponse405
    | GetInterfaceGREEndpointResponse406
    | GetInterfaceGREEndpointResponse409
    | GetInterfaceGREEndpointResponse415
    | GetInterfaceGREEndpointResponse422
    | GetInterfaceGREEndpointResponse424
    | GetInterfaceGREEndpointResponse500
    | GetInterfaceGREEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing Interface GRE.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: InterfaceGRE<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-interface-gre-get ]<br>**Required packages**: [ None
    ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInterfaceGREEndpointResponse400 | GetInterfaceGREEndpointResponse401 | GetInterfaceGREEndpointResponse403 | GetInterfaceGREEndpointResponse404 | GetInterfaceGREEndpointResponse405 | GetInterfaceGREEndpointResponse406 | GetInterfaceGREEndpointResponse409 | GetInterfaceGREEndpointResponse415 | GetInterfaceGREEndpointResponse422 | GetInterfaceGREEndpointResponse424 | GetInterfaceGREEndpointResponse500 | GetInterfaceGREEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
