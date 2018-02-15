<template>
    <v-card flat>
        <v-checkbox ref="checkbox"
            :input-value="checked_default" @change="updateValue()"
            :prepend-icon="icon" hide-details></v-checkbox>
        <v-card-text>
            <v-text-field
                type="number" v-if="checked_default"
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
          qty: 0,
//          checked: false
      }),
//      computed: {
//          qty: () => {this.value},
//          checked: () => {this.checked_default}
//      },

      props:
      {
          checked_default: {
              type: Boolean,
              default: true
          },
          quantity: {
              type: Number,
              default: 1
          },
          icon: {
              type: String,
              default: ''
          },
          type: {
              type: String,
              default: ''
          },
      },

      methods: {
          updateValue: function () {
              console.log(this.type);
              this.$emit('input', {
                  checked_default: !this.$refs.checkbox.inputValue,
                  quantity: 22,
                  icon: this.icon,
                  type: this.type
              })
          },
          updateCheckbox: function (val) {
              console.log(val);
//              this.$emit('input', val)
          }
      }
  }
</script>
