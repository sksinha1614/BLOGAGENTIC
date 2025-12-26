# src/llms/groqllm.py
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise RuntimeError("GROQ_API_KEY not set")

        return ChatGroq(
            api_key=groq_api_key,
            model_name="llama-3.1-8b-instant"
        )
