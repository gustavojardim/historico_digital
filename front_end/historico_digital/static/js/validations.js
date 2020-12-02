function validatePasswordsMatch(){
    let password = document.getElementById("id_password")
    let confirm_password = document.getElementById("id_password_1");
    if (confirm_password.value != "") {
        if(password.value != confirm_password.value) {
            confirm_password.setCustomValidity("Passwords Don't Match");
        } else {
            confirm_password.setCustomValidity('');
        }
    }
    document.getElementById("id_password_1").focus();
}

function validePasswordRequirements(){
    let password = document.getElementById("id_password")
    let str = password.value;
    if (str.match(/[a-z]/g) &&
        str.match(/[A-Z]/g) &&
        str.match(/[0-9]/g) &&
        str.match(/[^a-zA-Z\d]/g) &&
        str.length >= 6)
        password.setCustomValidity("");
    else
        password.setCustomValidity("Password does not meet the requirements");
    document.getElementById("id_password").focus();
}
