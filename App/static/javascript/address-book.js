
var formGroups = document.querySelectorAll(".input-card");

// Attach event listeners to each input field
formGroups.forEach(function(formGroup) {
  var input = formGroup.querySelector("input");
  
  if(input.value != ''){
    formGroup.classList.add("active");
  }
 
  // Add focus event listener
  input.addEventListener("focus", function() {
    formGroup.classList.add("active");
  });

  // Add blur event listener
  input.addEventListener("blur", function() {
    if (input.value === "") {
      formGroup.classList.remove("active");
    }
  });
});