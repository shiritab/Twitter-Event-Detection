<template>
  <div id="Compare-Page">
      <br>
    <h1>Alghorithms Comparison </h1>
    <br>
    <div id="algo-checkbox">
        <b-form-group v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group
                id="checkbox-group-1"
                v-model="selected"
                :options="options"
                :aria-describedby="ariaDescribedby"
                name="flavour-1"
            ></b-form-checkbox-group>

        </b-form-group>
    </div>
    <div id="compare">
        <CompareColumn :algorithms="selected"></CompareColumn>
        <CompareBar :algorithms="selected"></CompareBar>
    </div>
  </div>
</template>

<script>
import CompareColumn from "./../components/charts/CompareColumn.vue"
import CompareBar from "./../components/charts/CompareBar.vue"

export default {
    name: 'ComparePage',
    components:{
        CompareColumn,
        CompareBar
    },
    data(){
        return{
            selected: ['SedTwik', 'Twembeddings','Bert'],
            options: ['SedTwik', 'Twembeddings','Bert'],
        }
    }
}
</script>

<style>
#algo-checkbox{
    margin: 0 auto;
    display: table
}

#compare-button{
    margin: 0 auto;
    display: table
}
#compare{
    display: flex;
    width: 100%;
}
</style>