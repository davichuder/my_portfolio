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
    document.querySelector("#cookie-policy").style.visibility = 'hidden';
    setCookiePolicyCookie(true);
}

const showCookie = () => {
    document.querySelector("#cookie-policy").style.visibility = 'visible';
    setCookiePolicyCookie(false);
}

function verifyCookiePolicyCookie() {
    cookiePolicy = getCookiePolicyCookie();
    if (cookiePolicy === "false" | cookiePolicy === undefined) { showCookie(); }
}