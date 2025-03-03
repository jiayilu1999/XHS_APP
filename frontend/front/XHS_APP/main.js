import Vue from 'vue'
import App from './App'

// #ifndef VUE3
import './uni.promisify.adaptor'
import store from './store'

// 关闭生产提示
Vue.config.productionTip = false

// 设置应用类型
App.mpType = 'app'

// 创建Vue实例
const app = new Vue({
  store,
  ...App
})

// 挂载应用
app.$mount()

// #ifdef VUE3
import { createSSRApp } from 'vue'
export function createApp() {
  const app = createSSRApp(App)
  return {
    app
  }
}
// #endif

// 导出实例
export default {
  app
}