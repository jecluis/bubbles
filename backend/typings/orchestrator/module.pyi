# type: ignore
import datetime
import enum
from ._interface import CLICommandMeta as CLICommandMeta, DaemonDescription as DaemonDescription, DaemonDescriptionStatus as DaemonDescriptionStatus, DeviceLightLoc as DeviceLightLoc, GenericSpec as GenericSpec, HostSpec as HostSpec, InventoryFilter as InventoryFilter, InventoryHost as InventoryHost, IscsiServiceSpec as IscsiServiceSpec, NFSServiceSpec as NFSServiceSpec, NoOrchestrator as NoOrchestrator, OrchestratorClientMixin as OrchestratorClientMixin, OrchestratorError as OrchestratorError, OrchestratorValidationError as OrchestratorValidationError, RGWSpec as RGWSpec, ServiceDescription as ServiceDescription, json_to_generic_spec as json_to_generic_spec, raise_if_exception as raise_if_exception
from ceph.deployment.inventory import Device as Device
from mgr_module import HandleCommandResult, MgrModule
from typing import Any, List, Optional

def nice_delta(now: datetime.datetime, t: Optional[datetime.datetime], suffix: str = ...) -> str: ...
def nice_bytes(v: Optional[int]) -> str: ...

class Format(enum.Enum):
    plain: str
    json: str
    json_pretty: str
    yaml: str

class ServiceType(enum.Enum):
    mon: str
    mgr: str
    rbd_mirror: str
    cephfs_mirror: str
    crash: str
    alertmanager: str
    grafana: str
    node_exporter: str
    prometheus: str
    mds: str
    rgw: str
    nfs: str
    iscsi: str
    cephadm_exporter: str

class ServiceAction(enum.Enum):
    start: str
    stop: str
    restart: str
    redeploy: str
    reconfig: str

class DaemonAction(enum.Enum):
    start: str
    stop: str
    restart: str
    reconfig: str

def to_format(what: Any, format: Format, many: bool, cls: Any) -> Any: ...
def generate_preview_tables(data: Any, osd_only: bool = ...) -> str: ...
def preview_table_osd(data: List) -> str: ...
def preview_table_services(data: List) -> str: ...

class OrchestratorCli(OrchestratorClientMixin, MgrModule, metaclass=CLICommandMeta):
    MODULE_OPTIONS: Any
    NATIVE_OPTIONS: List[dict]
    ident: Any
    fault: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def light_on(self, fault_ident: str, devid: str) -> HandleCommandResult: ...
    def light_off(self, fault_ident: str, devid: str, force: bool) -> HandleCommandResult: ...
    class DeviceLightEnable(enum.Enum):
        on: str
        off: str
    class DeviceLightType(enum.Enum):
        ident: str
        fault: str
    def daemon_add_misc(self, daemon_type: Optional[ServiceType] = ..., placement: Optional[str] = ..., inbuf: Optional[str] = ...) -> HandleCommandResult: ...
    def apply_misc(self, service_type: Optional[ServiceType] = ..., placement: Optional[str] = ..., dry_run: bool = ..., format: Format = ..., unmanaged: bool = ..., no_overwrite: bool = ..., inbuf: Optional[str] = ...) -> HandleCommandResult: ...
    def self_test(self) -> None: ...
