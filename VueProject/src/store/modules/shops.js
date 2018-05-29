import readShops from '../../api/readShops'

const state = {
  all: []
};

const getters = {
    allShops: state => state.all
};

const actions = {
    getAllShops ({ commit }) {
        readShops((new Date()).toISOString().slice(0, 16))
            .then(data => {
                commit('SET_SHOPS', data)
            });
    },

    getFilterShops ({ commit }, filter) {
        readShops(filter.dt_from, filter.dt_to, filter.type_qty)
            .then(shops => {
                commit('SET_SHOPS', shops)
            });
    }
};

const mutations = {
    SET_SHOPS (state, { shops }) {
        state.all = shops
    },
};

export default {
    state,
    getters,
    actions,
    mutations
}

