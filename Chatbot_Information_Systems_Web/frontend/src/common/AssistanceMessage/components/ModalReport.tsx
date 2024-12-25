import { Form, Modal, Radio, Space } from 'antd';
import RoundButton from 'src/common/RoundButton';
import RoundInput from 'src/common/RoundInput';

interface ModalReportProps {
    openModal: boolean;
    handleCloseModal: () => void;
}

const ModalReport = ({ openModal, handleCloseModal }: ModalReportProps) => {
    const handleSubmit = (values: any) => {
        console.log(values);
    };

    return (
        <Modal centered width={560} open={openModal} onOk={handleCloseModal} onCancel={handleCloseModal} closable={false} footer={null}>
            <Form layout="vertical" className="flex flex-col" initialValues={{ remember: true }} onFinish={handleSubmit} autoComplete="off">
                <p className="text-xl text-[#151515] font-semibold">Hãy cho chúng tôi biết điều gì làm bạn không hài lòng</p>

                <Form.Item name="problem" label={<p className="text-base text-[#151515] font-semibold">Vấn đề bạn đang gặp phải</p>}>
                    <Radio.Group className="custom_radio_answer_item">
                        <Space direction="vertical">
                            <Radio value="a">Thiếu chính xác</Radio>
                            <Radio value="b">Không giảu quyết được vấn đề</Radio>
                            <Radio value="c">Không giao tiếp hiệu quả</Radio>
                        </Space>
                    </Radio.Group>
                </Form.Item>

                <Form.Item name="content" label={<p className="text-xl text-[#151515] font-semibold">Nội dung</p>}>
                    <RoundInput className="py-2 px-5" placeholder="Nhập nội dung" />
                </Form.Item>

                <div className="flex justify-end gap-x-2">
                    <RoundButton onClick={handleCloseModal} className="text-[#929292] text-xl font-semibold">
                        Huỷ bỏ
                    </RoundButton>
                    <RoundButton
                        className="bg-[#05D6AC] text-white text-xl font-semibold hover:!bg-[#00BB95] active:!bg-[#007961]"
                        type="primary"
                        htmlType="submit"
                    >
                        Tiếp tục
                    </RoundButton>
                </div>
            </Form>
        </Modal>
    );
};

export default ModalReport;
