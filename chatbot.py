import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

st.title("My Own ChatGPT! 🤖")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages in the chat
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Set the model (if not set already)
if "model" not in st.session_state:
    st.session_state.model = "gpt-4"

# Collect user input
if user_prompt := st.chat_input("Your prompt"):
    # Add the user message to the session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Send messages to the OpenAI API and get a response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Call the OpenAI API to get a response
            response = openai.ChatCompletion.create(
                model=st.session_state.model,
                messages=st.session_state.messages,
            )
            # Get the assistant's reply
            full_response = response["choices"][0]["message"]["content"]

        except Exception as e:
            # If there's an error, display it
            st.error(f"An error occurred: {e}")
            full_response = "Sorry, there was an error processing your request."

        # Display the response
        message_placeholder.markdown(full_response)

    # Append the assistant's reply to the session state
    st.session_state.messages.append({"role": "assistant", "content": full_response})
