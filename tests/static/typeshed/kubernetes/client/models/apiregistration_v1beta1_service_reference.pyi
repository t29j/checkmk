# Stubs for kubernetes.client.models.apiregistration_v1beta1_service_reference (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ApiregistrationV1beta1ServiceReference:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    name: Any = ...
    namespace: Any = ...
    def __init__(self, name: Optional[Any] = ..., namespace: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def namespace(self): ...
    @namespace.setter
    def namespace(self, namespace: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
