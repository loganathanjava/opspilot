from dotenv import load_dotenv
import os

# Load .env from project root
load_dotenv(override=True)


class Settings:

    #
    # Application
    #

    APP_NAME = "OpsPilot"

    DEFAULT_USER = "loganathan"

    DEFAULT_SESSION = "default"

    #
    # OpenShift
    #

    OPENSHIFT_API = os.getenv("OPENSHIFT_API", "")

    OPENSHIFT_TOKEN = os.getenv("OPENSHIFT_TOKEN", "")

    VERIFY_SSL = os.getenv("VERIFY_SSL", "false").lower() == "true"


settings = Settings()