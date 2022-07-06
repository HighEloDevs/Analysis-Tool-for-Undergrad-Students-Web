<template>
  <v-container
    :class="$vuetify.theme.dark ? 'background-dark' : 'background-light'"
    class="d-flex align-center justify-center flex-column"
    fluid
    fill-height
  >
    <v-alert
      :value="alertValue"
      type="error"
      max-width="400px"
    >
      Código de confirmação inválido.
    </v-alert>
    <v-card
      :loading="loading"
      max-width="400px"
    >
      <v-card-title> Confirmação do e-mail </v-card-title>
      <v-card-text>
        <v-text-field
          :rules="emailRules"
          v-model="email"
          label="E-mail para confirmação"
          outlined
        ></v-text-field>
        <v-otp-input
          v-model="code"
          length="6"
          @finish="confirmEmail"
        ></v-otp-input>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'EmailConfirmationPage',
  auth: false,

  data() {
    return {
      loading: false,
      email: this.$route.query.email,
      code: this.$route.query.code,
      alertValue: false,
      emailRules: [
        (v) => !!v || 'E-mail é obrigatório',
        (v) =>
          /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          'E-mail inválido'
      ]
    }
  },

  methods: {
    confirmEmail() {
      if (!!this.email && !!this.code) {
        this.loading = true
        this.$axios
          .post('/auth/confirm_email/', {
            email: this.email,
            code: this.code
          })
          .then(() => {
            this.$router.push('/auth/')
          })
          .catch((e) => {
            console.log(e)
            this.alertValue = true
          })
          .finally(() => {
            this.loading = false
          })
      }
    }
  },

  mounted() {
    this.confirmEmail()
  }
}
</script>

<style scoped>
.background-light {
  background-image: url('/background-light.jpg');
  background-size: cover;
  background-position: center;
}

.background-dark {
  background-image: url('/background-dark.jpg');
  background-size: cover;
  background-position: center;
}
</style>
