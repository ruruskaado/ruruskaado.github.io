const pfp1 = document.querySelector('#pfp1');
const pfp2 = document.querySelector('#pfp2');
const pfp3 = document.querySelector('#pfp3');

const pfps = document.querySelectorAll('.pvp');
const heart = document.querySelectorAll('.heartarrows');
const desc = document.querySelector('#desc');

const desc1 = 'LV8 Pirate<br>YARRR';
const desc2 = 'LV8 Thing<br>chirp';
const desc3 = 'LV8 Butler<br>You called?';



pfp1.addEventListener('focus', () => {
    for (let i of heart) {
        i.classList.remove('heartvisible')
    }
    pfp1.children[1].classList.add('heartvisible');
    desc.innerHTML = desc1
});

pfp2.addEventListener('focus', () => {
    for (let i of heart) {
        i.classList.remove('heartvisible')
    }
    pfp2.children[1].classList.add('heartvisible');
    desc.innerHTML = desc2
});

pfp3.addEventListener('focus', () => {
    for (let i of heart) {
        i.classList.remove('heartvisible')
    }
    pfp3.children[1].classList.add('heartvisible');
    desc.innerHTML = desc3
});
