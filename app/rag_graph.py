from typing import TypedDict

from langgraph.graph import StateGraph, END

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


# -----------------------
# STATE
# -----------------------

class RAGState(TypedDict):

    question: str
    context: str
    answer: str


# -----------------------
# NODES
# -----------------------

def retrieve(state: RAGState):

    results = vector_store.similarity_search(
        state["question"],
        k=3
    )

    context = "\n\n".join(
        doc.page_content
        for doc in results
    )

    return {
        "context": context
    }


def generate(state: RAGState):

    prompt = f"""
    Use ONLY the provided context.

    If the answer is not present say:
    "I could not find the answer in the documents"

    Context:
    {state["context"]}

    Question:
    {state["question"]}

    Answer:
    """

    answer = llm.invoke(prompt)

    return {
        "answer": answer
    }


# -----------------------
# GRAPH
# -----------------------

graph = StateGraph(RAGState)

graph.add_node(
    "retrieve",
    retrieve
)

graph.add_node(
    "generate",
    generate
)

graph.set_entry_point(
    "retrieve"
)

graph.add_edge(
    "retrieve",
    "generate"
)

graph.add_edge(
    "generate",
    END
)

app = graph.compile()


# -----------------------
# RUN
# -----------------------

if __name__ == "__main__":

    question = input(
        "Ask a question: "
    )

    result = app.invoke(
        {
            "question": question
        }
    )

    print("\nAnswer:\n")
    print(result["answer"])