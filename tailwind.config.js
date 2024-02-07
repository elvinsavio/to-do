/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html", "./templates/macros/*.html"],
  theme: {
    extend: {
      colors: {
        bodyBackground: "#0c0a09",
        background: "#0c0a09",
        accent: "#16a34a",
        text: "#F4F5FC",
      },
    },
  },
  plugins: [],
};
