import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    userInfo: null,
    generationHistory: []
  },
  mutations: {
    SET_USER_INFO(state, userInfo) {
      state.userInfo = userInfo
    },
    ADD_GENERATION_HISTORY(state, item) {
      state.generationHistory.unshift(item)
    }
  },
  actions: {
    async login({ commit }) {
      // 实现登录逻辑
    },
    saveGenerationHistory({ commit }, item) {
      commit('ADD_GENERATION_HISTORY', item)
    }
  }
})

export default store