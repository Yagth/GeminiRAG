from langchain_text_splitters import RecursiveCharacterTextSplitter
from llm.model import qa_chain
from flask import Flask, request, jsonify
from llm.model import qa_chain, vector_database
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from llm.model import embeddings


app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def qa():
    question = request.json["question"]
    result = qa_chain({"query": question})  # Convert the list to a tuple
    return jsonify(
        {
            "result": result["result"],
            "source_documents": [
                str(doc.page_content) for doc in result["source_documents"]
            ],
        }
    )


@app.route("/upload", methods=["POST"])
def upload():

    vector_database.delete_collection()

    file = request.files["document"]
    file_path = "./doc/" + file.filename
    file.save(file_path)
    pdf_loader = PyPDFLoader(file_path)
    pages = pdf_loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    context = "\n\n".join(str(p.page_content) for p in pages)
    texts = text_splitter.split_text(context)

    vector_index = Chroma.from_texts(texts, embeddings).as_retriever(
        search_kwargs={"k": 5}
    )

    qa_chain.retriever = vector_index

    return jsonify({"message": "Document uploaded successfully."})


if __name__ == "__main__":
    app.run()
