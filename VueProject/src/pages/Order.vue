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
    import { bikePrice, typePrice } from '../store/bikePrice'
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
                // get bike price to change order price
                const price = this.free_bikes[index].price[typePrice(this.period)];
                if (i > -1) {
                    this.selected.splice(i, 1);
                    this.price -= price
                } else {
                    this.selected.push(index);
                    this.price += price
                }
            },

            // activate default checkbox (suggest cheaper bikes) and calculate price
            getPriceAndSelected () {
                let { amount, selected } = bikePrice(this.free_bikes, this.bikeTypeQty, this.period);
                this.price = amount;
                Array.prototype.push.apply(this.selected, selected)
            }
        }
    }
</script>
