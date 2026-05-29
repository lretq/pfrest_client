from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_acme_certificate_action_endpoint_response_400 import (
    GetServicesACMECertificateActionEndpointResponse400,
)
from ...models.get_services_acme_certificate_action_endpoint_response_401 import (
    GetServicesACMECertificateActionEndpointResponse401,
)
from ...models.get_services_acme_certificate_action_endpoint_response_403 import (
    GetServicesACMECertificateActionEndpointResponse403,
)
from ...models.get_services_acme_certificate_action_endpoint_response_404 import (
    GetServicesACMECertificateActionEndpointResponse404,
)
from ...models.get_services_acme_certificate_action_endpoint_response_405 import (
    GetServicesACMECertificateActionEndpointResponse405,
)
from ...models.get_services_acme_certificate_action_endpoint_response_406 import (
    GetServicesACMECertificateActionEndpointResponse406,
)
from ...models.get_services_acme_certificate_action_endpoint_response_409 import (
    GetServicesACMECertificateActionEndpointResponse409,
)
from ...models.get_services_acme_certificate_action_endpoint_response_415 import (
    GetServicesACMECertificateActionEndpointResponse415,
)
from ...models.get_services_acme_certificate_action_endpoint_response_422 import (
    GetServicesACMECertificateActionEndpointResponse422,
)
from ...models.get_services_acme_certificate_action_endpoint_response_424 import (
    GetServicesACMECertificateActionEndpointResponse424,
)
from ...models.get_services_acme_certificate_action_endpoint_response_500 import (
    GetServicesACMECertificateActionEndpointResponse500,
)
from ...models.get_services_acme_certificate_action_endpoint_response_503 import (
    GetServicesACMECertificateActionEndpointResponse503,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    parent_id: int | str,
    id: int | str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parent_id: int | str
    json_parent_id = parent_id
    params["parent_id"] = json_parent_id

    json_id: int | str
    json_id = id
    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/acme/certificate/action",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesACMECertificateActionEndpointResponse400
    | GetServicesACMECertificateActionEndpointResponse401
    | GetServicesACMECertificateActionEndpointResponse403
    | GetServicesACMECertificateActionEndpointResponse404
    | GetServicesACMECertificateActionEndpointResponse405
    | GetServicesACMECertificateActionEndpointResponse406
    | GetServicesACMECertificateActionEndpointResponse409
    | GetServicesACMECertificateActionEndpointResponse415
    | GetServicesACMECertificateActionEndpointResponse422
    | GetServicesACMECertificateActionEndpointResponse424
    | GetServicesACMECertificateActionEndpointResponse500
    | GetServicesACMECertificateActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesACMECertificateActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesACMECertificateActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesACMECertificateActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesACMECertificateActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesACMECertificateActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesACMECertificateActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesACMECertificateActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesACMECertificateActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesACMECertificateActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesACMECertificateActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesACMECertificateActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesACMECertificateActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesACMECertificateActionEndpointResponse400
    | GetServicesACMECertificateActionEndpointResponse401
    | GetServicesACMECertificateActionEndpointResponse403
    | GetServicesACMECertificateActionEndpointResponse404
    | GetServicesACMECertificateActionEndpointResponse405
    | GetServicesACMECertificateActionEndpointResponse406
    | GetServicesACMECertificateActionEndpointResponse409
    | GetServicesACMECertificateActionEndpointResponse415
    | GetServicesACMECertificateActionEndpointResponse422
    | GetServicesACMECertificateActionEndpointResponse424
    | GetServicesACMECertificateActionEndpointResponse500
    | GetServicesACMECertificateActionEndpointResponse503
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
    parent_id: int | str,
    id: int | str,
) -> Response[
    GetServicesACMECertificateActionEndpointResponse400
    | GetServicesACMECertificateActionEndpointResponse401
    | GetServicesACMECertificateActionEndpointResponse403
    | GetServicesACMECertificateActionEndpointResponse404
    | GetServicesACMECertificateActionEndpointResponse405
    | GetServicesACMECertificateActionEndpointResponse406
    | GetServicesACMECertificateActionEndpointResponse409
    | GetServicesACMECertificateActionEndpointResponse415
    | GetServicesACMECertificateActionEndpointResponse422
    | GetServicesACMECertificateActionEndpointResponse424
    | GetServicesACMECertificateActionEndpointResponse500
    | GetServicesACMECertificateActionEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-get ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesACMECertificateActionEndpointResponse400 | GetServicesACMECertificateActionEndpointResponse401 | GetServicesACMECertificateActionEndpointResponse403 | GetServicesACMECertificateActionEndpointResponse404 | GetServicesACMECertificateActionEndpointResponse405 | GetServicesACMECertificateActionEndpointResponse406 | GetServicesACMECertificateActionEndpointResponse409 | GetServicesACMECertificateActionEndpointResponse415 | GetServicesACMECertificateActionEndpointResponse422 | GetServicesACMECertificateActionEndpointResponse424 | GetServicesACMECertificateActionEndpointResponse500 | GetServicesACMECertificateActionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    GetServicesACMECertificateActionEndpointResponse400
    | GetServicesACMECertificateActionEndpointResponse401
    | GetServicesACMECertificateActionEndpointResponse403
    | GetServicesACMECertificateActionEndpointResponse404
    | GetServicesACMECertificateActionEndpointResponse405
    | GetServicesACMECertificateActionEndpointResponse406
    | GetServicesACMECertificateActionEndpointResponse409
    | GetServicesACMECertificateActionEndpointResponse415
    | GetServicesACMECertificateActionEndpointResponse422
    | GetServicesACMECertificateActionEndpointResponse424
    | GetServicesACMECertificateActionEndpointResponse500
    | GetServicesACMECertificateActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-get ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesACMECertificateActionEndpointResponse400 | GetServicesACMECertificateActionEndpointResponse401 | GetServicesACMECertificateActionEndpointResponse403 | GetServicesACMECertificateActionEndpointResponse404 | GetServicesACMECertificateActionEndpointResponse405 | GetServicesACMECertificateActionEndpointResponse406 | GetServicesACMECertificateActionEndpointResponse409 | GetServicesACMECertificateActionEndpointResponse415 | GetServicesACMECertificateActionEndpointResponse422 | GetServicesACMECertificateActionEndpointResponse424 | GetServicesACMECertificateActionEndpointResponse500 | GetServicesACMECertificateActionEndpointResponse503
    """

    return sync_detailed(
        client=client,
        parent_id=parent_id,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> Response[
    GetServicesACMECertificateActionEndpointResponse400
    | GetServicesACMECertificateActionEndpointResponse401
    | GetServicesACMECertificateActionEndpointResponse403
    | GetServicesACMECertificateActionEndpointResponse404
    | GetServicesACMECertificateActionEndpointResponse405
    | GetServicesACMECertificateActionEndpointResponse406
    | GetServicesACMECertificateActionEndpointResponse409
    | GetServicesACMECertificateActionEndpointResponse415
    | GetServicesACMECertificateActionEndpointResponse422
    | GetServicesACMECertificateActionEndpointResponse424
    | GetServicesACMECertificateActionEndpointResponse500
    | GetServicesACMECertificateActionEndpointResponse503
]:
    """<h3>Description:</h3>Reads an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-get ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesACMECertificateActionEndpointResponse400 | GetServicesACMECertificateActionEndpointResponse401 | GetServicesACMECertificateActionEndpointResponse403 | GetServicesACMECertificateActionEndpointResponse404 | GetServicesACMECertificateActionEndpointResponse405 | GetServicesACMECertificateActionEndpointResponse406 | GetServicesACMECertificateActionEndpointResponse409 | GetServicesACMECertificateActionEndpointResponse415 | GetServicesACMECertificateActionEndpointResponse422 | GetServicesACMECertificateActionEndpointResponse424 | GetServicesACMECertificateActionEndpointResponse500 | GetServicesACMECertificateActionEndpointResponse503]
    """

    kwargs = _get_kwargs(
        parent_id=parent_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_id: int | str,
    id: int | str,
) -> (
    GetServicesACMECertificateActionEndpointResponse400
    | GetServicesACMECertificateActionEndpointResponse401
    | GetServicesACMECertificateActionEndpointResponse403
    | GetServicesACMECertificateActionEndpointResponse404
    | GetServicesACMECertificateActionEndpointResponse405
    | GetServicesACMECertificateActionEndpointResponse406
    | GetServicesACMECertificateActionEndpointResponse409
    | GetServicesACMECertificateActionEndpointResponse415
    | GetServicesACMECertificateActionEndpointResponse422
    | GetServicesACMECertificateActionEndpointResponse424
    | GetServicesACMECertificateActionEndpointResponse500
    | GetServicesACMECertificateActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-get ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies immediately**:
    Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesACMECertificateActionEndpointResponse400 | GetServicesACMECertificateActionEndpointResponse401 | GetServicesACMECertificateActionEndpointResponse403 | GetServicesACMECertificateActionEndpointResponse404 | GetServicesACMECertificateActionEndpointResponse405 | GetServicesACMECertificateActionEndpointResponse406 | GetServicesACMECertificateActionEndpointResponse409 | GetServicesACMECertificateActionEndpointResponse415 | GetServicesACMECertificateActionEndpointResponse422 | GetServicesACMECertificateActionEndpointResponse424 | GetServicesACMECertificateActionEndpointResponse500 | GetServicesACMECertificateActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
