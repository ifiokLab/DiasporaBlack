
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
    const ctx = document.getElementById('monthlyChart').getContext('2d');
    const chartData = {
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
                data: [250, 180, 300, 150, 200, 400, 380, 270, 350, 280, 3200, 410],
                backgroundColor: 'rgba(54, 162, 235, 0.7)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2
            },
            {
                label: 'Sales',
                data: [2000, 2200, 1800, 2100, 2500, 2800, 3000, 2900, 2700, 2300, 2200, 2500],
                backgroundColor: 'rgba(255, 99, 132, 0.7)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 2
            }
        ]
    };
    const options = {
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
        }
    };
    new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: options
    });
});
