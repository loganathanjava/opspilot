import streamlit as st

from services.openshift.cluster import ClusterService
from services.openshift.namespace_details import NamespaceDetailsService
from services.openshift.pod_details import PodDetailsService
from services.openshift.pod_events import PodEventsService
from services.openshift.pod_yaml import PodYamlService
from services.openshift.pods import PodService
from services.openshift.deployments import DeploymentService


@st.cache_data(ttl=30)
def get_cluster_summary():
    return ClusterService().summary()


@st.cache_data(ttl=30)
def get_namespace_health():
    return ClusterService().namespace_health()


@st.cache_data(ttl=30)
def get_namespace_summary(namespace: str):
    return NamespaceDetailsService().summary(
        namespace,
    )


@st.cache_data(ttl=30)
def get_pods(namespace: str):
    return PodService().list_pods(
        namespace,
    )


@st.cache_data(ttl=30)
def get_pod(namespace: str, pod_name: str):
    return PodDetailsService().get(
        namespace,
        pod_name,
    )


@st.cache_data(ttl=5)
def get_pod_logs(
        namespace: str,
        pod_name: str,
        container: str | None,
        previous: bool,
        tail_lines: int,
):
    return PodService().get_logs(
        namespace,
        pod_name,
        container,
        previous,
        tail_lines,
    )


@st.cache_data(ttl=30)
def get_pod_yaml(
        namespace: str,
        pod_name: str,
):
    return PodYamlService().get_yaml(
        namespace,
        pod_name,
    )


@st.cache_data(ttl=5)
def get_pod_events(
        namespace: str,
        pod_name: str,
):
    return PodEventsService().get_events(
        namespace,
        pod_name,
    )

@st.cache_data(ttl=30)
def get_deployments(
        namespace: str | None = None,
):
    """
    Returns deployments.
    """
    return DeploymentService().list_deployments(
        namespace,
    )