/* jshint esversion: 8, jquery: true */
// code copied from the bulma documentation
$(document).ready(function () {
    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });
    // get current year for Copyright info
    let getYear = new Date().getFullYear();
    let yearID = document.getElementById("year");
    if (getYear == 2022) {
        yearID.innerHTML = `\u00A0${getYear}\u00A0`;
    } else {
        yearID.innerHTML = `\u00A0 2022 - ${getYear}\u00A0`;
    }
});

// code copied from the bulma documentation
document.addEventListener("DOMContentLoaded", () => {
    (document.querySelectorAll(".notification .delete") || []).forEach(($delete) => {
        const $notification = $delete.parentNode;

        $delete.addEventListener("click", () => {
            $notification.parentNode.removeChild($notification);
        });
    });
});
