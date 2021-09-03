# Copyright (C) 2021 SUSE, LLC
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
from ceph.deployment.hostspec import HostSpec
from typing import Any, Dict, List, cast
from mgr_module import MgrModule
from bubbles.backend.controllers.orch import OrchController


class HostsController:
    _mgr: MgrModule
    _orch: OrchController

    def __init__(self, mgr: MgrModule, orch: OrchController) -> None:
        self._mgr = mgr
        self._orch = orch

    def list(self) -> Dict[str, Any]:
        hostsreq = self._orch.client.get_hosts()
        hosts = cast(List[HostSpec], hostsreq.result)
        hosts_map = {host.hostname: host.to_json() for host in hosts}

        return {
            "servers": self._mgr.list_servers(),
            "orch": hosts_map
        }
