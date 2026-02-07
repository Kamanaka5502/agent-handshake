class SystemState:
    def __init__(self, mode, actor_role, prior_actions):
        self.mode = mode
        self.actor_role = actor_role
        self.prior_actions = prior_actions


class ActionRequest:
    def __init__(self, action, required_role, allowed_modes):
        self.action = action
        self.required_role = required_role
        self.allowed_modes = allowed_modes


def preflight_check(state, request):
    if state.actor_role != request.required_role:
        return False

    if state.mode not in request.allowed_modes:
        return False

    return True
