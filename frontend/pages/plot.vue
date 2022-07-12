<template>
  <v-container class="ma-0 pa-0" fill-height fluid>
    <!-- New Plot Dialog -->
    <!-- <v-dialog
      v-model="stepperDialog"
      persistent
      max-width="550px"
      transition="dialog-transition"
    >
      <ThePlotStepper @finishStepper="onFinishStepper" />
    </v-dialog> -->

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
                <v-tab v-for="(_, i) in data" :key="i"> Plot {{ i }} </v-tab>
                <v-tab>
                  <v-icon left small>fa-paintbrush</v-icon>
                  Gráfico
                </v-tab>
              </v-tabs>
            </template>
          </v-toolbar>

          <v-tabs-items v-model="tab">
            <v-tab-item v-for="(d, i) in data" :key="i">
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
                      v-model="deletePlotDialogs[i]"
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
                            <v-btn color="error" text @click="removePlot(i)">
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
                      v-model="d.file"
                      prepend-icon=""
                      class="mt-6"
                      label="Arquivo de dados"
                      hint="Arquivos suportados: .csv, .tsv, .txt, .xlsx"
                      accept=".csv,.txt,.tsv,.xlsx"
                      outlined
                      dense
                      show-size
                      persistent-hint
                      @change="onFileChange(i, d.file)"
                    ></v-file-input>
                    <ThePlotDataTable :items="d.data" />
                  </v-card-text>
                </v-card>
                <v-btn color="secondary" @click="plot"> Ajustar </v-btn>
              </v-container>
            </v-tab-item>

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
                    v-model="title.text"
                    label="Título do gráfico"
                    outlined
                    dense
                    @change="plot"
                  ></v-text-field>
                  <v-text-field
                    v-model="title.subtext"
                    label="Subtítulo"
                    outlined
                    dense
                    @change="plot"
                  ></v-text-field>
                  <v-text-field
                    v-model="xAxis.name"
                    label="Título do eixo X"
                    outlined
                    dense
                    @change="plot"
                  ></v-text-field>
                  <v-text-field
                    v-model="yAxis.name"
                    label="Título do eixo Y"
                    outlined
                    dense
                    @change="plot"
                  ></v-text-field>
                </v-card-text>

                <v-card-title class="pt-0">
                  Configurações Avançadas
                  <v-divider class="ml-3"></v-divider>
                </v-card-title>
                <v-card-text class="py-0">
                  <v-expansion-panels popout flat>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Título</v-expansion-panel-header>
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
                        <v-radio-group
                          v-model="title.left"
                          class="my-0"
                          label="Posição"
                          row
                          @change="plot"
                        >
                          <v-radio label="Esquerda" value="left"></v-radio>
                          <v-radio label="Centro" value="center"></v-radio>
                          <v-radio label="Direita" value="right"></v-radio>
                        </v-radio-group>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Subtítulo</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-slider
                          v-model="title.subtextStyle.fontSize"
                          label="Tamanho da fonte"
                          step="1"
                          max="30"
                          min="5"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                        <v-slider
                          v-model="title.subtextStyle.fontWeight"
                          label="Grossura da fonte"
                          step="100"
                          max="900"
                          min="100"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Eixo X</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col cols="12" md="4">
                            <v-text-field
                              v-model="xAxis.min"
                              label="Mínimo"
                              outlined
                              dense
                              @change="plot"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" md="4">
                            <v-text-field
                              v-model="xAxis.max"
                              label="Máximo"
                              outlined
                              dense
                              @change="plot"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" md="4">
                            <v-text-field
                              v-model="xAxis.splitNumber"
                              label="Número de divisões"
                              outlined
                              dense
                              @change="plot"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-slider
                          v-model="xAxis.nameTextStyle.fontSize"
                          label="Tamanho da fonte"
                          step="1"
                          max="30"
                          min="5"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                        <v-slider
                          v-model="xAxis.nameTextStyle.fontWeight"
                          label="Grossura da fonte"
                          step="100"
                          max="900"
                          min="100"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                        <v-radio-group
                          v-model="xAxis.nameLocation"
                          class="my-0"
                          label="Posição"
                          row
                          @change="plot"
                        >
                          <v-radio label="Esquerda" value="start"></v-radio>
                          <v-radio label="Centro" value="center"></v-radio>
                          <v-radio label="Direita" value="end"></v-radio>
                        </v-radio-group>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Eixo Y</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-row>
                          <v-col cols="12" md="4">
                            <v-text-field
                              v-model="yAxis.min"
                              label="Mínimo"
                              outlined
                              dense
                              @change="plot"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" md="4">
                            <v-text-field
                              v-model="yAxis.max"
                              label="Máximo"
                              outlined
                              dense
                              @change="plot"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" md="4">
                            <v-text-field
                              v-model="yAxis.splitNumber"
                              label="Número de divisões"
                              outlined
                              dense
                              @change="plot"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-slider
                          v-model="yAxis.nameTextStyle.fontSize"
                          label="Tamanho da fonte"
                          step="1"
                          max="30"
                          min="5"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                        <v-slider
                          v-model="yAxis.nameTextStyle.fontWeight"
                          label="Grossura da fonte"
                          step="100"
                          max="900"
                          min="100"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                        <v-radio-group
                          v-model="yAxis.nameLocation"
                          class="my-0"
                          label="Posição"
                          row
                          @change="plot"
                        >
                          <v-radio label="Baixo" value="start"></v-radio>
                          <v-radio label="Centro" value="center"></v-radio>
                          <v-radio label="Cima" value="end"></v-radio>
                        </v-radio-group>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Gráfico</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-subheader class="pl-0"> Direita </v-subheader>
                        <v-slider
                          v-model="grid.right"
                          step="5"
                          max="200"
                          min="5"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                        <v-subheader class="pl-0"> Esquerda </v-subheader>
                        <v-slider
                          v-model="grid.left"
                          step="5"
                          max="200"
                          min="5"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                        <v-subheader class="pl-0"> Cima </v-subheader>
                        <v-slider
                          v-model="grid.top"
                          step="5"
                          max="200"
                          min="5"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                        <v-subheader class="pl-0"> Baixo </v-subheader>
                        <v-slider
                          v-model="grid.bottom"
                          step="5"
                          max="200"
                          min="5"
                          thumb-label
                          ticks
                          @change="plot"
                        ></v-slider>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </v-card-text>
              </v-card>
            </v-tab-item>
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

export default {
  name: 'PlotPage',
  data() {
    return {
      tab: null,
      fitDataDialogs: [],
      deletePlotDialogs: [],
      data: [
        {
          fitFunction: '',
          file: null,
          params: [],
          data: [],
          options: {
            fitRange: [0, 1],
            useSx: true,
            useSy: true,
            fit: true,
            connectDots: false
          },
          // This is the data returned from backend
          fitData: {
            params: [],
            corrMatrix: [
              [1, 0],
              [0, 1]
            ],
            covMatrix: [
              [1, 0],
              [0, 1]
            ],
            chi2: 0,
            sumRes: 0,
            ngl: 0
          }
        }
      ],
      stepperDialog: false,
      chart: null,
      projectData: {
        title: 'Título do projeto',
        subtitle: 'Subtitulo'
      },
      xAxis: {
        type: 'value',
        nameLocation: 'middle',
        minorTick: {
          show: true
        },
        minorSplitLine: {
          show: true
        },
        nameTextStyle: {
          fontSize: 12,
          fontWeight: '400'
        }
      },
      yAxis: {
        type: 'value',
        nameLocation: 'middle',
        minorTick: {
          show: true
        },
        minorSplitLine: {
          show: true
        },
        nameTextStyle: {
          fontSize: 12,
          fontWeight: '400'
        }
      },
      title: {
        left: 'center',
        top: 10,
        textStyle: {
          fontSize: 20,
          fontWeight: '400'
        },
        subtextStyle: {
          fontSize: 14,
          fontWeight: '400'
        }
      },
      tooltip: {
        axisPointer: { type: 'cross' }
      },
      grid: {
        left: '80',
        right: '80',
        top: '80',
        bottom: '80'
      }
    }
  },
  methods: {
    /**
     * Convert and ndarray to a LaTeX matrix
     * @param {Array} arr
     */
    arr2matrix(arr) {
      let output = []
      arr.forEach((row) => {
        output.push(row.join(' & '))
      })
      return '\\begin{bmatrix} ' + output.join(' \\\\ ') + ' \\end{bmatrix}'
    },

    /**
     * Triggered when the New Plot Stepper is finished
     * @param {Object} data The data from the stepper
     */
    onFinishStepper(data) {
      this.stepperDialog = false
      let arr = this.loadData(data.file)
      this.addPlot()
      this.data[this.data.length - 1]['data'] = arr
      this.data[this.data.length - 1]['params'] = data.params
      this.data[this.data.length - 1]['fitFunction'] = data.fitFunction
      this.data[this.data.length - 1]['file'] = data.file
      this.fit(-1)
    },

    /**
     * Triggered when the fit function changes
     * @param {Integer} projectId The project id
     * @param {String} newValue
     */
    onFitFunctionChange(plotIndex, newValue) {
      // Calls backend to parse the function
      this.fit(plotIndex)
    },

    onFileChange(plotIndex, newValue) {
      if (newValue === null) {
        this.data[plotIndex]['data'] = []
        this.plot()
      } else {
        this.loadData(plotIndex, newValue)
      }
    },

    /**
     * Fits the function to data
     * @param {Integer} plotIndex The index of the plot
     */
    fit(plotIndex) {
      // Calls backend to fit the data
      let data = this.data[plotIndex]
      this.$axios
        .post('/api/fit', data)
        .then((response) => {
          // Update the data
          this.data[plotIndex].fitData = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },

    /**
     * Reads the file from any format and returns a array
     * @param {File} file
     */
    loadData(plotIndex, file) {
      // Calls backend to load the data
      let fr = new FileReader()
      fr.onload = (e) => {
        let data = e.target.result
        let type = file.name.split('.').pop()
        this.$axios
          .post('/parsers/simple_parser', {
            data: data,
            type: type
          })
          .then((res) => {
            let output = []
            res.data.forEach((row) => {
              output.push({
                x: String(row[0]),
                y: String(row[1]),
                sy: String(row[2]) || '',
                sx: String(row[3]) || '',
                use: true
              })
              this.data[plotIndex]['data'] = output
            })
            this.plot()
          })
          .catch((err) => {
            console.log(err)
          })
      }
      fr.readAsText(file)
    },

    /**
     * Adds a new empty plot to the data
     */
    addPlot() {
      this.data.push({
        fitFunction: '',
        file: null,
        params: [],
        data: [],
        options: {
          fitRange: [0, 1],
          useSx: true,
          useSy: true,
          fit: true,
          connectDots: false
        },
        // This is the data returned from backend
        fitData: {
          params: [],
          corrMatrix: [
            [1, 0],
            [0, 1]
          ],
          covMatrix: [
            [1, 0],
            [0, 1]
          ],
          chi2: 0,
          sumRes: 0,
          ngl: 0
        }
      })
    },

    /**
     * Removes a plot from the data
     * @param {Integer} plotIndex The index of the plot
     */
    removePlot(plotIndex) {
      this.deletePlotDialogs[plotIndex] = false
      this.data.splice(plotIndex, 1)
      if (this.data.length === 0) {
        this.addPlot()
      }
    },

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
  },

  computed: {
    series() {
      return this.data.map((d, i) => {
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
      return this.data.map((d) => {
        return {
          source: d.data
        }
      })
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
  }
}
</script>

<style scoped>
/* Importing KateX library */
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
