/* router configuration */

import Vue from 'vue'
import Router from 'vue-router'
// @ is an alias for the /src directory
import Home from './pages/Home.vue'
import Order from './pages/Order.vue'
import LoginWindow from './pages/LoginWindow.vue'
import Account from './pages/Account.vue'
import NotFound from './components/errors/404.vue'

// tell Vue to use the vue-router plugin
Vue.use(Router);

function dynamicPropsFnOrder(route) {
    return {
        id: Number(route.query.id),
        from: route.query.from,
        period: Number(route.query.period),
        bikeTypeQty: JSON.parse(route.query.bikesTypeQty)
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
                    name: 'Order',
                    component: Order,
                    props: dynamicPropsFnOrder,
                },
                {
                    path: 'login',
                    name: 'Login',
                    component: LoginWindow,
                    // beforeEnter: ifNotAuthenticated,
                },
                {
                    path: 'account',
                    name: 'Account',
                    component: Account,
                    // beforeEnter: ifAuthenticated,
                },
                // {
                //     path: '*',
                //     component: NotFound
                // }
            ]
        },
    ]
})
