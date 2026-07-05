from models.openshift import Pod


class PodFormatter:
    """
    Formats Pod models into lightweight dictionaries for the AI.

    The formatter intentionally exposes only the fields that are useful
    for operators and the LLM. This keeps the prompt size small and
    produces much better responses.
    """

    @staticmethod
    def format(pod: Pod) -> dict:

        return {
            "name": pod.name,
            "namespace": pod.namespace,
            "ready": pod.ready,
            "status": pod.status,
            "restarts": pod.restart_count,
            "reason": pod.reason,
            "node": pod.node,
            "age": pod.age,
        }

    @staticmethod
    def format_list(pods: list[Pod]) -> list[dict]:

        return [
            PodFormatter.format(pod)
            for pod in pods
        ]