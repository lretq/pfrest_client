from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_certificate_domain_nsupdate_keyalgo import ACMECertificateDomainNsupdateKeyalgo
from ..models.acme_certificate_domain_nw_api_endpoint import ACMECertificateDomainNwApiEndpoint
from ..models.acme_certificate_domain_ovh_end_point import ACMECertificateDomainOvhEndPoint
from ..models.acme_certificate_domain_status import ACMECertificateDomainStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ACMECertificateDomain")


@_attrs_define
class ACMECertificateDomain:
    """
    Attributes:
        name (str | Unset): The fully-qualified domain name of this domain (SAN).<br>
        status (ACMECertificateDomainStatus | Unset): The activation status of the ACME certificate.<br> Default:
            ACMECertificateDomainStatus.ENABLE.
        method (str | Unset): The method to use to validate this domain.<br>
        webrootfolder (str | Unset): Folder into which the acme challenge response is written; for example:
            /usr/local/www/.well-known/acme-challenge/<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'webroot'`<br>
        webrootftpftpserver (str | Unset): Hostname of FTP server to which ACME will connect (e.g.
            ftps://www.webserver.tld ). Currently supports FTPS (passive) and SFTP.<br><br>This field is only available when
            the following conditions are met:<br>- `method` must be equal to `'webrootftp'`<br>
        webrootftpusername (str | Unset): Username for the remote server<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'webrootftp'`<br>
        webrootftppassword (str | Unset): Password to authenticate this user on the remote server<br><br>This field is
            only available when the following conditions are met:<br>- `method` must be equal to `'webrootftp'`<br>
        webrootftpfolder (str | Unset): Folder into which the acme challenge response is written (e.g. /.well-
            known/acme-challenge/)<br><br>This field is only available when the following conditions are met:<br>- `method`
            must be equal to `'webrootftp'`<br>
        standaloneport (str | Unset): HTTP listen port for stand-alone server. Must be 80 or have port 80 on WAN
            forwarded to this port. Firewall rules must allow traffic to reach this port.<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'standalone'`<br>
        standaloneipv6 (bool | Unset): Bind to IPv6 instead of IPv4.<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'standalone'`<br>
        standalonetlsport (str | Unset): TLS listen port for stand-alone server. Must be 443 or have port 443 on WAN
            forwarded to this port. Firewall rules must allow traffic to reach this port.<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'standalonetls'`<br>
        nsupdate_server (str | Unset): The DNS server to which updates are sent (IP address or hostname)<br><br>This
            field is only available when the following conditions are met:<br>- `method` must be equal to
            `'dns_nsupdate'`<br>
        nsupdate_keyname (str | Unset): (Optional) A name for the key, if it is different than _acme-
            challenge.[DomainName]<br><br>This field is only available when the following conditions are met:<br>- `method`
            must be equal to `'dns_nsupdate'`<br>
        nsupdate_keyalgo (ACMECertificateDomainNsupdateKeyalgo | Unset): Algorithm used to generate the authentication
            Key for this zone<br><br>This field is only available when the following conditions are met:<br>- `method` must
            be equal to `'dns_nsupdate'`<br>
        nsupdate_key (str | Unset): The key which authenticates updates for this zone<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_nsupdate'`<br>
        nsupdate_zone (str | Unset): (Optional) Explicitly set the zone name for updates.<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_nsupdate'`<br>
        one984hosting_username (str | Unset): 1984Hosting Username<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_1984hosting'`<br>
        one984hosting_password (str | Unset): 1984Hosting Password<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_1984hosting'`<br>
        acmeproxy_endpoint (str | Unset): Acmeproxy Endpoint URL (https://ip:port)<br><br>This field is only available
            when the following conditions are met:<br>- `method` must be equal to `'dns_acmeproxy'`<br>
        acmeproxy_username (str | Unset): Acmeproxy Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_acmeproxy'`<br>
        acmeproxy_password (str | Unset): Acmeproxy Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_acmeproxy'`<br>
        acmedns_username (str | Unset): acme-dns.io Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_acmedns'`<br>
        acmedns_password (str | Unset): acme-dns.io Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_acmedns'`<br>
        acmedns_subdomain (str | Unset): acme-dns.io subdomain<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_acmedns'`<br>
        acmedns_update_url (str | Unset): (optional) Custom ACME DNS Base URL<br><br>This field is only available when
            the following conditions are met:<br>- `method` must be equal to `'dns_acmedns'`<br>
        active24_token (str | Unset): Active24 Token<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_active24'`<br>
        akamai_host (str | Unset): Hostname<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_edgedns'`<br>
        akamai_access_token (str | Unset): Access Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_edgedns'`<br>
        akamai_client_token (str | Unset): Client Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_edgedns'`<br>
        akamai_client_secret (str | Unset): Client Secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_edgedns'`<br>
        ali_key (str | Unset): API Key<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_ali'`<br>
        ali_secret (str | Unset): API Secret<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_ali'`<br>
        kas_login (str | Unset): Login<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_kas'`<br>
        kas_authtype (str | Unset): Auth type (default: sha1)<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_kas'`<br>
        kas_authdata (str | Unset): Auth data<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_kas'`<br>
        ad_api_key (str | Unset): Alwaysdata API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_ad'`<br>
        anx_token (str | Unset): API Token<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_anx'`<br>
        af_api_username (str | Unset): ArtFiles Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_artfiles'`<br>
        af_api_password (str | Unset): ArtFiles Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_artfiles'`<br>
        arvan_token (str | Unset): Arvan API Token<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_arvan'`<br>
        aurora_key (str | Unset): API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_aurora'`<br>
        aurora_secret (str | Unset): API Secret. Obtain the key and secret from
            https://cp.pcextreme.nl/auroradns/users.<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_aurora'`<br>
        autodns_user (str | Unset): autoDNS Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_autodns'`<br>
        autodns_password (str | Unset): autoDNS Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_autodns'`<br>
        autodns_context (str | Unset): autoDNS Context<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_autodns'`<br>
        aws_access_key_id (str | Unset): AWS Access Key / API ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_aws'`<br>
        aws_secret_access_key (str | Unset): AWS Secret Access / API Key<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_aws'`<br>
        aws_dns_slowrate (str | Unset): Sleep interval after TXT record update, in seconds (default: 1)<br><br>This
            field is only available when the following conditions are met:<br>- `method` must be equal to `'dns_aws'`<br>
        azion_email (str | Unset): Account e-mail address<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_azion'`<br>
        azion_password (str | Unset): Account password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_azion'`<br>
        azuredns_subscriptionid (str | Unset): Azure Subscription ID. First, <a href="https://github.com/acmesh-
            official/acme.sh/wiki/How-to-use-Azure-DNS">setup a service principal for access to the DNS
            Zone</a>.<br><br>This field is only available when the following conditions are met:<br>- `method` must be equal
            to `'dns_azure'`<br>
        azuredns_tenantid (str | Unset): Azure Tenant ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_azure'`<br>
        azuredns_appid (str | Unset): Azure App ID<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_azure'`<br>
        azuredns_clientsecret (str | Unset): Azure Client Secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_azure'`<br>
        bookmyname_username (str | Unset): BookMyName Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_bookmyname'`<br>
        bookmyname_password (str | Unset): BookMyName Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_bookmyname'`<br>
        bunny_api_key (str | Unset): Bunny DNS API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_bunny'`<br>
        clouddns_email (str | Unset): CloudDNS e-mail address<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_clouddns'`<br>
        clouddns_client_id (str | Unset): CloudDNS client ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_clouddns'`<br>
        clouddns_password (str | Unset): CloudDNS Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_clouddns'`<br>
        cloudns_auth_id (str | Unset): Authentication ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cloudns'`<br>
        cloudns_sub_auth_id (str | Unset): Sub authentication ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cloudns'`<br>
        cloudns_auth_password (str | Unset): ClouDNS Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cloudns'`<br>
        cf_key (str | Unset): Cloudflare API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_cf'`<br>
        cf_email (str | Unset): Cloudflare API Email Address<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cf'`<br>
        cf_token (str | Unset): Cloudflare API Token<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_cf'`<br>
        cf_account_id (str | Unset): Cloudflare API Account ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cf'`<br>
        cf_zone_id (str | Unset): Cloudflare API Zone ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cf'`<br>
        conoha_username (str | Unset): Conoha Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_conoha'`<br>
        conoha_password (str | Unset): Conoha Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_conoha'`<br>
        conoha_tenantid (str | Unset): Conoha Tenant ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_conoha'`<br>
        conoha_identityserviceapi (str | Unset): Conoha Identity Service API<br><br>This field is only available when
            the following conditions are met:<br>- `method` must be equal to `'dns_conoha'`<br>
        constellix_key (str | Unset): Constellix Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_constellix'`<br>
        constellix_secret (str | Unset): Constellix Secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_constellix'`<br>
        cpanel_username (str | Unset): cPanel username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_cpanel'`<br>
        cpanel_apitoken (str | Unset): cPanel API token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cpanel'`<br>
        cpanel_hostname (str | Unset): URL to cPanel instance<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cpanel'`<br>
        cn_user (str | Unset): Core Networks Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_cn'`<br>
        cn_password (str | Unset): Core Networks Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_cn'`<br>
        curanet_authclientid (str | Unset): Authentication Client ID<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_curanet'`<br>
        curanet_authsecret (str | Unset): Authentication Secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_curanet'`<br>
        cy_username (str | Unset): CY username<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_cyon'`<br>
        cy_password (str | Unset): CY Password<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_cyon'`<br>
        ddnss_token (str | Unset): API Token (e.g. aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee)<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_ddnss'`<br>
        dedyn_token (str | Unset): deSEC.io API Token<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_desec'`<br>
        dedyn_name (str | Unset): deSEC.io Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_desec'`<br>
        do_api_key (str | Unset): DigitalOcean API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_dgon'`<br>
        da_api (str | Unset): DirectAdmin API URI (e.g.
            https://remoteUser:remotePassword@da.example.com:8443)<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_da'`<br>
        da_api_insecure (str | Unset): DirectAdmin API Security check, 0=check for valid SSL certificate, 1=always
            accept<br><br>This field is only available when the following conditions are met:<br>- `method` must be equal to
            `'dns_da'`<br>
        dnsexit_api_key (str | Unset): DNSExit API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_dnsexit'`<br>
        dnsexit_auth_user (str | Unset): DNSExit Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_dnsexit'`<br>
        dnsexit_auth_pass (str | Unset): DNSExit Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_dnsexit'`<br>
        dnshome_subdomain (str | Unset): Subdomain<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_dnshome'`<br>
        dnshome_subdomainpassword (str | Unset): Subdomain Password<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_dnshome'`<br>
        dnsimple_oauth_token (str | Unset): DNSimple oauth token, visit <a
            href="https://dnsimple.com/user">https://dnsimple.com/user</a> to generate.<br><br>This field is only available
            when the following conditions are met:<br>- `method` must be equal to `'dns_dnsimple'`<br>
        me_key (str | Unset): DNSMadeEasy API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_me'`<br>
        me_secret (str | Unset): DNSMadeEasy API Secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_me'`<br>
        dnsservices_username (str | Unset): dns.services Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_dnsservices'`<br>
        dnsservices_password (str | Unset): dns.services Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_dnsservices'`<br>
        do_letoken (str | Unset): DO.de API Token<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_doapi'`<br>
        do_pid (str | Unset): DO Customer ID<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_do'`<br>
        do_pw (str | Unset): DO Password<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_do'`<br>
        domeneshop_token (str | Unset): Domeneshop API Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_domeneshop'`<br>
        domeneshop_secret (str | Unset): Domeneshop API Secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_domeneshop'`<br>
        dp_id (str | Unset): Dnspod API ID<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_dp'`<br>
        dp_key (str | Unset): Dnspod API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_dp'`<br>
        dpi_id (str | Unset): Dnspod API ID<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_dpi'`<br>
        dpi_key (str | Unset): Dnspod API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_dpi'`<br>
        dh_api_key (str | Unset): Dreamhost API Token<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_dreamhost'`<br>
        duckdns_token (str | Unset): DuckDNS API Token (Look in DuckDNS account settings)<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_duckdns'`<br>
        dd_api_user (str | Unset): DurableDNS API User<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_durabledns'`<br>
        dd_api_key (str | Unset): DurableDNS API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_durabledns'`<br>
        dyn_customer (str | Unset): dyn.com customer ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_dyn'`<br>
        dyn_username (str | Unset): dyn.com API Username (Dyn Managed DNS user, Needs Z&R Permissions for RecordAdd,
            RecordUpdate, RecordDelete, RecordGet, ZoneGet, ZoneAddNode, ZoneRemoveNode, ZonePublish)<br><br>This field is
            only available when the following conditions are met:<br>- `method` must be equal to `'dns_dyn'`<br>
        dyn_password (str | Unset): dyn.com Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_dyn'`<br>
        df_user (str | Unset): dyndnsfree.de Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_df'`<br>
        df_password (str | Unset): dyndnsfree.de Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_df'`<br>
        dynu_clientid (str | Unset): Dynu API Client ID created in the Dynu account settings<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_dynu'`<br>
        dynu_secret (str | Unset): Dynu API Secret<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_dynu'`<br>
        easydns_key (str | Unset): easyDNS API Key. Sign up for a key at
            https://cp.easydns.com/manage/security/api/signup.php<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_easydns'`<br>
        easydns_token (str | Unset): easyDNS API Token<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_easydns'`<br>
        euserv_username (str | Unset): Euserv.eu Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_euserv'`<br>
        euserv_password (str | Unset): Euserv.eu Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_euserv'`<br>
        exoscale_api_key (str | Unset): Exoscale API Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_exoscale'`<br>
        exoscale_secret_key (str | Unset): Exoscale Secret Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_exoscale'`<br>
        fornex_api_key (str | Unset): Fornex API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_fornex'`<br>
        freedns_user (str | Unset): FreeDNS username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_freedns'`<br>
        freedns_password (str | Unset): FreeDNS Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_freedns'`<br>
        gandi_livedns_key (str | Unset): Gandi LiveDNS API Key, retrieved from <a
            href="https://account.gandi.net">https://account.gandi.net</a><br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_gandi_livedns'`<br>
        gcore_key (str | Unset): Gcore API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_gcore'`<br>
        geoscaling_username (str | Unset): Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_geoscaling'`<br>
        geoscaling_password (str | Unset): Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_geoscaling'`<br>
        gd_key (str | Unset): GoDaddy API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_gd'`<br>
        gd_secret (str | Unset): GoDaddy API Secret<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_gd'`<br>
        googledomains_access_token (str | Unset): Google Domains API Access Token<br><br>This field is only available
            when the following conditions are met:<br>- `method` must be equal to `'dns_googledomains'`<br>
        googledomains_zone (str | Unset): Google Domains DNS Zone<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_googledomains'`<br>
        hetzner_token (str | Unset): Hetzner API Token. Visit https://dns.hetzner.com/settings/api-token to
            retrieve.<br><br>This field is only available when the following conditions are met:<br>- `method` must be equal
            to `'dns_hetzner'`<br>
        hexonet_login (str | Unset): Hexonet Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_hexonet'`<br>
        hexonet_password (str | Unset): Hexonet Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_hexonet'`<br>
        huaweicloud_username (str | Unset): Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_huaweicloud'`<br>
        huaweicloud_password (str | Unset): Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_huaweicloud'`<br>
        huaweicloud_domainname (str | Unset): Domain Name<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_huaweicloud'`<br>
        he_username (str | Unset): Hurricane Electric username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_he'`<br>
        he_password (str | Unset): Hurricane Electric password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_he'`<br>
        hostingde_apikey (str | Unset): Hosting.de API Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_hostingde'`<br>
        hostingde_endpoint (str | Unset): Hosting.de API endpoint, e.g. https://secure.hosting.de<br><br>This field is
            only available when the following conditions are met:<br>- `method` must be equal to `'dns_hostingde'`<br>
        infoblox_creds (str | Unset): Infoblox credentials in <strong>username:password</strong> format<br><br>This
            field is only available when the following conditions are met:<br>- `method` must be equal to
            `'dns_infoblox'`<br>
        infoblox_server (str | Unset): Infoblox server IP address or hostname<br><br>This field is only available when
            the following conditions are met:<br>- `method` must be equal to `'dns_infoblox'`<br>
        infoblox_view (str | Unset): Infoblox DNS View name, or enter "default"<br><br>This field is only available when
            the following conditions are met:<br>- `method` must be equal to `'dns_infoblox'`<br>
        infomaniak_api_token (str | Unset): Infomaniak API token. Visit
            https://manager.infomaniak.com/v3/&lt;account_id&gt;/api/dashboard and generate a token with the scope
            Domain.<br><br>This field is only available when the following conditions are met:<br>- `method` must be equal
            to `'dns_infomaniak'`<br>
        default_infomaniak_api_url (str | Unset): Infomaniak API URL (Default: https://api.infomaniak.com)<br><br>This
            field is only available when the following conditions are met:<br>- `method` must be equal to
            `'dns_infomaniak'`<br>
        infomaniak_ttl (str | Unset): Infomaniak DNS record TTL (Default: 300)<br><br>This field is only available when
            the following conditions are met:<br>- `method` must be equal to `'dns_infomaniak'`<br>
        ionos_prefix (str | Unset): Prefix<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_ionos'`<br>
        ionos_secret (str | Unset): Secret. Read https://beta.developer.hosting.ionos.de/docs/getstarted to learn how to
            get a prefix and secret.<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_ionos'`<br>
        ipv64_token (str | Unset): IPv64.net Access Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_ipv64'`<br>
        internetbs_api_key (str | Unset): Internet.BS API Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_internetbs'`<br>
        internetbs_api_password (str | Unset): Internet.BS API Password<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_internetbs'`<br>
        inwx_username (str | Unset): INWX.de username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_inwx'`<br>
        inwx_password (str | Unset): INWX.de password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_inwx'`<br>
        inwx_shared_secret (str | Unset): INWX.de shared secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_inwx'`<br>
        ispc_user (str | Unset): ISPConfig remoteUser<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_ispconfig'`<br>
        ispc_password (str | Unset): ISPConfig remotePassword<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_ispconfig'`<br>
        ispc_api (str | Unset): API URL (e.g. https://ispc.domain.tld:8080/remote/json.php )<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_ispconfig'`<br>
        ispc_api_insecure (str | Unset): Set 1 for insecure and 0 for secure. Controls whether the server TLS
            certificate is checked for validity (0) or always accepted (1)<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_ispconfig'`<br>
        jd_access_key_id (str | Unset): jdcloud Access Key ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_jd'`<br>
        jd_access_key_secret (str | Unset): jdcloud Access Key Secret<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_jd'`<br>
        jd_region (str | Unset): jdcloud Region<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_jd'`<br>
        joker_username (str | Unset): Joker.com Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_joker'`<br>
        joker_password (str | Unset): Joker.com Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_joker'`<br>
        kappernetdns_key (str | Unset): kapper.net API Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_kappernet'`<br>
        kappernetdns_secret (str | Unset): kapper.net API Secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_kappernet'`<br>
        kinghost_username (str | Unset): Kinghost API Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_kinghost'`<br>
        kinghost_password (str | Unset): Kinghost API Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_kinghost'`<br>
        knot_server (str | Unset): IP address of the Knot server<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_knot'`<br>
        knot_key (str | Unset): Knot TSIG Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_knot'`<br>
        la_id (str | Unset): ID<br><br>This field is only available when the following conditions are met:<br>- `method`
            must be equal to `'dns_la'`<br>
        la_key (str | Unset): Key<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_la'`<br>
        lsw_key (str | Unset): Leaseweb API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_leaseweb'`<br>
        limacity_apikey (str | Unset): API Key must have the following roles: dns.admin, domains.reader<br><br>This
            field is only available when the following conditions are met:<br>- `method` must be equal to
            `'dns_limacity'`<br>
        linode_api_key (str | Unset): Linode API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_linode'`<br>
        linode_v4_api_key (str | Unset): Linode v4 API Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_linode_v4'`<br>
        loopia_user (str | Unset): Loopia username<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_loopia'`<br>
        loopia_password (str | Unset): Loopia Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_loopia'`<br>
        lua_key (str | Unset): Luadns API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_lua'`<br>
        lua_email (str | Unset): Luadns API Email Address<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_lua'`<br>
        miab_username (str | Unset): MailinaBox Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_miab'`<br>
        miab_password (str | Unset): MailinaBox Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_miab'`<br>
        miab_server (str | Unset): MailinaBox Server<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_miab'`<br>
        misaka_key (str | Unset): misaka.io Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_misaka'`<br>
        mydnsjp_masterid (str | Unset): MyDNS.jp Master ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_mydnsjp'`<br>
        mydnsjp_password (str | Unset): MyDNS.jp Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_mydnsjp'`<br>
        mb_ak (str | Unset): OAuth2 Key<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_mythic_beasts'`<br>
        mb_as (str | Unset): OAuth2 Secret<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_mythic_beasts'`<br>
        namecom_username (str | Unset): Name.com username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_namecom'`<br>
        namecom_token (str | Unset): Name.com API Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_namecom'`<br>
        namecheap_api_key (str | Unset): Namecheap API Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_namecheap'`<br>
        namecheap_username (str | Unset): Namecheap Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_namecheap'`<br>
        nm_user (str | Unset): namemaster.de API username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_nm'`<br>
        nm_sha256 (str | Unset): namemaster.de API password as SHA256 hash<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_nm'`<br>
        nanelo_token (str | Unset): Nanelo.com Access Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_nanelo'`<br>
        nederhost_key (str | Unset): NederHost API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_nederhost'`<br>
        namesilo_key (str | Unset): Namesilo API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_namesilo'`<br>
        neodigit_api_token (str | Unset): Neodigit API Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_neodigit'`<br>
        nc_apikey (str | Unset): Netcup API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_netcup'`<br>
        nc_apipw (str | Unset): Netcup API Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_netcup'`<br>
        nc_cid (str | Unset): Netcup Customer ID/Number<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_netcup'`<br>
        netlify_access_token (str | Unset): Netlify API Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_netlify'`<br>
        nic_clientid (str | Unset): nic.ru API Client ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_nic'`<br>
        nic_clientsecret (str | Unset): nic.ru API Client Secret<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_nic'`<br>
        nic_username (str | Unset): nic.ru Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_nic'`<br>
        nic_password (str | Unset): nic.ru Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_nic'`<br>
        ns1_key (str | Unset): NS1 API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_nsone'`<br>
        nw_api_token (str | Unset): NW API Token<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_nw'`<br>
        nw_api_endpoint (ACMECertificateDomainNwApiEndpoint | Unset): Choose the NW API Endpoint<br><br>This field is
            only available when the following conditions are met:<br>- `method` must be equal to `'dns_nw'`<br>
        onecom_user (str | Unset): One.com Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_one'`<br>
        onecom_password (str | Unset): One.com Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_one'`<br>
        online_api_key (str | Unset): Online.net API Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_online'`<br>
        oci_cli_tenancy (str | Unset): OCID of tenancy that contains the target DNS zone<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_oci'`<br>
        oci_cli_user (str | Unset): OCID of user with permission to add/remove records from zones<br><br>This field is
            only available when the following conditions are met:<br>- `method` must be equal to `'dns_oci'`<br>
        oci_cli_region (str | Unset): Tenancy home region<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_oci'`<br>
        oci_cli_key (str | Unset): The private API signing key in PEM format. Using an encrypted private key that needs
            a passphrase is not supported.<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_oci'`<br>
        openprovider_user (str | Unset): OpenProvider Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_openprovider'`<br>
        openprovider_passwordhash (str | Unset): OpenProvider Password Hash<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_openprovider'`<br>
        ovh_ak (str | Unset): OVH Application Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_ovh'`<br>
        ovh_as (str | Unset): OVH Application Secret<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_ovh'`<br>
        ovh_ck (str | Unset): OVH Consumer Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_ovh'`<br>
        ovh_end_point (ACMECertificateDomainOvhEndPoint | Unset): Choose the OVH API Endpoint / Region<br><br>This field
            is only available when the following conditions are met:<br>- `method` must be equal to `'dns_ovh'`<br>
        pleskxml_user (str | Unset): Plesk User<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_pleskxml'`<br>
        pleskxml_pass (str | Unset): Plesk Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_pleskxml'`<br>
        pleskxml_uri (str | Unset): Plesk Server URI<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_pleskxml'`<br>
        pointhq_key (str | Unset): PointHQ API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_pointhq'`<br>
        pointhq_email (str | Unset): PointHQ account E-mail address<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_pointhq'`<br>
        porkbun_api_key (str | Unset): API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_porkbun'`<br>
        porkbun_secret_api_key (str | Unset): Secret API Key. Obtain the key and secret from
            https://porkbun.com/account/api<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_porkbun'`<br>
        pdns_url (str | Unset): PowerDNS URL (e.g. http://ns.example.com:8081 )<br><br>This field is only available when
            the following conditions are met:<br>- `method` must be equal to `'dns_pdns'`<br>
        pdns_serverid (str | Unset): PowerDNS ServerId (e.g. localhost )<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_pdns'`<br>
        pdns_token (str | Unset): PowerDNS Token (e.g. 0123456789ABCDEF )<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_pdns'`<br>
        pdns_ttl (str | Unset): PowerDNS Record TTL (e.g. 60 )<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_pdns'`<br>
        rackcorp_apiuuid (str | Unset): API UUID<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_rackcorp'`<br>
        rackcorp_apisecret (str | Unset): API Secret<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_rackcorp'`<br>
        rackspace_username (str | Unset): Rackspace Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_rackspace'`<br>
        rackspace_apikey (str | Unset): Rackspace API Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_rackspace'`<br>
        rage4_username (str | Unset): Username<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_rage4'`<br>
        rage4_token (str | Unset): Token<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_rage4'`<br>
        rcode0_api_token (str | Unset): Rcode0 API Token<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_rcode0'`<br>
        rcode0_url (str | Unset): Rcode0 URL<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_rcode0'`<br>
        rcode0_ttl (str | Unset): Rcode0 TTL<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_rcode0'`<br>
        regru_api_username (str | Unset): reg.ru Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_regru'`<br>
        regru_api_password (str | Unset): reg.ru API Password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_regru'`<br>
        scaleway_api_token (str | Unset): API Token<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_scaleway'`<br>
        schlundtech_user (str | Unset): schlundtech.de Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_schlundtech'`<br>
        schlundtech_password (str | Unset): schlundtech.de Password<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_schlundtech'`<br>
        sl_key (str | Unset): Selectel API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_selectel'`<br>
        selfhostdns_username (str | Unset): Username (Customer number, not email address or DynDNS account)<br><br>This
            field is only available when the following conditions are met:<br>- `method` must be equal to
            `'dns_selfhost'`<br>
        selfhostdns_password (str | Unset): Password<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_selfhost'`<br>
        selfhostdns_map (str | Unset): Record ID (Edit the record, value is shown in brackets)<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_selfhost'`<br>
        servercow_api_username (str | Unset): Servercow username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_servercow'`<br>
        servercow_api_password (str | Unset): Servercow password<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_servercow'`<br>
        simply_accountname (str | Unset): Account Name<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_simply'`<br>
        simply_apikey (str | Unset): API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_simply'`<br>
        simply_api (str | Unset): API Endpoint URL. Default: https://api.simply.com/1<br><br>This field is only
            available when the following conditions are met:<br>- `method` must be equal to `'dns_simply'`<br>
        tele3_key (str | Unset): Tele3 Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_tele3'`<br>
        tele3_secret (str | Unset): Tele3 Secret<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_tele3'`<br>
        tencent_secretid (str | Unset): Tencent Secret ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_tencent'`<br>
        tencent_secretkey (str | Unset): Tencent Secret Key<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_tencent'`<br>
        udr_user (str | Unset): Username<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_udr'`<br>
        udr_pass (str | Unset): Password<br><br>This field is only available when the following conditions are met:<br>-
            `method` must be equal to `'dns_udr'`<br>
        ultra_usr (str | Unset): UltraDNS Username<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_ultra'`<br>
        ultra_pwd (str | Unset): UltraDNS Password<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_ultra'`<br>
        uno_user (str | Unset): UnoEuro username<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_unoeuro'`<br>
        uno_key (str | Unset): UnoEuro API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_unoeuro'`<br>
        variomedia_api_token (str | Unset): variomedia.de API Token<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_variomedia'`<br>
        veesp_user (str | Unset): Username<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_veesp'`<br>
        veesp_password (str | Unset): Password<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_veesp'`<br>
        vercel_token (str | Unset): Vercel Token<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_vercel'`<br>
        vscale_api_key (str | Unset): vscale API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_vscale'`<br>
        vultr_api_key (str | Unset): vultr.com API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_vultr'`<br>
        ws_apikey (str | Unset): API Key / "Identifier" in the WS Admin<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_websupport'`<br>
        ws_apisecret (str | Unset): API Secret / "Secret key" in the WS Admin. Obtain the API Key and Secret from
            https://admin.websupport.sk/en/auth/apiKey.<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_websupport'`<br>
        west_username (str | Unset): West.cn Domain API Username<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_west_cn'`<br>
        west_key (str | Unset): West.cn Domain API Key<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_west_cn'`<br>
        world4you_username (str | Unset): Username<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_world4you'`<br>
        world4you_password (str | Unset): Password<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_world4you'`<br>
        pdd_token (str | Unset): Yandex PDD Token, generate at <a href="https://pddimp.yandex.ru/api2/admin/get_token">h
            ttps://pddimp.yandex.ru/api2/admin/get_token</a><br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_yandex'`<br>
        yc_zone_id (str | Unset): DNS Zone ID<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_yc'`<br>
        yc_folder_id (str | Unset): Yandex Cloud Folder ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_yc'`<br>
        yc_sa_id (str | Unset): Service Account ID<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_yc'`<br>
        yc_sa_key_id (str | Unset): Service Account IAM Key ID<br><br>This field is only available when the following
            conditions are met:<br>- `method` must be equal to `'dns_yc'`<br>
        yc_sa_key_file_pem_b64 (str | Unset): Base64 content of private key.<br><br>This field is only available when
            the following conditions are met:<br>- `method` must be equal to `'dns_yc'`<br>
        zm_key (str | Unset): Zonomi API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_zonomi'`<br>
        zone_username (str | Unset): Zone.ee Username<br><br>This field is only available when the following conditions
            are met:<br>- `method` must be equal to `'dns_zone'`<br>
        zone_key (str | Unset): Zone.ee API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_zone'`<br>
        zilore_key (str | Unset): Zilore API Key<br><br>This field is only available when the following conditions are
            met:<br>- `method` must be equal to `'dns_zilore'`<br>
        technitium_server (str | Unset): Technitium DNS Server address<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_technitium'`<br>
        technitium_token (str | Unset): Technitium DNS Server API Token<br><br>This field is only available when the
            following conditions are met:<br>- `method` must be equal to `'dns_technitium'`<br>
        anydnschallengealias (str | Unset): (Optional) Adds the --challenge-alias flag to the acme.sh call.<br/>To use a
            CNAME for _acme-challenge.importantDomain.tld to direct the acme validation to a different (sub)domain _acme-
            challenge.aliasDomainForValidationOnly.tld, configure the alternate domain here.<br/>More information can be
            found <a href="https://github.com/acmesh-official/acme.sh/wiki/DNS-alias-mode"
            target="_new">here</a>.<br><br>This field is only available when the following conditions are met:<br>- `method`
            must not be one of [ webroot, webrootftp, standalone, standalonetls ]<br>
        anydnschallengedomain (bool | Unset): (Optional) Uses the challenge domain alias value as --domain-alias instead
            in the acme.sh call.<br><br>This field is only available when the following conditions are met:<br>- `method`
            must not be one of [ webroot, webrootftp, standalone, standalonetls ]<br>
    """

    name: str | Unset = UNSET
    status: ACMECertificateDomainStatus | Unset = ACMECertificateDomainStatus.ENABLE
    method: str | Unset = UNSET
    webrootfolder: str | Unset = UNSET
    webrootftpftpserver: str | Unset = UNSET
    webrootftpusername: str | Unset = UNSET
    webrootftppassword: str | Unset = UNSET
    webrootftpfolder: str | Unset = UNSET
    standaloneport: str | Unset = UNSET
    standaloneipv6: bool | Unset = UNSET
    standalonetlsport: str | Unset = UNSET
    nsupdate_server: str | Unset = UNSET
    nsupdate_keyname: str | Unset = UNSET
    nsupdate_keyalgo: ACMECertificateDomainNsupdateKeyalgo | Unset = UNSET
    nsupdate_key: str | Unset = UNSET
    nsupdate_zone: str | Unset = UNSET
    one984hosting_username: str | Unset = UNSET
    one984hosting_password: str | Unset = UNSET
    acmeproxy_endpoint: str | Unset = UNSET
    acmeproxy_username: str | Unset = UNSET
    acmeproxy_password: str | Unset = UNSET
    acmedns_username: str | Unset = UNSET
    acmedns_password: str | Unset = UNSET
    acmedns_subdomain: str | Unset = UNSET
    acmedns_update_url: str | Unset = UNSET
    active24_token: str | Unset = UNSET
    akamai_host: str | Unset = UNSET
    akamai_access_token: str | Unset = UNSET
    akamai_client_token: str | Unset = UNSET
    akamai_client_secret: str | Unset = UNSET
    ali_key: str | Unset = UNSET
    ali_secret: str | Unset = UNSET
    kas_login: str | Unset = UNSET
    kas_authtype: str | Unset = UNSET
    kas_authdata: str | Unset = UNSET
    ad_api_key: str | Unset = UNSET
    anx_token: str | Unset = UNSET
    af_api_username: str | Unset = UNSET
    af_api_password: str | Unset = UNSET
    arvan_token: str | Unset = UNSET
    aurora_key: str | Unset = UNSET
    aurora_secret: str | Unset = UNSET
    autodns_user: str | Unset = UNSET
    autodns_password: str | Unset = UNSET
    autodns_context: str | Unset = UNSET
    aws_access_key_id: str | Unset = UNSET
    aws_secret_access_key: str | Unset = UNSET
    aws_dns_slowrate: str | Unset = UNSET
    azion_email: str | Unset = UNSET
    azion_password: str | Unset = UNSET
    azuredns_subscriptionid: str | Unset = UNSET
    azuredns_tenantid: str | Unset = UNSET
    azuredns_appid: str | Unset = UNSET
    azuredns_clientsecret: str | Unset = UNSET
    bookmyname_username: str | Unset = UNSET
    bookmyname_password: str | Unset = UNSET
    bunny_api_key: str | Unset = UNSET
    clouddns_email: str | Unset = UNSET
    clouddns_client_id: str | Unset = UNSET
    clouddns_password: str | Unset = UNSET
    cloudns_auth_id: str | Unset = UNSET
    cloudns_sub_auth_id: str | Unset = UNSET
    cloudns_auth_password: str | Unset = UNSET
    cf_key: str | Unset = UNSET
    cf_email: str | Unset = UNSET
    cf_token: str | Unset = UNSET
    cf_account_id: str | Unset = UNSET
    cf_zone_id: str | Unset = UNSET
    conoha_username: str | Unset = UNSET
    conoha_password: str | Unset = UNSET
    conoha_tenantid: str | Unset = UNSET
    conoha_identityserviceapi: str | Unset = UNSET
    constellix_key: str | Unset = UNSET
    constellix_secret: str | Unset = UNSET
    cpanel_username: str | Unset = UNSET
    cpanel_apitoken: str | Unset = UNSET
    cpanel_hostname: str | Unset = UNSET
    cn_user: str | Unset = UNSET
    cn_password: str | Unset = UNSET
    curanet_authclientid: str | Unset = UNSET
    curanet_authsecret: str | Unset = UNSET
    cy_username: str | Unset = UNSET
    cy_password: str | Unset = UNSET
    ddnss_token: str | Unset = UNSET
    dedyn_token: str | Unset = UNSET
    dedyn_name: str | Unset = UNSET
    do_api_key: str | Unset = UNSET
    da_api: str | Unset = UNSET
    da_api_insecure: str | Unset = UNSET
    dnsexit_api_key: str | Unset = UNSET
    dnsexit_auth_user: str | Unset = UNSET
    dnsexit_auth_pass: str | Unset = UNSET
    dnshome_subdomain: str | Unset = UNSET
    dnshome_subdomainpassword: str | Unset = UNSET
    dnsimple_oauth_token: str | Unset = UNSET
    me_key: str | Unset = UNSET
    me_secret: str | Unset = UNSET
    dnsservices_username: str | Unset = UNSET
    dnsservices_password: str | Unset = UNSET
    do_letoken: str | Unset = UNSET
    do_pid: str | Unset = UNSET
    do_pw: str | Unset = UNSET
    domeneshop_token: str | Unset = UNSET
    domeneshop_secret: str | Unset = UNSET
    dp_id: str | Unset = UNSET
    dp_key: str | Unset = UNSET
    dpi_id: str | Unset = UNSET
    dpi_key: str | Unset = UNSET
    dh_api_key: str | Unset = UNSET
    duckdns_token: str | Unset = UNSET
    dd_api_user: str | Unset = UNSET
    dd_api_key: str | Unset = UNSET
    dyn_customer: str | Unset = UNSET
    dyn_username: str | Unset = UNSET
    dyn_password: str | Unset = UNSET
    df_user: str | Unset = UNSET
    df_password: str | Unset = UNSET
    dynu_clientid: str | Unset = UNSET
    dynu_secret: str | Unset = UNSET
    easydns_key: str | Unset = UNSET
    easydns_token: str | Unset = UNSET
    euserv_username: str | Unset = UNSET
    euserv_password: str | Unset = UNSET
    exoscale_api_key: str | Unset = UNSET
    exoscale_secret_key: str | Unset = UNSET
    fornex_api_key: str | Unset = UNSET
    freedns_user: str | Unset = UNSET
    freedns_password: str | Unset = UNSET
    gandi_livedns_key: str | Unset = UNSET
    gcore_key: str | Unset = UNSET
    geoscaling_username: str | Unset = UNSET
    geoscaling_password: str | Unset = UNSET
    gd_key: str | Unset = UNSET
    gd_secret: str | Unset = UNSET
    googledomains_access_token: str | Unset = UNSET
    googledomains_zone: str | Unset = UNSET
    hetzner_token: str | Unset = UNSET
    hexonet_login: str | Unset = UNSET
    hexonet_password: str | Unset = UNSET
    huaweicloud_username: str | Unset = UNSET
    huaweicloud_password: str | Unset = UNSET
    huaweicloud_domainname: str | Unset = UNSET
    he_username: str | Unset = UNSET
    he_password: str | Unset = UNSET
    hostingde_apikey: str | Unset = UNSET
    hostingde_endpoint: str | Unset = UNSET
    infoblox_creds: str | Unset = UNSET
    infoblox_server: str | Unset = UNSET
    infoblox_view: str | Unset = UNSET
    infomaniak_api_token: str | Unset = UNSET
    default_infomaniak_api_url: str | Unset = UNSET
    infomaniak_ttl: str | Unset = UNSET
    ionos_prefix: str | Unset = UNSET
    ionos_secret: str | Unset = UNSET
    ipv64_token: str | Unset = UNSET
    internetbs_api_key: str | Unset = UNSET
    internetbs_api_password: str | Unset = UNSET
    inwx_username: str | Unset = UNSET
    inwx_password: str | Unset = UNSET
    inwx_shared_secret: str | Unset = UNSET
    ispc_user: str | Unset = UNSET
    ispc_password: str | Unset = UNSET
    ispc_api: str | Unset = UNSET
    ispc_api_insecure: str | Unset = UNSET
    jd_access_key_id: str | Unset = UNSET
    jd_access_key_secret: str | Unset = UNSET
    jd_region: str | Unset = UNSET
    joker_username: str | Unset = UNSET
    joker_password: str | Unset = UNSET
    kappernetdns_key: str | Unset = UNSET
    kappernetdns_secret: str | Unset = UNSET
    kinghost_username: str | Unset = UNSET
    kinghost_password: str | Unset = UNSET
    knot_server: str | Unset = UNSET
    knot_key: str | Unset = UNSET
    la_id: str | Unset = UNSET
    la_key: str | Unset = UNSET
    lsw_key: str | Unset = UNSET
    limacity_apikey: str | Unset = UNSET
    linode_api_key: str | Unset = UNSET
    linode_v4_api_key: str | Unset = UNSET
    loopia_user: str | Unset = UNSET
    loopia_password: str | Unset = UNSET
    lua_key: str | Unset = UNSET
    lua_email: str | Unset = UNSET
    miab_username: str | Unset = UNSET
    miab_password: str | Unset = UNSET
    miab_server: str | Unset = UNSET
    misaka_key: str | Unset = UNSET
    mydnsjp_masterid: str | Unset = UNSET
    mydnsjp_password: str | Unset = UNSET
    mb_ak: str | Unset = UNSET
    mb_as: str | Unset = UNSET
    namecom_username: str | Unset = UNSET
    namecom_token: str | Unset = UNSET
    namecheap_api_key: str | Unset = UNSET
    namecheap_username: str | Unset = UNSET
    nm_user: str | Unset = UNSET
    nm_sha256: str | Unset = UNSET
    nanelo_token: str | Unset = UNSET
    nederhost_key: str | Unset = UNSET
    namesilo_key: str | Unset = UNSET
    neodigit_api_token: str | Unset = UNSET
    nc_apikey: str | Unset = UNSET
    nc_apipw: str | Unset = UNSET
    nc_cid: str | Unset = UNSET
    netlify_access_token: str | Unset = UNSET
    nic_clientid: str | Unset = UNSET
    nic_clientsecret: str | Unset = UNSET
    nic_username: str | Unset = UNSET
    nic_password: str | Unset = UNSET
    ns1_key: str | Unset = UNSET
    nw_api_token: str | Unset = UNSET
    nw_api_endpoint: ACMECertificateDomainNwApiEndpoint | Unset = UNSET
    onecom_user: str | Unset = UNSET
    onecom_password: str | Unset = UNSET
    online_api_key: str | Unset = UNSET
    oci_cli_tenancy: str | Unset = UNSET
    oci_cli_user: str | Unset = UNSET
    oci_cli_region: str | Unset = UNSET
    oci_cli_key: str | Unset = UNSET
    openprovider_user: str | Unset = UNSET
    openprovider_passwordhash: str | Unset = UNSET
    ovh_ak: str | Unset = UNSET
    ovh_as: str | Unset = UNSET
    ovh_ck: str | Unset = UNSET
    ovh_end_point: ACMECertificateDomainOvhEndPoint | Unset = UNSET
    pleskxml_user: str | Unset = UNSET
    pleskxml_pass: str | Unset = UNSET
    pleskxml_uri: str | Unset = UNSET
    pointhq_key: str | Unset = UNSET
    pointhq_email: str | Unset = UNSET
    porkbun_api_key: str | Unset = UNSET
    porkbun_secret_api_key: str | Unset = UNSET
    pdns_url: str | Unset = UNSET
    pdns_serverid: str | Unset = UNSET
    pdns_token: str | Unset = UNSET
    pdns_ttl: str | Unset = UNSET
    rackcorp_apiuuid: str | Unset = UNSET
    rackcorp_apisecret: str | Unset = UNSET
    rackspace_username: str | Unset = UNSET
    rackspace_apikey: str | Unset = UNSET
    rage4_username: str | Unset = UNSET
    rage4_token: str | Unset = UNSET
    rcode0_api_token: str | Unset = UNSET
    rcode0_url: str | Unset = UNSET
    rcode0_ttl: str | Unset = UNSET
    regru_api_username: str | Unset = UNSET
    regru_api_password: str | Unset = UNSET
    scaleway_api_token: str | Unset = UNSET
    schlundtech_user: str | Unset = UNSET
    schlundtech_password: str | Unset = UNSET
    sl_key: str | Unset = UNSET
    selfhostdns_username: str | Unset = UNSET
    selfhostdns_password: str | Unset = UNSET
    selfhostdns_map: str | Unset = UNSET
    servercow_api_username: str | Unset = UNSET
    servercow_api_password: str | Unset = UNSET
    simply_accountname: str | Unset = UNSET
    simply_apikey: str | Unset = UNSET
    simply_api: str | Unset = UNSET
    tele3_key: str | Unset = UNSET
    tele3_secret: str | Unset = UNSET
    tencent_secretid: str | Unset = UNSET
    tencent_secretkey: str | Unset = UNSET
    udr_user: str | Unset = UNSET
    udr_pass: str | Unset = UNSET
    ultra_usr: str | Unset = UNSET
    ultra_pwd: str | Unset = UNSET
    uno_user: str | Unset = UNSET
    uno_key: str | Unset = UNSET
    variomedia_api_token: str | Unset = UNSET
    veesp_user: str | Unset = UNSET
    veesp_password: str | Unset = UNSET
    vercel_token: str | Unset = UNSET
    vscale_api_key: str | Unset = UNSET
    vultr_api_key: str | Unset = UNSET
    ws_apikey: str | Unset = UNSET
    ws_apisecret: str | Unset = UNSET
    west_username: str | Unset = UNSET
    west_key: str | Unset = UNSET
    world4you_username: str | Unset = UNSET
    world4you_password: str | Unset = UNSET
    pdd_token: str | Unset = UNSET
    yc_zone_id: str | Unset = UNSET
    yc_folder_id: str | Unset = UNSET
    yc_sa_id: str | Unset = UNSET
    yc_sa_key_id: str | Unset = UNSET
    yc_sa_key_file_pem_b64: str | Unset = UNSET
    zm_key: str | Unset = UNSET
    zone_username: str | Unset = UNSET
    zone_key: str | Unset = UNSET
    zilore_key: str | Unset = UNSET
    technitium_server: str | Unset = UNSET
    technitium_token: str | Unset = UNSET
    anydnschallengealias: str | Unset = UNSET
    anydnschallengedomain: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        method = self.method

        webrootfolder = self.webrootfolder

        webrootftpftpserver = self.webrootftpftpserver

        webrootftpusername = self.webrootftpusername

        webrootftppassword = self.webrootftppassword

        webrootftpfolder = self.webrootftpfolder

        standaloneport = self.standaloneport

        standaloneipv6 = self.standaloneipv6

        standalonetlsport = self.standalonetlsport

        nsupdate_server = self.nsupdate_server

        nsupdate_keyname = self.nsupdate_keyname

        nsupdate_keyalgo: str | Unset = UNSET
        if not isinstance(self.nsupdate_keyalgo, Unset):
            nsupdate_keyalgo = self.nsupdate_keyalgo.value

        nsupdate_key = self.nsupdate_key

        nsupdate_zone = self.nsupdate_zone

        one984hosting_username = self.one984hosting_username

        one984hosting_password = self.one984hosting_password

        acmeproxy_endpoint = self.acmeproxy_endpoint

        acmeproxy_username = self.acmeproxy_username

        acmeproxy_password = self.acmeproxy_password

        acmedns_username = self.acmedns_username

        acmedns_password = self.acmedns_password

        acmedns_subdomain = self.acmedns_subdomain

        acmedns_update_url = self.acmedns_update_url

        active24_token = self.active24_token

        akamai_host = self.akamai_host

        akamai_access_token = self.akamai_access_token

        akamai_client_token = self.akamai_client_token

        akamai_client_secret = self.akamai_client_secret

        ali_key = self.ali_key

        ali_secret = self.ali_secret

        kas_login = self.kas_login

        kas_authtype = self.kas_authtype

        kas_authdata = self.kas_authdata

        ad_api_key = self.ad_api_key

        anx_token = self.anx_token

        af_api_username = self.af_api_username

        af_api_password = self.af_api_password

        arvan_token = self.arvan_token

        aurora_key = self.aurora_key

        aurora_secret = self.aurora_secret

        autodns_user = self.autodns_user

        autodns_password = self.autodns_password

        autodns_context = self.autodns_context

        aws_access_key_id = self.aws_access_key_id

        aws_secret_access_key = self.aws_secret_access_key

        aws_dns_slowrate = self.aws_dns_slowrate

        azion_email = self.azion_email

        azion_password = self.azion_password

        azuredns_subscriptionid = self.azuredns_subscriptionid

        azuredns_tenantid = self.azuredns_tenantid

        azuredns_appid = self.azuredns_appid

        azuredns_clientsecret = self.azuredns_clientsecret

        bookmyname_username = self.bookmyname_username

        bookmyname_password = self.bookmyname_password

        bunny_api_key = self.bunny_api_key

        clouddns_email = self.clouddns_email

        clouddns_client_id = self.clouddns_client_id

        clouddns_password = self.clouddns_password

        cloudns_auth_id = self.cloudns_auth_id

        cloudns_sub_auth_id = self.cloudns_sub_auth_id

        cloudns_auth_password = self.cloudns_auth_password

        cf_key = self.cf_key

        cf_email = self.cf_email

        cf_token = self.cf_token

        cf_account_id = self.cf_account_id

        cf_zone_id = self.cf_zone_id

        conoha_username = self.conoha_username

        conoha_password = self.conoha_password

        conoha_tenantid = self.conoha_tenantid

        conoha_identityserviceapi = self.conoha_identityserviceapi

        constellix_key = self.constellix_key

        constellix_secret = self.constellix_secret

        cpanel_username = self.cpanel_username

        cpanel_apitoken = self.cpanel_apitoken

        cpanel_hostname = self.cpanel_hostname

        cn_user = self.cn_user

        cn_password = self.cn_password

        curanet_authclientid = self.curanet_authclientid

        curanet_authsecret = self.curanet_authsecret

        cy_username = self.cy_username

        cy_password = self.cy_password

        ddnss_token = self.ddnss_token

        dedyn_token = self.dedyn_token

        dedyn_name = self.dedyn_name

        do_api_key = self.do_api_key

        da_api = self.da_api

        da_api_insecure = self.da_api_insecure

        dnsexit_api_key = self.dnsexit_api_key

        dnsexit_auth_user = self.dnsexit_auth_user

        dnsexit_auth_pass = self.dnsexit_auth_pass

        dnshome_subdomain = self.dnshome_subdomain

        dnshome_subdomainpassword = self.dnshome_subdomainpassword

        dnsimple_oauth_token = self.dnsimple_oauth_token

        me_key = self.me_key

        me_secret = self.me_secret

        dnsservices_username = self.dnsservices_username

        dnsservices_password = self.dnsservices_password

        do_letoken = self.do_letoken

        do_pid = self.do_pid

        do_pw = self.do_pw

        domeneshop_token = self.domeneshop_token

        domeneshop_secret = self.domeneshop_secret

        dp_id = self.dp_id

        dp_key = self.dp_key

        dpi_id = self.dpi_id

        dpi_key = self.dpi_key

        dh_api_key = self.dh_api_key

        duckdns_token = self.duckdns_token

        dd_api_user = self.dd_api_user

        dd_api_key = self.dd_api_key

        dyn_customer = self.dyn_customer

        dyn_username = self.dyn_username

        dyn_password = self.dyn_password

        df_user = self.df_user

        df_password = self.df_password

        dynu_clientid = self.dynu_clientid

        dynu_secret = self.dynu_secret

        easydns_key = self.easydns_key

        easydns_token = self.easydns_token

        euserv_username = self.euserv_username

        euserv_password = self.euserv_password

        exoscale_api_key = self.exoscale_api_key

        exoscale_secret_key = self.exoscale_secret_key

        fornex_api_key = self.fornex_api_key

        freedns_user = self.freedns_user

        freedns_password = self.freedns_password

        gandi_livedns_key = self.gandi_livedns_key

        gcore_key = self.gcore_key

        geoscaling_username = self.geoscaling_username

        geoscaling_password = self.geoscaling_password

        gd_key = self.gd_key

        gd_secret = self.gd_secret

        googledomains_access_token = self.googledomains_access_token

        googledomains_zone = self.googledomains_zone

        hetzner_token = self.hetzner_token

        hexonet_login = self.hexonet_login

        hexonet_password = self.hexonet_password

        huaweicloud_username = self.huaweicloud_username

        huaweicloud_password = self.huaweicloud_password

        huaweicloud_domainname = self.huaweicloud_domainname

        he_username = self.he_username

        he_password = self.he_password

        hostingde_apikey = self.hostingde_apikey

        hostingde_endpoint = self.hostingde_endpoint

        infoblox_creds = self.infoblox_creds

        infoblox_server = self.infoblox_server

        infoblox_view = self.infoblox_view

        infomaniak_api_token = self.infomaniak_api_token

        default_infomaniak_api_url = self.default_infomaniak_api_url

        infomaniak_ttl = self.infomaniak_ttl

        ionos_prefix = self.ionos_prefix

        ionos_secret = self.ionos_secret

        ipv64_token = self.ipv64_token

        internetbs_api_key = self.internetbs_api_key

        internetbs_api_password = self.internetbs_api_password

        inwx_username = self.inwx_username

        inwx_password = self.inwx_password

        inwx_shared_secret = self.inwx_shared_secret

        ispc_user = self.ispc_user

        ispc_password = self.ispc_password

        ispc_api = self.ispc_api

        ispc_api_insecure = self.ispc_api_insecure

        jd_access_key_id = self.jd_access_key_id

        jd_access_key_secret = self.jd_access_key_secret

        jd_region = self.jd_region

        joker_username = self.joker_username

        joker_password = self.joker_password

        kappernetdns_key = self.kappernetdns_key

        kappernetdns_secret = self.kappernetdns_secret

        kinghost_username = self.kinghost_username

        kinghost_password = self.kinghost_password

        knot_server = self.knot_server

        knot_key = self.knot_key

        la_id = self.la_id

        la_key = self.la_key

        lsw_key = self.lsw_key

        limacity_apikey = self.limacity_apikey

        linode_api_key = self.linode_api_key

        linode_v4_api_key = self.linode_v4_api_key

        loopia_user = self.loopia_user

        loopia_password = self.loopia_password

        lua_key = self.lua_key

        lua_email = self.lua_email

        miab_username = self.miab_username

        miab_password = self.miab_password

        miab_server = self.miab_server

        misaka_key = self.misaka_key

        mydnsjp_masterid = self.mydnsjp_masterid

        mydnsjp_password = self.mydnsjp_password

        mb_ak = self.mb_ak

        mb_as = self.mb_as

        namecom_username = self.namecom_username

        namecom_token = self.namecom_token

        namecheap_api_key = self.namecheap_api_key

        namecheap_username = self.namecheap_username

        nm_user = self.nm_user

        nm_sha256 = self.nm_sha256

        nanelo_token = self.nanelo_token

        nederhost_key = self.nederhost_key

        namesilo_key = self.namesilo_key

        neodigit_api_token = self.neodigit_api_token

        nc_apikey = self.nc_apikey

        nc_apipw = self.nc_apipw

        nc_cid = self.nc_cid

        netlify_access_token = self.netlify_access_token

        nic_clientid = self.nic_clientid

        nic_clientsecret = self.nic_clientsecret

        nic_username = self.nic_username

        nic_password = self.nic_password

        ns1_key = self.ns1_key

        nw_api_token = self.nw_api_token

        nw_api_endpoint: str | Unset = UNSET
        if not isinstance(self.nw_api_endpoint, Unset):
            nw_api_endpoint = self.nw_api_endpoint.value

        onecom_user = self.onecom_user

        onecom_password = self.onecom_password

        online_api_key = self.online_api_key

        oci_cli_tenancy = self.oci_cli_tenancy

        oci_cli_user = self.oci_cli_user

        oci_cli_region = self.oci_cli_region

        oci_cli_key = self.oci_cli_key

        openprovider_user = self.openprovider_user

        openprovider_passwordhash = self.openprovider_passwordhash

        ovh_ak = self.ovh_ak

        ovh_as = self.ovh_as

        ovh_ck = self.ovh_ck

        ovh_end_point: str | Unset = UNSET
        if not isinstance(self.ovh_end_point, Unset):
            ovh_end_point = self.ovh_end_point.value

        pleskxml_user = self.pleskxml_user

        pleskxml_pass = self.pleskxml_pass

        pleskxml_uri = self.pleskxml_uri

        pointhq_key = self.pointhq_key

        pointhq_email = self.pointhq_email

        porkbun_api_key = self.porkbun_api_key

        porkbun_secret_api_key = self.porkbun_secret_api_key

        pdns_url = self.pdns_url

        pdns_serverid = self.pdns_serverid

        pdns_token = self.pdns_token

        pdns_ttl = self.pdns_ttl

        rackcorp_apiuuid = self.rackcorp_apiuuid

        rackcorp_apisecret = self.rackcorp_apisecret

        rackspace_username = self.rackspace_username

        rackspace_apikey = self.rackspace_apikey

        rage4_username = self.rage4_username

        rage4_token = self.rage4_token

        rcode0_api_token = self.rcode0_api_token

        rcode0_url = self.rcode0_url

        rcode0_ttl = self.rcode0_ttl

        regru_api_username = self.regru_api_username

        regru_api_password = self.regru_api_password

        scaleway_api_token = self.scaleway_api_token

        schlundtech_user = self.schlundtech_user

        schlundtech_password = self.schlundtech_password

        sl_key = self.sl_key

        selfhostdns_username = self.selfhostdns_username

        selfhostdns_password = self.selfhostdns_password

        selfhostdns_map = self.selfhostdns_map

        servercow_api_username = self.servercow_api_username

        servercow_api_password = self.servercow_api_password

        simply_accountname = self.simply_accountname

        simply_apikey = self.simply_apikey

        simply_api = self.simply_api

        tele3_key = self.tele3_key

        tele3_secret = self.tele3_secret

        tencent_secretid = self.tencent_secretid

        tencent_secretkey = self.tencent_secretkey

        udr_user = self.udr_user

        udr_pass = self.udr_pass

        ultra_usr = self.ultra_usr

        ultra_pwd = self.ultra_pwd

        uno_user = self.uno_user

        uno_key = self.uno_key

        variomedia_api_token = self.variomedia_api_token

        veesp_user = self.veesp_user

        veesp_password = self.veesp_password

        vercel_token = self.vercel_token

        vscale_api_key = self.vscale_api_key

        vultr_api_key = self.vultr_api_key

        ws_apikey = self.ws_apikey

        ws_apisecret = self.ws_apisecret

        west_username = self.west_username

        west_key = self.west_key

        world4you_username = self.world4you_username

        world4you_password = self.world4you_password

        pdd_token = self.pdd_token

        yc_zone_id = self.yc_zone_id

        yc_folder_id = self.yc_folder_id

        yc_sa_id = self.yc_sa_id

        yc_sa_key_id = self.yc_sa_key_id

        yc_sa_key_file_pem_b64 = self.yc_sa_key_file_pem_b64

        zm_key = self.zm_key

        zone_username = self.zone_username

        zone_key = self.zone_key

        zilore_key = self.zilore_key

        technitium_server = self.technitium_server

        technitium_token = self.technitium_token

        anydnschallengealias = self.anydnschallengealias

        anydnschallengedomain = self.anydnschallengedomain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if method is not UNSET:
            field_dict["method"] = method
        if webrootfolder is not UNSET:
            field_dict["webrootfolder"] = webrootfolder
        if webrootftpftpserver is not UNSET:
            field_dict["webrootftpftpserver"] = webrootftpftpserver
        if webrootftpusername is not UNSET:
            field_dict["webrootftpusername"] = webrootftpusername
        if webrootftppassword is not UNSET:
            field_dict["webrootftppassword"] = webrootftppassword
        if webrootftpfolder is not UNSET:
            field_dict["webrootftpfolder"] = webrootftpfolder
        if standaloneport is not UNSET:
            field_dict["standaloneport"] = standaloneport
        if standaloneipv6 is not UNSET:
            field_dict["standaloneipv6"] = standaloneipv6
        if standalonetlsport is not UNSET:
            field_dict["standalonetlsport"] = standalonetlsport
        if nsupdate_server is not UNSET:
            field_dict["nsupdate_server"] = nsupdate_server
        if nsupdate_keyname is not UNSET:
            field_dict["nsupdate_keyname"] = nsupdate_keyname
        if nsupdate_keyalgo is not UNSET:
            field_dict["nsupdate_keyalgo"] = nsupdate_keyalgo
        if nsupdate_key is not UNSET:
            field_dict["nsupdate_key"] = nsupdate_key
        if nsupdate_zone is not UNSET:
            field_dict["nsupdate_zone"] = nsupdate_zone
        if one984hosting_username is not UNSET:
            field_dict["one984hosting_username"] = one984hosting_username
        if one984hosting_password is not UNSET:
            field_dict["one984hosting_password"] = one984hosting_password
        if acmeproxy_endpoint is not UNSET:
            field_dict["acmeproxy_endpoint"] = acmeproxy_endpoint
        if acmeproxy_username is not UNSET:
            field_dict["acmeproxy_username"] = acmeproxy_username
        if acmeproxy_password is not UNSET:
            field_dict["acmeproxy_password"] = acmeproxy_password
        if acmedns_username is not UNSET:
            field_dict["acmedns_username"] = acmedns_username
        if acmedns_password is not UNSET:
            field_dict["acmedns_password"] = acmedns_password
        if acmedns_subdomain is not UNSET:
            field_dict["acmedns_subdomain"] = acmedns_subdomain
        if acmedns_update_url is not UNSET:
            field_dict["acmedns_update_url"] = acmedns_update_url
        if active24_token is not UNSET:
            field_dict["active24_token"] = active24_token
        if akamai_host is not UNSET:
            field_dict["akamai_host"] = akamai_host
        if akamai_access_token is not UNSET:
            field_dict["akamai_access_token"] = akamai_access_token
        if akamai_client_token is not UNSET:
            field_dict["akamai_client_token"] = akamai_client_token
        if akamai_client_secret is not UNSET:
            field_dict["akamai_client_secret"] = akamai_client_secret
        if ali_key is not UNSET:
            field_dict["ali_key"] = ali_key
        if ali_secret is not UNSET:
            field_dict["ali_secret"] = ali_secret
        if kas_login is not UNSET:
            field_dict["kas_login"] = kas_login
        if kas_authtype is not UNSET:
            field_dict["kas_authtype"] = kas_authtype
        if kas_authdata is not UNSET:
            field_dict["kas_authdata"] = kas_authdata
        if ad_api_key is not UNSET:
            field_dict["ad_api_key"] = ad_api_key
        if anx_token is not UNSET:
            field_dict["anx_token"] = anx_token
        if af_api_username is not UNSET:
            field_dict["af_api_username"] = af_api_username
        if af_api_password is not UNSET:
            field_dict["af_api_password"] = af_api_password
        if arvan_token is not UNSET:
            field_dict["arvan_token"] = arvan_token
        if aurora_key is not UNSET:
            field_dict["aurora_key"] = aurora_key
        if aurora_secret is not UNSET:
            field_dict["aurora_secret"] = aurora_secret
        if autodns_user is not UNSET:
            field_dict["autodns_user"] = autodns_user
        if autodns_password is not UNSET:
            field_dict["autodns_password"] = autodns_password
        if autodns_context is not UNSET:
            field_dict["autodns_context"] = autodns_context
        if aws_access_key_id is not UNSET:
            field_dict["aws_access_key_id"] = aws_access_key_id
        if aws_secret_access_key is not UNSET:
            field_dict["aws_secret_access_key"] = aws_secret_access_key
        if aws_dns_slowrate is not UNSET:
            field_dict["aws_dns_slowrate"] = aws_dns_slowrate
        if azion_email is not UNSET:
            field_dict["azion_email"] = azion_email
        if azion_password is not UNSET:
            field_dict["azion_password"] = azion_password
        if azuredns_subscriptionid is not UNSET:
            field_dict["azuredns_subscriptionid"] = azuredns_subscriptionid
        if azuredns_tenantid is not UNSET:
            field_dict["azuredns_tenantid"] = azuredns_tenantid
        if azuredns_appid is not UNSET:
            field_dict["azuredns_appid"] = azuredns_appid
        if azuredns_clientsecret is not UNSET:
            field_dict["azuredns_clientsecret"] = azuredns_clientsecret
        if bookmyname_username is not UNSET:
            field_dict["bookmyname_username"] = bookmyname_username
        if bookmyname_password is not UNSET:
            field_dict["bookmyname_password"] = bookmyname_password
        if bunny_api_key is not UNSET:
            field_dict["bunny_api_key"] = bunny_api_key
        if clouddns_email is not UNSET:
            field_dict["clouddns_email"] = clouddns_email
        if clouddns_client_id is not UNSET:
            field_dict["clouddns_client_id"] = clouddns_client_id
        if clouddns_password is not UNSET:
            field_dict["clouddns_password"] = clouddns_password
        if cloudns_auth_id is not UNSET:
            field_dict["cloudns_auth_id"] = cloudns_auth_id
        if cloudns_sub_auth_id is not UNSET:
            field_dict["cloudns_sub_auth_id"] = cloudns_sub_auth_id
        if cloudns_auth_password is not UNSET:
            field_dict["cloudns_auth_password"] = cloudns_auth_password
        if cf_key is not UNSET:
            field_dict["cf_key"] = cf_key
        if cf_email is not UNSET:
            field_dict["cf_email"] = cf_email
        if cf_token is not UNSET:
            field_dict["cf_token"] = cf_token
        if cf_account_id is not UNSET:
            field_dict["cf_account_id"] = cf_account_id
        if cf_zone_id is not UNSET:
            field_dict["cf_zone_id"] = cf_zone_id
        if conoha_username is not UNSET:
            field_dict["conoha_username"] = conoha_username
        if conoha_password is not UNSET:
            field_dict["conoha_password"] = conoha_password
        if conoha_tenantid is not UNSET:
            field_dict["conoha_tenantid"] = conoha_tenantid
        if conoha_identityserviceapi is not UNSET:
            field_dict["conoha_identityserviceapi"] = conoha_identityserviceapi
        if constellix_key is not UNSET:
            field_dict["constellix_key"] = constellix_key
        if constellix_secret is not UNSET:
            field_dict["constellix_secret"] = constellix_secret
        if cpanel_username is not UNSET:
            field_dict["cpanel_username"] = cpanel_username
        if cpanel_apitoken is not UNSET:
            field_dict["cpanel_apitoken"] = cpanel_apitoken
        if cpanel_hostname is not UNSET:
            field_dict["cpanel_hostname"] = cpanel_hostname
        if cn_user is not UNSET:
            field_dict["cn_user"] = cn_user
        if cn_password is not UNSET:
            field_dict["cn_password"] = cn_password
        if curanet_authclientid is not UNSET:
            field_dict["curanet_authclientid"] = curanet_authclientid
        if curanet_authsecret is not UNSET:
            field_dict["curanet_authsecret"] = curanet_authsecret
        if cy_username is not UNSET:
            field_dict["cy_username"] = cy_username
        if cy_password is not UNSET:
            field_dict["cy_password"] = cy_password
        if ddnss_token is not UNSET:
            field_dict["ddnss_token"] = ddnss_token
        if dedyn_token is not UNSET:
            field_dict["dedyn_token"] = dedyn_token
        if dedyn_name is not UNSET:
            field_dict["dedyn_name"] = dedyn_name
        if do_api_key is not UNSET:
            field_dict["do_api_key"] = do_api_key
        if da_api is not UNSET:
            field_dict["da_api"] = da_api
        if da_api_insecure is not UNSET:
            field_dict["da_api_insecure"] = da_api_insecure
        if dnsexit_api_key is not UNSET:
            field_dict["dnsexit_api_key"] = dnsexit_api_key
        if dnsexit_auth_user is not UNSET:
            field_dict["dnsexit_auth_user"] = dnsexit_auth_user
        if dnsexit_auth_pass is not UNSET:
            field_dict["dnsexit_auth_pass"] = dnsexit_auth_pass
        if dnshome_subdomain is not UNSET:
            field_dict["dnshome_subdomain"] = dnshome_subdomain
        if dnshome_subdomainpassword is not UNSET:
            field_dict["dnshome_subdomainpassword"] = dnshome_subdomainpassword
        if dnsimple_oauth_token is not UNSET:
            field_dict["dnsimple_oauth_token"] = dnsimple_oauth_token
        if me_key is not UNSET:
            field_dict["me_key"] = me_key
        if me_secret is not UNSET:
            field_dict["me_secret"] = me_secret
        if dnsservices_username is not UNSET:
            field_dict["dnsservices_username"] = dnsservices_username
        if dnsservices_password is not UNSET:
            field_dict["dnsservices_password"] = dnsservices_password
        if do_letoken is not UNSET:
            field_dict["do_letoken"] = do_letoken
        if do_pid is not UNSET:
            field_dict["do_pid"] = do_pid
        if do_pw is not UNSET:
            field_dict["do_pw"] = do_pw
        if domeneshop_token is not UNSET:
            field_dict["domeneshop_token"] = domeneshop_token
        if domeneshop_secret is not UNSET:
            field_dict["domeneshop_secret"] = domeneshop_secret
        if dp_id is not UNSET:
            field_dict["dp_id"] = dp_id
        if dp_key is not UNSET:
            field_dict["dp_key"] = dp_key
        if dpi_id is not UNSET:
            field_dict["dpi_id"] = dpi_id
        if dpi_key is not UNSET:
            field_dict["dpi_key"] = dpi_key
        if dh_api_key is not UNSET:
            field_dict["dh_api_key"] = dh_api_key
        if duckdns_token is not UNSET:
            field_dict["duckdns_token"] = duckdns_token
        if dd_api_user is not UNSET:
            field_dict["dd_api_user"] = dd_api_user
        if dd_api_key is not UNSET:
            field_dict["dd_api_key"] = dd_api_key
        if dyn_customer is not UNSET:
            field_dict["dyn_customer"] = dyn_customer
        if dyn_username is not UNSET:
            field_dict["dyn_username"] = dyn_username
        if dyn_password is not UNSET:
            field_dict["dyn_password"] = dyn_password
        if df_user is not UNSET:
            field_dict["df_user"] = df_user
        if df_password is not UNSET:
            field_dict["df_password"] = df_password
        if dynu_clientid is not UNSET:
            field_dict["dynu_clientid"] = dynu_clientid
        if dynu_secret is not UNSET:
            field_dict["dynu_secret"] = dynu_secret
        if easydns_key is not UNSET:
            field_dict["easydns_key"] = easydns_key
        if easydns_token is not UNSET:
            field_dict["easydns_token"] = easydns_token
        if euserv_username is not UNSET:
            field_dict["euserv_username"] = euserv_username
        if euserv_password is not UNSET:
            field_dict["euserv_password"] = euserv_password
        if exoscale_api_key is not UNSET:
            field_dict["exoscale_api_key"] = exoscale_api_key
        if exoscale_secret_key is not UNSET:
            field_dict["exoscale_secret_key"] = exoscale_secret_key
        if fornex_api_key is not UNSET:
            field_dict["fornex_api_key"] = fornex_api_key
        if freedns_user is not UNSET:
            field_dict["freedns_user"] = freedns_user
        if freedns_password is not UNSET:
            field_dict["freedns_password"] = freedns_password
        if gandi_livedns_key is not UNSET:
            field_dict["gandi_livedns_key"] = gandi_livedns_key
        if gcore_key is not UNSET:
            field_dict["gcore_key"] = gcore_key
        if geoscaling_username is not UNSET:
            field_dict["geoscaling_username"] = geoscaling_username
        if geoscaling_password is not UNSET:
            field_dict["geoscaling_password"] = geoscaling_password
        if gd_key is not UNSET:
            field_dict["gd_key"] = gd_key
        if gd_secret is not UNSET:
            field_dict["gd_secret"] = gd_secret
        if googledomains_access_token is not UNSET:
            field_dict["googledomains_access_token"] = googledomains_access_token
        if googledomains_zone is not UNSET:
            field_dict["googledomains_zone"] = googledomains_zone
        if hetzner_token is not UNSET:
            field_dict["hetzner_token"] = hetzner_token
        if hexonet_login is not UNSET:
            field_dict["hexonet_login"] = hexonet_login
        if hexonet_password is not UNSET:
            field_dict["hexonet_password"] = hexonet_password
        if huaweicloud_username is not UNSET:
            field_dict["huaweicloud_username"] = huaweicloud_username
        if huaweicloud_password is not UNSET:
            field_dict["huaweicloud_password"] = huaweicloud_password
        if huaweicloud_domainname is not UNSET:
            field_dict["huaweicloud_domainname"] = huaweicloud_domainname
        if he_username is not UNSET:
            field_dict["he_username"] = he_username
        if he_password is not UNSET:
            field_dict["he_password"] = he_password
        if hostingde_apikey is not UNSET:
            field_dict["hostingde_apikey"] = hostingde_apikey
        if hostingde_endpoint is not UNSET:
            field_dict["hostingde_endpoint"] = hostingde_endpoint
        if infoblox_creds is not UNSET:
            field_dict["infoblox_creds"] = infoblox_creds
        if infoblox_server is not UNSET:
            field_dict["infoblox_server"] = infoblox_server
        if infoblox_view is not UNSET:
            field_dict["infoblox_view"] = infoblox_view
        if infomaniak_api_token is not UNSET:
            field_dict["infomaniak_api_token"] = infomaniak_api_token
        if default_infomaniak_api_url is not UNSET:
            field_dict["default_infomaniak_api_url"] = default_infomaniak_api_url
        if infomaniak_ttl is not UNSET:
            field_dict["infomaniak_ttl"] = infomaniak_ttl
        if ionos_prefix is not UNSET:
            field_dict["ionos_prefix"] = ionos_prefix
        if ionos_secret is not UNSET:
            field_dict["ionos_secret"] = ionos_secret
        if ipv64_token is not UNSET:
            field_dict["ipv64_token"] = ipv64_token
        if internetbs_api_key is not UNSET:
            field_dict["internetbs_api_key"] = internetbs_api_key
        if internetbs_api_password is not UNSET:
            field_dict["internetbs_api_password"] = internetbs_api_password
        if inwx_username is not UNSET:
            field_dict["inwx_username"] = inwx_username
        if inwx_password is not UNSET:
            field_dict["inwx_password"] = inwx_password
        if inwx_shared_secret is not UNSET:
            field_dict["inwx_shared_secret"] = inwx_shared_secret
        if ispc_user is not UNSET:
            field_dict["ispc_user"] = ispc_user
        if ispc_password is not UNSET:
            field_dict["ispc_password"] = ispc_password
        if ispc_api is not UNSET:
            field_dict["ispc_api"] = ispc_api
        if ispc_api_insecure is not UNSET:
            field_dict["ispc_api_insecure"] = ispc_api_insecure
        if jd_access_key_id is not UNSET:
            field_dict["jd_access_key_id"] = jd_access_key_id
        if jd_access_key_secret is not UNSET:
            field_dict["jd_access_key_secret"] = jd_access_key_secret
        if jd_region is not UNSET:
            field_dict["jd_region"] = jd_region
        if joker_username is not UNSET:
            field_dict["joker_username"] = joker_username
        if joker_password is not UNSET:
            field_dict["joker_password"] = joker_password
        if kappernetdns_key is not UNSET:
            field_dict["kappernetdns_key"] = kappernetdns_key
        if kappernetdns_secret is not UNSET:
            field_dict["kappernetdns_secret"] = kappernetdns_secret
        if kinghost_username is not UNSET:
            field_dict["kinghost_username"] = kinghost_username
        if kinghost_password is not UNSET:
            field_dict["kinghost_password"] = kinghost_password
        if knot_server is not UNSET:
            field_dict["knot_server"] = knot_server
        if knot_key is not UNSET:
            field_dict["knot_key"] = knot_key
        if la_id is not UNSET:
            field_dict["la_id"] = la_id
        if la_key is not UNSET:
            field_dict["la_key"] = la_key
        if lsw_key is not UNSET:
            field_dict["lsw_key"] = lsw_key
        if limacity_apikey is not UNSET:
            field_dict["limacity_apikey"] = limacity_apikey
        if linode_api_key is not UNSET:
            field_dict["linode_api_key"] = linode_api_key
        if linode_v4_api_key is not UNSET:
            field_dict["linode_v4_api_key"] = linode_v4_api_key
        if loopia_user is not UNSET:
            field_dict["loopia_user"] = loopia_user
        if loopia_password is not UNSET:
            field_dict["loopia_password"] = loopia_password
        if lua_key is not UNSET:
            field_dict["lua_key"] = lua_key
        if lua_email is not UNSET:
            field_dict["lua_email"] = lua_email
        if miab_username is not UNSET:
            field_dict["miab_username"] = miab_username
        if miab_password is not UNSET:
            field_dict["miab_password"] = miab_password
        if miab_server is not UNSET:
            field_dict["miab_server"] = miab_server
        if misaka_key is not UNSET:
            field_dict["misaka_key"] = misaka_key
        if mydnsjp_masterid is not UNSET:
            field_dict["mydnsjp_masterid"] = mydnsjp_masterid
        if mydnsjp_password is not UNSET:
            field_dict["mydnsjp_password"] = mydnsjp_password
        if mb_ak is not UNSET:
            field_dict["mb_ak"] = mb_ak
        if mb_as is not UNSET:
            field_dict["mb_as"] = mb_as
        if namecom_username is not UNSET:
            field_dict["namecom_username"] = namecom_username
        if namecom_token is not UNSET:
            field_dict["namecom_token"] = namecom_token
        if namecheap_api_key is not UNSET:
            field_dict["namecheap_api_key"] = namecheap_api_key
        if namecheap_username is not UNSET:
            field_dict["namecheap_username"] = namecheap_username
        if nm_user is not UNSET:
            field_dict["nm_user"] = nm_user
        if nm_sha256 is not UNSET:
            field_dict["nm_sha256"] = nm_sha256
        if nanelo_token is not UNSET:
            field_dict["nanelo_token"] = nanelo_token
        if nederhost_key is not UNSET:
            field_dict["nederhost_key"] = nederhost_key
        if namesilo_key is not UNSET:
            field_dict["namesilo_key"] = namesilo_key
        if neodigit_api_token is not UNSET:
            field_dict["neodigit_api_token"] = neodigit_api_token
        if nc_apikey is not UNSET:
            field_dict["nc_apikey"] = nc_apikey
        if nc_apipw is not UNSET:
            field_dict["nc_apipw"] = nc_apipw
        if nc_cid is not UNSET:
            field_dict["nc_cid"] = nc_cid
        if netlify_access_token is not UNSET:
            field_dict["netlify_access_token"] = netlify_access_token
        if nic_clientid is not UNSET:
            field_dict["nic_clientid"] = nic_clientid
        if nic_clientsecret is not UNSET:
            field_dict["nic_clientsecret"] = nic_clientsecret
        if nic_username is not UNSET:
            field_dict["nic_username"] = nic_username
        if nic_password is not UNSET:
            field_dict["nic_password"] = nic_password
        if ns1_key is not UNSET:
            field_dict["ns1_key"] = ns1_key
        if nw_api_token is not UNSET:
            field_dict["nw_api_token"] = nw_api_token
        if nw_api_endpoint is not UNSET:
            field_dict["nw_api_endpoint"] = nw_api_endpoint
        if onecom_user is not UNSET:
            field_dict["onecom_user"] = onecom_user
        if onecom_password is not UNSET:
            field_dict["onecom_password"] = onecom_password
        if online_api_key is not UNSET:
            field_dict["online_api_key"] = online_api_key
        if oci_cli_tenancy is not UNSET:
            field_dict["oci_cli_tenancy"] = oci_cli_tenancy
        if oci_cli_user is not UNSET:
            field_dict["oci_cli_user"] = oci_cli_user
        if oci_cli_region is not UNSET:
            field_dict["oci_cli_region"] = oci_cli_region
        if oci_cli_key is not UNSET:
            field_dict["oci_cli_key"] = oci_cli_key
        if openprovider_user is not UNSET:
            field_dict["openprovider_user"] = openprovider_user
        if openprovider_passwordhash is not UNSET:
            field_dict["openprovider_passwordhash"] = openprovider_passwordhash
        if ovh_ak is not UNSET:
            field_dict["ovh_ak"] = ovh_ak
        if ovh_as is not UNSET:
            field_dict["ovh_as"] = ovh_as
        if ovh_ck is not UNSET:
            field_dict["ovh_ck"] = ovh_ck
        if ovh_end_point is not UNSET:
            field_dict["ovh_end_point"] = ovh_end_point
        if pleskxml_user is not UNSET:
            field_dict["pleskxml_user"] = pleskxml_user
        if pleskxml_pass is not UNSET:
            field_dict["pleskxml_pass"] = pleskxml_pass
        if pleskxml_uri is not UNSET:
            field_dict["pleskxml_uri"] = pleskxml_uri
        if pointhq_key is not UNSET:
            field_dict["pointhq_key"] = pointhq_key
        if pointhq_email is not UNSET:
            field_dict["pointhq_email"] = pointhq_email
        if porkbun_api_key is not UNSET:
            field_dict["porkbun_api_key"] = porkbun_api_key
        if porkbun_secret_api_key is not UNSET:
            field_dict["porkbun_secret_api_key"] = porkbun_secret_api_key
        if pdns_url is not UNSET:
            field_dict["pdns_url"] = pdns_url
        if pdns_serverid is not UNSET:
            field_dict["pdns_serverid"] = pdns_serverid
        if pdns_token is not UNSET:
            field_dict["pdns_token"] = pdns_token
        if pdns_ttl is not UNSET:
            field_dict["pdns_ttl"] = pdns_ttl
        if rackcorp_apiuuid is not UNSET:
            field_dict["rackcorp_apiuuid"] = rackcorp_apiuuid
        if rackcorp_apisecret is not UNSET:
            field_dict["rackcorp_apisecret"] = rackcorp_apisecret
        if rackspace_username is not UNSET:
            field_dict["rackspace_username"] = rackspace_username
        if rackspace_apikey is not UNSET:
            field_dict["rackspace_apikey"] = rackspace_apikey
        if rage4_username is not UNSET:
            field_dict["rage4_username"] = rage4_username
        if rage4_token is not UNSET:
            field_dict["rage4_token"] = rage4_token
        if rcode0_api_token is not UNSET:
            field_dict["rcode0_api_token"] = rcode0_api_token
        if rcode0_url is not UNSET:
            field_dict["rcode0_url"] = rcode0_url
        if rcode0_ttl is not UNSET:
            field_dict["rcode0_ttl"] = rcode0_ttl
        if regru_api_username is not UNSET:
            field_dict["regru_api_username"] = regru_api_username
        if regru_api_password is not UNSET:
            field_dict["regru_api_password"] = regru_api_password
        if scaleway_api_token is not UNSET:
            field_dict["scaleway_api_token"] = scaleway_api_token
        if schlundtech_user is not UNSET:
            field_dict["schlundtech_user"] = schlundtech_user
        if schlundtech_password is not UNSET:
            field_dict["schlundtech_password"] = schlundtech_password
        if sl_key is not UNSET:
            field_dict["sl_key"] = sl_key
        if selfhostdns_username is not UNSET:
            field_dict["selfhostdns_username"] = selfhostdns_username
        if selfhostdns_password is not UNSET:
            field_dict["selfhostdns_password"] = selfhostdns_password
        if selfhostdns_map is not UNSET:
            field_dict["selfhostdns_map"] = selfhostdns_map
        if servercow_api_username is not UNSET:
            field_dict["servercow_api_username"] = servercow_api_username
        if servercow_api_password is not UNSET:
            field_dict["servercow_api_password"] = servercow_api_password
        if simply_accountname is not UNSET:
            field_dict["simply_accountname"] = simply_accountname
        if simply_apikey is not UNSET:
            field_dict["simply_apikey"] = simply_apikey
        if simply_api is not UNSET:
            field_dict["simply_api"] = simply_api
        if tele3_key is not UNSET:
            field_dict["tele3_key"] = tele3_key
        if tele3_secret is not UNSET:
            field_dict["tele3_secret"] = tele3_secret
        if tencent_secretid is not UNSET:
            field_dict["tencent_secretid"] = tencent_secretid
        if tencent_secretkey is not UNSET:
            field_dict["tencent_secretkey"] = tencent_secretkey
        if udr_user is not UNSET:
            field_dict["udr_user"] = udr_user
        if udr_pass is not UNSET:
            field_dict["udr_pass"] = udr_pass
        if ultra_usr is not UNSET:
            field_dict["ultra_usr"] = ultra_usr
        if ultra_pwd is not UNSET:
            field_dict["ULTRA_PWD"] = ultra_pwd
        if uno_user is not UNSET:
            field_dict["uno_user"] = uno_user
        if uno_key is not UNSET:
            field_dict["uno_key"] = uno_key
        if variomedia_api_token is not UNSET:
            field_dict["variomedia_api_token"] = variomedia_api_token
        if veesp_user is not UNSET:
            field_dict["veesp_user"] = veesp_user
        if veesp_password is not UNSET:
            field_dict["veesp_password"] = veesp_password
        if vercel_token is not UNSET:
            field_dict["vercel_token"] = vercel_token
        if vscale_api_key is not UNSET:
            field_dict["vscale_api_key"] = vscale_api_key
        if vultr_api_key is not UNSET:
            field_dict["vultr_api_key"] = vultr_api_key
        if ws_apikey is not UNSET:
            field_dict["ws_apikey"] = ws_apikey
        if ws_apisecret is not UNSET:
            field_dict["ws_apisecret"] = ws_apisecret
        if west_username is not UNSET:
            field_dict["west_username"] = west_username
        if west_key is not UNSET:
            field_dict["west_key"] = west_key
        if world4you_username is not UNSET:
            field_dict["world4you_username"] = world4you_username
        if world4you_password is not UNSET:
            field_dict["world4you_password"] = world4you_password
        if pdd_token is not UNSET:
            field_dict["pdd_token"] = pdd_token
        if yc_zone_id is not UNSET:
            field_dict["yc_zone_id"] = yc_zone_id
        if yc_folder_id is not UNSET:
            field_dict["yc_folder_id"] = yc_folder_id
        if yc_sa_id is not UNSET:
            field_dict["yc_sa_id"] = yc_sa_id
        if yc_sa_key_id is not UNSET:
            field_dict["yc_sa_key_id"] = yc_sa_key_id
        if yc_sa_key_file_pem_b64 is not UNSET:
            field_dict["yc_sa_key_file_pem_b64"] = yc_sa_key_file_pem_b64
        if zm_key is not UNSET:
            field_dict["zm_key"] = zm_key
        if zone_username is not UNSET:
            field_dict["zone_username"] = zone_username
        if zone_key is not UNSET:
            field_dict["zone_key"] = zone_key
        if zilore_key is not UNSET:
            field_dict["zilore_key"] = zilore_key
        if technitium_server is not UNSET:
            field_dict["technitium_server"] = technitium_server
        if technitium_token is not UNSET:
            field_dict["technitium_token"] = technitium_token
        if anydnschallengealias is not UNSET:
            field_dict["anydnschallengealias"] = anydnschallengealias
        if anydnschallengedomain is not UNSET:
            field_dict["anydnschallengedomain"] = anydnschallengedomain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: ACMECertificateDomainStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ACMECertificateDomainStatus(_status)

        method = d.pop("method", UNSET)

        webrootfolder = d.pop("webrootfolder", UNSET)

        webrootftpftpserver = d.pop("webrootftpftpserver", UNSET)

        webrootftpusername = d.pop("webrootftpusername", UNSET)

        webrootftppassword = d.pop("webrootftppassword", UNSET)

        webrootftpfolder = d.pop("webrootftpfolder", UNSET)

        standaloneport = d.pop("standaloneport", UNSET)

        standaloneipv6 = d.pop("standaloneipv6", UNSET)

        standalonetlsport = d.pop("standalonetlsport", UNSET)

        nsupdate_server = d.pop("nsupdate_server", UNSET)

        nsupdate_keyname = d.pop("nsupdate_keyname", UNSET)

        _nsupdate_keyalgo = d.pop("nsupdate_keyalgo", UNSET)
        nsupdate_keyalgo: ACMECertificateDomainNsupdateKeyalgo | Unset
        if isinstance(_nsupdate_keyalgo, Unset):
            nsupdate_keyalgo = UNSET
        else:
            nsupdate_keyalgo = ACMECertificateDomainNsupdateKeyalgo(_nsupdate_keyalgo)

        nsupdate_key = d.pop("nsupdate_key", UNSET)

        nsupdate_zone = d.pop("nsupdate_zone", UNSET)

        one984hosting_username = d.pop("one984hosting_username", UNSET)

        one984hosting_password = d.pop("one984hosting_password", UNSET)

        acmeproxy_endpoint = d.pop("acmeproxy_endpoint", UNSET)

        acmeproxy_username = d.pop("acmeproxy_username", UNSET)

        acmeproxy_password = d.pop("acmeproxy_password", UNSET)

        acmedns_username = d.pop("acmedns_username", UNSET)

        acmedns_password = d.pop("acmedns_password", UNSET)

        acmedns_subdomain = d.pop("acmedns_subdomain", UNSET)

        acmedns_update_url = d.pop("acmedns_update_url", UNSET)

        active24_token = d.pop("active24_token", UNSET)

        akamai_host = d.pop("akamai_host", UNSET)

        akamai_access_token = d.pop("akamai_access_token", UNSET)

        akamai_client_token = d.pop("akamai_client_token", UNSET)

        akamai_client_secret = d.pop("akamai_client_secret", UNSET)

        ali_key = d.pop("ali_key", UNSET)

        ali_secret = d.pop("ali_secret", UNSET)

        kas_login = d.pop("kas_login", UNSET)

        kas_authtype = d.pop("kas_authtype", UNSET)

        kas_authdata = d.pop("kas_authdata", UNSET)

        ad_api_key = d.pop("ad_api_key", UNSET)

        anx_token = d.pop("anx_token", UNSET)

        af_api_username = d.pop("af_api_username", UNSET)

        af_api_password = d.pop("af_api_password", UNSET)

        arvan_token = d.pop("arvan_token", UNSET)

        aurora_key = d.pop("aurora_key", UNSET)

        aurora_secret = d.pop("aurora_secret", UNSET)

        autodns_user = d.pop("autodns_user", UNSET)

        autodns_password = d.pop("autodns_password", UNSET)

        autodns_context = d.pop("autodns_context", UNSET)

        aws_access_key_id = d.pop("aws_access_key_id", UNSET)

        aws_secret_access_key = d.pop("aws_secret_access_key", UNSET)

        aws_dns_slowrate = d.pop("aws_dns_slowrate", UNSET)

        azion_email = d.pop("azion_email", UNSET)

        azion_password = d.pop("azion_password", UNSET)

        azuredns_subscriptionid = d.pop("azuredns_subscriptionid", UNSET)

        azuredns_tenantid = d.pop("azuredns_tenantid", UNSET)

        azuredns_appid = d.pop("azuredns_appid", UNSET)

        azuredns_clientsecret = d.pop("azuredns_clientsecret", UNSET)

        bookmyname_username = d.pop("bookmyname_username", UNSET)

        bookmyname_password = d.pop("bookmyname_password", UNSET)

        bunny_api_key = d.pop("bunny_api_key", UNSET)

        clouddns_email = d.pop("clouddns_email", UNSET)

        clouddns_client_id = d.pop("clouddns_client_id", UNSET)

        clouddns_password = d.pop("clouddns_password", UNSET)

        cloudns_auth_id = d.pop("cloudns_auth_id", UNSET)

        cloudns_sub_auth_id = d.pop("cloudns_sub_auth_id", UNSET)

        cloudns_auth_password = d.pop("cloudns_auth_password", UNSET)

        cf_key = d.pop("cf_key", UNSET)

        cf_email = d.pop("cf_email", UNSET)

        cf_token = d.pop("cf_token", UNSET)

        cf_account_id = d.pop("cf_account_id", UNSET)

        cf_zone_id = d.pop("cf_zone_id", UNSET)

        conoha_username = d.pop("conoha_username", UNSET)

        conoha_password = d.pop("conoha_password", UNSET)

        conoha_tenantid = d.pop("conoha_tenantid", UNSET)

        conoha_identityserviceapi = d.pop("conoha_identityserviceapi", UNSET)

        constellix_key = d.pop("constellix_key", UNSET)

        constellix_secret = d.pop("constellix_secret", UNSET)

        cpanel_username = d.pop("cpanel_username", UNSET)

        cpanel_apitoken = d.pop("cpanel_apitoken", UNSET)

        cpanel_hostname = d.pop("cpanel_hostname", UNSET)

        cn_user = d.pop("cn_user", UNSET)

        cn_password = d.pop("cn_password", UNSET)

        curanet_authclientid = d.pop("curanet_authclientid", UNSET)

        curanet_authsecret = d.pop("curanet_authsecret", UNSET)

        cy_username = d.pop("cy_username", UNSET)

        cy_password = d.pop("cy_password", UNSET)

        ddnss_token = d.pop("ddnss_token", UNSET)

        dedyn_token = d.pop("dedyn_token", UNSET)

        dedyn_name = d.pop("dedyn_name", UNSET)

        do_api_key = d.pop("do_api_key", UNSET)

        da_api = d.pop("da_api", UNSET)

        da_api_insecure = d.pop("da_api_insecure", UNSET)

        dnsexit_api_key = d.pop("dnsexit_api_key", UNSET)

        dnsexit_auth_user = d.pop("dnsexit_auth_user", UNSET)

        dnsexit_auth_pass = d.pop("dnsexit_auth_pass", UNSET)

        dnshome_subdomain = d.pop("dnshome_subdomain", UNSET)

        dnshome_subdomainpassword = d.pop("dnshome_subdomainpassword", UNSET)

        dnsimple_oauth_token = d.pop("dnsimple_oauth_token", UNSET)

        me_key = d.pop("me_key", UNSET)

        me_secret = d.pop("me_secret", UNSET)

        dnsservices_username = d.pop("dnsservices_username", UNSET)

        dnsservices_password = d.pop("dnsservices_password", UNSET)

        do_letoken = d.pop("do_letoken", UNSET)

        do_pid = d.pop("do_pid", UNSET)

        do_pw = d.pop("do_pw", UNSET)

        domeneshop_token = d.pop("domeneshop_token", UNSET)

        domeneshop_secret = d.pop("domeneshop_secret", UNSET)

        dp_id = d.pop("dp_id", UNSET)

        dp_key = d.pop("dp_key", UNSET)

        dpi_id = d.pop("dpi_id", UNSET)

        dpi_key = d.pop("dpi_key", UNSET)

        dh_api_key = d.pop("dh_api_key", UNSET)

        duckdns_token = d.pop("duckdns_token", UNSET)

        dd_api_user = d.pop("dd_api_user", UNSET)

        dd_api_key = d.pop("dd_api_key", UNSET)

        dyn_customer = d.pop("dyn_customer", UNSET)

        dyn_username = d.pop("dyn_username", UNSET)

        dyn_password = d.pop("dyn_password", UNSET)

        df_user = d.pop("df_user", UNSET)

        df_password = d.pop("df_password", UNSET)

        dynu_clientid = d.pop("dynu_clientid", UNSET)

        dynu_secret = d.pop("dynu_secret", UNSET)

        easydns_key = d.pop("easydns_key", UNSET)

        easydns_token = d.pop("easydns_token", UNSET)

        euserv_username = d.pop("euserv_username", UNSET)

        euserv_password = d.pop("euserv_password", UNSET)

        exoscale_api_key = d.pop("exoscale_api_key", UNSET)

        exoscale_secret_key = d.pop("exoscale_secret_key", UNSET)

        fornex_api_key = d.pop("fornex_api_key", UNSET)

        freedns_user = d.pop("freedns_user", UNSET)

        freedns_password = d.pop("freedns_password", UNSET)

        gandi_livedns_key = d.pop("gandi_livedns_key", UNSET)

        gcore_key = d.pop("gcore_key", UNSET)

        geoscaling_username = d.pop("geoscaling_username", UNSET)

        geoscaling_password = d.pop("geoscaling_password", UNSET)

        gd_key = d.pop("gd_key", UNSET)

        gd_secret = d.pop("gd_secret", UNSET)

        googledomains_access_token = d.pop("googledomains_access_token", UNSET)

        googledomains_zone = d.pop("googledomains_zone", UNSET)

        hetzner_token = d.pop("hetzner_token", UNSET)

        hexonet_login = d.pop("hexonet_login", UNSET)

        hexonet_password = d.pop("hexonet_password", UNSET)

        huaweicloud_username = d.pop("huaweicloud_username", UNSET)

        huaweicloud_password = d.pop("huaweicloud_password", UNSET)

        huaweicloud_domainname = d.pop("huaweicloud_domainname", UNSET)

        he_username = d.pop("he_username", UNSET)

        he_password = d.pop("he_password", UNSET)

        hostingde_apikey = d.pop("hostingde_apikey", UNSET)

        hostingde_endpoint = d.pop("hostingde_endpoint", UNSET)

        infoblox_creds = d.pop("infoblox_creds", UNSET)

        infoblox_server = d.pop("infoblox_server", UNSET)

        infoblox_view = d.pop("infoblox_view", UNSET)

        infomaniak_api_token = d.pop("infomaniak_api_token", UNSET)

        default_infomaniak_api_url = d.pop("default_infomaniak_api_url", UNSET)

        infomaniak_ttl = d.pop("infomaniak_ttl", UNSET)

        ionos_prefix = d.pop("ionos_prefix", UNSET)

        ionos_secret = d.pop("ionos_secret", UNSET)

        ipv64_token = d.pop("ipv64_token", UNSET)

        internetbs_api_key = d.pop("internetbs_api_key", UNSET)

        internetbs_api_password = d.pop("internetbs_api_password", UNSET)

        inwx_username = d.pop("inwx_username", UNSET)

        inwx_password = d.pop("inwx_password", UNSET)

        inwx_shared_secret = d.pop("inwx_shared_secret", UNSET)

        ispc_user = d.pop("ispc_user", UNSET)

        ispc_password = d.pop("ispc_password", UNSET)

        ispc_api = d.pop("ispc_api", UNSET)

        ispc_api_insecure = d.pop("ispc_api_insecure", UNSET)

        jd_access_key_id = d.pop("jd_access_key_id", UNSET)

        jd_access_key_secret = d.pop("jd_access_key_secret", UNSET)

        jd_region = d.pop("jd_region", UNSET)

        joker_username = d.pop("joker_username", UNSET)

        joker_password = d.pop("joker_password", UNSET)

        kappernetdns_key = d.pop("kappernetdns_key", UNSET)

        kappernetdns_secret = d.pop("kappernetdns_secret", UNSET)

        kinghost_username = d.pop("kinghost_username", UNSET)

        kinghost_password = d.pop("kinghost_password", UNSET)

        knot_server = d.pop("knot_server", UNSET)

        knot_key = d.pop("knot_key", UNSET)

        la_id = d.pop("la_id", UNSET)

        la_key = d.pop("la_key", UNSET)

        lsw_key = d.pop("lsw_key", UNSET)

        limacity_apikey = d.pop("limacity_apikey", UNSET)

        linode_api_key = d.pop("linode_api_key", UNSET)

        linode_v4_api_key = d.pop("linode_v4_api_key", UNSET)

        loopia_user = d.pop("loopia_user", UNSET)

        loopia_password = d.pop("loopia_password", UNSET)

        lua_key = d.pop("lua_key", UNSET)

        lua_email = d.pop("lua_email", UNSET)

        miab_username = d.pop("miab_username", UNSET)

        miab_password = d.pop("miab_password", UNSET)

        miab_server = d.pop("miab_server", UNSET)

        misaka_key = d.pop("misaka_key", UNSET)

        mydnsjp_masterid = d.pop("mydnsjp_masterid", UNSET)

        mydnsjp_password = d.pop("mydnsjp_password", UNSET)

        mb_ak = d.pop("mb_ak", UNSET)

        mb_as = d.pop("mb_as", UNSET)

        namecom_username = d.pop("namecom_username", UNSET)

        namecom_token = d.pop("namecom_token", UNSET)

        namecheap_api_key = d.pop("namecheap_api_key", UNSET)

        namecheap_username = d.pop("namecheap_username", UNSET)

        nm_user = d.pop("nm_user", UNSET)

        nm_sha256 = d.pop("nm_sha256", UNSET)

        nanelo_token = d.pop("nanelo_token", UNSET)

        nederhost_key = d.pop("nederhost_key", UNSET)

        namesilo_key = d.pop("namesilo_key", UNSET)

        neodigit_api_token = d.pop("neodigit_api_token", UNSET)

        nc_apikey = d.pop("nc_apikey", UNSET)

        nc_apipw = d.pop("nc_apipw", UNSET)

        nc_cid = d.pop("nc_cid", UNSET)

        netlify_access_token = d.pop("netlify_access_token", UNSET)

        nic_clientid = d.pop("nic_clientid", UNSET)

        nic_clientsecret = d.pop("nic_clientsecret", UNSET)

        nic_username = d.pop("nic_username", UNSET)

        nic_password = d.pop("nic_password", UNSET)

        ns1_key = d.pop("ns1_key", UNSET)

        nw_api_token = d.pop("nw_api_token", UNSET)

        _nw_api_endpoint = d.pop("nw_api_endpoint", UNSET)
        nw_api_endpoint: ACMECertificateDomainNwApiEndpoint | Unset
        if isinstance(_nw_api_endpoint, Unset):
            nw_api_endpoint = UNSET
        else:
            nw_api_endpoint = ACMECertificateDomainNwApiEndpoint(_nw_api_endpoint)

        onecom_user = d.pop("onecom_user", UNSET)

        onecom_password = d.pop("onecom_password", UNSET)

        online_api_key = d.pop("online_api_key", UNSET)

        oci_cli_tenancy = d.pop("oci_cli_tenancy", UNSET)

        oci_cli_user = d.pop("oci_cli_user", UNSET)

        oci_cli_region = d.pop("oci_cli_region", UNSET)

        oci_cli_key = d.pop("oci_cli_key", UNSET)

        openprovider_user = d.pop("openprovider_user", UNSET)

        openprovider_passwordhash = d.pop("openprovider_passwordhash", UNSET)

        ovh_ak = d.pop("ovh_ak", UNSET)

        ovh_as = d.pop("ovh_as", UNSET)

        ovh_ck = d.pop("ovh_ck", UNSET)

        _ovh_end_point = d.pop("ovh_end_point", UNSET)
        ovh_end_point: ACMECertificateDomainOvhEndPoint | Unset
        if isinstance(_ovh_end_point, Unset):
            ovh_end_point = UNSET
        else:
            ovh_end_point = ACMECertificateDomainOvhEndPoint(_ovh_end_point)

        pleskxml_user = d.pop("pleskxml_user", UNSET)

        pleskxml_pass = d.pop("pleskxml_pass", UNSET)

        pleskxml_uri = d.pop("pleskxml_uri", UNSET)

        pointhq_key = d.pop("pointhq_key", UNSET)

        pointhq_email = d.pop("pointhq_email", UNSET)

        porkbun_api_key = d.pop("porkbun_api_key", UNSET)

        porkbun_secret_api_key = d.pop("porkbun_secret_api_key", UNSET)

        pdns_url = d.pop("pdns_url", UNSET)

        pdns_serverid = d.pop("pdns_serverid", UNSET)

        pdns_token = d.pop("pdns_token", UNSET)

        pdns_ttl = d.pop("pdns_ttl", UNSET)

        rackcorp_apiuuid = d.pop("rackcorp_apiuuid", UNSET)

        rackcorp_apisecret = d.pop("rackcorp_apisecret", UNSET)

        rackspace_username = d.pop("rackspace_username", UNSET)

        rackspace_apikey = d.pop("rackspace_apikey", UNSET)

        rage4_username = d.pop("rage4_username", UNSET)

        rage4_token = d.pop("rage4_token", UNSET)

        rcode0_api_token = d.pop("rcode0_api_token", UNSET)

        rcode0_url = d.pop("rcode0_url", UNSET)

        rcode0_ttl = d.pop("rcode0_ttl", UNSET)

        regru_api_username = d.pop("regru_api_username", UNSET)

        regru_api_password = d.pop("regru_api_password", UNSET)

        scaleway_api_token = d.pop("scaleway_api_token", UNSET)

        schlundtech_user = d.pop("schlundtech_user", UNSET)

        schlundtech_password = d.pop("schlundtech_password", UNSET)

        sl_key = d.pop("sl_key", UNSET)

        selfhostdns_username = d.pop("selfhostdns_username", UNSET)

        selfhostdns_password = d.pop("selfhostdns_password", UNSET)

        selfhostdns_map = d.pop("selfhostdns_map", UNSET)

        servercow_api_username = d.pop("servercow_api_username", UNSET)

        servercow_api_password = d.pop("servercow_api_password", UNSET)

        simply_accountname = d.pop("simply_accountname", UNSET)

        simply_apikey = d.pop("simply_apikey", UNSET)

        simply_api = d.pop("simply_api", UNSET)

        tele3_key = d.pop("tele3_key", UNSET)

        tele3_secret = d.pop("tele3_secret", UNSET)

        tencent_secretid = d.pop("tencent_secretid", UNSET)

        tencent_secretkey = d.pop("tencent_secretkey", UNSET)

        udr_user = d.pop("udr_user", UNSET)

        udr_pass = d.pop("udr_pass", UNSET)

        ultra_usr = d.pop("ultra_usr", UNSET)

        ultra_pwd = d.pop("ULTRA_PWD", UNSET)

        uno_user = d.pop("uno_user", UNSET)

        uno_key = d.pop("uno_key", UNSET)

        variomedia_api_token = d.pop("variomedia_api_token", UNSET)

        veesp_user = d.pop("veesp_user", UNSET)

        veesp_password = d.pop("veesp_password", UNSET)

        vercel_token = d.pop("vercel_token", UNSET)

        vscale_api_key = d.pop("vscale_api_key", UNSET)

        vultr_api_key = d.pop("vultr_api_key", UNSET)

        ws_apikey = d.pop("ws_apikey", UNSET)

        ws_apisecret = d.pop("ws_apisecret", UNSET)

        west_username = d.pop("west_username", UNSET)

        west_key = d.pop("west_key", UNSET)

        world4you_username = d.pop("world4you_username", UNSET)

        world4you_password = d.pop("world4you_password", UNSET)

        pdd_token = d.pop("pdd_token", UNSET)

        yc_zone_id = d.pop("yc_zone_id", UNSET)

        yc_folder_id = d.pop("yc_folder_id", UNSET)

        yc_sa_id = d.pop("yc_sa_id", UNSET)

        yc_sa_key_id = d.pop("yc_sa_key_id", UNSET)

        yc_sa_key_file_pem_b64 = d.pop("yc_sa_key_file_pem_b64", UNSET)

        zm_key = d.pop("zm_key", UNSET)

        zone_username = d.pop("zone_username", UNSET)

        zone_key = d.pop("zone_key", UNSET)

        zilore_key = d.pop("zilore_key", UNSET)

        technitium_server = d.pop("technitium_server", UNSET)

        technitium_token = d.pop("technitium_token", UNSET)

        anydnschallengealias = d.pop("anydnschallengealias", UNSET)

        anydnschallengedomain = d.pop("anydnschallengedomain", UNSET)

        acme_certificate_domain = cls(
            name=name,
            status=status,
            method=method,
            webrootfolder=webrootfolder,
            webrootftpftpserver=webrootftpftpserver,
            webrootftpusername=webrootftpusername,
            webrootftppassword=webrootftppassword,
            webrootftpfolder=webrootftpfolder,
            standaloneport=standaloneport,
            standaloneipv6=standaloneipv6,
            standalonetlsport=standalonetlsport,
            nsupdate_server=nsupdate_server,
            nsupdate_keyname=nsupdate_keyname,
            nsupdate_keyalgo=nsupdate_keyalgo,
            nsupdate_key=nsupdate_key,
            nsupdate_zone=nsupdate_zone,
            one984hosting_username=one984hosting_username,
            one984hosting_password=one984hosting_password,
            acmeproxy_endpoint=acmeproxy_endpoint,
            acmeproxy_username=acmeproxy_username,
            acmeproxy_password=acmeproxy_password,
            acmedns_username=acmedns_username,
            acmedns_password=acmedns_password,
            acmedns_subdomain=acmedns_subdomain,
            acmedns_update_url=acmedns_update_url,
            active24_token=active24_token,
            akamai_host=akamai_host,
            akamai_access_token=akamai_access_token,
            akamai_client_token=akamai_client_token,
            akamai_client_secret=akamai_client_secret,
            ali_key=ali_key,
            ali_secret=ali_secret,
            kas_login=kas_login,
            kas_authtype=kas_authtype,
            kas_authdata=kas_authdata,
            ad_api_key=ad_api_key,
            anx_token=anx_token,
            af_api_username=af_api_username,
            af_api_password=af_api_password,
            arvan_token=arvan_token,
            aurora_key=aurora_key,
            aurora_secret=aurora_secret,
            autodns_user=autodns_user,
            autodns_password=autodns_password,
            autodns_context=autodns_context,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_dns_slowrate=aws_dns_slowrate,
            azion_email=azion_email,
            azion_password=azion_password,
            azuredns_subscriptionid=azuredns_subscriptionid,
            azuredns_tenantid=azuredns_tenantid,
            azuredns_appid=azuredns_appid,
            azuredns_clientsecret=azuredns_clientsecret,
            bookmyname_username=bookmyname_username,
            bookmyname_password=bookmyname_password,
            bunny_api_key=bunny_api_key,
            clouddns_email=clouddns_email,
            clouddns_client_id=clouddns_client_id,
            clouddns_password=clouddns_password,
            cloudns_auth_id=cloudns_auth_id,
            cloudns_sub_auth_id=cloudns_sub_auth_id,
            cloudns_auth_password=cloudns_auth_password,
            cf_key=cf_key,
            cf_email=cf_email,
            cf_token=cf_token,
            cf_account_id=cf_account_id,
            cf_zone_id=cf_zone_id,
            conoha_username=conoha_username,
            conoha_password=conoha_password,
            conoha_tenantid=conoha_tenantid,
            conoha_identityserviceapi=conoha_identityserviceapi,
            constellix_key=constellix_key,
            constellix_secret=constellix_secret,
            cpanel_username=cpanel_username,
            cpanel_apitoken=cpanel_apitoken,
            cpanel_hostname=cpanel_hostname,
            cn_user=cn_user,
            cn_password=cn_password,
            curanet_authclientid=curanet_authclientid,
            curanet_authsecret=curanet_authsecret,
            cy_username=cy_username,
            cy_password=cy_password,
            ddnss_token=ddnss_token,
            dedyn_token=dedyn_token,
            dedyn_name=dedyn_name,
            do_api_key=do_api_key,
            da_api=da_api,
            da_api_insecure=da_api_insecure,
            dnsexit_api_key=dnsexit_api_key,
            dnsexit_auth_user=dnsexit_auth_user,
            dnsexit_auth_pass=dnsexit_auth_pass,
            dnshome_subdomain=dnshome_subdomain,
            dnshome_subdomainpassword=dnshome_subdomainpassword,
            dnsimple_oauth_token=dnsimple_oauth_token,
            me_key=me_key,
            me_secret=me_secret,
            dnsservices_username=dnsservices_username,
            dnsservices_password=dnsservices_password,
            do_letoken=do_letoken,
            do_pid=do_pid,
            do_pw=do_pw,
            domeneshop_token=domeneshop_token,
            domeneshop_secret=domeneshop_secret,
            dp_id=dp_id,
            dp_key=dp_key,
            dpi_id=dpi_id,
            dpi_key=dpi_key,
            dh_api_key=dh_api_key,
            duckdns_token=duckdns_token,
            dd_api_user=dd_api_user,
            dd_api_key=dd_api_key,
            dyn_customer=dyn_customer,
            dyn_username=dyn_username,
            dyn_password=dyn_password,
            df_user=df_user,
            df_password=df_password,
            dynu_clientid=dynu_clientid,
            dynu_secret=dynu_secret,
            easydns_key=easydns_key,
            easydns_token=easydns_token,
            euserv_username=euserv_username,
            euserv_password=euserv_password,
            exoscale_api_key=exoscale_api_key,
            exoscale_secret_key=exoscale_secret_key,
            fornex_api_key=fornex_api_key,
            freedns_user=freedns_user,
            freedns_password=freedns_password,
            gandi_livedns_key=gandi_livedns_key,
            gcore_key=gcore_key,
            geoscaling_username=geoscaling_username,
            geoscaling_password=geoscaling_password,
            gd_key=gd_key,
            gd_secret=gd_secret,
            googledomains_access_token=googledomains_access_token,
            googledomains_zone=googledomains_zone,
            hetzner_token=hetzner_token,
            hexonet_login=hexonet_login,
            hexonet_password=hexonet_password,
            huaweicloud_username=huaweicloud_username,
            huaweicloud_password=huaweicloud_password,
            huaweicloud_domainname=huaweicloud_domainname,
            he_username=he_username,
            he_password=he_password,
            hostingde_apikey=hostingde_apikey,
            hostingde_endpoint=hostingde_endpoint,
            infoblox_creds=infoblox_creds,
            infoblox_server=infoblox_server,
            infoblox_view=infoblox_view,
            infomaniak_api_token=infomaniak_api_token,
            default_infomaniak_api_url=default_infomaniak_api_url,
            infomaniak_ttl=infomaniak_ttl,
            ionos_prefix=ionos_prefix,
            ionos_secret=ionos_secret,
            ipv64_token=ipv64_token,
            internetbs_api_key=internetbs_api_key,
            internetbs_api_password=internetbs_api_password,
            inwx_username=inwx_username,
            inwx_password=inwx_password,
            inwx_shared_secret=inwx_shared_secret,
            ispc_user=ispc_user,
            ispc_password=ispc_password,
            ispc_api=ispc_api,
            ispc_api_insecure=ispc_api_insecure,
            jd_access_key_id=jd_access_key_id,
            jd_access_key_secret=jd_access_key_secret,
            jd_region=jd_region,
            joker_username=joker_username,
            joker_password=joker_password,
            kappernetdns_key=kappernetdns_key,
            kappernetdns_secret=kappernetdns_secret,
            kinghost_username=kinghost_username,
            kinghost_password=kinghost_password,
            knot_server=knot_server,
            knot_key=knot_key,
            la_id=la_id,
            la_key=la_key,
            lsw_key=lsw_key,
            limacity_apikey=limacity_apikey,
            linode_api_key=linode_api_key,
            linode_v4_api_key=linode_v4_api_key,
            loopia_user=loopia_user,
            loopia_password=loopia_password,
            lua_key=lua_key,
            lua_email=lua_email,
            miab_username=miab_username,
            miab_password=miab_password,
            miab_server=miab_server,
            misaka_key=misaka_key,
            mydnsjp_masterid=mydnsjp_masterid,
            mydnsjp_password=mydnsjp_password,
            mb_ak=mb_ak,
            mb_as=mb_as,
            namecom_username=namecom_username,
            namecom_token=namecom_token,
            namecheap_api_key=namecheap_api_key,
            namecheap_username=namecheap_username,
            nm_user=nm_user,
            nm_sha256=nm_sha256,
            nanelo_token=nanelo_token,
            nederhost_key=nederhost_key,
            namesilo_key=namesilo_key,
            neodigit_api_token=neodigit_api_token,
            nc_apikey=nc_apikey,
            nc_apipw=nc_apipw,
            nc_cid=nc_cid,
            netlify_access_token=netlify_access_token,
            nic_clientid=nic_clientid,
            nic_clientsecret=nic_clientsecret,
            nic_username=nic_username,
            nic_password=nic_password,
            ns1_key=ns1_key,
            nw_api_token=nw_api_token,
            nw_api_endpoint=nw_api_endpoint,
            onecom_user=onecom_user,
            onecom_password=onecom_password,
            online_api_key=online_api_key,
            oci_cli_tenancy=oci_cli_tenancy,
            oci_cli_user=oci_cli_user,
            oci_cli_region=oci_cli_region,
            oci_cli_key=oci_cli_key,
            openprovider_user=openprovider_user,
            openprovider_passwordhash=openprovider_passwordhash,
            ovh_ak=ovh_ak,
            ovh_as=ovh_as,
            ovh_ck=ovh_ck,
            ovh_end_point=ovh_end_point,
            pleskxml_user=pleskxml_user,
            pleskxml_pass=pleskxml_pass,
            pleskxml_uri=pleskxml_uri,
            pointhq_key=pointhq_key,
            pointhq_email=pointhq_email,
            porkbun_api_key=porkbun_api_key,
            porkbun_secret_api_key=porkbun_secret_api_key,
            pdns_url=pdns_url,
            pdns_serverid=pdns_serverid,
            pdns_token=pdns_token,
            pdns_ttl=pdns_ttl,
            rackcorp_apiuuid=rackcorp_apiuuid,
            rackcorp_apisecret=rackcorp_apisecret,
            rackspace_username=rackspace_username,
            rackspace_apikey=rackspace_apikey,
            rage4_username=rage4_username,
            rage4_token=rage4_token,
            rcode0_api_token=rcode0_api_token,
            rcode0_url=rcode0_url,
            rcode0_ttl=rcode0_ttl,
            regru_api_username=regru_api_username,
            regru_api_password=regru_api_password,
            scaleway_api_token=scaleway_api_token,
            schlundtech_user=schlundtech_user,
            schlundtech_password=schlundtech_password,
            sl_key=sl_key,
            selfhostdns_username=selfhostdns_username,
            selfhostdns_password=selfhostdns_password,
            selfhostdns_map=selfhostdns_map,
            servercow_api_username=servercow_api_username,
            servercow_api_password=servercow_api_password,
            simply_accountname=simply_accountname,
            simply_apikey=simply_apikey,
            simply_api=simply_api,
            tele3_key=tele3_key,
            tele3_secret=tele3_secret,
            tencent_secretid=tencent_secretid,
            tencent_secretkey=tencent_secretkey,
            udr_user=udr_user,
            udr_pass=udr_pass,
            ultra_usr=ultra_usr,
            ultra_pwd=ultra_pwd,
            uno_user=uno_user,
            uno_key=uno_key,
            variomedia_api_token=variomedia_api_token,
            veesp_user=veesp_user,
            veesp_password=veesp_password,
            vercel_token=vercel_token,
            vscale_api_key=vscale_api_key,
            vultr_api_key=vultr_api_key,
            ws_apikey=ws_apikey,
            ws_apisecret=ws_apisecret,
            west_username=west_username,
            west_key=west_key,
            world4you_username=world4you_username,
            world4you_password=world4you_password,
            pdd_token=pdd_token,
            yc_zone_id=yc_zone_id,
            yc_folder_id=yc_folder_id,
            yc_sa_id=yc_sa_id,
            yc_sa_key_id=yc_sa_key_id,
            yc_sa_key_file_pem_b64=yc_sa_key_file_pem_b64,
            zm_key=zm_key,
            zone_username=zone_username,
            zone_key=zone_key,
            zilore_key=zilore_key,
            technitium_server=technitium_server,
            technitium_token=technitium_token,
            anydnschallengealias=anydnschallengealias,
            anydnschallengedomain=anydnschallengedomain,
        )

        acme_certificate_domain.additional_properties = d
        return acme_certificate_domain

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
