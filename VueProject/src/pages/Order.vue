<template>
    <v-dialog v-model="showDialog"
              max-width="500px"
              persistent
    >
        <v-card class="elevation-12">
            <v-card-media :src="shop.photo"
                          height="128px"
                          class="white--text"
            >
                <v-container fill-height fluid>
                    <v-layout fill-height>
                        <v-flex xs12 align-end flexbox>
                            <span class="headline">{{shop.name}}</span>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-card-media>

            <v-list two-line>
                <template v-for="(bike, index) in free_bikes">
                    <v-list-tile :key="index"
                                 @click=""
                    >
                        <v-list-tile-avatar>
                              <img :src="bike.photo">
                        </v-list-tile-avatar>

                        <v-list-tile-content>
                            <v-list-tile-title>{{ bike.name }}</v-list-tile-title>
                            <v-list-tile-sub-title>
                                {{ bike.price.workday_one_hour }} BYN
                            </v-list-tile-sub-title>
                        </v-list-tile-content>

                        <v-spacer></v-spacer>

                        <v-list-tile-action @click="changeStatus(index)">
                            <v-icon v-if="selected.indexOf(index) < 0">
                                check_box_outline_blank
                            </v-icon>
                            <v-icon v-else color="orange">check_box</v-icon>
                        </v-list-tile-action>
                    </v-list-tile>
                </template>
            </v-list>

            <v-card-actions>
                <v-btn color="blue darken-1" flat @click.native="goBack()">Cancel</v-btn>
                <v-spacer></v-spacer>
                <v-btn color="green darken-1" outline @click.native=""> {{ price }} BYN</v-btn>
                <!--<v-btn color="blue darken-1" flat @click.native="">Order</v-btn>-->
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    import readBikes from '../api/readBikes';
    import bikePrice from '../store/bikePrice'
    import axios from 'axios'

    export default {
        data () {
            return {
                showDialog: true,
                free_bikes: [],
                selected: [],
                shop: {name: "", photo: ""},
                price: 0
            }
        },

        props: {
            id: {type: Number, default: 0},
            from: {type: String, default: ''},
            period: {type: Number, default: 1},
            bikeTypeQty: {type: Array, default: function () { return [] }}
        },

        created () {
            // get Shop
            axios.get('/api/shops/' + this.id + '/')
                .then(response => {
                    this.shop = response.data
                });

            // get all free Bikes
            readBikes(this.from, this.dt_to, [], [this.id])
                .then(data => {
                    this.free_bikes = data.bikes;
                    this.getPriceAndSelected()
                });
        },

        methods: {
            goBack () {
                window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
            },

            changeStatus (index) {
                const i = this.selected.indexOf(index);
                if (i > -1) {
                    this.selected.splice(i, 1)
                } else {
                    this.selected.push(index)
                }
            },

            getQty (type) {
                let b = this.bikeTypeQty.find( t => String(t.type) === type);
                if (b) { return b.quantity }
                // default one bike
                else { return 1 }
            },

            // activate default checkbox (suggest cheaper bikes) and calculate price
            getPriceAndSelected () {
                let price = 0;
                for (let tq of this.bikeTypeQty) {
                    // compare by a type price:
                    const comp = 'workday_one_hour';
                    // get bikes of only appropriate type
                    // and sort to choose cheaper at first
                    const filt_sort_bikes = this.free_bikes
                        .filter(b => Number(b.type) === tq.type)
                        .sort((a, b) => {
                            if (a.price[comp] > b.price[comp]) { return 1; }
                            if (a.price[comp] < b.price[comp]) { return -1; }
                            return 0
                        });
                    for (let bike of filt_sort_bikes) {
                        for (let q = 1; q <= tq.quantity; q++) {
                            // add selected bikes for to check default
                            this.selected.push(
                                this.free_bikes.findIndex(b => b.id === bike.id)
                            );
                            // get price of bike
                            price += bike.price[bikePrice(this.period)]
                        }
                    }
                }
                this.price = price;
                }
        }
    }
</script>
