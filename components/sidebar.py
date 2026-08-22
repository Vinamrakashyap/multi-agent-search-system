import streamlit as st
from components.history import load_from_history

def render_sidebar():
    """Renders the minimal navigation menu, history, and swarm roster in the sidebar."""
    with st.sidebar:
        # 1. Swarm Branding
        st.markdown("""
        <div style="padding: 15px 0 25px 0; border-bottom: 1px solid rgba(255,255,255,0.06); margin-bottom: 20px;">
            <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.25rem; font-weight: 600; margin: 0; color: #FAFAFA; display: flex; align-items: center; gap: 8px;">
                <span style="color: #3B82F6;">🤖</span> Research Swarm
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # 2. Navigation Menu (Native Buttons)
        # Using type="primary" to highlight the selected navigation item
        nav_options = [
            ("💻 Workspace", "Workspace"),
            ("🗺️ Architecture", "Architecture"),
            ("🤖 Agents Roster", "Agents"),
            ("ℹ️ About Swarm", "About")
        ]
        
        st.markdown("<p style='font-size:0.75rem; text-transform:uppercase; color:#9CA3AF; letter-spacing:0.05em; font-weight:600; margin-bottom:8px;'>Navigation</p>", unsafe_allow_html=True)
        
        for label, val in nav_options:
            is_active = st.session_state.selected_nav == val
            btn_type = "primary" if is_active else "secondary"
            
            if st.button(label, key=f"nav_{val}", type=btn_type, use_container_width=True):
                st.session_state.selected_nav = val
                st.rerun()
                
        st.write("---")
        
        # 3. Research History
        st.markdown("<p style='font-size:0.75rem; text-transform:uppercase; color:#9CA3AF; letter-spacing:0.05em; font-weight:600; margin-bottom:8px;'>Research History</p>", unsafe_allow_html=True)
        
        if st.session_state.history:
            # Render history items
            for topic in list(st.session_state.history.keys()):
                # Mark as active if it's the currently focused topic in Workspace
                is_active_topic = (st.session_state.current_topic == topic and st.session_state.selected_nav == "Workspace")
                btn_type = "primary" if is_active_topic else "secondary"
                
                # Checkbox / minimal clickable text
                if st.button(topic, key=f"hist_{topic}", type=btn_type, use_container_width=True):
                    load_from_history(topic)
                    st.rerun()
        else:
            st.markdown("<p style='font-size:0.8rem; color:#9CA3AF; font-style:italic;'>No history in session.</p>", unsafe_allow_html=True)
            
        st.write("---")
        st.markdown("<div style='font-size:0.75rem; color:#9CA3AF; text-align:center;'>Research Swarm v2.0</div>", unsafe_allow_html=True)
