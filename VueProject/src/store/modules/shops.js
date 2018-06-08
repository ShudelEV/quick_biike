import readShops from '../../api/readShops'

const state = {
    all: [],
    active: {
        name: '',
        photo: '',
        contact_info: { phone: '', address: ''},
        animation: 0
    },
    // filter: {
    //     date_from: null,
    //     time_from: null,
    //     date_to: null,
    //     time_to: null,
    //     bikes: []
    // }
};

const getters = {
    allShops: state => state.all,
    activeShop: state => state.active,
    // date_from: state => state.date_from,
    // time_from: state => state.time_from,
    // date_to: state => state.date_to,
    // time_to: state => state.time_to
};

const actions = {
    getAllShops ({ commit }) {
        readShops((new Date()).toISOString().slice(0, 16))
            .then(shops => {
                commit('SET_SHOPS', shops)
            });
    },

    getFilteredShops ({ commit }, filter) {
        console.log(filter);
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
        shop.animation = 4;
        state.active = shop
    },

    // SET_DATE_FROM (state, d) {
    //     state.filter.date_from = d
    // }
};

export default {
    state,
    getters,
    actions,
    mutations
}

