# AWS Lex Chatbot

This project is an interactive chatbot using **Amazon Lex v2** that provides accommodation booking assistance.

## Features
- Uses **AWS Lex v2 Runtime** for natural language understanding.
- Recognizes intents like **greeting, booking, pricing, and fallback**.
- Communicates with users in a conversational style.
- Simple API integration using **boto3** (AWS SDK for Python).

---

## 1. Installation

### Prerequisites
Before starting, ensure you have the following:
- An **AWS Account** with permissions to create and manage Lex chatbots.
- **AWS CLI** installed and configured.
- **Python 3.x** installed (Recommended: Python 3.8+).
- **boto3** and **requests** Python libraries installed.
- **GitHub** account for version control.

### Step 1: Install Required Packages
```sh
pip install boto3 
```

### Step 2: Configure AWS CLI (If not already set up)
```sh
aws configure
```
You'll be prompted to enter:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region** (e.g., `ap-southeast-1`)
- **Output format** (leave blank or use `json`)

---

## 2. AWS Configuration

### Step 3: Setting Up AWS Lex Chatbot
1. Sign in to [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to **Amazon Lex**.
3. Click **Create bot** and select **Lex V2**.
4. Choose a template or create a bot from scratch.
5. Configure intents and responses (e.g., `greeting`, `booking`, `pricing`).
6. Save and build the bot.
7. Deploy an alias (e.g., `TSTALIASID`).

### Step 4: Retrieve AWS Credentials
1. Navigate to **IAM** in the AWS Console.
2. Create a new user with programmatic access.
3. Attach `AmazonLexFullAccess` permissions.
4. Copy **Access Key ID** and **Secret Access Key**.
5. Configure AWS CLI:
   ```sh
   aws configure
   ```

📌 **For detailed IAM setup, refer to** [AWS IAM Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

---

## 3. Running the Chatbot Locally

### Step 5: Clone the Repository
```sh
git clone https://github.com/yourusername/aws-lex-chatbot.git
cd aws-lex-chatbot
```

### Step 6: Create a Python Script (`lex_chatbot.py`)
```python
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
        botId="YOUR_ACCESID",
        botAliasId="YOUR_ALIASID",
        localeId="en_US",
        sessionId=session_id,
        text=user_input
    )

    if "messages" in response:
        for message in response["messages"]:
            print("Bot:", message["content"])

```

### Step 7: Run the Script
```sh
python lex_chatbot.py
```

#### Sample Response:
```json
{
   "messages": [
      {"content": "hello , are you looking for accommodations ?"},
      {"content": "We’ll set you up with a stylish and comfy stay."}
   ]
}
```

---

## 4. Notes
- **Security**: **Do NOT** share your AWS Access Keys publicly. Use `.env` files for secure storage.
- **IAM Setup**: Users must configure their own **Access Keys** and **Lex Bot IDs**.
- **Bot Customization**: You can modify intents and responses in the AWS Lex Console.

---

## 5. Deployment
You can deploy this chatbot using **AWS Lambda, EC2, or containerized services**. Ensure that the execution role has permissions for **Amazon Lex**.

---

## 6. Contributing
Feel free to open issues and pull requests. Let's improve this together! 🚀
