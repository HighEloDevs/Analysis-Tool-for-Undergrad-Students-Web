<template>
  <v-container
    fill-height
    fluid
    :class="$vuetify.theme.dark ? 'background-dark' : 'background-light'"
    class="d-flex flex-column align-center justify-center"
  >
    <v-alert type="warning" :value="true" width="400px">
      Por enquanto só estamos aceitando o cadastro de alunos da
      <strong>Universidade de São Paulo</strong>
    </v-alert>
    <v-alert type="error" :value="showAlert" width="400px">
      {{ alertMessage }}
    </v-alert>
    <v-card outlined width="400px">
      <v-card-title primary-title class="d-flex flex-column justify-center">
        <span>Cadastro de usuário</span>
        <span class="caption grey--text">
          Insira seus dados e comece a usar!
        </span>
      </v-card-title>
      <v-card-text>
        <v-form ref="signupForm" @submit.prevent="signup" lazy-validation>
          <div class="d-flex">
            <v-text-field
              :rules="required"
              v-model="data.firstName"
              class="mr-2"
              label="Nome"
              outlined
              dense
            ></v-text-field>
            <v-text-field
              :rules="required"
              v-model="data.lastName"
              class="ml-2"
              label="Sobrenome"
              outlined
              dense
            ></v-text-field>
          </div>
          <v-text-field
            :rules="usernameRules"
            v-model="data.username"
            label="Nome de usuário"
            outlined
            dense
          ></v-text-field>
          <v-text-field
            :rules="emailRules"
            v-model="data.email"
            label="E-mail"
            outlined
            dense
          ></v-text-field>
          <v-text-field
            :rules="passwordRules"
            :type="showPassword ? 'text' : 'password'"
            v-model="data.password"
            label="Senha"
            outlined
            dense
          >
            <template #append>
              <v-icon
                @click="showPassword = !showPassword"
                v-text="showPassword ? 'fa-eye' : 'fa-eye-slash'"
                dense
              >
              </v-icon>
            </template>
          </v-text-field>
          <v-text-field
            :rules="passwordRules"
            :type="showPassword1 ? 'text' : 'password'"
            v-model="data.password1"
            label="Confirme a senha"
            outlined
            dense
          >
            <template #append>
              <v-icon
                @click="showPassword1 = !showPassword1"
                v-text="showPassword1 ? 'fa-eye' : 'fa-eye-slash'"
                dense
              >
              </v-icon> </template
          ></v-text-field>
          <v-btn color="primary" type="submit" block>Cadastrar</v-btn>
          <div class="d-flex justify-center mt-3">
            <a href="/login" class="text-decoration-none">
              Já possui cadastro? Entre!
            </a>
          </div>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'SignInPage',
  auth: false,
  data() {
    return {
      data: {
        firstName: '',
        lastName: '',
        username: '',
        email: '',
        password: '',
        password1: '',
      },
      showAlert: false,
      alertMessage: '',
      showPassword: false,
      showPassword1: false,
      required: [(v) => !!v || 'Campo obrigatório!'],
      passwordRegex:
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/,
      usernameRegex:
        /^(?=.{4,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$/,
      nameRules: [(v) => !!v || 'Campo obrigatório!'],
      emailRules: [
        (v) => !!v || 'E-mail é obrigatório!',
        (v) => /.+@.+\..+/.test(v) || 'E-mail inválido!',
      ],
      passwordRules: [
        (v) => !!v || 'Senha é obrigatória!',
        (v) => this.passwordRegex.test(v) || 'Senha inválida!',
      ],
      usernameRules: [
        (v) => !!v || 'Usuário é obrigatório!',
        (v) => this.usernameRegex.test(v) || 'Usuário inválido!',
      ],
    }
  },

  methods: {
    signup() {
      if (!this.$refs.signupForm.validate()) return
      else if (this.data.password !== this.data.password1) {
        this.showAlert = true
        this.alertMessage = 'Senhas não conferem!'
        return
      }

      this.$axios
        .post('/auth/user/', this.data)
        .then(() => {
          this.$router.push('/login')
        })
        .catch((e) => {
          this.alert = true
          this.alertMessage = e.response.data.message
        })
    },
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
