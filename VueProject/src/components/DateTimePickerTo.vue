<template>
    <v-container fluid pa-0>
    <v-layout raw>
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
              label="Time To:"
              v-model="date"
              prepend-icon="event"
              readonly
            ></v-text-field>

            <v-date-picker v-model="date" no-title scrollable actions>
                <template slot-scope="{ save, cancel }">
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn flat color="primary" @click="cancel">Cancel</v-btn>
                        <v-btn flat color="primary" @click="save">OK</v-btn>
                    </v-card-actions>
                </template>
            </v-date-picker>
        </v-menu>
    </v-flex>

    <v-flex xs6>
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
                slot="activator"
                v-model="time"
                prepend-icon="access_time"
                readonly
            ></v-text-field>
            <v-time-picker v-model="time" autosave format="24hr"></v-time-picker>
        </v-menu>
    </v-flex>
    </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: 'DateTimePickerFrom',
        data: () => ({
            date: null,
            menu: false,
            time: null,
            menu2: false,
            modal2: false,
        })
    }
</script>
