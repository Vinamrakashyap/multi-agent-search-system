import re
from urllib.parse import urlparse

def get_domain_from_url(url: str) -> str:
    """Helper to extract domain name from a URL."""
    if not url:
        return "External Link"
    try:
        parsed_uri = urlparse(url)
        domain = parsed_uri.netloc
        if domain.startswith("www."):
            domain = domain[4:]
        return domain if domain else "External Link"
    except Exception:
        return "External Link"

def parse_sources(search_results_str: str) -> list:
    """Parses raw search results from the Search Agent into a list of dicts."""
    if not search_results_str:
        return []
    
    # Split by the divider
    raw_sources = search_results_str.split("\n----\n")
    sources = []
    
    for idx, raw in enumerate(raw_sources, 1):
        raw = raw.strip()
        if not raw:
            continue
        
        # Regex or line-by-line parsing
        title_match = re.search(r"Title:\s*(.*?)(?:\n|$)", raw, re.IGNORECASE)
        url_match = re.search(r"URL\s*:\s*(.*?)(?:\n|$)", raw, re.IGNORECASE)
        snippet_match = re.search(r"Snippet\s*:\s*(.*)", raw, re.IGNORECASE | re.DOTALL)
        
        title = title_match.group(1).strip() if title_match else "Untitled Source"
        url = url_match.group(1).strip() if url_match else ""
        snippet = snippet_match.group(1).strip() if snippet_match else ""
        
        # Clean snippet
        snippet = re.sub(r"^Snippet\s*:\s*", "", snippet, flags=re.IGNORECASE).strip()
        
        sources.append({
            "number": idx,
            "title": title,
            "url": url,
            "domain": get_domain_from_url(url),
            "preview": snippet
        })
    return sources

def parse_critic_feedback(feedback_str: str) -> dict:
    """Parses raw Critic Agent feedback into Score, Verdict, Strengths, and Areas to Improve."""
    if not feedback_str:
        return {
            "score": "N/A",
            "verdict": "No verdict available.",
            "strengths": [],
            "weaknesses": []
        }
    
    score = "N/A"
    strengths = []
    weaknesses = []
    verdict = ""
    
    # Parse Score
    score_match = re.search(r"Score:\s*([^\n]+)", feedback_str, re.IGNORECASE)
    if score_match:
        score = score_match.group(1).strip()
        
    # Standardize headers case insensitivity
    lower_feedback = feedback_str.lower()
    
    strengths_pos = lower_feedback.find("strengths:")
    improve_pos = lower_feedback.find("areas to improve:")
    verdict_pos = lower_feedback.find("one line verdict:")
    
    # Extract Strengths
    if strengths_pos != -1:
        end_pos = improve_pos if improve_pos != -1 else (verdict_pos if verdict_pos != -1 else len(feedback_str))
        strengths_chunk = feedback_str[strengths_pos + len("strengths:"):end_pos].strip()
        strengths = [
            line.strip().lstrip("-*• ").strip()
            for line in strengths_chunk.split("\n")
            if line.strip().lstrip("-*• ").strip()
        ]
        
    # Extract Weaknesses (Areas to Improve)
    if improve_pos != -1:
        end_pos = verdict_pos if verdict_pos != -1 else len(feedback_str)
        improve_chunk = feedback_str[improve_pos + len("areas to improve:"):end_pos].strip()
        weaknesses = [
            line.strip().lstrip("-*• ").strip()
            for line in improve_chunk.split("\n")
            if line.strip().lstrip("-*• ").strip()
        ]
        
    # Extract Verdict
    if verdict_pos != -1:
        verdict = feedback_str[verdict_pos + len("one line verdict:"):].strip()
        # Clean any trailing elements
        verdict = verdict.strip()
    else:
        # Fallback if no specific verdict label but text exists at the end
        lines = feedback_str.split("\n")
        if lines:
            verdict = lines[-1].strip()
            
    return {
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "verdict": verdict if verdict else "Review completed."
    }

def count_words(text: str) -> int:
    """Simple utility to count words in a block of text."""
    if not text:
        return 0
    return len(text.split())
