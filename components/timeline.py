import streamlit as st

def get_step_html(title: str, description: str, state: str, step_num: int) -> str:
    """Helper to generate HTML for a single timeline step based on its state."""
    icon = "○"
    badge_text = "Pending"
    item_class = "pending"
    
    if state == "completed":
        icon = "✓"
        badge_text = "Completed"
        item_class = "completed"
    elif state == "running":
        icon = "●"
        badge_text = "Running..."
        item_class = "active"
        
    return f"""
    <div class="timeline-item {item_class}">
        <div class="timeline-icon">{icon}</div>
        <div class="timeline-details">
            <h4 class="timeline-title">{title}</h4>
            <p class="timeline-desc">{description}</p>
        </div>
        <div class="timeline-badge">{badge_text}</div>
    </div>
    """

def render_timeline(placeholder, search_state="pending", reader_state="pending", writer_state="pending", critic_state="pending"):
    """Renders the execution timeline and active skeleton loading cards to the placeholder."""
    
    # Generate items
    step1 = get_step_html("Search Agent", "Querying trusted indices & collecting references...", search_state, 1)
    step2 = get_step_html("Reader Agent", "Parsing, filtering and scraping prime resource text...", reader_state, 2)
    step3 = get_step_html("Writer Agent", "Composing detailed research draft report...", writer_state, 3)
    step4 = get_step_html("Critic Agent", "Reviewing content, checking facts and rating quality...", critic_state, 4)
    
    # Layout of the timeline
    timeline_html = f"""
    <div class="timeline-container">
        <h4 style="font-family: 'Space Grotesk', sans-serif; text-align: center; margin: 0 0 20px 0; font-size: 1.15rem; color: #FAFAFA;">
            Research Pipeline Swarm
        </h4>
        {step1}
        <div class="timeline-connector"></div>
        {step2}
        <div class="timeline-connector"></div>
        {step3}
        <div class="timeline-connector"></div>
        {step4}
    </div>
    """
    
    # Skeleton loader card layout
    skeleton_html = """
    <div class="skeleton-card">
        <div class="skeleton-line title"></div>
        <div class="skeleton-line body-1"></div>
        <div class="skeleton-line body-2"></div>
        <div class="skeleton-line body-3"></div>
        <div class="skeleton-line body-4"></div>
    </div>
    """
    
    # Write to the empty placeholder
    with placeholder.container():
        st.markdown(timeline_html, unsafe_allow_html=True)
        st.markdown(skeleton_html, unsafe_allow_html=True)
