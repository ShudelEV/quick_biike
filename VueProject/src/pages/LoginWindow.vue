<template>
<v-dialog v-model="showDialog"
              max-width="500px"
              persistent>
    <v-form ref="form" v-model="valid" lazy-validation>
        <v-card class="elevation-12">
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn icon @click.native="goBack()">
                    <v-icon>close</v-icon>
                </v-btn>
            </v-card-actions>
            <v-card-text>
                <v-text-field class="input-group--focused"
                    v-model="loginName"
                    prepend-icon="face"
                    :rules="loginRules"
                    :counter="20"
                    label="Login"
                    required
                ></v-text-field>

                <v-text-field class="input-group--focused" color="green"
                    v-model="phone"
                    prepend-icon="phone"
                    prefix="+375"
                    mask=" (##) #######"
                    :rules="phoneRules"
                    label="Enter your phone number"
                    required
                ></v-text-field>

                <v-text-field class="input-group--focused" color="red"
                    v-model="password"
                    prepend-icon="fingerprint"
                    :rules="passwordRules"
                    :append-icon="e1 ? 'visibility' : 'visibility_off'"
                    :append-icon-cb="() => (e1 = !e1)"
                    :type="e1 ? 'password' : 'text'"
                    name="input-10-1"
                    label="Enter your password"
                    hint="At least 8 characters"
                    min="8"
                    :counter="20"
                    required
                ></v-text-field>
            </v-card-text>

            <v-card-actions>
                <v-btn outline color="red"
                       @click.prevent="clear()"
                >clear</v-btn>
                <v-spacer></v-spacer>
                <v-btn outline color="green"
                       :disabled="!valid"
                       @click.prevent="register()"
                >register</v-btn>
            </v-card-actions>
        </v-card>
    </v-form>
</v-dialog>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Login',

    data () {
        return {
            showDialog: true,
            valid: true,
            e1: true,

            loginName: '',
            loginRules: [
              v => !!v || 'Login is required',
              v => (v && v.length <= 25) || 'Login must be less than 20 characters'
            ],
            password: '',
            passwordRules: [
              v => !!v || 'Password is required',
              v => (v && v.length > 8) || 'Password must be more than 8 characters',
              v => /^/.test(v) || 'Password must be valid'
            ],
            phone: '',
            phoneRules: [
              v => !!v || 'Phone number is required',
              v => /^/.test(v) || 'Phone number must be valid'
            ],
            checkbox: false
        }
    },

    methods: {
        login () {
            if (this.$refs.form.validate()) {
                this.$auth.login({ email, password }).then(function () {
                    axios.post('/api/auth', {
                    login: this.login,
                    phone: this.phone,
                    password: this.password
                })
            })
            }
        },

        register () {
            this.$auth.register({ name, email, password }).then(function () {

            })
        },

        // Social account authentication
        authenticate (provider) {
            this.$auth.authenticate(provider).then(function () {

            })
        },

        clear () {
            this.$refs.form.reset()
        },

        goBack () {
            window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
        },
    }
}
</script>
