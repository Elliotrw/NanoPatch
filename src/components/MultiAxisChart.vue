<template>
    <div class="chart-container" style="position: relative; height:40vh; width:80vw">
        <canvas ref="multiAxisChart"></canvas>
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
        const ctx = this.$refs.multiAxisChart.getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: this.xAxisData,
                datasets: [
                    {
                        label: 'Temperature',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        data: this.chartData.temperature,
                        fill: false,
                        yAxisID: 'y',
                    },
                    {
                        label: 'Humidity',
                        backgroundColor: 'rgba(153, 102, 255, 0.2)',
                        borderColor: 'rgba(153, 102, 255, 1)',
                        data: this.chartData.humidity,
                        fill: false,
                        yAxisID: 'y1',
                    },
                    {
                        label: 'Moisture',
                        backgroundColor: 'rgba(255, 0, 255, 0.2)', // Magenta with transparency
                        borderColor: 'rgba(255, 0, 255, 1)', // Solid magenta
                        data: this.chartData.moisture,
                        fill: false,
                        yAxisID: 'y1',
                    }
                ]
            },
            options: {
                scales: {
                    y: {
                        title: {
                            display: true,
                            text: '°C'
                        }
                    },
                    y1: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        title: {
                            display: true,
                            text: '%'
                        },

                        // grid line settings
                        grid: {
                            drawOnChartArea: false, // only want the grid lines for one axis to show up
                        },
                    },
                }
            }
        });
    }
}
</script>

<style scoped>
</style>
  