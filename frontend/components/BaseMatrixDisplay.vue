<template>
  <div
    :style="'font-size: ' + fontSize"
    v-katex="arr2matrix(matrix)"
  ></div>
</template>

<script>
export default {
  props: {
    matrix: {
      type: Array,
      required: true,
      default: () => []
    },
    fontSize: {
      type: String,
      default: '20px'
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
    }
  }
}
</script>

<style scoped>
@import '../node_modules/katex/dist/katex.min.css';
</style>
