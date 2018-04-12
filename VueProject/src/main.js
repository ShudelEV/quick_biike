import Vue from 'vue'
import router from './router'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'

// tell Vue whether or not to show tips and warnings in the developer console of browser
Vue.config.productionTip = true

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
    router,
    template: '<App/>',
    components: { App }
});
