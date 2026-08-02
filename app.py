import base64
import streamlit as st
from pathlib import Path
from chatbot import ask_bot

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Kids AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# Ensure you have this file in your directory, or comment out the hero image if not.
img = get_base64("assets/logo.png")

st.markdown(f"""
<style>

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

.stApp {{
    background: #EEF5FF;
}}

.stApp, .stApp p, .stApp span, .stApp div, .stApp li, .stApp label {{
    color: #1E293B;
}}

/* Hero Section */
.hero {{
    height: 430px;
    border-radius: 25px;
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    margin-bottom: 25px;
    box-shadow: 0px 8px 30px rgba(0, 0, 0, .15);
}}

/* Header text */
.chat-title {{
    font-size: 34px;
    font-weight: 800;
    color: #1E293B;
    text-align: center;
    margin-bottom: 4px;
}}

.subtitle {{
    font-size: 18px;
    color: #475569;
    text-align: center;
    margin-bottom: 20px;
}}

/* Chat container */
.chat-box {{
    background: white;
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, .12);
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #4F46E5, #2563EB);
}}

section[data-testid="stSidebar"] * {{
    color: black;
}}

/* Buttons */
.stButton > button {{
    width: 100%;
    border-radius: 15px;
    height: 52px;
    background: white;
    transition: .3s;
}}

/* Target the text inside the button specifically */
.stButton > button * {{
    color: black !important;
    font-weight: bold;
}}

.stButton > button:hover {{
    background: #FACC15;
}}

.stButton > button:hover * {{
    color: black !important;
}}

/* Chat messages */
div[data-testid="stChatMessage"] {{
    border-radius: 18px;
    background: white;
    padding: 12px;
    margin-bottom: 12px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, .08);
}}

/* Chat Input */
.stChatInput {{
    border-radius: 20px;
}}

.stChatInput textarea,
.stChatInput textarea[data-testid="stChatInputTextArea"],
div[data-testid="stChatInput"] textarea {{
    color: #F1F5F9 !important;
    -webkit-text-fill-color: #F1F5F9 !important;
    caret-color: #F1F5F9 !important;
}}

.stChatInput textarea::placeholder,
div[data-testid="stChatInput"] textarea::placeholder {{
    color: #94A3B8 !important;
    -webkit-text-fill-color: #94A3B8 !important;
    opacity: 1;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO IMAGE ---------------- #

st.markdown('<div class="hero"></div>', unsafe_allow_html=True)

st.markdown(
    "<div class='chat-title'>🤖 Kids AI Chatbot</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>🌈 Learn • Play • Explore • Imagine</div>",
    unsafe_allow_html=True,
)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:
    st.title("🎈 Topics")

    if st.button("🌍 Science"):
        st.session_state.topic = "Tell me an interesting science fact."

    if st.button("➕ Math"):
        st.session_state.topic = "Teach me addition."

    if st.button("📚 English"):
        st.session_state.topic = "Teach me English."

    if st.button("🦁 Animals"):
        st.session_state.topic = "Tell me about animals."

    if st.button("🚀 Space"):
        st.session_state.topic = "Tell me about space."

    if st.button("💻 Coding"):
        st.session_state.topic = "Teach coding for kids."

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "👋 Hi! I'm **KidBot**.\n\n"
                    "I'm here to help you learn about 🌍 Science, ➕ Math, "
                    "🚀 Space, 📚 English, 🦁 Animals and 💻 Coding.\n\n"
                    "Ask me anything!"
                )
            }
        ]
        st.rerun()

# ---------------- CHAT SESSION ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Hello, little explorer!\n\n"
                "I'm **KidBot 🤖**\n\n"
                "I can help you learn about:\n"
                "🌍 Science\n"
                "➕ Math\n"
                "📚 English\n"
                "🦁 Animals\n"
                "🚀 Space\n"
                "💻 Coding\n\n"
                "Ask me anything! 😊"
            )
        }
    ]

# ---------------- DISPLAY CHAT ---------------- #

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- CHAT INPUT ---------------- #

prompt = st.chat_input("😊 Ask me anything...")

# Topic selected from sidebar
if "topic" in st.session_state:
    prompt = st.session_state.topic
    del st.session_state.topic

# ---------------- PROCESS MESSAGE ---------------- #

if prompt:
    # 1. Append user's message to state
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # 2. Display user's message
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Get and display assistant's response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            answer = ask_bot(prompt)
        st.markdown(answer)

    # 4. Append assistant's response to state
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )