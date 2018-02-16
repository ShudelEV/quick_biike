<template>
    <v-container fluid pa-0>
    <v-layout raw wrap>
        <!--Date Picker-->
    <v-flex xs6>
        <v-menu
            lazy
            :close-on-content-click="true"
            v-model="menu"
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
    <v-flex xs1></v-flex>
        <!--Time Picker-->
    <v-flex xs4>
        <v-menu
            ref="menu2"
            lazy
            :close-on-content-click="false"
            v-model="menu2"
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
                prepend-icon="access_time"
                readonly
            ></v-text-field>
            <!--Change action: save time in text-field after picking-->
            <v-time-picker
                v-model="time"
                @change="$refs.menu2.save(time)"
                format="24hr"
                :allowed-hours="allowedTimes.hours"
                :allowed-minutes="allowedTimes.minutes"
            ></v-time-picker>
        </v-menu>
    </v-flex>
    </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: 'DateTimePickerTo',

        data: () => ({
            date: null,
            menu: false,
            time: null,
            menu2: false,
            allowedTimes: {
                hours: null,
                minutes: null
            },
            allowedDates: null
        })
    }
</script>
