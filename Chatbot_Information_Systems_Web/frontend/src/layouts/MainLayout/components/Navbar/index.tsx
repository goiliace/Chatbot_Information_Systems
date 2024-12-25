import { Flex } from 'antd';
import { useNavigate } from 'react-router-dom';
import IconCollapseRight from 'src/assets/icons/IconCollapseRight';
import IconCollapseLeft from 'src/assets/icons/IconCollapseLeft';
import { SCREEN } from 'src/routes/path';
import MainMenu from './MainMenu';
import './MainMenu.scss'
interface Props {
    collapsed: boolean;
    handleCollapsed: () => void;
}

const Navbar = ({ collapsed, handleCollapsed }: Props) => {
    const navigate = useNavigate();

    return (
        <div className="flex flex-col h-full max-h-[1040px]">
            <Flex className={`ctrl-logo-icon  ${collapsed ? '' : ' ml-16 mt-2'} ${collapsed ? 'gap-[5px]' : 'gap-[46px]'}`}>
                <img src={`./logo.png`} alt="logo" className="hover:cursor-pointer" onClick={() => navigate(SCREEN.HOMEPAGE)} width={collapsed ? 62 : 80} />
            </Flex>
            <MainMenu collapsed={collapsed} onCollapsed={handleCollapsed} />
        </div>
    );
};

export default Navbar;

