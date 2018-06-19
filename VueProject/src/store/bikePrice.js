export default function (period) {
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
