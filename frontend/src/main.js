import './assets/main.css'
import axios from 'axios'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
axios.defaults.withCredentials = false
axios.defaults.baseURL = 'http://localhost:8000/'
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
