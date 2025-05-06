//////////////////////  Start Calculate  /////////////////////
document.addEventListener("DOMContentLoaded", function () {
document.querySelectorAll(".popup_content").forEach(popup_content => {
const basePrice = parseFloat(popup_content.getAttribute("data-base-price")) || 0;
const totalPriceElement = popup_content.querySelector("#total-price");
let selectedSizePrice = 0;

popup_content.querySelectorAll(".extra-checkbox").forEach(checkbox => {
checkbox.addEventListener("change", function () {
    updateTotalPrice();
});
});

popup_content.querySelectorAll(".size-options button").forEach(button => {
button.addEventListener("click", function () {
    popup_content.querySelectorAll(".size-options button").forEach(btn => btn.classList.remove("selected"));
    this.classList.add("selected");

    selectedSizePrice = parseFloat(this.getAttribute("data-price")) || 0;

    updateTotalPrice();
});
});

function updateTotalPrice() {
let extrasPrice = 0;
popup_content.querySelectorAll(".extra-checkbox:checked").forEach(checkbox => {
    extrasPrice += parseFloat(checkbox.getAttribute("data-price")) || 0;
});

const total = basePrice + selectedSizePrice + extrasPrice;
totalPriceElement.textContent = total.toFixed(2);
}

updateTotalPrice(); // حساب مبدأي
});
});
//////////////////////  End Calculate  /////////////////////