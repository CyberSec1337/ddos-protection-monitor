// إعداد الرسم البياني الإضافي (Vehicle Counts)
const vehicleCtx = document.getElementById('vehicleChart').getContext('2d');
new Chart(vehicleCtx, {
    type: 'line',
    data: {
        labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00', '24:00'],
        datasets: [{
            label: 'Vehicle Counts',
            data: [100, 200, 300, 400, 350, 250, 150],
            borderColor: '#00ff00',
            backgroundColor: 'rgba(0, 255, 0, 0.1)',
            fill: true,
            tension: 0.4,
        }]
    },
    options: {
        plugins: {
            legend: { display: true, labels: { color: '#00ff00' } }
        },
        scales: {
            x: {
                grid: { color: '#005500' },
                ticks: { color: '#00ff00' }
            },
            y: {
                grid: { color: '#005500' },
                ticks: { color: '#00ff00' }
            }
        }
    }
});

// إعداد الرسم البياني الإضافي (Traffic Flow Analysis)
const flowCtx = document.getElementById('flowChart').getContext('2d');
new Chart(flowCtx, {
    type: 'bar',
    data: {
        labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00', '24:00'],
        datasets: [{
            label: 'Inbound',
            data: [50, 60, 80, 120, 100, 70, 30],
            backgroundColor: 'rgba(0, 255, 0, 0.4)',
            borderColor: '#00ff00',
            borderWidth: 1,
        }, {
            label: 'Outbound',
            data: [40, 50, 70, 100, 80, 60, 20],
            backgroundColor: 'rgba(0, 255, 0, 0.2)',
            borderColor: '#00ff00',
            borderWidth: 1,
        }]
    },
    options: {
        plugins: {
            legend: { labels: { color: '#00ff00' } }
        },
        scales: {
            x: { grid: { color: '#005500' }, ticks: { color: '#00ff00' } },
            y: { grid: { color: '#005500' }, ticks: { color: '#00ff00' } }
        }
    }
});
