import colors from 'vuetify/es5/util/colors'

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s',
    title: 'Analysis Tool for Undergrad Students',
    htmlAttrs: {
      lang: 'pt-br'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Unica+One&display=swap'
      }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  transpile: [/echarts/],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '~/plugins/axios',
    '~/plugins/dark-mode-select',
    '~/plugins/katex',
    '~/plugins/vuelidate'
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    ['cookie-universal-nuxt', { alias: 'cookiz' }]
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: process.env.AXIOS_BASEURL,
    browserBaseURL: process.env.AXIOS_BROWSER_BASEURL
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        light: {
          primary: colors.teal.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        },
        dark: {
          primary: colors.teal.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    },
    defaultAssets: {
      icons: 'fa'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},

  router: { middleware: ['auth', 'dark-mode-select'] },

  auth: {
    strategies: {
      local: {
        user: {
          property: 'user'
        },
        token: {
          property: 'access',
          global: true,
          maxAge: 60 * 30 // 30 minutes
        },
        endpoints: {
          login: {
            url: '/auth/login/',
            method: 'post',
            propertyName: 'access'
          },
          logout: { url: '/auth/logout/', method: 'post' },
          user: { url: '/auth/user/', method: 'get' }
        }
      }
    },

    redirect: {
      login: '/auth',
      logout: '/auth',
      callback: '/auth',
      home: '/'
    }
  },

  ssr: true,
  target: 'server'
}
