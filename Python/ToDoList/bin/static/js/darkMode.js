
// document
//     .getElementsByClassName("add-task")[0]
//     .addEventListener("click", (e) => {
//         saveCookie();
//     });

// if (document.cookie) {
//     toggleDarkMode();
// }

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

    document
        .getElementsByClassName("dark-mode-btn")[0]
        .classList.toggle("dark");

    document.getElementsByClassName("add-task-btn")[0].classList.toggle("dark");
}

function deleteAllCookies() {
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }

    console.log("deleted cookie: " + document.cookie);
}

function saveCookie() {
    if (document.cookie) {
        deleteAllCookies();
    } else {
        document.cookie = "dark-mode=true";

        console.log("new cookie: " + document.cookie);
    }
}
