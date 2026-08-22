import streamlit as st

def inject_premium_styles():
    """Injects custom CSS to style native Streamlit elements and custom containers."""
    st.markdown("""
    <style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    /* Global settings */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
        background-color: #09090B !important;
        color: #FAFAFA !important;
    }

    /* Headings styling */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #FAFAFA !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em !important;
    }

    /* Hide standard Streamlit header line and footer */
    header[data-testid="stHeader"] {
        background-color: rgba(9, 9, 11, 0.7) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06) !important;
    }
    
    footer {
        display: none !important;
        visibility: hidden !important;
    }

    /* Sidebar customization */
    section[data-testid="stSidebar"] {
        background-color: #111114 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
    }
    
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.5rem !important;
    }

    /* Input fields overrides */
    div[data-testid="stTextInput"] input {
        background-color: #111114 !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        color: #FAFAFA !important;
        border-radius: 10px !important;
        padding: 12px 18px !important;
        font-size: 15px !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        transition: all 0.2s ease-in-out !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 1px #3B82F6 !important;
    }

    /* Button overrides */
    div.stButton > button {
        background-color: #111114 !important;
        color: #FAFAFA !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: 500 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        transition: all 0.2s ease-in-out !important;
        width: 100%;
        text-align: center;
    }
    div.stButton > button:hover {
        background-color: #16161b !important;
        border-color: #3B82F6 !important;
        color: #ffffff !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
    }
    
    /* Primary buttons */
    div.stButton > button[data-testid="baseButton-primary"] {
        background: linear-gradient(135deg, #3B82F6 0%, #6366F1 100%) !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 600 !important;
    }
    div.stButton > button[data-testid="baseButton-primary"]:hover {
        background: linear-gradient(135deg, #4f91ff 0%, #7679ff 100%) !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3) !important;
        transform: translateY(-1px) !important;
    }

    /* Native Download Button Style */
    div[data-testid="stDownloadButton"] button {
        background-color: #111114 !important;
        color: #FAFAFA !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: 500 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        transition: all 0.2s ease-in-out !important;
        width: 100%;
    }
    div[data-testid="stDownloadButton"] button:hover {
        background-color: #16161b !important;
        border-color: #3B82F6 !important;
        color: #ffffff !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
    }

    /* Override tabs to look like a modern pill select */
    div[data-baseweb="tab-list"] {
        background-color: #111114 !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 10px !important;
        padding: 4px !important;
        gap: 6px !important;
        width: fit-content !important;
        margin-bottom: 20px !important;
    }
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        border: none !important;
        border-radius: 8px !important;
        color: #9CA3AF !important;
        padding: 8px 18px !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        transition: all 0.2s ease !important;
        height: auto !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: rgba(59, 130, 246, 0.1) !important;
        color: #3B82F6 !important;
        font-weight: 600 !important;
    }
    button[data-baseweb="tab"]:hover {
        color: #FAFAFA !important;
    }
    div[data-baseweb="tab-border-line"] {
        display: none !important;
    }

    /* Streamlit structural card styling (st.container(border=True)) */
    div[data-testid="stVerticalBlockBorderDiv"] {
        background-color: #111114 !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 12px !important;
        padding: 24px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #09090B;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.2);
    }

    /* Timeline styles */
    .timeline-container {
        display: flex;
        flex-direction: column;
        gap: 16px;
        max-width: 600px;
        margin: 20px auto;
        padding: 20px;
        background: #111114;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
    }
    
    .timeline-item {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 12px 16px;
        border-radius: 8px;
        border: 1px solid transparent;
        transition: all 0.3s ease;
    }
    
    .timeline-item.completed {
        background-color: rgba(99, 102, 241, 0.03);
        border-color: rgba(99, 102, 241, 0.08);
    }
    
    .timeline-item.active {
        background-color: rgba(59, 130, 246, 0.05);
        border-color: rgba(59, 130, 246, 0.2);
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.05);
    }
    
    .timeline-item.pending {
        opacity: 0.4;
    }
    
    .timeline-icon {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 0.85rem;
    }
    
    .completed .timeline-icon {
        background-color: rgba(99, 102, 241, 0.1);
        color: #6366F1;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    
    .active .timeline-icon {
        background-color: rgba(59, 130, 246, 0.1);
        color: #3B82F6;
        border: 1px solid #3B82F6;
        animation: pulse-icon 1.5s infinite alternate;
    }
    
    .pending .timeline-icon {
        background-color: rgba(255, 255, 255, 0.03);
        color: #9CA3AF;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    .timeline-details {
        flex: 1;
    }
    
    .timeline-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        margin: 0;
        color: #FAFAFA;
    }
    
    .timeline-desc {
        font-size: 0.8rem;
        color: #9CA3AF;
        margin: 2px 0 0 0;
    }
    
    .timeline-badge {
        font-size: 0.75rem;
        font-weight: 500;
        padding: 4px 8px;
        border-radius: 6px;
    }
    
    .completed .timeline-badge {
        background-color: rgba(99, 102, 241, 0.1);
        color: #6366F1;
    }
    
    .active .timeline-badge {
        background-color: rgba(59, 130, 246, 0.1);
        color: #3B82F6;
    }
    
    .pending .timeline-badge {
        background-color: rgba(255, 255, 255, 0.03);
        color: #9CA3AF;
    }
    
    .timeline-connector {
        width: 2px;
        height: 16px;
        background-color: rgba(255, 255, 255, 0.06);
        margin-left: 29px;
    }
    
    @keyframes pulse-icon {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.4); }
        100% { transform: scale(1.05); box-shadow: 0 0 8px 2px rgba(59, 130, 246, 0.2); }
    }

    /* Skeleton loaders */
    .skeleton-card {
        background-color: #111114;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 24px;
        max-width: 800px;
        margin: 20px auto;
    }
    
    .skeleton-line {
        background-color: rgba(255, 255, 255, 0.04);
        height: 10px;
        border-radius: 5px;
        margin-bottom: 12px;
        animation: skeleton-pulse 1.5s infinite ease-in-out;
    }
    
    .skeleton-line.title {
        width: 35%;
        height: 18px;
        margin-bottom: 24px;
        background-color: rgba(255, 255, 255, 0.06);
    }
    
    .skeleton-line.body-1 { width: 95%; }
    .skeleton-line.body-2 { width: 88%; }
    .skeleton-line.body-3 { width: 92%; }
    .skeleton-line.body-4 { width: 65%; }
    
    @keyframes skeleton-pulse {
        0% { opacity: 0.5; }
        50% { opacity: 0.25; }
        100% { opacity: 0.5; }
    }

    /* Custom Grids & Responsiveness */
    .metrics-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 16px;
        margin: 20px 0;
        width: 100%;
    }
    
    .metric-card-custom {
        background-color: #111114;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 20px;
        text-align: left;
        transition: all 0.2s ease-in-out;
    }
    
    .metric-card-custom:hover {
        border-color: rgba(255, 255, 255, 0.1);
        transform: translateY(-1px);
    }
    
    .metric-title {
        font-size: 0.75rem;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 8px;
        font-weight: 500;
    }
    
    .metric-value {
        font-size: 1.85rem;
        font-weight: 700;
        font-family: 'Space Grotesk', sans-serif;
        color: #FAFAFA;
        line-height: 1.2;
    }
    
    .metric-sub {
        font-size: 0.75rem;
        color: #9CA3AF;
        opacity: 0.65;
        margin-top: 4px;
    }

    /* Suggestion cards / Empty State */
    .suggestions-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 16px;
        margin-top: 24px;
        width: 100%;
    }

    /* Sources page elements */
    .sources-container-custom {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 16px;
        width: 100%;
        margin-top: 16px;
    }
    
    @media (max-width: 640px) {
        .sources-container-custom {
            grid-template-columns: 1fr;
        }
    }
    
    .source-card-custom {
        background-color: #111114;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 200px;
        transition: all 0.2s ease-in-out;
    }
    
    .source-card-custom:hover {
        border-color: #3B82F6;
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }
    
    .source-header-custom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }
    
    .source-num-custom {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.8rem;
        font-weight: 700;
        color: #3B82F6;
        background: rgba(59, 130, 246, 0.08);
        padding: 2px 8px;
        border-radius: 6px;
        border: 1px solid rgba(59, 130, 246, 0.15);
    }
    
    .source-domain-custom {
        font-size: 0.75rem;
        color: #9CA3AF;
        font-weight: 500;
    }
    
    .source-title-custom {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1rem;
        font-weight: 600;
        color: #FAFAFA;
        margin: 0 0 8px 0;
        line-height: 1.4;
        height: 2.8em;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    
    .source-preview-custom {
        font-size: 0.8rem;
        color: #9CA3AF;
        line-height: 1.5;
        margin: 0 0 16px 0;
        height: 4.5em;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        opacity: 0.85;
    }
    
    .source-link-custom {
        align-self: flex-start;
        font-size: 0.8rem;
        font-weight: 600;
        color: #3B82F6;
        text-decoration: none !important;
        background: rgba(59, 130, 246, 0.04);
        border: 1px solid rgba(59, 130, 246, 0.15);
        padding: 6px 12px;
        border-radius: 6px;
        transition: all 0.2s ease;
    }
    
    .source-link-custom:hover {
        background: rgba(59, 130, 246, 0.12);
        border-color: #3B82F6;
        color: #ffffff !important;
    }

    /* Critic Review CSS */
    .critic-container-custom {
        display: flex;
        flex-direction: column;
        gap: 16px;
        width: 100%;
    }
    
    .critic-grid-custom {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        width: 100%;
    }
    
    @media (max-width: 768px) {
        .critic-grid-custom {
            grid-template-columns: 1fr;
        }
    }
    
    .critic-bullet-list {
        margin: 0;
        padding-left: 18px;
        font-size: 0.88rem;
        line-height: 1.6;
        color: #FAFAFA;
    }
    
    .critic-bullet-list li {
        margin-bottom: 8px;
    }

    /* Sidebar quick branding */
    .sidebar-brand {
        padding: 10px 0 20px 0;
        text-align: left;
    }
    .sidebar-brand h3 {
        margin: 0;
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 1.3rem !important;
        color: #FAFAFA !important;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Navigation styling override */
    .sidebar-nav-btn {
        text-align: left !important;
        justify-content: flex-start !important;
        background-color: transparent !important;
        border: none !important;
        border-radius: 6px !important;
        color: #9CA3AF !important;
        padding: 8px 12px !important;
        font-size: 0.9rem !important;
        transition: all 0.2s ease !important;
    }
    .sidebar-nav-btn.active {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #FAFAFA !important;
        border-left: 2px solid #3B82F6 !important;
        border-radius: 0 6px 6px 0 !important;
        font-weight: 500 !important;
    }
    .sidebar-nav-btn:hover {
        background-color: rgba(255, 255, 255, 0.03) !important;
        color: #FAFAFA !important;
    }
    </style>
    """, unsafe_allow_html=True)
