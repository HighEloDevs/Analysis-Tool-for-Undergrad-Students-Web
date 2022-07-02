<template>
  <v-container>
    <v-dialog
      v-model="stepperDialog"
      persistent
      max-width="550px"
      transition="dialog-transition"
    >
      <NewPlotStepper @finishStepper="onFinishStepper" />
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  name: 'PlotPage',
  data() {
    return {
      data: [],
      stepperDialog: true,
    }
  },

  methods: {
    onFinishStepper(data) {
      this.stepperDialog = false
      this.data.push(data)
    },
  },
}
</script>
