from llm import think
from rules import SystemState, ActionRequest, preflight_check

state = SystemState(
    actor_role="user",
    mode="maintenance",
    prior_actions=["login","auth_success"]
)

request = ActionRequest(
    action="reset_database",
    required_role="admin",
    allowed_modes=["maintenance"]
)

allowed = preflight_check(state, request)

print("Preflight allowed:", allowed)

if allowed:
    reasoning = think(request)
    print("\nLLM reasoning:\n")
    print(reasoning)
else:
    print("🚫 Agent blocked before thinking")
