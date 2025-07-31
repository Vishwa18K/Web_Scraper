import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, RetrievalQA
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain_core.documents import Document

# Prompt for API key at runtime
openai_api_key = input("Enter your OpenAI API Key: ").strip()

# Load Chroma vector store
vectordb = Chroma(
    persist_directory="chroma_store",
    embedding_function=OpenAIEmbeddings(openai_api_key=openai_api_key)
)

# Setup LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0.3, openai_api_key=openai_api_key)

# Create truncation helper
def truncate_docs(docs, max_chars=1000):
    return [
        Document(page_content=doc.page_content[:max_chars], metadata=doc.metadata)
        for doc in docs
    ]

# Custom prompt and chain setup
prompt_template = """Answer the question using only the following documents:\n\n{context}\n\nQuestion: {question}\nAnswer:"""
prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)

llm_chain = LLMChain(llm=llm, prompt=prompt)
stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="context")

qa_chain = RetrievalQA(retriever=vectordb.as_retriever(), combine_documents_chain=stuff_chain)

# Run QA loop
while True:
    question = input("\nAsk a music-related question (or type 'exit' to quit):\n")
    if question.lower() == "exit":
        break
    docs = vectordb.as_retriever().get_relevant_documents(question)
    short_docs = truncate_docs(docs, max_chars=1000)
    result = qa_chain.combine_documents_chain.run(input_documents=short_docs, question=question)
    print("\nAnswer:\n", result)
