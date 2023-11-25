<script setup>
import ValueTabs from "./components/ValueTabs.vue";
</script>

<script>
import MultiLineChart from './components/MultiLineChart.vue';

export default {
  components: {
    MultiLineChart
  },
  data() {
    return {
      npkData: {
        nitrogen: [10, 22, 15, 18, 25, 30, 35],
        phosphorus: [5, 8, 10, 12, 20, 22, 25],
        potassium: [8, 12, 13, 17, 23, 28, 33]
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
      <MultiLineChart :chart-data="npkData" />
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
}
</style>
