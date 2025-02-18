// vite.config.ts
import { defineConfig } from "file:///opt/webgenai/simple-spa/node_modules/vite/dist/node/index.js";
import react from "file:///opt/webgenai/simple-spa/node_modules/@vitejs/plugin-react/dist/index.mjs";
var vite_config_default = defineConfig({
  define: { "process.env": process.env },
  base: process.env.PROJECT_ID ? `/${process.env.PROJECT_ID}/spa-dev/` : "/spa-dev/",
  plugins: [react()],
  server: {
    host: true,
    // Needed for Docker container port mapping
    port: process.env.VITE_PORT,
    // You can use any port you prefer
    watch: {
      usePolling: true
    }
  }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcudHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCIvb3B0L3dlYmdlbmFpL3NpbXBsZS1zcGFcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfZmlsZW5hbWUgPSBcIi9vcHQvd2ViZ2VuYWkvc2ltcGxlLXNwYS92aXRlLmNvbmZpZy50c1wiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9pbXBvcnRfbWV0YV91cmwgPSBcImZpbGU6Ly8vb3B0L3dlYmdlbmFpL3NpbXBsZS1zcGEvdml0ZS5jb25maWcudHNcIjtpbXBvcnQgeyBkZWZpbmVDb25maWcgfSBmcm9tICd2aXRlJ1xuaW1wb3J0IHJlYWN0IGZyb20gJ0B2aXRlanMvcGx1Z2luLXJlYWN0J1xuXG4vLyBodHRwczovL3ZpdGUuZGV2L2NvbmZpZy9cbmV4cG9ydCBkZWZhdWx0IGRlZmluZUNvbmZpZyh7XG4gIGRlZmluZTogeyAncHJvY2Vzcy5lbnYnOiBwcm9jZXNzLmVudiB9LFxuICBiYXNlOiBwcm9jZXNzLmVudi5QUk9KRUNUX0lEID8gYC8ke3Byb2Nlc3MuZW52LlBST0pFQ1RfSUQgfS9zcGEtZGV2L2AgOiAnL3NwYS1kZXYvJyxcbiAgcGx1Z2luczogW3JlYWN0KCldLFxuICAgIHNlcnZlcjoge1xuICAgICAgICBob3N0OiB0cnVlLCAvLyBOZWVkZWQgZm9yIERvY2tlciBjb250YWluZXIgcG9ydCBtYXBwaW5nXG4gICAgICAgIHBvcnQ6IHByb2Nlc3MuZW52LlZJVEVfUE9SVCwgLy8gWW91IGNhbiB1c2UgYW55IHBvcnQgeW91IHByZWZlclxuICAgICAgICB3YXRjaDoge1xuICAgICAgICAgICAgdXNlUG9sbGluZzogdHJ1ZSxcbiAgICAgICAgfSxcbiAgICB9LFxufSlcblxuXG4vKlxuaW1wb3J0IHsgZGVmaW5lQ29uZmlnIH0gZnJvbSAndml0ZSdcbmltcG9ydCByZWFjdCBmcm9tICdAdml0ZWpzL3BsdWdpbi1yZWFjdCdcblxuLy8gaHR0cHM6Ly92aXRlLmRldi9jb25maWcvXG5leHBvcnQgZGVmYXVsdCBkZWZpbmVDb25maWcoe1xuICBiYXNlOiAnL3NwYS1kZXYvMDFKQzMwS1ZaWUdQRlZENFhCWURBTUVKRkMvbGFuZGluZy8nLFxuICBwbHVnaW5zOiBbcmVhY3QoKV0sXG4gICAgc2VydmVyOiB7XG4gICAgICAgIGhvc3Q6IHRydWUsIC8vIE5lZWRlZCBmb3IgRG9ja2VyIGNvbnRhaW5lciBwb3J0IG1hcHBpbmdcbiAgICAgICAgcG9ydDogNTE3MywgLy8gWW91IGNhbiB1c2UgYW55IHBvcnQgeW91IHByZWZlclxuICAgICAgICB3YXRjaDoge1xuICAgICAgICAgICAgdXNlUG9sbGluZzogdHJ1ZSxcbiAgICAgICAgfSxcbiAgICB9LFxuXG59KVxuKi8iXSwKICAibWFwcGluZ3MiOiAiO0FBQTBQLFNBQVMsb0JBQW9CO0FBQ3ZSLE9BQU8sV0FBVztBQUdsQixJQUFPLHNCQUFRLGFBQWE7QUFBQSxFQUMxQixRQUFRLEVBQUUsZUFBZSxRQUFRLElBQUk7QUFBQSxFQUNyQyxNQUFNLFFBQVEsSUFBSSxhQUFhLElBQUksUUFBUSxJQUFJLFVBQVcsY0FBYztBQUFBLEVBQ3hFLFNBQVMsQ0FBQyxNQUFNLENBQUM7QUFBQSxFQUNmLFFBQVE7QUFBQSxJQUNKLE1BQU07QUFBQTtBQUFBLElBQ04sTUFBTSxRQUFRLElBQUk7QUFBQTtBQUFBLElBQ2xCLE9BQU87QUFBQSxNQUNILFlBQVk7QUFBQSxJQUNoQjtBQUFBLEVBQ0o7QUFDSixDQUFDOyIsCiAgIm5hbWVzIjogW10KfQo=
