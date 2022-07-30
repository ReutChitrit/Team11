const navSlide = () => {
   const burger = document.querySelector('.burger');
   const nav = document.querySelector('.nav-links');
   const navLinks = document.querySelectorAll('.nav-links li');


   burger.addEventListener('click', () => {
      nav.classList.toggle('nav-active');


      //Animate Links
      navLinks.forEach((link, index) => {
         if (link.style.animation) {
            link.style.animation = '';
         } else {
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`
         }
      });
      //Burger Animation
      burger.classList.toggle('toggle');
   });
}


navSlide();
//pull the pathname from window location
const activePage = window.location.pathname;
/*create an array of the links in nav,
compare each to pathname and mark the one that is active
*/
const navLinks = document.querySelectorAll('nav a').forEach(link => {
   if (link.href.includes(`${activePage}`)) {
      link.classList.add('active');
   }
});


function clearForm() {
   var emailInput = document.getElementById("email");
   var usageInput = document.getElementById("usage");
   var textAreaInput = document.getElementById("textArea");
   var PhoneNumberInput = document.getElementById("PhoneNumber");
   if (emailInput.value != "" || usageInput.value != "" || textAreaInput.value != "" || PhoneNumberInput.value != "") {
      emailInput.value = "";
      usageInput.value = "";
      textAreaInput.value = "";
      PhoneNumberInput.value = "";
   }
}


//disable typing in dropbox (combobox)
function IgnoreAlpha(e) {
   if (!e) {
      e = window.event;
   }
   if (e.keyCode >= 65 && e.keyCode <= 90) // A to Z
   {
      e.returnValue = false;
      e.cancel = true;
   }
}


function GetLocation() {
   if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
   }
}


function showPosition(position) {
   fetch('http://127.3.3.7:5000/get_city_by_geolocation?' + new URLSearchParams({
      latitude: position.coords.latitude,
      longitude: position.coords.longitude
   }))
}


function showDiv(toggle) {
   document.getElementById(toggle).style.display = 'block';
}


function hideButtons(toggle2) {
   var myClasses = document.getElementsByClassName(toggle2),
      i = 0,
      l = myClasses.length;

   for (i; i < l; i++) {
      myClasses[i].style.display = 'none';
   }
}

function showDiv2(toggle2) {
   document.getElementById(toggle2).style.display = 'block';
   hideButtons(toggle2);
}