# Stubs for kubernetes.client.models.v1_flocker_volume_source (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1FlockerVolumeSource:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    dataset_name: Any = ...
    dataset_uuid: Any = ...
    def __init__(self, dataset_name: Optional[Any] = ..., dataset_uuid: Optional[Any] = ...) -> None: ...
    @property
    def dataset_name(self): ...
    @dataset_name.setter
    def dataset_name(self, dataset_name: Any) -> None: ...
    @property
    def dataset_uuid(self): ...
    @dataset_uuid.setter
    def dataset_uuid(self, dataset_uuid: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
