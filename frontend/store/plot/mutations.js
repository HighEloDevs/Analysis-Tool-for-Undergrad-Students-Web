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

  setPlotData: (state, payload) => {
    let index = payload.index
    let field = payload.field
    let value = payload.value
    state.plotData[index][field] = value
  },

  setProjectData: (state, field, value) => {
    state.projectData[field] = value
  },

  setxAxis: (state, field, value) => {
    state.xAxis[field] = value
  },

  setyAxis: (state, field, value) => {
    state.yAxis[field] = value
  },

  setTitle: (state, field, value) => {
    state.title[field] = value
  },

  setGrid: (state, field, value) => {
    state.grid[field] = value
  }
}
