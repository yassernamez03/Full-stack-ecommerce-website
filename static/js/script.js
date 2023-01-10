// import Swiper from 'https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.esm.browser.min.js';

let loginForm = document.querySelector('.login-form-container');

document.querySelector('#login-btn').onclick = () => {
    loginForm.classList.toggle('active');
}

document.querySelector('#close-login-btn').onclick = () => {
    loginForm.classList.remove('active');
}

let paymentForm = document.querySelector('.payment');

document.querySelector('#payment-btn').onclick = () => {
    paymentForm.classList.toggle('active');
}

document.querySelector('#close-payment-btn').onclick = () => {
    paymentForm.classList.remove('active');
}

let trakingdiv = document.querySelector('.traking');

document.querySelector('#traking-btn').onclick = () => {
    trakingdiv.classList.toggle('active');
}

document.querySelector('#close-traking-btn').onclick = () => {
    trakingdiv.classList.remove('active');
}