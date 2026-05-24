from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_postgres import PGVector


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


query = input("Ask a question: ")

results = vector_store.similarity_search(
    query,
    k=3
)

print("\nRetrieved Context:\n")

for i, doc in enumerate(results, start=1):

    print(f"Chunk {i}:")
    print(doc.page_content[:500])
    print("\n" + "-"*50 + "\n")