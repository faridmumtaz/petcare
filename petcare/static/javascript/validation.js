var click;

function clearErrors(id) {
    element = document.getElementById(id);
    element.getElementsByClassName('error')[0].innerHTML = "";
}

function seterror(id, error) {
    element = document.getElementById(id);
    element.getElementsByClassName('error')[0].innerHTML = error;

}

function firstNameCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /^[a-zA-Z]+$/;

    if (!regName.test(name)) {
        seterror("fname", "*only use A-Z or a-z");
        click = false;
    } else {
        clearErrors("fname");
        click = true;
    }
}

function lastNameCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /^[a-zA-Z]+$/;

    if (!regName.test(name)) {
        seterror("lname", "*only use A-Z or a-z");
        click = false;
    } else {
        clearErrors("lname");
        click = true;
    }
}

function userNameCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /^[A-Za-z0-9_.]{3,20}$/;

    if (!regName.test(name)) {
        seterror("uname", "*only use A-Z a-z 0-9 _ .");
        click = false;
    } else {
        clearErrors("uname");
        click = true;
    }
}

function eMailCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    if (!regName.test(name)) {
        seterror("email", "*give a valid email address");
        click = false;
    } else {
        clearErrors("email");
        click = true;
    }
}

function phoneNumberCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /^[6-9][0-9]{9}$/;

    if (!regName.test(name)) {
        seterror("phone", "*inappropriate number");
        click = false;
    } else {
        clearErrors("phone");
        click = true;
    }
}

function passwordCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[_@$!%*#?&])[A-Za-z\d_@$!%*#?&]{8,30}$/;

    if (!regName.test(name)) {
        seterror("pass", "*Minimum eight characters, at least letter, one number and one special character");
        click = false;
    } else {
        clearErrors("pass");
        click = true;
    }
}

function confirmPasswordCheck() {
    var element_id_1 = arguments[0];
    var element_id_2 = arguments[1];
    var name1 = document.getElementById(element_id_1).value;
    var name2 = document.getElementById(element_id_2).value;
    if (name1 != name2) {
        seterror("cpass", "*passwod didn't match");
        click = false;
    } else {
        clearErrors("cpass");
        click = true;
    }
}
//pet name check
function nameCheck() {
    var element_id = arguments[0];
    var name1 = document.getElementById(element_id).value;
    var regName = /^[A-Za-z]+$/;

    if (!regName.test(name1)) {
        seterror("name", "*only alphabates");
        click = false;
    } else {
        clearErrors("name");
        click = true;
    }
}

function breedCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /\w+/;

    if (!regName.test(name)) {
        seterror("breed", "*only alphabates");
        click = false;
    } else {
        clearErrors("name");
        click = true;
    }
}

function colorCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /\w+/;

    if (!regName.test(name)) {
        seterror("color", "*only alphabates");
        click = false;
    } else {
        clearErrors("color");
        click = true;
    }
}

function ageCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /^[0-2][0-7]$/;
    if (!regName.test(name)) {
        seterror("age", "*age between 00-17");
        click = false;
    } else {
        clearErrors("age");
        click = true;
    }
}

function addressCheck() {
    var element_id = arguments[0];
    var name = document.getElementById(element_id).value;
    var regName = /^[0-9a-zA-Z\s,]+$/;

    if (!regName.test(name)) {
        seterror("address", "*only use alphabates numbers commas( , ) and period( . )");
        click = false;
    } else {
        clearErrors("address");
        click = true;
    }
}

function allTrueCheck() {
    if (click == true) {
        return true;
    } else {
        return false;
    }
}