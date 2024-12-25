import { message } from 'antd';
import html2canvas from 'html2canvas';
import { useState } from 'react';
import IconCopy from 'src/assets/icons/IconCopy';
import IconDislike from 'src/assets/icons/IconDislike';
import IconDislikeFilled from 'src/assets/icons/IconDislikeFilled';
import IconDownload from 'src/assets/icons/IconDownload';
import IconLike from 'src/assets/icons/IconLike';
import IconLikeFilled from 'src/assets/icons/IconLikeFilled';
import IconReport from 'src/assets/icons/IconReport';
import IconShare from 'src/assets/icons/IconShare';
import { ContentType } from 'src/constants';
import { UseChatStreamChatMessage } from 'src/types/chat';

interface Props {
    content: UseChatStreamChatMessage;
    captureRef?: React.MutableRefObject<HTMLDivElement | null>;
    onOpenModalReport: () => void;
}

const InteractButtons = ({ content, captureRef, onOpenModalReport }: Props) => {
    const [isLiked, setIsLiked] = useState(false);
    const [isDisliked, setIsDisliked] = useState(false);

    const handleLike = () => {
        setIsLiked((prev) => !prev);
    };

    const handleDisliked = () => {
        setIsDisliked((prev) => !prev);
    };

    const handleCopy = async ({ content = '' }: UseChatStreamChatMessage) => {
        if (navigator.clipboard && window.isSecureContext) {
            return navigator.clipboard.writeText(content).then(
                () => {
                    message.success('Text copied to clipboard');
                },
                (err) => {
                    message.error('Could not copy text: ', err);
                }
            );
        } else {
            const textArea = document.createElement('textarea');
            textArea.value = content;
            textArea.style.position = 'fixed'; // Tránh việc cuộn trang
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            try {
                document.execCommand('copy');
                message.success('Text copied to clipboard');
            } catch (err) {
                message.error('Could not copy text');
            }
            document.body.removeChild(textArea);
        }
    };

    const handleDownload = () => {
        if (captureRef?.current) {
            let canvasPromise = html2canvas(captureRef.current, {
                useCORS: true,
            });
            canvasPromise.then((canvas) => {
                var dataURL = canvas.toDataURL('image/png');
                // Create an image element from the data URL
                var img = new Image();
                img.src = dataURL;
                // img.download = dataURL;
                // Create a link element
                var a = document.createElement('a');
                a.innerHTML = 'DOWNLOAD';
                a.target = '_blank';
                // Set the href of the link to the data URL of the image
                a.href = img.src;
                // Set the download attribute of the link
                a.download = 'capture-image';
                // Append the link to the page
                document.body.appendChild(a);
                // Click the link to trigger the download
                a.click();
            });
        }
    };

    const handleShare = () => { };

    return (
        <div className="flex gap-[15px] mt-[15px] hover:cursor-pointer">
            <div onClick={handleLike}>{isLiked ? <IconLikeFilled size={16} /> : <IconLike />}</div>
            <div onClick={handleDisliked}>{isDisliked ? <IconDislikeFilled size={16} /> : <IconDislike />}</div>
            <div onClick={() => handleCopy(content)}>
                <IconCopy />
            </div>
            {/* <div onClick={handleDownload}>
                <IconDownload />
            </div> */}
            {/* <div onClick={handleShare}>
                <IconShare />
            </div> */}
            <div onClick={onOpenModalReport}>
                <IconReport />
            </div>
        </div>
    );
};

export default InteractButtons;
