<template>
  <div id="Compare-Page">
    <br>
    <h1>Algorithm Comparison </h1>
    <br>

    <!-- Algorithms' checkboxes -->
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

    <!-- Graphs -->
    <div id="compare">
        <CompareAlgorithmsPerfomance :algorithms="selected"></CompareAlgorithmsPerfomance>
        <CompareAlgorithmEventAmount :algorithms="selected"></CompareAlgorithmEventAmount>
    </div>

  </div>
</template>

<script>
import CompareAlgorithmsPerfomance from "./../components/charts/compareAlgorithmsPerfomance.vue";
import CompareAlgorithmEventAmount from "../components/charts/compareAlgorithmEventAmount.vue";

export default {
    name: 'ComparePage',
    components:{
        CompareAlgorithmsPerfomance,
        CompareAlgorithmEventAmount
    },
    data(){
        return{
            selected: null,
            options: null,
        }
    },

    methods: {
        async getAlgorithms() {
            /** Get request for all saved algorithms in server */

            this.selected = [];
            this.options = [];
            try {
                const saves_algorithms = this.axios.get(`${this.$root.serverLink}/algorithm/all`);
                saves_algorithms.data.map((algorithm) => {
                    this.selected.push(algorithm);
                    this.options.push(algorithm);
                });

            } catch (error) {
                let default_algorithms = ['SedTwik', 'Twembeddings','Bert']
                this.selected = default_algorithms;
                this.options = default_algorithms;
                console.log(`error ${error} occured in ComparePage`);
            }
        }
    },
    created() {
        this.getAlgorithms();
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
    width: 102%;
}
</style>