//// Hide credential fields along with checkbox value

// Get the checkbox and the username/password fields
let manualCredentialsCheckbox = document.getElementById("manual-credentials");
let usernameField = document.getElementById("username");
let passwordField = document.getElementById("password");
let usernameLabel = document.querySelector("label[for='username']");
let passwordLabel = document.querySelector("label[for='password']");

// Listen for changes to the checkbox
manualCredentialsCheckbox.addEventListener("change", function() {
    if (!manualCredentialsCheckbox.checked) { // If the checkbox is not checked
        usernameField.style.display = "block";
        passwordField.style.display = "block";
        usernameLabel.style.display = "block";
        passwordLabel.style.display = "block";
    } else { // Otherwise, hide the username/password fields
        usernameField.style.display = "none";
        passwordField.style.display = "none";
        usernameLabel.style.display = "none";
        passwordLabel.style.display = "none";
    }
});



//// Create input fields to match the user's input
let fieldsNumberInput = document.getElementById("fields-number");
let fieldsContainer = document.getElementById("fields-container");

fieldsNumberInput.addEventListener("change", function() {
    // Get the number of fields the user wants
    let numberOfFields = fieldsNumberInput.value;

    // Clear the fields container
    fieldsContainer.innerHTML = "";

    // Create the new fields
    for (let i = 0; i < numberOfFields; i++) {
        // Create the key input
        let keyInput = document.createElement("input");
        keyInput.type = "text";
        keyInput.placeholder = "Key";

        // Create the value input
        let valueInput = document.createElement("input");
        valueInput.type = "text";
        valueInput.placeholder = "Value";

        // Create a container for the key/value inputs
        let fieldContainer = document.createElement("div");
        fieldContainer.appendChild(keyInput);
        fieldContainer.appendChild(valueInput);

        // Add the container to the fields container
        fieldsContainer.appendChild(fieldContainer);
    }
});

let tabLinks = document.querySelectorAll(".tab-link");
let tabs = document.querySelectorAll(".tab");

tabLinks.forEach(function(tabLink) {
    tabLink.addEventListener("click", function(event) {
        event.preventDefault();
        let tabId = this.id.replace("-link", "");
        tabs.forEach(function(tab) {
            if (tab.id === tabId) {
                tab.style.display = "block";
            } else {
                tab.style.display = "none";
            }
        });
    });
});

