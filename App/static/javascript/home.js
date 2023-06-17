const swiper = new Swiper('.swiper', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  autoplay: {
    delay: 3000, // 3 seconds
    disableOnInteraction: false, // Allow manual interaction to pause autoplay
  },

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    clickable: true, // Enable clickable pagination dots
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  
});





var gallery = document.getElementById("gallery-slider");
var prevBtn = document.getElementById("prev-button");
var nextBtn = document.getElementById("next-button");
var cardCount = 0;
var startIndex = 0;

function updateCards() {
  var cards = gallery.getElementsByClassName("gallery-card");
  for (var i = 0; i < cards.length; i++) {
    if (i >= startIndex && i < startIndex + cardCount) {
      cards[i].style.display = "block";
    } else {
      cards[i].style.display = "none";
    }
  }
}

/*function updateButtonVisibility() {
  prevBtn.style.display = startIndex > 0 ? "block" : "none";
  nextBtn.style.display =
    startIndex + cardCount < gallery.getElementsByClassName("gallery-card").length
      ? "block"
      : "none";
} */

function updateGallery() {
  updateCards();
  //updateButtonVisibility();
}

function calculateCardCount() {
  if (window.innerWidth >= 1024) {
    cardCount = 8;
  } else if (window.innerWidth >= 768) {
    cardCount = 4;
  } else {
    cardCount = 3;
  }
}

prevBtn.addEventListener("click", function() {
  startIndex -= cardCount;
  if (startIndex < 0) {
    startIndex = 0;
  }
  updateGallery();
});

nextBtn.addEventListener("click", function() {
  startIndex += cardCount;
  var maxIndex =
    gallery.getElementsByClassName("gallery-card").length - cardCount;
  if (startIndex > maxIndex) {
    startIndex = maxIndex;
  }
  updateGallery();
});

window.addEventListener("resize", function() {
  calculateCardCount();
  updateGallery();
});

// Initialize the gallery
calculateCardCount();
updateGallery();

//{% url 'product_detail' data.id %}
