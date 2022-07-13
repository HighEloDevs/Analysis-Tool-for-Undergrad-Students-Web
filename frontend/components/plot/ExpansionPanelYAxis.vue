<template>
  <v-expansion-panel>
    <v-expansion-panel-header>Eixo Y</v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-row>
        <v-col cols="12" md="4">
          <v-text-field
            :value="yAxis.min"
            label="Mínimo"
            outlined
            dense
            @change="setData({ path: 'yAxis.min', value: $event })"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            :value="yAxis.max"
            label="Máximo"
            outlined
            dense
            @change="setData({ path: 'yAxis.max', value: $event })"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            :value="yAxis.splitNumber"
            label="Número de divisões"
            outlined
            dense
            @change="setData({ path: 'yAxis.splitNumber', value: $event })"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-slider
        :value="yAxis.nameTextStyle.fontSize"
        label="Tamanho da fonte"
        step="1"
        max="30"
        min="5"
        thumb-label
        ticks
        @change="setData({ path: 'yAxis.nameTextStyle.fontSize', value: $event })"
      ></v-slider>
      <v-slider
        :value="yAxis.nameTextStyle.fontWeight"
        label="Grossura da fonte"
        step="100"
        max="900"
        min="100"
        thumb-label
        ticks
        @change="setData({ path: 'yAxis.nameTextStyle.fontWeight', value: $event })"
      ></v-slider>
      <v-radio-group
        :value="yAxis.nameLocation"
        class="my-0"
        label="Posição"
        row
        @change="setData({ path: 'yAxis.nameLocation', value: $event })"
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
      yAxis: (state) => state.plot.yAxis
    })
  },

  methods: {
    ...mapMutations({
      setData: 'plot/setData'
    })
  }
}
</script>
