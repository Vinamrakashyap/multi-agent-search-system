import streamlit as st
import time
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain
from components.styles import inject_premium_styles
from components.hero import render_hero_landing, render_empty_state_suggestions
from components.sidebar import render_sidebar
from components.timeline import render_timeline
from components.metrics import render_metrics_dashboard
from components.cards import (
    render_report_view,
    render_sources_view,
    render_critic_view,
    render_architecture_page,
    render_agents_page
)
from components.history import init_history_state, save_to_history

# 1. Set Page Configuration (Must be first Streamlit command)
st.set_page_config(
    page_title="Research Swarm",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject CSS Style overrides
inject_premium_styles()

# 3. Initialize history and navigation session state keys
init_history_state()
if "search_input_val" not in st.session_state:
    st.session_state.search_input_val = ""
if "trigger_run" not in st.session_state:
    st.session_state.trigger_run = False

# 4. Streamlit Research Pipeline Step Execution (Timeline-integrated)
def run_streamlit_research(topic: str, timeline_placeholder):
    """Executes the research swarm while driving the custom timeline UI."""
    start_time = time.time()
    
    try:
        # Step 1: Search Agent active
        render_timeline(timeline_placeholder, search_state="running", reader_state="pending", writer_state="pending", critic_state="pending")
        
        search_agent = build_search_agent()
        search_result = search_agent.invoke({
            "messages" : [("user", f"Find recent, reliable and detailed information about : {topic}")]
        })
        search_results = search_result["messages"][-1].content
        
        # Step 2: Reader Agent active
        render_timeline(timeline_placeholder, search_state="completed", reader_state="running", writer_state="pending", critic_state="pending")
        
        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke({
            "messages": [
                ("user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{search_results[:800]}"
                )
            ]
        })
        scraped_content = reader_result["messages"][-1].content
        
        # Step 3: Writer Chain active
        render_timeline(timeline_placeholder, search_state="completed", reader_state="completed", writer_state="running", critic_state="pending")
        
        research_combined = (
            f"SEARCH RESULTS : \n {search_results} \n\n"
            f"DETAILED SCRAPED CONTENT  : \n {scraped_content} \n\n"
        )
        report = writer_chain.invoke({
            "topic" : topic,
            "research" : research_combined
        })
        
        # Step 4: Critic Chain active
        render_timeline(timeline_placeholder, search_state="completed", reader_state="completed", writer_state="completed", critic_state="running")
        
        feedback = critic_chain.invoke({
            "report": report
        })
        
        # Timeline completed
        render_timeline(timeline_placeholder, search_state="completed", reader_state="completed", writer_state="completed", critic_state="completed")
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return {
            "search_results": search_results,
            "scraped_content": scraped_content,
            "report": report,
            "feedback": feedback,
            "execution_time": execution_time
        }
        
    except Exception as e:
        st.markdown(f"""
        <div style="background-color: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 8px; padding: 16px; margin: 20px 0; color: #ef4444;">
            <strong>❌ Swarm Pipeline Error:</strong> {e}
        </div>
        """, unsafe_allow_html=True)
        return None

# 5. Render Sidebar Navigation & History
render_sidebar()

# 6. Main Dashboard Routing Router
selected_page = st.session_state.selected_nav

if selected_page == "Workspace":
    # Main search workspace flow
    if st.session_state.current_results is None:
        # Renders the clean homepage empty state
        render_hero_landing()
        
        # Center column layout for input box
        col_space_l, col_search, col_space_r = st.columns([1, 4, 1])
        run_btn = False
        
        with col_search:
            topic_input = st.text_input(
                "Search topic",
                value=st.session_state.search_input_val,
                placeholder="Ask Research Swarm anything...",
                label_visibility="collapsed",
                key="search_query_box"
            )
            
            # Space out button
            col_btn_l, col_btn, col_btn_r = st.columns([1.5, 1.2, 1.5])
            with col_btn:
                run_btn = st.button("Generate Research", type="primary", use_container_width=True)
        
        # Execute research pipeline if run triggered
        if (run_btn and topic_input) or (st.session_state.trigger_run and st.session_state.search_input_val):
            # Reset suggest-triggers
            active_topic = topic_input if run_btn else st.session_state.search_input_val
            st.session_state.trigger_run = False
            st.session_state.search_input_val = active_topic
            st.session_state.current_topic = active_topic
            
            # Replace empty space with loading timeline
            st.write("##")
            timeline_placeholder = st.empty()
            
            results = run_streamlit_research(active_topic, timeline_placeholder)
            if results:
                save_to_history(active_topic, results)
                st.rerun()
                
        # Suggestions grid (empty state)
        if not run_btn and not st.session_state.trigger_run:
            render_empty_state_suggestions()
            
    else:
        # Renders the calculated research report dashboard
        res = st.session_state.current_results
        topic = st.session_state.current_topic
        
        # Workspace header
        st.markdown(f"<span style='color:#3B82F6; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; font-weight:600;'>Workspace Results</span>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='font-family: Space Grotesk, sans-serif; font-size: 1.8rem; margin: 0 0 16px 0; color:#FAFAFA;'>{topic}</h2>", unsafe_allow_html=True)
        
        # Render metrics grid
        render_metrics_dashboard(
            search_results=res["search_results"],
            scraped_content=res["scraped_content"],
            report=res["report"],
            execution_time=res.get("execution_time", 0.0)
        )
        
        st.write("##")
        
        # Premium navigation tabs
        tab1, tab2, tab3 = st.tabs(["📝 Final Report", "⚖️ Critic Review", "🕵️ Reference Sources"])
        
        with tab1:
            render_report_view(topic, res["report"])
            
        with tab2:
            render_critic_view(res["feedback"])
            
        with tab3:
            render_sources_view(res["search_results"])

elif selected_page == "Architecture":
    # Show pipeline visual diagram flow
    render_architecture_page()

elif selected_page == "Agents":
    # Show detailed descriptions of agents in cards
    render_agents_page()

elif selected_page == "About":
    # Renders the tech stack and description page
    st.markdown("<h2 style='font-family: Space Grotesk, sans-serif; font-size: 1.8rem; margin-bottom: 8px;'>About Research Swarm</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #9CA3AF; font-size: 0.95rem; margin-bottom: 30px;'>An autonomous collaborative multi-agent framework designed for premium data acquisition and synthesis.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        ### The Swarm Thesis
        Standard search paradigms require manual parsing, reading, structuring, and validation. **Research Swarm** automates these processes via an orchestrated, consensus-driven sequence:
        
        1. **Search**: Targeted exploration across indices.
        2. **Read**: Automated noise decomposition (stripping tags, scripts).
        3. **Synthesize**: Structured writing based on context payloads.
        4. **Critique**: Independent auditing to score output and guide improvements.
        
        ### Technology Architecture
        - **Orchestration**: LangChain Core & Chain expressions.
        - **Models**: Google Gemini 1.5 Flash API.
        - **Search**: Tavily optimized research indexes.
        - **Parsing**: BeautifulSoup4 text scrapers.
        - **UI/UX**: Custom styled Streamlit architecture.
        """)