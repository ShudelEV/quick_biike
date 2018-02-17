<template>
    <!--Create a form-->
    <!--Evoke getShops() method when button "Confirm" is clicked-->
<v-form
    ref="form"
    v-model="valid"
    lazy-validation
>
<v-card>
    <v-card-title
    class="yellow accent-1 pa-4 title"
    > Create order </v-card-title>

    <v-container fluid>
        <v-layout row wrap>
            <!-- Catch date and time from DateTimePickerFrom -->
            <date-time-picker-from
                :date="dateTo" :time="timeTo"
                @input="(date, time) => {this.dateTo = date, this.timeTo = time}"
            ></date-time-picker-from>
            <!-- Throw date and time to DateTimePickerTo -->
            <date-time-picker-to
                :dateTo="dateTo" :timeTo="timeTo"
            ></date-time-picker-to>

            <v-container fluid pa-0>
                <v-subheader> BikeQuantity </v-subheader>
                <v-layout raw wrap>
                    <v-flex xs4 v-for="bike in bikes" :key="bike.type">
                        <!--Transfer default args of bike to child component-->
                        <order-check-box
                            v-bind="bike"
                            @input="checked_default => {bike.checked_default = checked_default}"
                        ></order-check-box>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-layout>
    </v-container>

    <v-card-actions>
        <v-spacer></v-spacer>
        <!--<v-btn @click="clear">clear</v-btn>-->
        <v-btn @click="getShops" :disabled="!valid">Confirm</v-btn>
    </v-card-actions>
</v-card>
</v-form>
</template>

<script>
import DateTimePickerFrom from './DateTimePickerFrom.vue'
import DateTimePickerTo from './DateTimePickerTo.vue'
import OrderCheckBox from './OrderCheckBox.vue'

import axios from 'axios'

export default {
    components: {
        DateTimePickerFrom, DateTimePickerTo, OrderCheckBox
    },

    data: () => ({
        valid: true,
        dateTo: null,
        timeTo: null,
        bikes: [
            //            Type: Man
            { type: 'man', checked_default: true, quantity: 1, icon: 'face' },
            //            Type: Woman
            { type: 'woman', checked_default: false, quantity: 0, icon: 'pregnant_woman' },
            //            Type: Child
            { type: 'child', checked_default: false, quantity: 0, icon: 'child_care' }
        ]
    }),

    methods: {
        clear () {
            this.$refs.form.reset()
        },

        getShops () {
            if (this.$refs.form.validate()) {
                let inputs = this.$refs.form.inputs;
                this.date_time_from = inputs[0].value + 'T' + inputs[1].value;
                this.date_time_to = inputs[2].value + 'T' + inputs[3].value;
                let form = {
                    bike_is_free: {
                        date_time_from: this.date_time_from,
                        date_time_to: this.date_time_to
                    },
                    bikes:
                        {'man': inputs[5].inputValue},
                        // {type: 'woman', quantity: inputs[7].inputValue},
                        // {type: 'child', quantity: inputs[9].inputValue},

                };
                console.log('form = ', form);
                // axios({
                //     method: 'get',
                //     url: '/api-auth/login/',
                //     auth: {
                //         username: 'quickbike_admin',
                //         password: 'velik5000admin'
                //     }
                // }).then(function(response){console.log(response)});

                axios.post(
                    '/api/readShops/',
                    // Request Data in JSON format
                    JSON.stringify({'form': form}),
                    // Axios Configuration
                    {headers: {
                        'Content-Type': 'application/json'
                    }},
                    // {auth: {username: 'quickbike_admin', password: 'velik5000admin'}}
                ).then(function(response){console.log(response)})
            }
        }
    }
}
</script>
