from typing import Literal, Optional

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict, List
from pydantic import BaseModel, Field
from llms.llm import llm_openai as llm

class State(TypedDict):
    question: str
    history: List
class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "gpt"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore.",
    )
    rewrite_query: Optional[str| None] = Field(
        None,
        description="If the question is related to vectorstore but the question content does not have enough context, combine it with previous chat history to rephrase the user's question",
    )

structured_llm_router = llm.with_structured_output(RouteQuery)

# Prompt
system = """You are a Vietnamese expert in routing user queries to vectorstore or gpt.
The question may be misspelled, please correct the spelling first
Vectorstore contains documents related to information systems (IS) and management information systems (MIS) documents
Use vectorstore to ask about systems and information systems topics. Otherwise, go to gpt.
If the question is related to vectorstore but the question content does not have enough context, combine it with previous chat history to rephrase the user's question. Otherwise, rewrite the question to None"""
route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder("history"),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router

async def gen_route_and_rewrite(state: State):
    question = state["question"]
    history = state["history"]
    source = await question_router.ainvoke({"question": question, "history": history})
    if source.datasource == "vectorstore" and source.rewrite_query is not None:
        question = source.rewrite_query 

    return {
        "question": question,
        "router": source.datasource,
    }

title_system = """Bạn là một chuyên gia trong việc tóm tắt các cuộc trò chuyện của người dùng với AI thành title của conversation. Cung cấp 1 conversation và bạn sẽ tóm tắt nó thành title."""
class TitleResponse(BaseModel):
    title: str = Field(..., description="The title of the conversation")
title_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        MessagesPlaceholder("history"),
    ]
)
title_llm_router = llm.with_structured_output(TitleResponse)


title_pipe = title_prompt | title_llm_router
async def gen_title(state: State):
    history = state["history"]
    title = await title_pipe.ainvoke({"history": history})
    return {
        "title": title.title,
    }