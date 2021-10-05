<template>
    <b-card-group deck>
      <b-card v-for="tweet in tweets"
        :key="tweet.id"
        style="max-width: 20rem; margin: auto;"
        bg-variant="light" :header="tweet.date" class="text-center">
        <b-card-text>{{ tweet.content }}</b-card-text>
      </b-card>
    </b-card-group>
</template>

<script>
export default {
    name: "Tweet",
    props:{
        tweets:{
            type: Array,
            require: true,
        }
    }
}
</script>

<style scope>

</style>