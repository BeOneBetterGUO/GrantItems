document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');

    const ctx = document.getElementById('categoryChart').getContext('2d');
    const pieCtx = document.getElementById('categoryPieChart').getContext('2d');
    const statusCtx = document.getElementById('statusChart').getContext('2d');
    const statusPieCtx = document.getElementById('statusPieChart').getContext('2d');

    const categoryCounts = window.categoryCounts;
    const statusCounts = window.statusCounts;

    console.log('categoryCounts:', categoryCounts);
    console.log('statusCounts:', statusCounts);

    const categoryLabels = categoryCounts.map(item => item.type__name);
    const categoryData = categoryCounts.map(item => item.count);

    const statusLabels = statusCounts.map(item => item.status__name);
    const statusData = statusCounts.map(item => item.count);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: categoryLabels,
            datasets: [{
                label: '每种分类中物品的数量',
                data: categoryData,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    new Chart(pieCtx, {
        type: 'pie',
        data: {
            labels: categoryLabels,
            datasets: [{
                label: '每种分类中物品的比例',
                data: categoryData,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function (tooltipItem) {
                            return tooltipItem.label + ': ' + tooltipItem.raw + ' items';
                        }
                    }
                }
            }
        }
    });

    new Chart(statusCtx, {
        type: 'bar',
        data: {
            labels: statusLabels,
            datasets: [{
                label: '每种状态中物品的数量',
                data: statusData,
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    new Chart(statusPieCtx, {
        type: 'pie',
        data: {
            labels: statusLabels,
            datasets: [{
                label: '每种状态中物品的比例',
                data: statusData,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function (tooltipItem) {
                            return tooltipItem.label + ': ' + tooltipItem.raw + ' items';
                        }
                    }
                }
            }
        }
    });
});