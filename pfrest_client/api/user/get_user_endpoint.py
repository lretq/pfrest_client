from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_endpoint_response_400 import GetUserEndpointResponse400
from ...models.get_user_endpoint_response_401 import GetUserEndpointResponse401
from ...models.get_user_endpoint_response_403 import GetUserEndpointResponse403
from ...models.get_user_endpoint_response_404 import GetUserEndpointResponse404
from ...models.get_user_endpoint_response_405 import GetUserEndpointResponse405
from ...models.get_user_endpoint_response_406 import GetUserEndpointResponse406
from ...models.get_user_endpoint_response_409 import GetUserEndpointResponse409
from ...models.get_user_endpoint_response_415 import GetUserEndpointResponse415
from ...models.get_user_endpoint_response_422 import GetUserEndpointResponse422
from ...models.get_user_endpoint_response_424 import GetUserEndpointResponse424
from ...models.get_user_endpoint_response_500 import GetUserEndpointResponse500
from ...models.get_user_endpoint_response_503 import GetUserEndpointResponse503
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
        "url": "/api/v2/user",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetUserEndpointResponse400
    | GetUserEndpointResponse401
    | GetUserEndpointResponse403
    | GetUserEndpointResponse404
    | GetUserEndpointResponse405
    | GetUserEndpointResponse406
    | GetUserEndpointResponse409
    | GetUserEndpointResponse415
    | GetUserEndpointResponse422
    | GetUserEndpointResponse424
    | GetUserEndpointResponse500
    | GetUserEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetUserEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetUserEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetUserEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUserEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetUserEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetUserEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetUserEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetUserEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetUserEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetUserEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetUserEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetUserEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetUserEndpointResponse400
    | GetUserEndpointResponse401
    | GetUserEndpointResponse403
    | GetUserEndpointResponse404
    | GetUserEndpointResponse405
    | GetUserEndpointResponse406
    | GetUserEndpointResponse409
    | GetUserEndpointResponse415
    | GetUserEndpointResponse422
    | GetUserEndpointResponse424
    | GetUserEndpointResponse500
    | GetUserEndpointResponse503
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
    GetUserEndpointResponse400
    | GetUserEndpointResponse401
    | GetUserEndpointResponse403
    | GetUserEndpointResponse404
    | GetUserEndpointResponse405
    | GetUserEndpointResponse406
    | GetUserEndpointResponse409
    | GetUserEndpointResponse415
    | GetUserEndpointResponse422
    | GetUserEndpointResponse424
    | GetUserEndpointResponse500
    | GetUserEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserEndpointResponse400 | GetUserEndpointResponse401 | GetUserEndpointResponse403 | GetUserEndpointResponse404 | GetUserEndpointResponse405 | GetUserEndpointResponse406 | GetUserEndpointResponse409 | GetUserEndpointResponse415 | GetUserEndpointResponse422 | GetUserEndpointResponse424 | GetUserEndpointResponse500 | GetUserEndpointResponse503]
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
    GetUserEndpointResponse400
    | GetUserEndpointResponse401
    | GetUserEndpointResponse403
    | GetUserEndpointResponse404
    | GetUserEndpointResponse405
    | GetUserEndpointResponse406
    | GetUserEndpointResponse409
    | GetUserEndpointResponse415
    | GetUserEndpointResponse422
    | GetUserEndpointResponse424
    | GetUserEndpointResponse500
    | GetUserEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserEndpointResponse400 | GetUserEndpointResponse401 | GetUserEndpointResponse403 | GetUserEndpointResponse404 | GetUserEndpointResponse405 | GetUserEndpointResponse406 | GetUserEndpointResponse409 | GetUserEndpointResponse415 | GetUserEndpointResponse422 | GetUserEndpointResponse424 | GetUserEndpointResponse500 | GetUserEndpointResponse503
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
    GetUserEndpointResponse400
    | GetUserEndpointResponse401
    | GetUserEndpointResponse403
    | GetUserEndpointResponse404
    | GetUserEndpointResponse405
    | GetUserEndpointResponse406
    | GetUserEndpointResponse409
    | GetUserEndpointResponse415
    | GetUserEndpointResponse422
    | GetUserEndpointResponse424
    | GetUserEndpointResponse500
    | GetUserEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserEndpointResponse400 | GetUserEndpointResponse401 | GetUserEndpointResponse403 | GetUserEndpointResponse404 | GetUserEndpointResponse405 | GetUserEndpointResponse406 | GetUserEndpointResponse409 | GetUserEndpointResponse415 | GetUserEndpointResponse422 | GetUserEndpointResponse424 | GetUserEndpointResponse500 | GetUserEndpointResponse503]
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
    GetUserEndpointResponse400
    | GetUserEndpointResponse401
    | GetUserEndpointResponse403
    | GetUserEndpointResponse404
    | GetUserEndpointResponse405
    | GetUserEndpointResponse406
    | GetUserEndpointResponse409
    | GetUserEndpointResponse415
    | GetUserEndpointResponse422
    | GetUserEndpointResponse424
    | GetUserEndpointResponse500
    | GetUserEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-get ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserEndpointResponse400 | GetUserEndpointResponse401 | GetUserEndpointResponse403 | GetUserEndpointResponse404 | GetUserEndpointResponse405 | GetUserEndpointResponse406 | GetUserEndpointResponse409 | GetUserEndpointResponse415 | GetUserEndpointResponse422 | GetUserEndpointResponse424 | GetUserEndpointResponse500 | GetUserEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
