import axios from 'axios'


export default function (dt_from, dt_to, bikes) {

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

    axios.get('/api-auth/login/', {auth: {username: 'quickbike_admin', password: 'velik5000admin'}}
            ).then(function(response){console.log(response)});

    axios.post(
        '/api/readShops/',
        JSON.stringify({'form': form}), // Request Data in JSON format
            // Axios Configuration
        {headers: { 'Content-Type': 'application/json'}
        //     'Cookie': )
        },
        // {auth: {username: 'quickbike_admin', password: 'velik5000admin'}}
    ).then(function(response){console.log(response)});

}
