from dataclasses import dataclass

@dataclass
class SystemState:
    actor_role: str
    mode: str
    prior_actions: list

@dataclass
class ActionRequest:
    action: str
    required_role: str
    allowed_modes: list


def preflight_check(state: SystemState, request: ActionRequest) -> bool:
    if state.actor_role != request.required_role:
        return False

    if state.mode not in request.allowed_modes:
        return False

    return True
