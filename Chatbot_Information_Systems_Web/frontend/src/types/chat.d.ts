import { UploadFile } from 'antd';
import { ChatRole, ContentType } from 'src/constants';
import { useChatStream } from 'src/lib/hooks/agent/useChat';

type HttpMethod = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';

export type UseChatStreamRole = 'ai' | 'human' | 'system';

export type UseChatStreamChatMessage = {
    role: ChatRole;
    content?: string;
    id: string;
};

export type UseChatStreamOptions = {
    url: string;
    method: HttpMethod;
    query?: Record<string, string>;
    headers: HeadersInit;
    body?: Record<string, string>;
};

export type UseChatStreamEventHandlers = {
    onMessageAdded: (message: UseChatStreamChatMessage) => unknown | Promise<unknown>;
};

export type UseChatStreamInputMethod = {
    type: 'body' | 'query';
    key: string;
};

export type UseChatStreamInput = {
    options: UseChatStreamOptions;
    method: UseChatStreamInputMethod;
    handlers: UseChatStreamEventHandlers;
};

export type UseChatStreamResult = ReturnType<typeof useChatStream>;
