<template>
  <v-app dark>
    <v-app-bar v-if="$auth.loggedIn" app clipped-left color="primary" flat>
      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title class="grey--text text--lighten-2">
            {{ $auth.user.username }}
          </v-list-item-title>
          <v-list-item-subtitle
            class="grey--text text--lighten-2 d-flex align-center"
          >
            {{ $auth.user.email }}
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-icon
                  v-on="on"
                  v-bind="attrs"
                  class="ml-1 text--lighten-2"
                  :class="false ? 'green--text' : 'red--text'"
                  x-small
                >
                  {{ false ? 'fa-circle-check' : 'fa-circle-exclamation' }}
                </v-icon>
              </template>
              <span>
                {{ false ? 'E-mail verificado!' : 'E-mail não verificado!' }}
              </span>
            </v-tooltip>
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-spacer></v-spacer>
      <v-btn
        text
        small
        class="red--text font-weight-bold"
        @click="$auth.logout('local')"
      >
        Sair
      </v-btn>
    </v-app-bar>
    <v-main>
      <Nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      drawer: true,
      mini: true,
    }
  },

  methods: {
    logout() {},
  },
}
</script>
