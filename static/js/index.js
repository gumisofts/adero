
let header_menu=document.getElementById('header-menu');
let menu_btn=document.getElementById('header-menu-more');
let cancel_btn=document.getElementById('header-menu-less');

function toggleMenu(){
  cancel_btn.classList.toggle('hidden');
  menu_btn.classList.toggle('hidden');
  header_menu.classList.toggle('hidden');
  
}
cancel_btn.addEventListener('click',toggleMenu)
menu_btn.addEventListener('click',toggleMenu)
// Detect request animation frame
let scroll =
  window.requestAnimationFrame ||
  // IE Fallback
  function (callback) {
    window.setTimeout(callback, 1000 / 60);
  };
let elementsToShowBottom = document.querySelectorAll("div.animate-from-bottom");
let elementsToShowLeft = document.querySelectorAll("div.animate-from-left");
let elementsToShowRigth = document.querySelectorAll("div.animate-from-right");
function loop() {
  elementsToShowBottom.forEach(function (element) {
    if (isElementInViewport(element)) {
      element.classList.remove("opacity-0","translate-y-28");
      
    }else{
      element.classList.add("opacity-0","translate-y-28");
    }
  }
);
elementsToShowRigth.forEach(function (element) {
    if (isElementInViewport(element)) {
      element.classList.remove("opacity-0","translate-x-28");
      
    }else{
      element.classList.add("opacity-0","translate-x-28");
    }
  }
);
  elementsToShowLeft.forEach(function (element) {
    if (isElementInViewport(element)) {
      element.classList.remove("opacity-0","-translate-x-28");
      
    }else{
      element.classList.add("opacity-0","-translate-x-28");
    }
  }
);

  scroll(loop);
}

// Call the loop for the first time
loop();

// Helper function from: http://stackoverflow.com/a/7557433/274826
function isElementInViewport(el) {
  // special bonus for those using jQuery
  if (typeof jQuery === "function" && el instanceof jQuery) {
    el = el[0];
  }
  var rect = el.getBoundingClientRect();
  return (
    (rect.top <= 0 && rect.bottom >= 0) ||
    (rect.bottom >=
      (window.innerHeight || document.documentElement.clientHeight) &&
      rect.top <=
        (window.innerHeight || document.documentElement.clientHeight)) ||
    (rect.top >= 0 &&
      rect.bottom <=
        (window.innerHeight || document.documentElement.clientHeight))
  );
}

header = document.getElementById("header");
let body=document.body;
function onScroll(event) {

  if (checkScrollDirectionIsUp(event)) {
    header.classList.remove('-top-80');
  } else {
    header.classList.add('-top-80');
  }
}
body.addEventListener('wheel',onScroll)

var scrollableElement = document.body; //document.getElementById('scrollableElement');



function checkScrollDirectionIsUp(event) {
  if (event.wheelDelta) {
    return event.wheelDelta > 0;
  }
  return event.deltaY < 0;
}