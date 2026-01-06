"""LLM and embedding model initialization."""

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import streamlit as st

# Create the LLM
# Note: ty/Pylance may show warnings due to incomplete type stubs for langchain-openai.
# These parameters are correct and work at runtime.
llm = ChatOpenAI(
    api_key=st.secrets["OPENAI_API_KEY"],  # type: ignore[call-arg]
    model=st.secrets["OPENAI_MODEL"],  # type: ignore[call-arg]
)

# Create the Embedding model
embeddings = OpenAIEmbeddings(api_key=st.secrets["OPENAI_API_KEY"])  # type: ignore[call-arg]
