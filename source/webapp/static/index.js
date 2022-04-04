

async function addQuote(event){
    // console.log('api/v1/quote/')
    form = document.getElementById("quote_form")
    form.style.display = "block"
}
function getCookie(cookieName){
    let cookie = {}
    // console.log(document.cookie)
    document.cookie.split(';').forEach(function (el){
        let [key, value] = el.split('=');
        cookie[key.trim()] = value;

    })
    return cookie[cookieName];

}

function takeValues(){
    let name = document.getElementById("name").value;
    let text = document.getElementById("text").value;
    let email = document.getElementById("email").value;
    return {"name": name, "text": text, "email": email}
}

async function createQuote(event){
    event.preventDefault();

    let urlCsrf = event.target.dataset.toCsrf;
    await fetch(urlCsrf)
    let csrf = getCookie("csrftoken");

    let requestBody = {method: "POST"};
    requestBody["headers"] = {"X-CSRFToken": csrf};
    requestBody["headers"]["content-type"] = "application/json";

    let content = takeValues()

    requestBody["body"] = JSON.stringify(content)
    url = "api/v1/quote/"
    let response = await fetch(url, requestBody);

}

