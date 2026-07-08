import streamlit as st
from ollama_service import chat, getModels, connected
from helpers import render_message, export_chat

st.set_page_config(
    page_title="Tea Time With Ollama",
    page_icon="🍵",
    layout="wide"
)

st.title("🍵 Tea Time with Ollama")

# ---------------- Session State ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = None

if "pending_reply" not in st.session_state:
    st.session_state.pending_reply = False

# ---------------- Welcome ---------------- #

if not st.session_state.messages:
    st.markdown(
        """
        Welcome! Pull up a chair and start a conversation.

        ### Try asking:
        - Explain recursion like I'm five.
        - Write a Python web scraper.
        - Tell me an interesting fact.
        """
    )

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🍵 Tea Time")
    st.caption("Local AI Chat")

    st.session_state.model = st.selectbox(
        "Model",
        getModels()
    )

    st.divider()

    st.download_button(
        "📥 Download Conversation",
        data=export_chat(st.session_state.messages),
        file_name="conversation.txt",
        mime="text/plain",
        use_container_width=True
    )

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending_reply = False
        st.rerun()

    st.divider()

    if connected():
        st.success("🟢 Connected")
    else:
        st.error("🔴 Ollama Offline")
        st.stop()

# ---------------- Chat History ---------------- #

for message in st.session_state.messages:
    render_message(
        message["role"],
        message["content"]
    )

# ---------------- User Input ---------------- #

prompt = st.chat_input("Ask me anything")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    st.session_state.pending_reply = True

    st.rerun()

# ---------------- Generate Reply ---------------- #

if st.session_state.pending_reply:

    st.session_state.pending_reply = False

    try:

        with st.spinner("🍵 Brewing a response..."):

            reply = chat(
                st.session_state.model,
                st.session_state.messages
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

    except Exception as e:

        st.error(f"Failed to generate response.\n\n{e}")

    st.rerun()