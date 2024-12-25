import { axiosInstance as axios } from '../axios';
export async function GetMessages(conversation_id: string) {
    const token = localStorage.getItem('token');
    let baseUrl = '/conversation/history?conversation_id=' + conversation_id;
    try {
        const response = await axios({
            method: 'GET',
            url: baseUrl,
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${token}`,
            },
        });

        if (response.status === 200) {

            return response.data;
        }

        throw new Error(`Unexpected status code: ${response.status}`);
    } catch (error: any) {
        throw new Error(`Failed to fetch brand sentiment: ${error.message || error}`);
    }
}