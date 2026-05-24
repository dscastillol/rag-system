from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_postgres import PGVector
from langchain_ollama import OllamaLLM


CONNECTION = (
    "postgresql+psycopg://postgres:postgres@localhost:5432/ragdb"
)


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = PGVector(
    embeddings=embeddings,
    connection=CONNECTION,
    collection_name="documents"
)

llm = OllamaLLM(
    model="llama3.2"
)


query = input("Ask a question: ")

results = vector_store.similarity_search(
    query,
    k=3
)

context = "\n\n".join(
    [doc.page_content for doc in results]
)

prompt = f"""
You are a helpful assistant.

Use ONLY the provided context.

If the answer is not present in the context, say:

"I could not find the answer in the retrieved documents."

Context:
{context}

Question:
{query}

Answer:
"""


response = llm.invoke(prompt)

print("\nAnswer:\n")
print(response)