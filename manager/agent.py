from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.fi_mcp_agent.agent import fi_mcp_agent
# from .sub_agents.investment_intel_agent.agent import investment_intel_agent
# from .sub_agents.future_planner_agent.agent import future_planner_agent
# from .sub_agents.financial_health_agent.agent import financial_health_agent
# from .sub_agents.financial_wisdom_agent.agent import financial_wisdom_agent
# from .sub_agents.goal_planner_agent.agent import goal_planner_agent
# from .sub_agents.nudges_agent.agent import nudges_agent

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Orchestrates specialized finance agents to provide a unified personal finance assistant.",
    instruction="""
You are a manager agent overseeing specialized sub-agents. Route user requests to the right agent:
- fi_mcp_agent: Data sync and access.
- investment_intel_agent: Investment analysis/insights.
- future_planner_agent: Projections & what-if.
- financial_health_agent: Scoring and health.
- financial_wisdom_agent: Finance news/advice.
- goal_planner_agent: Saving for goals.
- nudges_agent: Summarize & notify.
""",
    sub_agents=[
        fi_mcp_agent, #investment_intel_agent, future_planner_agent,
        #financial_health_agent, financial_wisdom_agent, goal_planner_agent, nudges_agent,
    ],
    tools=[],
)
