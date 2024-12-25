import { Select } from 'antd';
import { BaseOptionType, SelectProps } from 'antd/es/select';
import './style.scss';

interface Props extends SelectProps {
    [key: string]: any;
}

const RoundSelect = ({ className, ...rest }: Props) => {
    return <Select className={`custom_select rounded-full border border-black ${className}`} {...rest} />;
};

export default RoundSelect;
