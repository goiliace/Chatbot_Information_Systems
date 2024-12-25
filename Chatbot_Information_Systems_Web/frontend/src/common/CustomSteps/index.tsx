import IconArrowRight from 'src/assets/icons/IconArrowRight';
import { twMerge } from 'tailwind-merge';

interface StepItem {
    step: number;
    label: string;
}

interface Props {
    steps: StepItem[];
    currentStep: number;
    className?: string;
}

const CustomStep = ({ steps, currentStep, className }: Props) => {
    return (
        <div className={twMerge('flex justify-center', className)}>
            {steps.map((item, index) => (
                <div className="flex items-center">
                    <div className="flex flex-col items-center justify-center min-w-[200px]" key={index}>
                        <div
                            className={`w-[40px] h-[40px] text-base font-semibold flex items-center justify-center rounded-full ${currentStep >= index + 1 ? 'text-white bg-[#151515]' : 'border-2 border-[#929292] text-[#929292]'}`}
                        >
                            {item.step}
                        </div>
                        <div className={`text-xl  font-semibold ${currentStep >= index + 1 ? 'text-[#151515]' : 'text-[#929292]'}`}>{item.label}</div>
                    </div>
                    {index !== steps.length - 1 && (
                        <div className="mx-[30px]">
                            <IconArrowRight fill={currentStep >= index + 1 ? '#151515' : '#929292'} />
                        </div>
                    )}
                </div>
            ))}
        </div>
    );
};

export default CustomStep;
