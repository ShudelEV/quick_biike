/* router configuration */

import Vue from 'vue'
import Router from 'vue-router'
// @ is an alias for the /src directory
import Home from './pages/Home.vue'

// tell Vue to use the vue-router plugin
Vue.use(Router);

export default new Router({
    mode: 'history',
    // base: __dirname,
    routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }
    ]
})
