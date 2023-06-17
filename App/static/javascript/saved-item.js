

function removeProduct(productId) {
    const xhr = new XMLHttpRequest(); // Create a new XMLHttpRequest object
    xhr.open('POST', `/remove-save-product/${productId}/`); // Set up the request
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // Set the request header
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
  
    xhr.onload = function() {
      if (xhr.status === 200) {
          console.log('success');
          location.reload();
         
      } else {
        console.error(`Server returned status ${xhr.status}`);
        //window.location.href = '/customer-login/'; 
      }
    };
    xhr.onerror = function() {
      console.error('Request failed');
      
    };
    xhr.send();
}