// Default Values for Plot State
export default () => ({
  // Array with all plots, each object corresponds to one tab
  plotData: [
    {
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
    }
  ],

  // Data for the currently selected plot
  projectData: {
    id: '',
    title: '',
    subtitle: ''
  },

  // Apache echarts API: https://echarts.apache.org/en/option.html#title
  // Settings for the x-axis of the canvas
  xAxis: {
    type: 'value',
    nameLocation: 'center',
    name: '',
    min: null,
    max: null,
    splitNumber: null,
    minorTick: {
      show: true
    },
    minorSplotLine: {
      show: true
    },
    nameTextStyle: {
      fontSize: 12,
      fontWeight: 400
    }
  },

  // Settings for the y-axis of the canvas
  yAxis: {
    type: 'value',
    nameLocation: 'center',
    name: '',
    min: null,
    max: null,
    splitNumber: null,
    minorTick: {
      show: true
    },
    minorSplotLine: {
      show: true
    },
    nameTextStyle: {
      fontSize: 12,
      fontWeight: 400
    }
  },

  // Settings for the title of the canvas
  title: {
    text: '',
    subtext: '',
    left: 'center',
    top: 10,
    textStyle: {
      fontSize: 20,
      fontWeight: 400
    },
    subtextStyle: {
      fontSize: 14,
      fontWeight: 400
    }
  },

  // Settings for the canvas itself
  grid: {
    left: '80',
    right: '80',
    top: '80',
    bottom: '80'
  },

  tooltip: {
    axisPointer: { type: 'cross' }
  }
})
