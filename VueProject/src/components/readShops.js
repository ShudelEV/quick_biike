
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


export default function (dt_from, dt_to='', bikes=[]) {

    console.log('readShops: ' +
        'from - ' + dt_from + ', to - ' + dt_to + '\n\t' +
        'bikes - ' +  bikes);

    let form = {
        bike_is_free: {
            from: dt_from,
            to: dt_to
        },
        bikes: bikes
    };

    // axios.get('/api-auth/login/', {auth: {username: 'quickbike_admin', password: 'velik5000admin'}}
    //         ).then(function(response){console.log(response)});

    return axios.post(
        '/api/readShops/',
        {'form': form}, // Request Data will be in JSON format
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
