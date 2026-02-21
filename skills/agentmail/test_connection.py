from agentmail import AgentMail
import os
from dotenv import load_dotenv

# Load env from .env file in the same directory as this script, or the skill root
load_dotenv("/home/clawd/.openclaw/workspace/skills/agentmail/.env")

api_key = os.getenv("AGENTMAIL_API_KEY")
if not api_key:
    print("Error: AGENTMAIL_API_KEY not found in environment.")
    exit(1)

try:
    client = AgentMail(api_key=api_key)
    # Simple test: list inboxes
    response = client.inboxes.list(limit=5)
    print("Successfully connected to AgentMail!")
    print(f"Found {len(response.inboxes)} inboxes:")
    for inbox in response.inboxes:
        print(f"- {inbox.email_address} (ID: {inbox.id})")
        
except Exception as e:
    print(f"Error connecting to AgentMail: {e}")
