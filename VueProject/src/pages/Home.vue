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

    <content-map></content-map>

    <v-navigation-drawer
        app fixed right
        :clipped="!clipped"
        v-model="rightDrawer"
        class="lime accent-1"
    >
        <right-menu></right-menu>
    </v-navigation-drawer>

    <!-- Go to the url /order (the pages "Price", "LoginWindow") -->
    <router-view></router-view>

</v-app>
</template>

<script>
import ContentMap from '../components/ContentMap.vue'
import LeftMenu from '../components/LeftMenu.vue'
import RightMenu from '../components/Order.vue'
import BaseFooter from '../components/Footer.vue'

export default {
    name: 'Home',

    components: {
        ContentMap, LeftMenu, RightMenu, BaseFooter
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
