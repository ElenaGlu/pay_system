import stripe
from django.http import JsonResponse

from django.views import View
from django.views.generic import TemplateView
import config as c
from app.models import Item

stripe.api_key = c.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "item_id": item.id
            },
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemLandingPageView(TemplateView):
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name="Test")
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "item": item,
            "STRIPE_PUBLIC_KEY": c.STRIPE_PUBLIC_KEY
        })
        return context
