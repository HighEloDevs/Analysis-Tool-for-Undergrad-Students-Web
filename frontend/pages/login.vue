<template>
  <v-container 
    class="d-md-flex justify-md-space-between d-flex-column justify-center align-center fill-height"
    style="max-width: 900px";  
  >
    <img src="~/static/logos/logo_vertical.svg" width="350px" class=""></img>
    <AuthenticationTab />
  </v-container>
</template>

<script>
export default {
  name: 'LoginPage',

  data() {
    return {}
  },

  methods: {},
}
</script>

<style lang="css">
.logo {
  font-family: 'Unica One', cursive;
}
</style>
