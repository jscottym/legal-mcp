# Legal MCP Server

US case law search, citation parsing, practice management, and federal court filings for AI assistants — powered by [FastMCP](https://gofastmcp.com).

Hosted at `https://legal-mcp-production.up.railway.app/mcp`

## Setup

Add the server to your Claude Code settings (`~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "legal-mcp": {
      "type": "url",
      "url": "https://legal-mcp-production.up.railway.app/mcp",
      "headers": {
        "X-CourtListener-Token": "YOUR_COURTLISTENER_TOKEN"
      }
    }
  }
}
```

### Getting a CourtListener token

1. Create a free account at https://www.courtlistener.com/sign-in/
2. Go to your profile and copy your API token
3. Add it as the `X-CourtListener-Token` header above

### Optional: Clio practice management

If you have a [Clio](https://www.clio.com) account with API access, add your OAuth token:

```json
"headers": {
  "X-CourtListener-Token": "YOUR_COURTLISTENER_TOKEN",
  "X-Clio-Token": "YOUR_CLIO_OAUTH_TOKEN"
}
```

## Available tools

| Tool | Description |
|------|-------------|
| `search_case_law` | Search 4M+ US court opinions by topic, court, or date range |
| `get_case_details` | Get full text and details of a specific opinion |
| `get_case_record` | Get docket info — parties, attorneys, judges, procedural history |
| `find_citing_cases` | Find cases that cite a given opinion |
| `find_cited_cases` | Find cases cited by a given opinion |
| `parse_legal_citations` | Parse Bluebook-format citations from text |
| `list_available_courts` | List all US courts and their filter codes |
| `list_reporter_abbreviations` | Reference for reporter abbreviations (U.S., F.3d, etc.) |
| `search_federal_cases` | Search PACER for federal cases (requires PACER credentials) |
| `get_federal_case` | Get federal case details from PACER |
| `get_court_filings` | Get docket entries for a federal case from PACER |
| `search_clients` | Search Clio contacts (requires Clio token) |
| `search_matters` | Search Clio matters/cases |
| `get_matter_details` | Get full matter details from Clio |
| `get_time_entries` | Get billable hours from Clio |
| `get_matter_tasks` | Get tasks for a matter in Clio |
| `get_matter_documents` | Search documents in Clio |
| `get_calendar` | Get calendar entries from Clio |

## Self-hosting

```bash
git clone https://github.com/jscottym/legal-mcp.git
cd legal-mcp
pip install -r requirements.txt
python -m legal_mcp.server
```

Or with Docker:

```bash
docker build -t legal-mcp .
docker run -p 8000:8000 -e COURTLISTENER_TOKEN=your_token legal-mcp
```

### Environment variables

| Variable | Description |
|----------|-------------|
| `PORT` | Server port (default: 8000) |
| `COURTLISTENER_TOKEN` | Fallback CourtListener API token |
| `CLIO_TOKEN` | Fallback Clio OAuth token |
| `PACER_USERNAME` | PACER login |
| `PACER_PASSWORD` | PACER password |
| `LEGAL_MCP_DEMO` | Set to `true` to use demo data without API keys |
