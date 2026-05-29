from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_services_free_radiusldap_endpoint_response_400 import GetServicesFreeRADIUSLDAPEndpointResponse400
from ...models.get_services_free_radiusldap_endpoint_response_401 import GetServicesFreeRADIUSLDAPEndpointResponse401
from ...models.get_services_free_radiusldap_endpoint_response_403 import GetServicesFreeRADIUSLDAPEndpointResponse403
from ...models.get_services_free_radiusldap_endpoint_response_404 import GetServicesFreeRADIUSLDAPEndpointResponse404
from ...models.get_services_free_radiusldap_endpoint_response_405 import GetServicesFreeRADIUSLDAPEndpointResponse405
from ...models.get_services_free_radiusldap_endpoint_response_406 import GetServicesFreeRADIUSLDAPEndpointResponse406
from ...models.get_services_free_radiusldap_endpoint_response_409 import GetServicesFreeRADIUSLDAPEndpointResponse409
from ...models.get_services_free_radiusldap_endpoint_response_415 import GetServicesFreeRADIUSLDAPEndpointResponse415
from ...models.get_services_free_radiusldap_endpoint_response_422 import GetServicesFreeRADIUSLDAPEndpointResponse422
from ...models.get_services_free_radiusldap_endpoint_response_424 import GetServicesFreeRADIUSLDAPEndpointResponse424
from ...models.get_services_free_radiusldap_endpoint_response_500 import GetServicesFreeRADIUSLDAPEndpointResponse500
from ...models.get_services_free_radiusldap_endpoint_response_503 import GetServicesFreeRADIUSLDAPEndpointResponse503
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/services/freeradius/ldap",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetServicesFreeRADIUSLDAPEndpointResponse400
    | GetServicesFreeRADIUSLDAPEndpointResponse401
    | GetServicesFreeRADIUSLDAPEndpointResponse403
    | GetServicesFreeRADIUSLDAPEndpointResponse404
    | GetServicesFreeRADIUSLDAPEndpointResponse405
    | GetServicesFreeRADIUSLDAPEndpointResponse406
    | GetServicesFreeRADIUSLDAPEndpointResponse409
    | GetServicesFreeRADIUSLDAPEndpointResponse415
    | GetServicesFreeRADIUSLDAPEndpointResponse422
    | GetServicesFreeRADIUSLDAPEndpointResponse424
    | GetServicesFreeRADIUSLDAPEndpointResponse500
    | GetServicesFreeRADIUSLDAPEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = GetServicesFreeRADIUSLDAPEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetServicesFreeRADIUSLDAPEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetServicesFreeRADIUSLDAPEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServicesFreeRADIUSLDAPEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = GetServicesFreeRADIUSLDAPEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = GetServicesFreeRADIUSLDAPEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetServicesFreeRADIUSLDAPEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = GetServicesFreeRADIUSLDAPEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = GetServicesFreeRADIUSLDAPEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = GetServicesFreeRADIUSLDAPEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = GetServicesFreeRADIUSLDAPEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetServicesFreeRADIUSLDAPEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetServicesFreeRADIUSLDAPEndpointResponse400
    | GetServicesFreeRADIUSLDAPEndpointResponse401
    | GetServicesFreeRADIUSLDAPEndpointResponse403
    | GetServicesFreeRADIUSLDAPEndpointResponse404
    | GetServicesFreeRADIUSLDAPEndpointResponse405
    | GetServicesFreeRADIUSLDAPEndpointResponse406
    | GetServicesFreeRADIUSLDAPEndpointResponse409
    | GetServicesFreeRADIUSLDAPEndpointResponse415
    | GetServicesFreeRADIUSLDAPEndpointResponse422
    | GetServicesFreeRADIUSLDAPEndpointResponse424
    | GetServicesFreeRADIUSLDAPEndpointResponse500
    | GetServicesFreeRADIUSLDAPEndpointResponse503
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
) -> Response[
    GetServicesFreeRADIUSLDAPEndpointResponse400
    | GetServicesFreeRADIUSLDAPEndpointResponse401
    | GetServicesFreeRADIUSLDAPEndpointResponse403
    | GetServicesFreeRADIUSLDAPEndpointResponse404
    | GetServicesFreeRADIUSLDAPEndpointResponse405
    | GetServicesFreeRADIUSLDAPEndpointResponse406
    | GetServicesFreeRADIUSLDAPEndpointResponse409
    | GetServicesFreeRADIUSLDAPEndpointResponse415
    | GetServicesFreeRADIUSLDAPEndpointResponse422
    | GetServicesFreeRADIUSLDAPEndpointResponse424
    | GetServicesFreeRADIUSLDAPEndpointResponse500
    | GetServicesFreeRADIUSLDAPEndpointResponse503
]:
    """<h3>Description:</h3>Reads current FreeRADIUS LDAP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSLDAP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-ldap-get ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesFreeRADIUSLDAPEndpointResponse400 | GetServicesFreeRADIUSLDAPEndpointResponse401 | GetServicesFreeRADIUSLDAPEndpointResponse403 | GetServicesFreeRADIUSLDAPEndpointResponse404 | GetServicesFreeRADIUSLDAPEndpointResponse405 | GetServicesFreeRADIUSLDAPEndpointResponse406 | GetServicesFreeRADIUSLDAPEndpointResponse409 | GetServicesFreeRADIUSLDAPEndpointResponse415 | GetServicesFreeRADIUSLDAPEndpointResponse422 | GetServicesFreeRADIUSLDAPEndpointResponse424 | GetServicesFreeRADIUSLDAPEndpointResponse500 | GetServicesFreeRADIUSLDAPEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesFreeRADIUSLDAPEndpointResponse400
    | GetServicesFreeRADIUSLDAPEndpointResponse401
    | GetServicesFreeRADIUSLDAPEndpointResponse403
    | GetServicesFreeRADIUSLDAPEndpointResponse404
    | GetServicesFreeRADIUSLDAPEndpointResponse405
    | GetServicesFreeRADIUSLDAPEndpointResponse406
    | GetServicesFreeRADIUSLDAPEndpointResponse409
    | GetServicesFreeRADIUSLDAPEndpointResponse415
    | GetServicesFreeRADIUSLDAPEndpointResponse422
    | GetServicesFreeRADIUSLDAPEndpointResponse424
    | GetServicesFreeRADIUSLDAPEndpointResponse500
    | GetServicesFreeRADIUSLDAPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current FreeRADIUS LDAP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSLDAP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-ldap-get ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesFreeRADIUSLDAPEndpointResponse400 | GetServicesFreeRADIUSLDAPEndpointResponse401 | GetServicesFreeRADIUSLDAPEndpointResponse403 | GetServicesFreeRADIUSLDAPEndpointResponse404 | GetServicesFreeRADIUSLDAPEndpointResponse405 | GetServicesFreeRADIUSLDAPEndpointResponse406 | GetServicesFreeRADIUSLDAPEndpointResponse409 | GetServicesFreeRADIUSLDAPEndpointResponse415 | GetServicesFreeRADIUSLDAPEndpointResponse422 | GetServicesFreeRADIUSLDAPEndpointResponse424 | GetServicesFreeRADIUSLDAPEndpointResponse500 | GetServicesFreeRADIUSLDAPEndpointResponse503
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetServicesFreeRADIUSLDAPEndpointResponse400
    | GetServicesFreeRADIUSLDAPEndpointResponse401
    | GetServicesFreeRADIUSLDAPEndpointResponse403
    | GetServicesFreeRADIUSLDAPEndpointResponse404
    | GetServicesFreeRADIUSLDAPEndpointResponse405
    | GetServicesFreeRADIUSLDAPEndpointResponse406
    | GetServicesFreeRADIUSLDAPEndpointResponse409
    | GetServicesFreeRADIUSLDAPEndpointResponse415
    | GetServicesFreeRADIUSLDAPEndpointResponse422
    | GetServicesFreeRADIUSLDAPEndpointResponse424
    | GetServicesFreeRADIUSLDAPEndpointResponse500
    | GetServicesFreeRADIUSLDAPEndpointResponse503
]:
    """<h3>Description:</h3>Reads current FreeRADIUS LDAP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSLDAP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-ldap-get ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServicesFreeRADIUSLDAPEndpointResponse400 | GetServicesFreeRADIUSLDAPEndpointResponse401 | GetServicesFreeRADIUSLDAPEndpointResponse403 | GetServicesFreeRADIUSLDAPEndpointResponse404 | GetServicesFreeRADIUSLDAPEndpointResponse405 | GetServicesFreeRADIUSLDAPEndpointResponse406 | GetServicesFreeRADIUSLDAPEndpointResponse409 | GetServicesFreeRADIUSLDAPEndpointResponse415 | GetServicesFreeRADIUSLDAPEndpointResponse422 | GetServicesFreeRADIUSLDAPEndpointResponse424 | GetServicesFreeRADIUSLDAPEndpointResponse500 | GetServicesFreeRADIUSLDAPEndpointResponse503]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetServicesFreeRADIUSLDAPEndpointResponse400
    | GetServicesFreeRADIUSLDAPEndpointResponse401
    | GetServicesFreeRADIUSLDAPEndpointResponse403
    | GetServicesFreeRADIUSLDAPEndpointResponse404
    | GetServicesFreeRADIUSLDAPEndpointResponse405
    | GetServicesFreeRADIUSLDAPEndpointResponse406
    | GetServicesFreeRADIUSLDAPEndpointResponse409
    | GetServicesFreeRADIUSLDAPEndpointResponse415
    | GetServicesFreeRADIUSLDAPEndpointResponse422
    | GetServicesFreeRADIUSLDAPEndpointResponse424
    | GetServicesFreeRADIUSLDAPEndpointResponse500
    | GetServicesFreeRADIUSLDAPEndpointResponse503
    | None
):
    """<h3>Description:</h3>Reads current FreeRADIUS LDAP.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: FreeRADIUSLDAP<br>**Parent model**: None<br>**Requires
    authentication**: Yes<br>**Supported authentication modes:** [ BasicAuth, JWTAuth, KeyAuth
    ]<br>**Allowed privileges**: [ page-all, api-v2-services-freeradius-ldap-get ]<br>**Required
    packages**: [ pfSense-pkg-freeradius3 ]<br>**Applies immediately**: Yes<br>**Utilizes cache**: None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServicesFreeRADIUSLDAPEndpointResponse400 | GetServicesFreeRADIUSLDAPEndpointResponse401 | GetServicesFreeRADIUSLDAPEndpointResponse403 | GetServicesFreeRADIUSLDAPEndpointResponse404 | GetServicesFreeRADIUSLDAPEndpointResponse405 | GetServicesFreeRADIUSLDAPEndpointResponse406 | GetServicesFreeRADIUSLDAPEndpointResponse409 | GetServicesFreeRADIUSLDAPEndpointResponse415 | GetServicesFreeRADIUSLDAPEndpointResponse422 | GetServicesFreeRADIUSLDAPEndpointResponse424 | GetServicesFreeRADIUSLDAPEndpointResponse500 | GetServicesFreeRADIUSLDAPEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
