from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from opspilot_agent.agent import root_agent

APP_NAME = "opspilot"
USER_ID = "loganathan"
SESSION_ID = "default"


class AgentService:

    def __init__(self):

        self.user_id = USER_ID
        self.session_id = SESSION_ID

        self.session_service = InMemorySessionService()

        #
        # IMPORTANT:
        # Use the synchronous APIs.
        #
        self.session_service.create_session_sync(
            app_name=APP_NAME,
            user_id=self.user_id,
            session_id=self.session_id,
        )

        self.runner = Runner(
            agent=root_agent,
            app_name=APP_NAME,
            session_service=self.session_service,
        )

    def _ensure_session(self):

        session = self.session_service.get_session_sync(
            app_name=APP_NAME,
            user_id=self.user_id,
            session_id=self.session_id,
        )

        if session is None:

            self.session_service.create_session_sync(
                app_name=APP_NAME,
                user_id=self.user_id,
                session_id=self.session_id,
            )

    def chat(self, message: str) -> str:

        self._ensure_session()

        user_message = types.Content(
            role="user",
            parts=[
                types.Part(text=message),
            ],
        )

        response = ""

        print("\n========== ADK EVENTS ==========\n")

        for event in self.runner.run(
                user_id=self.user_id,
                session_id=self.session_id,
                new_message=user_message,
        ):

            print(event)
            print()

            if event.content and event.content.parts:

                for part in event.content.parts:

                    if getattr(part, "text", None):
                        response += part.text

        print("\n===============================\n")

        return response