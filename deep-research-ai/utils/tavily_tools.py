from tavily import TavilyClient
from langchain.agents import Tool
import os

def get_tavily_tool():
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def search(query: str) -> dict:
        results = client.search(
            query=query,
            search_depth="basic",
            max_results=3
        )
        return {
            "query": query,
            "results": [{
                "title": r["title"],
                "content": r.get("content", "")[:300],
                "url": r["url"]
            } for r in results.get("results", [])]
        }

    return Tool.from_function(
        func=search,
        name="TavilySearch",
        description="Research tool"
    )
