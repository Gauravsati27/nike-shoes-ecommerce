let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

// Hide menu on scroll
let prevScrollPos = window.pageYOffset;
window.onscroll = () =>{
    let currentScrollPos = window.pageYOffset;
    
    if (prevScrollPos > currentScrollPos) {
        document.querySelector('header').style.top = "0";
    } else {
        document.querySelector('header').style.top = "-100px";
    }
    prevScrollPos = currentScrollPos;

    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
}

// Add smooth scroll behavior to navigation links
document.querySelectorAll('.nav-item').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({
            behavior: 'smooth'
        });
        
        // Close mobile menu after clicking
        menu.classList.remove('fa-times');
        navbar.classList.remove('active');
    });
}); 