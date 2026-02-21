from agentmail import AgentMail
import os
from dotenv import load_dotenv

# Load env
load_dotenv("/home/clawd/.openclaw/workspace/skills/agentmail/.env")

api_key = os.getenv("AGENTMAIL_API_KEY")
if not api_key:
    print("Error: AGENTMAIL_API_KEY not found.")
    exit(1)

client = AgentMail(api_key=api_key)

inbox_id = "alfred.agent@agentmail.to"
to_email = "Gary.efenterprises@gmail.com"

try:
    print(f"Sending email from {inbox_id} to {to_email}...")
    
    response = client.inboxes.messages.send(
        inbox_id=inbox_id,
        to=to_email,
        subject="Hello from Alfred!",
        text="Hello Gary,\n\nThis is a test email from your AI assistant, Alfred via AgentMail.\n\nBest,\nAlfred",
        html="<p>Hello Gary,</p><p>This is a test email from your AI assistant, Alfred via <strong>AgentMail</strong>.</p><p>Best,<br>Alfred</p>"
    )
    
    print(f"SUCCESS: Email sent!")
    # Check what the response object looks like
    print(f"Response: {response}")

except Exception as e:
    print(f"Error sending email: {e}")
    import traceback
    traceback.print_exc()
