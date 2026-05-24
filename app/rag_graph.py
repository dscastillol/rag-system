from typing import TypedDict

from langgraph.graph import StateGraph, END

from vector_store import get_vector_store
from llm import get_llm


# Inicializar componentes
vector_store = get_vector_store()
llm = get_llm()


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
You are a helpful assistant.

Use ONLY the provided context.

If the answer is not present in the context say:

"I could not find the answer in the retrieved documents"

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
# BUILD GRAPH
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
# RUN APP
# -----------------------

if __name__ == "__main__":

    while True:

        question = input(
            "\nAsk a question ('exit' to quit): "
        )

        if question.lower() == "exit":
            break

        result = app.invoke(
            {
                "question": question
            }
        )

        print("\nAnswer:\n")
        print(result["answer"])