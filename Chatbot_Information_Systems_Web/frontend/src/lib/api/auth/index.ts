import { axiosInstance as axios } from '../axios';

export async function SignIn(username: string, password: string) {
    try {
        const response = await axios({
            method: 'post',
            url: '/auth/token',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            data: new URLSearchParams({
                username: username,
                password: password
            }).toString()
        });
        if (response.status === 200) {
            return response.data.access_token;
        }

        throw new Error(`Unexpected status code: ${response.status}`);

    } catch (error: any) {
        throw new Error(`Failed to fetch brand sentiment: ${error.message || error}`);
    }
}

export async function getInfoUser() {
    const token = localStorage.getItem('token');
    try {
        const response = await axios({
            method: 'get',
            url: '/auth/users/me',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${token}`,
            },
        });


        if (response.status === 200) {
            return response.data;
        }
        throw new Error(`Unexpected status code: ${response.status}`);
    }
    catch (error: any) {
        throw new Error(`Failed to fetch brand sentiment: ${error.message || error}`);
    }
}
