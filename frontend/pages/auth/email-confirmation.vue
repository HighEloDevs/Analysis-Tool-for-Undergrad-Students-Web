<template>
  <v-container
    class="d-flex align-center justify-center flex-column"
    :class="$vuetify.theme.dark ? 'background-dark' : 'background-light'"
    fluid
    fill-height
  >
    <v-alert type="error" :value="alertValue" width="500px">
      Código de confirmação inválido.
    </v-alert>
    <v-card width="500px">
      <v-card-title> Confirmação do e-mail </v-card-title>
      <v-card-text>
        <v-text-field
          v-model="email"
          label="E-mail para confirmação"
          outlined
          :rules="emailRules"
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
      email: this.$route.query.email,
      code: this.$route.query.code,
      alertValue: false,
      emailRules: [
        (v) => !!v || 'E-mail é obrigatório',
        (v) =>
          /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          'E-mail inválido',
      ],
    }
  },

  methods: {
    confirmEmail() {
      if (!!this.email && !!this.code) {
        this.$axios
          .post('/auth/confirm_email/', {
            email: this.email,
            code: this.code,
          })
          .then(() => {
            this.$router.push('/auth/')
          })
          .catch((e) => {
            console.log(e)
            this.alertValue = true
          })
      }
    },
  },

  mounted() {
    this.confirmEmail()
  },
}
</script>

<style scoped>
.background-light {
  background-image: url('https://images.alphacoders.com/101/1018102.jpg');
  background-size: cover;
  background-position: center;
}

.background-dark {
  background-image: url('https://images8.alphacoders.com/101/1018165.jpg');
  background-size: cover;
  background-position: center;
}
</style>
