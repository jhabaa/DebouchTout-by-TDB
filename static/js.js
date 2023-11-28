let burger = document.querySelector('.burger');
//let bugerChid1 = burger.firstElementChild;
//let bugerChid2 = burger.lastElementChild;
let bar = document.querySelector('#navbar');
let navBarOpacity = document.querySelector('.back');
let video = document.querySelector('#video');
let logo = document.querySelector('#logo');
let header_links = document.querySelectorAll('.header_link');
let articles_page = document.querySelector('#articles');
let current_page = document.querySelector('#body').dataset.page;
if (current_page == "article") {
    var image_background = document.querySelector('#article_background');
}

/*
burger.addEventListener('click', function () {
    bugerChid2.classList.toggle('active');
    bugerChid1.classList.toggle('active2');
    bar.classList.toggle('extend');
});
*/
// Get scroll level
console.log(current_page)
let scroll = document.querySelector('#body');

//MARK: - Depending of the page we are on, we change the navbar links colors
switch (current_page) {
    case "home":
        
        header_links.forEach(function (item) {
            item.classList.color = "white";
        });
        break;
    case "articles":
        navBarOpacity.style.opacity = 0.6;
        // Set links color to black and invert logo
        header_links.forEach(function (item) {
            item.style.color = "black";
            logo.style.filter = "invert(1)";
        });
        break;
    case "about":
        //Set gradient on
        //navBarOpacity.style.background = "linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0.5) 100%)";
        navBarOpacity.style.opacity = 0.6;
    case "article":
        //Set color
        header_links.forEach(function (item) {
            item.style.color = "black";
        });
        //invert logo
        logo.style.filter = "invert(1)";
       // navBarOpacity.style.background = "linear-gradient(180deg, rgba(1,1,1,1) 0%, rgba(1,1,1,0.5) 100%)";
        navBarOpacity.style.opacity = 0.6;
    default:
        break;
}

    //Output scrollY value
window.onscroll = function () {
    console.log(scrollY);
    if (current_page == "home") {
        // Change navbar opacity
        navBarOpacity.style.opacity = scrollY / 100;
    }
    
    if (current_page == "article") {
        // Change backround image opacity
        image_background.style.opacity = 1 - scrollY / window.innerHeight;
        
    }
    

    if (current_page == "home") {
        header_links.forEach(function (item) {
            // Change links color
            item.style.filter = 'invert(' + scrollY / 100 + ')';
        });
        // Change logo colors by invert
        logo.style.filter = 'invert(' + scrollY / 100 + ')';
        // Change video opacity
        video.style.opacity = 1 - scrollY / 1000;
    }
}


