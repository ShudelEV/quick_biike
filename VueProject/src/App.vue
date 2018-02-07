<template>
<v-app>
    <v-navigation-drawer
        fixed
        :mini-variant="miniVariant"
        :clipped="clipped"
        v-model="drawer"
        app
    >

        <LeftMenu/>

    </v-navigation-drawer>
    <v-toolbar fixed app :clipped-left="clipped">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-btn icon @click.stop="miniVariant = !miniVariant">
            <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'"></v-icon>
        </v-btn>
        <v-btn icon @click.stop="clipped = !clipped">
            <v-icon>web</v-icon>
        </v-btn>
        <v-toolbar-title v-text="title"></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click.stop="rightDrawer = !rightDrawer">
            <v-icon>menu</v-icon>
        </v-btn>
    </v-toolbar>

    <Content/>

    <v-navigation-drawer
        temporary
        :right="right"
        v-model="rightDrawer"
        fixed
    >
        <v-list>
            <v-list-tile @click.native="right = !right">

                <Order/>

            </v-list-tile>
        </v-list>
    </v-navigation-drawer>

    <Footer/>

</v-app>
</template>

<script>
import Content from './components/Content.vue'
import LeftMenu from './components/LeftMenu.vue'
import Order from './components/Order.vue'
import Footer from './components/Footer.vue'

export default {
    components: {
        Content, LeftMenu, Order, Footer
    },
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  }
}
</script>
