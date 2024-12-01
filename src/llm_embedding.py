import os
import getpass

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

# your Groq Api key from console.groq.com
if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

# Initialize llm and embedding
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=158,
    timeout=None,
    max_retries=2,
)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
