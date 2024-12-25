import React, { createContext, useContext, useEffect, useState } from 'react';
import { getInfoUser } from 'src/lib/api/auth';

const AuthContext = createContext({});

// Make auth context available across the app by exporting it
export const useAuth = () => useContext<any>(AuthContext);

// Create the auth context provider
interface User {
    id: number;
    username: string;
    email: string;
    avatar_url: string;
    is_active: boolean;
}
export const AuthContextProvider = ({ children }: { children: React.ReactNode }) => {
    const [user, setUser] = useState<User | null>();
    const [token, setToken] = useState<string | null>(localStorage.getItem('token'));
    const [loading, setLoading] = useState<Boolean>(true);

    async function handleSetToken(token: string | null) {
        console.log(token);

        setToken(token);
        localStorage.setItem('token', token || '');
    }

    useEffect(() => {
        async function fetchData() {
            try {
                const user = await getInfoUser();
                setUser(user);
                setLoading(false);
            }
            catch (error) {
                setLoading(false);
                setUser(null);
            }
        }
        setLoading(true);
        fetchData();

    }, [token]);

    return <AuthContext.Provider value={{ user, loading, token, handleSetToken }}>{loading ? null : children}</AuthContext.Provider>;
};