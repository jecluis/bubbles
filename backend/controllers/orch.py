# Copyright (C) 2021 SUSE, LLC
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
from mgr_module import MgrModule
from orchestrator import OrchestratorClientMixin


class OrchClient(OrchestratorClientMixin):
    def __init__(self, mgr: MgrModule) -> None:
        self.set_mgr(mgr)


class OrchController:
    _orch: OrchClient
    _mgr: MgrModule

    def __init__(self, mgr: MgrModule) -> None:
        self._mgr = mgr
        self._orch = OrchClient(mgr)

    @property
    def client(self) -> OrchClient:
        return self._orch
