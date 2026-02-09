def build_context(state):
    return f"""
Actor role: {state.actor_role}
System mode: {state.mode}
Prior actions: {state.prior_actions}
"""
