// window.addEventListener("scroll", function(){
//   let nav = document.querySelector("nav");
//   nav.classList.toggle("position-sticky", this.window.scrollY > 0);
//   const navSticky = document.querySelector("#nav-sticky");
//   nav.classList.toggle("navbar-dark", this.window.scrollY === 0);
//   if (window.scrollY > 0){
//     navSticky.style.backgroundColor = "white";
//     navSticky.style.height = "60px";
//   } else {
//     navSticky.style.backgroundColor = "rgba(0,0,0,0)";
//     navSticky.style.height = "100px";
//   }
// })

// window.addEventListener("scroll", function(){
//   let nav = document.querySelector("nav");
//   nav.classList.toggle("sticky-top", this.window.scrollY > 0);
//   const navSticky = document.querySelector("#nav-sticky");
//   if (window.scrollY > 0){
//     navSticky.style.height = "60px";
//   } else {
//     navSticky.style.height = "90px";
//   }
// })

// window.addEventListener("scroll", function () {
//         let nav = document.querySelector("nav");
//         nav.classList.toggle("sticky-top", this.window.scrollY > 0);
//         const navSticky = document.querySelector("#nav-sticky");
//         nav.classList.toggle("navbar-dark", this.window.scrollY === 0);
//         const dropMenu = document.querySelector("#drop-menu");
//         const search = document.querySelector("i");
//         const logo = document.querySelector("#logo");
//         const navCol = document.querySelector("#navbarSupportedContent");

//         if (window.scrollY > 0) {
//             navSticky.style.backgroundColor = "white";
//             navSticky.style.height = "60px";
//             dropMenu.style.backgroundColor = "white";
//             navCol.style.backgroundColor = "white";
//             search.style.color = "black";
//             logo.src = "{% static 'images/logo.png' %}";
//         } else {
//             navSticky.style.backgroundColor = "#f08724";
//             navSticky.style.height = "90px";
//             dropMenu.style.backgroundColor = "#f08724";
//             navCol.style.backgroundColor = "#f08724";
//             search.style.color = "white";
//             logo.src = "{% static 'images/logo_w.png' %}";
//         }
//     })

// var swiper = new Swiper('.swiper-container', {
//   navigation: {
//     nextEl: '.swiper-button-next',
//     prevEl: '.swiper-button-prev',
//   },
//   slidesPerView: 1,  //초기값 설정 모바일값이 먼저!!
//   spaceBetween: 10,
//   pagination: {
//     el: ".swiper-pagination",
//     clickable: true,
//   },
//   breakpoints: {
  
//     768: {
//       slidesPerView: 2,  //브라우저가 768보다 클 때
//       spaceBetween: 20,
//     },
//     1024: {
//       slidesPerView: 3,  //브라우저가 1024보다 클 때
//       spaceBetween: 30,
//     },
//     3000: {
//       slidesPerView: 4,  
//       spaceBetween: 0,
//     }
//   },
//   autoplay:{
//       delay: 10000,
//   }
// });