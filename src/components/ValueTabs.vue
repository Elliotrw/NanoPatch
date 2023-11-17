<script setup>
  const N = 0, P = 0, K = 0, T = 0, H = 0, M = 0;
</script>

<script>
  import axios from 'axios'

  export default {
    mounted() {
      axios
        .get('http://127.0.0.1:5000/values')
        .then((response) => {
          console.log(response.data);
        })
    }
  }
</script>

<template>
  <div style="font-size: 40px; width: fit-content;">
    <div>
      <div class="valueBox">
        Nitrogen (N):&nbsp;
        <li class="list-group-item list-group-item-success">{{N}} ppm</li>
      </div>
      <div class="valueBox">
        Phosphorus (P):&nbsp;
        <li class="list-group-item list-group-item-warning">{{P}} ppm</li>
      </div>
      <div class="valueBox">
        Potassium (K):&nbsp;
        <li class="list-group-item list-group-item-danger">{{K}} ppm</li>
      </div>
      <div class="valueBox">
        Temperature:&nbsp;
        <li class="list-group-item list-group-item-success">{{T}} °C</li>
      </div>
      <div class="valueBox">
        Humidity:&nbsp;
        <li class="list-group-item list-group-item-warning">{{H}} gm⁻³</li>
      </div>
      <div class="valueBox">
        Moisture:&nbsp;
        <li class="list-group-item list-group-item-danger">{{M}} °C</li>
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
