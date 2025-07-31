import json
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

# Ask for API key
openai_api_key = input("🔐 Enter your OpenAI API Key: ").strip()

# Load scraped JSON
with open("scraped_data.json") as f:
    data = json.load(f)

# Convert each entry to a LangChain Document
docs = [
    Document(
        page_content=item["content"],
        metadata={"source": item["source"]}
    )
    for item in data
]

# Create embedding model
embedding_model = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Embed and store into ChromaDB
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma_store"
)

vectordb.persist()
print("✅ Successfully embedded scraped data and stored in ChromaDB.")
