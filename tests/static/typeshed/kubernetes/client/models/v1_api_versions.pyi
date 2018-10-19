# Stubs for kubernetes.client.models.v1_api_versions (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1APIVersions:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    api_version: str = ...
    kind: str = ...
    server_address_by_client_cid_rs: Any = ...
    versions: Any = ...
    def __init__(self, api_version: Optional[Any] = ..., kind: Optional[Any] = ..., server_address_by_client_cid_rs: Optional[Any] = ..., versions: Optional[Any] = ...) -> None: ...
    @property
    def api_version(self) -> str: ...
    @api_version.setter
    def api_version(self, api_version: str) -> None: ...
    @property
    def kind(self) -> str: ...
    @kind.setter
    def kind(self, kind: str) -> None: ...
    @property
    def server_address_by_client_cid_rs(self): ...
    @server_address_by_client_cid_rs.setter
    def server_address_by_client_cid_rs(self, server_address_by_client_cid_rs: Any) -> None: ...
    @property
    def versions(self): ...
    @versions.setter
    def versions(self, versions: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
