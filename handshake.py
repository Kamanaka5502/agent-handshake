from rules import preflight_check

def handshake(state, request):
    allowed = preflight_check(state, request)

    if not allowed:
        return "BLOCKED: Request denied before reasoning."

    return "ALLOWED: Safe to pass into LLM reasoning layer."
