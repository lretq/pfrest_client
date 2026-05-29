from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_services_acme_account_keys_endpoint_data_body_item import (
    PutServicesACMEAccountKeysEndpointDataBodyItem,
)
from ...models.put_services_acme_account_keys_endpoint_json_body_item import (
    PutServicesACMEAccountKeysEndpointJsonBodyItem,
)
from ...models.put_services_acme_account_keys_endpoint_response_400 import PutServicesACMEAccountKeysEndpointResponse400
from ...models.put_services_acme_account_keys_endpoint_response_401 import PutServicesACMEAccountKeysEndpointResponse401
from ...models.put_services_acme_account_keys_endpoint_response_403 import PutServicesACMEAccountKeysEndpointResponse403
from ...models.put_services_acme_account_keys_endpoint_response_404 import PutServicesACMEAccountKeysEndpointResponse404
from ...models.put_services_acme_account_keys_endpoint_response_405 import PutServicesACMEAccountKeysEndpointResponse405
from ...models.put_services_acme_account_keys_endpoint_response_406 import PutServicesACMEAccountKeysEndpointResponse406
from ...models.put_services_acme_account_keys_endpoint_response_409 import PutServicesACMEAccountKeysEndpointResponse409
from ...models.put_services_acme_account_keys_endpoint_response_415 import PutServicesACMEAccountKeysEndpointResponse415
from ...models.put_services_acme_account_keys_endpoint_response_422 import PutServicesACMEAccountKeysEndpointResponse422
from ...models.put_services_acme_account_keys_endpoint_response_424 import PutServicesACMEAccountKeysEndpointResponse424
from ...models.put_services_acme_account_keys_endpoint_response_500 import PutServicesACMEAccountKeysEndpointResponse500
from ...models.put_services_acme_account_keys_endpoint_response_503 import PutServicesACMEAccountKeysEndpointResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[PutServicesACMEAccountKeysEndpointJsonBodyItem]
    | list[PutServicesACMEAccountKeysEndpointDataBodyItem]
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/services/acme/account_keys",
    }

    if isinstance(body, list[PutServicesACMEAccountKeysEndpointJsonBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[PutServicesACMEAccountKeysEndpointDataBodyItem]):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutServicesACMEAccountKeysEndpointResponse400
    | PutServicesACMEAccountKeysEndpointResponse401
    | PutServicesACMEAccountKeysEndpointResponse403
    | PutServicesACMEAccountKeysEndpointResponse404
    | PutServicesACMEAccountKeysEndpointResponse405
    | PutServicesACMEAccountKeysEndpointResponse406
    | PutServicesACMEAccountKeysEndpointResponse409
    | PutServicesACMEAccountKeysEndpointResponse415
    | PutServicesACMEAccountKeysEndpointResponse422
    | PutServicesACMEAccountKeysEndpointResponse424
    | PutServicesACMEAccountKeysEndpointResponse500
    | PutServicesACMEAccountKeysEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PutServicesACMEAccountKeysEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutServicesACMEAccountKeysEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutServicesACMEAccountKeysEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutServicesACMEAccountKeysEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PutServicesACMEAccountKeysEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PutServicesACMEAccountKeysEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PutServicesACMEAccountKeysEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PutServicesACMEAccountKeysEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PutServicesACMEAccountKeysEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PutServicesACMEAccountKeysEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PutServicesACMEAccountKeysEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PutServicesACMEAccountKeysEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutServicesACMEAccountKeysEndpointResponse400
    | PutServicesACMEAccountKeysEndpointResponse401
    | PutServicesACMEAccountKeysEndpointResponse403
    | PutServicesACMEAccountKeysEndpointResponse404
    | PutServicesACMEAccountKeysEndpointResponse405
    | PutServicesACMEAccountKeysEndpointResponse406
    | PutServicesACMEAccountKeysEndpointResponse409
    | PutServicesACMEAccountKeysEndpointResponse415
    | PutServicesACMEAccountKeysEndpointResponse422
    | PutServicesACMEAccountKeysEndpointResponse424
    | PutServicesACMEAccountKeysEndpointResponse500
    | PutServicesACMEAccountKeysEndpointResponse503
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
    body: list[PutServicesACMEAccountKeysEndpointJsonBodyItem]
    | list[PutServicesACMEAccountKeysEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesACMEAccountKeysEndpointResponse400
    | PutServicesACMEAccountKeysEndpointResponse401
    | PutServicesACMEAccountKeysEndpointResponse403
    | PutServicesACMEAccountKeysEndpointResponse404
    | PutServicesACMEAccountKeysEndpointResponse405
    | PutServicesACMEAccountKeysEndpointResponse406
    | PutServicesACMEAccountKeysEndpointResponse409
    | PutServicesACMEAccountKeysEndpointResponse415
    | PutServicesACMEAccountKeysEndpointResponse422
    | PutServicesACMEAccountKeysEndpointResponse424
    | PutServicesACMEAccountKeysEndpointResponse500
    | PutServicesACMEAccountKeysEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing ACME Account Keys.<br><br>Note: You may need to register
    the account keys with the ACME server after replacing. You can register account keys using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-keys-put ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesACMEAccountKeysEndpointJsonBodyItem] | Unset):
        body (list[PutServicesACMEAccountKeysEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesACMEAccountKeysEndpointResponse400 | PutServicesACMEAccountKeysEndpointResponse401 | PutServicesACMEAccountKeysEndpointResponse403 | PutServicesACMEAccountKeysEndpointResponse404 | PutServicesACMEAccountKeysEndpointResponse405 | PutServicesACMEAccountKeysEndpointResponse406 | PutServicesACMEAccountKeysEndpointResponse409 | PutServicesACMEAccountKeysEndpointResponse415 | PutServicesACMEAccountKeysEndpointResponse422 | PutServicesACMEAccountKeysEndpointResponse424 | PutServicesACMEAccountKeysEndpointResponse500 | PutServicesACMEAccountKeysEndpointResponse503]
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
    body: list[PutServicesACMEAccountKeysEndpointJsonBodyItem]
    | list[PutServicesACMEAccountKeysEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesACMEAccountKeysEndpointResponse400
    | PutServicesACMEAccountKeysEndpointResponse401
    | PutServicesACMEAccountKeysEndpointResponse403
    | PutServicesACMEAccountKeysEndpointResponse404
    | PutServicesACMEAccountKeysEndpointResponse405
    | PutServicesACMEAccountKeysEndpointResponse406
    | PutServicesACMEAccountKeysEndpointResponse409
    | PutServicesACMEAccountKeysEndpointResponse415
    | PutServicesACMEAccountKeysEndpointResponse422
    | PutServicesACMEAccountKeysEndpointResponse424
    | PutServicesACMEAccountKeysEndpointResponse500
    | PutServicesACMEAccountKeysEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing ACME Account Keys.<br><br>Note: You may need to register
    the account keys with the ACME server after replacing. You can register account keys using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-keys-put ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesACMEAccountKeysEndpointJsonBodyItem] | Unset):
        body (list[PutServicesACMEAccountKeysEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesACMEAccountKeysEndpointResponse400 | PutServicesACMEAccountKeysEndpointResponse401 | PutServicesACMEAccountKeysEndpointResponse403 | PutServicesACMEAccountKeysEndpointResponse404 | PutServicesACMEAccountKeysEndpointResponse405 | PutServicesACMEAccountKeysEndpointResponse406 | PutServicesACMEAccountKeysEndpointResponse409 | PutServicesACMEAccountKeysEndpointResponse415 | PutServicesACMEAccountKeysEndpointResponse422 | PutServicesACMEAccountKeysEndpointResponse424 | PutServicesACMEAccountKeysEndpointResponse500 | PutServicesACMEAccountKeysEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesACMEAccountKeysEndpointJsonBodyItem]
    | list[PutServicesACMEAccountKeysEndpointDataBodyItem]
    | Unset = UNSET,
) -> Response[
    PutServicesACMEAccountKeysEndpointResponse400
    | PutServicesACMEAccountKeysEndpointResponse401
    | PutServicesACMEAccountKeysEndpointResponse403
    | PutServicesACMEAccountKeysEndpointResponse404
    | PutServicesACMEAccountKeysEndpointResponse405
    | PutServicesACMEAccountKeysEndpointResponse406
    | PutServicesACMEAccountKeysEndpointResponse409
    | PutServicesACMEAccountKeysEndpointResponse415
    | PutServicesACMEAccountKeysEndpointResponse422
    | PutServicesACMEAccountKeysEndpointResponse424
    | PutServicesACMEAccountKeysEndpointResponse500
    | PutServicesACMEAccountKeysEndpointResponse503
]:
    """<h3>Description:</h3>Replaces all existing ACME Account Keys.<br><br>Note: You may need to register
    the account keys with the ACME server after replacing. You can register account keys using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-keys-put ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesACMEAccountKeysEndpointJsonBodyItem] | Unset):
        body (list[PutServicesACMEAccountKeysEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutServicesACMEAccountKeysEndpointResponse400 | PutServicesACMEAccountKeysEndpointResponse401 | PutServicesACMEAccountKeysEndpointResponse403 | PutServicesACMEAccountKeysEndpointResponse404 | PutServicesACMEAccountKeysEndpointResponse405 | PutServicesACMEAccountKeysEndpointResponse406 | PutServicesACMEAccountKeysEndpointResponse409 | PutServicesACMEAccountKeysEndpointResponse415 | PutServicesACMEAccountKeysEndpointResponse422 | PutServicesACMEAccountKeysEndpointResponse424 | PutServicesACMEAccountKeysEndpointResponse500 | PutServicesACMEAccountKeysEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[PutServicesACMEAccountKeysEndpointJsonBodyItem]
    | list[PutServicesACMEAccountKeysEndpointDataBodyItem]
    | Unset = UNSET,
) -> (
    PutServicesACMEAccountKeysEndpointResponse400
    | PutServicesACMEAccountKeysEndpointResponse401
    | PutServicesACMEAccountKeysEndpointResponse403
    | PutServicesACMEAccountKeysEndpointResponse404
    | PutServicesACMEAccountKeysEndpointResponse405
    | PutServicesACMEAccountKeysEndpointResponse406
    | PutServicesACMEAccountKeysEndpointResponse409
    | PutServicesACMEAccountKeysEndpointResponse415
    | PutServicesACMEAccountKeysEndpointResponse422
    | PutServicesACMEAccountKeysEndpointResponse424
    | PutServicesACMEAccountKeysEndpointResponse500
    | PutServicesACMEAccountKeysEndpointResponse503
    | None
):
    """<h3>Description:</h3>Replaces all existing ACME Account Keys.<br><br>Note: You may need to register
    the account keys with the ACME server after replacing. You can register account keys using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Plural<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-keys-put ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (list[PutServicesACMEAccountKeysEndpointJsonBodyItem] | Unset):
        body (list[PutServicesACMEAccountKeysEndpointDataBodyItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutServicesACMEAccountKeysEndpointResponse400 | PutServicesACMEAccountKeysEndpointResponse401 | PutServicesACMEAccountKeysEndpointResponse403 | PutServicesACMEAccountKeysEndpointResponse404 | PutServicesACMEAccountKeysEndpointResponse405 | PutServicesACMEAccountKeysEndpointResponse406 | PutServicesACMEAccountKeysEndpointResponse409 | PutServicesACMEAccountKeysEndpointResponse415 | PutServicesACMEAccountKeysEndpointResponse422 | PutServicesACMEAccountKeysEndpointResponse424 | PutServicesACMEAccountKeysEndpointResponse500 | PutServicesACMEAccountKeysEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
