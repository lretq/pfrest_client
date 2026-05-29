from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_system_crl_endpoint_response_400 import DeleteSystemCRLEndpointResponse400
from ...models.delete_system_crl_endpoint_response_401 import DeleteSystemCRLEndpointResponse401
from ...models.delete_system_crl_endpoint_response_403 import DeleteSystemCRLEndpointResponse403
from ...models.delete_system_crl_endpoint_response_404 import DeleteSystemCRLEndpointResponse404
from ...models.delete_system_crl_endpoint_response_405 import DeleteSystemCRLEndpointResponse405
from ...models.delete_system_crl_endpoint_response_406 import DeleteSystemCRLEndpointResponse406
from ...models.delete_system_crl_endpoint_response_409 import DeleteSystemCRLEndpointResponse409
from ...models.delete_system_crl_endpoint_response_415 import DeleteSystemCRLEndpointResponse415
from ...models.delete_system_crl_endpoint_response_422 import DeleteSystemCRLEndpointResponse422
from ...models.delete_system_crl_endpoint_response_424 import DeleteSystemCRLEndpointResponse424
from ...models.delete_system_crl_endpoint_response_500 import DeleteSystemCRLEndpointResponse500
from ...models.delete_system_crl_endpoint_response_503 import DeleteSystemCRLEndpointResponse503
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
        "method": "delete",
        "url": "/api/v2/system/crl",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteSystemCRLEndpointResponse400
    | DeleteSystemCRLEndpointResponse401
    | DeleteSystemCRLEndpointResponse403
    | DeleteSystemCRLEndpointResponse404
    | DeleteSystemCRLEndpointResponse405
    | DeleteSystemCRLEndpointResponse406
    | DeleteSystemCRLEndpointResponse409
    | DeleteSystemCRLEndpointResponse415
    | DeleteSystemCRLEndpointResponse422
    | DeleteSystemCRLEndpointResponse424
    | DeleteSystemCRLEndpointResponse500
    | DeleteSystemCRLEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteSystemCRLEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteSystemCRLEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteSystemCRLEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteSystemCRLEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteSystemCRLEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteSystemCRLEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteSystemCRLEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteSystemCRLEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteSystemCRLEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteSystemCRLEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteSystemCRLEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteSystemCRLEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteSystemCRLEndpointResponse400
    | DeleteSystemCRLEndpointResponse401
    | DeleteSystemCRLEndpointResponse403
    | DeleteSystemCRLEndpointResponse404
    | DeleteSystemCRLEndpointResponse405
    | DeleteSystemCRLEndpointResponse406
    | DeleteSystemCRLEndpointResponse409
    | DeleteSystemCRLEndpointResponse415
    | DeleteSystemCRLEndpointResponse422
    | DeleteSystemCRLEndpointResponse424
    | DeleteSystemCRLEndpointResponse500
    | DeleteSystemCRLEndpointResponse503
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
    DeleteSystemCRLEndpointResponse400
    | DeleteSystemCRLEndpointResponse401
    | DeleteSystemCRLEndpointResponse403
    | DeleteSystemCRLEndpointResponse404
    | DeleteSystemCRLEndpointResponse405
    | DeleteSystemCRLEndpointResponse406
    | DeleteSystemCRLEndpointResponse409
    | DeleteSystemCRLEndpointResponse415
    | DeleteSystemCRLEndpointResponse422
    | DeleteSystemCRLEndpointResponse424
    | DeleteSystemCRLEndpointResponse500
    | DeleteSystemCRLEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSystemCRLEndpointResponse400 | DeleteSystemCRLEndpointResponse401 | DeleteSystemCRLEndpointResponse403 | DeleteSystemCRLEndpointResponse404 | DeleteSystemCRLEndpointResponse405 | DeleteSystemCRLEndpointResponse406 | DeleteSystemCRLEndpointResponse409 | DeleteSystemCRLEndpointResponse415 | DeleteSystemCRLEndpointResponse422 | DeleteSystemCRLEndpointResponse424 | DeleteSystemCRLEndpointResponse500 | DeleteSystemCRLEndpointResponse503]
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
    DeleteSystemCRLEndpointResponse400
    | DeleteSystemCRLEndpointResponse401
    | DeleteSystemCRLEndpointResponse403
    | DeleteSystemCRLEndpointResponse404
    | DeleteSystemCRLEndpointResponse405
    | DeleteSystemCRLEndpointResponse406
    | DeleteSystemCRLEndpointResponse409
    | DeleteSystemCRLEndpointResponse415
    | DeleteSystemCRLEndpointResponse422
    | DeleteSystemCRLEndpointResponse424
    | DeleteSystemCRLEndpointResponse500
    | DeleteSystemCRLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSystemCRLEndpointResponse400 | DeleteSystemCRLEndpointResponse401 | DeleteSystemCRLEndpointResponse403 | DeleteSystemCRLEndpointResponse404 | DeleteSystemCRLEndpointResponse405 | DeleteSystemCRLEndpointResponse406 | DeleteSystemCRLEndpointResponse409 | DeleteSystemCRLEndpointResponse415 | DeleteSystemCRLEndpointResponse422 | DeleteSystemCRLEndpointResponse424 | DeleteSystemCRLEndpointResponse500 | DeleteSystemCRLEndpointResponse503
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
    DeleteSystemCRLEndpointResponse400
    | DeleteSystemCRLEndpointResponse401
    | DeleteSystemCRLEndpointResponse403
    | DeleteSystemCRLEndpointResponse404
    | DeleteSystemCRLEndpointResponse405
    | DeleteSystemCRLEndpointResponse406
    | DeleteSystemCRLEndpointResponse409
    | DeleteSystemCRLEndpointResponse415
    | DeleteSystemCRLEndpointResponse422
    | DeleteSystemCRLEndpointResponse424
    | DeleteSystemCRLEndpointResponse500
    | DeleteSystemCRLEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSystemCRLEndpointResponse400 | DeleteSystemCRLEndpointResponse401 | DeleteSystemCRLEndpointResponse403 | DeleteSystemCRLEndpointResponse404 | DeleteSystemCRLEndpointResponse405 | DeleteSystemCRLEndpointResponse406 | DeleteSystemCRLEndpointResponse409 | DeleteSystemCRLEndpointResponse415 | DeleteSystemCRLEndpointResponse422 | DeleteSystemCRLEndpointResponse424 | DeleteSystemCRLEndpointResponse500 | DeleteSystemCRLEndpointResponse503]
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
    DeleteSystemCRLEndpointResponse400
    | DeleteSystemCRLEndpointResponse401
    | DeleteSystemCRLEndpointResponse403
    | DeleteSystemCRLEndpointResponse404
    | DeleteSystemCRLEndpointResponse405
    | DeleteSystemCRLEndpointResponse406
    | DeleteSystemCRLEndpointResponse409
    | DeleteSystemCRLEndpointResponse415
    | DeleteSystemCRLEndpointResponse422
    | DeleteSystemCRLEndpointResponse424
    | DeleteSystemCRLEndpointResponse500
    | DeleteSystemCRLEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing Certificate Revocation List.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: CertificateRevocationList<br>**Parent model**:
    None<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth,
    JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-system-crl-delete ]<br>**Required
    packages**: [ None ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSystemCRLEndpointResponse400 | DeleteSystemCRLEndpointResponse401 | DeleteSystemCRLEndpointResponse403 | DeleteSystemCRLEndpointResponse404 | DeleteSystemCRLEndpointResponse405 | DeleteSystemCRLEndpointResponse406 | DeleteSystemCRLEndpointResponse409 | DeleteSystemCRLEndpointResponse415 | DeleteSystemCRLEndpointResponse422 | DeleteSystemCRLEndpointResponse424 | DeleteSystemCRLEndpointResponse500 | DeleteSystemCRLEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
