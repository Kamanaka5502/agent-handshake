from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def ask_ai(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text


print("\n=== AI EXECUTION CONSOLE ===\n")
print("1 - Plan my day from schedule")
print("2 - Turn call notes into CRM + follow-up email")
print("3 - Write a professional client email")
print("4 - Clean up priorities")
print("5 - End of day → tomorrow plan")
print("6 - Custom request\n")

choice = input("Choose: ")
user_input = input("\nPaste your text here:\n\n")

if choice == "1":
    prompt = f"""
Here is my schedule for today:

{user_input}

Turn this into:
- A clear execution plan
- Priority order
- Talking points for each meeting
- Desired outcome for each call
"""

elif choice == "2":
    prompt = f"""
These are rough notes from a client call:

{user_input}

Turn this into:
1) Clean CRM entry
2) Professional follow-up email
"""

elif choice == "3":
    prompt = f"""
Write a professional client email from this:

{user_input}
"""

elif choice == "4":
    prompt = f"""
These are all the things on my mind:

{user_input}

Organize into:
- Priorities
- Delegations
- What to ignore
"""

elif choice == "5":
    prompt = f"""
This is a summary of my day:

{user_input}

Create:
- Follow-ups
- Reminders
- Tomorrow's execution plan
"""

else:
    prompt = user_input

print("\nThinking...\n")
result = ask_ai(prompt)
print(result)
