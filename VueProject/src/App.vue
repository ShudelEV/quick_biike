<template>
<v-app>
    <v-navigation-drawer
        fixed
        :mini-variant="miniVariant"
        :clipped="clipped"
        v-model="drawer"
        app
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

    <content-map></content-map>

    <v-navigation-drawer
        fixed
        :clipped="!clipped"
        right
        v-model="rightDrawer"
        app
        class="yellow accent-1"
    >

        <right-menu></right-menu>

    </v-navigation-drawer>

    <!--<base-footer></base-footer>-->

</v-app>
</template>

<script>
import ContentMap from './components/ContentMap.vue'
import LeftMenu from './components/LeftMenu.vue'
import RightMenu from './components/Order.vue'
import BaseFooter from './components/Footer.vue'

export default {
    components: {
        ContentMap, LeftMenu, RightMenu, BaseFooter
    },
    data () {
        return {
            clipped: true,
            drawer: false,
            fixed: false,
            miniVariant: true,
            rightDrawer: true,
            title: 'QuickBike'
        }
    }
}
</script>
