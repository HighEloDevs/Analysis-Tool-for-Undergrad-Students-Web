export default {
  addPlot: (state) => {
    state.plotData.push({
      fitFunction: '',
      params: [],
      data: [],
      options: {
        fitRange: [0, 1],
        useSx: true,
        useSy: true,
        fit: true,
        connectDots: false
      },
      fitData: {
        params: [],
        corrMatrix: [
          [1, 0],
          [0, 1]
        ],
        covMatrix: [
          [1, 0],
          [0, 1]
        ],
        chi2: 0,
        sumRes: 0,
        ngl: 0
      }
    })
  },

  removePlot: (state, index) => {
    state.plotData.splice(index, 1)
  },

  removeRow: (state, { dataIndex, rowIndex }) => {
    state.plotData[dataIndex].data.splice(rowIndex, 1)
  },

  addRow: (state, { dataIndex, values }) => {
    state.plotData[dataIndex].data.unshift(values)
  },

  setData(state, { path, value }) {
    let props = path.split('.')
    let lastIndex = props.pop()
    let lastObj = props.reduce((prev, curr) => prev[curr], state)
    lastObj[lastIndex] = value
  }
}
