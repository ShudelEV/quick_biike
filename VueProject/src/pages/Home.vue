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
<v-card flat>
    <content-map></content-map>
    <v-container fluid grid-list-md style="height: 100vh; overflow-y: scroll">
        <v-layout column fill-height>
            <v-flex xs3 md3>
                <v-layout row>
                    <!--Search menu-->
                    <v-flex xs12 sm6 md4>
                        <search-menu @show-shop-list="showShopList = true"></search-menu>
                    </v-flex>
                    <!--Toolbar-->
                    <v-flex xs12 sm6 md8>
                        <tool-bar></tool-bar>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex xs9 md9 wrap>
                <v-layout row>
                    <v-flex xs12 sm6 md4>
                        <!--List of Shops-->
                        <div v-if="showShopList">
                            <shop-list
                                v-for="shop in shops.all" :key="shop.id"
                                :shop="shop"
                                :dateTimeFrom="shops.dateTimeFrom"
                                :dateTimeTo="shops.dateTimeTo"
                                :period="shops.period"
                                :bikesTypeQty="shops.bikesTypeQty"
                            >
                            </shop-list>
                        </div>
                    </v-flex>
                    <v-flex xs12 sm6 md8 d-flex>
                        <!--Go to the url /order (the pages "Price", "LoginWindow") -->
                        <router-view></router-view>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
    </v-container>
</v-card>
</template>

<script>
import ContentMap from '../components/ContentMap.vue'
import LeftMenu from '../components/LeftMenu.vue'
import SearchMenu from '../components/SearchMenu.vue'
import ShopList from '../components/ShopList.vue'
import ToolBar from '../components/ToolBar.vue'

import { mapState } from 'vuex'

export default {
    name: 'Home',

    components: {
        ContentMap, LeftMenu, SearchMenu, ShopList, ToolBar
    },

    props: ['clipped', 'drawer', 'rightDrawer'],

    created () {
        // get shops when the index page starts
        this.$store.dispatch('getAllShops')
    },

    data () {
        return {
            fixed: false,
            miniVariant: false,
            title: 'QuickBike',
            // The list of shops
            showShopList: false
        }
    },

    computed: {
        ...mapState({
            shops: state => state.shops
        }),
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
