# -*- coding: utf-8 -*-

UINT64_MAX = 2 ** 64 - 1
UINT64_MIN = 0

INT64_MAX = 2 ** 63 - 1
INT64_MIN = -(2 ** 63)

UINT256_MAX = 2 ** 256 - 1

# Deployed to Ropsten revival on 2017-08-18 from commit 01554102f0a52fc5aec3f41dc46d53017108b400
ROPSTEN_REGISTRY_ADDRESS = '7205a22f083a12d1b22ee89d7e892d23b1f1438a'
ROPSTEN_DISCOVERY_ADDRESS = '1ed4eab14a09ba2f334d9ed579a5ee4ae57aec45'

DISCOVERY_REGISTRATION_GAS = 500000

MINUTE_SEC = 60
MINUTE_MS = 60 * 1000

NETTINGCHANNEL_SETTLE_TIMEOUT_MIN = 6

# TODO: add this as an attribute of the transport class
UDP_MAX_MESSAGE_SIZE = 1200
