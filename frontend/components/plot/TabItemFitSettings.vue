<template>
  <v-tab-item>
    <v-dialog v-model="deletePlotDialog" max-width="500px" style="z-index: 2001">
      <v-card flat>
        <v-card-title>
          <span> Deseja realmente remover o plot? </span>
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="deletePlotDialog = false"> Cancelar </v-btn>
          <v-btn
            color="error"
            text
            @click="
              deletePlotDialog = false
              removePlot(index)
            "
          >
            Remover
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="fitDataDialog" max-width="400px" style="z-index: 2001">
      <v-card flat>
        <v-card-title> Configurações extras do ajuste </v-card-title>
        <v-card-text>
          <header>Limites do ajuste no eixo <strong>x</strong></header>
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field
                :value="data.options.fitRange[0]"
                hint="Ajuste de ..."
                persistent-hint
                single-line
                outlined
                dense
                @change="
                  setData({ path: `plotData.${index}.options.fitRange.0`, value: $event })
                "
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                :value="data.options.fitRange[1]"
                hint="Ajuste até ..."
                persistent-hint
                single-line
                outlined
                dense
                @change="
                  setData({ path: `plotData.${index}.options.fitRange.1`, value: $event })
                "
              ></v-text-field>
            </v-col>
          </v-row>

          <header class="mt-2">Incertezas</header>
          <v-row>
            <v-col cols="12" md="6">
              <v-checkbox
                :value="data.options.useSx"
                class="ma-0"
                hide-details
                @change="
                  setData({ path: `plotData.${index}.options.useSx`, value: $event })
                "
              >
                <template #label>
                  <span> Considerar em <strong>x</strong> </span>
                </template>
              </v-checkbox>
            </v-col>
            <v-col cols="12" md="6">
              <v-checkbox
                :value="data.options.useSy"
                class="ma-0"
                hide-details
                @change="
                  setData({ path: `plotData.${index}.options.useSy`, value: $event })
                "
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
                :value="data.options.fit"
                class="ma-0"
                hide-details
                @change="
                  setData({ path: `plotData.${index}.options.fit`, value: $event })
                "
              >
                <template #label>
                  <span> Ajustar função </span>
                </template>
              </v-checkbox>
            </v-col>
            <v-col cols="12" md="6">
              <v-checkbox
                :value="data.options.connectDots"
                class="ma-0"
                hide-details
                @change="
                  setData({
                    path: `plotData.${index}.options.connectDots`,
                    value: $event
                  })
                "
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

    <v-container fluid>
      <v-card flat>
        <v-card-title>
          <span>Configurações do ajuste</span>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="fitDataDialog = true">
            <v-icon small left> fa-sliders </v-icon>
            Configurações
          </v-btn>
          <v-btn color="error" icon @click="deletePlotDialog = true">
            <v-icon small>fa-trash</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text class="px-6">
          <v-text-field
            :value="data.fitFunction"
            label="Função de ajuste"
            hint="Função que será ajustada"
            prefix="f(x) = "
            outlined
            dense
            @change="setData({ path: `plotData.${index}.fitFunction`, value: $event })"
          ></v-text-field>

          <header v-show="!!data.params.length">Valores iniciais dos parâmetros</header>

          <v-row>
            <v-col v-for="param in data.params" :key="param.name" cols="12" md="6">
              <v-text-field
                :prefix="param.name + ' = '"
                :value="param.value"
                hide-details
                outlined
                dense
              ></v-text-field>
            </v-col>
          </v-row>
          <v-divider class="mt-4 mb-2"></v-divider>
          <PlotTheFitParamsDataTable :data="fitData2Display" />

          <!-- Matrices -->
          <v-row class="mt-4 align-start">
            <v-col
              lg="6"
              cols="12"
              class="d-flex flex-column justify-center align-center"
            >
              <span class="font-weight-bold subtitle-1 text-center">
                Matriz de covariância
              </span>
              <BaseMatrixDisplay :matrix="data.fitData.covMatrix" />
            </v-col>
            <v-col
              lg="6"
              cols="12"
              class="d-flex flex-column justify-center align-center text-center"
            >
              <span class="font-weight-bold subtitle-1"> Matriz de correlação </span>
              <BaseMatrixDisplay :matrix="data.fitData.corrMatrix" />
            </v-col>
          </v-row>

          <!-- Data -->
          <v-divider class="my-6"></v-divider>
          <v-file-input
            :value="data.file"
            prepend-icon=""
            label="Arquivo de dados"
            hint="Arquivos suportados: .csv, .tsv, .txt, .xlsx"
            accept=".csv,.txt,.tsv,.xlsx"
            outlined
            dense
            show-size
            persistent-hint
            @change="onFileChange(index, $event)"
          ></v-file-input>
          <PlotTheDataTable :items="data.data" />
        </v-card-text>
      </v-card>
    </v-container>
  </v-tab-item>
</template>

<script>
import { mapMutations, mapState } from 'vuex'

export default {
  props: {
    index: {
      type: Number,
      required: true
    }
  },

  data() {
    return {
      fitDataDialog: false,
      deletePlotDialog: false
    }
  },

  computed: {
    ...mapState({
      plotData: (state) => state.plot.plotData
    }),

    data() {
      return this.plotData[this.index]
    },

    fitData2Display() {
      return this.data.fitData.params.concat([
        { name: 'Graus de Liberdade', value: this.data.fitData.ngl },
        {
          name: this.data.fitData.chi2 ? 'χ²' : 'Soma dos resíduos',
          value: this.data.fitData.chi2 || this.data.fitData.sumRes
        }
      ])
    }
  },

  methods: {
    ...mapMutations({
      setData: 'plot/setData',
      removePlot: 'plot/removePlot'
    }),

    async onFileChange(plotIndex, file) {
      let data = []
      this.setData({
        path: `plotData.${plotIndex}.file`,
        value: file
      })
      if (file !== null) {
        data = await this.loadData(file)
      }
      this.setData({
        path: `plotData.${plotIndex}.data`,
        value: data
      })
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
    }
  }
}
</script>
