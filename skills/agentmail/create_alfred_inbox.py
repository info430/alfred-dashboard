from agentmail import AgentMail
from agentmail.inboxes.types import CreateInboxRequest
import os
import random
import string
from dotenv import load_dotenv

load_dotenv("/home/clawd/.openclaw/workspace/skills/agentmail/.env")
client = AgentMail(api_key=os.getenv("AGENTMAIL_API_KEY"))

def try_create(username, display_name="Alfred"):
    print(f"Trying: {username}...")
    try:
        request = CreateInboxRequest(
            username=username, 
            display_name=display_name
        )
        inbox = client.inboxes.create(request=request)
        print(f"SUCCESS: Created {inbox.email_address}")
        return inbox
    except Exception as e:
        if "IsTakenError" in str(e):
            print(f"Taken: {username}")
        else:
            print(f"Error ({username}): {e}")
        return None

# Strategy: Try 'alfred.agent' first. If taken, try 'alfred.agent.[random]'
# This avoids a back-and-forth loop with the user.
if not try_create("alfred.agent"):
    suffix = ''.join(random.choices(string.digits, k=4))
    fallback = f"alfred.agent.{suffix}"
    try_create(fallback)
