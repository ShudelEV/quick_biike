<template>
    <v-card flat>
        <v-checkbox ref="checkbox"
            :input-value="value" @change="updateValue($refs.checkbox.inputValue)"
            :prepend-icon="icon" hide-details></v-checkbox>
        <v-card-text>
            <v-text-field
                type="number" v-if="value"
                :value="quantity"
                @input="updateValue($event.target.value)"
            ></v-text-field>
        </v-card-text>
    </v-card>
</template>

<script>
  export default {
      name: 'OrderCheckBox',
      data: () => ({
      }),
//      computed: {
//          qty: () => {this.value},
//          checked: () => {this.checked_default}
//      },

      props:
      {
          value: {
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
          }
      },

      methods: {
          updateValue: function (val) {
              console.log(val);
              this.$emit('input', !val)
          },
          updateCheckbox: function (val) {
              console.log(val);
//              this.$emit('input', val)
          }
      }
  }
</script>
