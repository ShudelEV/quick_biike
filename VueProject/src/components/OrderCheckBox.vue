<template>
    <v-container fluid pa-0>
    <v-subheader> BikeTypes </v-subheader>
    <v-layout raw wrap>
    <v-flex xs4>
        <v-checkbox v-model="man" label="Man" hide-details></v-checkbox>
    </v-flex>
    <v-flex xs4>
        <v-checkbox v-model="woman" label="Woman" hide-details></v-checkbox>
    </v-flex>
    <v-flex xs4>
        <v-checkbox v-model="child" label="Child" hide-details></v-checkbox>
    </v-flex>
    </v-layout>

    <v-layout raw wrap>
        <v-flex xs4 pl-2 pr-4>
            <v-text-field type="number" v-if="man" v-model.number="man_qty"></v-text-field>
        </v-flex>
        <v-flex xs4 pl-2 pr-4>
            <v-text-field type="number" v-if="woman" v-model.number="woman_qty"></v-text-field>
        </v-flex>
        <v-flex xs4 pl-2 pr-4>
            <v-text-field type="number" v-if="child" v-model.number="child_qty"></v-text-field>
        </v-flex>
    </v-layout>
    </v-container>
</template>

<script>
  export default {
      name: 'OrderCheckBox',
      data: () => ({
          man: true,
          woman: false,
          child: false,
          man_qty: 1,
          woman_qty: 1,
          child_qty: 1
      })
  }
</script>
