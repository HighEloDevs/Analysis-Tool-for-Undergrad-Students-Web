export const state = () => ({
  darkMode: true,
})

export const getters = {
  darkMode: (state) => state.darkMode,
}

export const mutations = {
  toggleDarkMode(state) {
    state.darkMode = !state.darkMode
  },
}

export const actions = {}
