<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        values: {0: {N:0}, 1: {P:0}, 2: {K:0}, 3: {T:0}, 4: {H:0}, 5: {M:0}},
      }
    },
    mounted() {
      this.getValues();
      setInterval(this.getValues, 5000);
    },
    methods: {
      getValues() {
        axios
          .get('http://127.0.0.1:5000/values')
          .then((response) => {
            this.values = response.data
        })
      },
      getClass(value) {
        if (value > 5 && value <= 10) {
          return 'list-group-item-success'; // Success class
        } else if ((value >= 0 && value <= 5) || (value > 10 && value <= 15)) {
          return 'list-group-item-warning'; // Warning class
        } else {
          return 'list-group-item-danger'; // Danger class
        }
      },
    },
  }
</script>

<template>
  <div style="font-size: 40px; width: fit-content;">
    <div>
      <div class="valueBox">
        Nitrogen (N):&nbsp;
        <li class="list-group-item" v-bind:class="getClass(values[0].N)">{{values[0].N}} ppm</li>
      </div>
      <div class="valueBox">
        Phosphorus (P):&nbsp;
        <li class="list-group-item" v-bind:class="getClass(values[1].P)">{{values[1].P}} ppm</li>
      </div>
      <div class="valueBox">
        Potassium (K):&nbsp;
        <li class="list-group-item" v-bind:class="getClass(values[2].K)">{{values[2].K}} ppm</li>
      </div>
      <div class="valueBox">
        Temperature:&nbsp;
        <li class="list-group-item" v-bind:class="getClass(values[3].T)">{{values[3].T}} °C</li>
      </div>
      <div class="valueBox">
        Humidity:&nbsp;
        <li class="list-group-item" v-bind:class="getClass(values[4].H)">{{values[4].H}} gm⁻³</li>
      </div>
      <div class="valueBox">
        Moisture:&nbsp;
        <li class="list-group-item" v-bind:class="getClass(values[5].M)">{{values[5].M}} °C</li>
      </div>
    </div>
  </div>
</template>

<style scoped>
.valueBox {
  display: flex;
  padding-bottom: 2%;
}
</style>
