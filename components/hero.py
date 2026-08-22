import streamlit as st

def render_hero_landing():
    """Renders the top branding, subtitle, and agent workflow pills."""
    st.markdown("""
    <div style="text-align: center; padding: 40px 0 20px 0;">
        <h1 style="font-family: 'Space Grotesk', sans-serif; font-size: 3rem; font-weight: 700; margin-bottom: 0.35rem; color: #FAFAFA; letter-spacing: -0.02em;">
            Research Swarm
        </h1>
        <p style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.1rem; color: #9CA3AF; margin-bottom: 1.8rem; font-weight: 400; letter-spacing: 0.05em; text-transform: uppercase;">
            Autonomous Multi-Agent Research System
        </p>
        <div style="display: flex; justify-content: center; gap: 12px; margin-bottom: 2rem; flex-wrap: wrap;">
            <span style="font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; font-weight: 500; color: #3B82F6; background: rgba(59, 130, 246, 0.05); border: 1px solid rgba(59, 130, 246, 0.12); padding: 4px 12px; border-radius: 100px;">Search.</span>
            <span style="font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; font-weight: 500; color: #6366F1; background: rgba(99, 102, 241, 0.05); border: 1px solid rgba(99, 102, 241, 0.12); padding: 4px 12px; border-radius: 100px;">Read.</span>
            <span style="font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; font-weight: 500; color: #3B82F6; background: rgba(59, 130, 246, 0.05); border: 1px solid rgba(59, 130, 246, 0.12); padding: 4px 12px; border-radius: 100px;">Synthesize.</span>
            <span style="font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; font-weight: 500; color: #6366F1; background: rgba(99, 102, 241, 0.05); border: 1px solid rgba(99, 102, 241, 0.12); padding: 4px 12px; border-radius: 100px;">Critique.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_empty_state_suggestions():
    """Renders the clickable quick start suggestion cards on the empty homepage."""
    st.write("##")
    st.markdown("""
    <div style="margin-bottom: 12px;">
        <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; color: #FAFAFA; font-weight: 600; text-align: center; margin-bottom: 24px;">
            Suggested Research Topics
        </h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Suggestion data
    suggestions = [
        {"topic": "Recent AI Trends", "desc": "Frontier model updates, scaling laws, and hardware progress.", "emoji": "🚀"},
        {"topic": "Climate Change", "desc": "Atmospheric metrics, carbon capture tech, and mitigation policies.", "emoji": "🌍"},
        {"topic": "Quantum Computing", "desc": "Silicon spin qubits, error correction breakthroughs, and industry roadmap.", "emoji": "💻"},
        {"topic": "Indian Economy", "desc": "Fiscal growth corridors, manufacturing shift, and tech services expansion.", "emoji": "📈"},
        {"topic": "LLMs & RAG", "desc": "Vector database structures, chunking techniques, and fine-tuning trends.", "emoji": "🧠"},
        {"topic": "Autonomous AI Agents", "desc": "Multi-agent orchestration frameworks, tool usage, and loop feedback systems.", "emoji": "🤖"}
    ]
    
    # Render suggestion grid
    cols = st.columns([1, 1, 1])
    
    for idx, sugg in enumerate(suggestions):
        col_idx = idx % 3
        with cols[col_idx]:
            # Create a styled card container
            with st.container(border=True):
                st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                    <span style="font-size: 1.3rem;">{sugg['emoji']}</span>
                    <strong style="font-family: 'Space Grotesk', sans-serif; font-size: 0.95rem; color: #FAFAFA;">{sugg['topic']}</strong>
                </div>
                <p style="font-size: 0.78rem; color: #9CA3AF; margin-bottom: 14px; min-height: 38px; line-height: 1.4;">
                    {sugg['desc']}
                </p>
                """, unsafe_allow_html=True)
                
                # Render native clickable button
                if st.button("Explore Topic →", key=f"sugg_btn_{idx}", use_container_width=True):
                    # Set the state and trigger run
                    st.session_state.search_input_val = sugg['topic']
                    st.session_state.trigger_run = True
                    st.rerun()
