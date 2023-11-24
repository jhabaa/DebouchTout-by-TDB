let burger = document.querySelector('.burger');
let bugerChid1 = burger.firstElementChild;
let bugerChid2 = burger.lastElementChild;
let bar = document.querySelector('#navbar');
let navBarOpacity = document.querySelector('.back');

burger.addEventListener('click', function () {
    bugerChid2.classList.toggle('active');
    bugerChid1.classList.toggle('active2');
    bar.classList.toggle('extend');
});

// Get scroll level
let scroll = document.querySelector('#body');
//Output scrollY value
window.onscroll = function () {
    console.log(scrollY);
    // Change navbar opacity
        navBarOpacity.style.opacity = scrollY / 100;
    
}