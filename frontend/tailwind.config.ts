import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./lib/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#17201b",
        mist: "#f7f9f7",
        leaf: "#2f855a",
        amber: "#a16207",
        brick: "#b42318"
      }
    }
  },
  plugins: []
};

export default config;
