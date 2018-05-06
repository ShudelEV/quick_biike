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
                <div v-for="bike in bikes" :key="bike.id">
                    <v-list-tile  @click="">
                        <v-list-tile-avatar>
                              <img :src="bike.photo">
                        </v-list-tile-avatar>
                        <v-list-tile-content>
                            <v-list-tile-title>{{bike.name}}</v-list-tile-title>
                            <v-list-tile-sub-title>Price</v-list-tile-sub-title>
                        </v-list-tile-content>
                        <v-spacer></v-spacer>
                        <v-text-field v-if="bike.checked"
                                      type="number" solo flat
                                      @change="validateQty"
                        ></v-text-field>
                        <v-checkbox :input-value="bike.checked"
                                    @change="changeStatus(bike.id, bike.checked)"
                                    color="orange"
                        ></v-checkbox>
                    </v-list-tile>
                </div>
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
            axios.get('/api/shops/' + this.id + '/').then(response => {
                this.shop = response.data
            });

            // get Bikes
            readBikes(this.dt_from, this.dt_to, this.bikeTypeQty, [this.id])
                .then(data => {
                    this.bikes = data.bikes;
                    // Add a check box for each bike
                    for (let i = 0; i < this.bikes.length; i++) {
                        this.bikes[i]["checked"] = false
                    }
                });
        },

        methods: {
            goBack () {
                window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
            },

            changeStatus (id, checked) {
                // this.bikes.find({id: id})["checked"] = !checked;
            }
        }
    }
</script>
