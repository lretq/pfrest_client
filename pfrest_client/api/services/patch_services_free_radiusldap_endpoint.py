from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_services_free_radiusldap_endpoint_data_body import PatchServicesFreeRADIUSLDAPEndpointDataBody
from ...models.patch_services_free_radiusldap_endpoint_json_body import PatchServicesFreeRADIUSLDAPEndpointJsonBody
from ...models.patch_services_free_radiusldap_endpoint_response_400 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse400,
)
from ...models.patch_services_free_radiusldap_endpoint_response_401 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse401,
)
from ...models.patch_services_free_radiusldap_endpoint_response_403 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse403,
)
from ...models.patch_services_free_radiusldap_endpoint_response_404 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse404,
)
from ...models.patch_services_free_radiusldap_endpoint_response_405 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse405,
)
from ...models.patch_services_free_radiusldap_endpoint_response_406 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse406,
)
from ...models.patch_services_free_radiusldap_endpoint_response_409 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse409,
)
from ...models.patch_services_free_radiusldap_endpoint_response_415 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse415,
)
from ...models.patch_services_free_radiusldap_endpoint_response_422 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse422,
)
from ...models.patch_services_free_radiusldap_endpoint_response_424 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse424,
)
from ...models.patch_services_free_radiusldap_endpoint_response_500 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse500,
)
from ...models.patch_services_free_radiusldap_endpoint_response_503 import (
    PatchServicesFreeRADIUSLDAPEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchServicesFreeRADIUSLDAPEndpointJsonBody | PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/services/freeradius/ldap",
    }

    if isinstance(body, PatchServicesFreeRADIUSLDAPEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchServicesFreeRADIUSLDAPEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchServicesFreeRADIUSLDAPEndpointResponse400
    | PatchServicesFreeRADIUSLDAPEndpointResponse401
    | PatchServicesFreeRADIUSLDAPEndpointResponse403
    | PatchServicesFreeRADIUSLDAPEndpointResponse404
    | PatchServicesFreeRADIUSLDAPEndpointResponse405
    | PatchServicesFreeRADIUSLDAPEndpointResponse406
    | PatchServicesFreeRADIUSLDAPEndpointResponse409
    | PatchServicesFreeRADIUSLDAPEndpointResponse415
    | PatchServicesFreeRADIUSLDAPEndpointResponse422
    | PatchServicesFreeRADIUSLDAPEndpointResponse424
    | PatchServicesFreeRADIUSLDAPEndpointResponse500
    | PatchServicesFreeRADIUSLDAPEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PatchServicesFreeRADIUSLDAPEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchServicesFreeRADIUSLDAPEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchServicesFreeRADIUSLDAPEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchServicesFreeRADIUSLDAPEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PatchServicesFreeRADIUSLDAPEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PatchServicesFreeRADIUSLDAPEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchServicesFreeRADIUSLDAPEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PatchServicesFreeRADIUSLDAPEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PatchServicesFreeRADIUSLDAPEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PatchServicesFreeRADIUSLDAPEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PatchServicesFreeRADIUSLDAPEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PatchServicesFreeRADIUSLDAPEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchServicesFreeRADIUSLDAPEndpointResponse400
    | PatchServicesFreeRADIUSLDAPEndpointResponse401
    | PatchServicesFreeRADIUSLDAPEndpointResponse403
    | PatchServicesFreeRADIUSLDAPEndpointResponse404
    | PatchServicesFreeRADIUSLDAPEndpointResponse405
    | PatchServicesFreeRADIUSLDAPEndpointResponse406
    | PatchServicesFreeRADIUSLDAPEndpointResponse409
    | PatchServicesFreeRADIUSLDAPEndpointResponse415
    | PatchServicesFreeRADIUSLDAPEndpointResponse422
    | PatchServicesFreeRADIUSLDAPEndpointResponse424
    | PatchServicesFreeRADIUSLDAPEndpointResponse500
    | PatchServicesFreeRADIUSLDAPEndpointResponse503
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
    body: PatchServicesFreeRADIUSLDAPEndpointJsonBody | PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesFreeRADIUSLDAPEndpointResponse400
    | PatchServicesFreeRADIUSLDAPEndpointResponse401
    | PatchServicesFreeRADIUSLDAPEndpointResponse403
    | PatchServicesFreeRADIUSLDAPEndpointResponse404
    | PatchServicesFreeRADIUSLDAPEndpointResponse405
    | PatchServicesFreeRADIUSLDAPEndpointResponse406
    | PatchServicesFreeRADIUSLDAPEndpointResponse409
    | PatchServicesFreeRADIUSLDAPEndpointResponse415
    | PatchServicesFreeRADIUSLDAPEndpointResponse422
    | PatchServicesFreeRADIUSLDAPEndpointResponse424
    | PatchServicesFreeRADIUSLDAPEndpointResponse500
    | PatchServicesFreeRADIUSLDAPEndpointResponse503
]:
    """<h3>Description:</h3>Updates current FreeRADIUS LDAP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSLDAP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-ldap-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSLDAPEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesFreeRADIUSLDAPEndpointResponse400 | PatchServicesFreeRADIUSLDAPEndpointResponse401 | PatchServicesFreeRADIUSLDAPEndpointResponse403 | PatchServicesFreeRADIUSLDAPEndpointResponse404 | PatchServicesFreeRADIUSLDAPEndpointResponse405 | PatchServicesFreeRADIUSLDAPEndpointResponse406 | PatchServicesFreeRADIUSLDAPEndpointResponse409 | PatchServicesFreeRADIUSLDAPEndpointResponse415 | PatchServicesFreeRADIUSLDAPEndpointResponse422 | PatchServicesFreeRADIUSLDAPEndpointResponse424 | PatchServicesFreeRADIUSLDAPEndpointResponse500 | PatchServicesFreeRADIUSLDAPEndpointResponse503]
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
    body: PatchServicesFreeRADIUSLDAPEndpointJsonBody | PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesFreeRADIUSLDAPEndpointResponse400
    | PatchServicesFreeRADIUSLDAPEndpointResponse401
    | PatchServicesFreeRADIUSLDAPEndpointResponse403
    | PatchServicesFreeRADIUSLDAPEndpointResponse404
    | PatchServicesFreeRADIUSLDAPEndpointResponse405
    | PatchServicesFreeRADIUSLDAPEndpointResponse406
    | PatchServicesFreeRADIUSLDAPEndpointResponse409
    | PatchServicesFreeRADIUSLDAPEndpointResponse415
    | PatchServicesFreeRADIUSLDAPEndpointResponse422
    | PatchServicesFreeRADIUSLDAPEndpointResponse424
    | PatchServicesFreeRADIUSLDAPEndpointResponse500
    | PatchServicesFreeRADIUSLDAPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current FreeRADIUS LDAP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSLDAP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-ldap-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSLDAPEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesFreeRADIUSLDAPEndpointResponse400 | PatchServicesFreeRADIUSLDAPEndpointResponse401 | PatchServicesFreeRADIUSLDAPEndpointResponse403 | PatchServicesFreeRADIUSLDAPEndpointResponse404 | PatchServicesFreeRADIUSLDAPEndpointResponse405 | PatchServicesFreeRADIUSLDAPEndpointResponse406 | PatchServicesFreeRADIUSLDAPEndpointResponse409 | PatchServicesFreeRADIUSLDAPEndpointResponse415 | PatchServicesFreeRADIUSLDAPEndpointResponse422 | PatchServicesFreeRADIUSLDAPEndpointResponse424 | PatchServicesFreeRADIUSLDAPEndpointResponse500 | PatchServicesFreeRADIUSLDAPEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesFreeRADIUSLDAPEndpointJsonBody | PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset = UNSET,
) -> Response[
    PatchServicesFreeRADIUSLDAPEndpointResponse400
    | PatchServicesFreeRADIUSLDAPEndpointResponse401
    | PatchServicesFreeRADIUSLDAPEndpointResponse403
    | PatchServicesFreeRADIUSLDAPEndpointResponse404
    | PatchServicesFreeRADIUSLDAPEndpointResponse405
    | PatchServicesFreeRADIUSLDAPEndpointResponse406
    | PatchServicesFreeRADIUSLDAPEndpointResponse409
    | PatchServicesFreeRADIUSLDAPEndpointResponse415
    | PatchServicesFreeRADIUSLDAPEndpointResponse422
    | PatchServicesFreeRADIUSLDAPEndpointResponse424
    | PatchServicesFreeRADIUSLDAPEndpointResponse500
    | PatchServicesFreeRADIUSLDAPEndpointResponse503
]:
    """<h3>Description:</h3>Updates current FreeRADIUS LDAP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSLDAP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-ldap-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSLDAPEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServicesFreeRADIUSLDAPEndpointResponse400 | PatchServicesFreeRADIUSLDAPEndpointResponse401 | PatchServicesFreeRADIUSLDAPEndpointResponse403 | PatchServicesFreeRADIUSLDAPEndpointResponse404 | PatchServicesFreeRADIUSLDAPEndpointResponse405 | PatchServicesFreeRADIUSLDAPEndpointResponse406 | PatchServicesFreeRADIUSLDAPEndpointResponse409 | PatchServicesFreeRADIUSLDAPEndpointResponse415 | PatchServicesFreeRADIUSLDAPEndpointResponse422 | PatchServicesFreeRADIUSLDAPEndpointResponse424 | PatchServicesFreeRADIUSLDAPEndpointResponse500 | PatchServicesFreeRADIUSLDAPEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PatchServicesFreeRADIUSLDAPEndpointJsonBody | PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset = UNSET,
) -> (
    PatchServicesFreeRADIUSLDAPEndpointResponse400
    | PatchServicesFreeRADIUSLDAPEndpointResponse401
    | PatchServicesFreeRADIUSLDAPEndpointResponse403
    | PatchServicesFreeRADIUSLDAPEndpointResponse404
    | PatchServicesFreeRADIUSLDAPEndpointResponse405
    | PatchServicesFreeRADIUSLDAPEndpointResponse406
    | PatchServicesFreeRADIUSLDAPEndpointResponse409
    | PatchServicesFreeRADIUSLDAPEndpointResponse415
    | PatchServicesFreeRADIUSLDAPEndpointResponse422
    | PatchServicesFreeRADIUSLDAPEndpointResponse424
    | PatchServicesFreeRADIUSLDAPEndpointResponse500
    | PatchServicesFreeRADIUSLDAPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Updates current FreeRADIUS LDAP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSLDAP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-ldap-patch ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Args:
        body (PatchServicesFreeRADIUSLDAPEndpointJsonBody | Unset):
        body (PatchServicesFreeRADIUSLDAPEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServicesFreeRADIUSLDAPEndpointResponse400 | PatchServicesFreeRADIUSLDAPEndpointResponse401 | PatchServicesFreeRADIUSLDAPEndpointResponse403 | PatchServicesFreeRADIUSLDAPEndpointResponse404 | PatchServicesFreeRADIUSLDAPEndpointResponse405 | PatchServicesFreeRADIUSLDAPEndpointResponse406 | PatchServicesFreeRADIUSLDAPEndpointResponse409 | PatchServicesFreeRADIUSLDAPEndpointResponse415 | PatchServicesFreeRADIUSLDAPEndpointResponse422 | PatchServicesFreeRADIUSLDAPEndpointResponse424 | PatchServicesFreeRADIUSLDAPEndpointResponse500 | PatchServicesFreeRADIUSLDAPEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
