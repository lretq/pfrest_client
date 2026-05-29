from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_user_auth_servers_endpoint_data_body_item import PutUserAuthServersEndpointDataBodyItem
from ...models.put_user_auth_servers_endpoint_json_body_item import PutUserAuthServersEndpointJsonBodyItem
from ...models.put_user_auth_servers_endpoint_response_400 import PutUserAuthServersEndpointResponse400
from ...models.put_user_auth_servers_endpoint_response_401 import PutUserAuthServersEndpointResponse401
from ...models.put_user_auth_servers_endpoint_response_403 import PutUserAuthServersEndpointResponse403
from ...models.put_user_auth_servers_endpoint_response_404 import PutUserAuthServersEndpointResponse404
from ...models.put_user_auth_servers_endpoint_response_405 import PutUserAuthServersEndpointResponse405
from ...models.put_user_auth_servers_endpoint_response_406 import PutUserAuthServersEndpointResponse406
from ...models.put_user_auth_servers_endpoint_response_409 import PutUserAuthServersEndpointResponse409
from ...models.put_user_auth_servers_endpoint_response_415 import PutUserAuthServersEndpointResponse415
from ...models.put_user_auth_servers_endpoint_response_422 import PutUserAuthServersEndpointResponse422
from ...models.put_user_auth_servers_endpoint_response_424 import PutUserAuthServersEndpointResponse424
from ...models.put_user_auth_servers_endpoint_response_500 import PutUserAuthServersEndpointResponse500
from ...models.put_user_auth_servers_endpoint_response_503 import PutUserAuthServersEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutUserAuthServersEndpointJsonBodyItem] | list[PutUserAuthServersEndpointDataBodyItem] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/user/auth_servers",
    }

    if isinstance(body, list[PutUserAuthServersEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutUserAuthServersEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutUserAuthServersEndpointResponse400
    | PutUserAuthServersEndpointResponse401
    | PutUserAuthServersEndpointResponse403
    | PutUserAuthServersEndpointResponse404
    | PutUserAuthServersEndpointResponse405
    | PutUserAuthServersEndpointResponse406
    | PutUserAuthServersEndpointResponse409
    | PutUserAuthServersEndpointResponse415
    | PutUserAuthServersEndpointResponse422
    | PutUserAuthServersEndpointResponse424
    | PutUserAuthServersEndpointResponse500
    | PutUserAuthServersEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutUserAuthServersEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutUserAuthServersEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutUserAuthServersEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutUserAuthServersEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutUserAuthServersEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutUserAuthServersEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutUserAuthServersEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutUserAuthServersEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutUserAuthServersEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutUserAuthServersEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutUserAuthServersEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutUserAuthServersEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutUserAuthServersEndpointResponse400
    | PutUserAuthServersEndpointResponse401
    | PutUserAuthServersEndpointResponse403
    | PutUserAuthServersEndpointResponse404
    | PutUserAuthServersEndpointResponse405
    | PutUserAuthServersEndpointResponse406
    | PutUserAuthServersEndpointResponse409
    | PutUserAuthServersEndpointResponse415
    | PutUserAuthServersEndpointResponse422
    | PutUserAuthServersEndpointResponse424
    | PutUserAuthServersEndpointResponse500
    | PutUserAuthServersEndpointResponse503
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
    body: list[PutUserAuthServersEndpointJsonBodyItem] | list[PutUserAuthServersEndpointDataBodyItem] | Unset = UNSET,
) -> Response[
    PutUserAuthServersEndpointResponse400
    | PutUserAuthServersEndpointResponse401
    | PutUserAuthServersEndpointResponse403
    | PutUserAuthServersEndpointResponse404
    | PutUserAuthServersEndpointResponse405
    | PutUserAuthServersEndpointResponse406
    | PutUserAuthServersEndpointResponse409
    | PutUserAuthServersEndpointResponse415
    | PutUserAuthServersEndpointResponse422
    | PutUserAuthServersEndpointResponse424
    | PutUserAuthServersEndpointResponse500
    | PutUserAuthServersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing authentication servers.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-servers-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutUserAuthServersEndpointJsonBodyItem] | Unset):
        body (list[PutUserAuthServersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutUserAuthServersEndpointResponse400 | PutUserAuthServersEndpointResponse401 | PutUserAuthServersEndpointResponse403 | PutUserAuthServersEndpointResponse404 | PutUserAuthServersEndpointResponse405 | PutUserAuthServersEndpointResponse406 | PutUserAuthServersEndpointResponse409 | PutUserAuthServersEndpointResponse415 | PutUserAuthServersEndpointResponse422 | PutUserAuthServersEndpointResponse424 | PutUserAuthServersEndpointResponse500 | PutUserAuthServersEndpointResponse503]
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
    body: list[PutUserAuthServersEndpointJsonBodyItem] | list[PutUserAuthServersEndpointDataBodyItem] | Unset = UNSET,
) -> (
    PutUserAuthServersEndpointResponse400
    | PutUserAuthServersEndpointResponse401
    | PutUserAuthServersEndpointResponse403
    | PutUserAuthServersEndpointResponse404
    | PutUserAuthServersEndpointResponse405
    | PutUserAuthServersEndpointResponse406
    | PutUserAuthServersEndpointResponse409
    | PutUserAuthServersEndpointResponse415
    | PutUserAuthServersEndpointResponse422
    | PutUserAuthServersEndpointResponse424
    | PutUserAuthServersEndpointResponse500
    | PutUserAuthServersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing authentication servers.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-servers-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutUserAuthServersEndpointJsonBodyItem] | Unset):
        body (list[PutUserAuthServersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutUserAuthServersEndpointResponse400 | PutUserAuthServersEndpointResponse401 | PutUserAuthServersEndpointResponse403 | PutUserAuthServersEndpointResponse404 | PutUserAuthServersEndpointResponse405 | PutUserAuthServersEndpointResponse406 | PutUserAuthServersEndpointResponse409 | PutUserAuthServersEndpointResponse415 | PutUserAuthServersEndpointResponse422 | PutUserAuthServersEndpointResponse424 | PutUserAuthServersEndpointResponse500 | PutUserAuthServersEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutUserAuthServersEndpointJsonBodyItem] | list[PutUserAuthServersEndpointDataBodyItem] | Unset = UNSET,
) -> Response[
    PutUserAuthServersEndpointResponse400
    | PutUserAuthServersEndpointResponse401
    | PutUserAuthServersEndpointResponse403
    | PutUserAuthServersEndpointResponse404
    | PutUserAuthServersEndpointResponse405
    | PutUserAuthServersEndpointResponse406
    | PutUserAuthServersEndpointResponse409
    | PutUserAuthServersEndpointResponse415
    | PutUserAuthServersEndpointResponse422
    | PutUserAuthServersEndpointResponse424
    | PutUserAuthServersEndpointResponse500
    | PutUserAuthServersEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing authentication servers.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-servers-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutUserAuthServersEndpointJsonBodyItem] | Unset):
        body (list[PutUserAuthServersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutUserAuthServersEndpointResponse400 | PutUserAuthServersEndpointResponse401 | PutUserAuthServersEndpointResponse403 | PutUserAuthServersEndpointResponse404 | PutUserAuthServersEndpointResponse405 | PutUserAuthServersEndpointResponse406 | PutUserAuthServersEndpointResponse409 | PutUserAuthServersEndpointResponse415 | PutUserAuthServersEndpointResponse422 | PutUserAuthServersEndpointResponse424 | PutUserAuthServersEndpointResponse500 | PutUserAuthServersEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutUserAuthServersEndpointJsonBodyItem] | list[PutUserAuthServersEndpointDataBodyItem] | Unset = UNSET,
) -> (
    PutUserAuthServersEndpointResponse400
    | PutUserAuthServersEndpointResponse401
    | PutUserAuthServersEndpointResponse403
    | PutUserAuthServersEndpointResponse404
    | PutUserAuthServersEndpointResponse405
    | PutUserAuthServersEndpointResponse406
    | PutUserAuthServersEndpointResponse409
    | PutUserAuthServersEndpointResponse415
    | PutUserAuthServersEndpointResponse422
    | PutUserAuthServersEndpointResponse424
    | PutUserAuthServersEndpointResponse500
    | PutUserAuthServersEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing authentication servers.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: AuthServer<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-user-auth-servers-put ]<br>**Required packages**: [
    None ]<br>**Applies immediately**: No<br>**Utilizes cache**: None

    Args:
        body (list[PutUserAuthServersEndpointJsonBodyItem] | Unset):
        body (list[PutUserAuthServersEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutUserAuthServersEndpointResponse400 | PutUserAuthServersEndpointResponse401 | PutUserAuthServersEndpointResponse403 | PutUserAuthServersEndpointResponse404 | PutUserAuthServersEndpointResponse405 | PutUserAuthServersEndpointResponse406 | PutUserAuthServersEndpointResponse409 | PutUserAuthServersEndpointResponse415 | PutUserAuthServersEndpointResponse422 | PutUserAuthServersEndpointResponse424 | PutUserAuthServersEndpointResponse500 | PutUserAuthServersEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
