<template>
<v-app>
    <v-navigation-drawer
        app fixed
        :mini-variant="miniVariant"
        :clipped="clipped"
        v-model="drawer"
    >

        <left-menu></left-menu>

    </v-navigation-drawer>

    <v-toolbar fixed app :clipped-left="clipped" color="lime accent-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <!--<v-btn icon @click.stop="clipped = !clipped">-->
            <!--<v-icon>web</v-icon>-->
        <!--</v-btn>-->
        <v-toolbar-title v-text="title"></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click.stop="rightDrawer = !rightDrawer">
            <v-icon v-html="rightDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>
        </v-btn>
    </v-toolbar>

    <content-map :shops="shops"></content-map>

    <v-navigation-drawer
        app fixed right
        :clipped="!clipped"
        v-model="rightDrawer"
        class="lime accent-1"
    >

        <right-menu
            :shops="shops"
            @setShopsOnMap="(dtFrom, dtTo, bikes) => {
                setShops(dtFrom, dtTo, bikes)}"
        ></right-menu>

    </v-navigation-drawer>

    <!--<base-footer></base-footer>-->

</v-app>
</template>

<script>
import ContentMap from './components/ContentMap.vue'
import LeftMenu from './components/LeftMenu.vue'
import RightMenu from './components/Order.vue'
import BaseFooter from './components/Footer.vue'

import readShops from './components/readShops';

export default {
    components: {
        ContentMap, LeftMenu, RightMenu, BaseFooter
    },

    data () {
        return {
            clipped: true,
            drawer: false,
            fixed: false,
            miniVariant: false,
            rightDrawer: true,
            title: 'QuickBike',

            shops: null
        }
    },

    created () {
        // get shops when the index page starts
        readShops((new Date()).toISOString().slice(0, 16))
            .then(data => {
                this.shops = data.shops
            });
    },

    methods: {
        // update the list of shops when any input in Order is changed
        setShops (dtFrom, dtTo, bikes) {
              readShops(dtFrom, dtTo, bikes)
                  .then(data => {
                      this.shops = data.shops
                  })
        },
    }
}
</script>
