import { create } from 'zustand';

import { type Conversation } from 'src/types/conversation';

interface ListAgentNavbarState {
    listAgentNavbar: Conversation[];
    setListAgentNavbar: (listAgentNavbar: Conversation[]) => void;
}

export const useListAgentNavbar = create<ListAgentNavbarState>((set) => ({
    listAgentNavbar: [],
    setListAgentNavbar: (listAgentNavbar) => set({ listAgentNavbar }),
}));
