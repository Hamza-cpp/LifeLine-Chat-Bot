import glob
from collections.abc import Iterator

from langchain_core.documents import Document
from langchain_community.document_loaders.text import TextLoader


def load_docs_from_directory(directory_path: str) -> list[Document]:
    """Loads documents from a directory.

    Args:
        directory_path: The path to the directory containing the documents.

    Returns:
        A list of the documents in the directory.
    """

    documents = []
    for file_path in glob.glob(directory_path):
        document_loader = TextLoader(file_path)
        documents.extend(document_loader.load())
    return documents


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
