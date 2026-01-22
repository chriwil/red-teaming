import asyncio
import os
import threading

from agent_framework import AgentRunResponse
from agent_framework import AgentRunResponse
from agent_framework.microsoft import CopilotStudioAgent
from azure.ai.evaluation.red_team import RedTeam, RiskCategory, AttackStrategy
from azure.identity import ClientSecretCredential

from dotenv import load_dotenv
load_dotenv()

# Environment variables needed:
# COPILOTSTUDIOAGENT__ENVIRONMENTID - Environment ID where your copilot is deployed
# COPILOTSTUDIOAGENT__SCHEMANAME - Agent identifier/schema name of your copilot
# COPILOTSTUDIOAGENT__AGENTAPPID - Client ID for authentication
# COPILOTSTUDIOAGENT__TENANTID - Tenant ID for authentication
# AZURE_PROJECT_ENDPOINT - Azure AI Project Endpoint
# TENANT_ID - Tenant ID for authentication
# CLIENT_ID - Client ID for authentication
# CLIENT_SECRET - Client Secret for authentication

# Define a callback that uses a Copilot Studio Agent to generate responses
async def copilot_studio_agent_callback(query) -> AgentRunResponse:
    """
    Uses a Copilot Studio Agent to generate a response for the given query.

    Args:
        query: The input query to send to the Copilot Studio Agent.

    Returns:
        AgentRunResponse: The response object containing the agent's reply.
    """
    agent = CopilotStudioAgent()
    response: AgentRunResponse = await agent.run(query)
    return response

def copilot_studio_agent_sync(query: str) -> str:
    """
    Synchronous wrapper that runs async CopilotStudioAgent in a separate thread.
    """
    result = None
    exception = None
    
    def run_in_thread():
        nonlocal result, exception
        try:
            # Create a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                async def run_agent():
                    agent = CopilotStudioAgent()
                    response = await agent.run(query)
                    return response.text
                
                result = loop.run_until_complete(run_agent())
            finally:
                loop.close()
        except Exception as e:
            exception = e
    
    thread = threading.Thread(target=run_in_thread)
    thread.start()
    thread.join()
    
    if exception:
        raise exception
    return result
   

async def main() -> None:
    """
    Main asynchronous function to run the red team evaluation workflow.
    - Authenticates using environment variables.
    - Initializes a red team agent with code vulnerability risk category.
    - Runs a red team scan with Base64 attack strategy against the Copilot Studio Agent.
    - Saves results to red_team_results.json.
    """

    credential = ClientSecretCredential(
        tenant_id=os.getenv("TENANT_ID"),
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET")
    )

    # Initialize red team agent with code vulnerability risk category
    red_team_agent = RedTeam(
        credential=credential,
        azure_ai_project=os.getenv("AZURE_PROJECT_ENDPOINT"),
        risk_categories=[RiskCategory.CodeVulnerability],
        num_objectives=1
    )

    # Run red team scan with Base64 attack strategy against the Copilot Studio Agent
    await red_team_agent.scan(
        target=copilot_studio_agent_sync,
        scan_name="Copilot-Scan",
        attack_strategies=[AttackStrategy.Base64],
        output_path="red_team_results.json"
    )

if __name__ == "__main__":
    asyncio.run(main())