import stripe

from config.settings import API_KEY_STRIPE
from payment.models import Payment


def get_pay(amount_payment, user):
    stripe.api_key = API_KEY_STRIPE
    pay = stripe.PaymentIntent.create(
        amount=amount_payment,
        currency="usd",
        automatic_payment_methods={"enabled": True}
    )

    payment = Payment.objects.create(
        user=user,
        amount_payment=amount_payment,
        stripe_id=pay.id
    )

    return payment
