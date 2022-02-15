let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
// let appearance = {
//     theme: "night",
//     variables: {
//         fontFamily: "Sohne, system-ui, sans-serif",
//         fontWeightNormal: "500",
//         borderRadius: "8px",
//         colorPrimary: "#EFC078",
//         colorText: "white",
//         colorTextSecondary: "white",
//         colorTextPlaceholder: "#727F96",
//         colorIconTab: "white",
//         colorLogo: "dark",
//     },
//     rules: {
//         ".Input, .Block": {
//             backgroundColor: "#0A2540",
//             border: "1.5px solid var(--colorPrimary)",
//         },
//     },
// };

// Set up Stripe.js and Elements to use in checkout form
let elements = stripe.elements();

let card = elements.create("card", {
    iconstyle: "solid",
    style: {
        base: {
            iconColor: "#c4f0ff",
            color: "#fff",
            fontWeight: 500,
            fontFamily: "Roboto, Open Sans, Segoe UI, sans-serif",
            fontSize: "16px",
            fontSmoothing: "antialiased",

            ":-webkit-autofill": {
                color: "#fce883",
            },
            "::placeholder": {
                color: "#87BBFD",
            },
        },
        invalid: {
            iconColor: "#FFC7EE",
            color: "#FFC7EE",
        },
    },
});
card.mount("#card-element");

card.on("change", function (event) {
    var displayError = document.getElementById("card-errors");
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = "";
    }
});

let form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    card.update({ disabled: true });
    $("#submit-button").attr("disabled", true);

    let saveInfo = Boolean($("#id-save-info").attr("checked"));
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        csrfmiddlewaretoken: csrfToken,
        client_secret: clientSecret,
        save_info: saveInfo,
    };
    let url = "/checkout/cache_checkout_data/";

    $.post(url, postData)
        .done(function () {
            stripe
                .confirmCardPayment(clientSecret, {
                    payment_method: {
                        type: "card",
                        card: card,
                        billing_details: {
                            name: $.trim(form.full_name.value),
                            email: $.trim(form.email.value),
                            address: {
                                line1: $.trim(form.street_address1.value),
                                line2: $.trim(form.street_address2.value),
                                city: $.trim(form.city.value),
                                state: $.trim(form.state.value),
                                country: $.trim(form.country.value),
                            },
                        },
                    },
                })
                .then(function (result) {
                    if (result.error) {
                        let errorDiv = document.getElementById("card-errors");
                        let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
                        $(errorDiv).html(html);

                        card.update({ disabled: false });
                        $("#submit-button").attr("disabled", false);
                    } else {
                        if (result.paymentIntent.status === "succeeded") {
                            form.submit();
                        }
                    }
                });
        })
        .fail(function () {
            // just reload the page, the error will be in django messages
            location.reload();
        });
});
