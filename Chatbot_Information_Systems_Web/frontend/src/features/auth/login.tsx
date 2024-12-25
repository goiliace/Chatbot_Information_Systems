import React, { useState } from 'react';
import { Form, Input, Button, Checkbox } from 'antd';
import { UserOutlined, LockOutlined, EyeOutlined, EyeInvisibleOutlined } from '@ant-design/icons';
import { Navigate, useNavigate } from 'react-router-dom';
import { SignIn } from "src/lib/api/auth";
import { useAuth } from "src/lib/hooks/useAuthContext";
import { useEffect } from 'react';
const LoginPage = () => {
    const { handleSetToken } = useAuth();


    const onFinish = async (values: any) => {
        const token = await SignIn(values.username, values.password);

        if (token) {
            await handleSetToken(token);
        }

    };
    return (
        <div className="w-[364px] mx-auto">
            <h2 className="text-3xl font-bold mb-8 text-center">Đăng nhập</h2>
            <Form
                name="login"
                onFinish={onFinish}
                layout="vertical"
                className="space-y-6"
            >
                <Form.Item
                    name="username"
                    rules={[{ required: true, message: 'Vui lòng nhập tên đăng nhập hoặc số điện thoại, email!' }]}
                >
                    <Input
                        prefix={<UserOutlined className="site-form-item-icon mr-2" />}
                        placeholder="Tên đăng nhập hoặc số điện thoại, email"
                        style={{
                            background: '#FCFCFD',
                            border: '1px solid #F2F4F7',
                            width: '360px',
                            height: '40px',
                            padding: '8px 12px',
                            gap: '0px',
                            color: '#98A2B3',
                            borderRadius: '8px 0px 0px 0px',
                            borderTop: '1px solid #F2F4F7',
                            borderLeft: '1px solid #F2F4F7',
                            borderRight: '1px solid #F2F4F7',
                            borderBottom: 'none',
                            opacity: '1'
                        }}
                    />
                </Form.Item>
                <Form.Item
                    name="password"
                    rules={[{ required: true, message: 'Vui lòng nhập mật khẩu!' }]}
                >
                    <Input.Password
                        prefix={<LockOutlined className="site-form-item-icon mr-2" />}
                        placeholder="Mật khẩu của bạn"
                        iconRender={visible => (visible ? <EyeInvisibleOutlined /> : <EyeOutlined />)}
                        style={{
                            background: '#FCFCFD',
                            border: '1px solid #F2F4F7',
                            width: '360px',
                            height: '40px',
                            padding: '8px 12px',
                            gap: '0px',
                            color: '#98A2B3',
                            borderRadius: '8px 0px 0px 0px',
                            borderTop: '1px solid #F2F4F7',
                            borderLeft: '1px solid #F2F4F7',
                            borderRight: '1px solid #F2F4F7',
                            borderBottom: 'none',
                            opacity: '1'
                        }}
                    />
                </Form.Item>

                <Form.Item>
                    <div className="flex items-center justify-between">
                        <Checkbox>Lưu tài khoản</Checkbox>
                        <a href="#" className="text-sm text-blue-500 hover:underline">Lấy lại mật khẩu</a>
                    </div>
                </Form.Item>

                <Form.Item>
                    <Button
                        type="primary"
                        htmlType="submit"
                        className="w-full"
                    >
                        Đăng nhập
                    </Button>
                </Form.Item>
            </Form>
        </div>
    );
};

export default LoginPage;