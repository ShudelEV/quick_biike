<template>
<v-card>
    <v-card-media
        :src="shop.photo"
        height="128px"
        class="white--text"
        @mouseover="activateShop()"
    >
        <v-container fill-height fluid>
            <v-layout fill-height>
                <v-flex xs12 align-end flexbox>
                    <span class="headline">{{ shop.name }}</span>
                </v-flex>
            </v-layout>
        </v-container>
    </v-card-media>

    <!--<v-card-title primary-title>-->
        <!--<h4>{{ shop.contact_info.address }}, {{ shop.contact_info.phone }}</h4>-->
    <!--</v-card-title>-->

    <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" outline :to="createPath()">
            {{ shop.price ? shop.price + ' BYN' : 'order' }}
        </v-btn>
        <!--<v-btn flat color="purple"-->
               <!--@click.native="show = !show"-->
               <!--v-show="!show"-->
        <!--&gt;Show Bikes</v-btn>-->
        <!--<v-btn icon @click.native="show = !show">-->
            <!--<v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>-->
        <!--</v-btn>-->
    </v-card-actions>

    <!--<v-list two-line v-show="show">-->
        <!--<template v-for="bike in bikes">-->
            <!--<v-list-tile :key="bike.id" @click="">-->
                <!--<v-list-tile-avatar>-->
                      <!--<img :src="bike.photo">-->
                <!--</v-list-tile-avatar>-->
                <!--<v-list-tile-content>-->
                    <!--<v-list-tile-title>{{bike.name}}</v-list-tile-title>-->
                    <!--<v-list-tile-sub-title>Price</v-list-tile-sub-title>-->
                <!--</v-list-tile-content>-->
            <!--</v-list-tile>-->
        <!--</template>-->
    <!--</v-list>-->
    <v-divider></v-divider>
</v-card>
</template>

<script>
import readBikes from '../api/readBikes';

export default {
    name: 'ListOfShops',

    props: {
        dateTimeFrom: {type: String, default: null},
        dateTimeTo: {type: String, default: null},
        period: {type: Number, default: 1},
        bikesTypeQty: {type: Array, default: () => []},
        shop: {type: Object, default: null}
    },

    data: () => ({
        show: false
    }),

    methods: {
        createPath () {
            let query = {
                id: this.shop.id,
                from: this.dateTimeFrom,
                period: this.period,
                bikesTypeQty: JSON.stringify(this.bikesTypeQty)
            };
            return { name: 'Order', query: query }
        },

        activateShop () {
            this.$store.commit('SET_ACTIVE_SHOP', this.shop)
        }
    }
}
</script>
