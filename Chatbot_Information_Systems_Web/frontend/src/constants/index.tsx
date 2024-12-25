export const HEAD_HEIGHT = 64;

// More than 8 characters
// Include as least 1 uppercase
// Include as least 1 lowercase
// Include as least 1 special character
// Include as least 1 number
// No space
export const REGEX_PASSWORD =
    /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?`~])[A-Za-z\d!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?`~]{8,}$/;

export enum ContentType {
    TEXT = 'agent_text',
    IMAGE = 'agent_image',
    DOCUMENT = 'agent_document',
}

export enum ChatRole {
    ASSISTANCE = 'ai',
    USER = 'human',
}
export enum ImageQuality {
    STANDARD = 'standard',
    HD = 'hd',
}

export enum AgentHomepage {
    TEXT = 'agent_text',
    IMAGE = 'agent_image',
    DOCUMENT = 'agent_document',
}