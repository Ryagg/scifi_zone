const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
const clientSecret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripePublicKey);

const options = {
    clientSecret: "{{CLIENT_SECRET}}",
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

// Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in step 2
const elements = stripe.elements(clientSecret, appearance);

// Create and mount the Payment Element
const paymentElement = elements.create("payment");
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
