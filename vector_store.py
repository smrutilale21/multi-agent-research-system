import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import get_openai_api_key

FAISS_DIR = "faiss_index"
DATA_FILE = "data/knowledge_base.txt"


def load_knowledge_base() -> str:
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"{DATA_FILE} not found. Please create the file first.")

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return file.read()


def create_documents(text: str) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80
    )

    chunks = splitter.split_text(text)
    documents = []
    for index, chunk in enumerate(chunks):
        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "source": DATA_FILE,
                    "chunk_id": index
                }
            )
        )

    return documents


def get_embeddings() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=get_openai_api_key()
    )


def get_vector_store() -> FAISS:
    embeddings = get_embeddings()

    if os.path.exists(FAISS_DIR):
        return FAISS.load_local(
            folder_path=FAISS_DIR,
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )

    text = load_knowledge_base()
    documents = create_documents(text)

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    vector_store.save_local(FAISS_DIR)

    return vector_store