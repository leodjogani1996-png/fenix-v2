import streamlit as st
from openai import OpenAI

# =========================================
# FENIX V2 - WEB APP
# =========================================

# Get Groq API Key securely from Streamlit Secrets
API_KEY = st.secrets["GROQ_API_KEY"]

# Connect to Groq API
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=API_KEY
)

# =========================================
# FENIX IDENTITY
# =========================================

FENIX_IDENTITY = """
You are Fenix, a helpful and intelligent AI assistant.

You were created and developed by Leo Đogani.

Your principles:

- Be honest.
- Be kind.
- Be helpful.
- Explain things clearly.
- Think logically.
- Admit when you do not know something.
- Never pretend to know something you do not know.
- Treat every human with respect.
"""

# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(page_title="Fenix AI", page_icon="🔥")
st.title("🔥 Fenix V2")
st.caption("Your personal AI assistant. Creator: Leo Đogani")

# =========================================
# CHAT MEMORY INITIALIZATION
# =========================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": FENIX_IDENTITY}
    ]

# =========================================
# DISPLAY CHAT HISTORY
# =========================================

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# =========================================
# USER INPUT & BOT RESPONSE
# =========================================

if prompt := st.chat_input("Write a message to Fenix..."):
    
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Fenix thinks and responds
    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            )
            fenix_response = response.choices[0].message.content
            st.markdown(fenix_response)
            
            # Save Fenix response to chat history
            st.session_state.messages.append({"role": "assistant", "content": fenix_response})
        
        except Exception as error:
            st.error(f"System Error: {error}")