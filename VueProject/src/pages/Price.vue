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
                <template v-for="(bike, index) in bikes">
                    <v-list-tile :key="index"
                                 @click=""
                    >
                        <v-list-tile-avatar>
                              <img :src="bike.photo">
                        </v-list-tile-avatar>

                        <v-list-tile-content>
                            <v-list-tile-title>{{bike.name}}</v-list-tile-title>
                            <v-list-tile-sub-title>Price</v-list-tile-sub-title>
                        </v-list-tile-content>

                        <v-spacer></v-spacer>

                        <v-text-field v-if="!(selected.indexOf(index) < 0)"
                                      solo flat box
                                      type="number"
                                      :value="getQty(bike.type)"
                                      @change=""
                        ></v-text-field>

                        <v-list-tile-action @click="changeStatus(index)">
                            <v-icon v-if="selected.indexOf(index) < 0"
                            >check_box_outline_blank</v-icon>
                            <v-icon v-else
                                    color="orange"
                            >check_box</v-icon>
                        </v-list-tile-action>
                    </v-list-tile>
                </template>
            </v-list>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" flat @click.native="goBack()">Close</v-btn>
                <v-btn color="blue darken-1" flat @click.native="">Save</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    import readBikes from '../components/readBikes';
    import axios from 'axios'

    export default {
        data () {
            return {
                showDialog: true,
                bikes: [],
                selected: [],
                shop: {name: "", photo: ""}
            }
        },

        props: {
            id: {type: Number, default: 0},
            dt_from: {type: String, default: ''},
            dt_to: {type: String, default: ''},
            bikeTypeQty: {type: Array, default: []},
        },

        created () {
            // get Shop
            axios.get('/api/shops/' + this.id + '/')
                .then(response => {
                    this.shop = response.data
                });

            // get Bikes
            readBikes(this.dt_from, this.dt_to, this.bikeTypeQty, [this.id])
                .then(data => {
                    this.bikes = data.bikes
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
                else { return 1 }
            }
        }
    }
</script>
