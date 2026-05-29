from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_user_endpoint_data_body import PatchUserEndpointDataBody
from ...models.patch_user_endpoint_json_body import PatchUserEndpointJsonBody
from ...models.patch_user_endpoint_response_400 import PatchUserEndpointResponse400
from ...models.patch_user_endpoint_response_401 import PatchUserEndpointResponse401
from ...models.patch_user_endpoint_response_403 import PatchUserEndpointResponse403
from ...models.patch_user_endpoint_response_404 import PatchUserEndpointResponse404
from ...models.patch_user_endpoint_response_405 import PatchUserEndpointResponse405
from ...models.patch_user_endpoint_response_406 import PatchUserEndpointResponse406
from ...models.patch_user_endpoint_response_409 import PatchUserEndpointResponse409
from ...models.patch_user_endpoint_response_415 import PatchUserEndpointResponse415
from ...models.patch_user_endpoint_response_422 import PatchUserEndpointResponse422
from ...models.patch_user_endpoint_response_424 import PatchUserEndpointResponse424
from ...models.patch_user_endpoint_response_500 import PatchUserEndpointResponse500
from ...models.patch_user_endpoint_response_503 import PatchUserEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchUserEndpointJsonBody | PatchUserEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/user",
    }

    if isinstance(body, PatchUserEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchUserEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchUserEndpointResponse400
    | PatchUserEndpointResponse401
    | PatchUserEndpointResponse403
    | PatchUserEndpointResponse404
    | PatchUserEndpointResponse405
    | PatchUserEndpointResponse406
    | PatchUserEndpointResponse409
    | PatchUserEndpointResponse415
    | PatchUserEndpointResponse422
    | PatchUserEndpointResponse424
    | PatchUserEndpointResponse500
    | PatchUserEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchUserEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchUserEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchUserEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchUserEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchUserEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchUserEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchUserEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchUserEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchUserEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchUserEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchUserEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchUserEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchUserEndpointResponse400
    | PatchUserEndpointResponse401
    | PatchUserEndpointResponse403
    | PatchUserEndpointResponse404
    | PatchUserEndpointResponse405
    | PatchUserEndpointResponse406
    | PatchUserEndpointResponse409
    | PatchUserEndpointResponse415
    | PatchUserEndpointResponse422
    | PatchUserEndpointResponse424
    | PatchUserEndpointResponse500
    | PatchUserEndpointResponse503
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
    body: PatchUserEndpointJsonBody | PatchUserEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchUserEndpointResponse400
    | PatchUserEndpointResponse401
    | PatchUserEndpointResponse403
    | PatchUserEndpointResponse404
    | PatchUserEndpointResponse405
    | PatchUserEndpointResponse406
    | PatchUserEndpointResponse409
    | PatchUserEndpointResponse415
    | PatchUserEndpointResponse422
    | PatchUserEndpointResponse424
    | PatchUserEndpointResponse500
    | PatchUserEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-patch ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchUserEndpointJsonBody | Unset):
        body (PatchUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUserEndpointResponse400 | PatchUserEndpointResponse401 | PatchUserEndpointResponse403 | PatchUserEndpointResponse404 | PatchUserEndpointResponse405 | PatchUserEndpointResponse406 | PatchUserEndpointResponse409 | PatchUserEndpointResponse415 | PatchUserEndpointResponse422 | PatchUserEndpointResponse424 | PatchUserEndpointResponse500 | PatchUserEndpointResponse503]
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
    body: PatchUserEndpointJsonBody | PatchUserEndpointDataBody | Unset = UNSET,
) -> (
    PatchUserEndpointResponse400
    | PatchUserEndpointResponse401
    | PatchUserEndpointResponse403
    | PatchUserEndpointResponse404
    | PatchUserEndpointResponse405
    | PatchUserEndpointResponse406
    | PatchUserEndpointResponse409
    | PatchUserEndpointResponse415
    | PatchUserEndpointResponse422
    | PatchUserEndpointResponse424
    | PatchUserEndpointResponse500
    | PatchUserEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-patch ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchUserEndpointJsonBody | Unset):
        body (PatchUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUserEndpointResponse400 | PatchUserEndpointResponse401 | PatchUserEndpointResponse403 | PatchUserEndpointResponse404 | PatchUserEndpointResponse405 | PatchUserEndpointResponse406 | PatchUserEndpointResponse409 | PatchUserEndpointResponse415 | PatchUserEndpointResponse422 | PatchUserEndpointResponse424 | PatchUserEndpointResponse500 | PatchUserEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchUserEndpointJsonBody | PatchUserEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchUserEndpointResponse400
    | PatchUserEndpointResponse401
    | PatchUserEndpointResponse403
    | PatchUserEndpointResponse404
    | PatchUserEndpointResponse405
    | PatchUserEndpointResponse406
    | PatchUserEndpointResponse409
    | PatchUserEndpointResponse415
    | PatchUserEndpointResponse422
    | PatchUserEndpointResponse424
    | PatchUserEndpointResponse500
    | PatchUserEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-patch ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchUserEndpointJsonBody | Unset):
        body (PatchUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUserEndpointResponse400 | PatchUserEndpointResponse401 | PatchUserEndpointResponse403 | PatchUserEndpointResponse404 | PatchUserEndpointResponse405 | PatchUserEndpointResponse406 | PatchUserEndpointResponse409 | PatchUserEndpointResponse415 | PatchUserEndpointResponse422 | PatchUserEndpointResponse424 | PatchUserEndpointResponse500 | PatchUserEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchUserEndpointJsonBody | PatchUserEndpointDataBody | Unset = UNSET,
) -> (
    PatchUserEndpointResponse400
    | PatchUserEndpointResponse401
    | PatchUserEndpointResponse403
    | PatchUserEndpointResponse404
    | PatchUserEndpointResponse405
    | PatchUserEndpointResponse406
    | PatchUserEndpointResponse409
    | PatchUserEndpointResponse415
    | PatchUserEndpointResponse422
    | PatchUserEndpointResponse424
    | PatchUserEndpointResponse500
    | PatchUserEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing User.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: User<br>**Parent model**: None<br>**Requires authentication**:
    Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed
    privileges**: [ page-all, api-v2-user-patch ]<br>**Required packages**: [ None ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchUserEndpointJsonBody | Unset):
        body (PatchUserEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUserEndpointResponse400 | PatchUserEndpointResponse401 | PatchUserEndpointResponse403 | PatchUserEndpointResponse404 | PatchUserEndpointResponse405 | PatchUserEndpointResponse406 | PatchUserEndpointResponse409 | PatchUserEndpointResponse415 | PatchUserEndpointResponse422 | PatchUserEndpointResponse424 | PatchUserEndpointResponse500 | PatchUserEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
