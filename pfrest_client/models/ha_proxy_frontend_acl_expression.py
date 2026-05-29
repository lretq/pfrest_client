from enum import Enum


class HAProxyFrontendACLExpression(str, Enum):
    BACKENDSERVERCOUNT = "backendservercount"
    CUSTOM = "custom"
    HOST_CONTAINS = "host_contains"
    HOST_ENDS_WITH = "host_ends_with"
    HOST_MATCHES = "host_matches"
    HOST_REGEX = "host_regex"
    HOST_STARTS_WITH = "host_starts_with"
    PATH_CONTAINS = "path_contains"
    PATH_DIR = "path_dir"
    PATH_ENDS_WITH = "path_ends_with"
    PATH_MATCHES = "path_matches"
    PATH_REGEX = "path_regex"
    PATH_STARTS_WITH = "path_starts_with"
    SOURCE_IP = "source_ip"
    SSL_C_CA_COMMONNAME = "ssl_c_ca_commonname"
    SSL_C_VERIFY = "ssl_c_verify"
    SSL_C_VERIFY_CODE = "ssl_c_verify_code"
    SSL_SNI_CONTAINS = "ssl_sni_contains"
    SSL_SNI_ENDS_WITH = "ssl_sni_ends_with"
    SSL_SNI_MATCHES = "ssl_sni_matches"
    SSL_SNI_REGEX = "ssl_sni_regex"
    SSL_SNI_STARTS_WITH = "ssl_sni_starts_with"
    TRAFFIC_IS_HTTP = "traffic_is_http"
    TRAFFIC_IS_SSL = "traffic_is_ssl"
    URL_PARAMETER = "url_parameter"

    def __str__(self) -> str:
        return str(self.value)
