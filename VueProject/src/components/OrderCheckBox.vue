<template>
    <v-card flat>
        <v-checkbox ref="checkbox"
            :id="type"
            :input-value="checked_default" @change="updateCheckbox($refs.checkbox.inputValue)"
            :prepend-icon="icon" hide-details></v-checkbox>
        <v-card-text>
            <v-text-field
                type="number" v-if="checked_default"
                :value="quantity"
            ></v-text-field>
        </v-card-text>
    </v-card>
</template>

<script>
  export default {
      name: 'OrderCheckBox',
      data: () => ({
      }),

      props:
      {
          checked_default: {
              type: Boolean,
              default: true
          },
          icon: {
              type: String,
              default: ''
          },
          quantity: {
              type: Number,
              default: 1
          },
          type: {
              type: String,
              default: ''
          }
      },

      methods: {
          updateCheckbox (val) {
//              console.log(val);
              this.$emit('input', !val)
          }
      }
  }
</script>
