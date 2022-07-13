<template>
  <v-container class="ma-0 pa-0" fill-height fluid>
    <!-- Body -->
    <v-container class="ma-0 pa-0 d-flex" fill-height fluid>
      <v-row class="align-self-stretch" no-gutters>
        <!-- Left Panel -->
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
            <v-tab-item v-for="(d, i) in plotData" :key="i">
              <v-container
                fluid
                style="height: calc(100vh - 96px)"
                class="d-flex flex-column"
              >
                <v-card flat class="overflow-y-auto flex-grow-1">
                  <v-card-title>
                    <span>Configurações do ajuste</span>
                    <v-spacer></v-spacer>
                    <v-dialog
                      v-model="fitDataDialogs[i]"
                      max-width="400px"
                      transition="dialog-transition"
                      style="z-index: 2001"
                    >
                      <template #activator="{ on, attrs }">
                        <v-btn v-on="on" v-bind="attrs" text color="primary">
                          <v-icon small left> fa-sliders </v-icon>
                          Configurações
                        </v-btn>
                      </template>

                      <v-card flat>
                        <v-card-title> Configurações extras do ajuste </v-card-title>
                        <v-card-text>
                          <header>Limites do ajuste no eixo <strong>x</strong></header>
                          <v-row>
                            <v-col cols="12" sm="6">
                              <v-text-field
                                v-model="d.options.fitRange[0]"
                                class="removeArrows"
                                type="number"
                                hint="Ajuste de ..."
                                persistent-hint
                                single-line
                                outlined
                                dense
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6">
                              <v-text-field
                                v-model="d.options.fitRange[1]"
                                class="removeArrows"
                                type="number"
                                hint="Ajuste até ..."
                                persistent-hint
                                single-line
                                outlined
                                dense
                              ></v-text-field>
                            </v-col>
                          </v-row>

                          <header class="mt-2">Incertezas</header>
                          <v-row>
                            <v-col cols="12" md="6">
                              <v-checkbox
                                v-model="d.options.useSx"
                                class="ma-0"
                                hide-details
                              >
                                <template #label>
                                  <span> Considerar em <strong>x</strong> </span>
                                </template>
                              </v-checkbox>
                            </v-col>
                            <v-col cols="12" md="6">
                              <v-checkbox
                                v-model="d.options.useSy"
                                class="ma-0"
                                hide-details
                              >
                                <template #label>
                                  <span> Considerar em <strong>y</strong> </span>
                                </template>
                              </v-checkbox>
                            </v-col>
                          </v-row>

                          <v-row>
                            <v-col cols="12" md="6">
                              <v-checkbox
                                v-model="d.options.fit"
                                class="ma-0"
                                hide-details
                              >
                                <template #label>
                                  <span> Ajustar função </span>
                                </template>
                              </v-checkbox>
                            </v-col>
                            <v-col cols="12" md="6">
                              <v-checkbox
                                v-model="d.options.connectDots"
                                class="ma-0"
                                hide-details
                              >
                                <template #label>
                                  <span> Ligar pontos </span>
                                </template>
                              </v-checkbox>
                            </v-col>
                          </v-row>
                        </v-card-text>
                      </v-card>
                    </v-dialog>
                    <v-dialog
                      max-width="500px"
                      transition="dialog-transition"
                      style="z-index: 2001"
                    >
                      <template #activator="{ on, attrs }">
                        <v-btn v-on="on" v-bind="attrs" color="error" icon>
                          <v-icon small>fa-trash</v-icon>
                        </v-btn>
                      </template>

                      <template #default="dialog">
                        <v-card flat>
                          <v-card-title>
                            <span> Deseja realmente remover o plot? </span>
                          </v-card-title>
                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="primary" text @click="dialog.value = false">
                              Cancelar
                            </v-btn>
                            <v-btn
                              color="error"
                              text
                              @click="
                                dialog.value = false
                                removePlot(i)
                              "
                            >
                              Remover
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </template>
                    </v-dialog>
                  </v-card-title>
                  <v-card-text class="px-6">
                    <v-text-field
                      @change="onFitFunctionChange(i, d.fitFunction)"
                      v-model="d.fitFunction"
                      label="Função de ajuste"
                      hint="Função que será ajustada"
                      prefix="f(x) = "
                      outlined
                      dense
                    ></v-text-field>

                    <header v-show="!!d.params.length">
                      Valores iniciais dos parâmetros
                    </header>

                    <v-row>
                      <v-col v-for="param in d.params" :key="param.name" cols="12" md="6">
                        <v-text-field
                          :prefix="param.name + ' = '"
                          v-model="param.value"
                          hide-details
                          outlined
                          dense
                        ></v-text-field>
                      </v-col>
                    </v-row>

                    <v-divider class="mt-4 mb-2"></v-divider>

                    <v-simple-table dense>
                      <template v-slot:default>
                        <thead>
                          <tr>
                            <th class="text-left">Parâmetro</th>
                            <th class="text-left">Valor</th>
                            <th class="text-left">Incerteza</th>
                            <th class="text-right">Ações</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="param in d.fitData.params" :key="param.name">
                            <td>{{ param.name }}</td>
                            <td>{{ param.value }}</td>
                            <td>{{ param.sigma }}</td>
                            <td class="d-flex justify-end">
                              <v-tooltip bottom>
                                <template #activator="{ on, attrs }">
                                  <v-btn v-on="on" v-bind="attrs" icon small>
                                    <v-icon small>fa-copy</v-icon>
                                  </v-btn>
                                </template>
                                Copiar
                              </v-tooltip>
                            </td>
                          </tr>
                          <tr>
                            <td>Graus de liberdade</td>
                            <td>{{ d.fitData.ngl }}</td>
                            <td></td>
                            <td class="d-flex justify-end">
                              <v-tooltip bottom>
                                <template #activator="{ on, attrs }">
                                  <v-btn v-on="on" v-bind="attrs" icon small>
                                    <v-icon small>fa-copy</v-icon>
                                  </v-btn>
                                </template>
                                Copiar
                              </v-tooltip>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              {{
                                d.fitData.chi2 ? '𝜒²' : 'Somatória dos resíduos absolutos'
                              }}
                            </td>
                            <td>
                              {{ d.fitData.chi2 ? d.fitData.chi2 : d.fitData.sumRes }}
                            </td>
                            <td></td>
                            <td class="d-flex justify-end">
                              <v-tooltip bottom>
                                <template #activator="{ on, attrs }">
                                  <v-btn v-on="on" v-bind="attrs" icon small>
                                    <v-icon small>fa-copy</v-icon>
                                  </v-btn>
                                </template>
                                Copiar
                              </v-tooltip>
                            </td>
                          </tr>
                        </tbody>
                      </template>
                    </v-simple-table>

                    <v-row class="mt-4 align-start">
                      <v-col
                        lg="6"
                        cols="12"
                        class="d-flex flex-column justify-center align-center"
                      >
                        <span class="font-weight-bold subtitle-1 text-center">
                          Matriz de covariância
                        </span>
                        <BaseMatrixDisplay :matrix="d.fitData.covMatrix" />
                      </v-col>
                      <v-col
                        lg="6"
                        cols="12"
                        class="d-flex flex-column justify-center align-center text-center"
                      >
                        <span class="font-weight-bold subtitle-1">
                          Matriz de correlação
                        </span>
                        <BaseMatrixDisplay :matrix="d.fitData.corrMatrix" />
                      </v-col>
                    </v-row>

                    <!-- Data -->
                    <v-divider class="mt-6"></v-divider>
                    <v-file-input
                      prepend-icon=""
                      class="mt-6"
                      label="Arquivo de dados"
                      hint="Arquivos suportados: .csv, .tsv, .txt, .xlsx"
                      accept=".csv,.txt,.tsv,.xlsx"
                      outlined
                      dense
                      show-size
                      persistent-hint
                      @change="onFileChange(i, $event)"
                    ></v-file-input>
                    <PlotTheDataTable :items="d.data" />
                  </v-card-text>
                </v-card>
                <v-btn color="secondary" @click="plot"> Ajustar </v-btn>
              </v-container>
            </v-tab-item>

            <PlotTabItemCanvasSettings />
          </v-tabs-items>
        </v-col>

        <!-- Canvas -->
        <v-col class="pa-0" cols="12" md="7">
          <div ref="canvas" class="canvas"></div>
        </v-col>
      </v-row>
    </v-container>
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

    async onFitFunctionChange(plotIndex, newValue) {},

    async onFileChange(plotIndex, file) {
      let data = []
      if (file !== null) data = await this.loadData(file)
      this.setData({
        path: `plotData.${plotIndex}.data`,
        value: data
      })
      this.plot()
    },

    async loadData(file) {
      let output = []
      let text = await file.text()
      try {
        let res = await this.$axios.post('/parsers/simple_parser', {
          data: text,
          type: file.name.split('.').pop()
        })
        res.data.forEach((row) => {
          output.push({
            x: String(row[0]) || '',
            y: String(row[1]) || '',
            sy: String(row[2]) || '',
            sx: String(row[3]) || '',
            use: true
          })
        })
      } catch (error) {
        console.log(error)
      }
      return output
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
    plotData: {
      handler() {
        this.plot()
      },
      deep: true
    },
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
  }
}
</script>

<style scoped>
@import '../node_modules/katex/dist/katex.min.css';
.removeArrows >>> input[type='number'] {
  -moz-appearance: textfield;
}
.removeArrows >>> input::-webkit-outer-spin-button,
.removeArrows >>> input::-webkit-inner-spin-button {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}
.canvas {
  width: 100%;
  height: 100%;
  min-height: 500px;
}
</style>
