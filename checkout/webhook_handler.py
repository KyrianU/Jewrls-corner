from django.http import HttpResponse


class StripeWH_Handler:
    """Handles stripes webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, request):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
 
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent_payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )