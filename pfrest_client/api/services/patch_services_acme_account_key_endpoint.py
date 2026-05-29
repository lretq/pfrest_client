from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_acme_account_key_endpoint_data_body import PatchServicesACMEAccountKeyEndpointDataBody
from ...models.patch_services_acme_account_key_endpoint_json_body import PatchServicesACMEAccountKeyEndpointJsonBody
from ...models.patch_services_acme_account_key_endpoint_response_400 import (
    PatchServicesACMEAccountKeyEndpointResponse400,
)
from ...models.patch_services_acme_account_key_endpoint_response_401 import (
    PatchServicesACMEAccountKeyEndpointResponse401,
)
from ...models.patch_services_acme_account_key_endpoint_response_403 import (
    PatchServicesACMEAccountKeyEndpointResponse403,
)
from ...models.patch_services_acme_account_key_endpoint_response_404 import (
    PatchServicesACMEAccountKeyEndpointResponse404,
)
from ...models.patch_services_acme_account_key_endpoint_response_405 import (
    PatchServicesACMEAccountKeyEndpointResponse405,
)
from ...models.patch_services_acme_account_key_endpoint_response_406 import (
    PatchServicesACMEAccountKeyEndpointResponse406,
)
from ...models.patch_services_acme_account_key_endpoint_response_409 import (
    PatchServicesACMEAccountKeyEndpointResponse409,
)
from ...models.patch_services_acme_account_key_endpoint_response_415 import (
    PatchServicesACMEAccountKeyEndpointResponse415,
)
from ...models.patch_services_acme_account_key_endpoint_response_422 import (
    PatchServicesACMEAccountKeyEndpointResponse422,
)
from ...models.patch_services_acme_account_key_endpoint_response_424 import (
    PatchServicesACMEAccountKeyEndpointResponse424,
)
from ...models.patch_services_acme_account_key_endpoint_response_500 import (
    PatchServicesACMEAccountKeyEndpointResponse500,
)
from ...models.patch_services_acme_account_key_endpoint_response_503 import (
    PatchServicesACMEAccountKeyEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesACMEAccountKeyEndpointJsonBody | PatchServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/acme/account_key",
    }

    if isinstance(body, PatchServicesACMEAccountKeyEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesACMEAccountKeyEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesACMEAccountKeyEndpointResponse400
    | PatchServicesACMEAccountKeyEndpointResponse401
    | PatchServicesACMEAccountKeyEndpointResponse403
    | PatchServicesACMEAccountKeyEndpointResponse404
    | PatchServicesACMEAccountKeyEndpointResponse405
    | PatchServicesACMEAccountKeyEndpointResponse406
    | PatchServicesACMEAccountKeyEndpointResponse409
    | PatchServicesACMEAccountKeyEndpointResponse415
    | PatchServicesACMEAccountKeyEndpointResponse422
    | PatchServicesACMEAccountKeyEndpointResponse424
    | PatchServicesACMEAccountKeyEndpointResponse500
    | PatchServicesACMEAccountKeyEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesACMEAccountKeyEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesACMEAccountKeyEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesACMEAccountKeyEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesACMEAccountKeyEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesACMEAccountKeyEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesACMEAccountKeyEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesACMEAccountKeyEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesACMEAccountKeyEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesACMEAccountKeyEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesACMEAccountKeyEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesACMEAccountKeyEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesACMEAccountKeyEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesACMEAccountKeyEndpointResponse400
    | PatchServicesACMEAccountKeyEndpointResponse401
    | PatchServicesACMEAccountKeyEndpointResponse403
    | PatchServicesACMEAccountKeyEndpointResponse404
    | PatchServicesACMEAccountKeyEndpointResponse405
    | PatchServicesACMEAccountKeyEndpointResponse406
    | PatchServicesACMEAccountKeyEndpointResponse409
    | PatchServicesACMEAccountKeyEndpointResponse415
    | PatchServicesACMEAccountKeyEndpointResponse422
    | PatchServicesACMEAccountKeyEndpointResponse424
    | PatchServicesACMEAccountKeyEndpointResponse500
    | PatchServicesACMEAccountKeyEndpointResponse503
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
    body: PatchServicesACMEAccountKeyEndpointJsonBody | PatchServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesACMEAccountKeyEndpointResponse400
    | PatchServicesACMEAccountKeyEndpointResponse401
    | PatchServicesACMEAccountKeyEndpointResponse403
    | PatchServicesACMEAccountKeyEndpointResponse404
    | PatchServicesACMEAccountKeyEndpointResponse405
    | PatchServicesACMEAccountKeyEndpointResponse406
    | PatchServicesACMEAccountKeyEndpointResponse409
    | PatchServicesACMEAccountKeyEndpointResponse415
    | PatchServicesACMEAccountKeyEndpointResponse422
    | PatchServicesACMEAccountKeyEndpointResponse424
    | PatchServicesACMEAccountKeyEndpointResponse500
    | PatchServicesACMEAccountKeyEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing ACME Account Key.<br><br>Note: You may need to re-register
    the account key with the ACME server after updating. You can register the account key using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMEAccountKeyEndpointJsonBody | Unset):
        body (PatchServicesACMEAccountKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMEAccountKeyEndpointResponse400 | PatchServicesACMEAccountKeyEndpointResponse401 | PatchServicesACMEAccountKeyEndpointResponse403 | PatchServicesACMEAccountKeyEndpointResponse404 | PatchServicesACMEAccountKeyEndpointResponse405 | PatchServicesACMEAccountKeyEndpointResponse406 | PatchServicesACMEAccountKeyEndpointResponse409 | PatchServicesACMEAccountKeyEndpointResponse415 | PatchServicesACMEAccountKeyEndpointResponse422 | PatchServicesACMEAccountKeyEndpointResponse424 | PatchServicesACMEAccountKeyEndpointResponse500 | PatchServicesACMEAccountKeyEndpointResponse503]
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
    body: PatchServicesACMEAccountKeyEndpointJsonBody | PatchServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesACMEAccountKeyEndpointResponse400
    | PatchServicesACMEAccountKeyEndpointResponse401
    | PatchServicesACMEAccountKeyEndpointResponse403
    | PatchServicesACMEAccountKeyEndpointResponse404
    | PatchServicesACMEAccountKeyEndpointResponse405
    | PatchServicesACMEAccountKeyEndpointResponse406
    | PatchServicesACMEAccountKeyEndpointResponse409
    | PatchServicesACMEAccountKeyEndpointResponse415
    | PatchServicesACMEAccountKeyEndpointResponse422
    | PatchServicesACMEAccountKeyEndpointResponse424
    | PatchServicesACMEAccountKeyEndpointResponse500
    | PatchServicesACMEAccountKeyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing ACME Account Key.<br><br>Note: You may need to re-register
    the account key with the ACME server after updating. You can register the account key using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMEAccountKeyEndpointJsonBody | Unset):
        body (PatchServicesACMEAccountKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMEAccountKeyEndpointResponse400 | PatchServicesACMEAccountKeyEndpointResponse401 | PatchServicesACMEAccountKeyEndpointResponse403 | PatchServicesACMEAccountKeyEndpointResponse404 | PatchServicesACMEAccountKeyEndpointResponse405 | PatchServicesACMEAccountKeyEndpointResponse406 | PatchServicesACMEAccountKeyEndpointResponse409 | PatchServicesACMEAccountKeyEndpointResponse415 | PatchServicesACMEAccountKeyEndpointResponse422 | PatchServicesACMEAccountKeyEndpointResponse424 | PatchServicesACMEAccountKeyEndpointResponse500 | PatchServicesACMEAccountKeyEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMEAccountKeyEndpointJsonBody | PatchServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesACMEAccountKeyEndpointResponse400
    | PatchServicesACMEAccountKeyEndpointResponse401
    | PatchServicesACMEAccountKeyEndpointResponse403
    | PatchServicesACMEAccountKeyEndpointResponse404
    | PatchServicesACMEAccountKeyEndpointResponse405
    | PatchServicesACMEAccountKeyEndpointResponse406
    | PatchServicesACMEAccountKeyEndpointResponse409
    | PatchServicesACMEAccountKeyEndpointResponse415
    | PatchServicesACMEAccountKeyEndpointResponse422
    | PatchServicesACMEAccountKeyEndpointResponse424
    | PatchServicesACMEAccountKeyEndpointResponse500
    | PatchServicesACMEAccountKeyEndpointResponse503
]:
    """<h3>Description:</h3>Updates an existing ACME Account Key.<br><br>Note: You may need to re-register
    the account key with the ACME server after updating. You can register the account key using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMEAccountKeyEndpointJsonBody | Unset):
        body (PatchServicesACMEAccountKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesACMEAccountKeyEndpointResponse400 | PatchServicesACMEAccountKeyEndpointResponse401 | PatchServicesACMEAccountKeyEndpointResponse403 | PatchServicesACMEAccountKeyEndpointResponse404 | PatchServicesACMEAccountKeyEndpointResponse405 | PatchServicesACMEAccountKeyEndpointResponse406 | PatchServicesACMEAccountKeyEndpointResponse409 | PatchServicesACMEAccountKeyEndpointResponse415 | PatchServicesACMEAccountKeyEndpointResponse422 | PatchServicesACMEAccountKeyEndpointResponse424 | PatchServicesACMEAccountKeyEndpointResponse500 | PatchServicesACMEAccountKeyEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesACMEAccountKeyEndpointJsonBody | PatchServicesACMEAccountKeyEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesACMEAccountKeyEndpointResponse400
    | PatchServicesACMEAccountKeyEndpointResponse401
    | PatchServicesACMEAccountKeyEndpointResponse403
    | PatchServicesACMEAccountKeyEndpointResponse404
    | PatchServicesACMEAccountKeyEndpointResponse405
    | PatchServicesACMEAccountKeyEndpointResponse406
    | PatchServicesACMEAccountKeyEndpointResponse409
    | PatchServicesACMEAccountKeyEndpointResponse415
    | PatchServicesACMEAccountKeyEndpointResponse422
    | PatchServicesACMEAccountKeyEndpointResponse424
    | PatchServicesACMEAccountKeyEndpointResponse500
    | PatchServicesACMEAccountKeyEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates an existing ACME Account Key.<br><br>Note: You may need to re-register
    the account key with the ACME server after updating. You can register the account key using the
    /api/v2/services/acme/account_key/register endpoint.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKey<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-patch ]<br>**Required
    packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesACMEAccountKeyEndpointJsonBody | Unset):
        body (PatchServicesACMEAccountKeyEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesACMEAccountKeyEndpointResponse400 | PatchServicesACMEAccountKeyEndpointResponse401 | PatchServicesACMEAccountKeyEndpointResponse403 | PatchServicesACMEAccountKeyEndpointResponse404 | PatchServicesACMEAccountKeyEndpointResponse405 | PatchServicesACMEAccountKeyEndpointResponse406 | PatchServicesACMEAccountKeyEndpointResponse409 | PatchServicesACMEAccountKeyEndpointResponse415 | PatchServicesACMEAccountKeyEndpointResponse422 | PatchServicesACMEAccountKeyEndpointResponse424 | PatchServicesACMEAccountKeyEndpointResponse500 | PatchServicesACMEAccountKeyEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
