/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/templates/*.html", "./src/templates/macros/*.html"],
  theme: {
    extend: {
      colors: {
        bodyBackground: "#0c0a09",
        background: "#1c1917",
        accent: "#16a34a",
        text: "#F4F5FC",
      },
    },
  },
  plugins: [],
};
