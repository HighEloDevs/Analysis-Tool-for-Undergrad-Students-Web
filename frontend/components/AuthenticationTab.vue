<template>
  <v-card class="round">
    <v-alert
      class="mb-3"
      transition="scale-transition"
      :value="alert"
      :type="alertType"
    >
      {{ alertMessage }}
    </v-alert>

    <v-card width="400px">
      <!-- Recover Password -->
      <v-container flat class="pa-5" v-if="forgotPassword">
        <v-card-title primary-title> Recuperação de senha </v-card-title>
        <v-form
          lazy-validation
          value
          class="d-flex flex-column justify-center"
          ref="formRecover"
        >
          <v-text-field
            v-model="passRecoverData.email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
        </v-form>
        <v-card-actions class="justify-end">
          <v-btn text color="white" @click="forgotPassword = !forgotPassword">
            VOLTAR
          </v-btn>
          <v-btn text color="primary" @click="recoverPassword">
            ENVIAR SOLICITAÇÃO
          </v-btn>
        </v-card-actions>
      </v-container>

      <!-- Email Validation -->
      <v-container class="pa-5" v-else-if="emailValidation">
        <v-card-title primary-title>
          Insira o código de verificação
        </v-card-title>
        <v-overlay absolute :value="loading">
          <v-progress-circular
            indeterminate
            color="primary"
          ></v-progress-circular>
        </v-overlay>
        <v-otp-input
          length="6"
          v-model="confirmationCode"
          @finish="validateEmail"
        ></v-otp-input>
        <v-card-actions class="justify-end">
          <v-btn text color="white" @click="emailValidation = !emailValidation">
            VOLTAR
          </v-btn>
        </v-card-actions>
      </v-container>

      <!-- Tabs -->
      <v-container v-else fluid class="pa-0">
        <v-tabs v-model="tab" fixed-tabs>
          <v-tabs-slider></v-tabs-slider>
          <v-tab href="#tab-1"> ENTRAR </v-tab>
          <v-tab href="#tab-2"> CADASTRAR </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
          <!-- Login Tab -->
          <v-tab-item value="tab-1">
            <v-container fluid class="pa-5">
              <v-form
                lazy-validation
                value
                class="d-flex flex-column justify-center"
                ref="formLogin"
              >
                <v-text-field
                  v-model="loginData.username"
                  :rules="usernameRules"
                  label="Nome de usuário"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="loginData.password"
                  :rules="passwordRules"
                  :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="showPassword ? 'text' : 'password'"
                  label="Senha"
                  required
                  @click:append="showPassword = !showPassword"
                ></v-text-field>
                <v-btn block color="primary" @click="login" class="mt-3">
                  ENTRAR
                </v-btn>
                <a
                  class="text-center mt-3"
                  @click="forgotPassword = !forgotPassword"
                  >Esqueceu a senha?
                </a>
              </v-form>
            </v-container>
          </v-tab-item>

          <!-- SignIn Tab -->
          <v-tab-item value="tab-2">
            <v-container fluid class="pa-5">
              <v-form
                lazy-validation
                value
                class="d-flex flex-column justify-center"
                ref="formSignup"
              >
                <div class="d-flex">
                  <v-text-field
                    v-model="signupData.firstName"
                    :rules="nameRules"
                    label="Nome"
                    class="mr-2"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="signupData.lastName"
                    :rules="nameRules"
                    label="Sobrenome"
                    class="ml-2"
                    required
                  ></v-text-field>
                </div>
                <v-text-field
                  v-model="signupData.username"
                  :rules="usernameRules"
                  label="Nome de usuário"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="signupData.email"
                  :rules="emailRules"
                  label="E-mail"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="signupData.password"
                  :rules="passwordRules"
                  :append-icon="showPassword1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="showPassword1 ? 'text' : 'password'"
                  label="Senha"
                  required
                  @click:append="showPassword1 = !showPassword1"
                ></v-text-field>
                <v-text-field
                  v-model="signupData.password1"
                  :rules="passwordRules"
                  :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="showPassword2 ? 'text' : 'password'"
                  label="Confirme a senha"
                  required
                  @click:append="showPassword2 = !showPassword2"
                ></v-text-field>
                <p class="grey--text darken-4 caption ma-0">
                  A senha deve conter, pelo menos:
                </p>
                <p class="grey--text darken-4 caption ma-0">- 8 caracteres;</p>
                <p class="grey--text darken-4 caption ma-0">
                  - um caracter especial;
                </p>
                <p class="grey--text darken-4 caption ma-0">
                  - uma letra maiúscula;
                </p>
                <p class="grey--text darken-4 caption ma-0">- um número.</p>
                <v-btn block color="primary" @click="signup" class="mt-3">
                  CADASTRAR
                </v-btn>
              </v-form>
            </v-container>
          </v-tab-item>
        </v-tabs-items>
      </v-container>
    </v-card>
  </v-card>
</template>

<script>
export default {
  name: 'LoginPage',

  data() {
    return {
      tab: 'tab-1',
      confirmationCode: '',
      alertMessage: '',
      alertType: 'success',
      alert: false,
      loading: false,
      showPassword: false,
      showPassword1: false,
      showPassword2: false,
      forgotPassword: false,
      emailValidation: false,
      loginData: {
        username: '',
        password: '',
      },
      signupData: {
        firstName: '',
        lastName: '',
        username: '',
        email: '',
        password: '',
        password1: '',
      },
      passRecoverData: {
        email: '',
      },

      passwordRegex:
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/,
      usernameRegex:
        /^(?=.{6,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$/,

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
    async login() {
      if (!this.$refs.formLogin.validate()) return
      this.$auth
        .loginWith('local', { data: this.loginData })
        .then((r) => {
          console.log(r)
        })
        .catch((err) => {
          console.log(err)
          this.alertMessage = err.response.data.message
          this.alertType = 'error'
          this.alert = true
        })
      //   this.$axios
      //     .post('/auth/login', this.loginData)
      //     .then((r) => {
      //       console.log(r)
      //     })
      //     .catch((e) => {
      //       this.alert = true
      //       this.alertMessage = e.response.data.message
      //       this.alertType = 'error'
      //     })
    },

    async signup() {
      if (!this.$refs.formSignup.validate()) return
      else if (this.signupData.password !== this.signupData.password1) {
        this.alert = true
        this.alertMessage = 'Senhas não conferem!'
        this.alertType = 'error'
        return
      }

      this.$axios
        .post('/auth/user/', this.signupData)
        .then((r) => {
          // this.emailValidation = true
          this.alert = true
          this.alertMessage = 'Cadastro realizado com sucesso!'
          this.alertType = 'success'
          this.tab = 'tab-1'
        })
        .catch((e) => {
          this.alert = true
          this.alertMessage = e.response.data.message
          this.alertType = 'error'
        })
    },

    async recoverPassword() {
      if (!this.$refs.formRecover.validate()) return
      this.forgotPassword = !this.forgotPassword
    },

    async validateEmail(rsp) {
      this.loading = true
      this.$axios
        .post('/auth/validateEmail', {
          confirmationCode: rsp,
          username: this.username,
        })
        .then((r) => {
          this.alert = true
          this.alertMessage = 'Cadastro realizado com sucesso!'
          this.alertType = 'success'
          this.emailValidation = false
          this.tab = 'tab-1'
        })
        .catch((e) => {
          if (e.response.status === 400) {
            this.alert = true
            this.alertMessage = e.response.data.message
            this.alertType = 'error'
          }
        })
      this.loading = false
    },
  },

  watch: {
    alert(val) {
      if (val) {
        setTimeout(() => {
          this.alert = false
        }, 5000)
      }
    },
  },
}
</script>
