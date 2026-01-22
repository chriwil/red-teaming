# Azure imports
import os
from azure.identity import DefaultAzureCredential
from azure.ai.evaluation.red_team import RedTeam, RiskCategory, AttackStrategy
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

azure_ai_project = os.getenv("AZURE_AI_PROJECT")

red_team_agent = RedTeam(
    azure_ai_project=azure_ai_project, 
    credential=DefaultAzureCredential(),
    risk_categories=[RiskCategory.CodeVulnerability],
    num_objectives=1
)

# A simple example application callback function that always returns a fixed response
def simple_callback(query: str) -> str:
    return "I'm an AI assistant that follows ethical guidelines. I cannot provide harmful content."

# Runs a red teaming scan on the simple callback target
async def main():
    red_team_result = await red_team_agent.scan(
        target=simple_callback,
        attack_strategies=[AttackStrategy.Base64]
    )
    return red_team_result

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())