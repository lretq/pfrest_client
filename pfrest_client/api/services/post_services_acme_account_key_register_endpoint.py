from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_acme_account_key_register_endpoint_data_body import (
    PostServicesACMEAccountKeyRegisterEndpointDataBody,
)
from ...models.post_services_acme_account_key_register_endpoint_json_body import (
    PostServicesACMEAccountKeyRegisterEndpointJsonBody,
)
from ...models.post_services_acme_account_key_register_endpoint_response_400 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse400,
)
from ...models.post_services_acme_account_key_register_endpoint_response_401 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse401,
)
from ...models.post_services_acme_account_key_register_endpoint_response_403 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse403,
)
from ...models.post_services_acme_account_key_register_endpoint_response_404 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse404,
)
from ...models.post_services_acme_account_key_register_endpoint_response_405 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse405,
)
from ...models.post_services_acme_account_key_register_endpoint_response_406 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse406,
)
from ...models.post_services_acme_account_key_register_endpoint_response_409 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse409,
)
from ...models.post_services_acme_account_key_register_endpoint_response_415 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse415,
)
from ...models.post_services_acme_account_key_register_endpoint_response_422 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse422,
)
from ...models.post_services_acme_account_key_register_endpoint_response_424 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse424,
)
from ...models.post_services_acme_account_key_register_endpoint_response_500 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse500,
)
from ...models.post_services_acme_account_key_register_endpoint_response_503 import (
    PostServicesACMEAccountKeyRegisterEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesACMEAccountKeyRegisterEndpointJsonBody
    | PostServicesACMEAccountKeyRegisterEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/acme/account_key/register",
    }

    if isinstance(body, PostServicesACMEAccountKeyRegisterEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesACMEAccountKeyRegisterEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesACMEAccountKeyRegisterEndpointResponse400
    | PostServicesACMEAccountKeyRegisterEndpointResponse401
    | PostServicesACMEAccountKeyRegisterEndpointResponse403
    | PostServicesACMEAccountKeyRegisterEndpointResponse404
    | PostServicesACMEAccountKeyRegisterEndpointResponse405
    | PostServicesACMEAccountKeyRegisterEndpointResponse406
    | PostServicesACMEAccountKeyRegisterEndpointResponse409
    | PostServicesACMEAccountKeyRegisterEndpointResponse415
    | PostServicesACMEAccountKeyRegisterEndpointResponse422
    | PostServicesACMEAccountKeyRegisterEndpointResponse424
    | PostServicesACMEAccountKeyRegisterEndpointResponse500
    | PostServicesACMEAccountKeyRegisterEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesACMEAccountKeyRegisterEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesACMEAccountKeyRegisterEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesACMEAccountKeyRegisterEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesACMEAccountKeyRegisterEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesACMEAccountKeyRegisterEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesACMEAccountKeyRegisterEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesACMEAccountKeyRegisterEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesACMEAccountKeyRegisterEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesACMEAccountKeyRegisterEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesACMEAccountKeyRegisterEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesACMEAccountKeyRegisterEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesACMEAccountKeyRegisterEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesACMEAccountKeyRegisterEndpointResponse400
    | PostServicesACMEAccountKeyRegisterEndpointResponse401
    | PostServicesACMEAccountKeyRegisterEndpointResponse403
    | PostServicesACMEAccountKeyRegisterEndpointResponse404
    | PostServicesACMEAccountKeyRegisterEndpointResponse405
    | PostServicesACMEAccountKeyRegisterEndpointResponse406
    | PostServicesACMEAccountKeyRegisterEndpointResponse409
    | PostServicesACMEAccountKeyRegisterEndpointResponse415
    | PostServicesACMEAccountKeyRegisterEndpointResponse422
    | PostServicesACMEAccountKeyRegisterEndpointResponse424
    | PostServicesACMEAccountKeyRegisterEndpointResponse500
    | PostServicesACMEAccountKeyRegisterEndpointResponse503
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
    body: PostServicesACMEAccountKeyRegisterEndpointJsonBody
    | PostServicesACMEAccountKeyRegisterEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesACMEAccountKeyRegisterEndpointResponse400
    | PostServicesACMEAccountKeyRegisterEndpointResponse401
    | PostServicesACMEAccountKeyRegisterEndpointResponse403
    | PostServicesACMEAccountKeyRegisterEndpointResponse404
    | PostServicesACMEAccountKeyRegisterEndpointResponse405
    | PostServicesACMEAccountKeyRegisterEndpointResponse406
    | PostServicesACMEAccountKeyRegisterEndpointResponse409
    | PostServicesACMEAccountKeyRegisterEndpointResponse415
    | PostServicesACMEAccountKeyRegisterEndpointResponse422
    | PostServicesACMEAccountKeyRegisterEndpointResponse424
    | PostServicesACMEAccountKeyRegisterEndpointResponse500
    | PostServicesACMEAccountKeyRegisterEndpointResponse503
]:
    """<h3>Description:</h3>Registers an existing ACME Account Key.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKeyRegister<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-register-post
    ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMEAccountKeyRegisterEndpointJsonBody | Unset):
        body (PostServicesACMEAccountKeyRegisterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMEAccountKeyRegisterEndpointResponse400 | PostServicesACMEAccountKeyRegisterEndpointResponse401 | PostServicesACMEAccountKeyRegisterEndpointResponse403 | PostServicesACMEAccountKeyRegisterEndpointResponse404 | PostServicesACMEAccountKeyRegisterEndpointResponse405 | PostServicesACMEAccountKeyRegisterEndpointResponse406 | PostServicesACMEAccountKeyRegisterEndpointResponse409 | PostServicesACMEAccountKeyRegisterEndpointResponse415 | PostServicesACMEAccountKeyRegisterEndpointResponse422 | PostServicesACMEAccountKeyRegisterEndpointResponse424 | PostServicesACMEAccountKeyRegisterEndpointResponse500 | PostServicesACMEAccountKeyRegisterEndpointResponse503]
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
    body: PostServicesACMEAccountKeyRegisterEndpointJsonBody
    | PostServicesACMEAccountKeyRegisterEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesACMEAccountKeyRegisterEndpointResponse400
    | PostServicesACMEAccountKeyRegisterEndpointResponse401
    | PostServicesACMEAccountKeyRegisterEndpointResponse403
    | PostServicesACMEAccountKeyRegisterEndpointResponse404
    | PostServicesACMEAccountKeyRegisterEndpointResponse405
    | PostServicesACMEAccountKeyRegisterEndpointResponse406
    | PostServicesACMEAccountKeyRegisterEndpointResponse409
    | PostServicesACMEAccountKeyRegisterEndpointResponse415
    | PostServicesACMEAccountKeyRegisterEndpointResponse422
    | PostServicesACMEAccountKeyRegisterEndpointResponse424
    | PostServicesACMEAccountKeyRegisterEndpointResponse500
    | PostServicesACMEAccountKeyRegisterEndpointResponse503
    | None
):
    """<h3>Description:</h3>Registers an existing ACME Account Key.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKeyRegister<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-register-post
    ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMEAccountKeyRegisterEndpointJsonBody | Unset):
        body (PostServicesACMEAccountKeyRegisterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMEAccountKeyRegisterEndpointResponse400 | PostServicesACMEAccountKeyRegisterEndpointResponse401 | PostServicesACMEAccountKeyRegisterEndpointResponse403 | PostServicesACMEAccountKeyRegisterEndpointResponse404 | PostServicesACMEAccountKeyRegisterEndpointResponse405 | PostServicesACMEAccountKeyRegisterEndpointResponse406 | PostServicesACMEAccountKeyRegisterEndpointResponse409 | PostServicesACMEAccountKeyRegisterEndpointResponse415 | PostServicesACMEAccountKeyRegisterEndpointResponse422 | PostServicesACMEAccountKeyRegisterEndpointResponse424 | PostServicesACMEAccountKeyRegisterEndpointResponse500 | PostServicesACMEAccountKeyRegisterEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMEAccountKeyRegisterEndpointJsonBody
    | PostServicesACMEAccountKeyRegisterEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesACMEAccountKeyRegisterEndpointResponse400
    | PostServicesACMEAccountKeyRegisterEndpointResponse401
    | PostServicesACMEAccountKeyRegisterEndpointResponse403
    | PostServicesACMEAccountKeyRegisterEndpointResponse404
    | PostServicesACMEAccountKeyRegisterEndpointResponse405
    | PostServicesACMEAccountKeyRegisterEndpointResponse406
    | PostServicesACMEAccountKeyRegisterEndpointResponse409
    | PostServicesACMEAccountKeyRegisterEndpointResponse415
    | PostServicesACMEAccountKeyRegisterEndpointResponse422
    | PostServicesACMEAccountKeyRegisterEndpointResponse424
    | PostServicesACMEAccountKeyRegisterEndpointResponse500
    | PostServicesACMEAccountKeyRegisterEndpointResponse503
]:
    """<h3>Description:</h3>Registers an existing ACME Account Key.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKeyRegister<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-register-post
    ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMEAccountKeyRegisterEndpointJsonBody | Unset):
        body (PostServicesACMEAccountKeyRegisterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesACMEAccountKeyRegisterEndpointResponse400 | PostServicesACMEAccountKeyRegisterEndpointResponse401 | PostServicesACMEAccountKeyRegisterEndpointResponse403 | PostServicesACMEAccountKeyRegisterEndpointResponse404 | PostServicesACMEAccountKeyRegisterEndpointResponse405 | PostServicesACMEAccountKeyRegisterEndpointResponse406 | PostServicesACMEAccountKeyRegisterEndpointResponse409 | PostServicesACMEAccountKeyRegisterEndpointResponse415 | PostServicesACMEAccountKeyRegisterEndpointResponse422 | PostServicesACMEAccountKeyRegisterEndpointResponse424 | PostServicesACMEAccountKeyRegisterEndpointResponse500 | PostServicesACMEAccountKeyRegisterEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesACMEAccountKeyRegisterEndpointJsonBody
    | PostServicesACMEAccountKeyRegisterEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesACMEAccountKeyRegisterEndpointResponse400
    | PostServicesACMEAccountKeyRegisterEndpointResponse401
    | PostServicesACMEAccountKeyRegisterEndpointResponse403
    | PostServicesACMEAccountKeyRegisterEndpointResponse404
    | PostServicesACMEAccountKeyRegisterEndpointResponse405
    | PostServicesACMEAccountKeyRegisterEndpointResponse406
    | PostServicesACMEAccountKeyRegisterEndpointResponse409
    | PostServicesACMEAccountKeyRegisterEndpointResponse415
    | PostServicesACMEAccountKeyRegisterEndpointResponse422
    | PostServicesACMEAccountKeyRegisterEndpointResponse424
    | PostServicesACMEAccountKeyRegisterEndpointResponse500
    | PostServicesACMEAccountKeyRegisterEndpointResponse503
    | None
):
    """<h3>Description:</h3>Registers an existing ACME Account Key.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: ACMEAccountKeyRegister<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-account-key-register-post
    ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**: Not
    Applicable<br>**Utilizes cache**: None

    Args:
        body (PostServicesACMEAccountKeyRegisterEndpointJsonBody | Unset):
        body (PostServicesACMEAccountKeyRegisterEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesACMEAccountKeyRegisterEndpointResponse400 | PostServicesACMEAccountKeyRegisterEndpointResponse401 | PostServicesACMEAccountKeyRegisterEndpointResponse403 | PostServicesACMEAccountKeyRegisterEndpointResponse404 | PostServicesACMEAccountKeyRegisterEndpointResponse405 | PostServicesACMEAccountKeyRegisterEndpointResponse406 | PostServicesACMEAccountKeyRegisterEndpointResponse409 | PostServicesACMEAccountKeyRegisterEndpointResponse415 | PostServicesACMEAccountKeyRegisterEndpointResponse422 | PostServicesACMEAccountKeyRegisterEndpointResponse424 | PostServicesACMEAccountKeyRegisterEndpointResponse500 | PostServicesACMEAccountKeyRegisterEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
