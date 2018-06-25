<template>
<!--Create a form-->
<!--Evoke getShops() method when a value of order is changed-->
<v-card>
    <v-form ref="form" v-model="valid" lazy-validation>
        <v-container fluid pa-2>
        <v-layout column fill-height>
            <v-flex xs2 md2 fill-height>
                <v-layout row justify-space-around>
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
                                hide-details
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
                                autofocus
                                hide-details
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
                    <v-spacer></v-spacer>
                    <!--Variant #2 for DateTimePickerTo-->
                    <v-flex xs4>
                        <v-select
                            :items="timeItems"
                            v-model="period"
                            label="Period:"
                            hide-details
                            prepend-icon="timer"
                        ></v-select>
                    </v-flex>
                </v-layout>
            </v-flex>
                <!--<v-subheader> Bike Type and Quantity </v-subheader>-->
            <v-flex xs1 md1>
            <v-layout row align-center justify-space-between wrap>
                <v-flex xs4
                        v-for="(b, i) in bikesTypeQty"
                        :key="i"
                >
                    <v-layout row align-center>
                        <v-flex d-flex>
                            <v-chip color="teal"
                                    text-color="white"
                                    close @input="REMOVE_TYPE_QTY(b.type)"
                            >
                                <!--<v-icon flat> directions_bike </v-icon>-->
                                {{ getTypeName(b.type) }}
                            </v-chip>
                        </v-flex>
                        <v-flex d-flex>
                            <!-- No label: padding-top: 0;-->
                            <v-select hide-details style="padding-top: 0;"
                                      v-model="b.quantity"
                                      :items="[1,2,3,4,5]"
                            ></v-select>
                        </v-flex>
                    </v-layout>
                </v-flex>
                <!--Add button. To add a type and quantity of bikes from the popup menu-->
                <v-menu
                    origin="center center"
                    transition="scale-transition"
                    bottom
                >
                    <!--don't appear the add button when no type items-->
                    <v-btn left fab small
                           color="primary"
                           slot="activator"
                           v-show="showAddButton"
                    >
                        <v-icon>add</v-icon>
                    </v-btn>
                    <v-list>
                        <v-list-tile v-for="(item, i) in filterTypeItems()" :key="i"
                                     @click="PUSH_TYPE_QTY({ type: item.value, quantity: 1 })"
                        >
                            <v-list-tile-title>{{ item.text }}</v-list-tile-title>
                        </v-list-tile>
                    </v-list>
                </v-menu>
                <v-spacer></v-spacer>
                <!--the submit button for to take shops using the filter form-->
                <v-btn round color="cyan"
                       v-show="showSearchButton"
                       @click="getShopList(); textSearchButton = 'UPDATE'"
                >
                    <v-icon>search</v-icon>
                    {{ textSearchButton }}
                </v-btn>
            </v-layout>
            </v-flex>
        </v-layout>
        </v-container>
    </v-form>
</v-card>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
    name: 'SearchMenu',

    data: () => ({
        // DateTime Pickers
            // from:
        dateFromMenu: false,
        timeFromMenu: false,
        dateFrom: (new Date()).toISOString().slice(0, 10),
        timeFrom: '12:00',
        allowedTimes: {
            hours: null,
            minutes: null
        },
        allowedDates: null,
            // to:
        period: 1,
        timeItems: [
            { text: '1 hour', value: 1 },
            { text: '2 hours', value: 2 },
            { text: '3 hours', value: 3 },
            { text: '1 day', value: 24 },
            { text: '3 days', value: 72 }
        ],
        // Bike type and quantity
        typeItems: [
            { text: 'man', value: 1 },
            { text: 'woman', value: 2 },
            { text: 'child', value: 3 }
        ],
        // Visibility of add button
        showAddButton: true,
        // Form
        valid: true,
        showSearchButton: true,
        textSearchButton: 'GO!',
    }),

    computed: {
        ...mapGetters([
            'dateTimeFrom', 'dateTimeTo', 'bikesTypeQty'
        ]),
    },

    created () {
        this.SET_DATE_TIME_FROM({ date: this.dateFrom, time: this.timeFrom });
        this.SET_DATE_TIME_TO(this.period)
    },

    watch: {
        dateFrom: function () {
            this.SET_DATE_TIME_FROM({ date: this.dateFrom, time: this.timeFrom });
            this.SET_DATE_TIME_TO(this.period)
        },
        timeFrom: function () {
            this.SET_DATE_TIME_FROM({ date: this.dateFrom, time: this.timeFrom });
            this.SET_DATE_TIME_TO(this.period)
        },
        period: function () {
            this.SET_DATE_TIME_TO(this.period)
        }

    },

    methods: {
        ...mapMutations([
            'SET_DATE_TIME_FROM', 'SET_DATE_TIME_TO', 'PUSH_TYPE_QTY', 'REMOVE_TYPE_QTY'
        ]),

        upShops () {
            // update the list of shops in store
            this.$store.dispatch('getFilteredShops', {
                dt_from: this.dateTimeFrom,
                dt_to: this.dateTimeTo,
                type_qty: this.bikesTypeQty
            })
        },

        // get a bike type name for chips
        getTypeName (type) {
            return this.typeItems.find(item => item.value === type).text
        },

        // don't allow to choose a similar type of bikes
        filterTypeItems () {
            let items = this.typeItems.filter(
                i => !this.bikesTypeQty.map(i => i.type).includes(i.value)
            );
            this.showAddButton = !!items.length;
            return items
        },

        getShopList () {
            if (this.$refs.form.validate()) {
                // update shops list
                this.upShops();
                this.$emit('show-shop-list')
            }
        }
    }
}
</script>
