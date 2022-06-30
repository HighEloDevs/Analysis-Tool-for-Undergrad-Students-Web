<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :search="search"
    style="border-radius: 0px; background: transparent"
    sort-by="Último acesso"
    color="blue"
    dense
    show-select
  >
    <template v-slot:top>
      <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
          <v-card-title class="text-h6">
            {{ deleteMessage }}
          </v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeDelete">
              Cancel
            </v-btn>
            <v-btn color="blue darken-1" text @click="deleteItemConfirm">
              OK
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-text-field
        class="pa-3"
        label="Procurar projetos"
        prepend-inner-icon="mdi-magnify"
        outlined
        dense
        hide-details
        v-model="search"
      ></v-text-field>
    </template>

    <template v-slot:item.actions="{ item }">
      <v-icon small class="ml-2" @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>

    <template v-slot:no-data>
      {{ emptyMessage }}
    </template>
  </v-data-table>
</template>

<script>
export default {
  props: ['headers', 'items', 'deleteMessage', 'emptyMessage'],
  data: () => ({
    dialog: false,
    dialogDelete: false,
    search: '',
  }),

  watch: {
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },

  methods: {
    deleteItem(item) {
      this.editedIndex = this.items.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm() {
      this.items.splice(this.editedIndex, 1)
      this.closeDelete()
    },

    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
  },
}
</script>
