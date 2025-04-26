from utils.tavily_tools import get_tavily_tool
from langchain.agents import Tool
from transformers import pipeline
import os

class ResearchAgent:
    def __init__(self):
        self.pipeline = pipeline(
            'question-answering',
            model="distilbert-base-cased-distilled-squad",
            device="cpu"
        )

    def answer_question(self, context: str, question: str) -> dict:
        result = self.pipeline(question=question, context=context)
        return {
            "answer": result['answer'],
            "confidence": float(result['score'])
        }

def run_workflow(query: str):
    try:
        tavily_tool = get_tavily_tool()
        results = tavily_tool.run(query)
        context = "\n".join(f"{r['title']}: {r.get('content', '')}" for r in results["results"])
        agent = ResearchAgent()
        answer = agent.answer_question(context, query)
        print(f"Answer: {answer['answer']}")
        print(f"Confidence: {answer['confidence']}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    query = "Latest AI in medicine research?"
    run_workflow(query)
