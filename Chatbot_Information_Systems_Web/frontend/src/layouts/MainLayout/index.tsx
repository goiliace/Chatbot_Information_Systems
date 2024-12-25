import { Layout } from 'antd';
import { Content } from 'antd/es/layout/layout';
import Sider from 'antd/es/layout/Sider';
import { useState } from 'react';
// import LayoutHeader from './LayoutHeader';
import Navbar from './components/Navbar';

interface Props {
    children: React.ReactNode;
}

const siderStyle: React.CSSProperties = {
    height: 'calc(100vh - 40px)', // Chiều cao của sider để trừ khoảng cách top và bottom
    position: 'fixed',
    top: '20px',
    left: '20px',
    bottom: '20px',
    backgroundColor: '#FFFFFF',
    borderRadius: '16px',
};

const MainLayout = ({ children }: Props) => {
    const [collapsed, setCollapsed] = useState(false);

    const handleCollapsed = () => {
        // setCollapsed((prev) => !prev);
    };

    return (
        <Layout className="w-full h-full min-h-screen bg-[#EEF7FF]">
            <Sider
                style={siderStyle}
                width={240}
                collapsedWidth={100}
                trigger={null}
                collapsible
                collapsed={collapsed}
                className='shadow'
            >
                <Navbar collapsed={collapsed} handleCollapsed={handleCollapsed} />
            </Sider>
            <Layout style={{ marginLeft: collapsed ? 120 : 260 }}> {/* Adjust margin inline start */}
                <Content className="bg-[#FFFFFF]">
                    <div className="h-full bg-[#EEF7FF] rounded-t-[10px] p-[20px]">
                        {children}
                    </div>
                </Content>
            </Layout>
        </Layout>
    );
};

export default MainLayout;
