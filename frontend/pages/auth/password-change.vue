<template>
  <v-container
    fill-height
    fluid
    class="d-flex flex-column justify-center align-center"
    :class="$vuetify.theme.dark ? 'background-dark' : 'background-light'"
  >
    <v-alert
      :type="alertType"
      :value="showAlert"
      v-text="alertMessage"
      max-width="400px"
    >
    </v-alert>
    <v-card
      :loading="loading"
      max-width="400px"
    >
      <v-card-title> Trocar senha </v-card-title>
      <!-- In case there's a token -->
      <v-card-text v-if="code">
        <v-form
          ref="form"
          @submit.prevent="changePassword"
        >
          <v-text-field
            :type="showPassword ? 'text' : 'password'"
            :rules="passwordRules"
            v-model="password"
            label="Nova senha"
            outlined
          >
            <template #append>
              <v-icon
                dense
                @click="showPassword = !showPassword"
              >
                {{ showPassword ? 'fa-eye' : 'fa-eye-slash' }}
              </v-icon>
            </template>
          </v-text-field>
          <v-text-field
            :type="showPassword1 ? 'text' : 'password'"
            :rules="passwordRules"
            v-model="password1"
            label="Confirmar senha"
            outlined
          >
            <template #append>
              <v-icon
                dense
                @click="showPassword1 = !showPassword1"
              >
                {{ showPassword1 ? 'fa-eye' : 'fa-eye-slash' }}
              </v-icon>
            </template>
          </v-text-field>
          <div class="d-flex flex-column mb-4">
            <span class="grey--text subtitle-2">
              A senha deve conter, pelo menos:
            </span>
            <span class="grey--text subtitle-2"> - Uma letra maiúscula; </span>
            <span class="grey--text subtitle-2"> - Um número; </span>
            <span class="grey--text subtitle-2"> - 8 caracteres. </span>
            <span class="grey--text subtitle-2">
              - Um caracter especial (ex.: !@#$%&*).
            </span>
          </div>
          <v-btn
            :loading="loading"
            color="primary"
            type="submit"
            block
          >
            Trocar senha
          </v-btn>
        </v-form>
      </v-card-text>

      <v-card-text v-else>
        <v-form
          ref="form"
          @submit.prevent="sendPasswordChangeRequest"
        >
          <v-text-field
            :rules="emailRules"
            v-model="email"
            label="E-mail"
            outlined
          ></v-text-field>
          <v-btn
            :loading="loading"
            color="primary"
            type="submit"
            block
          >
            Enviar solicitação
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'PasswordChangePage',
  auth: false,

  data() {
    return {
      code: this.$route.query.code,
      email: this.$route.query.email,
      loading: false,
      password: '',
      password1: '',
      showPassword: false,
      showPassword1: false,
      showAlert: false,
      alertMessage: '',
      alertType: 'error',
      passwordRegex:
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/,
      emailRules: [
        (v) => !!v || 'E-mail é obrigatório!',
        (v) => /.+@.+\..+/.test(v) || 'E-mail inválido!'
      ],
      passwordRules: [
        (v) => !!v || 'Senha é obrigatória!',
        (v) => this.passwordRegex.test(v) || 'Senha inválida!'
      ]
    }
  },

  methods: {
    sendPasswordChangeRequest() {
      if (this.$refs.form.validate()) {
        this.loading = true
        this.$axios
          .post('/auth/send_password_change_request/', {
            email: this.email
          })
          .then(() => {
            this.showAlert = true
            this.alertMessage = 'Solicitação enviada com sucesso!'
            this.alertType = 'success'
          })
          .catch(() => {
            this.showAlert = true
            this.alertMessage = 'Erro ao enviar solicitação!'
            this.alertType = 'error'
          })
          .finally(() => {
            this.loading = false
          })
      }
    },

    changePassword() {
      if (this.password != this.password1) {
        this.showAlert = true
        this.alertMessage = 'Senhas não conferem!'
        this.alertType = 'error'
        return
      } else if (this.$refs.form.validate()) {
        this.loading = true
        this.$axios
          .post('/auth/change_password/', {
            email: this.email,
            code: this.code,
            password: this.password
          })
          .then(() => {
            this.showAlert = true
            this.alertMessage = 'Senha alterada com sucesso!'
            this.alertType = 'success'
            setTimeout(() => {
              this.$router.push('/auth/')
            }, 2000)
          })
          .catch((e) => {
            this.showAlert = true
            this.alertMessage = e.response.data.message
            this.alertType = 'error'
          })
          .finally(() => {
            this.loading = false
          })
      }
    }
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
