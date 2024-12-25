import { z } from 'zod';
import UseChatStreamChatMessage from './chat';
const questionItemSchema = z.object({
    id: z.string(),
    user: UseChatStreamChatMessage,
    assistant: UseChatStreamChatMessage,
    date: z.string(),
    time: z.string(),
    assistance_name: z.string(),
    assistance_avatar: z.string(),
    assistance_description: z.string(),
})
const HistoryItemSchema = z.object({
    id: z.string(),
    date: z.string(),
    listQuestions: z.array(questionItemSchema),
});

export type IHistoryItem = z.infer<typeof HistoryItemSchema>
export type IQuestionItem = z.infer<typeof questionItemSchema>