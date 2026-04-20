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

# def chat(messages):
#     message = client.messages.create(
#        model=model,
#         max_tokens=1000,
#         messages=messages,
#     )
#     return message.content[0].text

# chat function with system prompts
def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

# Start with an empty message list
# messages = []

# Add the initial user question
#add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
# answer = chat(messages)

# Add Claude's response to the conversation history
#add_assistant_message(messages, answer)

# Add a follow-up question
# add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context
# final_answer = chat(messages)


# Make an initial list of messages
messages = []

add_user_message(messages, "Write a Python function that checks a string for duplicate characters.")

answer = chat(messages, system="You are a Python enginner who writes very concise code")

print(answer)