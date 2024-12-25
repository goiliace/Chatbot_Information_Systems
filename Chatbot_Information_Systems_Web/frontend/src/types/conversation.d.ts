import { z } from "zod";

// Define a UUID regex pattern or use a custom UUID validator
const uuidSchema = z.string().uuid();

const ConversationSchema = z.object({
    id: uuidSchema,
    name: z.string().nonempty(),
    is_active: z.boolean().default(true),
    create_at: z.date().or(z.string().datetime()),
    create_by: uuidSchema.optional()
});

export type Conversation = z.infer<typeof ConversationSchema>;
