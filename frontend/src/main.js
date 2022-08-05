import { createApp } from 'vue'
import {Vuex} from 'vuex'
import App from './App.vue'
import store from './store'
import router from '@/router/index'


createApp(App).use(store).use(Vuex).use(router).mount('#app')