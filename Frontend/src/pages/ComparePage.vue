<template>
  <div id="Compare-Page">
    <br>
    <h1>Algorithms Comparison </h1>
    <br>

    <!-- Algorithms' checkboxes -->
    <div id="algo-checkbox">
        <b-form-group v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group
                id="checkbox-group-1"
                v-model="selected_algorithms"
                :options="options_algorithms"
                :aria-describedby="ariaDescribedby"
                name="flavour-1"
            ></b-form-checkbox-group>

        </b-form-group>
    </div>

    <!-- Graphs -->
    <div id="compare">
        <CompareColumn :algorithms="selected_algorithms"></CompareColumn>
        <CompareBar :algorithms="selected_algorithms"></CompareBar>
    </div>

  </div>
</template>

<script>
import CompareColumn from "../components/charts/algorithmPerfomance.vue"
import CompareBar from "../components/charts/compareAlgorithmEventAmount.vue"

export default {
    name: 'ComparePage',
    components:{
        CompareColumn,
        CompareBar
    },
    data(){
        return{
            selected_algorithms: [],
            options_algorithms: [],
        }
    },
    methods: {
        async getAllAlgorithms() {
            /* Get request for all saved algorithms. */

            this.selected_algorithms = [];
            this.options_algorithms = [];
            try {
                
                const saved_algorithms = await this.axios.get(`${this.$root.serverLink}/algorithm/all`);

                saved_algorithms.data.map((algorithm) => {
                    this.selected_algorithms.push(algorithm);
                    this.options_algorithms.push(algorithm);
                });

            } catch (error) {
                this.selected_algorithms = ['SedTwik', 'Twembeddings','Bert'];
                this.options_algorithms = ['SedTwik', 'Twembeddings','Bert'];
                console.log(`error occured on getAllAlgorithms ComparePage. error: ${error}`);
            }

        }
    },
    created() {
        console.log("Created ComparePage");
        this.getAllAlgorithms();
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