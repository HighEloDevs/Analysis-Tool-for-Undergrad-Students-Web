<template>
  <v-container>
    <v-btn text small color="primary" @click="logout">Logout</v-btn>
  </v-container>
</template>

<script>
export default {
  name: 'IndexPage',

  data() {
    return {}
  },

  methods: {
    logout() {
      this.$auth.logout('local')
    },
  },
}
</script>
