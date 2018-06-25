<template>
    <!--<v-container fluid fill-height pa-0>-->
        <!--<v-layout justify-center align-center>-->
            <gmap-map style="width: 100%; height: 100%; position: absolute;"
                      :center="center"
                      :zoom="12"
                      :draggable="true"
            >
                <gmap-info-window
                    :options="infoOptions"
                    :position="infoWindowPos"
                    :opened="infoWinOpen"
                    @closeclick="infoWinOpen=false"
                    :zIndex="500"
                >
                    <v-card>
                        <v-list two-line>
                            <v-list-tile @click="">
                                <v-list-tile-action>
                                    <v-list-tile-avatar size="50">
                                        <img :src="activeShop.photo"/>
                                    </v-list-tile-avatar>
                                </v-list-tile-action>
                                <v-list-tile-content>
                                  <v-list-tile-title>{{activeShop.name}}</v-list-tile-title>
                                  <v-list-tile-sub-title>{{activeShop.contact_info.phone}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-divider inset></v-divider>
                            <v-list-tile>
                                <v-list-tile-action>
                                  <v-icon color="green">location_on</v-icon>
                                </v-list-tile-action>
                                <v-list-tile-content>
                                  <v-list-tile-title>{{activeShop.contact_info.address}}</v-list-tile-title>
                                  <!--<v-list-tile-sub-title></v-list-tile-sub-title>-->
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card>
                </gmap-info-window>
                <gmap-cluster  :grid-size="50" v-if="clustering">
                    <gmap-marker
                        :key="sh.id"
                        v-for="sh in allShops"
                        :position="{
                            lat: sh.contact_info.latitude,
                            lng: sh.contact_info.longitude
                        }"
                        :title="sh.name"
                        :animation="sh.animation"
                        :clickable="true"
                        :draggable="false"
                        @click="$store.commit('SET_ACTIVE_SHOP', sh)"
                    >
                            <gmap-info-window
                                :opened="sh.id != activeShop.id || !infoWinOpen"
                            >
                                <v-chip color="orange"
                                        text-color="white"
                                >{{ sh.price }} BYN</v-chip>
                            </gmap-info-window>

                    </gmap-marker>
                </gmap-cluster>
            </gmap-map>
        <!--</v-layout>-->
    <!--</v-container>-->
</template>

<script>
import * as VueGoogleMaps from 'vue2-google-maps';
import Vue from 'vue';

import { mapGetters, mapActions } from 'vuex'


Vue.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyB5XIFkcMz1v5ljV-43Tae2Z917rVWt14Q',
        //          libraries: 'places', //// If you need to use place input
    }
});

export default {
    data () {
        return {
            clustering: true,
            infoWindowPos: {
                lat: 0,
                lng: 0
            },
            infoWinOpen: false,
            animation: 4,
            currentMidx: null,
            // optional: offset infowindow so it visually sits nicely on top of our marker
            infoOptions: {
                pixelOffset: {
                    width: 0,
                    height: -35
                }
            },
            center: { lat: 53.90259, lng: 27.4691211 }
        }
    },

    computed: {
        ...mapGetters([ 'allShops', 'activeShop' ]),
    },

    watch: {
        activeShop: function () {
            this.infoWindowPos = {
                lat: this.activeShop.contact_info.latitude,
                lng: this.activeShop.contact_info.longitude
            };
            // check if its the same marker that was selected if yes toggle
            if (this.currentMidx == this.activeShop.id) {
//                this.infoWinOpen = !this.infoWinOpen;
            }
            // if different marker set infowindow to open and reset current marker index
            else {
                this.infoWinOpen = true;
                this.currentMidx = this.activeShop.id;
            }
        }
    }
}
</script>

<!---->
<style>
/* remove a close button from infowindow */
div.gm-style div:first-child div:nth-child(3) div:nth-child(2) div:nth-child(4) div:first-child { overflow: hidden; }
.gm-style-iw {text-align: center; }
.gm-style-iw + div {display: none}
/* remove "full screen" button */
.gmnoprint.gm-style-cc + button {display: none}
</style>
