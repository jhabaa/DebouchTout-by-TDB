let burger = document.querySelector('.burger');
let bugerChid1 = burger.firstElementChild;
let bugerChid2 = burger.lastElementChild;
let bar = document.querySelector('#navbar');

burger.addEventListener('click', function () {
    bugerChid2.classList.toggle('active');
    bugerChid1.classList.toggle('active2');
    bar.classList.toggle('extend');
});