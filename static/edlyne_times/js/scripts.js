var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}
  x[myIndex-1].style.display = "block";
  setTimeout(carousel, 3000); // Change image every 3 seconds
}


//nav background color change onscroll

var myNav = document.getElementById('main_header');
var myNav_a = document.getElementById('main_header');
window.onscroll = function () {
    "use strict";
     if (document.body.scrollTop >= 200 || document.documentElement.scrollTop >= 200 )
    {
        myNav.classList.add("nav-colored");
        myNav.classList.remove("nav-transparent");
    }
    else {
        myNav.classList.add("nav-transparent");
        myNav.classList.remove("nav-colored");
    }
};




// const pass_field = document.querySelector('.pass-key');
//      const showBtn = document.querySelector('.show');
//      showBtn.addEventListener('click', function(){
//       if(pass_field.type === "password"){
//         pass_field.type = "text";
//         showBtn.textContent = "HIDE";
//         showBtn.style.color = "#3498db";
//       }else{
//         pass_field.type = "password";
//         showBtn.textContent = "SHOW";
//         showBtn.style.color = "#222";
//       }
//      });
//
//$(document).ready(function(){
//  $(".dropdown-toggle").dropdown();
//});