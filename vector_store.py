import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import get_openai_api_key
from logger import setup_logger

logger = setup_logger()

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "research_knowledge_base"
DATA_FILE = "data/knowledge_base.txt"


def load_knowledge_base() -> str:
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"{DATA_FILE} not found. Please create it first.")

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


def get_vector_store() -> Chroma:
    embeddings = get_embeddings()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

    existing_count = vector_store._collection.count()

    if existing_count > 0:
        logger.info(f"Loaded existing Chroma collection with {existing_count} documents")
        return vector_store

    logger.info("Creating new Chroma vector store")

    text = load_knowledge_base()
    documents = create_documents(text)

    vector_store.add_documents(documents)

    logger.info(f"Added {len(documents)} documents to Chroma")

    return vector_store