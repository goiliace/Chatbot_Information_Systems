import { Button, ButtonProps } from 'antd';
import { twMerge } from 'tailwind-merge';

interface Props extends ButtonProps {
    [key: string]: any;
}

const RoundButton = ({ className, ...rest }: Props) => {
    return <Button className={twMerge(`rounded-full px-8 py-5`, className)} {...rest} />;
};

export default RoundButton;
