module.exports = {
  content: [
    "./public/**/*.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    // "./node_modules/flowbite/**/*.js",
  ],
  darkMode: "class",
  theme: {
    extend: {
      width: {
        sidebar: "350px",
        search: "400px",
      },
      rotate: {
        137: "137deg",
      },
      backgroundColor: {
        packed: "#EEF6FF",
        // packed: "#f2f2f2", you can use this color if you like
      },
      backgroundImage: {
        "logo-light": "url('./src/assets/img/logo.png')",
        "logo-dark": "url('./src/assets/img/logo-izied-05.png')",
      },
      colors: {
        primary: "#4F46E5",
      },
      fontFamily: {
        lexend: "'Lexend', sans-serif",
      },
    },
  },
  variants: {
    extend: {
      backgroundImage: ["dark"],
    },
  },
  plugins: [],
};
