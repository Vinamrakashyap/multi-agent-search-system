import streamlit as st
from components.utils import parse_sources, count_words

def render_metrics_dashboard(search_results: str, scraped_content: str, report: str, execution_time: float):
    """Calculates and renders real computed metrics in a premium grid."""
    
    # 1. Calculate metrics
    sources = parse_sources(search_results)
    sources_count = len(sources)
    
    # Check if scraping succeeded
    is_scraped = scraped_content and not scraped_content.strip().startswith("could not scrap")
    urls_parsed = 1 if is_scraped else 0
    
    # Count report words
    words_count = count_words(report)
    
    # Format time
    time_str = f"{execution_time:.1f}s"
    
    # 2. Render cards using responsive CSS grid defined in styles.py
    metrics_html = f"""
    <div class="metrics-container">
        <div class="metric-card-custom">
            <div class="metric-title">Sources Found</div>
            <div class="metric-value">{sources_count}</div>
            <div class="metric-sub">Verified web references</div>
        </div>
        <div class="metric-card-custom">
            <div class="metric-title">URLs Parsed</div>
            <div class="metric-value">{urls_parsed}</div>
            <div class="metric-sub">Scraped for deep text</div>
        </div>
        <div class="metric-card-custom">
            <div class="metric-title">Execution Time</div>
            <div class="metric-value">{time_str}</div>
            <div class="metric-sub">Swarm consensus speed</div>
        </div>
        <div class="metric-card-custom">
            <div class="metric-title">Words Generated</div>
            <div class="metric-value">{words_count:,}</div>
            <div class="metric-sub">Report length generated</div>
        </div>
    </div>
    """
    
    st.markdown(metrics_html, unsafe_allow_html=True)
