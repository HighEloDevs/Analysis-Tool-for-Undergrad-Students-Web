<template>
  <v-container
    class="d-flex"
    fluid
    fill-height
    ma-0
    pa-0
  >
    <!-- Left Panel -->
    <div
      class="fill-height primary d-none d-md-flex flex-column"
      :class="$vuetify.theme.dark ? 'background-dark' : 'background-light'"
      style="flex-grow: 3"
    >
      <v-app-bar
        color="transparent"
        flat
      >
        <v-btn
          @click="toggleDarkMode"
          color="white"
          icon
        >
          <v-icon>{{ $vuetify.theme.dark ? 'fa-moon' : 'fa-sun' }}</v-icon>
        </v-btn>
        <v-btn
          color="white"
          text
          >Sobre</v-btn
        >
        <v-btn
          color="white"
          text
          >Contato</v-btn
        >
      </v-app-bar>
      <v-spacer vertical></v-spacer>
      <v-footer
        color="transparent"
        height="65px"
      >
        <img
          src="~/static/logos/highelo-logo-full-white.png"
          alt="High Elo Logotipo"
          width="150px"
          class="mb-6"
        />
      </v-footer>
    </div>

    <!-- Right Panel -->
    <div
      class="d-flex fill-height justify-center align-center"
      style="flex-grow: 1"
    >
      <v-card
        color="transparent"
        width="350px"
        flat
      >
        <v-card-title
          class="flex-column justify-center black--text"
          primary-title
        >
          <img
            v-if="$vuetify.theme.dark"
            src="~/static/logos/highelo-logo-vert-white.png"
            alt="High Elo Logo"
            width="150px"
            class="mb-3"
          />
          <img
            v-else
            src="~/static/logos/highelo-logo-vert-black.png"
            alt="High Elo Logo"
            width="150px"
            class="mb-3"
          />

          <span :class="{ 'white--text': $vuetify.theme.dark }">
            Seja bem-vindo!
          </span>
          <span class="caption grey--text mb-3">
            Insira seus dados para entrar no ATUS
          </span>
        </v-card-title>
        <v-form
          @submit.prevent="login"
          ref="loginForm"
        >
          <v-alert
            type="error"
            :value="alertValue"
          >
            {{ alertMessage }}
          </v-alert>
          <v-text-field
            v-model="data.username"
            label="Nome de usuário"
            outlined
            :error-messages="usernameErrors"
            @input="$v.data.username.$touch()"
            @blur="$v.data.username.$touch()"
          ></v-text-field>
          <v-text-field
            :type="seePassword ? 'text' : 'password'"
            label="Senha"
            v-model="data.password"
            :error-messages="passwordErrors"
            @input="$v.data.password.$touch()"
            @blur="$v.data.password.$touch()"
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
          <v-btn
            color="primary"
            type="submit"
            block
          >
            Entrar
          </v-btn>
        </v-form>
        <div class="d-flex align-center justify-center my-2">
          <a
            href="/auth/password-change"
            class="text-decoration-none"
            >Esqueceu a senha?</a
          >
        </div>
        <v-divider></v-divider>
        <v-btn
          color="secondary"
          class="mt-5"
          href="/auth/signup"
          block
        >
          Cadastrar
        </v-btn>
      </v-card>
    </div>
  </v-container>
</template>

<script>
import { required } from 'vuelidate/lib/validators'
export default {
  name: 'LoginPage',

  data() {
    return {
      data: {
        username: '',
        password: ''
      },
      seePassword: false,
      alertValue: false,
      alertMessage: ''
    }
  },

  methods: {
    login() {
      this.$v.$touch()
      if (!this.$v.$invalid) {
        this.$auth.loginWith('local', { data: this.data }).catch(() => {
          this.alertValue = true
          this.alertMessage = 'Nome de usuário ou senha incorretos!'
        })
      }
    },

    toggleDarkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
      this.$cookiz.set('darkMode', this.$vuetify.theme.dark)
    }
  },

  validations() {
    return {
      data: {
        username: { required },
        password: { required }
      }
    }
  },

  computed: {
    usernameErrors() {
      const errors = []
      if (!this.$v.data.username.$dirty) return errors
      !this.$v.data.username.required && errors.push('Campo obrigatório!')
      return errors
    },

    passwordErrors() {
      const errors = []
      if (!this.$v.data.password.$dirty) return errors
      !this.$v.data.password.required && errors.push('Campo obrigatório!')
      return errors
    }
  },

  watch: {
    alertValue(val) {
      if (val) {
        setTimeout(() => {
          this.alert = false
        }, 8000)
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
