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

                        <v-text-field class="input-group--focused" color="blue"
                            v-model="phone"
                            prepend-icon="phone"
                            prefix="+375"
                            mask=" (##) #######"
                            :rules="phoneRules"
                            label="Enter phone number"
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
                    </v-card-text>
                    <v-card-text>
                        <v-avatar title="vk" color="grey" tile>
                            <img src="/static/images/vk_icon.svg" alt="">
                        </v-avatar>
                        <v-avatar title="facebook" color="grey" tile>
                            <img src="/static/images/facebook_icon.svg" alt="">
                        </v-avatar>
                        <v-avatar title="twitter" color="grey" tile>
                            <img src="/static/images/twitter_icon.svg" alt="">
                        </v-avatar>
                    </v-card-text>

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

        <v-tab-item id="reg">
            <v-card class="elevation-12">
                <v-form ref="formReg" v-model="valid" lazy-validation>
                    <v-card-text>

                        <v-text-field class="input-group--focused" color="blue"
                            v-model="phone"
                            prepend-icon="phone"
                            prefix="+375"
                            mask=" (##) #######"
                            :rules="phoneRules"
                            label="Enter phone number"
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
                               @click.prevent="register()"
                        >register</v-btn>
                    </v-card-actions>
                </v-form>
            </v-card>
        </v-tab-item>

    </v-tabs-items>
</v-dialog>
</template>

<script>
export default {
    name: 'Login',

    data () {
        return {
            showDialog: true,
            model: 'log',
            valid: true,
            e1: true,
            e2: true,

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
            ],
            checkbox: false,
            error: null
        }
    },

    methods: {
        login () {
            if (this.$refs.formLog.validate()) {
                this.$auth.login({ phone: this.phone, password: this.password })
                    .then(request => this.loginSuccessful(request))
                    .catch(() => this.loginFailed())
            }
        },

        loginSuccessful (req) {
            if (!req.data.token) {
                this.loginFailed();
                return
            }

            localStorage.token = req.data.token;
            this.error = false;

            this.$router.replace(this.$route.query.redirect || '/account')
        },

        loginFailed () {
            this.error = 'Login failed!';
            delete localStorage.token
        },

        register () {
            if (this.$refs.formReg.validate()) {
                this.$auth.register({ phone: this.phone, password: this.password }).then(function () {

                })
            }
        },

        // Social account authentication
        authenticate (provider) {
            this.$auth.authenticate(provider).then(function () {

            })
        },

        goBack () {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
        },
    }
}
</script>
