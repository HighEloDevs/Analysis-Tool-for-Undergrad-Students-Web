<template>
  <v-container
    fill-height
    fluid
    class="d-flex flex-column justify-center align-center"
    :class="$vuetify.theme.dark ? 'background-dark' : 'background-light'"
  >
    <v-card width="400px">
      <v-card-title> Trocar senha </v-card-title>
      <v-card-text>
        <v-text-field
          :type="showPassword ? 'text' : 'password'"
          v-model="password"
          label="Nova senha"
          type="password"
          outlined
          dense
        >
          <template #append>
            <v-btn
              icon
              @click="showPassword = !showPassword"
            >
              <v-icon dense>
                {{ showPassword ? 'fa-eye' : 'fa-eye-slash' }}
              </v-icon>
            </v-btn>
          </template>
        </v-text-field>
        <v-text-field
          :type="showPassword1 ? 'text' : 'password'"
          v-model="password1"
          label="Confirmar senha"
          outlined
          dense
        >
          <template #append>
            <v-btn
              icon
              @click="showPassword = !showPassword"
            >
              <v-icon dense>
                {{ showPassword ? 'fa-eye' : 'fa-eye-slash' }}
              </v-icon>
            </v-btn>
          </template>
        </v-text-field>
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
      password: '',
      password1: '',
      showPassword: false,
      showPassword1: false
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
