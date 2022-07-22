function toggleDarkMode() {
    saveCookie();

    document.getElementsByTagName("body")[0].classList.toggle("body-dark-mode");

    document.getElementsByClassName("header")[0].classList.toggle("dark");

    document.getElementsByClassName("navbar-item")[0].classList.toggle("dark");

    document.querySelectorAll(".card-item.head").forEach((el) => {
        el.classList.toggle("dark");
    });

    document.querySelectorAll(".card-item.body").forEach((el) => {
        el.classList.toggle("dark");
    });

    document.querySelectorAll(".input-field").forEach((el) => {
        el.classList.toggle("dark");
    });

    document.querySelectorAll(".inp-label").forEach((el) => {
        el.classList.toggle("dark");
    });

    document.getElementsByClassName("dark-mode-btn")[0].classList.toggle("dark");

    document.getElementsByClassName("add-task-btn")[0].classList.toggle("dark");
}
