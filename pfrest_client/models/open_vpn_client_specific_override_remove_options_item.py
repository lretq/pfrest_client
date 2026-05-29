from enum import Enum


class OpenVPNClientSpecificOverrideRemoveOptionsItem(str, Enum):
    REMOVE_BLOCKOUTSIDEDNS = "remove_blockoutsidedns"
    REMOVE_DNSDOMAIN = "remove_dnsdomain"
    REMOVE_DNSSERVERS = "remove_dnsservers"
    REMOVE_INACTIVE = "remove_inactive"
    REMOVE_IROUTE = "remove_iroute"
    REMOVE_NETBIOS_NTYPE = "remove_netbios_ntype"
    REMOVE_NETBIOS_SCOPE = "remove_netbios_scope"
    REMOVE_NTPSERVERS = "remove_ntpservers"
    REMOVE_PING = "remove_ping"
    REMOVE_PING_ACTION = "remove_ping_action"
    REMOVE_REDIRECT_GATEWAY = "remove_redirect_gateway"
    REMOVE_ROUTE = "remove_route"
    REMOVE_WINS = "remove_wins"

    def __str__(self) -> str:
        return str(self.value)
