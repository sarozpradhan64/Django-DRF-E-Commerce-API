import {resolve } from 'path';
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


module.exports = {
  plugins: [react({include:'**/*.disabled'})],
  root: resolve('./static/src'),
  base: '/static/',
  server: {
    host: 'localhost',
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: ['.js', '.json'],
  },
  build: {
    outDir: resolve('./static/dist'),
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: resolve('./static/src/js/main.jsx'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
};