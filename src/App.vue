<script setup>
import ValueTabs from "./components/ValueTabs.vue";
</script>

<script>
import MultiLineChart from './components/MultiLineChart.vue';
import MultiAxisChart from './components/MultiAxisChart.vue';

export default {
  components: {
    MultiLineChart,
    MultiAxisChart
  },
  data() {
    return {
      npkData: {
        nitrogen: [10, 22, 15, 18, 25, 30, 35],
        phosphorus: [5, 8, 10, 12, 20, 22, 25],
        potassium: [8, 12, 13, 17, 23, 28, 33]
      },
      thmData: {
        temperature: [4, 15, 16, 18, 20, 10, 12],
        humidity: [25, 12, 2, 22, 19, 16, 25],
        moisture: [8, 12, 13, 33, 23, 28, 10]
      }
    }
  }
}
</script>

<template>
  <div class="app-container">
    <div class="top-section">
      <div class="logo-container">
        <img alt="Vue logo" src="./assets/NanoPatch.png" />
      </div>
      <div class="value-tabs-container">
        <ValueTabs />
      </div>
    </div>
    <div class="bottom-section">
      <MultiLineChart :chart-data="npkData" />
      <MultiAxisChart :chart-data="thmData" />
    </div>
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.top-section {
  display: flex;
  flex: 1;
  /* position: relative; */
}

.logo-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo-container img {
  width: 35vw;
  height: auto;
}

.value-tabs-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.bottom-section {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 0.5;
  gap: 10px; /* Adds a gap between the Graph components */
}

/* Responsive adjustments for mobile screens */
@media (max-width: 768px) {
  .bottom-section {
    flex-direction: column; /* Stack the Graph components */
    gap: 0; /* Removes the gap when stacked vertically */
  }

  .logo-container img {
    width: 50vw; /* Adjust logo size for smaller screens */
  }

  .value-tabs-container {
    right: 10%;
    width: 80%;
  }
}
</style>
