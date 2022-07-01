<template>
  <v-container class="ma-0 pa-0">
    <!-- New folder dialog -->
    <v-dialog v-model="newFolderDialog" max-width="300px">
      <v-card>
        <v-card-title>
          <span class="headline">Criar nova pasta</span>
        </v-card-title>
        <v-card-text>
          <v-container class="d-inline align-center justify-center flex-column">
            <v-text-field
              :rules="required"
              v-model="newFolderName"
              label="Nome da pasta"
              maxlength="25"
              required
              counter
            ></v-text-field>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text @click.native="newFolderDialog = false">
            Fechar
          </v-btn>
          <v-btn
            color="primary"
            text
            @click.native="createNewFolder(newFolderName)"
          >
            Salvar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Navigation Drawer -->
    <v-navigation-drawer app permanent clipped width="300px">
      <v-list dense>
        <v-list-item>
          <v-btn color="primary" block rounded elevation-5>Novo Projeto</v-btn>
        </v-list-item>
        <v-list-item @click="selectedFolder = -1" dense>
          <v-list-item-title> Todos os projetos </v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-subheader>Pastas</v-subheader>

        <v-list-item dense @click="newFolderDialog = !newFolderDialog">
          <v-list-item-icon>
            <v-icon dense>fa-plus</v-icon>
          </v-list-item-icon>
          <v-list-item-title> Nova Pasta </v-list-item-title>
        </v-list-item>

        <v-list-item
          v-for="(item, i) in folders"
          :key="i"
          @click="selectedFolder = i"
          dense
        >
          <v-list-item-icon>
            <v-icon dense
              class="fa-thin"
              v-text="i == selectedFolder ? 'fa-folder-open' : 'fa-folder'"
              :color="item.color"
            ></v-icon>
          </v-list-item-icon>
          <v-list-item-title> {{ item.text }} </v-list-item-title>
          <v-menu offset-y offset-x>
            <template v-slot:activator="{ on }">
              <v-btn icon small v-on="on" v-on:click.prevent>
                <v-icon small>fa-ellipsis-vertical</v-icon>
              </v-btn>
            </template>
            <v-list>
              <!-- Rename Folder Dialog -->
              <v-dialog max-width="300px">
                <template v-slot:activator="{ on }">
                  <v-list-item v-on="on">
                    <v-list-item-title>Renomear</v-list-item-title>
                  </v-list-item>
                </template>
                <template v-slot:default="dialog">
                  <v-card>
                    <v-card-title>
                      <span class="headline">Criar nova pasta</span>
                    </v-card-title>
                    <v-card-text>
                      <v-container
                        class="d-inline align-center justify-center flex-column"
                      >
                        <v-text-field
                          v-model="editFolderValue"
                          label="Nome da pasta"
                        ></v-text-field>
                      </v-container>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="error"
                        text
                        @click.native="dialog.value = false"
                      >
                        Fechar
                      </v-btn>
                      <v-btn
                        color="primary"
                        text
                        @click.native="
                          renameFolder(i, editFolderValue);
                          dialog.value = false
                        "
                      >
                        Salvar
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>

              <!-- Recolor Folder Dialog -->
              <v-dialog max-width="300px">
                <template v-slot:activator="{ on }">
                  <v-list-item v-on="on">
                    <v-list-item-title>Alterar cor</v-list-item-title>
                  </v-list-item>
                </template>
                <template v-slot:default="dialog">
                  <v-card>
                    <v-card-title>
                      <span class="headline">Alterar a cor da pasta</span>
                    </v-card-title>
                    <v-card-text>
                      <v-container
                        class="d-inline align-center justify-center flex-column"
                      >
                        <v-color-picker
                          v-model="editFolderValue"
                          dot-size="15"
                          hide-inputs
                          hide-sliders
                          show-swatches
                          swatches-max-height="150px"
                        ></v-color-picker>
                      </v-container>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="error"
                        text
                        @click.native="dialog.value = false"
                      >
                        Fechar
                      </v-btn>
                      <v-btn
                        color="primary"
                        text
                        @click.native="
                          recolorFolder(i, editFolderValue);
                          dialog.value = false
                        "
                      >
                        Salvar
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>

              <!-- Delete Folder Dialog -->
              <v-dialog max-width="400px">
                <template v-slot:activator="{ on }">
                  <v-list-item v-on="on" class="red--text">
                    <v-list-item-title>Deletar</v-list-item-title>
                  </v-list-item>
                </template>
                <template v-slot:default="dialog">
                  <v-card>
                    <v-card-title>
                      <span class="headline"
                        >Tem certeza que deseja deletar a pasta?</span
                      >
                    </v-card-title>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn text @click.native="dialog.value = false">
                        Fechar
                      </v-btn>
                      <v-btn
                        color="red"
                        text
                        @click.native="
                          deleteFolder(i);
                          dialog.value = false
                        "
                      >
                        Deletar
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
            </v-list>
          </v-menu>
        </v-list-item>

        <v-list-item @click="selectedFolder = -2" dense>
          <v-list-item-icon>
            <v-icon color="grey" dense>{{
              selectedFolder == -2 ? 'fa-folder-open' : 'fa-folder'
            }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title> Sem Categoria </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Table -->
    <ProjectDataTable :headers="headers" :items="projects" :folders="folders" />
  </v-container>
</template>

<script>
export default {
  name: 'IndexPage',

  data() {
    return {
      editFolderValue: '',
      newFolderName: '',
      newFolderDialog: false,
      renameFolderDialog: false,
      selectedFolder: -1,
      required: [(v) => !!v || "O nome é obrigatório!"],
      headers: [
        {
          text: 'Título',
          align: 'start',
          value: 'title',
        },
        {
          text: 'Pastas',
          value: 'folders',
          filter: this.filterByFolder,
          width: '30%',
        },
        {
          text: 'Tipo',
          align: 'start',
          value: 'type',
          divider: true,
          width: '150px',
        },
        { text: 'Último acesso', value: 'lastChanged', width: '150px' },
        { text: 'Ações', value: 'actions', width: '30px' },
      ],

      folders: [
        {
          text: 'Lab. 01',
          color: 'rgb(106, 27, 154)',
        },
      ],

      projects: [
        {
          title: 'Histograma - Lab. IV',
          subtitle: 'Cálculo da gravidade',
          lastChanged: '1 hour ago',
          folders: ["Lab. 01"],
          type: 'Histograma',
          url: '/',
        },
        {
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folders: [],
          type: 'Ajuste',
          url: '/',
        },
        {
          title: 'Ajuste - Grupo 02',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folders: [],
          type: 'Ajuste',
          url: '/',
        },
        {
          title: 'Ajuste - Grupo 03',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folders: [],
          type: 'Ajuste',
          url: '/',
        },
        {
          title: 'Ajuste - Grupo 04',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folders: [],
          type: 'Histograma',
          url: '/',
        },
      ],
    }
  },

  methods: {
    debug() {
      console.log('debug!')
    },

    filterByFolder(value) {
      if (this.selectedFolder === -1 || this.selectedFolder === undefined) {
        return true
      } else if (this.selectedFolder === -2) {
        return value.includes('') || !value.length
      } else {
        return value.includes(this.folders[this.selectedFolder].text)
      }
    },

    createNewFolder(name) {
      this.folders.push({
        text: name,
        color: 'grey',
      })
      this.newFolderDialog = false
      this.newFolderName = ''
    },

    renameFolder(index, value) {
      // Saving old name
      let oldName = this.folders[index]['text']
      this.folders[index]['text'] = value

      // Renaming all projects with this folder
      this.projects.forEach((proj) => {
        let valueIndex = proj.folders.indexOf(oldName)
        if (valueIndex != -1) {
          proj.folders.splice(valueIndex, 1, value)
        }
      })

      this.editFolderValue = ''
    },

    recolorFolder(index, value) {
      this.folders[index].color = value
      this.editFolderValue = ''
    },

    deleteFolder(index) {
      let folderName = this.folders[index].text
      this.folders.splice(index, 1)

      this.projects.forEach((proj) => {
        let valueIndex = proj.folders.indexOf(folderName)
        if (valueIndex != -1) {
          proj.folders.splice(valueIndex, 1)
        }
      })
    },
  },

  watch: {
    folders: {
      deep: true,

      handler(newList) {
        console.log("Folders changed!")
      }
    },

    projects: {
      deep: true,

      handler(newList) {
        console.log('Projects changed!')
      },
    },
  },
}
</script>
