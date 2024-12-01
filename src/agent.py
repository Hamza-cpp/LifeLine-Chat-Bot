import pprint
from utils import create_retriever

recipe_retriever = create_retriever(top_k_results=2, dir_path="../data/recipes/*")
product_retriever = create_retriever(top_k_results=5, dir_path="../data/products/*")

recipe_docs = recipe_retriever.get_relevant_documents("Any lasagne recipes?")
product_docs = product_retriever.get_relevant_documents("Any Tomatoes?")
pprint.pprint([doc.metadata for doc in recipe_docs])
pprint.pprint([doc.metadata for doc in product_docs])
