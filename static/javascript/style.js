window.addEventListener("scroll", function(){
  let nav = document.querySelector("nav");
  nav.classList.toggle("position-sticky", this.window.scrollY > 0);
  const navSticky = document.querySelector("#nav-sticky");
  nav.classList.toggle("navbar-dark", this.window.scrollY === 0);
  if (window.scrollY > 0){
    navSticky.style.backgroundColor = "white";
    navSticky.style.height = "60px";
  } else {
    navSticky.style.backgroundColor = "rgba(0,0,0,0)";
    navSticky.style.height = "100px";
  }
})