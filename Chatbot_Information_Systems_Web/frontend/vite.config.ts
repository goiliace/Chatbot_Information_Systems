import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

import dotenv from 'dotenv';
dotenv.config();
export default defineConfig({
  plugins: [react()],
  define: {
    'process.env': process.env,
  },
  preview: {
    port: 3000,
    host: true,
  },
  resolve: {
    alias: {
      src: path.resolve(__dirname, './src'),
    },
  },
});
