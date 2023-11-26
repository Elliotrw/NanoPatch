<template>
    <div class="chart-container" style="position: relative; height:40vh; width:80vw">
        <canvas ref="multiLineChart"></canvas>
    </div>
</template>
  
<script>
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
    props: {
        chartData: {
            type: Object,
            required: true
        },
        xAxisData: {
            type: Array,
            required: true
        },
    },
    mounted() {
        const ctx = this.$refs.multiLineChart.getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: this.xAxisData,
                datasets: [
                    {
                        label: 'Nitrogen',
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        data: this.chartData.nitrogen,
                        fill: false,
                    },
                    {
                        label: 'Phosphorus',
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        data: this.chartData.phosphorus,
                        fill: false,
                    },
                    {
                        label: 'Potassium',
                        backgroundColor: 'rgba(255, 206, 86, 0.2)',
                        borderColor: 'rgba(255, 206, 86, 1)',
                        data: this.chartData.potassium,
                        fill: false,
                    }
                ]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'ppm'
                        }
                    }
                }
            }
        });
    }
}
</script>

<style scoped>
</style>
  