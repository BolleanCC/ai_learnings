from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"


# helper functions
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

# Implementing temperature in code
def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }

    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

# Make an initial list of messages
messages = []

add_user_message(messages, "what is the capital in Japan?")

answer = chat(messages, temperature=1.0)

print(answer)