function getCookies() {
    return document.cookie
        .split(';')
        .map(cookie => cookie.split('='))
        .reduce((accumulator, [key, value]) => ({ ...accumulator, [key.trim()]: decodeURIComponent(value) }), {});
}

function setCookiePolicyCookie(state) {
    document.cookie = `cookiePolicy=${state}`;
}

function getCookiePolicyCookie() {
    return getCookies().cookiePolicy;
}

const hideCookie = () => {
    document.querySelector("#cookie-policy").setAttribute("hidden", "true");
    setCookiePolicyCookie(true);
}

function verifyCookiePolicyCookie() {
    cookiePolicy = getCookiePolicyCookie();
    if (cookiePolicy === "true") {hideCookie();}
}