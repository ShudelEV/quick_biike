<template>
    <v-card>
        <v-checkbox ref="checkbox"
            :id="type"
            :input-value="checked_default" @change="updateCheckbox($refs.checkbox.inputValue)"
            :prepend-icon="icon" hide-details></v-checkbox>
        <v-text-field
            ref="qty"
            type="number" v-if="checked_default"
            solo
            :min="minQty"
            :max="maxQty"
            :value="quantity"
            @change="validateQty"
        ></v-text-field>
    </v-card>
</template>

<script>
  export default {
      name: 'OrderCheckBox',

      data: () => ({
          minQty: 1,
          maxQty: 10
      }),

      props:
      {
          checked_default: { type: Boolean, default: true},
          icon: { type: String, default: ''},
          quantity: { type: Number, default: 1},
          type: { type: String, default: ''}
      },

      methods: {
          updateCheckbox (val) {
              this.$emit('input', !val)
          },
          validateQty () {
              let val = this.$refs.qty.inputValue;
              if (val < this.minQty) { this.$refs.qty.inputValue = this.minQty }
              else if (val > this.maxQty) { this.$refs.qty.inputValue = this.maxQty }
          }
      }
  }
</script>
