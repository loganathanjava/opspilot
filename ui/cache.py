import streamlit as st

from services.openshift.cluster import ClusterService
from services.openshift.namespace_details import NamespaceDetailsService


@st.cache_data(ttl=30)
def get_cluster_summary():
    return ClusterService().summary()


@st.cache_data(ttl=30)
def get_namespace_health():
    return ClusterService().namespace_health()


@st.cache_data(ttl=30)
def get_namespace_summary(namespace: str):
    return NamespaceDetailsService().summary(namespace)