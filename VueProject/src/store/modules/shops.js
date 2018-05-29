import readShops from '../../api/readShops'

const state = {
    all: [],
    active: {
        name: '',
        photo: '',
        contact_info: { phone: '', address: ''},
        animation: 0
    },
};

const getters = {
    allShops: state => state.all,
    activeShop: state => state.active
};

const actions = {
    getAllShops ({ commit }) {
        readShops((new Date()).toISOString().slice(0, 16))
            .then(shops => {
                commit('SET_SHOPS', shops)
            });
    },

    getFilterShops ({ commit }, filter) {
        readShops(filter.dt_from, filter.dt_to, filter.type_qty)
            .then(shops => {
                commit('SET_SHOPS', shops)
            });
    },

    getShop ({ commit }) {
        readShops((new Date()).toISOString().slice(0, 16))
            .then(shop => {
                commit('SET_ACTIVE_SHOP', shop)
            });
    },
};

const mutations = {
    SET_SHOPS (state, { shops }) {
        state.all = shops
    },

    SET_ACTIVE_SHOP (state, shop ) {
        shop.animation = 4,
        state.active = shop
    },
};

export default {
    state,
    getters,
    actions,
    mutations
}

