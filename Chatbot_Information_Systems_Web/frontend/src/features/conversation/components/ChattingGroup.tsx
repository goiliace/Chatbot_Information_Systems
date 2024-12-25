import { useEffect, useRef } from 'react';
import AssistanceMessage from 'src/common/AssistanceMessage';
import UserMessage from 'src/common/UserMessage';
import { ReactTyped } from "react-typed";
import { type UseChatStreamChatMessage } from 'src/types/chat';

interface Props {
    listChat: UseChatStreamChatMessage[];
}

const ChattingGroup = ({ listChat }: Props) => {
    const chatContainerRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        // Cuộn đến cuối danh sách mỗi khi listChat thay đổi
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
        }
    }, [listChat]);

    return (
        <div className="h-4/5">
            <div className="flex flex-col gap-[30px] h-full overflow-scroll hide_scroll" ref={chatContainerRef}>

                {listChat.length > 0 ? listChat.map((item) => {
                    switch (item.role) {
                        case "human":
                            return <UserMessage key={item.id} content={item} />;
                        case "ai":
                            return <AssistanceMessage captureRef={chatContainerRef} key={item.id} content={item} />;
                        default:
                            return null;
                    }
                }) :
                    <div className="w-full h-full flex items-center justify-center">
                        <div className="text-center">
                            <ReactTyped className="text-4xl font-semibold text-[#00529C]" strings={["Bạn cần giúp giúp gì về hệ thống quản lý thông tin?"]} typeSpeed={40}
                                backSpeed={50} />
                        </div>
                    </div>
                }
            </div>
        </div>
    );
};

export default ChattingGroup;