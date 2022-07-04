<template>
  <div>
    <v-data-table :headers="headers" :items="items" dense>
      <template v-slot:item.x="props">
        <v-edit-dialog
          :return-value.sync="props.item.x"
          @save="save"
          @cancel="cancel"
          @open="open"
        >
          {{ props.item.x }}
          <template v-slot:input>
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
      <template v-slot:item.y="props">
        <v-edit-dialog
          :return-value.sync="props.item.y"
          @save="save"
          @cancel="cancel"
          @open="open"
        >
          {{ props.item.y }}
          <template v-slot:input>
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
      <template v-slot:item.sy="props">
        <v-edit-dialog
          :return-value.sync="props.item.sy"
          @save="save"
          @cancel="cancel"
          @open="open"
        >
          {{ props.item.sy }}
          <template v-slot:input>
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
      <template v-slot:item.sx="props">
        <v-edit-dialog
          :return-value.sync="props.item.sx"
          @save="save"
          @cancel="cancel"
          @open="open"
        >
          {{ props.item.sx }}
          <template v-slot:input>
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

      <template v-slot:action="{ attrs }">
        <v-btn v-bind="attrs" text @click="snack = false"> Close </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  props: ['items'],
  model: {
    prop: 'items',
    event: 'updateInput',
  },
  data() {
    return {
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
