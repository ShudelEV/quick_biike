<template>
    <!--<v-navigation-drawer-->
        <!--app fixed-->
        <!--:mini-variant="miniVariant"-->
        <!--:clipped="clipped"-->
        <!--v-model="drawer"-->
        <!--id="d"-->
    <!--&gt;-->
        <!--<left-menu></left-menu>-->
    <!--</v-navigation-drawer>-->

    <!--<v-navigation-drawer-->
        <!--app fixed right-->
        <!--:clipped="!clipped"-->
        <!--v-model="rightDrawer"-->
        <!--class="lime accent-1"-->
    <!--&gt;-->
<div>
    <content-map></content-map>
    <v-container fluid grid-list-md  style="max-height: 100vh; overflow-y: scroll">
        <v-layout row>
            <v-flex xs12 md4>
                <search-menu></search-menu>
            </v-flex>
            <v-flex xs12 md8>
                <!--Go to the url /order (the pages "Price", "LoginWindow") -->
                <router-view></router-view>
            </v-flex>
        </v-layout>
    </v-container>
    </div>
</template>

<script>
import ContentMap from '../components/ContentMap.vue'
import LeftMenu from '../components/LeftMenu.vue'
import SearchMenu from '../components/SearchMenu.vue'

export default {
    name: 'Home',

    components: {
        ContentMap, LeftMenu, SearchMenu
    },

    props: ['clipped', 'drawer', 'rightDrawer'],

    data () {
        return {
            fixed: false,
            miniVariant: false,
            title: 'QuickBike',
        }
    },

    created () {
        // get shops when the index page starts
        this.$store.dispatch('getAllShops')
    }
}
</script>

<style>
    .order {
        position: absolute;
        top: 0px;
        left: 0px;
        margin: 8px;
        padding: 0;
    }
</style>
