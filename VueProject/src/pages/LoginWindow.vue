<template>
<v-dialog v-model="showDialog"
              max-width="500px"
              persistent>
    <v-card class="elevation-12">
        <v-card-title></v-card-title>
    </v-card>
</v-dialog>
</template>

<script>
export default {
    data () {
        return {
            showDialog: true,
        }
    }
}
</script>
