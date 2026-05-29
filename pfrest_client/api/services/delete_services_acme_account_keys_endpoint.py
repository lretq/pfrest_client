from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_acme_account_keys_endpoint_query import DeleteServicesACMEAccountKeysEndpointQuery
from ...models.delete_services_acme_account_keys_endpoint_response_400 import (
    DeleteServicesACMEAccountKeysEndpointResponse400,
)
from ...models.delete_services_acme_account_keys_endpoint_response_401 import (
    DeleteServicesACMEAccountKeysEndpointResponse401,
)
from ...models.delete_services_acme_account_keys_endpoint_response_403 import (
    DeleteServicesACMEAccountKeysEndpointResponse403,
)
from ...models.delete_services_acme_account_keys_endpoint_response_404 import (
    DeleteServicesACMEAccountKeysEndpointResponse404,
)
from ...models.delete_services_acme_account_keys_endpoint_response_405 import (
    DeleteServicesACMEAccountKeysEndpointResponse405,
)
from ...models.delete_services_acme_account_keys_endpoint_response_406 import (
    DeleteServicesACMEAccountKeysEndpointResponse406,
)
from ...models.delete_services_acme_account_keys_endpoint_response_409 import (
    DeleteServicesACMEAccountKeysEndpointResponse409,
)
from ...models.delete_services_acme_account_keys_endpoint_response_415 import (
    DeleteServicesACMEAccountKeysEndpointResponse415,
)
from ...models.delete_services_acme_account_keys_endpoint_response_422 import (
    DeleteServicesACMEAccountKeysEndpointResponse422,
)
from ...models.delete_services_acme_account_keys_endpoint_response_424 import (
    DeleteServicesACMEAccountKeysEndpointResponse424,
)
from ...models.delete_services_acme_account_keys_endpoint_response_500 import (
    DeleteServicesACMEAccountKeysEndpointResponse500,
)
from ...models.delete_services_acme_account_keys_endpoint_response_503 import (
    DeleteServicesACMEAccountKeysEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesACMEAccountKeysEndpointQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_query: dict[str, Any] | Unset = UNSET
    if not isinstance(query, Unset):
        json_query = query.to_dict()
    if not isinstance(json_query, Unset):
        params.update(json_query)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/services/acme/account_keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesACMEAccountKeysEndpointResponse400
    | DeleteServicesACMEAccountKeysEndpointResponse401
    | DeleteServicesACMEAccountKeysEndpointResponse403
    | DeleteServicesACMEAccountKeysEndpointResponse404
    | DeleteServicesACMEAccountKeysEndpointResponse405
    | DeleteServicesACMEAccountKeysEndpointResponse406
    | DeleteServicesACMEAccountKeysEndpointResponse409
    | DeleteServicesACMEAccountKeysEndpointResponse415
    | DeleteServicesACMEAccountKeysEndpointResponse422
    | DeleteServicesACMEAccountKeysEndpointResponse424
    | DeleteServicesACMEAccountKeysEndpointResponse500
    | DeleteServicesACMEAccountKeysEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesACMEAccountKeysEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesACMEAccountKeysEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesACMEAccountKeysEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesACMEAccountKeysEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesACMEAccountKeysEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesACMEAccountKeysEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesACMEAccountKeysEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesACMEAccountKeysEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesACMEAccountKeysEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesACMEAccountKeysEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesACMEAccountKeysEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesACMEAccountKeysEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesACMEAccountKeysEndpointResponse400
    | DeleteServicesACMEAccountKeysEndpointResponse401
    | DeleteServicesACMEAccountKeysEndpointResponse403
    | DeleteServicesACMEAccountKeysEndpointResponse404
    | DeleteServicesACMEAccountKeysEndpointResponse405
    | DeleteServicesACMEAccountKeysEndpointResponse406
    | DeleteServicesACMEAccountKeysEndpointResponse409
    | DeleteServicesACMEAccountKeysEndpointResponse415
    | DeleteServicesACMEAccountKeysEndpointResponse422
    | DeleteServicesACMEAccountKeysEndpointResponse424
    | DeleteServicesACMEAccountKeysEndpointResponse500
    | DeleteServicesACMEAccountKeysEndpointResponse503
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
    query: DeleteServicesACMEAccountKeysEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteServicesACMEAccountKeysEndpointResponse400
    | DeleteServicesACMEAccountKeysEndpointResponse401
    | DeleteServicesACMEAccountKeysEndpointResponse403
    | DeleteServicesACMEAccountKeysEndpointResponse404
    | DeleteServicesACMEAccountKeysEndpointResponse405
    | DeleteServicesACMEAccountKeysEndpointResponse406
    | DeleteServicesACMEAccountKeysEndpointResponse409
    | DeleteServicesACMEAccountKeysEndpointResponse415
    | DeleteServicesACMEAccountKeysEndpointResponse422
    | DeleteServicesACMEAccountKeysEndpointResponse424
    | DeleteServicesACMEAccountKeysEndpointResponse500
    | DeleteServicesACMEAccountKeysEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing ACME Account Keys using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-keys-delete ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesACMEAccountKeysEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesACMEAccountKeysEndpointResponse400 | DeleteServicesACMEAccountKeysEndpointResponse401 | DeleteServicesACMEAccountKeysEndpointResponse403 | DeleteServicesACMEAccountKeysEndpointResponse404 | DeleteServicesACMEAccountKeysEndpointResponse405 | DeleteServicesACMEAccountKeysEndpointResponse406 | DeleteServicesACMEAccountKeysEndpointResponse409 | DeleteServicesACMEAccountKeysEndpointResponse415 | DeleteServicesACMEAccountKeysEndpointResponse422 | DeleteServicesACMEAccountKeysEndpointResponse424 | DeleteServicesACMEAccountKeysEndpointResponse500 | DeleteServicesACMEAccountKeysEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
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
    query: DeleteServicesACMEAccountKeysEndpointQuery | Unset = UNSET,
) -> (
    DeleteServicesACMEAccountKeysEndpointResponse400
    | DeleteServicesACMEAccountKeysEndpointResponse401
    | DeleteServicesACMEAccountKeysEndpointResponse403
    | DeleteServicesACMEAccountKeysEndpointResponse404
    | DeleteServicesACMEAccountKeysEndpointResponse405
    | DeleteServicesACMEAccountKeysEndpointResponse406
    | DeleteServicesACMEAccountKeysEndpointResponse409
    | DeleteServicesACMEAccountKeysEndpointResponse415
    | DeleteServicesACMEAccountKeysEndpointResponse422
    | DeleteServicesACMEAccountKeysEndpointResponse424
    | DeleteServicesACMEAccountKeysEndpointResponse500
    | DeleteServicesACMEAccountKeysEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing ACME Account Keys using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-keys-delete ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesACMEAccountKeysEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesACMEAccountKeysEndpointResponse400 | DeleteServicesACMEAccountKeysEndpointResponse401 | DeleteServicesACMEAccountKeysEndpointResponse403 | DeleteServicesACMEAccountKeysEndpointResponse404 | DeleteServicesACMEAccountKeysEndpointResponse405 | DeleteServicesACMEAccountKeysEndpointResponse406 | DeleteServicesACMEAccountKeysEndpointResponse409 | DeleteServicesACMEAccountKeysEndpointResponse415 | DeleteServicesACMEAccountKeysEndpointResponse422 | DeleteServicesACMEAccountKeysEndpointResponse424 | DeleteServicesACMEAccountKeysEndpointResponse500 | DeleteServicesACMEAccountKeysEndpointResponse503
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesACMEAccountKeysEndpointQuery | Unset = UNSET,
) -> Response[
    DeleteServicesACMEAccountKeysEndpointResponse400
    | DeleteServicesACMEAccountKeysEndpointResponse401
    | DeleteServicesACMEAccountKeysEndpointResponse403
    | DeleteServicesACMEAccountKeysEndpointResponse404
    | DeleteServicesACMEAccountKeysEndpointResponse405
    | DeleteServicesACMEAccountKeysEndpointResponse406
    | DeleteServicesACMEAccountKeysEndpointResponse409
    | DeleteServicesACMEAccountKeysEndpointResponse415
    | DeleteServicesACMEAccountKeysEndpointResponse422
    | DeleteServicesACMEAccountKeysEndpointResponse424
    | DeleteServicesACMEAccountKeysEndpointResponse500
    | DeleteServicesACMEAccountKeysEndpointResponse503
]:
    """<h3>Description:</h3>Deletes multiple existing ACME Account Keys using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-keys-delete ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesACMEAccountKeysEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesACMEAccountKeysEndpointResponse400 | DeleteServicesACMEAccountKeysEndpointResponse401 | DeleteServicesACMEAccountKeysEndpointResponse403 | DeleteServicesACMEAccountKeysEndpointResponse404 | DeleteServicesACMEAccountKeysEndpointResponse405 | DeleteServicesACMEAccountKeysEndpointResponse406 | DeleteServicesACMEAccountKeysEndpointResponse409 | DeleteServicesACMEAccountKeysEndpointResponse415 | DeleteServicesACMEAccountKeysEndpointResponse422 | DeleteServicesACMEAccountKeysEndpointResponse424 | DeleteServicesACMEAccountKeysEndpointResponse500 | DeleteServicesACMEAccountKeysEndpointResponse503]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 0,
    offset: int | Unset = 0,
    query: DeleteServicesACMEAccountKeysEndpointQuery | Unset = UNSET,
) -> (
    DeleteServicesACMEAccountKeysEndpointResponse400
    | DeleteServicesACMEAccountKeysEndpointResponse401
    | DeleteServicesACMEAccountKeysEndpointResponse403
    | DeleteServicesACMEAccountKeysEndpointResponse404
    | DeleteServicesACMEAccountKeysEndpointResponse405
    | DeleteServicesACMEAccountKeysEndpointResponse406
    | DeleteServicesACMEAccountKeysEndpointResponse409
    | DeleteServicesACMEAccountKeysEndpointResponse415
    | DeleteServicesACMEAccountKeysEndpointResponse422
    | DeleteServicesACMEAccountKeysEndpointResponse424
    | DeleteServicesACMEAccountKeysEndpointResponse500
    | DeleteServicesACMEAccountKeysEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes multiple existing ACME Account Keys using a query.<br><br>WARNING: This
    will delete all objects that match the query, use with caution.<br><h3>Details:</h3>**Endpoint
    type**: Plural<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-keys-delete ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        limit (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        query (DeleteServicesACMEAccountKeysEndpointQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesACMEAccountKeysEndpointResponse400 | DeleteServicesACMEAccountKeysEndpointResponse401 | DeleteServicesACMEAccountKeysEndpointResponse403 | DeleteServicesACMEAccountKeysEndpointResponse404 | DeleteServicesACMEAccountKeysEndpointResponse405 | DeleteServicesACMEAccountKeysEndpointResponse406 | DeleteServicesACMEAccountKeysEndpointResponse409 | DeleteServicesACMEAccountKeysEndpointResponse415 | DeleteServicesACMEAccountKeysEndpointResponse422 | DeleteServicesACMEAccountKeysEndpointResponse424 | DeleteServicesACMEAccountKeysEndpointResponse500 | DeleteServicesACMEAccountKeysEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            query=query,
        )
    ).parsed
