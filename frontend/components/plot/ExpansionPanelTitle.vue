<template>
  <v-expansion-panel>
    <v-expansion-panel-header class="">Título</v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-slider
        :value="title.textStyle.fontSize"
        label="Tamanho da fonte"
        step="1"
        max="30"
        min="10"
        thumb-label
        ticks
        @change="setData({ path: 'title.textStyle.fontSize', value: $event })"
      ></v-slider>
      <v-slider
        :value="title.textStyle.fontWeight"
        label="Grossura da fonte"
        step="100"
        max="900"
        min="100"
        thumb-label
        ticks
        @change="setData({ path: 'title.textStyle.fontWeight', value: $event })"
      ></v-slider>
      <v-radio-group
        :value="title.left"
        class="my-0"
        label="Posição"
        row
        @change="setData({ path: 'title.left', value: $event })"
      >
        <v-radio label="Esquerda" value="left"></v-radio>
        <v-radio label="Centro" value="center"></v-radio>
        <v-radio label="Direita" value="right"></v-radio>
      </v-radio-group>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  computed: {
    ...mapState({
      title: (state) => state.plot.title
    })
  },

  methods: {
    ...mapMutations({
      setData: 'plot/setData'
    })
  }
}
</script>
