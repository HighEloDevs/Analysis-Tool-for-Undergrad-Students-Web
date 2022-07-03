export default function ({ app, $vuetify }) {
  if (!process.client) {
    // only in ssr mode
    // console.log(context.$cookiz.get('darkMode'))
    const darkMode = app.$cookiz.get('darkMode')
    // const themeMode = app.localStorage.getItem('dark_theme') === 'true'
    // const themeMode = 'light'
    console.log(darkMode)
    $vuetify.theme.dark = darkMode
    // if (!darkMode) {
    //   $vuetify.theme.dark = false
    // } else {
    //   $vuetify.theme.dark = true
    // }
  }
}
