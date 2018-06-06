<template>
<v-app>
    <v-toolbar id="toolbar" app :clipped-left="clipped" color="lime accent-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <!--<v-btn icon @click.stop="clipped = !clipped">-->
            <!--<v-icon>web</v-icon>-->
        <!--</v-btn>-->
        <v-toolbar-title v-text="title"></v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn flat
               v-if="!user.loggedIn"
               :to="{ name: 'Login' }"
        >
            login
        </v-btn>
        <v-btn flat icon
               v-if="!user.loggedIn"
               @click="signInGoogle"
               title="Sig in with Google"
        >
            <v-icon>public</v-icon>
        </v-btn>
        <div v-if="user.loggedIn">Hello, {{currentUserName || currentUserEmail}}</div>

        <v-btn flat
               v-if="user.loggedIn"
               @click="signOut"
               :title="currentUserName"
        > signout </v-btn>
        <v-btn icon @click.stop="rightDrawer = !rightDrawer">
            <v-icon v-html="rightDrawer ? 'chevron_right' : 'chevron_left'"></v-icon>
        </v-btn>
    </v-toolbar>

    <v-content>
        <v-container fluid pa-0>
            <!-- pages/Home -->
            <router-view
                :clipped="clipped"
                :drawer="drawer"
                :rightDrawer="rightDrawer"
            ></router-view>
        </v-container>
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

import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'App',

    components: { BaseFooter, },

    data () {
        return {
            clipped: true,
            drawer: false,
            rightDrawer: true,
            title: 'QuickBike',
            name: ''
        }
    },

    computed: mapGetters(['user', 'currentUserName', 'currentUserEmail']),

    methods: {
        ...mapActions(['signInGoogle', 'signOut'])
    }
}
</script>
