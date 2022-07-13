<template>
  <v-expansion-panel>
    <v-expansion-panel-header>Gráfico</v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-subheader class="pl-0"> Direita </v-subheader>
      <v-slider
        :value="grid.right"
        step="5"
        max="200"
        min="5"
        thumb-label
        ticks
        @change="setData({ path: 'grid.right', value: $event })"
      ></v-slider>
      <v-subheader class="pl-0"> Esquerda </v-subheader>
      <v-slider
        :value="grid.left"
        step="5"
        max="200"
        min="5"
        thumb-label
        ticks
        @change="setData({ path: 'grid.left', value: $event })"
      ></v-slider>
      <v-subheader class="pl-0"> Cima </v-subheader>
      <v-slider
        :value="grid.top"
        step="5"
        max="200"
        min="5"
        thumb-label
        ticks
        @change="setData({ path: 'grid.top', value: $event })"
      ></v-slider>
      <v-subheader class="pl-0"> Baixo </v-subheader>
      <v-slider
        :value="grid.bottom"
        step="5"
        max="200"
        min="5"
        thumb-label
        ticks
        @change="setData({ path: 'grid.bottom', value: $event })"
      ></v-slider>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  computed: {
    ...mapState({
      grid: (state) => state.plot.grid
    })
  },

  methods: {
    ...mapMutations({
      setData: 'plot/setData'
    })
  }
}
</script>
