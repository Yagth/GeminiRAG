from llm.model import qa_chain


question = "Describe What a RAG is in detail?"
result = qa_chain({"query": question})
result["result"]

print(result["result"])
# print(result["source_documents"])
