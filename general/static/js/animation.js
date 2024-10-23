var slideRight = {
    interval: '1000',
    delay: 0,
    distance: '20%',
    duration: '1000',
    easing: 'ease-in-out',
    interval: '2000',
    origin: 'right',
    rotate: {},

};
var slideLeft = {
    interval: '1000',
    delay: 0,
    distance: '20%',
    duration: '1000',
    easing: 'ease-in-out',
    interval: '2000',
    origin: 'left',
    opacity: 0.5,
    rotate: {},

};
var slideLeftDelay = {
    interval: 2000,
    delay: 1000,
    distance: '250%',
    duration: 2000,
    easing: 'ease-in-out',
    origin: 'left',
    rotate: {
        x: 50,
        y: 25,
        z: 12,
    },
    opacity: 0,

};
var slideRightDelay = {
    interval: 2000,
    delay: 1000,
    distance: '250%',
    duration: 2000,
    easing: 'ease-in-out',
    origin: 'right',
    rotate: {
        x: 50,
        y: 25,
        z: 12,
    },
    opacity: 0,

};
var slide1 = {
    interval: 500,
    delay: 500,
    distance: '200%',
    duration: 2000,
    easing: 'ease-in-out',
    origin: 'right',
    rotate: {
        x: 160,
        y: 80,
        z: 50,
    },
    opacity: 0,

};
ScrollReveal().reveal('.slide-right', slideRight);
ScrollReveal().reveal('.slide-left', slideLeft);
ScrollReveal().reveal('.slide-left-delay-2000', slideLeftDelay);
ScrollReveal().reveal('.slide-right-delay-2000', slideRightDelay);
ScrollReveal().reveal('.slide1', slide1);