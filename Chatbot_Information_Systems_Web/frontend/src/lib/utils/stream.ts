import { UseChatStreamOptions, UseChatStreamInputMethod } from 'src/types/chat';

const DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
};

const mergeInputInOptions = (input: string, options: UseChatStreamOptions, method: UseChatStreamInputMethod) => {
    options.query = options.query ?? {};
    console.log(input);
    return options;
};

export async function* getStream(
    conversation_id: string,
    input: string,
    options: UseChatStreamOptions,
    method: UseChatStreamInputMethod
): AsyncIterableIterator<string> {
    options = mergeInputInOptions(input, options, method);

    const params = '?' + new URLSearchParams(options.query).toString();
    console.log({
        ...DEFAULT_HEADERS,
        ...options.headers,
    });

    const response = await fetch(options.url + params, {
        method: options.method,
        headers: {
            ...DEFAULT_HEADERS,
            ...options.headers,
        },
        body: JSON.stringify({
            question: input,
            conversation_id: conversation_id,
            ...options.body,
        }),
    });

    if (!response.ok) throw new Error(response.statusText);
    if (!response.body) {
        throw new Error('No body');
    }
    // Lấy đối tượng reader từ response body
    const reader = response.body.getReader();

    let buffer = '';
    while (true) {
        const { done, value } = await reader.read();

        if (done) {
            break;
        }

        if (!value) {
            continue;
        }
        buffer = new TextDecoder().decode(value);
        yield buffer;
    }
}
