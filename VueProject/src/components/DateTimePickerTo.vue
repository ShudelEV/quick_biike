<template>
    <v-container fluid pa-0>
    <v-layout raw wrap>
        <!--Date Picker-->
    <v-flex xs6>
        <v-menu
            lazy
            :close-on-content-click="false"
            v-model="menu"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            max-width="285px"
            min-width="285px"
        >

            <v-text-field
                ref="date"
              slot="activator"
              label="To:"
              v-model="date"
              prepend-icon="event"
              readonly
              required
            ></v-text-field>

            <v-date-picker v-model="date" no-title scrollable actions>
                <template slot-scope="{ save, cancel }">
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn flat color="primary" @click="cancel">Cancel</v-btn>
                        <!--Raise a TimeMenu after the Ok button clicking-->
                        <v-btn flat color="primary" @click="save" @click.stop="menu2 = !menu2">OK</v-btn>
                    </v-card-actions>
                </template>
            </v-date-picker>
        </v-menu>
    </v-flex>
    <v-flex xs1></v-flex>
        <!--Time Picker-->
    <v-flex xs4>
        <v-menu
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
                ref="time"
                slot="activator"
                v-model="time"
                prepend-icon="access_time"
                readonly
            ></v-text-field>
            <v-time-picker
                v-model="time"
                autosave
                @input="updateValue()"
                format="24hr"
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
        }),

        props: {
            value: {
                type: String,
                default: ''
            }
        },

        methods: {
            updateValue: function () {
//                to ISO 8601
                var res = this.$refs.date.value + 'T' + this.$refs.time.value;
//                Emit event "input" for Parent component and update 'value' in Parent
                this.$emit('input', res)
            },
        }
    }
</script>
