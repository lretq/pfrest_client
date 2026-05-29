from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_services_acme_certificate_action_endpoint_response_400 import (
    DeleteServicesACMECertificateActionEndpointResponse400,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_401 import (
    DeleteServicesACMECertificateActionEndpointResponse401,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_403 import (
    DeleteServicesACMECertificateActionEndpointResponse403,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_404 import (
    DeleteServicesACMECertificateActionEndpointResponse404,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_405 import (
    DeleteServicesACMECertificateActionEndpointResponse405,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_406 import (
    DeleteServicesACMECertificateActionEndpointResponse406,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_409 import (
    DeleteServicesACMECertificateActionEndpointResponse409,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_415 import (
    DeleteServicesACMECertificateActionEndpointResponse415,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_422 import (
    DeleteServicesACMECertificateActionEndpointResponse422,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_424 import (
    DeleteServicesACMECertificateActionEndpointResponse424,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_500 import (
    DeleteServicesACMECertificateActionEndpointResponse500,
)
from ...models.delete_services_acme_certificate_action_endpoint_response_503 import (
    DeleteServicesACMECertificateActionEndpointResponse503,
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
        "method": "delete",
        "url": "/api/v2/services/acme/certificate/action",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteServicesACMECertificateActionEndpointResponse400
    | DeleteServicesACMECertificateActionEndpointResponse401
    | DeleteServicesACMECertificateActionEndpointResponse403
    | DeleteServicesACMECertificateActionEndpointResponse404
    | DeleteServicesACMECertificateActionEndpointResponse405
    | DeleteServicesACMECertificateActionEndpointResponse406
    | DeleteServicesACMECertificateActionEndpointResponse409
    | DeleteServicesACMECertificateActionEndpointResponse415
    | DeleteServicesACMECertificateActionEndpointResponse422
    | DeleteServicesACMECertificateActionEndpointResponse424
    | DeleteServicesACMECertificateActionEndpointResponse500
    | DeleteServicesACMECertificateActionEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = DeleteServicesACMECertificateActionEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteServicesACMECertificateActionEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteServicesACMECertificateActionEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteServicesACMECertificateActionEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = DeleteServicesACMECertificateActionEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = DeleteServicesACMECertificateActionEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteServicesACMECertificateActionEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = DeleteServicesACMECertificateActionEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = DeleteServicesACMECertificateActionEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = DeleteServicesACMECertificateActionEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = DeleteServicesACMECertificateActionEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DeleteServicesACMECertificateActionEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteServicesACMECertificateActionEndpointResponse400
    | DeleteServicesACMECertificateActionEndpointResponse401
    | DeleteServicesACMECertificateActionEndpointResponse403
    | DeleteServicesACMECertificateActionEndpointResponse404
    | DeleteServicesACMECertificateActionEndpointResponse405
    | DeleteServicesACMECertificateActionEndpointResponse406
    | DeleteServicesACMECertificateActionEndpointResponse409
    | DeleteServicesACMECertificateActionEndpointResponse415
    | DeleteServicesACMECertificateActionEndpointResponse422
    | DeleteServicesACMECertificateActionEndpointResponse424
    | DeleteServicesACMECertificateActionEndpointResponse500
    | DeleteServicesACMECertificateActionEndpointResponse503
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
    DeleteServicesACMECertificateActionEndpointResponse400
    | DeleteServicesACMECertificateActionEndpointResponse401
    | DeleteServicesACMECertificateActionEndpointResponse403
    | DeleteServicesACMECertificateActionEndpointResponse404
    | DeleteServicesACMECertificateActionEndpointResponse405
    | DeleteServicesACMECertificateActionEndpointResponse406
    | DeleteServicesACMECertificateActionEndpointResponse409
    | DeleteServicesACMECertificateActionEndpointResponse415
    | DeleteServicesACMECertificateActionEndpointResponse422
    | DeleteServicesACMECertificateActionEndpointResponse424
    | DeleteServicesACMECertificateActionEndpointResponse500
    | DeleteServicesACMECertificateActionEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-delete ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesACMECertificateActionEndpointResponse400 | DeleteServicesACMECertificateActionEndpointResponse401 | DeleteServicesACMECertificateActionEndpointResponse403 | DeleteServicesACMECertificateActionEndpointResponse404 | DeleteServicesACMECertificateActionEndpointResponse405 | DeleteServicesACMECertificateActionEndpointResponse406 | DeleteServicesACMECertificateActionEndpointResponse409 | DeleteServicesACMECertificateActionEndpointResponse415 | DeleteServicesACMECertificateActionEndpointResponse422 | DeleteServicesACMECertificateActionEndpointResponse424 | DeleteServicesACMECertificateActionEndpointResponse500 | DeleteServicesACMECertificateActionEndpointResponse503]
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
    DeleteServicesACMECertificateActionEndpointResponse400
    | DeleteServicesACMECertificateActionEndpointResponse401
    | DeleteServicesACMECertificateActionEndpointResponse403
    | DeleteServicesACMECertificateActionEndpointResponse404
    | DeleteServicesACMECertificateActionEndpointResponse405
    | DeleteServicesACMECertificateActionEndpointResponse406
    | DeleteServicesACMECertificateActionEndpointResponse409
    | DeleteServicesACMECertificateActionEndpointResponse415
    | DeleteServicesACMECertificateActionEndpointResponse422
    | DeleteServicesACMECertificateActionEndpointResponse424
    | DeleteServicesACMECertificateActionEndpointResponse500
    | DeleteServicesACMECertificateActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-delete ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesACMECertificateActionEndpointResponse400 | DeleteServicesACMECertificateActionEndpointResponse401 | DeleteServicesACMECertificateActionEndpointResponse403 | DeleteServicesACMECertificateActionEndpointResponse404 | DeleteServicesACMECertificateActionEndpointResponse405 | DeleteServicesACMECertificateActionEndpointResponse406 | DeleteServicesACMECertificateActionEndpointResponse409 | DeleteServicesACMECertificateActionEndpointResponse415 | DeleteServicesACMECertificateActionEndpointResponse422 | DeleteServicesACMECertificateActionEndpointResponse424 | DeleteServicesACMECertificateActionEndpointResponse500 | DeleteServicesACMECertificateActionEndpointResponse503
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
    DeleteServicesACMECertificateActionEndpointResponse400
    | DeleteServicesACMECertificateActionEndpointResponse401
    | DeleteServicesACMECertificateActionEndpointResponse403
    | DeleteServicesACMECertificateActionEndpointResponse404
    | DeleteServicesACMECertificateActionEndpointResponse405
    | DeleteServicesACMECertificateActionEndpointResponse406
    | DeleteServicesACMECertificateActionEndpointResponse409
    | DeleteServicesACMECertificateActionEndpointResponse415
    | DeleteServicesACMECertificateActionEndpointResponse422
    | DeleteServicesACMECertificateActionEndpointResponse424
    | DeleteServicesACMECertificateActionEndpointResponse500
    | DeleteServicesACMECertificateActionEndpointResponse503
]:
    """<h3>Description:</h3>Deletes an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-delete ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServicesACMECertificateActionEndpointResponse400 | DeleteServicesACMECertificateActionEndpointResponse401 | DeleteServicesACMECertificateActionEndpointResponse403 | DeleteServicesACMECertificateActionEndpointResponse404 | DeleteServicesACMECertificateActionEndpointResponse405 | DeleteServicesACMECertificateActionEndpointResponse406 | DeleteServicesACMECertificateActionEndpointResponse409 | DeleteServicesACMECertificateActionEndpointResponse415 | DeleteServicesACMECertificateActionEndpointResponse422 | DeleteServicesACMECertificateActionEndpointResponse424 | DeleteServicesACMECertificateActionEndpointResponse500 | DeleteServicesACMECertificateActionEndpointResponse503]
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
    DeleteServicesACMECertificateActionEndpointResponse400
    | DeleteServicesACMECertificateActionEndpointResponse401
    | DeleteServicesACMECertificateActionEndpointResponse403
    | DeleteServicesACMECertificateActionEndpointResponse404
    | DeleteServicesACMECertificateActionEndpointResponse405
    | DeleteServicesACMECertificateActionEndpointResponse406
    | DeleteServicesACMECertificateActionEndpointResponse409
    | DeleteServicesACMECertificateActionEndpointResponse415
    | DeleteServicesACMECertificateActionEndpointResponse422
    | DeleteServicesACMECertificateActionEndpointResponse424
    | DeleteServicesACMECertificateActionEndpointResponse500
    | DeleteServicesACMECertificateActionEndpointResponse503
    | None
):
    """<h3>Description:</h3>Deletes an existing ACME Certificate Action.<br><h3>Details:</h3>**Endpoint
    type**: Singular<br>**Associated model**: ACMECertificateAction<br>**Parent model**:
    ACMECertificate<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-acme-
    certificate-action-delete ]<br>**Required packages**: [ pfSense-pkg-acme ]<br>**Applies
    immediately**: Yes<br>**Utilizes cache**: None

    Args:
        parent_id (int | str):
        id (int | str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServicesACMECertificateActionEndpointResponse400 | DeleteServicesACMECertificateActionEndpointResponse401 | DeleteServicesACMECertificateActionEndpointResponse403 | DeleteServicesACMECertificateActionEndpointResponse404 | DeleteServicesACMECertificateActionEndpointResponse405 | DeleteServicesACMECertificateActionEndpointResponse406 | DeleteServicesACMECertificateActionEndpointResponse409 | DeleteServicesACMECertificateActionEndpointResponse415 | DeleteServicesACMECertificateActionEndpointResponse422 | DeleteServicesACMECertificateActionEndpointResponse424 | DeleteServicesACMECertificateActionEndpointResponse500 | DeleteServicesACMECertificateActionEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_id=parent_id,
            id=id,
        )
    ).parsed
