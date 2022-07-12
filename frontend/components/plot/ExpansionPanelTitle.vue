<template>
  <div class="expansion-panel-title">
    {{ left }}
  </div>
  <!-- <v-expansion-panel>
    <v-expansion-panel-header class="">Título</v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-slider
        v-model="title.textStyle.fontSize"
        label="Tamanho da fonte"
        step="1"
        max="30"
        min="10"
        thumb-label
        ticks
        @change="plot"
      ></v-slider>
      <v-slider
        v-model="title.textStyle.fontWeight"
        label="Grossura da fonte"
        step="100"
        max="900"
        min="100"
        thumb-label
        ticks
        @change="plot"
      ></v-slider>
      <v-radio-group v-model="title.left" class="my-0" label="Posição" row @change="plot">
        <v-radio label="Esquerda" value="left"></v-radio>
        <v-radio label="Centro" value="center"></v-radio>
        <v-radio label="Direita" value="right"></v-radio>
      </v-radio-group>
    </v-expansion-panel-content>
  </v-expansion-panel> -->
</template>

<script>
export default {
  props: ['left']
}
</script>
