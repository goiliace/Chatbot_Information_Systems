import { z } from 'zod';

const UserSchema = z.object({
    id: z.string(),
    email: z.string().email(),
    name: z.string(),
    role: z.enum(['admin', 'employee', 'user']),
    status: z.enum(['active', 'inactive', 'deleted']),
    photoURL: z.string().url(),
    createdAt: z.string().datetime(),
});

export type User = z.infer<typeof UserSchema>;
