import os
import sys
from pathlib import Path
from langgraph.graph import Graph
from transformers import pipeline
from utils.tavily_tools import get_tavily_tool

# 👉 Set your Tavily API Key properly
os.environ["TAVILY_API_KEY"] = "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"

# Configure environment
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Set up imports
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Research Agent to query with Tavily
class ResearchAgent:
    def __init__(self, search_tool):
        self.search_tool = search_tool

    def run(self, query):
        try:
            results = self.search_tool(query)
            return results
        except Exception as e:
            print(f"Error in ResearchAgent: {e}")
            return None

# Writer Agent to process the results and draft an answer
class WriterAgent:
    def __init__(self):
        self.pipeline = pipeline(
            'question-answering',
            model="distilbert-base-cased-distilled-squad",
            device="cpu"
        )

    def run(self, context, question):
        try:
            result = self.pipeline(question=question, context=context)
            return {
                "answer": result['answer'],
                "confidence": result['score']
            }
        except Exception as e:
            print(f"Error in WriterAgent: {e}")
            return None

class Workflow:
    def __init__(self):
        self.graph = Graph()
        self.search_tool = get_tavily_tool()
        self.researcher = ResearchAgent(self.search_tool)
        self.writer = WriterAgent()

        self.graph.add_node("researcher", self.researcher.run)
        self.graph.add_node("writer", self.writer.run)

        self.graph.set_entry_point("researcher")
        self.graph.add_edge("researcher", "writer")
        self.graph.add_edge("writer", "END")

    def run(self, query):
        try:
            result = self.graph.invoke({"input": query})
            return result
        except Exception as e:
            print(f"ERROR: Workflow failed: {e}")
            return None

if __name__ == "__main__":
    print("\nDevice set to use cpu\n")
    workflow = Workflow()
    query = "Latest AI in medicine research?"
    result = workflow.run(query)

    if result:
        print("\nFINAL ANSWER:\n", result)
    else:
        print("\nERROR: Workflow failed\n")
