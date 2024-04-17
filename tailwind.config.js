/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html", "./templates/*/*.html"],
  theme: {
    fontFamily: {
      sans: ['"montserrat"', '"PT Sans"', 'sans-serif']
    },
    extend: {
      colors: {
        background: 'hsl(0, 0%, 0.9%)',
        foreground: 'hsl(0, 0%, 90%)',
        card: 'hsl(0, 0%, 2.9%)',
        'card-foreground': 'hsl(0, 0%, 98%)',
        popover: 'hsl(0, 0%, 3.9%)',
        'popover-foreground': 'hsl(0, 0%, 98%)',
        primary: 'hsl(151, 66%, 21%)',
        'primary-foreground': 'hsl(0, 85.7%, 97.3%)',
        secondary: 'hsl(0, 0%, 14.9%)',
        'secondary-foreground': 'hsl(0, 0%, 98%)',
        muted: 'hsl(0, 0%, 14.9%)',
        'muted-foreground': 'hsl(0, 0%, 63.9%)',
        accent: 'hsl(0, 0%, 14.9%)',
        'accent-foreground': 'hsl(0, 0%, 98%)',
        destructive: 'hsl(0, 62.8%, 30.6%)',
        'destructive-foreground': 'hsl(0, 0%, 98%)',
        border: 'hsl(0, 0%, 14.9%)',
        input: 'hsl(0, 0%, 14.9%)',
        ring: 'hsl(151, 66%, 21%)',
      }
    },
  },
  plugins: [],
}

