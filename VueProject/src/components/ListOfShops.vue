<template>
<v-card>
    <v-card-title primary-title>
        <h4>{{shop.name}}</h4>
    </v-card-title>

    <v-list two-line>
        <template v-for="bike in bikes">
            <v-list-tile  @click="">
                <v-list-tile-avatar>
                      <img :src="bike.photo">
                </v-list-tile-avatar>
                <v-list-tile-content>
                    <v-list-tile-title>{{bike.name}}</v-list-tile-title>
                    <v-list-tile-sub-title>Price</v-list-tile-sub-title>
                </v-list-tile-content>
            </v-list-tile>
        </template>
    </v-list>
    <v-divider></v-divider>
</v-card>
</template>

<script>
import readBikes from './readBikes';

export default {
    name: 'ListOfShops',

    props: {
        shop: {type: Object, default: null},
        dt_from: {type: String, default: null},
        dt_to: {type: String, default: null},
        bike_types: {type: Array, default: []},
    },

    data: () => ({
        bikes: null
    }),

    created () {
        this.getBikes()
    },

    watch: {
        shop: function () {
            this.getBikes()
        }
    },

    methods: {
        getBikes () {
            let bikesSet = [];
            let i = 1;
            for (let bike of this.bike_types) {
                if (bike.checked_default) {
                    bikesSet.push({type: i, quantity: bike.quantity})
                }
                i += 1
            }
            // get bikes
            readBikes(this.dt_from, this.dt_to, bikesSet, [this.shop.id])
                .then(data => {
                    this.bikes = data.bikes
                });
        }
    }
}
</script>
