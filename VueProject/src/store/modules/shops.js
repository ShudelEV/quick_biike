import readShops from '../../api/readShops'

const state = {
    all: [],
    active: {
        name: '',
        photo: '',
        contact_info: { phone: '', address: ''},
        animation: 0
    },
    //Form:
        dateTimeFrom: null,
        dateTimeTo: null,
        bikesTypeQty: [
            { type: 1, quantity : 1}
            ]
};

const getters = {
    allShops: state => state.all,
    activeShop: state => state.active,
    dateTimeFrom: state => state.dateTimeFrom,
    dateTimeTo: state => state.dateTimeTo,
    bikesTypeQty: state => state.bikesTypeQty
};

const actions = {
    getAllShops ({ commit }) {
        readShops((new Date()).toISOString().slice(0, 16))
            .then(shops => {
                commit('SET_SHOPS', shops)
            });
    },

    getFilteredShops ({ commit }, filter) {
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

    SET_ACTIVE_SHOP (state, shop) {
        shop.animation = 4;
        state.active = shop
    },

    SET_DATE_TIME_FROM (state, { date, time }) {
        let dtNow = (new Date()).toISOString().slice(0, 16);
        if ( date && time ) {
            state.dateTimeFrom = date + 'T' + time
        } else if (date) {
            state.dateTimeFrom = date + dtNow.slice(10, 16)
        } else {
            state.dateTimeFrom = dtNow
        }
    },

    SET_DATE_TIME_TO (state, period) {
        let dtFrom = new Date(state.dateTimeFrom);
        let dtTo = dtFrom.setHours(dtFrom.getHours() + period);
        state.dateTimeTo = (new Date(dtTo)).toISOString().slice(0, 16)
    },

    PUSH_TYPE_QTY (state, { type, quantity }) {
        state.bikesTypeQty.push({ type: type, quantity: quantity })
    },

    REMOVE_TYPE_QTY (state, type) {
        let i = state.bikesTypeQty.findIndex(b => b.type === type);
        state.bikesTypeQty.splice(i , 1)
    }

};

export default {
    state,
    getters,
    actions,
    mutations
}

