import json
import streamlit as st
import streamlit.components.v1 as components
from st_copy_to_clipboard import st_copy_to_clipboard

def render_message(role, content):

    if role == "user":

        st.markdown(f"""
        <div style="display:flex; justify-content:flex-end; margin:14px 0;">
            <div style="
                background:#C68B59;
                color:#1A1816;
                padding:14px 18px;
                border-radius:20px 20px 6px 20px;
                max-width:72%;
                line-height:1.6;
                box-shadow:0 2px 6px rgba(0,0,0,.25);
                word-wrap:break-word;
            ">
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div style="display:flex; justify-content:flex-start; margin:14px 0;">
            <div style="
                background:#332D28;
                color:#F5F2EB;
                padding:14px 18px;
                border-radius:20px 20px 20px 6px;
                max-width:72%;
                line-height:1.6;
                border:1px solid #4E433B;
                box-shadow:0 2px 6px rgba(0,0,0,.25);
                word-wrap:break-word;
            ">
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)

def export_chat(messages):
    lines = ["# Tea Time with Ollama\n"]

    for message in st.session_state.messages:
        role = "👤 You" if message["role"] == "user" else "🤖 Assistant"

        lines.append(f"## {role}")
        lines.append(message["content"])
        lines.append("")

    return "\n".join(lines)