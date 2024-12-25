from collections.abc import  Sequence

from langchain_core.messages.ai import AIMessage
from langchain_core.messages.base import BaseMessage
from langchain_core.messages.human import HumanMessage
from langchain_core.messages.system import SystemMessage


def _message_from_dict(message: dict) -> BaseMessage:
    _type = message["role"]
    if _type == "human":
        return HumanMessage(content=message["content"], type=message["role"], id=message["id"])
    elif _type == "ai":
        return AIMessage(content=message["content"], type=message["role"], id=message["id"])
    elif _type == "system":
        return SystemMessage(content=message["content"], type=message["role"], id=message["id"])
    
def messages_from_dict(messages: Sequence[dict]) -> list[BaseMessage]:
    return [_message_from_dict(m) for m in messages]

