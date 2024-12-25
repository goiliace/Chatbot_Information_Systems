
import { z } from 'zod';

const BaseAgentSchema = z.object({
    id: z.string(),
    name: z.string(),
    description: z.string(),
    avatar_url: z.string().url(),
    premium: z.boolean(),
    is_favorite: z.boolean(),
    group_ids: z.array(z.string()),
});
const optionsSchema = z.record(z.string(), z.string());

const fieldSchema = z.object({
    name: z.string(),
    type: z.enum(['Text', 'Select', 'Textarea']),
    options: z.optional(optionsSchema),
});
const inputInfoSchema = z.record(z.string(), fieldSchema);
const AgentSchema = BaseAgentSchema.extend({
    standout: z.string().optional(), // đảm bảo trường standout là tùy chọn
    input_infomation: inputInfoSchema,
});

const AgentCategorySchema = z.object({
    id: z.string(),
    name: z.string(),
    description: z.string(),

})
export type BaseAgent = z.infer<typeof BaseAgentSchema>;
export type Agent = z.infer<typeof AgentSchema>;
export type InputInfo = z.infer<typeof inputInfoSchema>;
export type AgentCategory = z.infer<typeof AgentCategorySchema>;
