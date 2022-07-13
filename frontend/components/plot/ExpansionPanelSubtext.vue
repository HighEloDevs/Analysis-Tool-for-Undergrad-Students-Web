<template>
  <v-expansion-panel>
    <v-expansion-panel-header>Subtítulo</v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-slider
        :value="title.subtextStyle.fontSize"
        label="Tamanho da fonte"
        step="1"
        max="30"
        min="5"
        thumb-label
        ticks
        @change="setData({ path: 'title.subtextStyle.fontSize', value: $event })"
      ></v-slider>
      <v-slider
        :value="title.subtextStyle.fontWeight"
        label="Grossura da fonte"
        step="100"
        max="900"
        min="100"
        thumb-label
        ticks
        @change="setData({ path: 'title.subtextStyle.fontWeight', value: $event })"
      ></v-slider>
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
