import { useState } from 'react';
import IconSendMessage from 'src/assets/icons/IconSendMessage';
import IconUpload from 'src/assets/icons/IconUpload';
import RoundInput from 'src/common/RoundInput';

interface Props {
    input: any;
    handleInputChange: any;
    handleSubmit: any;
    isStreaming: boolean;
}

const ActionGroup = ({ input, handleInputChange, handleSubmit, isStreaming }: Props) => {
    const [isLiked, setIsLiked] = useState(false);

    const handleLike = () => {
        setIsLiked((prev) => !prev);
    };

    const handleChangeTone = (tone: string) => {
        console.log('tone', tone);
    };

    return (
        <div className="px-[40px]">
            <RoundInput
                value={input}
                onChange={handleInputChange}
                className="py-[10px] bg-[#FFFFFF] pl-8"
                placeholder="Hướng dẫn"
                type="text"
                onPressEnter={handleSubmit}
                addonAfter={
                    <div className='flex'>
                        <div className="mr-5">
                            <IconUpload />
                        </div>
                        <div onClick={handleSubmit} className="mr-[30px]">
                            <IconSendMessage />
                        </div>

                    </div>
                }
                disabled={isStreaming}
            />
        </div>
    );
};

export default ActionGroup;