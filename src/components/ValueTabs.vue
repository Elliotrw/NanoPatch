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
  <div>
    <h1>Nitrogen (N): {{N}} ppm</h1>
    <h1>Phosphorus (P): {{P}} ppm</h1>
    <h1>Potassium (K): {{K}} ppm</h1>
  </div>

  <div>
    <h1>Temperature: {{T}}°C</h1>
    <h1>Humidity: {{H}} gm⁻³</h1>
    <h1>Moisture: {{M}}°C</h1>
  </div>
</template>

<style scoped>

</style>
