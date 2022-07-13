<template>
  <v-tab-item>
    <v-card
      fluid
      style="height: calc(100vh - 96px)"
      class="overflow-y-auto d-flex flex-column pa-3"
    >
      <v-card-title>
        Configurações do Rápidas
        <v-divider class="ml-3"></v-divider>
      </v-card-title>
      <v-card-text class="py-0">
        <v-text-field
          :value="title.text"
          label="Título do gráfico"
          outlined
          dense
          @change="setData({ path: 'title.text', value: $event })"
        ></v-text-field>
        <v-text-field
          :value="title.subtext"
          label="Subtítulo"
          outlined
          dense
          @change="setData({ path: 'title.subtext', value: $event })"
        ></v-text-field>
        <v-text-field
          :value="xAxis.name"
          label="Título do eixo X"
          outlined
          dense
          @change="setData({ path: 'xAxis.name', value: $event })"
        ></v-text-field>
        <v-text-field
          :value="yAxis.name"
          label="Título do eixo Y"
          outlined
          dense
          @change="setData({ path: 'yAxis.name', value: $event })"
        ></v-text-field>
      </v-card-text>

      <v-card-title class="pt-0">
        Configurações Avançadas
        <v-divider class="ml-3"></v-divider>
      </v-card-title>
      <v-card-text class="py-0">
        <v-expansion-panels popout flat>
          <PlotExpansionPanelTitle />
          <PlotExpansionPanelSubtext />
          <PlotExpansionPanelXAxis />
          <PlotExpansionPanelYAxis />
          <PlotExpansionPanelCanvas />
        </v-expansion-panels>
      </v-card-text>
    </v-card>
  </v-tab-item>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  computed: {
    ...mapState({
      yAxis: (state) => state.plot.yAxis,
      xAxis: (state) => state.plot.xAxis,
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
