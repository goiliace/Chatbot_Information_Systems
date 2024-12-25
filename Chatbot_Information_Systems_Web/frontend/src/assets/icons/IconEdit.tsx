const IconEdit = ({ size = 24, fill = '#374957' }: { size?: number; fill?: string }) => {
    return (
        <svg width={size} height={size} viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_1_24111)">
                <path
                    d="M22.8533 1.14795C22.1734 0.469151 21.252 0.0878906 20.2913 0.0878906C19.3305 0.0878906 18.4091 0.469151 17.7293 1.14795L1.46526 17.412C0.999511 17.8751 0.630221 18.426 0.378757 19.0327C0.127293 19.6395 -0.00135384 20.2901 0.000259122 20.947V23C0.000259122 23.2652 0.105616 23.5195 0.293152 23.7071C0.480689 23.8946 0.735043 24 1.00026 24H3.05326C3.71002 24.0018 4.36063 23.8734 4.96741 23.6221C5.5742 23.3708 6.12511 23.0016 6.58826 22.536L22.8533 6.27095C23.5318 5.59115 23.9128 4.66992 23.9128 3.70945C23.9128 2.74899 23.5318 1.82776 22.8533 1.14795ZM5.17426 21.122C4.61026 21.6822 3.84822 21.9977 3.05326 22H2.00026V20.947C1.99925 20.5529 2.07642 20.1625 2.2273 19.7984C2.37818 19.4343 2.59977 19.1038 2.87926 18.826L15.2223 6.48295L17.5223 8.78295L5.17426 21.122ZM21.4383 4.85695L18.9323 7.36395L16.6323 5.06895L19.1393 2.56195C19.2903 2.41126 19.4695 2.29179 19.6667 2.21036C19.8639 2.12893 20.0752 2.08714 20.2885 2.08738C20.5019 2.08761 20.7131 2.12986 20.9101 2.21172C21.1071 2.29357 21.2861 2.41343 21.4368 2.56445C21.5875 2.71547 21.7069 2.8947 21.7884 3.09189C21.8698 3.28908 21.9116 3.50038 21.9113 3.71372C21.9111 3.92706 21.8689 4.13827 21.787 4.33529C21.7051 4.5323 21.5853 4.71126 21.4343 4.86195L21.4383 4.85695Z"
                    fill={fill}
                />
            </g>
            <defs>
                <clipPath id="clip0_1_24111">
                    <rect width="24" height="24" fill="white" />
                </clipPath>
            </defs>
        </svg>
    );
};

export default IconEdit;