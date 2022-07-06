<template>
  <v-container
    class="ma-0 pa-0"
    fill-height
    fluid
  >
    <!-- App Bar -->
    <v-app-bar
      color="primary"
      app
      dense
    >
      <v-tooltip right>
        <template #activator="{ on, attrs }">
          <v-btn
            v-on="on"
            v-bind="attrs"
            to="/"
            icon
          >
            <v-icon
              class="white--text"
              small
              >fa-chevron-left</v-icon
            >
          </v-btn>
        </template>
        Voltar
      </v-tooltip>
      <v-spacer></v-spacer>
      <div class="d-flex flex-column text-center white--text">
        <span>{{ projectData.title }}</span>
        <span class="caption grey--text text--lighten-2">
          {{ projectData.subtitle }}
        </span>
      </div>
      <v-icon
        class="ml-3 white--text"
        small
        >fa-edit</v-icon
      >
      <v-spacer></v-spacer>
    </v-app-bar>

    <!-- New Plot Dialog -->
    <v-dialog
      v-model="stepperDialog"
      persistent
      max-width="550px"
      transition="dialog-transition"
    >
      <NewPlotStepper @finishStepper="onFinishStepper" />
    </v-dialog>

    <!-- Body -->
    <v-container
      class="ma-0 pa-0 align-stretch"
      fill-height
      fluid
    >
      <v-row class="ma-0">
        <!-- Left Panel -->
        <v-col
          cols="12"
          md="6"
          class="ma-0 pa-0"
        >
          <v-tabs :vertical="$vuetify.breakpoint.mdAndUp">
            <!-- Tabs -->
            <div
              class="d-flex flex-md-column"
              style="width: 100%; height: 100%"
            >
              <v-tab
                v-for="(_, i) in data"
                :key="i"
              >
                Plot {{ i }}
              </v-tab>
              <v-tooltip
                right
                :bottom="!$vuetify.breakpoint.mdAndUp"
              >
                <template #activator="{ on, attrs }">
                  <v-btn
                    v-on="on"
                    v-bind="attrs"
                    class="elevation-0 flex-grow-1"
                    style="height: auto"
                    color="transparent"
                    @click="addPlot"
                    tile
                  >
                    <v-icon
                      class="primary--text"
                      v-show="data.length"
                      dense
                    >
                      fa-plus
                    </v-icon>
                  </v-btn>
                </template>
                Adicionar um Plot
              </v-tooltip>
            </div>

            <!-- Tab Content -->
            <v-tab-item
              v-for="(d, i) in data"
              :key="i"
              style="height: calc(100vh - 48px)"
              class="overflow-y-auto"
            >
              <v-card flat>
                <v-card-title>
                  <span>Configurações do ajuste</span>
                  <v-spacer></v-spacer>
                  <v-tooltip bottom>
                    <template #activator="{ on, attrs }">
                      <v-btn
                        v-on="on"
                        v-bind="attrs"
                        icon
                      >
                        <v-icon small>fa-square-poll-vertical</v-icon>
                      </v-btn>
                    </template>
                    Dados do ajuste
                  </v-tooltip>
                  <v-tooltip bottom>
                    <template #activator="{ on, attrs }">
                      <v-btn
                        v-on="on"
                        v-bind="attrs"
                        color="error"
                        icon
                      >
                        <v-icon small>fa-trash</v-icon>
                      </v-btn>
                    </template>
                    Excluir esses dados
                  </v-tooltip>
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

                  <header v-show="d.params.length">
                    Valores iniciais dos parâmetros
                  </header>
                  <v-row>
                    <v-col
                      v-for="param in d.params"
                      :key="param.name"
                      cols="12"
                      md="6"
                    >
                      <v-text-field
                        :prefix="param.name + ' = '"
                        v-model="param.value"
                        hide-details
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>

                  <header class="mt-6">
                    Limites do ajuste no eixo <strong>x</strong>
                  </header>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="6"
                    >
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
                    <v-col
                      cols="12"
                      sm="6"
                    >
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

                  <header class="mt-6">Incertezas</header>
                  <v-row>
                    <v-col
                      cols="12"
                      md="6"
                    >
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
                    <v-col
                      cols="12"
                      md="6"
                    >
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
                    <v-col
                      cols="12"
                      md="6"
                    >
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
                    <v-col
                      cols="12"
                      md="6"
                    >
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

                  <!-- <v-card class="mt-6" flat>
                    <v-card-title class="pa-0"> Dados do ajuste </v-card-title>
                    <v-card-text class="py-4 px-0">
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
                            <tr
                              v-for="param in d.fitData.params"
                              :key="param.name"
                            >
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
                          </tbody>
                        </template>
                      </v-simple-table>

                      <v-row class="mt-4 align-start">
                        <v-col
                          cols="6"
                          class="d-flex flex-column justify-center align-center text-center"
                        >
                          <span class="font-weight-bold subtitle-1">NGL</span>
                          <span>{{ d.fitData.ngl }}</span>
                        </v-col>
                        <v-col
                          cols="6"
                          class="d-flex flex-column justify-center align-center"
                        >
                          <span
                            v-if="d.fitData.chi2 !== null"
                            class="font-weight-bold subtitle-1"
                          >
                            𝜒²
                          </span>
                          <span
                            v-if="d.fitData.chi2 !== null"
                            class="subtitle-2"
                          >
                            {{ d.fitData.chi2 }}
                          </span>
                          <span
                            v-if="d.fitData.chi2 === null"
                            class="font-weight-bold subtitle-1 text-center"
                          >
                            Somatória dos resíduos absolutos
                          </span>

                          <span
                            v-if="d.fitData.chi2 === null"
                            class="subtitle-2"
                          >
                            {{ d.fitData.sumRes }}
                          </span>
                        </v-col>
                        <v-col
                          lg="6"
                          cols="12"
                          class="d-flex flex-column justify-center align-center"
                        >
                          <span class="font-weight-bold subtitle-1 text-center">
                            Matriz de covariância
                          </span>
                          <div
                            class="mt-2"
                            style="font-size: 20px"
                            v-katex="arr2matrix(d.fitData.covMatrix)"
                          ></div>
                        </v-col>
                        <v-col
                          lg="6"
                          cols="12"
                          class="d-flex flex-column justify-center align-center text-center"
                        >
                          <span class="font-weight-bold subtitle-1"
                            >Matriz de correlação</span
                          >
                          <div
                            class="mt-2"
                            style="font-size: 20px"
                            v-katex="arr2matrix(d.fitData.corrMatrix)"
                          ></div>
                        </v-col>
                      </v-row>
                    </v-card-text>
                  </v-card> -->

                  <!-- Data -->
                  <v-file-input
                    v-model="d.file"
                    class="mt-7"
                    label="Arquivo de dados"
                    @change="onFileChange(i, d.file)"
                    outlined
                    dense
                  ></v-file-input>
                  <DataTableEditable :items="d.data" />
                  <!-- <v-card class="mt-5" flat>
                    <v-card-title class="pa-0">
                      Dados a serem ajustados
                    </v-card-title>
                    <v-card-text class="">
                    </v-card-text>
                  </v-card> -->
                </v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs>
        </v-col>

        <!-- Canvas -->
        <v-col
          class="pa-0"
          cols="12"
          md="6"
        >
          <v-card
            height="100%"
            color="gold"
            min-height="500px"
            flat
          >
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: 'PlotPage',
  data() {
    return {
      data: [],
      projectData: {
        title: 'Título do projeto',
        subtitle: 'Subtitulo'
      },
      stepperDialog: true
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
      } else {
        this.data[plotIndex]['data'] = this.loadData(newValue)
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
    loadData(file) {
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
            return res.data
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
          corrMatrix: [],
          covMatrix: [],
          chi2: 0,
          sumRes: 0,
          ngl: 0
        }
      })
    }
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
</style>
