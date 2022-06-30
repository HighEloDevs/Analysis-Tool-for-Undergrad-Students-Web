<template>
  <v-container fluid>
    <v-navigation-drawer app permanent clipped width="300px">
      <v-list dense>
        <v-list-item>
          <v-btn color="primary" block rounded elevation-5>Novo Projeto</v-btn>
        </v-list-item>
        <v-list-item @click="filter = none" dense>
          <v-list-item-title> Todos os projetos </v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-subheader>Pastas</v-subheader>
        <v-list-item @click="newFolderPopup = !newFolderPopup" dense>
          <v-list-item-icon>
            <v-icon>mdi-plus</v-icon>
          </v-list-item-icon>

          <v-list-item-title> Nova Pasta </v-list-item-title>
        </v-list-item>
        <v-list-item-group v-model="filter">
          <v-list-item v-for="(item, i) in filters" :key="item.text" dense>
            <v-list-item-icon>
              <v-icon
                v-text="i === filter ? 'mdi-folder-open' : 'mdi-folder'"
                :color="item.color"
              ></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon>mdi-dots-vertical</v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-item-group>
        <v-list-item @click="filter = 'uncategorized'" dense>
          <v-list-item-icon>
            <v-icon color="grey">{{
              filter == 'uncategorized' ? 'mdi-folder-open' : 'mdi-folder'
            }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title> Sem Categoria </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    {{ filter }}
    <ProjectDataTable
      :headers="headers"
      :items="projects"
      class="fill-height fill-width"
      deleteMessage="Tem certeza que deseja deletar esse projeto?"
      emptyMessage="Clique em 'Novo Projeto' para criar um novo projeto."
    />
  </v-container>
</template>

<script>
export default {
  name: 'IndexPage',

  data() {
    return {
      newFolderPopup: false,
      filter: '',
      headers: [
        {
          text: 'Título',
          align: 'start',
          value: 'title',
        },
        { text: 'Pasta', value: 'folder' },
        { text: 'Último acesso', value: 'lastChanged' },
        { text: 'Ações', value: 'actions', sortable: false },
      ],
      filters: [
        {
          text: 'Lab. 01',
          color: '#0f0',
        },
        {
          text: 'Histogramas',
          color: '#f00',
        },
        {
          text: 'Plots',
          color: '#00f',
        },
      ],
      projects: [
        {
          color: '#1F7087',
          src: '',
          title: 'Histograma - Lab. IV',
          subtitle: 'Cálculo da gravidade',
          lastChanged: '1 hour ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'lab 1',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
        {
          color: '#952175',
          src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Ajuste - Grupo 01',
          subtitle: 'Experimento massa',
          lastChanged: '2 hours ago',
          folder: 'histograma',
        },
      ],
    }
  },

  methods: {
    logout() {
      this.$auth.logout('local')
    },

    teste() {
      console.log('teste')
    },
  },
}
</script>
