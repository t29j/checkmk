# Stubs for kubernetes.client.models.v1_job_spec (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1JobSpec:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    active_deadline_seconds: Any = ...
    backoff_limit: Any = ...
    completions: Any = ...
    manual_selector: Any = ...
    parallelism: Any = ...
    selector: Any = ...
    template: Any = ...
    ttl_seconds_after_finished: Any = ...
    def __init__(self, active_deadline_seconds: Optional[Any] = ..., backoff_limit: Optional[Any] = ..., completions: Optional[Any] = ..., manual_selector: Optional[Any] = ..., parallelism: Optional[Any] = ..., selector: Optional[Any] = ..., template: Optional[Any] = ..., ttl_seconds_after_finished: Optional[Any] = ...) -> None: ...
    @property
    def active_deadline_seconds(self): ...
    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds: Any) -> None: ...
    @property
    def backoff_limit(self): ...
    @backoff_limit.setter
    def backoff_limit(self, backoff_limit: Any) -> None: ...
    @property
    def completions(self): ...
    @completions.setter
    def completions(self, completions: Any) -> None: ...
    @property
    def manual_selector(self): ...
    @manual_selector.setter
    def manual_selector(self, manual_selector: Any) -> None: ...
    @property
    def parallelism(self): ...
    @parallelism.setter
    def parallelism(self, parallelism: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    @property
    def template(self): ...
    @template.setter
    def template(self, template: Any) -> None: ...
    @property
    def ttl_seconds_after_finished(self): ...
    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
