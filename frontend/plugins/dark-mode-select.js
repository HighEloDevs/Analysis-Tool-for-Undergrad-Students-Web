export default function ({ app, $vuetify }) {
  if (process.client) {
    // only in client mode
    const themeMode = app.$cookiz.get('darkMode')
    $vuetify.theme.dark = themeMode
  }
}
