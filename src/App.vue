<script setup>
import ValueTabs from "./components/ValueTabs.vue";
</script>

<script>
import axios from "axios"
import MultiLineChart from './components/MultiLineChart.vue';
import MultiAxisChart from './components/MultiAxisChart.vue';

export default {
  components: {
    MultiLineChart,
    MultiAxisChart
  },
  mounted() {
    this.getPastValues();
  },
  created() {
    this.pastSevenDaysData = this.getPastSevenDays();
  },
  methods: {
    getPastValues() {
      axios
        .get('/past-values')
        .then((response) => {
          this.npkData = response.data.npkData
          this.thmData = response.data.thmData
        })
    },
    getPastSevenDays() {
      const dates = [];
      for (let i = 6; i >= 0; i--) {
        const date = new Date();
        date.setDate(date.getDate() - i);
        const formattedDate = `${date.getDate().toString().padStart(2, '0')}/${(date.getMonth() + 1).toString().padStart(2, '0')}`;
        dates.push(formattedDate);
      }
      return dates;
    }
  },
  data() {
    return {
      pastSevenDaysData: [],
      npkData: null,
      thmData: null
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
      <MultiLineChart v-if="npkData" :chart-data="npkData" :x-axis-data=pastSevenDaysData />
      <MultiAxisChart v-if="thmData" :chart-data="thmData" :x-axis-data=pastSevenDaysData />
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
