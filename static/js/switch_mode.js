const lightTheme = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "light");
    document.querySelector("#icon-theme").setAttribute("class", "bi bi-sun-fill");
    document.querySelector("#icon-logo").setAttribute("class", "icon-logo-dark");
}

const darkTheme = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "dark");
    document.querySelector("#icon-theme").setAttribute("class", "bi bi-moon-fill");
    document.querySelector("#icon-logo").setAttribute("class", "icon-logo-light");
}

const switchTheme = () => {
    document.querySelector("body").getAttribute("data-bs-theme") === "light" ? darkTheme() : lightTheme();
}