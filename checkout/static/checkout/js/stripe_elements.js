const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
const clientSecret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripePublicKey);

const options = {
    clientSecret: clientSecret,
    // Fully customizable with appearance API.
    appearance: {
        theme: "night",
        variables: {
            fontFamily: "Sohne, system-ui, sans-serif",
            fontWeightNormal: "500",
            borderRadius: "8px",
            colorBackground: "#0A2540",
            colorPrimary: "#EFC078",
            colorPrimaryText: "#1A1B25",
            colorText: "black",
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

// Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in step 2
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElement = elements.create("payment");
paymentElement.mount("#payment-element");

const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    // disable card element and submit button to prevent multiple submissions
    paymentElement.update({ disabled: true });
    $("#submit-button").attr("disabled", true);

    const { error } = await stripe.confirmPayment({
        //`Elements` instance that was used to create the Payment Element
        elements,
        confirmParams: {
            return_url: "https://www.google.com",
        },
    });

    if (error) {
        // This point will only be reached if there is an immediate error when
        // confirming the payment. Show error to your customer (for example, payment
        // details incomplete)
        const messageContainer = document.querySelector("#error-message");
        messageContainer.textContent = error.message;
        paymentElement.update({ disabled: false });
        $("#submit-button").attr("disabled", false);
    } else {
        // Your customer will be redirected to your `return_url`. For some payment
        // methods like iDEAL, your customer will be redirected to an intermediate
        // site first to authorize the payment, then redirected to the `return_url`.
        // submit form
        if (result.paymentIntent.status === "succeeded") {
            form.submit();
        }
    }

    // the view updates the paymentIntent
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
                                state: $.trim(form.county.value),
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
                            state: $.trim(form.county.value),
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
                        paymentElement.update({ disabled: false });
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
});
