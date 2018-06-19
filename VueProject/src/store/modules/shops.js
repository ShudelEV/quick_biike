import readShops from '../../api/readShops'
import bikePrice from '../bikePrice'

const state = {
    // Shop:
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
    period: 1,
    bikesTypeQty: [
        /* default: one man bike*/
        {type: 1, quantity : 1},
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

// calculate total order price for a shop
function eval_total_price (bikes) {
    let amount = 0;
    for (let tq of state.bikesTypeQty) {
        // compare by a type price:
        const comp = 'workday_one_hour';
        // get bikes of only appropriate type
        // and sort to choose cheaper at first
        const filt_sort_bikes = bikes
            .filter(b => Number(b.type) === tq.type)
            .sort((a, b) => {
                if (a.price[comp] > b.price[comp]) { return 1; }
                if (a.price[comp] < b.price[comp]) { return -1; }
                return 0
            });
        if (!!filt_sort_bikes.length) {
            for (let q = 0; q < tq.quantity; q++) {
            // get price of bike
            amount += filt_sort_bikes[q].price[bikePrice(state.period)]
            }
        }
    }
    return amount
}

const mutations = {
    SET_SHOPS (state, { shops }) {
        for (let shop of shops) {
            shop.price = eval_total_price(shop.bikes)
        }
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
        state.period = period;
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

