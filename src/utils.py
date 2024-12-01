from collections.abc import Iterator
import glob
from typing import Any
from llm_embedding import embeddings

from langchain.document_loaders import TextLoader
from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.vectorstores.base import VectorStoreRetriever
from tqdm import tqdm


def chunks(input_list: list[Document], chunk_size: int) -> Iterator[list[Document]]:
    """
    This function divides a list into smaller lists (chunks) of a specified size.

    Args:
        input_list (list): The original list that needs to be split into chunks.
        chunk_size (int): The maximum number of elements each chunk should contain.

    Yields:
        Iterator[list[Document]]: A generator that produces each chunk of the list one by one.
    """
   
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i : i + chunk_size]


def load_docs_from_directory(dir_path: str) -> list[Document]:
    """Loads a series of docs from a directory.

    Args:
      dir_path: The path to the directory containing the docs.

    Returns:
      A list of the docs in the directory.
    """

    docs = []
    for file_path in glob.glob(dir_path):
        loader = TextLoader(file_path)
        docs = docs + loader.load()
    return docs


def create_retriever(top_k_results: int, dir_path: str) -> VectorStoreRetriever:
    """Create a recipe retriever from a list of top results and a list of web pages.

    Args:
        top_k_results: number of results to return when retrieving
        dir_path: List of web pages.

    Returns:
        A recipe retriever.
    """

    BATCH_SIZE_EMBEDDINGS = 5
    docs = load_docs_from_directory(dir_path=dir_path)
    doc_chunk = chunks(docs, BATCH_SIZE_EMBEDDINGS)
    for index, chunk in tqdm(enumerate(doc_chunk)):
        if index == 0:
            db = FAISS.from_documents(chunk, embeddings)
        else:
            db.add_documents(chunk)

    retriever = db.as_retriever(search_kwargs={"k": top_k_results})
    return retriever
