from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_data_body import (
    PostServicesHAProxySettingsEmailMailerEndpointDataBody,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_json_body import (
    PostServicesHAProxySettingsEmailMailerEndpointJsonBody,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_400 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse400,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_401 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse401,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_403 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse403,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_404 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse404,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_405 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse405,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_406 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse406,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_409 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse409,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_415 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse415,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_422 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse422,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_424 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse424,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_500 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse500,
)
from ...models.post_services_ha_proxy_settings_email_mailer_endpoint_response_503 import (
    PostServicesHAProxySettingsEmailMailerEndpointResponse503,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostServicesHAProxySettingsEmailMailerEndpointJsonBody
    | PostServicesHAProxySettingsEmailMailerEndpointDataBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/services/haproxy/settings/email_mailer",
    }

    if isinstance(body, PostServicesHAProxySettingsEmailMailerEndpointJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostServicesHAProxySettingsEmailMailerEndpointDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostServicesHAProxySettingsEmailMailerEndpointResponse400
    | PostServicesHAProxySettingsEmailMailerEndpointResponse401
    | PostServicesHAProxySettingsEmailMailerEndpointResponse403
    | PostServicesHAProxySettingsEmailMailerEndpointResponse404
    | PostServicesHAProxySettingsEmailMailerEndpointResponse405
    | PostServicesHAProxySettingsEmailMailerEndpointResponse406
    | PostServicesHAProxySettingsEmailMailerEndpointResponse409
    | PostServicesHAProxySettingsEmailMailerEndpointResponse415
    | PostServicesHAProxySettingsEmailMailerEndpointResponse422
    | PostServicesHAProxySettingsEmailMailerEndpointResponse424
    | PostServicesHAProxySettingsEmailMailerEndpointResponse500
    | PostServicesHAProxySettingsEmailMailerEndpointResponse503
    | None
):
    if response.status_code == 400:
        response_400 = PostServicesHAProxySettingsEmailMailerEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostServicesHAProxySettingsEmailMailerEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostServicesHAProxySettingsEmailMailerEndpointResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostServicesHAProxySettingsEmailMailerEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = PostServicesHAProxySettingsEmailMailerEndpointResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = PostServicesHAProxySettingsEmailMailerEndpointResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostServicesHAProxySettingsEmailMailerEndpointResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 415:
        response_415 = PostServicesHAProxySettingsEmailMailerEndpointResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = PostServicesHAProxySettingsEmailMailerEndpointResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 424:
        response_424 = PostServicesHAProxySettingsEmailMailerEndpointResponse424.from_dict(response.json())

        return response_424

    if response.status_code == 500:
        response_500 = PostServicesHAProxySettingsEmailMailerEndpointResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostServicesHAProxySettingsEmailMailerEndpointResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostServicesHAProxySettingsEmailMailerEndpointResponse400
    | PostServicesHAProxySettingsEmailMailerEndpointResponse401
    | PostServicesHAProxySettingsEmailMailerEndpointResponse403
    | PostServicesHAProxySettingsEmailMailerEndpointResponse404
    | PostServicesHAProxySettingsEmailMailerEndpointResponse405
    | PostServicesHAProxySettingsEmailMailerEndpointResponse406
    | PostServicesHAProxySettingsEmailMailerEndpointResponse409
    | PostServicesHAProxySettingsEmailMailerEndpointResponse415
    | PostServicesHAProxySettingsEmailMailerEndpointResponse422
    | PostServicesHAProxySettingsEmailMailerEndpointResponse424
    | PostServicesHAProxySettingsEmailMailerEndpointResponse500
    | PostServicesHAProxySettingsEmailMailerEndpointResponse503
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
    body: PostServicesHAProxySettingsEmailMailerEndpointJsonBody
    | PostServicesHAProxySettingsEmailMailerEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxySettingsEmailMailerEndpointResponse400
    | PostServicesHAProxySettingsEmailMailerEndpointResponse401
    | PostServicesHAProxySettingsEmailMailerEndpointResponse403
    | PostServicesHAProxySettingsEmailMailerEndpointResponse404
    | PostServicesHAProxySettingsEmailMailerEndpointResponse405
    | PostServicesHAProxySettingsEmailMailerEndpointResponse406
    | PostServicesHAProxySettingsEmailMailerEndpointResponse409
    | PostServicesHAProxySettingsEmailMailerEndpointResponse415
    | PostServicesHAProxySettingsEmailMailerEndpointResponse422
    | PostServicesHAProxySettingsEmailMailerEndpointResponse424
    | PostServicesHAProxySettingsEmailMailerEndpointResponse500
    | PostServicesHAProxySettingsEmailMailerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Email Mailer.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyEmailMailer<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-email-mailer-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxySettingsEmailMailerEndpointJsonBody | Unset):
        body (PostServicesHAProxySettingsEmailMailerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxySettingsEmailMailerEndpointResponse400 | PostServicesHAProxySettingsEmailMailerEndpointResponse401 | PostServicesHAProxySettingsEmailMailerEndpointResponse403 | PostServicesHAProxySettingsEmailMailerEndpointResponse404 | PostServicesHAProxySettingsEmailMailerEndpointResponse405 | PostServicesHAProxySettingsEmailMailerEndpointResponse406 | PostServicesHAProxySettingsEmailMailerEndpointResponse409 | PostServicesHAProxySettingsEmailMailerEndpointResponse415 | PostServicesHAProxySettingsEmailMailerEndpointResponse422 | PostServicesHAProxySettingsEmailMailerEndpointResponse424 | PostServicesHAProxySettingsEmailMailerEndpointResponse500 | PostServicesHAProxySettingsEmailMailerEndpointResponse503]
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
    body: PostServicesHAProxySettingsEmailMailerEndpointJsonBody
    | PostServicesHAProxySettingsEmailMailerEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxySettingsEmailMailerEndpointResponse400
    | PostServicesHAProxySettingsEmailMailerEndpointResponse401
    | PostServicesHAProxySettingsEmailMailerEndpointResponse403
    | PostServicesHAProxySettingsEmailMailerEndpointResponse404
    | PostServicesHAProxySettingsEmailMailerEndpointResponse405
    | PostServicesHAProxySettingsEmailMailerEndpointResponse406
    | PostServicesHAProxySettingsEmailMailerEndpointResponse409
    | PostServicesHAProxySettingsEmailMailerEndpointResponse415
    | PostServicesHAProxySettingsEmailMailerEndpointResponse422
    | PostServicesHAProxySettingsEmailMailerEndpointResponse424
    | PostServicesHAProxySettingsEmailMailerEndpointResponse500
    | PostServicesHAProxySettingsEmailMailerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Email Mailer.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyEmailMailer<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-email-mailer-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxySettingsEmailMailerEndpointJsonBody | Unset):
        body (PostServicesHAProxySettingsEmailMailerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxySettingsEmailMailerEndpointResponse400 | PostServicesHAProxySettingsEmailMailerEndpointResponse401 | PostServicesHAProxySettingsEmailMailerEndpointResponse403 | PostServicesHAProxySettingsEmailMailerEndpointResponse404 | PostServicesHAProxySettingsEmailMailerEndpointResponse405 | PostServicesHAProxySettingsEmailMailerEndpointResponse406 | PostServicesHAProxySettingsEmailMailerEndpointResponse409 | PostServicesHAProxySettingsEmailMailerEndpointResponse415 | PostServicesHAProxySettingsEmailMailerEndpointResponse422 | PostServicesHAProxySettingsEmailMailerEndpointResponse424 | PostServicesHAProxySettingsEmailMailerEndpointResponse500 | PostServicesHAProxySettingsEmailMailerEndpointResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxySettingsEmailMailerEndpointJsonBody
    | PostServicesHAProxySettingsEmailMailerEndpointDataBody
    | Unset = UNSET,
) -> Response[
    PostServicesHAProxySettingsEmailMailerEndpointResponse400
    | PostServicesHAProxySettingsEmailMailerEndpointResponse401
    | PostServicesHAProxySettingsEmailMailerEndpointResponse403
    | PostServicesHAProxySettingsEmailMailerEndpointResponse404
    | PostServicesHAProxySettingsEmailMailerEndpointResponse405
    | PostServicesHAProxySettingsEmailMailerEndpointResponse406
    | PostServicesHAProxySettingsEmailMailerEndpointResponse409
    | PostServicesHAProxySettingsEmailMailerEndpointResponse415
    | PostServicesHAProxySettingsEmailMailerEndpointResponse422
    | PostServicesHAProxySettingsEmailMailerEndpointResponse424
    | PostServicesHAProxySettingsEmailMailerEndpointResponse500
    | PostServicesHAProxySettingsEmailMailerEndpointResponse503
]:
    """<h3>Description:</h3>Creates a new HAProxy Email Mailer.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyEmailMailer<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-email-mailer-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxySettingsEmailMailerEndpointJsonBody | Unset):
        body (PostServicesHAProxySettingsEmailMailerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServicesHAProxySettingsEmailMailerEndpointResponse400 | PostServicesHAProxySettingsEmailMailerEndpointResponse401 | PostServicesHAProxySettingsEmailMailerEndpointResponse403 | PostServicesHAProxySettingsEmailMailerEndpointResponse404 | PostServicesHAProxySettingsEmailMailerEndpointResponse405 | PostServicesHAProxySettingsEmailMailerEndpointResponse406 | PostServicesHAProxySettingsEmailMailerEndpointResponse409 | PostServicesHAProxySettingsEmailMailerEndpointResponse415 | PostServicesHAProxySettingsEmailMailerEndpointResponse422 | PostServicesHAProxySettingsEmailMailerEndpointResponse424 | PostServicesHAProxySettingsEmailMailerEndpointResponse500 | PostServicesHAProxySettingsEmailMailerEndpointResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostServicesHAProxySettingsEmailMailerEndpointJsonBody
    | PostServicesHAProxySettingsEmailMailerEndpointDataBody
    | Unset = UNSET,
) -> (
    PostServicesHAProxySettingsEmailMailerEndpointResponse400
    | PostServicesHAProxySettingsEmailMailerEndpointResponse401
    | PostServicesHAProxySettingsEmailMailerEndpointResponse403
    | PostServicesHAProxySettingsEmailMailerEndpointResponse404
    | PostServicesHAProxySettingsEmailMailerEndpointResponse405
    | PostServicesHAProxySettingsEmailMailerEndpointResponse406
    | PostServicesHAProxySettingsEmailMailerEndpointResponse409
    | PostServicesHAProxySettingsEmailMailerEndpointResponse415
    | PostServicesHAProxySettingsEmailMailerEndpointResponse422
    | PostServicesHAProxySettingsEmailMailerEndpointResponse424
    | PostServicesHAProxySettingsEmailMailerEndpointResponse500
    | PostServicesHAProxySettingsEmailMailerEndpointResponse503
    | None
):
    """<h3>Description:</h3>Creates a new HAProxy Email Mailer.<br><h3>Details:</h3>**Endpoint type**:
    Singular<br>**Associated model**: HAProxyEmailMailer<br>**Parent model**:
    HAProxySettings<br>**Requires authentication**: Yes<br>**Supported authentication modes:** [
    BasicAuth, JWTAuth, KeyAuth ]<br>**Allowed privileges**: [ page-all, api-v2-services-haproxy-
    settings-email-mailer-post ]<br>**Required packages**: [ pfSense-pkg-haproxy ]<br>**Applies
    immediately**: No<br>**Utilizes cache**: None

    Args:
        body (PostServicesHAProxySettingsEmailMailerEndpointJsonBody | Unset):
        body (PostServicesHAProxySettingsEmailMailerEndpointDataBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServicesHAProxySettingsEmailMailerEndpointResponse400 | PostServicesHAProxySettingsEmailMailerEndpointResponse401 | PostServicesHAProxySettingsEmailMailerEndpointResponse403 | PostServicesHAProxySettingsEmailMailerEndpointResponse404 | PostServicesHAProxySettingsEmailMailerEndpointResponse405 | PostServicesHAProxySettingsEmailMailerEndpointResponse406 | PostServicesHAProxySettingsEmailMailerEndpointResponse409 | PostServicesHAProxySettingsEmailMailerEndpointResponse415 | PostServicesHAProxySettingsEmailMailerEndpointResponse422 | PostServicesHAProxySettingsEmailMailerEndpointResponse424 | PostServicesHAProxySettingsEmailMailerEndpointResponse500 | PostServicesHAProxySettingsEmailMailerEndpointResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
