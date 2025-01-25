from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import Chroma
from langchain.schema.document import Document
from langchain_ollama import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama

def load_and_split_docs():
    loader = PyPDFLoader("assets/Machine Learning.pdf")
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(pages)
    print(f"Split {len(pages)} documents into {len(chunks)} chunks")
    embeddings = FastEmbedEmbeddings()
    Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="./sql_chroma_db")

def rag_chain():
    model = ChatOllama(model="llama3")
    prompt = PromptTemplate.from_template(
        """
        <s> [Instructions] You are a friendly assistant. Answer the user's question based only on the follwing context.
        If you don't know the answer, just say that you don't know, don't try to make up an answer. [/Instructions]
        </s>
        [Instructions] Question: {input}
        context: {context}
        Answer: [/Instructions]
        """
    )
    embeddings = FastEmbedEmbeddings()
    vectorstore = Chroma(persist_directory="./sql_chroma_db", embedding_function=embeddings)
    retriever = vectorstore.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "score_threshold": 0.5,
            "k": 3,
        }
    )

    document_chain = create_stuff_documents_chain(model, prompt)
    chain = create_retrieval_chain(retriever, document_chain)

    return chain

def ask():
    chain = rag_chain()
    result = chain.invoke({"input": "What's the trade-off between bias and variance?"})
    print("Answer:", result.get("answer", "No answer provided"))
    if "context" in result:
        for doc in result["context"]:
            print("Source:", doc.metadata["source"])

# Ensure you call load_and_split_docs before ask
load_and_split_docs()
ask()
