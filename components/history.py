import streamlit as st

def init_history_state():
    """Initializes standard history keys inside session state."""
    if "history" not in st.session_state:
        st.session_state.history = {}
    if "current_topic" not in st.session_state:
        st.session_state.current_topic = ""
    if "current_results" not in st.session_state:
        st.session_state.current_results = None
    if "selected_nav" not in st.session_state:
        st.session_state.selected_nav = "Workspace"

def save_to_history(topic: str, results: dict):
    """Saves a research topic run and its corresponding outputs to session state."""
    if not st.session_state.history:
        st.session_state.history = {}
    st.session_state.history[topic] = results
    st.session_state.current_topic = topic
    st.session_state.current_results = results

def load_from_history(topic: str):
    """Loads a previously researched topic's data into active focus."""
    if st.session_state.history and topic in st.session_state.history:
        st.session_state.current_topic = topic
        st.session_state.current_results = st.session_state.history[topic]
        # Force navigation back to Workspace page when a history item is clicked
        st.session_state.selected_nav = "Workspace"

def clear_history():
    """Wipes all search history and current topic from session state."""
    st.session_state.history = {}
    st.session_state.current_topic = ""
    st.session_state.current_results = None
