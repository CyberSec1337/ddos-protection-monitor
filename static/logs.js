// إعداد الرسم البياني الأساسي باستخدام Chart.js
const ctx = document.getElementById('trafficChart').getContext('2d');
const trafficChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Allowed', 'Blocked'],
        datasets: [{
            data: [0, 0],
            backgroundColor: ['#28a745', '#dc3545'],
        }]
    },
    options: {
        responsive: true,
        plugins: {
            tooltip: {
                callbacks: {
                    label: function (context) {
                        return `${context.label}: ${context.raw} requests`;
                    }
                }
            }
        }
    }
});

// مؤشر تحميل
const loadingSpinner = document.querySelector(".loading-spinner");

// تحديث الرسم البياني
function updateChart(allowed, blocked) {
    trafficChart.data.datasets[0].data = [allowed, blocked];
    trafficChart.update();
}

// تحديث الجدول
function updateTable(data) {
    const logBody = document.getElementById('logBody');
    logBody.innerHTML = '';

    if (data.length === 0) {
        Swal.fire({
            icon: 'info',
            title: 'No Traffic Data',
            text: 'No traffic records found.',
        });
        return;
    }

    const fragment = document.createDocumentFragment();
    for (const entry of data) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${entry.ip}</td>
            <td>${entry.timestamp}</td>
            <td class="${entry.status.toLowerCase()}">${entry.status}</td>
            <td>${entry.geo_info.city || 'Unknown'}</td>
            <td>${entry.geo_info.region || 'Unknown'}</td>
            <td>${entry.geo_info.country || 'Unknown'}</td>
        `;
        fragment.appendChild(row);
    }
    logBody.appendChild(fragment);
}

// جلب البيانات
async function fetchData() {
    try {
        loadingSpinner.style.display = 'block';
        const response = await fetch('/traffic');
        if (!response.ok) throw new Error('Failed to fetch traffic data');
        const data = await response.json();

        const allowed = data.traffic_log.filter(entry => entry.status === 'Allowed').length;
        const blocked = data.traffic_log.filter(entry => entry.status === 'Blocked').length;

        updateChart(allowed, blocked);
        updateTable(data.traffic_log);
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: error.message,
        });
    } finally {
        loadingSpinner.style.display = 'none';
    }
}

// تحديث البيانات دوريًا
document.addEventListener("DOMContentLoaded", () => {
    fetchData();
    setInterval(fetchData, 5000);
});
