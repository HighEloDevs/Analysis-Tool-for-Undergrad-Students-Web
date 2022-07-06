<template>
  <v-stepper
    v-model="step"
    vertical
  >
    <!-- Step 1 -->
    <v-stepper-step
      :complete="step > 1"
      :rules="[() => uploadedFiles.length != 0]"
      step="1"
      edit-icon="fa-pen"
      editable
    >
      <span> Quais serão os dados? </span>
      <small>Arquivo contendo os dados do projeto</small>
    </v-stepper-step>
    <v-stepper-content step="1">
      <DropFilesZone
        :uploadedFiles="uploadedFiles"
        accept=".csv,.txt,.tsv,.xlsx"
        class="mb-3"
      />
      <v-btn
        color="primary"
        @click="step = 2"
      >
        Avançar
      </v-btn>
      <v-btn
        text
        color="error"
        to="/"
      >
        Cancelar
      </v-btn>
    </v-stepper-content>

    <!-- Step 2 -->
    <v-stepper-step
      :complete="step > 2"
      step="2"
      edit-icon="fa-pen"
      editable
    >
      Qual a função a ser ajustada?
      <small>Opcional</small>
    </v-stepper-step>
    <v-stepper-content step="2">
      <v-text-field
        v-model="fitFunction"
        @change="getParams"
        class="my-1"
        label="Função"
        prefix="f(x) = "
        hide-details
        outlined
        dense
      ></v-text-field>
      <v-list color="transparent">
        <v-list-item v-if="params.length">
          <v-list-item-title class="grey--text text--darken-1"
            >Parâmetro</v-list-item-title
          >
          <p class="grey--text text--darken-1 text-no-wrap mb-0">
            Valor inicial
          </p>
        </v-list-item>
        <v-list-item
          v-for="param in params"
          :key="param.param"
        >
          <v-list-item-title>{{ param.param }}</v-list-item-title>
          <v-text-field
            v-model="param.value"
            hide-details
            outlined
            dense
          ></v-text-field>
        </v-list-item>
      </v-list>
      <v-btn
        color="primary"
        @click="step = 3"
      >
        Avançar
      </v-btn>
      <v-btn
        text
        color="error"
        to="/"
      >
        Cancelar
      </v-btn>
    </v-stepper-content>

    <!-- Step 3 -->
    <v-stepper-step
      :complete="step > 3"
      step="3"
      edit-icon="fa-pen"
      editable
    >
      Resumo
    </v-stepper-step>
    <v-stepper-content step="3">
      <v-list-item>
        <v-list-item-title>Arquivo de dados</v-list-item-title>
        <v-list-item-subtitle class="text-left">{{
          uploadedFiles.length ? uploadedFiles[0].name : 'Nenhum'
        }}</v-list-item-subtitle>
      </v-list-item>
      <v-list-item>
        <v-list-item-title>Função de ajuste</v-list-item-title>
        <v-list-item-subtitle class="text-left">{{
          !!fitFunction ? fitFunction : 'Nenhum'
        }}</v-list-item-subtitle>
      </v-list-item>
      <v-list-item
        v-for="param in params"
        :key="param.param"
      >
        <v-list-item-title>{{ param.param }}</v-list-item-title>
        <v-list-item-subtitle class="text-left">{{
          param.value
        }}</v-list-item-subtitle>
      </v-list-item>
      <v-btn
        color="primary"
        class="mt-4"
        @click="emitPlot"
        :disabled="!uploadedFiles.length"
      >
        Plot
      </v-btn>
      <v-btn
        text
        color="error"
        class="mt-4"
        to="/"
      >
        Cancelar
      </v-btn>
    </v-stepper-content>
  </v-stepper>
</template>

<script>
export default {
  data() {
    return {
      step: 1,
      fitFunction: '',
      uploadDialog: true,
      uploadedFiles: [],
      params: []
    }
  },
  methods: {
    getParams() {
      console.log(this.fitFunction)
    },

    emitPlot() {
      this.$emit('finishStepper', {
        fitFunction: this.fitFunction,
        file: this.uploadedFiles[0],
        params: this.params
      })
    }
  }
}
</script>
