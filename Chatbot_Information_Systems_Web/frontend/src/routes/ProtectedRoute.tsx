
import React, { ReactNode } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { getInfoUser } from 'src/lib/api/auth';
import { useAuth } from 'src/lib/hooks/useAuthContext';
const isAuthenticated = () => {
    const token = localStorage.getItem('token');
    return !!token;
};
interface Props {
    children?: ReactNode;
}

const ProtectedRoute = ({ children }: Props) => {
    const { user, loading } = useAuth();
    if (!loading) {
        if (user) {
            return children ? <>{children}</> : <Outlet />;
        }
        return <Navigate to="/login" replace />;
    }
    return <Navigate to="/login" replace />;

};

export default ProtectedRoute;