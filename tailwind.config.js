/** @type {import('tailwindcss').Config} */

const typography = require('@tailwindcss/typography');

module.exports = {

  content: [
    "./blog/templates/**/*.html",
    "./yourproject/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    typography,
  ],
  darkMode: "selector",
};
