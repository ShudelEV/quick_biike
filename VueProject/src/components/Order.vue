<template>
    <!--Create a form-->
    <!--Evoke getShops() method when button "Confirm" is clicked-->
<form @submit.prevent="getShops">
<v-card>
    <v-card-title
    class="yellow accent-1 pa-4 title"
    > Create order </v-card-title>

    <v-container fluid>
        <v-layout row wrap>
            <date-time-picker-from v-model="form.bike_is_free.date_time_from"></date-time-picker-from>
            <date-time-picker-to></date-time-picker-to>
            <order-check-box></order-check-box>
        </v-layout>
    </v-container>

    <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn flat color="primary" type="submit">Confirm</v-btn>
    </v-card-actions>
</v-card>
</form>
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
        form: {
            bike_is_free: {
                date_time_from: null,
                date_time_to: null
            },
            bikes: []
        }
    }),

    methods: {
        getShops: function () {
            console.log('bike is free = ', this.form.bike_is_free.date_time_from)
        }
    }
}
</script>
