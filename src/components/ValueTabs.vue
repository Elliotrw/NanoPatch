<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        values: {0: {N:0}, 1: {P:0}, 2: {K:0}, 3: {T:0}, 4: {H:0}, 5: {M:0}},
      }
    },
    mounted() {
      axios
        .get('http://127.0.0.1:5000/values')
        .then((response) => {
          this.values = response.data
        })
    }
  }
</script>

<template>
  <div style="font-size: 40px; width: fit-content;">
    <div>
      <div class="valueBox">
        Nitrogen (N):&nbsp;
        <li class="list-group-item list-group-item-success">{{values[0].N}} ppm</li>
      </div>
      <div class="valueBox">
        Phosphorus (P):&nbsp;
        <li class="list-group-item list-group-item-warning">{{values[1].P}} ppm</li>
      </div>
      <div class="valueBox">
        Potassium (K):&nbsp;
        <li class="list-group-item list-group-item-danger">{{values[2].K}} ppm</li>
      </div>
      <div class="valueBox">
        Temperature:&nbsp;
        <li class="list-group-item list-group-item-success">{{values[3].T}} °C</li>
      </div>
      <div class="valueBox">
        Humidity:&nbsp;
        <li class="list-group-item list-group-item-warning">{{values[4].H}} gm⁻³</li>
      </div>
      <div class="valueBox">
        Moisture:&nbsp;
        <li class="list-group-item list-group-item-danger">{{values[5].M}} °C</li>
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
