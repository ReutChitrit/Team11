const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav-links');
  const navLinks = document.querySelectorAll('.nav-links li');


  burger.addEventListener('click', () => {
     //Toggle Nav
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

/*create an arey of the links in nav, 
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

function sendMessageAfterSumbit(e) {

  alert("הודעתך נשלחה בהצלחה");
  e.preventDefault();

}

//reset = clear input after submit
const form = document.getElementById('contactUs');

form.addEventListener('submit', function handleSubmit(event) {
  event.preventDefault();

  form.reset();
});


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
     console.log("in get location");
     navigator.geolocation.getCurrentPosition(showPosition);
  } else {
     document.getElementById("p").innerHTML = "לא הצלחנו למצוא את המיקום שלך";
  }
}


function showPosition(position) {
  var x = document.getElementById("p");
  var y = document.getElementById("locaionImg");
  x.innerHTML = "Your In <br>" + "Latitude: " + position.coords.latitude +
     "<br>Longitude: " + position.coords.longitude;
  y.innerHTML = "try me again";
  console.log(position);
}

function moveToNearBeaches() {
  window.location.href = "near beaches.html"
}