let listbar = document.getElementById("listbar");
let listitems = document.getElementById("listitems");




listbar.addEventListener("click", ()=> {
    listitems.classList.toggle("hidden")
})


// coursel 

 let slideIndex = 0;
  let slides = document.querySelectorAll('.carousel-item');

  function nextSlide() {
    slideIndex = (slideIndex + 1) % slides.length;
    updateCarousel();
  }

  function prevSlide() {
    slideIndex = (slideIndex - 1 + slides.length) % slides.length;
    updateCarousel();
  }

  function updateCarousel() {
    slides.forEach((slide, index) => {
      slide.style.display = index === slideIndex ? 'block' : 'none';
    });
  }

  // Auto-play carousel
  setInterval(nextSlide, 5000); // Change image every 5 seconds

  // Initialize carousel
  updateCarousel();