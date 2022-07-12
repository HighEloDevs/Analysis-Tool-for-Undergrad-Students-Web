export default function ({ app, $vuetify }) {
  if (!process.client) {
    const darkMode = app.$cookiz.get('darkMode')
    $vuetify.theme.dark = darkMode
  }
}
