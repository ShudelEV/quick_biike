<template>
    <v-dialog v-model="showDialog"
              max-width="700px"
              persistent

    >
        <v-card class="elevation-12">
            <v-card-title>
                <span class="headline">{{id}}</span>
            </v-card-title>
            <v-card-text>{{dt_from}}</v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" flat @click.native="goBack()">Close</v-btn>
                <v-btn color="blue darken-1" flat @click.native="">Save</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        data () {
            return {
                showDialog: true,
            }
        },

        props: {
            id: {
                type: Number,
                default: 0
            },
            dt_from: {
                type: String,
                default: ''
            },
            dt_to: {
                type: String,
                default: ''
            }
        },

        methods: {
            goBack () {
                window.history.length > 1
                ? this.$router.go(-1)
                : this.$router.push('/')
            }
        }
    }
</script>
