/*===== LINK ACTIVE  =====*/
const linkColor = document.querySelectorAll(".nav__link");

function colorLink() {
    linkColor.forEach((l) => l.classList.remove("active"));
    this.classList.add("active");
}
linkColor.forEach((l) => l.addEventListener("click", colorLink));

/*===== COLLAPSE MENU  =====*/
const linkCollapse = document.getElementsByClassName("collapse__link");
let i;

for (i = 0; i < linkCollapse.length; i++) {
    linkCollapse[i].addEventListener("click", function() {
        // linkCollapse.forEach(function () {
        //   collapseMenu.classList.remove("showCollapse");
        // });
        const collapseMenu = this.nextElementSibling;
        // collapseMenu.classList.remove("showCollapse");
        console.log(collapseMenu);
        collapseMenu.classList.toggle("showCollapse");

        const rotate = collapseMenu.previousElementSibling;
        console.log(rotate);
        rotate.classList.toggle("rotate");
    });
}

const logoutBtn = document.querySelector(".topmenu-link-description-logout");

logoutBtn.addEventListener("click", function() {
    document.querySelector(".logout-form").style.opacity = 1;
    document.querySelector(".logout-form").style.visibility = "visible";
    // document.querySelector(".grid-container").style.filter = "blur(2px)";
});

const logoutBtn2 = document.querySelector(".topmenu-link-description-logout2");

logoutBtn2.addEventListener("click", function() {
    document.querySelector(".logout-form").style.opacity = 1;
    document.querySelector(".logout-form").style.visibility = "visible";
    // document.querySelector(".grid-container").style.filter = "blur(2px)";
});

const cancelBtn = document.querySelector(".logout-form-button-cancel");

cancelBtn.addEventListener("click", function() {
    document.querySelector(".logout-form").style.opacity = 0;
    document.querySelector(".logout-form").style.visibility = "hidden";
    // document.querySelector(".grid-container").style.filter = "blur(0px)";
});