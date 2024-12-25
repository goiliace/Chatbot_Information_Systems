// import { HEAD_HEIGHT } from 'src/constants';
import { useSearchParams, useNavigate, useParams, Navigate } from "react-router-dom";
import { useState, useEffect } from 'react';
import ActionGroup from './components/ActionGroup';
import ChattingGroup from './components/ChattingGroup';
import { LIST_CHAT } from './constants';
import { IChat } from './type';
import { useChatStream } from 'src/lib/hooks/useChat';
import { UseChatStreamChatMessage, UseChatStreamInput } from 'src/types/chat';
import { GetMessages } from 'src/lib/api/chat';
import { useAuth } from 'src/lib/hooks/useAuthContext';
import { CreateConversation } from 'src/lib/api/conversation';
import { GetConversations } from 'src/lib/api/conversation';
import { Conversation } from 'src/types/conversation';
import { Link } from 'react-router-dom';
import { useListAgentNavbar } from 'src/lib/hooks/useNavbar'
const Chatting = () => {
    const { id } = useParams();
    const { user, token } = useAuth();

    const [searchParams, setSearchParams] = useSearchParams();
    const navigate = useNavigate();
    const { listAgentNavbar, setListAgentNavbar } = useListAgentNavbar();

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await GetConversations();
                if (Array.isArray(response)) {
                    setListAgentNavbar(response as Conversation[]);
                } else {
                    console.error("Unexpected response format:", response);
                }
            } catch (error) {
                console.error("Failed to fetch conversations:", error);
            }
        }
        if (!id || !listAgentNavbar.find((item) => item.id == id)) {
            navigate("/")
        }
        fetchData();
    }, [user, id]);
    const { messages, input, isStreaming, setMessages, handleInputChange, handleSubmit } = useChatStream({
        options: {
            url: process.env.REACT_APP_API_IP + '/conversation/chat',
            method: 'POST',
            headers: {
                Authorization: `Bearer ${token}`,
            },
            // body: {
            //     conversation_id: id || "",
            // },
        },
        method: {
            type: 'body',
            key: 'question',
        },
        handlers: {
            onMessageAdded: (message) => { },
        },
    },
    );

    useEffect(() => {
        async function getMessages(id: string) {
            try {
                const response = (await GetMessages(id)) as UseChatStreamChatMessage[];
                if (response) {

                    setMessages(response);
                }
            }
            catch (error) {
                navigate('/')
            }
        }

        if (id) getMessages(id);
        else setMessages([]);
    }, [id, user]);

    const handleUserSubmit = async () => {
        if (!id) {
            const conversation_id = await CreateConversation();
            await handleSubmit(conversation_id);
            navigate(`/c/${conversation_id}`);
        }
        else
            await handleSubmit(id);

    }
    return user && (
        <div style={{ height: `calc(100vh - 24px` }} className="w-full flex flex-col justify-between px-[100px] py-[30px]">
            <ChattingGroup listChat={messages} />
            {/* <ActionGroup listChat={listChat} setListChat={setListChat} />
             */}
            <ActionGroup
                input={input}
                isStreaming={isStreaming}
                handleSubmit={handleUserSubmit}
                handleInputChange={handleInputChange}
            />
        </div>
    );
};

export default Chatting;