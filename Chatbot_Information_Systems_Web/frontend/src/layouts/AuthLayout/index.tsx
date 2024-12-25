import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from "src/lib/hooks/useAuthContext";
import { useEffect } from 'react';

interface Props {
    children: React.ReactNode;
}
const AuthLayout = ({ children }: Props) => {
    const navigate = useNavigate();
    const { user } = useAuth();
    useEffect(() => {
        if (user) {
            navigate('/');
        }
    }, [user]);
    return (
        <div className="flex h-screen "
            style={{
                background: 'linear-gradient(180deg, #002053 41.36%, #0053D7 94%)',
            }}>
            <div className=" flex-1 flex flex-col justify-between p-12 text-white ">
                <div className='relative w-full h-full'>
                    <div className="absolute top-[20px] left-[20px] flex flex-col items-start" style={{ transform: "translateY(-70%)", gap: "62px" }}>
                        <div className="w-[180px]">
                            <img
                                src="./logo_white.png"
                                alt="negative-image"
                            // style={{ filter: "invert(100%) brightness(10)" }}
                            // className="-ml-[48px]"
                            />
                        </div>

                    </div>
                    <div className="absolute top-[50%] left-[66px] flex flex-col items-start" style={{ transform: "translateY(-70%)", gap: "10px" }}>

                        <div className="w-[752px] h-[53px]">
                            <h2 className="text-[44px] font-semibold">INFOMATION SYSTEM CHATBOT</h2>
                        </div>
                        <div
                            className="text-sm"
                            style={{
                                fontFamily: 'SF Pro Display, sans-serif',
                                fontSize: '14px',
                                fontWeight: 400,
                                lineHeight: '22px',
                                textAlign: 'left',
                            }}
                        >
                            <p>Produced by <b>Cao Nguyen Gia Hung - 20089711</b></p>
                        </div>
                    </div>
                </div>

            </div>
            <div className="w-[480px] bg-white flex items-center justify-center">
                <div className=" p-6 pb-16 flex flex-col justify-center" style={{ left: '960px' }}>
                    {children}
                </div>
            </div>
        </div>
    );
};

export default AuthLayout;