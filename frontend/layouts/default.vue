<template>
  <v-app dark>
    <v-app-bar
      v-if="$auth.loggedIn"
      app
      dense
      clipped-left
      color="primary"
      flat
    >
      <v-toolbar-title class="text-subtitle-1">
        Bem-vindo,
        <strong>{{ $auth.user.first_name }} {{ $auth.user.last_name }}</strong
        >!
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text small @click="logout">Logout</v-btn>
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
    logout() {
      this.$auth.logout('local')
    },
  },
}
</script>
