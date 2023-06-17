

let element = document.getElementById('sidebar');
function ToggleMobileNavigation(){
    element.classList.toggle('active');
}


function show1(){
    let element = document.getElementById('extra-nav-items');
    let icon = document.getElementById('user-chev1');
    if(icon.classList.contains('fa-chevron-down')){
      icon.classList.remove('fa-chevron-down');
      icon.classList.add('fa-chevron-up');
    }
    else{
      icon.classList.remove('fa-chevron-up');
      icon.classList.add('fa-chevron-down');
  
    }
   
    element.classList.toggle('active');
  }
  function show2(){
    let element = document.getElementById('extra-nav-items2');
    let icon = document.getElementById('user-chev2');
    if(icon.classList.contains('fa-chevron-down')){
      icon.classList.remove('fa-chevron-down');
      icon.classList.add('fa-chevron-up');
    }
    else{
      icon.classList.remove('fa-chevron-up');
      icon.classList.add('fa-chevron-down');
  
    }
   
    element.classList.toggle('active');
  }
  


  
window.addEventListener('DOMContentLoaded', function() {
  var messageContainers = document.querySelectorAll('.message');

  // Add shake animation class to message containers
  for (var i = 0; i < messageContainers.length; i++) {
      messageContainers[i].classList.add('animated', 'shake');
  }

  // After a delay, remove the shake animation class and fade out the message containers
  setTimeout(function() {
      for (var i = 0; i < messageContainers.length; i++) {
          messageContainers[i].classList.remove('animated', 'shake');
          
          fadeOutElement(messageContainers[i]);
      }
  }, 3000); // Adjust the delay (in milliseconds) as needed

  // Helper function to fade out an element
  function fadeOutElement(element) {
      var opacity = 1;
      var timer = setInterval(function() {
          if (opacity <= 0.1) {
              clearInterval(timer);
              element.style.display = 'none';
          }
          element.style.opacity = opacity;
          element.style.filter = 'alpha(opacity=' + opacity * 100 + ')';
          opacity -= opacity * 0.1;
      }, 20);
  }
});


