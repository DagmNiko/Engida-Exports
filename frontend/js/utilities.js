let i = document.querySelector('nav .toggle i');
now = 'list'
let smallScreen = document.querySelector('nav .small-screen');

i.addEventListener('click', () => {
    if (now == 'list') {
        i.classList.replace('bi-list', 'bi-x-lg');
        smallScreen.style.opacity = 1;
        smallScreen.style.pointerEvents = 'all'
        now = 'x'
    } else {
        i.classList.replace('bi-x-lg', 'bi-list');
        smallScreen.style.opacity = 0;
        smallScreen.style.pointerEvents = 'none'
        now = 'list'
    }
})