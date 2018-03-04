<template>
<div>
    <!--Create a form-->
    <!--Evoke getShops() method when a value of order is changed-->
<v-form
    ref="form"
    v-model="valid"
    lazy-validation
>
<v-card>
    <v-toolbar class="lime accent-2">
        <v-toolbar-title>
            Create order
        </v-toolbar-title>
    </v-toolbar>
    <v-container fluid>
        <v-layout row wrap>
            <!-- Catch date and time from DateTimePickerFrom -->
            <date-time-picker-from
                @input="(date, time) => {
                    setDateTimeTo(date, time);
                    this.dateTimeFrom = date + 'T' + time;
                }"
            ></date-time-picker-from>
            <!-- Throw date and time to DateTimePickerTo -->
            <!-- And catch date and time from DateTimePickerTo -->
            <date-time-picker-to
                :actDateTo="actDateTo"
                :actTimeTo="actTimeTo"
                :activeDateTimeTo="activeDateTimeTo"
                @input="(date, time) => {
                    this.dateTimeTo = date + 'T' + time;
                }"
            ></date-time-picker-to>

            <v-container fluid pa-0>
                <v-subheader> BikeQuantity </v-subheader>
                <v-layout raw wrap>
                    <v-flex xs4 v-for="bike in bikes" :key="bike.type">
                        <!--Transfer default args of bike to child component-->
                        <order-check-box
                            v-bind="bike"
                            @input="(checked_default, quantity) => {
                                bike.checked_default = checked_default;
                                bike.quantity = quantity;
                                getShops();
                            }"
                        ></order-check-box>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-layout>
    </v-container>

    <v-card-actions>
        <v-spacer></v-spacer>
        <!--<v-btn @click="clear">clear</v-btn>-->
        <v-btn @click="listOfShopsActive = !listOfShopsActive" :disabled="!valid">Confirm</v-btn>
    </v-card-actions>
</v-card>
</v-form>

    <!-- List of Shops appears after clicking the button  -->
<v-list :hidden="!listOfShopsActive">
<list-of-shops
    :key="shop.id"
    v-for="shop in shops"
    :shop="shop"
>
</list-of-shops>
</v-list>
</div>
</template>

<script>
import DateTimePickerFrom from './DateTimePickerFrom.vue'
import DateTimePickerTo from './DateTimePickerTo.vue'
import OrderCheckBox from './OrderCheckBox.vue'
import ListOfShops from './ListOfShops.vue'

export default {
    name: 'Order',

    components: {
        DateTimePickerFrom, DateTimePickerTo, OrderCheckBox, ListOfShops
    },

    data: () => ({
        valid: true,
        // actDateTo, actTimeTo - for activate dateTimeTo field
        actDateTo: null,
        actTimeTo: null,
        // dateTimeFrom, dateTimeTo - for update the list of shops on the map
        dateTimeFrom: (new Date()).toISOString().slice(0, 16),
        dateTimeTo: null,
        bikes: [
            //            Type: Man
            { type: 'man', checked_default: false, quantity: 1, icon: 'face' },
            //            Type: Woman
            { type: 'woman', checked_default: false, quantity: 1, icon: 'pregnant_woman' },
            //            Type: Child
            { type: 'child', checked_default: false, quantity: 1, icon: 'child_care' }
        ],
        listOfShopsActive: false,
        shops: []
    }),

    computed: {
        // Activate DateTimePickerTo after a picking TimeFrom
        activeDateTimeTo: function () {
            return this.actTimeTo ? true : false
        }
    },

    watch: {
        dateTimeFrom: function (val) {
            // if time is not picked - set 00:00
            if (val.slice(11) == 'null') {
                this.dateTimeFrom = val.slice(0, 10) + 'T00:00'
            }
            this.getShops()
        },
        dateTimeTo: function (val) {
            // if time is not picked - set actTimeTo
            if (val.slice(11) == 'null') {
                this.dateTimeTo = val.slice(0, 11) + this.actTimeTo
            }
            this.getShops()
        },
    },

    methods: {
        clear () {
            this.$refs.form.reset()
        },

        getShops () {
            let bikesSet = [];
            let i = 1;
            for (let bike of this.bikes) {
                if (bike.checked_default) {
                    bikesSet.push({type: i, quantity: bike.quantity})
                }
                i += 1
            }
            // emit event to update the list of shops in ContentMap
            this.$bus.$emit('setShopsOnMap', this.dateTimeFrom, this.dateTimeTo, bikesSet)
        },

        setDateTimeTo (date, time) {
            // Set +1 hours (rent for at least 1 hour)
            let h = 0, m = 0;
            let resDate = date;

            if (time) {
                h = Number(time.slice(0, 2));
                m = Number(time.slice(3));

                if (h == 23) {
                    h = 0;
                    // Set dateTo +1 day, if h = 23.
                    let tomorrow = new Date(date);
                    tomorrow.setDate(tomorrow.getDate() + 1);
                    resDate = tomorrow.toISOString().slice(0, 10);
                }
                else {
                    h += 1
                }

                this.actDateTo = resDate;
                this.actTimeTo = h + ':' + m;
            }
        }
    }
}
</script>
