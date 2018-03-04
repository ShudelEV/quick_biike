<template>
<v-card>
    <v-card-title>
        {{shop.name}}
    </v-card-title>
</v-card>
</template>

<script>
export default {
    name: 'ListOfShops',

    props: {
        shop: {type: Object, default: null},
    },

    data: () => ({
    })
}
</script>
