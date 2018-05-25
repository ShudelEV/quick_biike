<template>
<v-app>

    <v-toolbar fixed app :clipped-left="clipped"  color="lime accent-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <!--<v-btn icon @click.stop="clipped = !clipped">-->
            <!--<v-icon>web</v-icon>-->
        <!--</v-btn>-->
        <v-toolbar-title v-text="title"></v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn flat icon  :to="{ name: 'Login' }">
            <v-icon>account_circle</v-icon>
        </v-btn>
        <v-btn icon @click.stop="rightDrawer = !rightDrawer">
            <v-icon v-html="rightDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>
        </v-btn>
    </v-toolbar>

    <!-- pages/Home -->
    <router-view
        :clipped="clipped"
        :drawer="drawer"
        :rightDrawer="rightDrawer"
    ></router-view>

    <!--<base-footer></base-footer>-->

</v-app>
</template>

<script>

export default {
    name: 'App',

    components: {
    },

    data () {
        return {
            clipped: true,
            drawer: false,
            rightDrawer: true,
            title: 'QuickBike',
        }
    }
}
</script>
