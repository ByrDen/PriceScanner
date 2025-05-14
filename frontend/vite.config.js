import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    allowedHosts: ['5eadcdb2f09e55.lhr.life'],
  },
    build: {
    outDir: 'dist', // должно быть dist
  },
})

