<template>
<v-card>
    <v-card-title
    class="yellow accent-1 pa-4 title"
    > Create order </v-card-title>

    <v-container fluid>
        <v-layout row wrap>
            <date-time-picker-from></date-time-picker-from>
            <date-time-picker-to></date-time-picker-to>
        </v-layout>
    </v-container>

    <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn flat color="primary" @click="">Confirm</v-btn>
    </v-card-actions>
</v-card>
</template>

<script>
import DateTimePickerFrom from './DateTimePickerFrom.vue'
import DateTimePickerTo from './DateTimePickerTo.vue'

export default {
    components: {
        DateTimePickerFrom, DateTimePickerTo
    }
}
</script>
