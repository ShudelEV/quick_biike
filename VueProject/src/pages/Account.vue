<template>
<v-dialog v-model="showDial"
          max-width="500px"
          persistent>
    <v-card>
        Account Page
    </v-card>
</v-dialog>
</template>

<script>
export default {
    data () {
        return {
            showDial: true
        }
    }
}
</script>
