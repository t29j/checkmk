# Stubs for kubernetes.client.models.v1beta1_daemon_set_spec (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1DaemonSetSpec:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    min_ready_seconds: Any = ...
    revision_history_limit: Any = ...
    selector: Any = ...
    template: Any = ...
    template_generation: Any = ...
    update_strategy: Any = ...
    def __init__(self, min_ready_seconds: Optional[Any] = ..., revision_history_limit: Optional[Any] = ..., selector: Optional[Any] = ..., template: Optional[Any] = ..., template_generation: Optional[Any] = ..., update_strategy: Optional[Any] = ...) -> None: ...
    @property
    def min_ready_seconds(self): ...
    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds: Any) -> None: ...
    @property
    def revision_history_limit(self): ...
    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    @property
    def template(self): ...
    @template.setter
    def template(self, template: Any) -> None: ...
    @property
    def template_generation(self): ...
    @template_generation.setter
    def template_generation(self, template_generation: Any) -> None: ...
    @property
    def update_strategy(self): ...
    @update_strategy.setter
    def update_strategy(self, update_strategy: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
