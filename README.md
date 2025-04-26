Here’s your complete **`README.md`** — clean and ready to upload:

---

# Deep Research AI

This project builds a **Dual-Agent Research System** that can search the web, extract information, and answer queries intelligently. It uses **Tavily API**, **LangChain**, **LangGraph**, and **Transformers**.

## Features
- Search the web using Tavily API.
- Analyze and answer queries based on the search results.
- Modular design with utilities and agents separated.
- Supports future extensions like citation tracking, multi-hop reasoning, etc.

## Tech Stack
- Python 3
- Tavily API
- LangChain
- LangGraph
- HuggingFace Transformers (DistilBERT QA model)
- TensorFlow

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/deep-research-ai.git
cd deep-research-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, install manually:
```bash
pip install langchain tavily-python tensorflow transformers langgraph
```

### 3. Add API Key
Create a file named `.env` in the root directory and add your Tavily API Key:
```env
TAVILY_API_KEY=your_tavily_key_here
```

### 4. Run the Project
```bash
python agents/working.py
```

It will ask a question (like "Latest AI in medicine research?"), search online, and output an answer based on the retrieved data.

---

## Folder Structure

```
deep-research-ai/
├── agents/
│   ├── working.py          # Main entry point
│   └── dual_agent.py       # (Optional) Dual agent management
│
├── utils/
│   └── tavily_tools.py     # Tavily API integration
│
├── .env                    # API keys
├── requirements.txt        # Package dependencies
└── README.md               # Project guide
```

---

## Example Output

```
Device set to use CPU

User Query: Latest AI in medicine research?
Crawling web for research...
Sources Retrieved: 3

FINAL ANSWER (Confidence: 92%):
AI is transforming medicine with advances in drug discovery, diagnostics, and personalized treatments.
```

---

## Notes
- If you see TensorFlow warnings, they are safe to ignore.
- If using **Anaconda**, make sure the correct environment is activated.
- Currently runs on CPU — GPU acceleration is optional.

---

## License

This project is licensed under the MIT License.

---

✅ **Now you just copy this and save it as a `README.md` file in your project.**

---

Would you also like me to create a sample `requirements.txt` file for you in one go too? 🚀  
(so that your setup becomes even faster)
