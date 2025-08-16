import streamlit as st
from model import generate_response

# Page configuration
st.set_page_config(
    page_title="🎓 GPT-2 Medium Chatbot",
    page_icon="🤖",
    layout="wide",
)

# App header
st.title("🤖 GPT-2 Medium Chatbot")
st.markdown(
    """
    Ask me anything related to any topic or just chat for fun!  
    I will try to give coherent and interesting answers.  
    """
)

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_area("Your question or prompt:", height=100)

# Generate response button
if st.button("Send"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            response = generate_response(user_input)
        # Add to chat history
        st.session_state.history.append({"user": user_input, "bot": response})
        user_input = ""

# Display chat history
for chat in reversed(st.session_state.history):
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")

# Footer
st.markdown(
    """
    <div style="text-align:center; font-size:12px; color:gray;">
    Powered by GPT-2 Medium | Streamlit App
    </div>
    """,
    unsafe_allow_html=True,
)
