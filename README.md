# red-teaming
Sample Scripts for Red Teaming!

## Scripts

### `red_team_local_run.py`
Demonstrates Azure AI Red Team evaluation using the `azure.ai.evaluation.red_team` SDK. Runs a simple red teaming scan against a callback function using configurable risk categories and attack strategies (e.g., Base64 encoding).

### `pyrit_gandalf.py`
Uses the PyRIT (Python Risk Identification Tool) framework to run a multi-turn red teaming attack against the Gandalf challenge. An AI attacker attempts to extract a secret password from a simulated "wizard" bot using various social engineering tactics.

### `copilotstudio_agentframework.py`
Integrates Azure AI Red Team evaluation with a Microsoft Copilot Studio Agent. Runs automated red team scans against a deployed Copilot Studio agent to test for vulnerabilities like code injection.

## Requirements

This project contains multiple scripts with different dependencies:

| Script | Requirements File |
|--------|-------------------|
| `red_team_local_run.py` | `requirements.txt` |
| `pyrit_gandalf.py` | `requirements_gandalf.txt` |
| `copilotstudio_agentframework.py` | `requirements.txt` |

Install the appropriate dependencies based on which script you want to run:

```bash
# For red_team_local_run.py and copilotstudio_agentframework.py
pip install -r requirements.txt

# For pyrit_gandalf.py
pip install -r requirements_gandalf.txt
```

## Environment Variables

Create a `.env` file in the project root with the required variables for each script:

### `red_team_local_run.py`
```env
AZURE_AI_PROJECT=<your-azure-ai-project-connection-string>
```

### `pyrit_gandalf.py`
```env
OPENAI_API_KEY=<your-openai-api-key>
OPENAI_ENDPOINT=<your-openai-endpoint>
OPENAI_DEPLOYMENT=<your-deployment-name>
```

### `copilotstudio_agentframework.py`
```env
# Copilot Studio Agent configuration
COPILOTSTUDIOAGENT__ENVIRONMENTID=<environment-id>
COPILOTSTUDIOAGENT__SCHEMANAME=<agent-schema-name>
COPILOTSTUDIOAGENT__AGENTAPPID=<agent-app-id>
COPILOTSTUDIOAGENT__TENANTID=<tenant-id>

# Azure authentication
AZURE_PROJECT_ENDPOINT=<azure-ai-project-endpoint>
TENANT_ID=<tenant-id>
CLIENT_ID=<client-id>
CLIENT_SECRET=<client-secret>
```
