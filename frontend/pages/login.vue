<template>
  <v-container class="d-flex" fluid fill-height ma-0 pa-0>
    <div
      class="fill-height primary d-none d-md-flex flex-column background"
      style="flex-grow: 3"
    >
      <v-app-bar color="transparent" flat>
        <v-btn @click="toggleDarkMode" color="white" icon>
          <v-icon>{{ $vuetify.theme.dark ? 'fa-moon' : 'fa-sun' }}</v-icon>
        </v-btn>
        <v-btn color="white" text>Sobre</v-btn>
        <v-btn color="white" text>Contato</v-btn>
      </v-app-bar>

      <v-spacer vertical></v-spacer>

      <v-footer color="transparent" height="65px">
        <img
          src="~/static/logos/highelo-logo-full-white.png"
          alt="High Elo Logotipo"
          width="150px"
          class="mb-6"
        />
      </v-footer>
    </div>
    <div
      class="d-flex fill-height justify-center align-center"
      style="flex-grow: 1"
    >
      <v-card color="transparent" width="350px" flat>
        <v-card-title
          class="flex-column justify-center black--text"
          primary-title
        >
          <span :class="{ 'white--text': $vuetify.theme.dark }">
            Seja bem-vindo!
          </span>
          <span class="caption grey--text mb-3">
            Insira seus dados para entrar no ATUS
          </span>
        </v-card-title>
        <v-form @submit.prevent="login" ref="loginForm">
          <v-alert type="error" :value="alertValue">
            {{ alertMessage }}
          </v-alert>
          <v-text-field
            :rules="required"
            v-model="data.username"
            label="Nome de usuário"
            outlined
          ></v-text-field>
          <v-text-field
            :type="seePassword ? 'text' : 'password'"
            :rules="required"
            v-model="data.password"
            label="Senha"
            outlined
          >
            <template #append>
              <v-icon
                @click="seePassword = !seePassword"
                v-text="seePassword ? 'fa-eye' : 'fa-eye-slash'"
                dense
              >
              </v-icon>
            </template>
          </v-text-field>
          <v-btn color="primary" type="submit" block> Entrar </v-btn>
        </v-form>
        <div class="d-flex align-center justify-center my-2">
          <a href="/" class="text-decoration-none">Esqueceu a senha?</a>
        </div>
        <v-divider></v-divider>
        <v-btn color="secondary" class="mt-5" href="/signup" block>
          Cadastrar
        </v-btn>
      </v-card>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      data: {
        username: '',
        password: '',
      },
      seePassword: false,
      alertValue: false,
      alertMessage: '',
      required: [(v) => !!v || 'Campo obrigatório!'],
    }
  },

  methods: {
    login() {
      if (!this.$refs.loginForm.validate()) return
      this.$auth.loginWith('local', { data: this.data }).catch(() => {
        this.alertValue = true
        this.alertMessage = 'Nome de usuário ou senha incorretos!'
      })
    },

    toggleDarkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
      localStorage.setItem('dark_theme', this.$vuetify.theme.dark.toString())
    },
  },
  watch: {
    alertValue(val) {
      if (val) {
        setTimeout(() => {
          this.alert = false
        }, 8000)
      }
    },
  },
}
</script>

<style scoped>
.background {
  background-image: url('~/static/background.png');
  background-size: cover;
  background-position: center;
}
</style>
