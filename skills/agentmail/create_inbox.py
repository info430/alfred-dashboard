from agentmail import AgentMail
from agentmail.inboxes.types import CreateInboxRequest
import os
from dotenv import load_dotenv

# Load env
load_dotenv("/home/clawd/.openclaw/workspace/skills/agentmail/.env")

api_key = os.getenv("AGENTMAIL_API_KEY")
if not api_key:
    print("Error: AGENTMAIL_API_KEY not found.")
    exit(1)

client = AgentMail(api_key=api_key)

try:
    print("Creating inbox for user 'gary'...")
    
    # Construct the request object
    request = CreateInboxRequest(
        username="gary", 
        display_name="Gary"
    )
    
    # Pass it to the create method
    inbox = client.inboxes.create(request=request)
    
    print(f"SUCCESS: Created inbox!")
    print(f"ID: {inbox.id}")
    print(f"Email: {inbox.email_address}")
    print(f"Name: {inbox.name}")

except Exception as e:
    print(f"Error creating inbox: {e}")
    import traceback
    traceback.print_exc()
