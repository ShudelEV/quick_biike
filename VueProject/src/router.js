/* router configuration */

import Vue from 'vue'
import Router from 'vue-router'
// @ is an alias for the /src directory
import Home from './pages/Home.vue'
import Price from './pages/Price.vue'
import LoginWindow from './pages/LoginWindow.vue'

// tell Vue to use the vue-router plugin
Vue.use(Router);

function dynamicPropsFnOrder(route) {
    return {
        id: route.query.id,
        dt_from: route.query.dt_from,
        dt_to: route.query.dt_to,
        bikeTypeQty: JSON.parse(route.query.bikeTypeQty)
    }
}

export default new Router({
    mode: 'history',
    // base: __dirname,
    routes: [
    {
        path: '/',
        name: 'index',
        component: Home,
        children: [
            {
                path: 'order',
                name: 'order',
                component: Price,
                props: dynamicPropsFnOrder
            },
            {
                path: 'login',
                name: 'login',
                component: LoginWindow
            }
        ]
    },
    ]
})
