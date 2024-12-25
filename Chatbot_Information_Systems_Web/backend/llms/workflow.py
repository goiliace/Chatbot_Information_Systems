
from typing import List
from typing_extensions import TypedDict
from langgraph.graph import START, END, StateGraph
from llms import rag

class GraphState(TypedDict):
    question: str
    generation: str
    documents: List[str]
    merge_documents: str
    history: List
    
async def retrieve(state:GraphState):
    question = state["question"]
    documents = await rag.compression_retriever.ainvoke(question)
    return {"documents": documents, "question": question}


async def grade_documents(state):
    question = state["question"]
    documents = state["documents"]
    # filtered_docs = await rag.retrieval_grader.abatch(
    #         [
    #             {
    #                 "question": question,
    #                 "document":
    #                     {
    #                         "id": doc.metadata["id"],
    #                         "text": doc.page_content,
    #                     }
    #             } for doc in documents
    #         ])
    # res_dict = {r.id: r.binary_score for  r in filtered_docs}
    # res = [
    #     doc for doc in documents
    #     if res_dict.get(doc.metadata["id"]) == "yes"
    # ]
    return {
        "documents": documents,
        "question": question,
    }
async def merge_doc(state:GraphState):
    documents = state["documents"]
    question = state["question"]
    contents = ""
    for doc in documents:
        contents += """\n\n
        ID: {id}
        CONTENT: 
        ```
        {text}
        ```\n
        """.format(id=doc.metadata["id"], text=doc.page_content)
        contents += "-"*20
    merge_documents =contents# await rag.merge_pipeline.ainvoke({"documents": documents})
    return {"documents": documents, "question": question, "merge_documents": merge_documents}


async def generate(state:GraphState):
    question = state["question"]
    history = state["history"]
    merge_documents = state["merge_documents"]
    generation = await rag.generator_pipeline.ainvoke({
        "history": history,
        "question": question,
        "context": merge_documents
    })
    return {
        "documents": state["documents"],
        "question": state["question"],
        "generation": generation.answer
    }
from langchain_core.runnables import chain
@chain
async def generate_chain(state:GraphState):
    history = state["history"]
    return rag.generator_pipeline.astream_events({
        "history": history,
        "question": state['question'],
        "context": state['merge_documents']
    }, version="v1")

    
from langgraph.graph import END, StateGraph, START

workflow_rag = StateGraph(GraphState)
workflow_rag.add_node('retrieve',retrieve)
workflow_rag.add_node('grade_documents' ,grade_documents)
workflow_rag.add_node('merge_doc',merge_doc)
# workflow_rag.add_node('generate',generate)
workflow_rag.add_edge(START, "retrieve")
workflow_rag.add_edge("retrieve", "grade_documents")
workflow_rag.add_edge("grade_documents", "merge_doc")
workflow_rag.add_edge("merge_doc", END)
app = workflow_rag.compile()

pipeline = app | generate_chain