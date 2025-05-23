# Random Password Generator

A simple and stylish web app that generates strong, random passwords with a single click.

# Features

* Generates 12-character passwords by default
* Ensures at least one uppercase letter, one lowercase letter, one number, and one symbol
* Easy-to-use interface with a clean, modern design
* Responsive layout that works well on desktop and mobile


# How it works

* The app combines uppercase letters, lowercase letters, numbers, and symbols
* It guarantees each password contains at least one character from each category
* The rest of the characters are randomly picked from the full combined set


# Technologies

* **HTML5** — markup for layout and structure
* **CSS3** — styling and responsive design
* **JavaScript** — password generation logic and interactivity


## Usage

1. Open `index.html` in a web browser
2. Click the **Generate Password** button
3. The generated password appears in the input box

---

## Code snippets

### JavaScript Password Generator Logic

```js
const length = 12;

const upperCase = "AQWERTYUIOPSDFGHJKLZXCVBNM";
const lowerCase = "qwertyuiopasdfghjklzxcvbnm";
const number = "1234567890";
const symbols = "!@#$%^&*()[]{}|/?.><=+-_";

const allChars = upperCase + lowerCase + number + symbols;

function createPassword() {
    let password = "";
    password += upperCase[Math.floor(Math.random() * upperCase.length)];
    password += lowerCase[Math.floor(Math.random() * lowerCase.length)];
    password += number[Math.floor(Math.random() * number.length)];
    password += symbols[Math.floor(Math.random() * symbols.length)];

    while (password.length < length) {
        password += allChars[Math.floor(Math.random() * allChars.length)];
    }

    document.getElementById("password").value = password;
}
```

---

## How to run

* Download or clone this repo
* Open `index.html` in your favorite browser
* Click the **Generate Password** button and enjoy!

---

## Possible improvements

* Add a copy-to-clipboard button
* Let users customize password length and character sets
* Add password strength meter
* Save generated passwords locally

