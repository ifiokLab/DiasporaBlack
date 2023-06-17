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
    const monthlyOrdersCtx = document.getElementById('monthlyOrdersChart').getContext('2d');
    const monthlyOrdersData = {
        labels: [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ],
        datasets: [
            {
                label: 'Orders',
                data: [250, 180, 300, 150, 200, 400, 380, 270, 350, 280, 320, 410],
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2,
                fill: false,
                tension: 0.4
            }
        ]
    };
    const monthlyOrdersOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    precision: 0,
                    stepSize: 500
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
            duration: 0 // Disable animations
        }
    };
    new Chart(monthlyOrdersCtx, {
        type: 'line',
        data: monthlyOrdersData,
        options: monthlyOrdersOptions
    });

    const orderStatusCtx = document.getElementById('orderStatusChart').getContext('2d');
    const orderStatusData = {
        labels: ['Pending', 'Ordered', 'Delivered'],
        datasets: [
            {
                label: 'Order Status',
                data: [15, 35, 30],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'blue'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 2
            }
        ]
    };
    const orderStatusOptions = {
        responsive: true,
        maintainAspectRatio: false,
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
            duration: 0 // Disable animations
        }
    };
    new Chart(orderStatusCtx, {
        type: 'pie',
        data: orderStatusData,
        options: orderStatusOptions
    });
});