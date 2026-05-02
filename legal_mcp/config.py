import os
from contextvars import ContextVar

COURTLISTENER_API_URL = "https://www.courtlistener.com/api/rest/v4"
COURTLISTENER_TOKEN = os.environ.get("COURTLISTENER_TOKEN", "")

CLIO_API_URL = "https://app.clio.com/api/v4"
CLIO_TOKEN = os.environ.get("CLIO_TOKEN", "")

PACER_API_URL = "https://pcl.uscourts.gov/pcl-public-api/rest"
PACER_USERNAME = os.environ.get("PACER_USERNAME", "")
PACER_PASSWORD = os.environ.get("PACER_PASSWORD", "")

DEMO_MODE = os.environ.get("LEGAL_MCP_DEMO", "").lower() in ("1", "true", "yes")

# Per-request token overrides (set by middleware from client headers)
request_courtlistener_token: ContextVar[str] = ContextVar("request_courtlistener_token", default="")
request_clio_token: ContextVar[str] = ContextVar("request_clio_token", default="")
