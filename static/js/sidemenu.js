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

// hamburger-btn handler
const menuBtn = document.querySelector('.menu-btn');
let menuOpened = false;
// let collapseLinks = document.querySelectorAll(".logout .item2 .nav .nav__list")

menuBtn.addEventListener('click', function() {
    if (!menuOpened) {

        $.each($(".logout .item2 .nav .nav__list .collapse"), function(indexInArray, valueOfElement) {
            // $(valueOfElement).css("display", "block !important");
            $(valueOfElement).attr("style", "display:grid !important");
        });
        // $(".nav__link .topmenu-link-description-logout2").attr("style", "display:grid !important");
        $(".logout .item2 .nav .topmenu-link-description-logout2").css("display", "grid !important");

        console.log($(".menu-burger:before"));
        $(".menu-burger::before").attr("style", "after:transform: rotate(-45deg);");
        $(".menu-burger::after").attr("style", "after:transform: rotate(45deg);");
        // $(".logout .item2 .nav .nav__list .collapse").addClass("display");
        // document.querySelectorAll(".logout .item2 .nav .nav__list .collapse").style.display = "block !important";
        menuOpened = true;
    } else {
        $.each($(".logout .item2 .nav .nav__list .collapse"), function(indexInArray, valueOfElement) {
            $(valueOfElement).attr("style", "display:none !important");
        });
        $(".nav__link .topmenu-link-description-logout2").attr("style", "display:none !important");

        menuBtn.classList.remove('open');
        menuOpened = false;
    }
});