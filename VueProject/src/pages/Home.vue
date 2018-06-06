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
        <v-dialog
            v-model="rightDrawer"
            content-class="map-order"
            hide-overlay persistent
            max-width="300px">
            <right-menu></right-menu>
        </v-dialog>
         <!--Go to the url /order (the pages "Price", "LoginWindow") -->
        <router-view></router-view>
    </div>
</template>

<script>
import ContentMap from '../components/ContentMap.vue'
import LeftMenu from '../components/LeftMenu.vue'
import RightMenu from '../components/Order.vue'

export default {
    name: 'Home',

    components: {
        ContentMap, LeftMenu, RightMenu
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
    .map-order {
        position: absolute;
        top: 96px;
        right: 0px;
    }
</style>
