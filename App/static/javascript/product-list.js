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


