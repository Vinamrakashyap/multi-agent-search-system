from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from rich import print
from dotenv import load_dotenv
load_dotenv()

tavily = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))

@tool
#to create a tool make sure to define a function. to convert function to tool we'll use tool operator @tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic. Return Titles, Urls and Snippets."""
    response = tavily.search(query=query, max_results=5)

    formatted = []

    for result in response["results"]:
        formatted.append(
            f"""Title: {result['title']}\n URL : {result['url']}\n Snippet : {result['content'][:300]}\n"""
        )
    return "\n----\n".join(formatted)



@tool
def scrape_url(url : str)->str:
    """scrape and return clean text content from a given url for deeper reading."""
    try:
        resp = requests.get(url, timeout = 8, headers = {"User-Agent" : "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip = True)[:3000]
    except Exception as e:
        return f"could not scrap URL : {str(e)}"