const navbarLoginButton = document.querySelector(".navbar-login-button");
const loginButton = document.querySelector(".login");
const loginCancelButton = document.querySelector(".login-buttons-cancel");
const backgroundClick = document.querySelector(".background-img");

navbarLoginButton.addEventListener("click", function () {
  document.querySelector(".login").style.opacity = 0.8;
  backgroundClick.style.filter = "blur(5px)";
});

loginCancelButton.addEventListener("click", function () {
  document.querySelector(".login").style.opacity = 0;
  backgroundClick.style.filter = "blur(0px)";
});

backgroundClick.addEventListener("click", function () {
  document.querySelector(".login").style.opacity = 0;
  backgroundClick.style.filter = "blur(0px)";
});
