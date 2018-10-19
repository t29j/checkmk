# Stubs for kubernetes.client.apis.events_v1beta1_api (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..api_client import ApiClient
from typing import Any, Optional

class EventsV1beta1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_namespaced_event(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_event_with_http_info(self, namespace: Any, body: Any, **kwargs: Any): ...
    def delete_collection_namespaced_event(self, namespace: Any, **kwargs: Any): ...
    def delete_collection_namespaced_event_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_event(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def delete_namespaced_event_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_event_for_all_namespaces(self, **kwargs: Any): ...
    def list_event_for_all_namespaces_with_http_info(self, **kwargs: Any): ...
    def list_namespaced_event(self, namespace: Any, **kwargs: Any): ...
    def list_namespaced_event_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def patch_namespaced_event(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_event_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def read_namespaced_event(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_event_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def replace_namespaced_event(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_event_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
