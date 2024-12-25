
from __future__ import annotations

import json
import logging
import re
import uuid
from typing import List, Optional, Sequence

import psycopg
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict
from psycopg import sql

logger = logging.getLogger(__name__)




def _get_messages_query(table_name: str) -> sql.Composed:
    """Make a SQL query to get messages for a given session."""
    return sql.SQL(
        "SELECT  id, role, content, create_at "
        "FROM {table_name} "
        "WHERE conversation_id = %(session_id)s "
        "ORDER BY create_at;"
    ).format(table_name=sql.Identifier(table_name))


def _delete_by_session_id_query(table_name: str) -> sql.Composed:
    """Make a SQL query to delete messages for a given session."""
    return sql.SQL(
        "DELETE FROM {table_name} WHERE session_id = %(session_id)s;"
    ).format(table_name=sql.Identifier(table_name))


def _delete_message_query(table_name: str) -> sql.Composed:
    """Make a SQL query to delete a message."""
    return sql.SQL(
        "DELETE FROM {table_name} WHERE id = %(message_id)s;"
    ).format(table_name=sql.Identifier(table_name))

def _insert_message_query(table_name: str, return_id: bool = False) -> sql.Composed:
    """Make a SQL query to insert a message."""
    query =  "INSERT INTO {table_name} (conversation_id, role, content) VALUES (%s, %s, %s) " 
    if return_id:
        query += "RETURNING id;"
        
    return sql.SQL(
       query
    ).format(table_name=sql.Identifier(table_name))
    
def _update_message_query(table_name: str, return_id: bool = False) -> sql.Composed:
    """Make a SQL query to update a message."""
    query =  "UPDATE {table_name} SET content = %s WHERE id = %s " 
    if return_id:
        query += "RETURNING id;"
        
    return sql.SQL(
       query
    ).format(table_name=sql.Identifier(table_name))


class PostgresChatMessageHistory(BaseChatMessageHistory):
    def __init__(
        self,
        session_id: str,
        table_name: str = "message",
        /,
        *,
        sync_connection: Optional[psycopg.Connection] = None,
        async_connection: Optional[psycopg.AsyncConnection] = None,
    ) -> None:
        
        if not sync_connection and not async_connection:
            raise ValueError("Must provide sync_connection or async_connection")

        self._connection = sync_connection
        self._aconnection = async_connection

        # Validate that session id is a UUID
        try:
            uuid.UUID(session_id)
        except ValueError:
            raise ValueError(
                f"Invalid session id. Session id must be a valid UUID. Got {session_id}"
            )
        self._session_id = session_id
        if not re.match(r"^\w+$", table_name):
            raise ValueError(
                "Invalid table name. Table name must contain only alphanumeric "
                "characters and underscores."
            )
        self._table_name = table_name



    async def aadd_messages(self, messages: Sequence[BaseMessage]) -> None:
        """Add messages to the chat message history."""
        if self._aconnection is None:
            raise ValueError(
                "Please initialize the PostgresChatMessageHistory "
                "with an async connection or use the sync add_messages method instead."
            )
        values = []
        for message in messages:
            message = message_to_dict(message)
            
            values.append(
                (
                    self._session_id, message['type'], message['data']['content']
                )
            )
        print(values)
        query = _insert_message_query(self._table_name)
        async with self._aconnection.cursor() as cursor:
            await cursor.executemany(query, values)
        await self._aconnection.commit()
    async def aadd_message(self, message: BaseMessage) -> None:
        if self._aconnection is None:
            raise ValueError(
                "Please initialize the PostgresChatMessageHistory "
                "with an async connection or use the sync add_messages method instead."
            )

        message = message_to_dict(message)
        query = _insert_message_query(self._table_name, True)
        async with self._aconnection.cursor() as cursor:
            await cursor.execute(query, (self._session_id, message['type'], message['data']['content']))
            message_id = await cursor.fetchone()
        await self._aconnection.commit()
        return message_id[0]
    
    async def aupdate_message(self, message_id: int, content: str) -> None:
        if self._aconnection is None:
            raise ValueError(
                "Please initialize the PostgresChatMessageHistory "
                "with an async connection or use the sync add_messages method instead."
            )
        query = _update_message_query(self._table_name)
        async with self._aconnection.cursor() as cursor:
            await cursor.execute(query, (content, message_id))
        await self._aconnection.commit()
    async def adelete_message(self, message_id: int) -> None:
        if self._aconnection is None:
            raise ValueError(
                "Please initialize the PostgresChatMessageHistory "
                "with an async connection or use the sync add_messages method instead."
            )
        query = _delete_message_query(self._table_name)
        async with self._aconnection.cursor() as cursor:
            await cursor.execute(query, {"message_id": message_id})
        await self._aconnection.commit()
    

    async def aget_messages(self) -> List[BaseMessage]:
        """Retrieve messages from the chat message history."""
        if self._aconnection is None:
            raise ValueError(
                "Please initialize the PostgresChatMessageHistory "
                "with an async connection or use the sync get_messages method instead."
            )

        query = _get_messages_query(self._table_name)
        async with self._aconnection.cursor() as cursor:
            await cursor.execute(query, {"session_id": self._session_id})
            # items = [record for record in await cursor.fetchall()]
            messages = [
                {
                    "id": record[0],
                    "role": record[1],
                    "content": record[2],
                    "conversation_id": self._session_id
                } for record in await cursor.fetchall()
            ]
        # messages = messages_from_dict(items)
        return messages

    

    def clear(self) -> None:
        """Clear the chat message history for the GIVEN session."""
        if self._connection is None:
            raise ValueError(
                "Please initialize the PostgresChatMessageHistory "
                "with a sync connection or use the async clear method instead."
            )

        query = _delete_by_session_id_query(self._table_name)
        with self._connection.cursor() as cursor:
            cursor.execute(query, {"session_id": self._session_id})
        self._connection.commit()

    async def aclear(self) -> None:
        """Clear the chat message history for the GIVEN session."""
        if self._aconnection is None:
            raise ValueError(
                "Please initialize the PostgresChatMessageHistory "
                "with an async connection or use the sync clear method instead."
            )

        query = _delete_by_session_id_query(self._table_name)
        async with self._aconnection.cursor() as cursor:
            await cursor.execute(query, {"session_id": self._session_id})
        await self._aconnection.commit()
