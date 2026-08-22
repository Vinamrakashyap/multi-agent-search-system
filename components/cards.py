import streamlit as st
import html
from components.utils import parse_sources, parse_critic_feedback

def render_report_view(topic: str, report: str):
    """Renders the Markdown report with a header bar featuring Copy and Download buttons."""
    
    # Renders the control action bar using Streamlit columns
    col_title, col_copy, col_dl_md, col_dl_txt = st.columns([2.5, 1.1, 1.2, 1.2])
    
    with col_title:
        st.markdown(f"<h3 style='margin: 0; font-family: Space Grotesk, sans-serif; font-size: 1.3rem; color: #FAFAFA;'>Report: {topic}</h3>", unsafe_allow_html=True)
        
    with col_copy:
        # Embed custom self-contained JavaScript button to copy report
        escaped_report = html.escape(report)
        copy_html = f"""
        <textarea id="reportText" style="display:none;">{escaped_report}</textarea>
        <button onclick="navigator.clipboard.writeText(document.getElementById('reportText').value); this.innerText = 'Copied!'; setTimeout(() => this.innerText = 'Copy Report', 2000);" 
                style="width:100%; padding:10px; background-color:#111114; color:#FAFAFA; border:1px solid rgba(255,255,255,0.06); border-radius:10px; font-weight:500; font-family:'Plus Jakarta Sans',sans-serif; cursor:pointer; font-size: 0.85rem; transition:all 0.2s ease-in-out;"
                onmouseover="this.style.borderColor='#3B82F6'; this.style.color='#ffffff';"
                onmouseout="this.style.borderColor='rgba(255,255,255,0.06)'; this.style.color='#FAFAFA';">
            📋 Copy Report
        </button>
        """
        st.markdown(copy_html, unsafe_allow_html=True)
        
    with col_dl_md:
        st.download_button(
            label="📥 Markdown",
            data=report,
            file_name=f"research_{topic.replace(' ', '_').lower()}.md",
            mime="text/markdown",
            use_container_width=True
        )
        
    with col_dl_txt:
        st.download_button(
            label="📥 TXT Format",
            data=report,
            file_name=f"research_{topic.replace(' ', '_').lower()}.txt",
            mime="text/plain",
            use_container_width=True
        )
        
    st.write("---")
    
    # Display styled report content inside a container
    with st.container(border=True):
        st.markdown(report)

def render_sources_view(search_results_str: str):
    """Renders the sources list as a beautiful grid of individual cards."""
    sources = parse_sources(search_results_str)
    
    if not sources:
        st.markdown("<p style='font-size:0.9rem; color:#9CA3AF; font-style:italic;'>No references found.</p>", unsafe_allow_html=True)
        return
        
    cards_html = []
    for s in sources:
        card = f"""
        <div class="source-card-custom">
            <div>
                <div class="source-header-custom">
                    <span class="source-num-custom">#{s['number']}</span>
                    <span class="source-domain-custom">{s['domain']}</span>
                </div>
                <h4 class="source-title-custom">{s['title']}</h4>
                <p class="source-preview-custom">{s['preview']}</p>
            </div>
            <a href="{s['url']}" target="_blank" class="source-link-custom">Open Link ↗</a>
        </div>
        """
        cards_html.append(card)
        
    grid_html = f"""
    <div class="sources-container-custom">
        {"".join(cards_html)}
    </div>
    """
    st.markdown(grid_html, unsafe_allow_html=True)

def render_critic_view(feedback_str: str):
    """Parses Critic feedback output and displays it inside premium metric and list cards."""
    parsed = parse_critic_feedback(feedback_str)
    
    # 1. Header Overview Card
    st.markdown(f"""
    <div style="background-color: #111114; border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 24px; display: flex; align-items: center; gap: 24px; margin-bottom: 20px;">
        <div style="background: rgba(59, 130, 246, 0.05); border: 1px solid rgba(59, 130, 246, 0.2); width: 80px; height: 80px; border-radius: 50%; display: flex; flex-direction: column; justify-content: center; align-items: center; flex-shrink: 0;">
            <span style="font-size: 0.65rem; color: #9CA3AF; text-transform: uppercase; font-weight: 600; letter-spacing:0.05em;">Score</span>
            <span style="font-size: 1.4rem; font-family: 'Space Grotesk', sans-serif; font-weight: 700; color: #3B82F6;">{parsed.get('score', 'N/A')}</span>
        </div>
        <div>
            <h4 style="font-family: 'Space Grotesk', sans-serif; margin: 0 0 6px 0; color: #FAFAFA; font-size: 1.05rem;">Swarm Audit Verdict</h4>
            <p style="margin: 0; color: #9CA3AF; font-size: 0.9rem; font-style: italic; line-height: 1.45; opacity: 0.9;">"{parsed.get('verdict', 'Audit review completed successfully.')}"</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Strengths and Weaknesses Lists
    strengths_items = "".join([f"<li>{html.escape(item)}</li>" for item in parsed.get("strengths", [])])
    weaknesses_items = "".join([f"<li>{html.escape(item)}</li>" for item in parsed.get("weaknesses", [])])
    
    # Fallback placeholders if lists are empty
    if not strengths_items:
        strengths_items = "<li>No specific strengths highlighted by the critic.</li>"
    if not weaknesses_items:
        weaknesses_items = "<li>No specific weaknesses found. The writing is highly sound.</li>"
        
    critic_grid_html = f"""
    <div class="critic-grid-custom">
        <div style="background-color: #111114; border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 24px;">
            <h4 style="font-family: 'Space Grotesk', sans-serif; margin: 0 0 16px 0; color: #6366F1; display: flex; align-items: center; gap: 8px; font-size: 1rem;">
                <span style="display:inline-block; width: 8px; height: 8px; border-radius: 50%; background-color: #6366F1;"></span>
                Strengths
            </h4>
            <ul class="critic-bullet-list">
                {strengths_items}
            </ul>
        </div>
        
        <div style="background-color: #111114; border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 24px;">
            <h4 style="font-family: 'Space Grotesk', sans-serif; margin: 0 0 16px 0; color: #3B82F6; display: flex; align-items: center; gap: 8px; font-size: 1rem;">
                <span style="display:inline-block; width: 8px; height: 8px; border-radius: 50%; background-color: #3B82F6;"></span>
                Areas to Improve
            </h4>
            <ul class="critic-bullet-list">
                {weaknesses_items}
            </ul>
        </div>
    </div>
    """
    
    st.markdown(critic_grid_html, unsafe_allow_html=True)

def render_architecture_page():
    """Renders a beautiful visual workflow flow representing the swarm execution stages."""
    st.markdown("<h2 style='font-family: Space Grotesk, sans-serif; font-size: 1.8rem; margin-bottom: 8px;'>System Architecture</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #9CA3AF; font-size: 0.95rem; margin-bottom: 30px;'>A visual breakdown of how data flows through our autonomous multi-agent research sequence.</p>", unsafe_allow_html=True)
    
    steps = [
        {"title": "User Query Input", "subtitle": "Topic is submitted to the coordinator workspace.", "type": "input", "bg": "rgba(255, 255, 255, 0.02)", "border": "rgba(255, 255, 255, 0.08)"},
        {"title": "🔍 Search Agent", "subtitle": "Executes optimized Google queries via Tavily API and aggregates relevant page references.", "type": "agent", "bg": "rgba(59, 130, 246, 0.03)", "border": "rgba(59, 130, 246, 0.2)"},
        {"title": "📖 Reader Agent", "subtitle": "Selects the most statistically relevant source, scrapes the raw text content via BeautifulSoup, and filters noise.", "type": "agent", "bg": "rgba(59, 130, 246, 0.03)", "border": "rgba(59, 130, 246, 0.2)"},
        {"title": "✍️ Writer Agent", "subtitle": "Synthesizes web snippets and raw scraped materials into a structured markdown report template.", "type": "chain", "bg": "rgba(99, 102, 241, 0.03)", "border": "rgba(99, 102, 241, 0.2)"},
        {"title": "⚖️ Critic Agent", "subtitle": "Reviews draft reports and scores them against factuality, spelling, formatting, and layout standards.", "type": "chain", "bg": "rgba(99, 102, 241, 0.03)", "border": "rgba(99, 102, 241, 0.2)"},
        {"title": "Audited Output Report", "subtitle": "Markdown file with a scorecard is presented to the dashboard.", "type": "output", "bg": "rgba(255, 255, 255, 0.02)", "border": "rgba(255, 255, 255, 0.08)"}
    ]
    
    # Render flow cards vertically
    for idx, step in enumerate(steps):
        st.markdown(f"""
        <div style="background-color: {step['bg']}; border: 1px solid {step['border']}; border-radius: 12px; padding: 20px; max-width: 650px; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <h4 style="font-family: 'Space Grotesk', sans-serif; margin: 0; color: #FAFAFA; font-size: 1.05rem;">{step['title']}</h4>
                <span style="font-size: 0.68rem; text-transform: uppercase; color: #9CA3AF; background-color: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); padding: 2px 8px; border-radius: 6px; font-weight: 500;">
                    {step['type']}
                </span>
            </div>
            <p style="margin: 0; font-size: 0.85rem; color: #9CA3AF; line-height: 1.45;">{step['subtitle']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Draw connector arrow unless it is the final step
        if idx < len(steps) - 1:
            st.markdown("""
            <div style="text-align: center; margin: 8px 0; color: #9CA3AF; opacity: 0.4; font-size: 1.2rem;">
                ↓
            </div>
            """, unsafe_allow_html=True)

def render_agents_page():
    """Renders information cards detailing the configuration and tools of each Swarm Agent."""
    st.markdown("<h2 style='font-family: Space Grotesk, sans-serif; font-size: 1.8rem; margin-bottom: 8px;'>Agent Roster</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #9CA3AF; font-size: 0.95rem; margin-bottom: 30px;'>An in-depth review of each agent, their scope of work, their tools, and data processing models.</p>", unsafe_allow_html=True)
    
    agents = [
        {
            "name": "🔍 Search Agent",
            "purpose": "Web research & Information Gathering",
            "input": "Search queries representing the user research topic",
            "output": "Aggregated title list, webpage URL directories, and contextual summary text blocks",
            "tools": "Tavily Search API (`web_search` tool)",
            "desc": "Uses Tavily's dedicated LLM search index. Resolves fresh facts, news, and deep statistics, filtering away spam pages to maximize research accuracy.",
            "color": "#3B82F6"
        },
        {
            "name": "📖 Reader Agent",
            "purpose": "Resource Scraping & Noise Filtering",
            "input": "List of URLs compiled by the Search Agent",
            "output": "Clean text payload extracted from the target webpage (up to 3,000 characters)",
            "tools": "BeautifulSoup Parser & Requests Session (`scrape_url` tool)",
            "desc": "Analyzes raw search index snippets and loads the highest matching page. Strips CSS stylesheets, JS scripts, headers, navigation bars, and footers.",
            "color": "#3B82F6"
        },
        {
            "name": "✍️ Writer Agent",
            "purpose": "Information Synthesis & Composition",
            "input": "Unified payload containing search summaries and scraped webpage content",
            "output": "A draft report covering an introduction, key findings, conclusions, and references",
            "tools": "Gemini 1.5 Flash Model (`writer_chain` template)",
            "desc": "Orchestrates research facts. Condenses multi-source raw material, establishes semantic coherence, and compiles a comprehensive, readable report.",
            "color": "#6366F1"
        },
        {
            "name": "⚖️ Critic Agent",
            "purpose": "Quality Auditing & Scorecarding",
            "input": "Draft report written by the Writer Agent",
            "output": "Constructive report card containing a rating (X/10), key strengths, areas to improve, and verdict",
            "tools": "Gemini 1.5 Flash Model (`critic_chain` template)",
            "desc": "Impartial reviewer. Audits the factual integrity, formatting, spelling, and readability constraints, ensuring reports align with publication quality standards.",
            "color": "#6366F1"
        }
    ]
    
    # Display agents in a 2x2 grid
    cols = st.columns([1, 1])
    for idx, agent in enumerate(agents):
        col_idx = idx % 2
        with cols[col_idx]:
            with st.container(border=True):
                st.markdown(f"""
                <div style="border-left: 3px solid {agent['color']}; padding-left: 12px; margin-bottom: 16px;">
                    <h4 style="font-family: 'Space Grotesk', sans-serif; margin: 0; font-size: 1.15rem; color: #FAFAFA;">{agent['name']}</h4>
                    <span style="font-size: 0.72rem; color: #9CA3AF; text-transform: uppercase; font-weight: 500; letter-spacing: 0.05em;">{agent['purpose']}</span>
                </div>
                
                <p style="font-size: 0.85rem; color: #9CA3AF; margin-bottom: 14px; line-height: 1.45;">
                    {agent['desc']}
                </p>
                
                <div style="font-size: 0.8rem; line-height: 1.6;">
                    <div style="margin-bottom: 6px;">
                        <span style="color: #9CA3AF; font-weight: 500;">📥 Input:</span>
                        <code style="background-color: rgba(255,255,255,0.03); padding: 2px 6px; border-radius: 4px; color: #FAFAFA; font-family: monospace; font-size: 0.75rem;">{agent['input']}</code>
                    </div>
                    <div style="margin-bottom: 6px;">
                        <span style="color: #9CA3AF; font-weight: 500;">📤 Output:</span>
                        <code style="background-color: rgba(255,255,255,0.03); padding: 2px 6px; border-radius: 4px; color: #FAFAFA; font-family: monospace; font-size: 0.75rem;">{agent['output']}</code>
                    </div>
                    <div>
                        <span style="color: #9CA3AF; font-weight: 500;">🛠️ Active Tools:</span>
                        <code style="background-color: rgba(59,130,246,0.05); padding: 2px 6px; border-radius: 4px; color: #3B82F6; font-family: monospace; font-size: 0.75rem;">{agent['tools']}</code>
                    </div>
                </div>
                """, unsafe_allow_html=True)
