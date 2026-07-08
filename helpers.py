import json
import streamlit as st
import streamlit.components.v1 as components
from st_copy_to_clipboard import st_copy_to_clipboard

def copy_button(text: str, key: str):
    escaped = json.dumps(text)

    components.html(
        f"""
        <button
            onclick="navigator.clipboard.writeText({escaped})"
            style="
                border:none;
                background:#2d2d2d;
                color:white;
                padding:6px 12px;
                border-radius:8px;
                cursor:pointer;
                font-size:14px;
            "
        >
            📋 Copy
        </button>
        """,
        height=40,
    )

def render_message(role, content):
    if role == "user":
        st.markdown(f"""
        <div style="display:flex; justify-content:flex-end; margin:12px 0;">
            <div style="
                background:#2563eb;
                color:white;
                padding:12px 16px;
                border-radius:18px;
                max-width:70%;
            ">
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style="display:flex; justify-content:flex-start; margin:12px 0;">
            <div style="
                background:#374151;
                color:white;
                padding:12px 16px;
                border-radius:18px;
                max-width:70%;
            ">
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)
        st_copy_to_clipboard(content, "📋 Copy")

def export_chat(messages):
    lines = ["# Tea Time with Ollama\n"]

    for message in st.session_state.messages:
        role = "👤 You" if message["role"] == "user" else "🤖 Assistant"

        lines.append(f"## {role}")
        lines.append(message["content"])
        lines.append("")

    return "\n".join(lines)