<template>
<v-container fluid pa-2>
<v-layout column fill-height>
    <v-flex xs1 md1 fill-height>
        <v-layout row align-center>
            <v-spacer></v-spacer>
            <!--SignIn with E-mail button-->
            <v-btn class="white" round
                   v-if="!user.loggedIn"
                   :to="{ name: 'Login' }"
                   title="Login with e-mail"
            > login </v-btn>
            <!--Google SignIn button-->
            <v-btn fab color="white" small
                   :loading="loading"
                   :disabled="loading"
                   v-if="!user.loggedIn"
                   @click.native="signInGoogle(); loader = 'loading'"
                   title="Sign in with Google"
            >
                <!--<span slot="loader" class="custom-loader">-->
                <v-avatar size="28px">
                    <img src="https://madeby.google.com/static/images/google_g_logo.svg">
                </v-avatar>
                <!--</span>-->
            </v-btn>
            <!--Profile button-->
            <v-speed-dial
                v-model="fab"
                direction="bottom"
                open-on-hover
            >
                <v-btn fab
                       color="cyan"
                       slot="activator"
                       v-model="fab"
                       v-if="user.loggedIn"
                       :title="currentUserName || currentUserEmail"
                >
                    <v-avatar v-if="user.photoURL" size="56px">
                        <img :src="user.photoURL">
                    </v-avatar>
                    <v-icon v-else>account_circle</v-icon>
                    <v-icon>close</v-icon>
                </v-btn>
                <v-btn fab dark medium
                       color="blue darken-0"
                       title="Account"
                       :to="{ name: 'Account' }"
                >
                    <v-icon>account_circle</v-icon>
                </v-btn>
                <v-btn fab dark small
                       color="green"
                       title="SignOut"
                       @click.native="signOut()"
                >
                    <v-icon>exit_to_app</v-icon>
                </v-btn>
            </v-speed-dial>
            <!--<v-btn class="green accent-4" round-->
                   <!--v-if="user.loggedIn"-->
                   <!--@click="signOut"-->
                   <!--:title="currentUserName"-->
            <!--&gt; signout </v-btn>-->
        </v-layout>
    </v-flex>
    <v-flex xs2 md2 fill-height></v-flex>
</v-layout>
</v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'ToolBar',

    data () {
        return {
            loader: null,
            loading: false,
            fab: false,
//            name: ''
        }
    },

    watch: {
        loader () {
            const l = this.loader;
            this[l] = !this[l];
            setTimeout(() => (this[l] = false), 3000);
            this.loader = null
        }
    },

    computed: mapGetters(['user', 'currentUserName', 'currentUserEmail']),

    methods: {
        ...mapActions(['signInGoogle', 'signOut'])
    }
}
</script>

<style>
.custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
</style>
