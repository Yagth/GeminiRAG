import urllib
import warnings
from pathlib import Path as p
from pprint import pprint

import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# from llm import FILE_PATH, GOOGLE_API_KEY

warnings.filterwarnings("ignore")


import os

GOOGLE_API_KEY = "AIzaSyBKc-zB8RCnO0DdhE_QZ0Ii-3QsbqR1gyA"
FILE_PATH = "./doc/Retrieval-Augmented Generation for.pdf"

model = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2,
    convert_system_message_to_human=True,
)

pdf_loader = PyPDFLoader(FILE_PATH)
pages = pdf_loader.load_and_split()
# print(pages[3].page_content)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
context = "\n\n".join(str(p.page_content) for p in pages)
texts = text_splitter.split_text(context)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", google_api_key=GOOGLE_API_KEY
)

vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k": 5})

template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
{context}
Question: {question}
Helpful Answer:"""
PROMPT = PromptTemplate.from_template(template)  # Run chain
qa_chain = RetrievalQA.from_chain_type(
    model,
    retriever=vector_index,
    return_source_documents=True,
    chain_type_kwargs={
        "verbose": False,
        "prompt": PROMPT,
        "memory": ConversationBufferMemory(memory_key="history", input_key="question"),
    },
)
