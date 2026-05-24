from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_postgres import PGVector
from langchain_core.documents import Document


CONNECTION = (
    "postgresql+psycopg://postgres:postgres@localhost:5432/ragdb"
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = PGVector(
    embeddings=embeddings,
    connection=CONNECTION,
    collection_name="test_collection"
)

docs = [
    Document(
        page_content="Machine learning is a subset of artificial intelligence."
    ),
    Document(
        page_content="Deep learning uses neural networks with many layers."
    ),
    Document(
        page_content="Python is a programming language."
    )
]

vector_store.add_documents(docs)

query = "What is machine learning?"

results = vector_store.similarity_search(
    query,
    k=2
)

print("\nQuery:")
print(query)

print("\nResults:")

for doc in results:
    print("-")
    print(doc.page_content)