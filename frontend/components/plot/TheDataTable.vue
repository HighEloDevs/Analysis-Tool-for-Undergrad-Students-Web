<template>
  <div>
    <v-dialog v-model="operationsDialog" max-width="500px" transition="dialog-transition">
      <v-card>
        <v-card-title>
          <span class="headline">Operações</span>
        </v-card-title>
        <v-card-text>
          <v-combobox
            label="Operação"
            v-model="operation"
            :items="operations"
            outlined
            dense
          ></v-combobox>
          <v-row>
            <v-col :cols="operation.value === 'switch' ? 6 : 12">
              <v-combobox
                label="Coluna"
                v-model="columns2Switch[0]"
                :items="headers"
                outlined
                dense
                hide-details
              ></v-combobox>
            </v-col>
            <v-col v-show="operation.value === 'switch'">
              <v-combobox
                label="Coluna"
                v-model="columns2Switch[1]"
                :items="headers"
                outlined
                dense
              ></v-combobox>
            </v-col>
            <v-col v-show="operation.value !== 'switch'" cols="12">
              <v-text-field
                label="Valor"
                v-model="operationValue"
                outlined
                dense
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text @click="operationsDialog = false"> Cancelar </v-btn>
          <v-btn color="primary" text @click="applyOperation"> Aplicar </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-data-table
      :headers="headers"
      :items="items"
      :search="search"
      hide-default-footer
      no-data-text="Nenhum dado encontrado"
      no-results-text="Nenhum dado encontrado"
    >
      <template #top>
        <v-toolbar color="transparent" dense flat>
          <v-tooltip bottom>
            <template #activator="{ on, attrs }">
              <v-btn v-on="on" v-bind="attrs" @click="addRow" dense icon>
                <v-icon small>fa-plus</v-icon>
              </v-btn>
            </template>
            Adicionar linha
          </v-tooltip>
          <v-tooltip bottom>
            <template #activator="{ on, attrs }">
              <v-btn v-on="on" v-bind="attrs" @click="operationsDialog = true" dense icon>
                <v-icon small>fa-pen</v-icon>
              </v-btn>
            </template>
            Operações
          </v-tooltip>
          <v-text-field
            v-model="search"
            label="Pesquisar"
            outlined
            hide-details
            dense
          ></v-text-field>
        </v-toolbar>
      </template>
      <template #item.use="props">
        <v-checkbox
          :input-value="props.item.use"
          class="ma-0"
          hide-details
          dense
          @change="changeValue('use', props, $event)"
        ></v-checkbox>
      </template>
      <template #item.x="props">
        <v-edit-dialog :return-value.sync="props.item.x" @save="onSave">
          {{ props.item.x }}
          <template #input>
            <v-text-field
              :value="props.item.x"
              label="Editar"
              single-line
              counter
              @change="changeValue('x', props, $event)"
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
      <template #item.y="props">
        <v-edit-dialog :return-value.sync="props.item.y" @save="onSave">
          {{ props.item.y }}
          <template #input>
            <v-text-field
              :value="props.item.y"
              label="Editar"
              single-line
              counter7
              @change="changeValue('y', props, $event)"
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
      <template #item.sy="props">
        <v-edit-dialog :return-value.sync="props.item.sy" @save="onSave">
          {{ props.item.sy }}
          <template #input>
            <v-text-field
              :value="props.item.sy"
              label="Editar"
              single-line
              counter
              @change="changeValue('sy', props, $event)"
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
      <template #item.sx="props">
        <v-edit-dialog :return-value.sync="props.item.sx" @save="onSave">
          {{ props.item.sx }}
          <template #input>
            <v-text-field
              :value="props.item.sx"
              label="Editar"
              single-line
              counter
              @change="changeValue('sx', props, $event)"
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
      <template #item.actions="item">
        <v-edit-dialog>
          <v-btn icon small>
            <v-icon small color="error">fa-trash</v-icon>
          </v-btn>
          <template #input>
            <v-card flat>
              <v-card-title> Tem certeza? </v-card-title>
              <v-card-text class="d-flex justify-center">
                <v-btn
                  @click="removeRow({ dataIndex: dataIndex, rowIndex: $event.index })"
                  color="error"
                  text
                >
                  Deletar
                </v-btn>
              </v-card-text>
            </v-card>
          </template>
        </v-edit-dialog>
      </template>
      <template #footer="{ props }">
        <v-pagination
          :length="props.pagination.pageCount"
          v-model="props.options.page"
        ></v-pagination>
      </template>
    </v-data-table>

    <v-snackbar v-model="snack" :timeout="3000" :color="snackColor">
      {{ snackText }}

      <template #action="{ attrs }">
        <v-btn v-bind="attrs" text @click="snack = false"> Close </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  props: {
    items: {
      type: Array,
      default: () => []
    },
    dataIndex: {
      type: Number,
      required: true
    }
  },

  model: {
    prop: 'items',
    event: 'updateInput'
  },

  data() {
    return {
      search: '',
      operationsDialog: false,
      operationValue: 0,
      snack: false,
      snackColor: '',
      snackText: '',
      pagination: {},
      operations: [
        {
          text: 'Somar',
          value: 'sum'
        },
        {
          text: 'Subtrair',
          value: 'subtract'
        },
        {
          text: 'Multiplicar',
          value: 'multiply'
        },
        {
          text: 'Dividir',
          value: 'divide'
        },
        {
          text: 'Substituir',
          value: 'replace'
        },
        {
          text: 'Trocar Colunas',
          value: 'switch'
        }
      ],
      headers: [
        { text: '', value: 'use', sortable: false, width: '20px' },
        { text: 'X', value: 'x' },
        { text: 'Y', value: 'y' },
        { text: 'σY', value: 'sy' },
        { text: 'σX', value: 'sx' },
        {
          text: 'Ações',
          value: 'actions',
          sortable: false,
          align: 'right',
          width: '20px'
        }
      ],
      columns2Switch: [
        { text: 'X', value: 'x' },
        { text: 'Y', value: 'y' }
      ],
      operation: {
        text: 'Somar',
        value: 'sum'
      }
    }
  },
  methods: {
    ...mapMutations({
      setData: 'plot/setData',
      removeRow: 'plot/removeRow',
      _addRow: 'plot/addRow'
    }),

    addRow() {
      this._addRow({
        dataIndex: this.dataIndex,
        values: {
          x: 0,
          y: 0,
          sy: 0,
          sx: 0,
          use: true
        }
      })
    },

    deleteRow(item) {
      this.items.splice(item.index, 1)
    },

    updateInput(value) {
      this.$emit('update', value)
    },

    onSave() {
      this.snack = true
      this.snackColor = 'success'
      this.snackText = 'Alteração salva!'
    },

    changeValue(field, props, newValue) {
      let path = `plotData.${this.dataIndex}.data.${props.index}.${field}`
      this.setData({
        path: path,
        value: newValue
      })
    },

    applyOperation() {
      let output = this.items
      if (this.operation.value === 'sum') {
        output.forEach((item) => {
          item[this.columns2Switch[0].value] += this.operationValue
        })
      } else if (this.operation.value === 'subtract') {
        this.items.forEach((item) => {
          this.$set(
            item,
            this.columns2Switch[0].value,
            Number(item[this.columns2Switch[0].value]) - Number(this.operationValue)
          )
        })
      } else if (this.operation.value === 'multiply') {
        this.items.forEach((item) => {
          this.$set(
            item,
            this.columns2Switch[0].value,
            Number(item[this.columns2Switch[0].value]) * Number(this.operationValue)
          )
        })
      } else if (this.operation.value === 'divide' && this.operationValue != 0) {
        this.items.forEach((item) => {
          this.$set(
            item,
            this.columns2Switch[0].value,
            Number(item[this.columns2Switch[0].value]) / Number(this.operationValue)
          )
        })
      } else if (this.operation.value === 'replace') {
        this.items.forEach((item) => {
          this.$set(item, this.columns2Switch[0].value, Number(this.operationValue))
        })
      } else if (this.operation.value === 'switch') {
        this.items.forEach((item) => {
          let aux = item[this.columns2Switch[0].value]
          this.$set(
            item,
            this.columns2Switch[0].value,
            item[this.columns2Switch[1].value]
          )
          this.$set(item, this.columns2Switch[1].value, aux)
        })
      }
    }
  }
}
</script>
