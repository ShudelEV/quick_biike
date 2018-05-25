import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'
import VueAuthenticate from 'vue-authenticate'

// tell Vue whether or not to show tips and warnings in the developer console of browser
Vue.config.productionTip = true;

Vue.use(Vuetify);
// wrapper for integrating axios to Vuejs
Vue.use(VueAxios, axios);

Vue.use(VueAuthenticate, {
  baseUrl: 'http://localhost:8000', // Your API domain

  providers: {
    // github: {
    //   clientId: '',
    //   redirectUri: 'http://localhost:8000/auth/callback' // Your client app URL
    // }
  }
});

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
