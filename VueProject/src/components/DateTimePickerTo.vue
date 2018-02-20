<template>
    <v-container fluid pa-0>
    <v-layout raw wrap>
        <!--Date Picker-->
    <v-flex xs6>
        <v-menu
            lazy
            :close-on-content-click="true"
            v-model="menu"
            :disabled="!activeDateTimeTo"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            max-width="285px"
            min-width="285px"
        >
            <v-text-field
                slot="activator"
                label="To:"
                v-model="date"
                :disabled="!activeDateTimeTo"
                prepend-icon="event"
                readonly
                required
            ></v-text-field>
            <!--Change action: appear the TimePicker after-->
            <v-date-picker
                v-model="date"
                @change="menu2 = !menu2"
                no-title
                scrollable
                :min="date"
                :allowed-dates="allowedDates"
            >
                <!--<template slot-scope="{ save, cancel }">-->
                    <!--<v-card-actions>-->
                        <!--<v-spacer></v-spacer>-->
                        <!--<v-btn flat color="primary" @click="cancel">Cancel</v-btn>-->
                        <!--&lt;!&ndash;Raise a TimeMenu after the Ok button clicking&ndash;&gt;-->
                        <!--<v-btn flat color="primary" @click="save" @click.stop="menu2 = !menu2">OK</v-btn>-->
                    <!--</v-card-actions>-->
                <!--</template>-->
            </v-date-picker>
        </v-menu>
    </v-flex>
    <v-spacer></v-spacer>
        <!--Time Picker-->
    <v-flex xs4>
        <v-menu
            ref="menu2"
            lazy
            :close-on-content-click="false"
            v-model="menu2"
            :disabled="!activeDateTimeTo"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            max-width="285px"
            min-width="285px"
        >
            <v-text-field
                slot="activator"
                v-model="time"
                :disabled="!activeDateTimeTo"
                prepend-icon="access_time"
                readonly
            ></v-text-field>
            <!--Change action: save time in text-field after picking-->
            <v-time-picker
                v-model="time"
                @change="$refs.menu2.save(time)"
                format="24hr"
                :min="timeTo"
                :allowed-hours="allowedTimes.hours"
                :allowed-minutes="allowedTimes.minutes"
            ></v-time-picker>
        </v-menu>
    </v-flex>
    <v-spacer></v-spacer>
    </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: 'DateTimePickerTo',

        props: ['dateTo', 'timeTo', 'activeDateTimeTo'],

        // The hook is to update the date when the dateTo have changed
        beforeUpdate () {
            this.date = this.dateTo
        },

        data: () => ({
            menu: false,
            menu2: false,
            time: null,
            date: null,
            allowedTimes: {
                hours: null,
                minutes: null
            },
            allowedDates: null
        })
    }
</script>
