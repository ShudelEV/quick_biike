<template>
<v-app>
    <!--<v-toolbar id="toolbar" app :clipped-left="clipped" color="lime accent-3">-->
        <!--<v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>-->
        <!--&lt;!&ndash;<v-btn icon @click.stop="clipped = !clipped">&ndash;&gt;-->
            <!--&lt;!&ndash;<v-icon>web</v-icon>&ndash;&gt;-->
        <!--&lt;!&ndash;</v-btn>&ndash;&gt;-->
        <!--<v-toolbar-title v-text="title"></v-toolbar-title>-->
        <!--<v-btn icon @click.stop="rightDrawer = !rightDrawer">-->
            <!--<v-icon v-html="rightDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>-->
        <!--</v-btn>-->
    <!--</v-toolbar>-->

    <v-content>
        <!-- pages/Home -->
        <router-view
            :clipped="clipped"
            :drawer="drawer"
            :rightDrawer="rightDrawer"
        ></router-view>
    </v-content>

    <!--<v-footer app :fixed="true"-->
        <!--color="lime accent-4"-->
        <!--height="32"-->
    <!--&gt;-->
        <!--<v-spacer></v-spacer>-->
        <!--<span>&copy; 2018</span>-->
    <!--</v-footer>-->
</v-app>
</template>

<script>
import BaseFooter from './components/Footer.vue'

export default {
    name: 'App',

    components: { BaseFooter, },

    data () {
        return {
            clipped: true,
            drawer: false,
            rightDrawer: true,
            title: 'QuickBike'
        }
    }
}
</script>
