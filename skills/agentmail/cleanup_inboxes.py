from agentmail import AgentMail
import os
from dotenv import load_dotenv

load_dotenv("/home/clawd/.openclaw/workspace/skills/agentmail/.env")
client = AgentMail(api_key=os.getenv("AGENTMAIL_API_KEY"))

# List and cleanup
try:
    response = client.inboxes.list()
    keep = "alfred.agent@agentmail.to"
    
    print(f"Found {len(response.inboxes)} inboxes.")
    
    for inbox in response.inboxes:
        print(f"Checking: {inbox.inbox_id}")
        if inbox.inbox_id != keep:
            print(f"Deleting extra inbox: {inbox.inbox_id}")
            # client.inboxes.delete(inbox_id=inbox.inbox_id)  # Hypothetical delete method
            # If delete isn't obvious, I'll just ignore it for now to be safe.
            # Checking available methods on client.inboxes first.
            pass
        else:
            print(f"Keeping primary inbox: {inbox.inbox_id}")

except Exception as e:
    print(f"Error: {e}")
