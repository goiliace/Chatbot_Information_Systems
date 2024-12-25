import { ChangeEvent, FormEvent, useEffect, useState } from 'react';
import { getStream } from 'src/lib/utils/stream';
import { UseChatStreamChatMessage, UseChatStreamInput } from 'src/types/chat';
import { ChatRole, ContentType } from 'src/constants';
import { stringify } from 'querystring';
const BOT_ERROR_MESSAGE = 'Something went wrong fetching AI response.';

export const useChatStream = (
    input: UseChatStreamInput,
) => {
    const [messages, setMessages] = useState<UseChatStreamChatMessage[]>([]);
    const [formInput, setFormInput] = useState('');
    const [isStreaming, setIsStreaming] = useState(false);
    // const [conversationId, setConversationId] = useState<string>(input.options.body?.conversation_id || "");
    useEffect(() => {
        setMessages([]);
        setFormInput('');
        setIsStreaming(false);
        // setConversationId("");
    }, [input.options.body?.conversation_id]);

    const handleInputChange = (e: ChangeEvent<HTMLInputElement> | ChangeEvent<HTMLTextAreaElement>) => {
        setFormInput(e.target.value);
    };

    const handleSubmit = async (id: string) => {
        await resetInputAndGetResponse(id);
    };

    const addMessage = (message: Omit<UseChatStreamChatMessage, 'id'>) => {
        const messageWithId = { ...message, id: crypto.randomUUID() as string };
        setMessages((messages) => [...messages, messageWithId]);

        return messageWithId;
    };

    const appendMessageToChat = (message: string) => {
        setMessages((messages) => {
            const latestMessage = messages[messages.length - 1];

            return [...messages.slice(0, -1), { ...latestMessage, content: latestMessage.content + message }];
        });
    };

    const fetchAndUpdateAIResponse = async (conversationId: string, message: string) => {
        const stream = await getStream(conversationId, message, input.options, input.method);
        const initialMessage = addMessage({ content: '', role: ChatRole.ASSISTANCE });
        let response = '';

        for await (const chunk of stream) {
            appendMessageToChat(chunk);
            console.log(chunk);

            response = chunk;
        }
        return { ...initialMessage, content: response };
    };

    const submitMessage = async (message: string) => resetInputAndGetResponse(message);

    const resetInputAndGetResponse = async (id: string, message?: string) => {
        setIsStreaming(true);

        const addedMessage = addMessage({ content: message ?? formInput, role: ChatRole.USER });
        // await input.handlers.onMessageAdded?.(addedMessage);
        setFormInput('');

        try {
            const addedMessage = await fetchAndUpdateAIResponse(id, message ?? formInput);
            // await input.handlers.onMessageAdded?.(addedMessage);
        } catch (error) {
            console.log(error);

            const addedMessage = appendMessageToChat(BOT_ERROR_MESSAGE);
            // await input.handlers.onMessageAdded?.(addedMessage);
        } finally {
            setIsStreaming(false);
        }
    };

    return {
        messages,
        setMessages,
        input: formInput,
        setInput: setFormInput,
        handleInputChange,
        handleSubmit,
        submitMessage,
        isStreaming,
    };
};
