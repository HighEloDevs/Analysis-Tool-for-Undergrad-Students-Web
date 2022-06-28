<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card width="400px">
      <v-tabs v-if="!forgotPassword" v-model="tab" fixed-tabs>
        <v-tabs-slider></v-tabs-slider>
        <v-tab href="#tab-1"> ENTRAR </v-tab>
        <v-tab href="#tab-2"> CADASTRAR </v-tab>
      </v-tabs>

      <v-tabs-items v-if="!forgotPassword" v-model="tab">
        <v-tab-item value="tab-1">
          <v-card flat class="pa-5">
            <v-form
              lazy-validation
              value
              input="Event"
              reset="Function"
              validate="Function"
              class="d-flex flex-column justify-center"
              ref="formLogin"
            >
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                :rules="passwordRules"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showPassword ? 'text' : 'password'"
                label="Senha"
                required
                @click:append="showPassword = !showPassword"
              ></v-text-field>
              <v-btn block color="primary" @click="teste" class="mt-3">
                ENTRAR
              </v-btn>
              <a
                class="text-center mt-3"
                @click="forgotPassword = !forgotPassword"
                >Esqueceu a senha?</a
              >
            </v-form>
          </v-card>
        </v-tab-item>

        <v-tab-item value="tab-2">
          <v-card flat class="pa-5">
            <v-form
              lazy-validation
              value
              input="Event"
              reset="Function"
              validate="Function"
              class="d-flex flex-column justify-center"
              ref="formSignin"
            >
              <v-text-field
                v-model="username"
                :rules="usernameRules"
                label="Nome de Usuário"
                required
              ></v-text-field>
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                required
              ></v-text-field>
              <v-text-field
                v-model="password1"
                :rules="passwordRules"
                :append-icon="showPassword1 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showPassword1 ? 'text' : 'password'"
                label="Senha"
                required
                @click:append="showPassword1 = !showPassword1"
              ></v-text-field>
              <v-text-field
                v-model="password2"
                :rules="passwordRules"
                :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showPassword2 ? 'text' : 'password'"
                label="Senha"
                required
                @click:append="showPassword2 = !showPassword2"
              ></v-text-field>
              <v-btn block color="primary" @click="signin" class="mt-3">
                CADASTRAR
              </v-btn>
            </v-form>
          </v-card>
        </v-tab-item>
      </v-tabs-items>

      <v-card v-else flat class="pa-5">
        <v-card-title primary-title> Recuperação de senha </v-card-title>
        <v-form
          lazy-validation
          value
          input="Event"
          reset="Function"
          validate="Function"
          class="d-flex flex-column justify-center"
          ref="formRecover"
        >
          <v-text-field
            v-model="email"
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
      </v-card>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'IndexPage',

  data() {
    return {
      tab: null,
      showPassword: false,
      showPassword1: false,
      showPassword2: false,
      forgotPassword: false,
      email: '',
      emailRules: [
        (v) => !!v || 'E-mail é obrigatório!',
        (v) => /.+@.+\..+/.test(v) || 'E-mail inválido!',
      ],
      password: '',
      password1: '',
      password2: '',
      passwordRules: [(v) => !!v || 'Senha é obrigatória!'],
      username: '',
      usernameRules: [(v) => !!v || 'Usuário é obrigatório!'],
    }
  },

  methods: {
    async teste() {
      let teste = this.$axios
        .$get('/auth/teste', { params: { teste: 123 } })
        .then((r) => {
          console.log(r)
        })
    },

    async login() {
      if (!this.$refs.formLogin.validate()) return
    },

    async signin() {
      if (!this.$refs.formSignin.validate()) return
    },

    async recoverPassword() {
      if (!this.$refs.formRecover.validate()) return
      this.forgotPassword = !this.forgotPassword
    },
  },
}
</script>
