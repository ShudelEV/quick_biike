<template>
    <!--<v-container fluid fill-height pa-0>-->
        <!--<v-layout justify-center align-center>-->
            <gmap-map style="width: 100%; height: 90%; position: absolute;"
                      :center="center"
                      :zoom="12"
                      :draggable="true"
            >
                <gmap-info-window
                    :options="infoOptions"
                    :position="infoWindowPos"
                    :opened="infoWinOpen"
                    @closeclick="infoWinOpen=false"
                >
                    <v-card>
                        <!--<v-card-title primary-title>-->
                            <!--<div>-->
                                <!--<div class="headline">{{shop.name}}</div>-->
                                <!--<span class="grey&#45;&#45;text">{{shop.contact_info.phone}}</span>-->
                            <!--</div>-->
                        <!--</v-card-title>-->
                        <v-list two-line>
                            <v-list-tile @click="">
                                <v-list-tile-action>
                                    <v-list-tile-avatar size="50">
                                        <img :src="shop.photo"/>
                                    </v-list-tile-avatar>
                                </v-list-tile-action>
                                <v-list-tile-content>
                                  <v-list-tile-title>{{shop.name}}</v-list-tile-title>
                                  <v-list-tile-sub-title>{{shop.contact_info.phone}}</v-list-tile-sub-title>
                                </v-list-tile-content>
                            </v-list-tile>
                            <v-divider inset></v-divider>
                            <v-list-tile>
                                <v-list-tile-action>
                                  <v-icon color="green">location_on</v-icon>
                                </v-list-tile-action>
                                <v-list-tile-content>
                                  <v-list-tile-title>{{shop.contact_info.address}}</v-list-tile-title>
                                  <!--<v-list-tile-sub-title></v-list-tile-sub-title>-->
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card>
                </gmap-info-window>
                <gmap-marker
                    :key="sh.id"
                    v-for="sh in shops"
                    :position="{
                        lat: sh.contact_info.latitude,
                        lng: sh.contact_info.longitude
                    }"
                    :title="sh.name"
                    :animation="sh.animation"
                    :clickable="true"
                    :draggable="false"
                    @click="$store.commit('SET_ACTIVE_SHOP', sh)"
                ></gmap-marker>
            </gmap-map>
        <!--</v-layout>-->
    <!--</v-container>-->
</template>

<script>
  import * as VueGoogleMaps from 'vue2-google-maps';
  import Vue from 'vue';


  Vue.use(VueGoogleMaps, {
      load: {
          key: 'AIzaSyB5XIFkcMz1v5ljV-43Tae2Z917rVWt14Q',
//          libraries: 'places', //// If you need to use place input
      }
  });

  export default {
      data () {
          return {
              infoContent: '',
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
              center: {lat: 53.9023238, lng: 27.5618025}
          }
      },

      computed: {
          shops: function () {
              return this.$store.getters.allShops
          },
          shop: function () {
              return this.$store.getters.activeShop
          }
      },

      watch: {
          shop: function () {
              this.infoWindowPos = {
                  lat: this.shop.contact_info.latitude,
                  lng: this.shop.contact_info.longitude
              };
              // check if its the same marker that was selected if yes toggle
              if (this.currentMidx == this.shop.id) {
//                  this.infoWinOpen = !this.infoWinOpen;
              }
              // if different marker set infowindow to open and reset current marker index
              else {
                  this.infoWinOpen = true;
                  this.currentMidx = this.shop.id;
              }
          }
      },

      methods: {
      }
  }
</script>

<style>
.map-panel {
  absolute: 4 1 80%;
}
</style>
