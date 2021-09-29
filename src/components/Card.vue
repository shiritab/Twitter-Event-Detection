<template>
  <div>
    <b-card-group deck>
      <b-card v-for="info in infos"
        border-variant="info"
        :header="info.title"
        header-border-variant="info"
        header-text-variant="info"
        align="center"
        :key="info.id"
      >
        <!-- chart type? -->
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
    name: "Card",
    props:{
      infos:{
        type: Array,
        required: true
      }
    }
}
</script>

<style>

</style>