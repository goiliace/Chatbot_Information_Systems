
import { useState } from 'react';
import Markdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import { CodeBlock } from 'src/features/conversation/components/Codeblock';
import { type UseChatStreamChatMessage } from 'src/types/chat';
import InteractButtons from './components/InteractButtons';
import ModalReport from './components/ModalReport';
// import React from 'react';
import { Flex, Spin, Switch } from 'antd';
import './styles.scss';

interface Props {
    content: UseChatStreamChatMessage;
    captureRef?: React.MutableRefObject<HTMLDivElement | null>;
}

const AssistanceMessage = ({ content, captureRef }: Props) => {
    const [openModalReport, setOpenModalReport] = useState(false);

    const handleOpenModal = () => {
        setOpenModalReport(true);
    };

    const handleCloseModal = () => {
        setOpenModalReport(false);
    };



    return (
        <div className="w-full flex justify-start gap-[20px]">
            <img
                className="w-[28px] h-[28px] rounded-full object-cover"
                src="https://img.freepik.com/free-psd/3d-illustration-human-avatar-profile_23-2150671142.jpg?size=338&ext=jpg&ga=GA1.1.2008272138.1721779200&semt=ais_user"
            />
            <div className="w-fit max-w-[80%] text-md font-medium text-[#13529C] px-[30px] py-[20px] rounded-[30px]  bg-[#FFFFFF]">
                {content.content ? (
                    <>
                        <Markdown
                            remarkPlugins={[remarkMath, remarkGfm]}
                            components={{
                                code(props) {
                                    const { children, className, node, ...rest } = props;
                                    const match = /language-(\w+)/.exec(className || '');
                                    return match ? (
                                        <CodeBlock
                                            key={Math.random()}
                                            language={(match && match[1]) || ''}
                                            value={String(children).replace(/\n$/, '')}
                                            {...props}
                                        />
                                    ) : (
                                        <code {...rest} className={className}>
                                            {children}
                                        </code>
                                    );
                                },
                            }}
                        >
                            {content.content}
                        </Markdown>
                    </>
                ) : (
                    <Spin size="large" />
                )}
                <InteractButtons content={content} captureRef={captureRef} onOpenModalReport={handleOpenModal} />
            </div>
            <ModalReport openModal={openModalReport} handleCloseModal={handleCloseModal} />
        </div>
    );
};

export default AssistanceMessage;
