/* chose price type to use in calculation price */
function typePrice (period=1) {
    let price = '';
    switch (period) {
        case 1: price = 'workday_one_hour'; break;
        case 2: price = 'workday_one_hour'; break;
        case 3: price = 'workday_three_hours'; break;
        case 24: price = 'workday_one_hour'; break;
        case 72: price = 'workday_one_hour'; break;
    }
    return price
}

/* calculate min order price for an array of bike objects
  * and return indexes of bikes that cheaper */
function bikePrice (bikes, bikesTypeQty=[], period=1) {
    const price = typePrice(period);
    // sort bikes by a type price:
    const comp = 'workday_one_hour';
    let amount = 0;
    let selected = [];
    for (let tq of bikesTypeQty) {
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
                const bike = filt_sort_bikes[q];
                // add selected bikes for to check default
                selected.push(bikes.findIndex(b => b.id === bike.id));
                // get price of bike
                amount += bike.price[price]
            }
        }
    }
    return { amount, selected }
}

export { bikePrice, typePrice }
