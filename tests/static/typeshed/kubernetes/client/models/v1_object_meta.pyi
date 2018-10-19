# Stubs for kubernetes.client.models.v1_object_meta (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Dict, Optional

class V1ObjectMeta:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    annotations: Any = ...
    cluster_name: Any = ...
    creation_timestamp: Any = ...
    deletion_grace_period_seconds: Any = ...
    deletion_timestamp: Any = ...
    finalizers: Any = ...
    generate_name: Any = ...
    generation: Any = ...
    initializers: Any = ...
    labels: Any = ...
    name: Any = ...
    namespace: Any = ...
    owner_references: Any = ...
    resource_version: Any = ...
    self_link: Any = ...
    uid: Any = ...
    def __init__(self, annotations: Optional[Any] = ..., cluster_name: Optional[Any] = ..., creation_timestamp: Optional[Any] = ..., deletion_grace_period_seconds: Optional[Any] = ..., deletion_timestamp: Optional[Any] = ..., finalizers: Optional[Any] = ..., generate_name: Optional[Any] = ..., generation: Optional[Any] = ..., initializers: Optional[Any] = ..., labels: Optional[Any] = ..., name: Optional[Any] = ..., namespace: Optional[Any] = ..., owner_references: Optional[Any] = ..., resource_version: Optional[Any] = ..., self_link: Optional[Any] = ..., uid: Optional[Any] = ...) -> None: ...
    @property
    def annotations(self) -> Optional[Dict[str, str]]: ...
    @annotations.setter
    def annotations(self, annotations: Optional[Dict[str, str]]) -> None: ...
    @property
    def cluster_name(self) -> Optional[str]: ...
    @cluster_name.setter
    def cluster_name(self, cluster_name: Optional[str]) -> None: ...
    @property
    def creation_timestamp(self): ...
    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp: Any) -> None: ...
    @property
    def deletion_grace_period_seconds(self): ...
    @deletion_grace_period_seconds.setter
    def deletion_grace_period_seconds(self, deletion_grace_period_seconds: Any) -> None: ...
    @property
    def deletion_timestamp(self): ...
    @deletion_timestamp.setter
    def deletion_timestamp(self, deletion_timestamp: Any) -> None: ...
    @property
    def finalizers(self): ...
    @finalizers.setter
    def finalizers(self, finalizers: Any) -> None: ...
    @property
    def generate_name(self): ...
    @generate_name.setter
    def generate_name(self, generate_name: Any) -> None: ...
    @property
    def generation(self): ...
    @generation.setter
    def generation(self, generation: Any) -> None: ...
    @property
    def initializers(self): ...
    @initializers.setter
    def initializers(self, initializers: Any) -> None: ...
    @property
    def labels(self): ...
    @labels.setter
    def labels(self, labels: Any) -> None: ...
    @property
    def name(self) -> Optional[str]: ...
    @name.setter
    def name(self, name: Optional[str]) -> None: ...
    @property
    def namespace(self): ...
    @namespace.setter
    def namespace(self, namespace: Any) -> None: ...
    @property
    def owner_references(self): ...
    @owner_references.setter
    def owner_references(self, owner_references: Any) -> None: ...
    @property
    def resource_version(self): ...
    @resource_version.setter
    def resource_version(self, resource_version: Any) -> None: ...
    @property
    def self_link(self): ...
    @self_link.setter
    def self_link(self, self_link: Any) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
