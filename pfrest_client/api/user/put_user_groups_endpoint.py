from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_user_groups_endpoint_data_body_item import PutUserGroupsEndpointDataBodyItem
from ...models.put_user_groups_endpoint_json_body_item import PutUserGroupsEndpointJsonBodyItem
from ...models.put_user_groups_endpoint_response_400 import PutUserGroupsEndpointResponse400
from ...models.put_user_groups_endpoint_response_401 import PutUserGroupsEndpointResponse401
from ...models.put_user_groups_endpoint_response_403 import PutUserGroupsEndpointResponse403
from ...models.put_user_groups_endpoint_response_404 import PutUserGroupsEndpointResponse404
from ...models.put_user_groups_endpoint_response_405 import PutUserGroupsEndpointResponse405
from ...models.put_user_groups_endpoint_response_406 import PutUserGroupsEndpointResponse406
from ...models.put_user_groups_endpoint_response_409 import PutUserGroupsEndpointResponse409
from ...models.put_user_groups_endpoint_response_415 import PutUserGroupsEndpointResponse415
from ...models.put_user_groups_endpoint_response_422 import PutUserGroupsEndpointResponse422
from ...models.put_user_groups_endpoint_response_424 import PutUserGroupsEndpointResponse424
from ...models.put_user_groups_endpoint_response_500 import PutUserGroupsEndpointResponse500
from ...models.put_user_groups_endpoint_response_503 import PutUserGroupsEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutUserGroupsEndpointJsonBodyItem] | list[PutUserGroupsEndpointDataBodyItem] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/user/groups",
    }

    if isinstance(body, list[PutUserGroupsEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutUserGroupsEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutUserGroupsEndpointResponse400
    | PutUserGroupsEndpointResponse401
    | PutUserGroupsEndpointResponse403
    | PutUserGroupsEndpointResponse404
    | PutUserGroupsEndpointResponse405
    | PutUserGroupsEndpointResponse406
    | PutUserGroupsEndpointResponse409
    | PutUserGroupsEndpointResponse415
    | PutUserGroupsEndpointResponse422
    | PutUserGroupsEndpointResponse424
    | PutUserGroupsEndpointResponse500
    | PutUserGroupsEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutUserGroupsEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutUserGroupsEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutUserGroupsEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutUserGroupsEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutUserGroupsEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutUserGroupsEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutUserGroupsEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutUserGroupsEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutUserGroupsEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutUserGroupsEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutUserGroupsEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutUserGroupsEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutUserGroupsEndpointResponse400
    | PutUserGroupsEndpointResponse401
    | PutUserGroupsEndpointResponse403
    | PutUserGroupsEndpointResponse404
    | PutUserGroupsEndpointResponse405
    | PutUserGroupsEndpointResponse406
    | PutUserGroupsEndpointResponse409
    | PutUserGroupsEndpointResponse415
    | PutUserGroupsEndpointResponse422
    | PutUserGroupsEndpointResponse424
    | PutUserGroupsEndpointResponse500
    | PutUserGroupsEndpointResponse503
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
    body: list[PutUserGroupsEndpointJsonBodyItem] | list[PutUserGroupsEndpointDataBodyItem] | Unset = UNSET,
) -> Response[
    PutUserGroupsEndpointResponse400
    | PutUserGroupsEndpointResponse401
    | PutUserGroupsEndpointResponse403
    | PutUserGroupsEndpointResponse404
    | PutUserGroupsEndpointResponse405
    | PutUserGroupsEndpointResponse406
    | PutUserGroupsEndpointResponse409
    | PutUserGroupsEndpointResponse415
    | PutUserGroupsEndpointResponse422
    | PutUserGroupsEndpointResponse424
    | PutUserGroupsEndpointResponse500
    | PutUserGroupsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing User Groups.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-groups-put ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutUserGroupsEndpointJsonBodyItem] | Unset):
        body (list[PutUserGroupsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutUserGroupsEndpointResponse400 | PutUserGroupsEndpointResponse401 | PutUserGroupsEndpointResponse403 | PutUserGroupsEndpointResponse404 | PutUserGroupsEndpointResponse405 | PutUserGroupsEndpointResponse406 | PutUserGroupsEndpointResponse409 | PutUserGroupsEndpointResponse415 | PutUserGroupsEndpointResponse422 | PutUserGroupsEndpointResponse424 | PutUserGroupsEndpointResponse500 | PutUserGroupsEndpointResponse503]
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
    body: list[PutUserGroupsEndpointJsonBodyItem] | list[PutUserGroupsEndpointDataBodyItem] | Unset = UNSET,
) -> (
    PutUserGroupsEndpointResponse400
    | PutUserGroupsEndpointResponse401
    | PutUserGroupsEndpointResponse403
    | PutUserGroupsEndpointResponse404
    | PutUserGroupsEndpointResponse405
    | PutUserGroupsEndpointResponse406
    | PutUserGroupsEndpointResponse409
    | PutUserGroupsEndpointResponse415
    | PutUserGroupsEndpointResponse422
    | PutUserGroupsEndpointResponse424
    | PutUserGroupsEndpointResponse500
    | PutUserGroupsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing User Groups.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-groups-put ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutUserGroupsEndpointJsonBodyItem] | Unset):
        body (list[PutUserGroupsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutUserGroupsEndpointResponse400 | PutUserGroupsEndpointResponse401 | PutUserGroupsEndpointResponse403 | PutUserGroupsEndpointResponse404 | PutUserGroupsEndpointResponse405 | PutUserGroupsEndpointResponse406 | PutUserGroupsEndpointResponse409 | PutUserGroupsEndpointResponse415 | PutUserGroupsEndpointResponse422 | PutUserGroupsEndpointResponse424 | PutUserGroupsEndpointResponse500 | PutUserGroupsEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutUserGroupsEndpointJsonBodyItem] | list[PutUserGroupsEndpointDataBodyItem] | Unset = UNSET,
) -> Response[
    PutUserGroupsEndpointResponse400
    | PutUserGroupsEndpointResponse401
    | PutUserGroupsEndpointResponse403
    | PutUserGroupsEndpointResponse404
    | PutUserGroupsEndpointResponse405
    | PutUserGroupsEndpointResponse406
    | PutUserGroupsEndpointResponse409
    | PutUserGroupsEndpointResponse415
    | PutUserGroupsEndpointResponse422
    | PutUserGroupsEndpointResponse424
    | PutUserGroupsEndpointResponse500
    | PutUserGroupsEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing User Groups.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-groups-put ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutUserGroupsEndpointJsonBodyItem] | Unset):
        body (list[PutUserGroupsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutUserGroupsEndpointResponse400 | PutUserGroupsEndpointResponse401 | PutUserGroupsEndpointResponse403 | PutUserGroupsEndpointResponse404 | PutUserGroupsEndpointResponse405 | PutUserGroupsEndpointResponse406 | PutUserGroupsEndpointResponse409 | PutUserGroupsEndpointResponse415 | PutUserGroupsEndpointResponse422 | PutUserGroupsEndpointResponse424 | PutUserGroupsEndpointResponse500 | PutUserGroupsEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutUserGroupsEndpointJsonBodyItem] | list[PutUserGroupsEndpointDataBodyItem] | Unset = UNSET,
) -> (
    PutUserGroupsEndpointResponse400
    | PutUserGroupsEndpointResponse401
    | PutUserGroupsEndpointResponse403
    | PutUserGroupsEndpointResponse404
    | PutUserGroupsEndpointResponse405
    | PutUserGroupsEndpointResponse406
    | PutUserGroupsEndpointResponse409
    | PutUserGroupsEndpointResponse415
    | PutUserGroupsEndpointResponse422
    | PutUserGroupsEndpointResponse424
    | PutUserGroupsEndpointResponse500
    | PutUserGroupsEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing User Groups.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: UserGroup<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-groups-put ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutUserGroupsEndpointJsonBodyItem] | Unset):
        body (list[PutUserGroupsEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutUserGroupsEndpointResponse400 | PutUserGroupsEndpointResponse401 | PutUserGroupsEndpointResponse403 | PutUserGroupsEndpointResponse404 | PutUserGroupsEndpointResponse405 | PutUserGroupsEndpointResponse406 | PutUserGroupsEndpointResponse409 | PutUserGroupsEndpointResponse415 | PutUserGroupsEndpointResponse422 | PutUserGroupsEndpointResponse424 | PutUserGroupsEndpointResponse500 | PutUserGroupsEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
