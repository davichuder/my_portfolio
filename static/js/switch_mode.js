function setThemeCookie(name) {
    document.cookie = `theme=${name}`;
}

function getThemeCookie() {
    return getCookies().theme;
}

const lightTheme = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "light");
    document.querySelector("#icon-theme").setAttribute("class", "bi bi-sun-fill");
    document.querySelector("#icon-logo").setAttribute("class", "icon-logo-dark");
    setThemeCookie("light");
}

const darkTheme = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "dark");
    document.querySelector("#icon-theme").setAttribute("class", "bi bi-moon-fill");
    document.querySelector("#icon-logo").setAttribute("class", "icon-logo-light");
    setThemeCookie("dark");
}

const switchTheme = () => {
    getThemeCookie() === "light" ? darkTheme() : lightTheme();
}

function verifyThemeCookie() {
    theme = getThemeCookie();
    if (theme === "light") { lightTheme(); }
    else if (theme === "dark") { darkTheme(); }
    else { darkTheme(); }
}