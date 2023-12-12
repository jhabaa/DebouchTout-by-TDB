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
let services_cards = document.querySelectorAll('.service_carrousel_item');
let services_index_show = window.innerWidth > 768 ? [0,1,2] : [0];
let service_carrousel = document.querySelector('.service_carrousel');
let carrousel_right_btn = document.querySelector('#btn-right');
let carrousel_left_btn = document.querySelector('#btn-left');
let carrousel = document.querySelector('#carrousel-1');

//INIT AOS
AOS.init(); 

//reviews
let reviews = document.querySelectorAll('.review');
if (current_page == "article") {
    var image_background = document.querySelector('#article_background');
}
console.log("Values are: ", current_page, window.innerWidth);

//MARK: - Carrousel
//MARK: - Services carrousel
var index = 0;
function moveCarrouselLeft() {
    carrousel.appendChild(services_cards[index]);
    index ++;
    if (index == services_cards.length) {
        index = 0;
    }
}
function moveCarrouselRight() {
    if (index <= 0) {
        index = services_cards.length - 1;
    }
    console.log(index);
    carrousel.insertBefore(services_cards[index], services_cards[0]);
    index --;
    
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
        carrousel_left_btn.addEventListener('click', function () {
            //console.log("left");
            //console.log(services_index_show);
            //add last element to the beginning
            //let removedNode = carrousel.removeChild(services_cards[0]);
            moveCarrouselLeft();
        });
        carrousel_right_btn.addEventListener('click', function () {
            //console.log("right");
            //console.log(services_index_show);
            //add last element to the beginning
            //let removedNode = carrousel.removeChild(services_cards[0]);
            moveCarrouselRight();
        });
        
        //MARK: - Automatic carrousel every 5 seconds
        setInterval(function () {
            moveCarrouselLeft();
        }, 5000);
        header_links.forEach(function (item) {
            item.classList.color = "white";
        });
        //always move reviews to the left
//move cards to the left in async
let cardWidth = reviews[0].offsetWidth;
anime({
    targets: reviews,
    translateX: ((window.innerWidth / cardWidth) + ((cardWidth * reviews.length) - (window.innerWidth/cardWidth)) - window.innerWidth) * -1,
    loop: true,
    //delay: anime.stagger(100),
    duration: 50000,
    easing: 'easeInOutSine',
    direction: 'alternate',
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



//if review is out of screen, move it to the right



