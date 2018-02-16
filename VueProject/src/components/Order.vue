<template>
    <!--Create a form-->
    <!--Evoke getShops() method when button "Confirm" is clicked-->
<v-form
    v-model="valid"
    ref="form"
    lazy-validation
>
<v-card>
    <v-card-title
    class="yellow accent-1 pa-4 title"
    > Create order </v-card-title>

    <v-container fluid>
        <v-layout row wrap>
            <!-- V-model is value for the children component, that will be updated $emit('input', value) -->
            <date-time-picker-from v-model="date_time_from"></date-time-picker-from>
            <date-time-picker-to v-model="date_time_to"></date-time-picker-to>

            <v-container fluid pa-0>
                <v-subheader> BikeQuantity </v-subheader>
                <v-layout raw wrap>
                    <v-flex xs4 v-for="bike in bikes" :key="bike.type">
                        <!--Transfer all args of bike to child component-->
                        <order-check-box
                            :value="bike.checked_default"
                            :icon="bike.icon"
                            :quantity="bike.quantity"
                            @input="value => {bike.checked_default = value}"
                        ></order-check-box>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-layout>
    </v-container>

    <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="clear">clear</v-btn>
        <v-btn @click="submit" :disabled="!valid">submit</v-btn>
    </v-card-actions>
</v-card>
</v-form>
</template>

<script>
import DateTimePickerFrom from './DateTimePickerFrom.vue'
import DateTimePickerTo from './DateTimePickerTo.vue'
import OrderCheckBox from './OrderCheckBox.vue'

export default {
    components: {
        DateTimePickerFrom, DateTimePickerTo, OrderCheckBox
    },

    data: () => ({
        valid: true,
        date_time_from: null,
        date_time_to: null,
        bikes: [
            //            Type: Man
            { checked_default: true, quantity: 1, icon: 'face' },
            //            Type: Woman
            { checked_default: false, quantity: 0, icon: 'pregnant_woman' },
            //            Type: Child
            { checked_default: false, quantity: 0, icon: 'child_care' }
        ]
//        form: {
//            bike_is_free: {
//                date_time_from: null,
//                date_time_to: null
//            },
//            bikes: [
//                { type: 'man', quantity: 1 },
//                { type: 'woman', quantity: 0 },
//                { type: 'child', quantity: 0 }
//            ]
//        }
    }),

    methods: {
        clear () {
            this.$refs.form.reset()
        },

        submit () {
            if (this.$refs.form.validate()) {
                console.log('bike is free = ', this.bikes)
            }
        },

        getShops: function () {
            console.log()
        }
    }
}
</script>
