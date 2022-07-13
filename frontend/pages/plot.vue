<template>
  <v-container class="ma-0 pa-0 d-flex" fill-height fluid>
    <v-row class="align-self-stretch" no-gutters>
      <v-col cols="12" md="5" class="elevation-10">
        <v-toolbar color="primary" flat dense>
          <v-btn icon to="/">
            <v-icon class="white--text" small> fa-chevron-left </v-icon>
          </v-btn>
          <v-toolbar-title class="white--text">{{ projectData.title }}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn class="white--text" text @click="addPlot">
            <v-icon class="white--text" left>fa-plus</v-icon>
            <span> Adicionar Plot </span>
          </v-btn>
          <template v-slot:extension>
            <v-tabs
              v-model="tab"
              background-color="primary"
              dark
              grow
              centered
              show-arrows
              center-active
            >
              <v-tab v-for="(_, i) in plotData" :key="i"> Plot {{ i }} </v-tab>
              <v-tab>
                <v-icon left small>fa-paintbrush</v-icon>
                Gráfico
              </v-tab>
            </v-tabs>
          </template>
        </v-toolbar>
        <v-tabs-items v-model="tab">
          <PlotTabItemFitSettings
            v-for="(_, index) in plotData"
            :key="index"
            :index="index"
          />
          <PlotTabItemCanvasSettings />
        </v-tabs-items>
      </v-col>
      <v-col class="pa-0" cols="12" md="7">
        <div ref="canvas" class="canvas"></div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import * as echarts from 'echarts'
import { mapMutations, mapState } from 'vuex'

export default {
  name: 'PlotPage',

  data() {
    return {
      tab: null,
      chart: null,
      fitDataDialogs: []
    }
  },

  computed: {
    ...mapState({
      plotData: (state) => state.plot.plotData,
      projectData: (state) => state.plot.projectData,
      xAxis: (state) => state.plot.xAxis,
      yAxis: (state) => state.plot.yAxis,
      title: (state) => state.plot.title,
      grid: (state) => state.plot.grid,
      tooltip: (state) => state.plot.tooltip
    }),

    series() {
      return this.plotData.map((d, i) => {
        return {
          type: 'scatter',
          datasetIndex: i,
          colorBy: 'data',
          itemStyle: {
            color: this.getRandomColor()
          }
        }
      })
    },

    dataset() {
      return this.plotData.map((d) => {
        return {
          source: d.data
        }
      })
    }
  },

  watch: {
    // plotData: {
    //   handler() {
    //     this.plot()
    //   },
    //   deep: true
    // },
    xAxis: {
      handler() {
        this.plot()
      },
      deep: true
    },
    yAxis: {
      handler() {
        this.plot()
      },
      deep: true
    },
    title: {
      handler() {
        this.plot()
      },
      deep: true
    },
    grid: {
      handler() {
        this.plot()
      },
      deep: true
    }
  },

  mounted() {
    let chart = echarts.init(
      this.$refs.canvas,
      this.$vuetify.theme.dark ? 'dark' : 'light',
      { renderer: 'svg' }
    )
    window.addEventListener('resize', () => {
      chart.resize()
    })
    setTimeout(() => {
      chart.resize()
    }, 200)
    this.chart = chart
    this.plot()
  },

  methods: {
    ...mapMutations({
      setData: 'plot/setData',
      addPlot: 'plot/addPlot',
      removePlot: 'plot/removePlot'
    }),

    getRandomColor() {
      var letters = '0123456789ABCDEF'
      var color = '#'
      for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)]
      }
      return color
    },

    plot() {
      this.chart.setOption({
        dataset: this.dataset,
        tooltip: this.tooltip,
        xAxis: this.xAxis,
        yAxis: this.yAxis,
        series: this.series,
        title: this.title,
        grid: this.grid
      })
    }
  }
}
</script>

<style scoped>
.canvas {
  width: 100%;
  height: 100%;
  min-height: 500px;
}
</style>
