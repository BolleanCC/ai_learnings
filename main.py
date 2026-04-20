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

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
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

# Use a 'While True' loop to run the chatbot forever
while True:
    # Get user input
    user_input = input("> ")

    if user_input.lower() in ["q", "quit", "exit"]:
        break

    # Add user input to the messages list
    add_user_message(messages, user_input)
    # Call Claude with the 'chat' function
    answer = chat(messages)
    # Add generated text to the list of messages
    add_assistant_message(messages, answer)
    # Print the generated text
    print(answer)