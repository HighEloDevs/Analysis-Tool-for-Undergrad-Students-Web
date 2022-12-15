import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

export default defineNuxtPlugin(nuxtApp => {
  const vuetify = createVuetify({
    components,
      directives,
    
      theme: {
          defaultTheme: 'dark',
          themes: {
              dark: {
                  primary: '#3f51b5',
                  secondary: '#b0bec5',
                  accent: '#8c9eff',
                  error: '#b71c1c',
                  success: '#4caf50',
                  info: '#2196f3',
                  warning: '#ffeb3b',
              },
            },
      }
  })

  nuxtApp.vueApp.use(vuetify)
})
