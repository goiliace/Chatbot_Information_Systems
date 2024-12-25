import { Input } from 'antd';
import { forwardRef } from 'react';

interface Props {
    [key: string]: any;
}

const RoundInput = forwardRef(({ className, ...rest }: Props, ref) => {
    return <Input className={`rounded-full border border-black ${className}`} {...rest} />;
});

export default RoundInput;
