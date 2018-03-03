import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'


Vue.use(Vuetify);

// For emitting events between non-bind components
const EventBus = new Vue();

Object.defineProperties(Vue.prototype, {
    $bus: {
        get: function () {
          return EventBus
        }
    }
});

let vm = new Vue({
    el: '#app',
    render: h => h(App)
});
