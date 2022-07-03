<template>
  <v-container
    @drop.prevent="onDrop($event)"
    @dragover.prevent="dragOver = true"
    @dragenter.prevent="dragOver = true"
    @dragleave.prevent="dragOver = false"
    :class="{ 'grey lighten-2': dragOver }"
    class="d-flex flex-column align-center"
  >
    <input
      type="file"
      ref="fileInput"
      class="d-none"
      :multiple="multiple"
      :accept="accept"
      @change="loadFiles"
    />
    <v-card
      v-if="uploadedFiles.length == 0"
      @mouseover="mouseOver = true"
      @mouseleave="mouseOver = false"
      @click="$refs.fileInput.click()"
      color="transparent"
      class="d-flex flex-column justify-center align-center py-4"
      flat
    >
      <v-icon
        class="mb-2 primary--text"
        size="60"
        :class="{ 'vert-move': dragOver || mouseOver }"
      >
        fa-cloud-arrow-up
      </v-icon>
      <p class="mb-0">
        Arraste seu(s) arquivos(s) ou clique para seleciona-lo(s).
      </p>
      <p class="mb-0 caption grey--text">
        Extensões aceitas: {{ accept.split(',').join(' / ') }}
      </p>
    </v-card>
    <v-virtual-scroll
      v-if="uploadedFiles.length > 0"
      :items="uploadedFiles"
      style="width: 100%"
      max-height="200"
      item-height="50"
    >
      <template v-slot:default="{ item }">
        <v-list-item :key="item.name">
          <v-list-item-content>
            <v-list-item-title>
              {{ item.name }}
              <span class="ml-3 text--secondary"> {{ item.size }} bytes</span>
            </v-list-item-title>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn @click.stop="removeFile(item.name)" icon>
              <v-icon> fa-xmark </v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
      </template>
    </v-virtual-scroll>
    <v-btn
      v-if="uploadedFiles.length != 0 && multiple"
      class="primary--text"
      @click="$refs.fileInput.click()"
      text
    >
      <v-icon small left>fa-plus</v-icon>
      Adicionar
    </v-btn>
  </v-container>
</template>

<script>
export default {
  props: {
    multiple: {
      type: Boolean,
      default: false,
    },
    uploadedFiles: {
      type: Array,
      default: [],
    },
    accept: {
      type: String,
      default: '*',
    },
  },

  data() {
    return {
      mouseOver: false,
      dragOver: false,
    }
  },

  methods: {
    removeFile(fileName) {
      // Find the index of the file
      const index = this.uploadedFiles.findIndex(
        (file) => file.name === fileName
      )

      // If file is in uploaded files remove it
      if (index > -1) this.uploadedFiles.splice(index, 1)
    },

    onDrop(e) {
      this.dragOver = false
      let droppedFiles = Array.from(e.dataTransfer.files)

      // If user has uploaded multiple files but the component is not multiple throw error
      if (!this.multiple && droppedFiles.length > 1) return
      // Add each file to the array of uploaded files
      else {
        droppedFiles.forEach((element) => {
          let fileExt = element.name.split('.').pop()
          if (this.accept.includes(fileExt)) this.uploadedFiles.push(element)
        })
      }
    },

    loadFiles(e) {
      let files = Array.from(e.target.files)
      files.forEach((element) => this.uploadedFiles.push(element))
    },
  },
}
</script>

<style>
.vert-move {
  -webkit-animation: mover 1s infinite alternate;
  animation: mover 1s infinite alternate;
}

.vert-move {
  -webkit-animation: mover 1s infinite alternate;
  animation: mover 1s infinite alternate;
}

@-webkit-keyframes mover {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-10px);
  }
}

@keyframes mover {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-10px);
  }
}
</style>
