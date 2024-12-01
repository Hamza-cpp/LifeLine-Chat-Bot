from llm_embedding import embeddings
from langchain_community.vectorstores import FAISS

vector_store = FAISS(embedding_function=embeddings)