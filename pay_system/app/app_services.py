from .models import Item
import config as c
import stripe
from django.http import JsonResponse
from django.views import View


# class Pay:
#
#     @staticmethod
#     def check_item(item_id: str) -> dict:
#         id = int(item_id)
#         return Item.objects.filter(id=id).first()



