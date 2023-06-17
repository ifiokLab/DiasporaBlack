
const sideMenu = document.querySelector("aside")
const menuBtn = document.querySelector("#menu_btn")
const closeBtn = document.querySelector("#close_btn")
const themeToggler = document.querySelector(".theme_toggler")

// show sidebar
menuBtn.addEventListener('click', ()=> {
    //sideMenu.style.display = "block";
    sideMenu.classList.toggle('show');
})

// hide sidebar
closeBtn.addEventListener('click', ()=> {
    //sideMenu.style.display = "none";
    sideMenu.classList.remove('show');
})

// change theme
themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables')

    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})


document.addEventListener('DOMContentLoaded', function() {
            const customerStatsCtx = document.getElementById('customerStatsChart').getContext('2d');
            const customerStatsData = {
                labels: ['January', 'February', 'March', 'April', 'May'],
                datasets: [
                    {
                        label: 'New Customers',
                        data: [20, 30, 25, 40, 35],
                        backgroundColor: 'rgba(54, 162, 235, 0.7)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 2
                    },
                    {
                        label: 'Total Customers',
                        data: [100, 130, 120, 150, 140],
                        backgroundColor: 'rgba(75, 192, 192, 0.7)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 2
                    }
                ]
            };
            const customerStatsOptions = {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            precision: 0,
                            stepSize: 50
                        }
                    }
                },
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            font: {
                                size: 14
                            }
                        }
                    }
                },
                animation: {
                    duration: 0
                }
            };
            new Chart(customerStatsCtx, {
                type: 'bar',
                data: customerStatsData,
                options: customerStatsOptions
            });

            const recentCustomersCtx = document.getElementById('recentCustomersChart').getContext('2d');
            const recentCustomersData = {
                labels: ['January', 'February', 'March', 'April', 'May'],
                datasets: [
                    {
                        label: 'Recent Customers',
                        data: [5, 8, 3, 6, 4],
                        backgroundColor: 'rgba(255, 99, 132, 0.7)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 2,
                        pointBackgroundColor: 'rgba(255, 99, 132, 1)',
                        pointRadius: 4,
                        fill: false,
                        tension: 0.4
                    }
                ]
            };
            const recentCustomersOptions = {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            precision: 0,
                            stepSize: 5
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: true
                    }
                },
                interaction: {
                    intersect: false,
                    mode: 'index'
                },
                animation: {
                    duration: 0
                }
            };
            new Chart(recentCustomersCtx, {
                type: 'line',
                data: recentCustomersData,
                options: recentCustomersOptions
            });
});