const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
const clientSecret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const options = {
    clientSecret: clientSecret,
    appearance: {
        theme: "night",
        variables: {
            fontFamily: "Sohne, system-ui, sans-serif",
            fontWeightNormal: "500",
            borderRadius: "8px",
            colorBackground: "#0A2540",
            colorPrimary: "#EFC078",
            colorPrimaryText: "#1A1B25",
            colorText: "white",
            colorTextSecondary: "white",
            colorTextPlaceholder: "#727F96",
            colorIconTab: "white",
            colorLogo: "dark",
        },
        rules: {
            ".Input, .Block": {
                backgroundColor: "transparent",
                border: "1.5px solid var(--colorPrimary)",
            },
        },
    },
};
const elements = stripe.elements(options);

const paymentElement = elements.create("payment");
/* mount the card element */
paymentElement.mount("#payment-element");

const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const { error } = await stripe.confirmPayment({
        //`Elements` instance that was used to create the Payment Element
        elements,
        confirmParams: {
            return_url: "",
        },
    });

    if (error) {
        // This point will only be reached if there is an immediate error when
        // confirming the payment. Show error to your customer (for example, payment
        // details incomplete)
        const messageContainer = document.querySelector("#error-message");
        messageContainer.textContent = error.message;
    } else {
        // Your customer will be redirected to your `return_url`. For some payment
        // methods like iDEAL, your customer will be redirected to an intermediate
        // site first to authorize the payment, then redirected to the `return_url`.
    }
});

const appendedClientSecret = new URLSearchParams(window.location.search).get(
    "payment_intent_client_secret"
);

// Retrieve the PaymentIntent
stripe.retrievePaymentIntent(appendedClientSecret).then(({ paymentIntent }) => {
    const message = document.querySelector("#message");

    // Inspect the PaymentIntent `status` to indicate the status of the payment
    // to your customer.
    //
    // Some payment methods will [immediately succeed or fail][0] upon
    // confirmation, while others will first enter a `processing` state.
    //
    // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
    switch (paymentIntent.status) {
        case "succeeded":
            message.innerText = "Success! Payment received.";
            break;

        case "processing":
            message.innerText = "Payment processing. We'll update you when payment is received.";
            break;

        case "requires_payment_method":
            message.innerText = "Payment failed. Please try another payment method.";
            // Redirect your user back to your payment page to attempt collecting
            // payment again
            break;

        default:
            message.innerText = "Something went wrong.";
            break;
    }
});

// the view updates the paymentIntent
/*
$.post(url, postData)
    .done(function () {
        stripe
            // call confirmCardPayment method from Stripe
            .confirmCardPayment(clientSecret, {
                payment_method: {
                    paymentElement: paymentElement,
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
                shipping: {
                    name: $.trim(form.full_name.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        post_code: $.trim(form.postcode.value),
                        state: $.trim(form.state.value),
                        country: $.trim(form.country.value),
                    },
                },
            })
            .then(function (result) {
                if (result.error) {
                    var errorDiv = document.getElementById("card-errors");
                    var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                    $(errorDiv).html(html);
                    $("#payment-form").fadeToggle(100);
                    $("#loading-overlay").fadeToggle(100);
                    // re-enable card element + button to allow fixes
                    card.update({ disabled: false });
                    $("#submit-button").attr("disabled", false);
                } else {
                    // submit form
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
*/
