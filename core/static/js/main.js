// Navbar
var nav = document.querySelector(".navbar");

window.addEventListener("scroll", function(event) {
    event.preventDefault();
    if (window.scrollY <= 50) {
        nav.style.backgroundColor = "transparent";
        nav.style.boxShadow = "0px 0px 0px rgba(0, 0, 0, 0.5)";

    } else {
        nav.style.background = "#333952";
        nav.style.boxShadow = "0px 4px 5px rgba(0, 0, 0, 0.5)";
    }
});

// Modais
//// PEGANDO os botões que abrem o Modal:
var modalBtns = document.querySelectorAll(".modal-open");

//// ABRINDO Modais ao clicar nos botoes
modalBtns.forEach(function(btn) {
    btn.onclick = function() {
        var modal = btn.getAttribute("data-modal");
        document.getElementById(modal).style.display = "block";
    };
});

//// PEGANDO os botões que fecham o Modal
var closeBtns = document.querySelectorAll(".modal-close");

//// FECHANDO Modais
closeBtns.forEach(function(btn) {
    btn.onclick = function() {
        var modal = (btn.closest(".modal").style.display = "none");
    };
});

//// FECHANDO Modais ao clicar fora da tela
window.onclick = function(e) {
    if (e.target.className === "modal") {
        e.target.style.display = "none"
    }
}