import IconUpload from 'src/assets/icons/IconUpload';
import RoundInput from '../RoundInput';
import IconSendMessage from 'src/assets/icons/IconSendMessage';

interface Props {
    value: string;
    isStreaming: boolean;
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
    onSendMessage: () => void;
}

const InputChat = ({ value, isStreaming, onChange, onSendMessage }: Props) => {
    return (
        <RoundInput
            value={value}
            onChange={onChange}
            className="py-[10px]"
            placeholder="Hướng dẫn"
            onPressEnter={onSendMessage}
            addonBefore={
                <div className="ml-[30px]">
                    <IconUpload />
                </div>
            }
            disabled={isStreaming}
            addonAfter={
                <div onClick={onSendMessage} className="mr-[30px]">
                    <IconSendMessage />
                </div>
            }
        />
    );
};

export default InputChat;
