<template>
    <v-content>
        <v-container fluid fill-height pa-0>
            <v-layout justify-center align-center>
                <gmap-map
                  :center="center"
                  :zoom="12"
                  style="width: 100%; height: 100%"
                >
                    <gmap-info-window
                        :options="infoOptions"
                        :position="infoWindowPos"
                        :opened="infoWinOpen"
                        @closeclick="infoWinOpen=false"
                    >
                        {{infoContent}}
                    </gmap-info-window>

                    <gmap-marker
                        :key="sh.id"
                        v-for="sh in shops"
                        :position="{
                                      lat: sh.contact_info.latitude,
                                      lng: sh.contact_info.longitude
                                   }"
                        :clickable="true"
                        :draggable="true"
                        @click="
                            // center=m.position;
                            toggleInfoWindow(sh)"
                    ></gmap-marker>
                </gmap-map>
            </v-layout>
        </v-container>
    </v-content>
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
              currentMidx: null,
              // optional: offset infowindow so it visually sits nicely on top of our marker
              infoOptions: {
                  pixelOffset: {
                    width: 0,
                    height: -35
                  }
              },
              center: {lat: 53.9023238, lng: 27.5618025},
          }
      },

      props: {
          shops: {type: Array, default: null}
      },

      methods: {
          toggleInfoWindow: function(marker) {
              this.infoWindowPos = {
                                      lat: marker.contact_info.latitude,
                                      lng: marker.contact_info.longitude
                                   };
              this.infoContent = marker.name;
              // check if its the same marker that was selected if yes toggle
              if (this.currentMidx == marker.id) {
                  this.infoWinOpen = !this.infoWinOpen;
              }
              // if different marker set infowindow to open and reset current marker index
              else {
                  this.infoWinOpen = true;
                  this.currentMidx = marker.id;
              }
          }
      }
  }

</script>
