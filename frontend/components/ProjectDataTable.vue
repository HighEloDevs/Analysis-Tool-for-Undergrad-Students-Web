<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :search="search"
    style="border-radius: 0px; background: transparent"
    sort-by="Último acesso"
    color="blue"
    disable-pagination
    hide-default-footer
  >
    <template v-slot:top>
      <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
          <v-card-title class="text-h6">
            Tem certeza que deseja deletar esse projeto?
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
        prepend-inner-icon="fa-magnifying-glass"
        outlined
        dense
        hide-details
        v-model="search"
      ></v-text-field>
    </template>

    <template v-slot:item.title="{ item }">
      <v-list-item two-line dense>
        <v-list-item-avatar>
          <v-btn :href="item.url" icon>
            <v-icon small>fa-up-right-from-square</v-icon>
          </v-btn>
        </v-list-item-avatar>
        <v-list-item-content class="ma-0 pa-0">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
          <v-list-item-subtitle>{{ item.subtitle }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </template>

    <template v-slot:item.actions="{ item }">
      <v-icon small class="ml-2" @click="deleteItem(item)"> fa-delete </v-icon>
    </template>

    <template v-slot:item.folders="{ item }">
      <v-container class="d-flex ma-0 pa-0 align-center" max-width="100px">
        <v-row>
          <v-col xl="6">
            <v-chip
              v-for="folder in item.folders"
              :key="folder"
              :color="getColor(folder)"
              class="font-weight-medium grey--text text--lighten-3"
              small
            >
              {{ folder }}
            </v-chip>
          </v-col>
        </v-row>
      </v-container>
    </template>

    <template v-slot:no-data>
      Clique em 'Novo Projeto' para criar um novo projeto.
    </template>
  </v-data-table>
</template>

<script>
export default {
  props: ['headers', 'items', 'folders', 'deleteMessage', 'emptyMessage'],
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

    getColor(folder) {
      let colors = this.folders.filter((v) => v.text === folder)
      if (!colors.length) return 'grey'
      else {
        return colors[0].color
      }
    },
  },
}
</script>
