const nameElement = document.getElementById("typing-name");

const fullName = "Rafael Lemos";

let index = 0;

function typeName() {
    if (index < fullName.length) {
        nameElement.innerHTML =
            fullName.substring(0, index + 1) +
            '<span class="cursor">|</span>';

        index++;

        setTimeout(typeName, 120);
    } else {
        nameElement.innerHTML =
            fullName +
            '<span class="cursor">|</span>';
    }
}

typeName();