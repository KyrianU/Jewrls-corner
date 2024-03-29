


var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#100',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }

    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545',
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');
