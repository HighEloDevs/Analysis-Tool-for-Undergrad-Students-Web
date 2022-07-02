<template>
  <v-container>
    <v-dialog
      v-model="stepperDialog"
      persistent
      max-width="600px"
      transition="dialog-transition"
    >
      <NewPlotStepper />
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  name: 'PlotPage',
  data() {
    return {
      stepperDialog: true,
    }
  },
}
</script>
