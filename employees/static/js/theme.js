const body = document.body;
const btn = document.getElementById("theme-toggle");

function updateTheme(theme) {

    if (theme === "dark") {

        body.classList.add("dark");

        btn.innerHTML = '<i class="bi bi-sun-fill"></i>';

    } else {

        body.classList.remove("dark");

        btn.innerHTML = '<i class="bi bi-moon-stars-fill"></i>';

    }

}

const savedTheme = localStorage.getItem("theme") || "light";

updateTheme(savedTheme);

btn.addEventListener("click", () => {

    const newTheme = body.classList.contains("dark")
        ? "light"
        : "dark";

    localStorage.setItem("theme", newTheme);

    updateTheme(newTheme);

});