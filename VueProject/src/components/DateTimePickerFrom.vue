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
                id="date_from"
                slot="activator"
                label="From:"
                v-model="date"
                prepend-icon="event"
                readonly
                required
            ></v-text-field>
            <!--Change action: appear the TimePicker after
                and set min, date in DateTimePickerTo (through parent component)-->
            <v-date-picker
                v-model="date"
                @change="menu2 = !menu2; setDateTimeTo()"
                no-title
                scrollable
                :min="(new Date()).toISOString().slice(0, 10)"

                :allowed-dates="allowedDates"
            >
                <!--SAVE, CANCEL buttons (vuetify v0.17)-->
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
                v-model="time"
                prepend-icon="access_time"
                readonly
            ></v-text-field>
            <!--Change action: save time in text-field after picking
                    and set min time in DateTimePickerTo (through parent component)-->
            <v-time-picker
                v-model="time"
                @change="$refs.menu2.save(time); setDateTimeTo()"
                format="24hr"
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
        name: 'DateTimePickerFrom',

        data: () => ({
            // date now in 'yyyy-mm-dd' format
            date: (new Date()).toISOString().slice(0, 10),
            menu: false,
            time: null,
            menu2: false,
            allowedTimes: {
                hours: null,
                minutes: null
            },
            allowedDates: null
        }),

        methods: {
            setDateTimeTo () {
                // Set +1 hours (rent for at least 1 hour)
                let h, m;
                let resDate = this.date;

                if (this.time.slice(0, 2) && this.time.slice(3)) {
                    h = Number(this.time.slice(0, 2));
                    m = Number(this.time.slice(3));

                    if (h==23) {
                        h = 0;
                        // Set dateTo + 1 day, if h=23.
                        let tomorrow = new Date(this.date);
                        tomorrow.setDate(tomorrow.getDate() + 1);
                        resDate = tomorrow.toISOString().slice(0, 10);
                    }
                    else { h += 1 }
                    this.$emit('input', resDate, ( h + ':' + m ))
                }
            }
        }
    }
</script>
