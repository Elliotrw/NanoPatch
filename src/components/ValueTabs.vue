<script>
import axios from 'axios'
import * as bootstrap from 'bootstrap/dist/js/bootstrap'

export default {
  data() {
    return {
      values: { 0: { N: 0 }, 1: { P: 0 }, 2: { K: 0 }, 3: { T: 0 }, 4: { H: 0 }, 5: { M: 0 } },
      rangeN: [20, 50, 70, 350],
      rangeP: [9, 14, 150, 200],
      rangeK: [100, 180, 600, 800],
      rangeT: [6, 10, 12, 27],
      rangeHM: [15, 50, 70, 85],
    }
  },
  mounted() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

    this.getValues();
    setInterval(this.getValues, 7000);
  },
  methods: {
    getValues() {
      axios
        .get('/values')
        .then((response) => {
          this.values = response.data
        })
    },
    getClass(value, warn_min, good_min, good_max, warn_max) {
      if (value > good_min && value <= good_max) {
        return 'list-group-item-success'; // Success class
      } else if ((value >= warn_min && value <= good_min) || (value > good_max && value <= warn_max)) {
        return 'list-group-item-warning'; // Warning class
      } else {
        return 'list-group-item-danger'; // Danger class
      }
    },
  },
}
</script>

<template>
  <div class="allBoxes">
    <div>
      <div class="valueBox">
        Nitrogen (N):&nbsp;
        <li class="list-group-item"
          v-bind:class="getClass(values[0].N, this.rangeN[0], this.rangeN[1], this.rangeN[2], this.rangeN[3])"
          data-bs-toggle="tooltip"
          :data-bs-title="'Ideal conditions: ' + this.rangeN[1] + '-' + this.rangeN[2] + ' ppm'">{{
            values[0].N }} ppm</li>
      </div>
      <div class="valueBox">
        Phosphorus (P):&nbsp;
        <li class="list-group-item"
          v-bind:class="getClass(values[1].P, this.rangeP[0], this.rangeP[1], this.rangeP[2], this.rangeP[3])"
          data-bs-toggle="tooltip"
          :data-bs-title="'Ideal conditions: ' + this.rangeP[1] + '-' + this.rangeP[2] + ' ppm'">{{
            values[1].P }} ppm</li>
      </div>
      <div class="valueBox">
        Potassium (K):&nbsp;
        <li class="list-group-item"
          v-bind:class="getClass(values[2].K, this.rangeK[0], this.rangeK[1], this.rangeK[2], this.rangeK[3])"
          data-bs-toggle="tooltip"
          :data-bs-title="'Ideal conditions: ' + this.rangeK[1] + '-' + this.rangeK[2] + ' ppm'">{{
            values[2].K }} ppm</li>
      </div>
      <div class="valueBox">
        Temperature:&nbsp;
        <li class="list-group-item"
          v-bind:class="getClass(values[3].T, this.rangeT[0], this.rangeT[1], this.rangeT[2], this.rangeT[3])"
          data-bs-toggle="tooltip" :data-bs-title="'Ideal conditions: ' + this.rangeT[1] + '-' + this.rangeT[2] + ' °C'">
          {{
            values[3].T }} °C</li>
      </div>
      <div class="valueBox">
        Humidity:&nbsp;
        <li class="list-group-item"
          v-bind:class="getClass(values[4].H, this.rangeHM[0], this.rangeHM[1], this.rangeHM[2], this.rangeHM[3])"
          data-bs-toggle="tooltip" :data-bs-title="'Ideal conditions: ' + this.rangeHM[1] + '-' + this.rangeHM[2] + ' %'">
          {{
            values[4].H }} %</li>
      </div>
      <div class="valueBox">
        Moisture:&nbsp;
        <li class="list-group-item"
          v-bind:class="getClass(values[5].M, this.rangeHM[0], this.rangeHM[1], this.rangeHM[2], this.rangeHM[3])"
          data-bs-toggle="tooltip" :data-bs-title="'Ideal conditions: ' + this.rangeHM[1] + '-' + this.rangeHM[2] + ' %'">
          {{
            values[5].M }} %</li>
      </div>
    </div>
  </div>
</template>

<style scoped>
.allBoxes {
  /* font-size: 40px; */
  font-size: 2vw;
  width: fit-content;
  /* padding-top: 5%; */
}

.valueBox {
  display: flex;
  padding-bottom: 2%;
}

/* Responsive adjustments for mobile screens */
@media (max-width: 768px) {
  .allBoxes {
    font-size: 1.6vh;
  }
}</style>
