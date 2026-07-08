// ================================
// Theme Toggle
// ================================

const themeBtn = document.getElementById("theme-btn");

// Load saved theme
if (localStorage.getItem("theme") === "dark") {

    document.body.classList.add("dark");
    themeBtn.textContent = "☀️";

} else {

    themeBtn.textContent = "🌙";

}

// Toggle theme
themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {

        themeBtn.textContent = "☀️";
        localStorage.setItem("theme", "dark");

    } else {

        themeBtn.textContent = "🌙";
        localStorage.setItem("theme", "light");

    }

});


// ================================
// Button Animation
// ================================

const form = document.querySelector("form");

const submitBtn = document.querySelector("button[type='submit']");

form.addEventListener("submit", () => {

    submitBtn.innerHTML = "⏳ Analyzing...";

    submitBtn.disabled = true;

});
const textarea = document.getElementById("review");
const counter = document.getElementById("charCount");

if(textarea){

    counter.textContent = textarea.value.length;

    textarea.addEventListener("input", ()=>{

        counter.textContent = textarea.value.length;

    });

}