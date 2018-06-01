<template>
<v-dialog v-model="showDialog"
              max-width="500px"
              persistent>

    <v-toolbar color="cyan" dark tabs>
        <v-tabs  color="cyan" v-model="model" slider-color="yellow">
            <v-tab href="#log"> Login </v-tab>
            <v-tab href="#reg"> Register </v-tab>
        </v-tabs>
        <v-spacer></v-spacer>
        <v-btn icon @click.native="goBack()">
            <v-icon>close</v-icon>
        </v-btn>
    </v-toolbar>

    <v-tabs-items v-model="model">
        <!--Login window-->
        <v-tab-item id="log">
            <v-card class="elevation-12">
                <v-form ref="formLog" v-model="valid" lazy-validation>
                    <v-card-text>
                        <!--<v-text-field class="input-group&#45;&#45;focused"-->
                            <!--v-model="loginName"-->
                            <!--prepend-icon="face"-->
                            <!--:rules="loginRules"-->
                            <!--:counter="20"-->
                            <!--label="Login"-->
                            <!--required-->
                        <!--&gt;</v-text-field>-->

                        <v-text-field class="input-group--focused"
                            v-model="email"
                            prepend-icon="email"
                            :rules="emailRules"
                            label="E-mail"
                            required
                        ></v-text-field>

                        <!--<v-text-field class="input-group&#45;&#45;focused" color="blue"-->
                            <!--v-model="phone"-->
                            <!--prepend-icon="phone"-->
                            <!--prefix="+375"-->
                            <!--mask=" (##) #######"-->
                            <!--:rules="phoneRules"-->
                            <!--label="Enter phone number"-->
                            <!--required-->
                        <!--&gt;</v-text-field>-->

                        <v-text-field class="input-group--focused" color="green"
                            v-model="password"
                            prepend-icon="fingerprint"
                            :rules="passwordRules"
                            :append-icon="e1 ? 'visibility' : 'visibility_off'"
                            :append-icon-cb="() => (e1 = !e1)"
                            :type="e1 ? 'password' : 'text'"
                            name="input-10-1"
                            label="Enter password"
                            hint="At least 8 characters"
                            min="8"
                            :counter="20"
                            required
                        >
                        </v-text-field>
                    </v-card-text>
                    <!-- Error message -->
                    <v-card-title class="error"
                                  v-if="error.errorMessage"
                    > {{ error.errorMessage }} </v-card-title>

                    <!--<v-card-text>-->
                        <!--<v-avatar title="vk" color="grey" tile>-->
                            <!--<img src="/static/images/vk_icon.svg" alt="">-->
                        <!--</v-avatar>-->
                        <!--<v-avatar title="facebook" color="grey" tile>-->
                            <!--<img src="/static/images/facebook_icon.svg" alt="">-->
                        <!--</v-avatar>-->
                        <!--<v-avatar title="twitter" color="grey" tile>-->
                            <!--<img src="/static/images/twitter_icon.svg" alt="">-->
                        <!--</v-avatar>-->
                    <!--</v-card-text>-->

                    <v-card-actions>
                        <v-btn outline color="red"
                               @click.prevent="$refs.formLog.reset()"
                        >
                            <v-icon>delete</v-icon>
                            clear
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn outline color="green"
                               :disabled="!valid"
                               @click.prevent="login()"
                        >login</v-btn>
                    </v-card-actions>

                </v-form>
            </v-card>
        </v-tab-item>
        <!--Registration window-->
        <v-tab-item id="reg">
            <v-card class="elevation-12">
                <v-form ref="formReg" v-model="valid" lazy-validation>
                    <v-card-text>

                        <!--<v-text-field class="input-group&#45;&#45;focused" color="blue"-->
                            <!--v-model="phone"-->
                            <!--prepend-icon="phone"-->
                            <!--prefix="+375"-->
                            <!--mask=" (##) #######"-->
                            <!--:rules="phoneRules"-->
                            <!--label="Enter phone number"-->
                            <!--required-->
                        <!--&gt;</v-text-field>-->

                        <v-text-field class="input-group--focused"
                            v-model="email"
                            prepend-icon="email"
                            :rules="emailRules"
                            label="E-mail"
                            required
                        ></v-text-field>

                        <v-text-field class="input-group--focused" color="green"
                            v-model="password"
                            prepend-icon="fingerprint"
                            :rules="passwordRules"
                            :append-icon="e1 ? 'visibility' : 'visibility_off'"
                            :append-icon-cb="() => (e1 = !e1)"
                            :type="e1 ? 'password' : 'text'"
                            name="input-10-1"
                            label="Enter password"
                            hint="At least 8 characters"
                            min="8"
                            :counter="20"
                            required
                        ></v-text-field>

                        <v-text-field class="input-group--focused" color="green"
                            v-if="password"
                            v-model="password2"
                            prepend-icon="fingerprint"
                            :rules="passwordRules2"
                            :append-icon="e2 ? 'visibility' : 'visibility_off'"
                            :append-icon-cb="() => (e2 = !e2)"
                            :type="e2 ? 'password' : 'text'"
                            name="input-10-2"
                            label="Repeat password"
                            hint="At least 8 characters"
                            min="8"
                            :counter="20"
                            required
                        ></v-text-field>
                    </v-card-text>
                    <!-- Error message -->
                    <v-card-title class="error"
                                  v-if="error.errorMessage"
                    > {{ error.errorMessage }} </v-card-title>

                    <v-card-actions>
                        <v-btn outline color="red"
                               @click.prevent="$refs.formReg.reset()"
                        >
                            <v-icon>delete</v-icon>
                            clear
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn outline color="green"
                               :disabled="!valid"
                               @click="register()"
                        >register</v-btn>
                    </v-card-actions>
                </v-form>
            </v-card>
        </v-tab-item>

    </v-tabs-items>
</v-dialog>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'Login',

    mounted() {
//        console.log(this.$refs.password)
    },

    data () {
        return {
            showDialog: true,
            model: 'log',
            valid: true,
            e1: true,
            e2: true,

            email: '',
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
            ],
            loginName: '',
            loginRules: [
                v => !!v || 'Login is required',
                v => (v && v.length <= 25) || 'Login must be less than 20 characters'
            ],
            password: '',
            password2: '',
            passwordRules: [
                v => !!v || 'Password is required',
                v => (v && v.length >= 8) || 'Password must be at least 8 characters',
                v => /^/.test(v) || 'Password must be valid'
            ],
            passwordRules2: [
                v => !!v || 'Password is required',
                v => (v === this.password) || 'Password must be equal',
            ],
            phone: '',
            phoneRules: [
                v => !!v || 'Phone number is required',
                v => (v && v.length >= 9) || 'Phone number must be 7 characters'
            ]
        }
    },

    computed: {
        ...mapGetters(['error'])
    },

    methods: {
        login () {
            if (this.$refs.formLog.validate()) {
                this.$store.dispatch('signInWithEmailAndPassword', {
                    email: this.email,
                    password: this.password,
                    // go back if login is OK
                    result: () => { this.goBack() }
                })
            }
        },

        register () {
            if (this.$refs.formReg.validate()) {
                this.$store.dispatch('registerWithEmailAndPassword', {
                    email: this.email,
                    password: this.password,
                    // go back if register is OK
                    result: () => { this.goBack() }
                })
            }
        },

        goBack () {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
        },
    }
}
</script>
