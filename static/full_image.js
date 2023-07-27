document.addEventListener("DOMContentLoaded", function () {
    var img = document.getElementById("fullScreenImage");
  
    if (img) {
      img.addEventListener("click", function () {
        if (img.requestFullscreen) {
          img.requestFullscreen();
        } else if (img.mozRequestFullScreen) {
          img.mozRequestFullScreen();
        } else if (img.webkitRequestFullscreen) {
          img.webkitRequestFullscreen();
        } else if (img.msRequestFullscreen) {
          img.msRequestFullscreen();
        }
      });
    }
  });