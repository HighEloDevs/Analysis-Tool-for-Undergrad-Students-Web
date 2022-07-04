<template>
  <div>
    <v-dialog
      v-model="operationsDialog"
      max-width="500px"
      transition="dialog-transition"
    >
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
                v-model="columns[0]"
                :items="headers"
                outlined
                dense
                hide-details
              ></v-combobox>
            </v-col>
            <v-col v-show="operation.value === 'switch'">
              <v-combobox
                label="Coluna"
                v-model="columns[1]"
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
          <v-btn color="error" text @click="operationsDialog = false">
            Cancelar
          </v-btn>
          <v-btn color="primary" text @click="applyOperation"> Aplicar </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-data-table :headers="headers" :items="items" dense>
      <template #top>
        <v-toolbar color="transparent" dense flat>
          <v-tooltip bottom>
            <template #activator="{ on, attrs }">
              <v-btn v-on="on" v-bind="attrs" @click="addLine" dense icon>
                <v-icon small>fa-plus</v-icon>
              </v-btn>
            </template>
            Adicionar linha
          </v-tooltip>
          <v-tooltip bottom>
            <template #activator="{ on, attrs }">
              <v-btn
                v-on="on"
                v-bind="attrs"
                @click="operationsDialog = true"
                dense
                icon
              >
                <v-icon small>fa-pen</v-icon>
              </v-btn>
            </template>
            Operações
          </v-tooltip>
        </v-toolbar>
      </template>
      <template #item.x="props">
        <v-edit-dialog
          :return-value.sync="props.item.x"
          @save="save"
          @cancel="cancel"
          @open="open"
        >
          {{ props.item.x }}
          <template #input>
            <v-text-field
              v-model="props.item.x"
              :rules="[max25chars]"
              label="Editar"
              single-line
              counter
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
      <template #item.y="props">
        <v-edit-dialog
          :return-value.sync="props.item.y"
          @save="save"
          @cancel="cancel"
          @open="open"
        >
          {{ props.item.y }}
          <template #input>
            <v-text-field
              v-model="props.item.y"
              :rules="[max25chars]"
              label="Editar"
              single-line
              counter
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
      <template #item.sy="props">
        <v-edit-dialog
          :return-value.sync="props.item.sy"
          @save="save"
          @cancel="cancel"
          @open="open"
        >
          {{ props.item.sy }}
          <template #input>
            <v-text-field
              v-model="props.item.sy"
              :rules="[max25chars]"
              label="Editar"
              single-line
              counter
            ></v-text-field>
          </template>
        </v-edit-dialog>
      </template>
      <template #item.sx="props">
        <v-edit-dialog
          :return-value.sync="props.item.sx"
          @save="save"
          @cancel="cancel"
          @open="open"
        >
          {{ props.item.sx }}
          <template #input>
            <v-text-field
              v-model="props.item.sx"
              :rules="[max25chars]"
              label="Editar"
              single-line
              counter
            ></v-text-field>
          </template>
        </v-edit-dialog>
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
export default {
  props: {
    items: {
      type: Array,
      default: [],
    },
  },
  model: {
    prop: 'items',
    event: 'updateInput',
  },
  data() {
    return {
      operationsDialog: false,
      operation: {
        text: 'Somar',
        value: 'sum',
      },
      operationValue: 0,
      snack: false,
      snackColor: '',
      snackText: '',
      max25chars: (v) => v.length <= 25 || 'Input too long!',
      pagination: {},
      headers: [
        { text: 'X', value: 'x' },
        { text: 'Y', value: 'y' },
        { text: 'σY', value: 'sy' },
        { text: 'σX', value: 'sx' },
      ],
      operations: [
        {
          text: 'Somar',
          value: 'sum',
        },
        {
          text: 'Subtrair',
          value: 'subtract',
        },
        {
          text: 'Multiplicar',
          value: 'multiply',
        },
        {
          text: 'Dividir',
          value: 'divide',
        },
        {
          text: 'Substituir',
          value: 'replace',
        },
        {
          text: 'Trocar Colunas',
          value: 'switch',
        },
      ],
      columns: [
        { text: 'X', value: 'x' },
        { text: 'Y', value: 'y' },
      ],
    }
  },
  methods: {
    updateInput(value) {
      this.$emit('update', value)
    },
    save() {
      this.snack = true
      this.snackColor = 'success'
      this.snackText = 'Data saved'
    },
    cancel() {
      this.snack = true
      this.snackColor = 'error'
      this.snackText = 'Canceled'
    },
    open() {
      this.snack = true
      this.snackColor = 'info'
      this.snackText = 'Dialog opened'
    },
    applyOperation() {
      if (this.operation.value === 'sum') {
        this.items.forEach((item) => {
          this.$set(
            item,
            this.columns[0].value,
            Number(item[this.columns[0].value]) + Number(this.operationValue)
          )
        })
      } else if (this.operation.value === 'subtract') {
        this.items.forEach((item) => {
          this.$set(
            item,
            this.columns[0].value,
            Number(item[this.columns[0].value]) - Number(this.operationValue)
          )
        })
      } else if (this.operation.value === 'multiply') {
        this.items.forEach((item) => {
          this.$set(
            item,
            this.columns[0].value,
            Number(item[this.columns[0].value]) * Number(this.operationValue)
          )
        })
      } else if (
        this.operation.value === 'divide' &&
        this.operationValue != 0
      ) {
        this.items.forEach((item) => {
          this.$set(
            item,
            this.columns[0].value,
            Number(item[this.columns[0].value]) / Number(this.operationValue)
          )
        })
      } else if (this.operation.value === 'replace') {
        this.items.forEach((item) => {
          this.$set(item, this.columns[0].value, Number(this.operationValue))
        })
      } else if (this.operation.value === 'switch') {
        this.items.forEach((item) => {
          let aux = item[this.columns[0].value]
          this.$set(item, this.columns[0].value, item[this.columns[1].value])
          this.$set(item, this.columns[1].value, aux)
        })
      }
    },
    addLine() {
      this.items.unshift({
        x: 0,
        y: 0,
        sy: 0,
        sx: 0,
      })
    },
  },

  watch: {
    items: {
      handler(items) {
        this.updateInput(items)
      },
      deep: true,
    },
  },
}
</script>
