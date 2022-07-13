<template>
  <v-expansion-panel>
    <v-expansion-panel-header>Eixo X</v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-row>
        <v-col cols="12" md="4">
          <v-text-field
            :value="xAxis.min"
            label="Mínimo"
            outlined
            dense
            @change="setData({ path: 'xAxis.min', value: $event || null })"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            :value="xAxis.max"
            label="Máximo"
            outlined
            dense
            @change="setData({ path: 'xAxis.max', value: $event || null })"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            :value="xAxis.splitNumber"
            label="Número de divisões"
            outlined
            dense
            @change="setData({ path: 'xAxis.splitNumber', value: $event || null })"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-slider
        :value="xAxis.nameTextStyle.fontSize"
        label="Tamanho da fonte"
        step="1"
        max="30"
        min="5"
        thumb-label
        ticks
        @change="setData({ path: 'xAxis.nameTextStyle.fontSize', value: $event })"
      ></v-slider>
      <v-slider
        :value="xAxis.nameTextStyle.fontWeight"
        label="Grossura da fonte"
        step="100"
        max="900"
        min="100"
        thumb-label
        ticks
        @change="setData({ path: 'xAxis.nameTextStyle.fontWeight', value: $event })"
      ></v-slider>
      <v-radio-group
        :value="xAxis.nameLocation"
        class="my-0"
        label="Posição"
        row
        @change="setData({ path: 'xAxis.nameLocation', value: $event })"
      >
        <v-radio label="Esquerda" value="start"></v-radio>
        <v-radio label="Centro" value="center"></v-radio>
        <v-radio label="Direita" value="end"></v-radio>
      </v-radio-group>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  computed: {
    ...mapState({
      xAxis: (state) => state.plot.xAxis
    })
  },

  methods: {
    ...mapMutations({
      setData: 'plot/setData'
    })
  }
}
</script>
