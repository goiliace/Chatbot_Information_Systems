import ReactDOM from 'react-dom/client';
import { RouterProvider } from 'react-router-dom';
import { AuthContextProvider } from 'src/lib/hooks/useAuthContext';
import router from './routes';
import './index.scss';
import { ConfigProvider } from 'antd';

ReactDOM.createRoot(document.getElementById('root')!).render(
  // <React.StrictMode>
  <ConfigProvider
    theme={{
      components: {
        Slider: {
          railSize: 8,
          railBg: '#929292',
          railHoverBg: '#929292',
          handleSize: 14,
        },
      },
    }}
  >
    <AuthContextProvider>
      <RouterProvider router={router} />
    </AuthContextProvider>
  </ConfigProvider>
  // </React.StrictMode >
);
