# from langchain_huggingface import HuggingFaceEmbeddings
# import pprint

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
# emb = embeddings.embed_query("Hello, world!")
# pprint.pprint(emb)

# import os
# import getpass
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# if "GROQ_API_KEY" not in os.environ:
#     os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

# llm = ChatGroq(
#     model="llama3-8b-8192",
#     temperature=0,
#     max_tokens=158,
#     timeout=None,
#     max_retries=2,
# )


# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# ai_msg = llm.invoke(messages)
# print(ai_msg)
# print("#######################################################")
# print(ai_msg.content)



# from langchain_community.document_loaders.text import TextLoader
# products_docs = TextLoader("./data/products/angus_beef_lean_mince.txt").load()
# print(products_docs[0].page_content)


from src.document_loaders import load_docs_from_directory,chunks
from tqdm import tqdm
from src.llm_embedding import embeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)

docs_list = load_docs_from_directory("data/products/*")
chunks_list = text_splitter.split_documents(docs_list)
# chunks_list = chunks(docs_list,3)
vector_store = FAISS.from_documents(documents=chunks_list,embedding=embeddings)

retriever = vector_store.as_retriever(k=4)

docs = retriever.invoke("What is the best way to cook angus beef mince?")

print(docs)
print(docs[0].page_content) 

# for index , chunk in tqdm(enumerate(chunks_list)):
#     tqdm.write(f"Index: {index}, Chunk: {chunk}")
#     for i  in range (len(chunk)):
#         tqdm.write(chunk[i].page_content)
#     print("########################################")
# print("FINAL")
