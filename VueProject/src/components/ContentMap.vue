<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout justify-center align-center>
                <gmap-map
                  :center="center"
                  :zoom="12"
                  style="width: 100%; height: 100%"
                >
                  <gmap-marker
                    :key="index"
                    v-for="(m, index) in markers"
                    :position="m.position"
                    :clickable="true"
                    :draggable="true"
                    @click="center=m.position"
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
      // libraries: 'places', //// If you need to use place input
    }
  });

  var markers = [{
          position: {lat: 53.870899, lng: 27.517329}
        }, {
          position: {lat: 53.893001, lng: 27.603587}
        }, {
          position: {lat: 53.930904, lng: 27.519106}
        }]

  export default {
    data () {
      return {
        center: {lat: 53.9023238, lng: 27.5618025},
        markers: markers
      }
    }
  }

</script>

<style>
    .fill-height {
        padding: unset;
    }
</style>
