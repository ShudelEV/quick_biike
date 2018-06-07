<template>
    <!--Create a form-->
    <!--Evoke getShops() method when a value of order is changed-->
<v-card>
    <v-form ref="form" v-model="valid" lazy-validation>
        <v-container fluid>
            <v-layout row justify-space-around>
                <!-- Catch date and time from DateTimePickerFrom -->
                <!--<date-time-picker-from-->
                    <!--@input="(date, time) => {-->
                        <!--setDateTimeTo(date, time);-->
                        <!--this.dateTimeFrom = date + 'T' + time;-->
                    <!--}"-->
                <!--&gt;</date-time-picker-from>-->

                <!--Variant #1 for DateTimePickerTo-->
                <!-- Throw date and time to DateTimePickerTo -->
                <!-- And catch date and time from DateTimePickerTo -->
                <!--<date-time-picker-to-->
                    <!--:actDateTo="actDateTo"-->
                    <!--:actTimeTo="actTimeTo"-->
                    <!--:activeDateTimeTo="activeDateTimeTo"-->
                    <!--@input="(date, time) => {-->
                        <!--this.dateTimeTo = date + 'T' + time;-->
                    <!--}"-->
                <!--&gt;</date-time-picker-to>-->

                <!--DateFrom Picker-->
                <v-flex xs4>
                    <v-menu
                        lazy
                        :close-on-content-click="true"
                        v-model="dateFromMenu"
                        transition="scale-transition"
                        offset-y
                        full-width
                        :nudge-right="40"
                        max-width="285px"
                        min-width="285px"
                    >
                        <v-text-field
                            id="date_from"
                            slot="activator"
                            label="From Time:"
                            v-model="dateFrom"
                            :rules="[v => !!v || 'Date is required']"
                            prepend-icon="event"
                            readonly
                            required
                        ></v-text-field>
                        <!--Change action: appear the TimePicker after
                            and set min, date in DateTimePickerTo (through parent component)-->
                        <v-date-picker
                            v-model="dateFrom"
                            @change="timeFromMenu = !timeFromMenu"
                            no-title
                            scrollable
                            :min="(new Date()).toISOString().slice(0, 10)"
                            :allowed-dates="allowedDates"
                        >
                        </v-date-picker>
                    </v-menu>
                </v-flex>
                <!--TimeFrom Picker-->
                <v-flex xs2>
                    <v-menu
                        ref="timeFromMenu"
                        lazy
                        :close-on-content-click="false"
                        v-model="timeFromMenu"
                        transition="scale-transition"
                        offset-y
                        full-width
                        :nudge-right="40"
                        max-width="285px"
                        min-width="285px"
                    >
                        <v-text-field
                            id="time_from"
                            slot="activator"
                            label=""
                            v-model="timeFrom"
                            :rules="[v => !!v || 'Time is required']"
                            readonly
                            required
                        ></v-text-field>
                        <!--Change action: save time in text-field after picking-->
                        <v-time-picker
                            v-model="timeFrom"
                            format="24hr"
                            :min="(new Date()).toISOString().slice(11, 16)"
                            :allowed-hours="allowedTimes.hours"
                            :allowed-minutes="allowedTimes.minutes"
                            @change="$refs.timeFromMenu.save(timeFrom)"
                        ></v-time-picker>
                    </v-menu>
                </v-flex>
                <!--Variant #2 for DateTimePickerTo-->
                <v-flex xs5>
                    <v-select
                        :items="timeItems"
                        v-model="period"
                        label="Period:"
                        prepend-icon="event"
                        :rules="[v => !!v || 'Field is required']"
                        required
                    ></v-select>
                </v-flex>
            </v-layout>

                <!--<v-subheader> Bike Type and Quantity </v-subheader>-->
            <v-layout row align-center>
                <v-flex xs4>
                    <v-chip close>
                        <v-avatar>
                            <img src="/static/images/bikecuny_favicon.ico" alt="man">
                        </v-avatar>
                        <v-select :items="[1,2,3]"></v-select>
                    </v-chip>
                </v-flex>
                <v-flex xs3>
                <v-btn fab dark small color="primary">
                    <v-icon dark>add</v-icon>
                </v-btn>
                </v-flex>

                <!--<v-flex xs4 v-for="bike in bikes" :key="bike.type">-->
                    <!--Transfer default args of bike to child component-->
                    <!--<order-check-box-->
                        <!--v-bind="bike"-->
                        <!--@input="(checked_default, quantity) => {-->
                            <!--bike.checked_default = checked_default;-->
                            <!--bike.quantity = quantity;-->
                            <!--upShops();-->
                        <!--}"-->
                    <!--&gt;</order-check-box>-->
                <!--</v-flex>-->
            </v-layout>
        </v-container>
    </v-form>

    <!--<v-card-actions>-->
        <!--<v-spacer></v-spacer>-->
        <!--<v-btn outline color="red" @click="clear">-->
            <!--<v-icon>delete</v-icon>-->
            <!--clear-->
        <!--</v-btn>-->
        <!--<v-btn outline color="green" -->
               <!--:disabled="!valid"-->
               <!--@click="listOfShopsActive = !listOfShopsActive" -->
        <!--&gt;-->
            <!--<v-icon>search</v-icon>-->
            <!--search-->
        <!--</v-btn>-->
    <!--</v-card-actions>-->

    <!-- List of Shops appears after clicking the button  -->
    <v-list :hidden="!listOfShopsActive">
        <list-of-shops
            v-for="shop in allShops"
            :key="shop.id"
            :shop="shop"
            :dt_from="dateTimeFrom"
            :dt_to="dateTimeTo"
            :bikeTypeQty="getBikeTypeQty()"
        >
        </list-of-shops>
    </v-list>
</v-card>
</template>

<script>
import DateTimePickerFrom from './DateTimePickerFrom.vue'
import DateTimePickerTo from './DateTimePickerTo.vue'
import OrderCheckBox from './OrderCheckBox.vue'
import ListOfShops from './ListOfShops.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'Order',

    components: {
        ListOfShops
    },

    data: () => ({
        // DateTime Pickers
            // from:
        dateFromMenu: false,
        timeFromMenu: false,
        dateFrom: (new Date()).toISOString().slice(0, 10),
        timeFrom: null,
        allowedTimes: {
            hours: null,
            minutes: null
        },
        allowedDates: null,
            // to:
        dateTimeToMenu: false,
        period: 1,
        timeItems: [
            { text: '1 hour', value: 1 },
            { text: '2 hours', value: 2 },
            { text: '3 hours', value: 3 },
            { text: '1 day', value: 24 },
            { text: '3 days', value: 72 }
        ],
        // Bike type and quantity
        type: 1,
        typeItems: [
            { text: 'man', value: 1 },
            { text: 'woman', value: 2 },
            { text: 'child', value: 3 }
        ],
        // Form
        valid: true,
        // dateTimeFrom, dateTimeTo - for update the list of shops on the map
        dateTimeFrom: (new Date()).toISOString().slice(0, 16),
        dateTimeTo: null,
        bikes: [
            { type: 1, quantity: 1 },
        ],
        listOfShopsActive: false
    }),

    computed: {
        ...mapGetters([ 'allShops' ]),
    },

    watch: {
        dateTimeFrom: function (val) {
            // if time is not picked - set 00:00
            if (val.slice(11) == 'null') {
                this.dateTimeFrom = val.slice(0, 10) + 'T00:00'
            }
            this.upShops()
        },

        dateTimeTo: function (val) {
            // if time is not picked - set actTimeTo
            if (val.slice(11) == 'null') {
                this.dateTimeTo = val.slice(0, 11) + this.actTimeTo
            }
            this.upShops()
        }
    },

    methods: {
        clear () {
            this.$refs.form.reset()
        },

        upShops () {
            // update the list of shops in store
            this.$store.dispatch('getFilterShops', {
                dt_from: this.dateTimeFrom,
                dt_to: this.dateTimeTo,
                type_qty: this.getBikeTypeQty()
            })
        },

        getBikeTypeQty () {
            let bikesSet = [];
            let i = 1;
            for (let bike of this.bikes) {
                if (bike.checked_default) {
                    bikesSet.push({type: i, quantity: bike.quantity})
                }
                i += 1
            }
            return bikesSet
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
