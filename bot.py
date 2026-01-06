import os

import streamlit as st

# Export LangSmith secrets as env vars (before importing LangChain)
if "LANGCHAIN_API_KEY" in st.secrets:
    os.environ["LANGCHAIN_TRACING_V2"] = st.secrets.get("LANGCHAIN_TRACING_V2", "true")
    os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
    os.environ["LANGCHAIN_PROJECT"] = st.secrets.get("LANGCHAIN_PROJECT", "default")

from agent import generate_response
from utils import write_message

# Page Config
st.set_page_config("Ebert", page_icon=":movie_camera:")

# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi, I'm the GraphAcademy Chatbot! How can I help you?",
        },
    ]


# Submit handler
def handle_submit(message):
    """Handle user message submission.

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """
    # Handle the response
    with st.spinner("Thinking..."):
        # CAll the agent
        response = generate_response(message)
        write_message("assistant", response)


# Display messages in Session State
for message in st.session_state.messages:
    write_message(message["role"], message["content"], save=False)

# Handle any user input
# st.chat_input() renders a chat input box at the bottom of the page.
# It returns None on every script re-run UNTIL the user submits text,
# then returns the submitted string exactly once.
#
# The walrus operator (:=) combines two operations:
#   1. Assigns the return value of st.chat_input() to 'question'
#   2. Evaluates 'question' as a boolean for the if-condition
# This is equivalent to:
#   question = st.chat_input("What is up?")
#   if question:
#       ...
if question := st.chat_input("What is up?"):
    # User has submitted input - 'question' now contains their text.
    # Display the user's message in the chat UI and save it to session state.
    write_message("user", question)

    # Pass the user's question to the submit handler.
    # In this skeleton, it simply echoes the message back.
    # TODO: Replace handle_submit() internals with actual LLM call.
    handle_submit(question)
