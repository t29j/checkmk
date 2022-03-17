#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest

from testlib import on_time, get_value_store_fixture
from cmk.utils.type_defs import CheckPluginName
from cmk.base.api.agent_based import register
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    Metric,
    Result,
    Service,
    State,
)
from cmk.base.plugins.agent_based.agent_based_api.v1.type_defs import CheckResult, DiscoveryResult
from cmk.base.plugins.agent_based.fritz import (
    check_fritz_wan_if,
    discover_fritz_wan_if,
    parse_fritz,
    Section,
)
from cmk.base.plugins.agent_based.utils.interfaces import (
    CHECK_DEFAULT_PARAMETERS,
    DISCOVERY_DEFAULT_PARAMETERS,
)

from cmk.base.plugins.agent_based.utils import interfaces

value_store_fixture = get_value_store_fixture(interfaces)

_STRING_TABLE = [
    ["VersionOS", "137.06.83"],
    ["VersionDevice", "AVM", "FRITZ!Box", "7412", "(UI)"],
    ["NewVoipDNSServer1", "217.237.148.102"],
    ["NewDNSServer2", "217.237.151.115"],
    ["NewDNSServer1", "217.237.148.102"],
    ["NewVoipDNSServer2", "217.237.151.115"],
    ["NewIdleDisconnectTime", "0"],
    ["NewLayer1DownstreamMaxBitRate", "25088000"],
    ["NewWANAccessType", "DSL"],
    ["NewByteSendRate", "197"],
    ["NewPacketReceiveRate", "0"],
    ["NewConnectionStatus", "Connected"],
    ["NewRoutedBridgedModeBoth", "1"],
    ["NewUptime", "1"],
    ["NewTotalBytesReceived", "178074787"],
    ["NewPacketSendRate", "0"],
    ["NewPhysicalLinkStatus", "Up"],
    ["NewLinkStatus", "Up"],
    ["NewLayer1UpstreamMaxBitRate", "5056000"],
    ["NewTotalBytesSent", "40948982"],
    ["NewLastConnectionError", "ERROR_NONE"],
    ["NewAutoDisconnectTime", "0"],
    ["NewExternalIPAddress", "217.235.84.223"],
    ["NewLinkType", "PPPoE"],
    ["NewByteReceiveRate", "0"],
    ["NewUpnpControlEnabled", "1"],
]

_SECTION = {
    "NewAutoDisconnectTime": "0",
    "NewByteReceiveRate": "0",
    "NewByteSendRate": "197",
    "NewConnectionStatus": "Connected",
    "NewDNSServer1": "217.237.148.102",
    "NewDNSServer2": "217.237.151.115",
    "NewExternalIPAddress": "217.235.84.223",
    "NewIdleDisconnectTime": "0",
    "NewLastConnectionError": "ERROR_NONE",
    "NewLayer1DownstreamMaxBitRate": "25088000",
    "NewLayer1UpstreamMaxBitRate": "5056000",
    "NewLinkStatus": "Up",
    "NewLinkType": "PPPoE",
    "NewPacketReceiveRate": "0",
    "NewPacketSendRate": "0",
    "NewPhysicalLinkStatus": "Up",
    "NewRoutedBridgedModeBoth": "1",
    "NewTotalBytesReceived": "178074787",
    "NewTotalBytesSent": "40948982",
    "NewUpnpControlEnabled": "1",
    "NewUptime": "1",
    "NewVoipDNSServer1": "217.237.148.102",
    "NewVoipDNSServer2": "217.237.151.115",
    "NewWANAccessType": "DSL",
    "VersionDevice": "AVM FRITZ!Box 7412 (UI)",
    "VersionOS": "137.06.83",
}


def test_parse_fritz() -> None:
    assert parse_fritz(_STRING_TABLE) == _SECTION


@pytest.mark.parametrize(
    [
        "section",
        "expected_result",
    ],
    [
        pytest.param(
            _SECTION,
            [
                Service(
                    item="0",
                    parameters={
                        "discovered_oper_status": ["1"],
                        "discovered_speed": 25088000,
                    },
                ),
            ],
            id="standard case",
        ),
        pytest.param(
            {},
            [],
            id="empty data",
        ),
    ],
)
def test_discover_fritz_wan_if(
    section: Section,
    expected_result: DiscoveryResult,
) -> None:
    assert (list(discover_fritz_wan_if(
        [DISCOVERY_DEFAULT_PARAMETERS],
        section,
    )) == expected_result)


@pytest.mark.parametrize(
    [
        "section",
        "expected_result",
    ],
    [
        pytest.param(
            _SECTION,
            [
                Result(
                    state=State.OK,
                    summary="[WAN]",
                ),
                Result(
                    state=State.OK,
                    summary="(up)",
                    details="Operational state: up",
                ),
                Result(
                    state=State.OK,
                    summary="Speed: 25.1 MBit/s",
                ),
            ],
            id="standard case",
        ),
    ],
)
@pytest.mark.usefixtures("value_store")
def test_check_fritz_wan_if(
    section: Section,
    expected_result: CheckResult,
) -> None:
    assert (list(check_fritz_wan_if(
        "0",
        CHECK_DEFAULT_PARAMETERS,
        section,
    )) == expected_result)


@pytest.mark.parametrize(
    [
        "section",
        "expected_result",
    ],
    [
        pytest.param(
            _SECTION,
            [Service()],
            id="standard case",
        ),
        pytest.param(
            {},
            [],
            id="empty data",
        ),
    ],
)
@pytest.mark.usefixtures("config_load_all_checks")
def test_discover_fritz_conn(
    section: Section,
    expected_result: DiscoveryResult,
) -> None:
    plugin = register.get_check_plugin(CheckPluginName("fritz_conn"))
    assert plugin
    assert list(plugin.discovery_function(section)) == expected_result


@pytest.mark.parametrize(
    [
        "section",
        "expected_result",
    ],
    [
        pytest.param(
            _SECTION,
            [
                Result(
                    state=State.OK,
                    summary="Status: Connected",
                ),
                Result(
                    state=State.OK,
                    summary="WAN IP Address: 217.235.84.223",
                ),
                Result(
                    state=State.OK,
                    summary="Up since Thu Mar 17 11:07:38 2022, uptime: 0:00:01",
                ),
                Metric(
                    "uptime",
                    1.0,
                ),
            ],
            id="standard case",
        ),
        pytest.param(
            {},
            [
                Result(
                    state=State.OK,
                    summary="Status: None",
                ),
                Result(
                    state=State.UNKNOWN,
                    summary="unhandled connection status",
                ),
                Result(
                    state=State.WARN,
                    notice="Not connected",
                ),
            ],
            id="empty data",
        ),
    ],
)
@pytest.mark.usefixtures("config_load_all_checks")
def test_check_fritz_conn(
    section: Section,
    expected_result: CheckResult,
) -> None:
    plugin = register.get_check_plugin(CheckPluginName("fritz_conn"))
    assert plugin
    with on_time(1647515259, "UTC"):
        assert list(plugin.check_function(
            params={},
            section=section,
        )) == expected_result


@pytest.mark.parametrize(
    [
        "section",
        "expected_result",
    ],
    [
        pytest.param(
            _SECTION,
            [Service()],
            id="standard case",
        ),
        pytest.param(
            {},
            [],
            id="empty data",
        ),
    ],
)
@pytest.mark.usefixtures("config_load_all_checks")
def test_discover_fritz_config(
    section: Section,
    expected_result: DiscoveryResult,
) -> None:
    plugin = register.get_check_plugin(CheckPluginName("fritz_config"))
    assert plugin
    assert list(plugin.discovery_function(section)) == expected_result


@pytest.mark.parametrize(
    [
        "section",
        "expected_result",
    ],
    [
        pytest.param(
            _SECTION,
            [
                Result(
                    state=State.OK,
                    summary=
                    "Auto Disconnect Time: 0, DNS-Server1: 217.237.148.102, DNS-Server2: 217.237.151.115, VoIP-DNS-Server1: 217.237.148.102, VoIP-DNS-Server2: 217.237.151.115, uPnP Config Enabled: 1",
                ),
            ],
            id="standard case",
        ),
        pytest.param(
            {},
            [
                Result(
                    state=State.UNKNOWN,
                    summary="Configuration info is missing",
                ),
            ],
            id="empty data",
        ),
    ],
)
@pytest.mark.usefixtures("config_load_all_checks")
def test_check_fritz_config(
    section: Section,
    expected_result: CheckResult,
) -> None:
    plugin = register.get_check_plugin(CheckPluginName("fritz_config"))
    assert plugin
    assert list(plugin.check_function(
        params={},
        section=section,
    )) == expected_result


@pytest.mark.parametrize(
    [
        "section",
        "expected_result",
    ],
    [
        pytest.param(
            _SECTION,
            [Service()],
            id="standard case",
        ),
        pytest.param(
            {},
            [],
            id="empty data",
        ),
    ],
)
@pytest.mark.usefixtures("config_load_all_checks")
def test_discover_fritz_link(
    section: Section,
    expected_result: DiscoveryResult,
) -> None:
    plugin = register.get_check_plugin(CheckPluginName("fritz_link"))
    assert plugin
    assert list(plugin.discovery_function(section)) == expected_result


@pytest.mark.parametrize(
    [
        "section",
        "expected_result",
    ],
    [
        pytest.param(
            _SECTION,
            [
                Result(
                    state=State.OK,
                    summary=
                    "Link Status: Up, Physical Link Status: Up, Link Type: PPPoE, WAN Access Type: DSL",
                ),
            ],
            id="standard case",
        ),
        pytest.param(
            {},
            [Result(
                state=State.UNKNOWN,
                summary="Link info is missing",
            )],
            id="empty data",
        ),
    ],
)
@pytest.mark.usefixtures("config_load_all_checks")
def test_check_fritz_link(
    section: Section,
    expected_result: CheckResult,
) -> None:
    plugin = register.get_check_plugin(CheckPluginName("fritz_link"))
    assert plugin
    assert list(plugin.check_function(
        params={},
        section=section,
    )) == expected_result
