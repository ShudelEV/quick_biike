import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'
import router from './router'

import axios from 'axios'
import VueAxios from 'vue-axios'

import Firebase from "./api/firebase"

import store from './store/index'
import App from './App.vue'

// tell Vue whether or not to show tips and warnings in the developer console of browser
Vue.config.productionTip = true;

Vue.use(Vuetify);

// wrapper for integrating axios to Vuejs
Vue.use(VueAxios, axios);

Firebase.initFirebase();

const app = new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: { App }
});

global._App = app;
