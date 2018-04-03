
/* AJAX request to get list of bikes using filter:
{ "bike_is_free": {
        "from": <str(date)>,
        "to": <str(date)> },
  "bikes: [
        { "type": <int>, "quantity": <int> },
        { "type": <int>, "quantity": <int> },
           ...
        ],
  ?"shop": { "id": <[int]> }
} */

import axios from 'axios'


export default function (dt_from, dt_to='', bikes=[], shop_ids=[]) {

    let filter = {
        bike_is_free: {
            from: dt_from,
            to: dt_to
        },
        bikes: bikes,
        shop: {
            id: shop_ids
        }
    };

    console.log('readBikes/Form: ', filter);

    // axios.get('/api-auth/login/', {auth: {username: 'quickbike_admin', password: 'velik5000admin'}}
    //         ).then(function(response){console.log(response)});

    return axios.post(
        '/api/readBikes/',
        // Request Data will be in JSON format
        {'filter': filter},
        // Axios Configuration
        {headers: { 'Content-Type': 'application/json'}},
        // {auth: {username: 'quickbike_admin', password: 'velik5000admin'}}
    )
        .then(response => {
            // console.log(response.data);
            return response.data
        });
        // .catch(e => {console.log(e)});
}
