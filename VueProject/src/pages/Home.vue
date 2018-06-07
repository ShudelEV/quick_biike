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
        <v-dialog content-class="order"
                  v-model="rightDrawer"
                  hide-overlay persistent
                  max-width="420px"
        >
            <order></order>
        </v-dialog>
         <!--Go to the url /order (the pages "Price", "LoginWindow") -->
        <router-view></router-view>
    </div>
</template>

<script>
import ContentMap from '../components/ContentMap.vue'
import LeftMenu from '../components/LeftMenu.vue'
import Order from '../components/Order.vue'

export default {
    name: 'Home',

    components: {
        ContentMap, LeftMenu, Order
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
    }
</style>
