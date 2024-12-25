import { createBrowserRouter, Outlet } from 'react-router-dom';
import MainLayout from 'src/layouts/MainLayout';
import AuthLayout from 'src/layouts/AuthLayout';
import { SCREEN } from './path';
import LoginPage from 'src/features/auth/login';
import ProtectedRoute from 'src/routes/ProtectedRoute';
import Chatting from 'src/features/conversation';


const router = createBrowserRouter([
    {
        path: '/',
        element: (
            <ProtectedRoute>
                <MainLayout>
                    <Outlet />
                </MainLayout>
            </ProtectedRoute>

        ),
        children: [
            {
                path: SCREEN.HOMEPAGE,
                element: <Chatting />,
            },
            {
                path: SCREEN.CHATTING,
                element: <Chatting />,
            },
        ],
    },
    {
        path: '/',
        element: (
            // <AuthenticationLayout>
            // </AuthenticationLayout>\
            <AuthLayout>
                <Outlet />
            </AuthLayout>

        ),
        children: [
            {
                path: SCREEN.LOGIN,
                element: <LoginPage />,
            },
        ],
    },
]);

export default router;
