import uvicorn 
from fastapi import FastAPI,Request
from src.graphs.graph_builder import GraphBuilder
from src.states.blogstate import BlogState
from src.llms.groqllm import GroqLLM

import os
from dotenv import load_dotenv

load_dotenv()

app=FastAPI()

# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

##API's

@app.post("/blogs")
async def blog(request: Request):
    data = await request.json()
    topic = data.get("topic")

    if not topic:
        return {"error": "topic is required"}

    llm = GroqLLM().get_llm()
    graph = GraphBuilder(llm).build_topic_graph()

    state = graph.invoke({
        "topic": topic,
        "blog": {"title": "", "content": ""},
        "current_language": "en"
    })

    return {"data": state}


if __name__=="__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)

    
    
