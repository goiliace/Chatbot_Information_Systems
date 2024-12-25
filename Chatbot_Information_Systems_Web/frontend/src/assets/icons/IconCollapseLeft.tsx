
import React from 'react';

interface IconProps {
    width?: number;
    height?: number;
}

const IconCollapseLeft: React.FC<IconProps> = ({ width = 36, height = 36 }) => {
    return (
        <svg
            width={width}
            height={height}
            viewBox="0 0 36 36"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
        >
            <path d="M26.5186 6.19866V3.09286C26.5186 2.82366 26.2092 2.675 26.0003 2.83974L7.88781 16.9866C7.73392 17.1063 7.6094 17.2595 7.52374 17.4347C7.43808 17.6098 7.39355 17.8022 7.39355 17.9971C7.39355 18.1921 7.43808 18.3844 7.52374 18.5595C7.6094 18.7347 7.73392 18.8879 7.88781 19.0076L26.0003 33.1545C26.2133 33.3192 26.5186 33.1705 26.5186 32.9013V29.7955C26.5186 29.5987 26.4262 29.4098 26.2735 29.2893L11.8092 17.9991L26.2735 6.70491C26.4262 6.58438 26.5186 6.39554 26.5186 6.19866Z"
                fill="white"
                fill-opacity="0.88" />
        </svg>
    );
};

export default IconCollapseLeft;
