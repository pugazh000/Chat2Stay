import boto3

# Check AWS credentials
session = boto3.Session()
credentials = session.get_credentials()

print("AWS Access Key:", credentials.access_key)
print("AWS Secret Key:", credentials.secret_key)
print("AWS Session Token:", credentials.token)


import boto3

# Initialize Lex client
client = boto3.client('lexv2-runtime', region_name="ap-southeast-1")

session_id = "test-session"  # Maintain session

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:  # Stop the loop if user types exit
        print("Chatbot session ended.")
        break
    
    response = client.recognize_text(
        botId="RAGG8R2WDU",
        botAliasId="TSTALIASID",
        localeId="en_US",
        sessionId=session_id,
        text=user_input
    )

    if "messages" in response:
        for message in response["messages"]:
            print("Bot:", message["content"])
