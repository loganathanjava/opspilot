from google.adk.agents import Agent

from opspilot_agent.prompt import SYSTEM_PROMPT
from opspilot_agent.tools import (
    list_namespaces,
    list_pods,
    list_unhealthy_pods,
)

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="AI-powered OpenShift Operations Assistant",
    instruction=SYSTEM_PROMPT,
    tools=[
        list_namespaces,
        list_pods,
        list_unhealthy_pods,
    ],
)