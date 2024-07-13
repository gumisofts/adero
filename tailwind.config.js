/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: [
          "'Inter'",
          ...defaultTheme.fontFamily.sans
          ]
      },
      colors: {
        'primary': '#219EBC',
        'secondary': '#023047',
      },
    },
  },
  plugins: [],
}

