


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



//$("document").ready(function(){
//  $(".tab-slider--body").hide();
//  $(".tab-slider--body:first").show();
//});
//
//$(".tab-slider--nav li").click(function() {
//  $(".tab-slider--body").hide();
//  var activeTab = $(this).attr("rel");
//  $("#"+activeTab).fadeIn();
//  if($(this).attr("rel") == "tab2"){
//    $('.tab-slider--tabs').addClass('slide');
//  }else{
//    $('.tab-slider--tabs').removeClass('slide');
//  }
//  $(".tab-slider--nav li").removeClass("active");
//  $(this).addClass("active");
//});


$(function () {
    $('.tab-content:not(:first)').hide();
    $('#tabs-nav a').bind('click', function (e) {
        e.preventDefault();
        $this = $(this);
        $target = $(this.hash);
        $('#tabs-nav a.current').removeClass('current');
        $('.tab-content:visible').slideUp("slow", function () {
            $this.addClass('current');
            $target.slideDown("slow");
        });
    }).filter(':first').click();
});



//$(document).ready(function() {
//    $('.dropdown-content').hover(function(){
//        $('#page-top').addClass('opacity');
//        console.log("hehehehhehe")
//    },
//    function(){
//        $('#page-top').removeClass('opacity');
//    });
//});


$('.dropdown').hover(
       function(){ $('.main-wrapper').addClass('opacity');
        },
       function(){ $('.main-wrapper').removeClass('opacity') ;
       }
)