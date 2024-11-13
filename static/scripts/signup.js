// Signup validation. Credit w3schools
var myInput = document.getElementById("password");
var lower = document.getElementById("lower");
var upper = document.getElementById("upper");
var number = document.getElementById("number");
var special = document.getElementById("special");
var length = document.getElementById("length");

onload = function() {
    document.getElementById("message").style.visibility = "hidden"
    document.getElementById("message").style.height = "0"
}
myInput.onfocus = function() {
    document.getElementById("message").style.visibility = "visible"
    document.getElementById("message").style.height = "inherit"
}
myInput.onblur = function() {
    document.getElementById("message").style.visibility = "hidden"
    document.getElementById("message").style.height = "0"
}
myInput.onkeyup = function() {

    // Validate lowercase letters
    var lowerCaseLetters = /[a-z]/g;
    if(myInput.value.match(lowerCaseLetters)) {  
        lower.classList.remove("invalid");
        lower.classList.add("valid");
    } else {
        lower.classList.remove("valid");
        lower.classList.add("invalid");
    }

    // Validate capital letters
    var upperCaseLetters = /[A-Z]/g;
    if(myInput.value.match(upperCaseLetters)) {  
        upper.classList.remove("invalid");
        upper.classList.add("valid");
    } else {
        upper.classList.remove("valid");
        upper.classList.add("invalid");
    }

    // Validate numbers
    var numbers = /[0-9]/g;
    if(myInput.value.match(numbers)) {  
        number.classList.remove("invalid");
        number.classList.add("valid");
    } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
    }

    // Validate specials
    var specials = /[^\w\s]/g;
    if(myInput.value.match(specials)) {  
        special.classList.remove("invalid");
        special.classList.add("valid");
    } else {
        special.classList.remove("valid");
        special.classList.add("invalid");
    }

    // Validate length
    if(myInput.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
    }
}