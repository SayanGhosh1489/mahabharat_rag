import streamlit as st
import os
import sys
from mahabharat_rag.pipeline.generator_pipeline import GeneratorPipeline
from mahabharat_rag.components.embedding import Embedding
from mahabharat_rag.entity.config import embeddingConfig
from mahabharat_rag.logger import logging
from mahabharat_rag.exception import MahabharatXception
import warnings

warnings.filterwarnings("ignore")

# Streamlit page config
st.set_page_config(page_title="Mahabharat Chatbot")

# Initialize embedding at the start to reduce runtime delay
embedding_config = embeddingConfig()
embedding = Embedding(embedding_config=embedding_config)
embedding_artifact = embedding.initiate_get_embedding()

def start_generator_pipeline():
    logging.info("Starting the start_generator_pipeline pipeline")
    try:
        pipeline = GeneratorPipeline()
        qa_artifact = pipeline.run_pipeline(embedding_artifact=embedding_artifact)
        logging.info("Exited the Loader pipeline")
        return qa_artifact
    except Exception as e:
        raise MahabharatXception(e, sys)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Ask me anything about Mahabharat!"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

qa_artifact = start_generator_pipeline()
qa_staff = qa_artifact.retrivel

# Function to generate chatbot response with context
def generate_response(user_query, history):
    context = "\n".join([msg["content"] for msg in history if msg["role"] == "assistant" or msg["role"] == "user"])
    response = qa_staff.invoke({'query': user_query, 'context': context})
    return response['result']

# User input field
if prompt := st.chat_input("Ask your question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate response with context
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, st.session_state.messages)
            st.write(response)
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})