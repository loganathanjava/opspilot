import streamlit as st

from services.openshift.cluster import ClusterService
from services.openshift.namespace_details import NamespaceDetailsService
from services.openshift.pod_details import PodDetailsService
from services.openshift.pods import PodService


@st.cache_data(ttl=30)
def get_cluster_summary():
    """
    Returns cluster summary.
    """
    return ClusterService().summary()


@st.cache_data(ttl=30)
def get_namespace_health():
    """
    Returns namespace health.
    """
    return ClusterService().namespace_health()


@st.cache_data(ttl=30)
def get_namespace_summary(namespace: str):
    """
    Returns namespace summary.
    """
    return NamespaceDetailsService().summary(namespace)


@st.cache_data(ttl=30)
def get_pods(namespace: str):
    """
    Returns pods for a namespace.
    """
    return PodService().list_pods(namespace)


@st.cache_data(ttl=30)
def get_pod(namespace: str, pod_name: str):
    """
    Returns pod details.
    """
    return PodDetailsService().get(
        namespace,
        pod_name,
    )