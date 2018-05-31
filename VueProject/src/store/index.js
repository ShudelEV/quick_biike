import Vue from 'vue'
import Vuex from 'vuex'
import shops from './modules/shops'
import auth from './modules/auth'
// import createLogger from '../../../src/plugins/logger'

Vue.use(Vuex);

// const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
    modules: {
        shops,
        auth
    },
    // strict: debug,
    // plugins: debug ? [createLogger()] : []
})
