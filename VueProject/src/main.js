import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'

Vue.use(Vuetify, {
    theme: {
        primary: '#ed582f',
        secondary: '#f7c183',
        accent: '#ff7700',
        error: '#b71c1c'
    }
})

Vue({
    el: '#app',
    render: h => h(App)
})
