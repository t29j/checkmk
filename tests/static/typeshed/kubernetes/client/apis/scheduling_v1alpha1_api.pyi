# Stubs for kubernetes.client.apis.scheduling_v1alpha1_api (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..api_client import ApiClient
from typing import Any, Optional

class SchedulingV1alpha1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_priority_class(self, body: Any, **kwargs: Any): ...
    def create_priority_class_with_http_info(self, body: Any, **kwargs: Any): ...
    def delete_collection_priority_class(self, **kwargs: Any): ...
    def delete_collection_priority_class_with_http_info(self, **kwargs: Any): ...
    def delete_priority_class(self, name: Any, body: Any, **kwargs: Any): ...
    def delete_priority_class_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_priority_class(self, **kwargs: Any): ...
    def list_priority_class_with_http_info(self, **kwargs: Any): ...
    def patch_priority_class(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_priority_class_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def read_priority_class(self, name: Any, **kwargs: Any): ...
    def read_priority_class_with_http_info(self, name: Any, **kwargs: Any): ...
    def replace_priority_class(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_priority_class_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
