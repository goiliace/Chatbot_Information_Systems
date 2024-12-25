import { Suspense, lazy, useEffect, useState } from 'react';
import IconDelete from 'src/assets/icons/IconDelete';
import IconLogout from 'src/assets/icons/IconLogout';
import IconPlus from 'src/assets/icons/IconPlus';
import RoundButton from 'src/common/RoundButton';

import { useLocation, useNavigate } from 'react-router-dom';
import { SCREEN } from 'src/routes/path';
import { useAuth } from "src/lib/hooks/useAuthContext";
import { LIST_USING_AGENT, MENU_NAVIGATE } from './constant';
import { GetConversations } from 'src/lib/api/conversation';
import { Conversation } from 'src/types/conversation';
import { Link } from 'react-router-dom';
import { useListAgentNavbar } from 'src/lib/hooks/useNavbar'
import { ReactTyped } from "react-typed";
import { Popover } from 'antd';

interface Props {
    collapsed: boolean;
    onCollapsed: () => void;
}
const NavChatItem = ({ idx, conversation }: { idx: number, conversation: Conversation }) => {
    const navigate = useNavigate();
    return (
        <div onClick={() => navigate(`/c/${conversation.id}`)} >
            <Popover content={conversation.name} className='flex items-center justify-between px-[20px] py-[10px] border rounded-2xl hover:bg-[#c7cace]'>
                <div className="flex gap-x-[10px] w-4/5">
                    {/* <img className="w-[24px] h-[24px] rounded-full" src= /> */}
                    {
                        idx == 0 ? (
                            <ReactTyped className="text-[#151515] font-semibold line-clamp-1" strings={[conversation.name]} typeSpeed={120} showCursor={false} />
                        ) : (<p className="text-[#151515] font-semibold line-clamp-1">
                            {conversation.name}
                        </p>)
                    }

                </div>
                <div className="hover:cursor-pointer">
                    <IconDelete />
                </div>
            </Popover>
        </div >
    );
};
const MainMenu = ({ collapsed, onCollapsed }: Props) => {
    const { user } = useAuth();
    const { listAgentNavbar } = useListAgentNavbar();

    // useEffect(() => {
    //     async function fetchData() {
    //         try {
    //             const response = await GetConversations();
    //             if (Array.isArray(response)) {
    //                 setListAgentNavbar(response as Conversation[]);
    //             } else {
    //                 console.error("Unexpected response format:", response);
    //             }
    //         } catch (error) {
    //             console.error("Failed to fetch conversations:", error);
    //         }
    //     }
    //     fetchData();
    // }, [user]);

    return (
        <div className="hide_scroll grow flex flex-col justify-between gap-y-[20px]">
            <Suspense fallback={<div>Loading...</div>}>
                <div className="flex flex-col gap-y-[20px] mt-[20px] px-[20px]">
                    <div>
                        <div className="hide_scroll flex flex-col mt-[20px] gap-y-[6px] max-h-[500px] overflow-scroll">
                            {listAgentNavbar.map((item, index) => (

                                <NavChatItem key={item.id} idx={index} conversation={item} />
                            ))}
                        </div>
                    </div>

                    <div className="w-full border-t-[3px] border-[#929292] mt-[20px]">
                        <Link to={SCREEN.HOMEPAGE}>
                            <RoundButton className="w-full flex justify-between px-[15px] mt-[20px] !text-[#151515] border border-[#151515] bg-transparent hover:!border-[#04a786] hover:!bg-transparent">
                                <p className="font-semibold">Chat mới</p>
                                <IconPlus />
                            </RoundButton>
                        </Link>
                    </div>
                </div>
            </Suspense>
            <div className={`${collapsed ? 'px-[10px] py-[20px]' : 'py-[20px] px-[24px]'}`}>
                <div className="t-logout-ctrl">
                    <div className="left-content">
                        <div className="logout-ft" >
                            <div className="avata">
                                <img src="https://img-cdn.pixlr.com/image-generator/history/65bb506dcb310754719cf81f/ede935de-1138-4f66-8ed7-44bd16efc709/medium.webp" alt="img" />
                            </div>
                            {!collapsed && <p>{user?.name}</p>}
                        </div>
                    </div>
                    <div className="right-content">
                        <div className="logout-ft" >
                            <IconLogout />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MainMenu;
