
/* AJAX request to get list of shops using filter:
{ "bike_is_free": {
        "from": <str(date)>,
        "to": <str(date)> },
  "bikes: [
        { "type": <int>, "quantity": <int> },
        { "type": <int>, "quantity": <int> },
           ...
        ]
 } */

import axios from 'axios'
import cookies from "js-cookie"

import getters from '../store/modules/auth'


export default function (dt_from, dt_to='', bikes=[]) {

    let filter = {
        bike_is_free: {
            from: dt_from,
            to: dt_to
        },
        bikes: bikes
    };

    console.log(getters.getToken);

    return axios.post(
        '/api/readShops/',
        // Request Data will be in JSON format
        filter,
        // Axios Configuration
        {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': cookies.get('csrftoken'),
                'authorization': 'key=' + getters.getToken
            }
        },
    )
        .then(response => {
            // console.log(response.data);
            return response.data
        });
        // .catch(e => {console.log(e)});
}
