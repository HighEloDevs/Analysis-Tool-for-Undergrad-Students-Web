<template>
  <v-stepper v-model="step" vertical>
    <v-stepper-step
      :complete="step > 1"
      :rules="[() => uploadedFiles.length != 0]"
      step="1"
      edit-icon="fa-pen"
      editable
    >
      Quais serão os dados?
      <small>Arquivo contendo os dados do projeto</small>
    </v-stepper-step>
    <v-stepper-content step="1">
      <DropFilesZone
        :uploadedFiles="uploadedFiles"
        multiple
        accept=".csv,.txt,.tsv,.xlsx"
        class="mb-3"
      />
      <v-btn color="primary" @click="step = 2"> Continuar </v-btn>
      <v-btn text color="error" to="/"> Cancelar </v-btn>
    </v-stepper-content>
  </v-stepper>
</template>

<script>
export default {
  data() {
    return {
      step: 1,
      uploadDialog: true,
      uploadedFiles: [],
    }
  },
  methods: {
    processUpload(event) {
      console.log(event)
    },
  },
}
</script>
