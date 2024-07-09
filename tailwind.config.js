/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    fontFamily: {
      sans: [
        "Inter",
        "ui-sans-serif",
        "system-ui", 
        "sans-serif",
        "Apple Color Emoji",
        "Segoe UI Emoji", 
        "Segoe UI Symbol", 
        "Noto Color Emoji",
        ]
    },
    extend: {
      colors: {
        'primary': '#219EBC',
        'secondary': '#023047',
      },
    },
  },
  plugins: [],
}

