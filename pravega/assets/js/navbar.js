document.addEventListener("DOMContentLoaded", function () {
  // Fetch the navigation bar content
  fetch('/pravega/header.html')
    .then(response => response.text())
    .then(data => {
      // Inject the navigation bar content into a container on the page
      const navContainer = document.getElementById('header-container');
      if (navContainer) {
        navContainer.innerHTML = data;
      }
    })
    .catch(error => {
      console.error('Error fetching navigation bar:', error);
    });
});