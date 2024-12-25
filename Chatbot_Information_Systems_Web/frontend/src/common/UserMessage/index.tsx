import { type UseChatStreamChatMessage } from 'src/types/chat';
const UserMessage = ({ content }: { content: UseChatStreamChatMessage }) => {

    return (
        <div className="w-full flex justify-end">
            <div className="w-fit max-w-[80%]">
                <p className="text-md text-[#13529C]  px-[30px] py-[20px] rounded-[30px] bg-[#FFFFFF] font-medium">{content.content}</p>
            </div>
        </div>
    )
};

export default UserMessage;
