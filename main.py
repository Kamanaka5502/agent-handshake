from rules import SystemState, ActionRequest
from handshake import handshake

state = SystemState(
    actor_role="admin",
    mode="maintenance",
    prior_actions=["login", "auth_success"]
)

request = ActionRequest(
    action="reset_database",
    required_role="admin",
    allowed_modes=["maintenance"]
)

result = handshake(state, request)
print(result)
