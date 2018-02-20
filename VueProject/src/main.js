import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'


// For emitting events between non-bind components
export var bus = new Vue();

Vue.use(Vuetify);

new Vue({
    el: '#app',
    render: h => h(App)
})

