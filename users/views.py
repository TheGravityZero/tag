import json
import uuid
from datetime import datetime, timedelta

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from yookassa import Configuration, Receipt, Payment

from index.models import Location, Images, Video, Promo
from users.models import TypeActivity, Wishlist, CustomUser


Configuration.configure('258399', 'live_SVv1Z-8_GD3BLoX7i3BSfxr9_CgYlMB4rzEN6YNxNBk')

class LKView(ListView):
    model = TypeActivity
    template_name = 'lk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wishlist'] = Wishlist.objects.filter(user=self.request.user)
        context['img'] = Images.objects.all()
        context['video'] = Video.objects.all()
        context['date'] = timezone.now()
        return context

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=request.user.pk)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.city = request.POST.get('city')
        if request.POST.get('social') == 'Telegram':
            user.telegram = request.POST.get('username')
            user.insta = None
        else:
            user.telegram = None
            user.insta = request.POST.get('username')
        user.save()
        return redirect('/accounts')

def add_wishlist(request):
    location = Location.objects.get(pk=request.GET['location'])
    Wishlist.objects.create(location=location, user=request.user)
    return JsonResponse({'result':'success'})

def change_city(request):
    city = request.GET.get('city')
    user = CustomUser.objects.get(pk=request.user.pk)
    user.city = city
    user.save()
    return JsonResponse({'result':'success'})

def delete_wishlist(request):
    location = Location.objects.get(pk=request.GET['location'])
    Wishlist.objects.get(location=location, user=CustomUser.objects.get(pk=request.user.pk)).delete()
    return JsonResponse({'result':'success'})

def logout_view(request):
    logout(request)
    return redirect('index')

def pay_mounth(request):
    if request.GET.get('promo'):
        try:
            promo = Promo.objects.filter(title=request.GET.get('promo'))[0].percent
        except:
            promo = 0
        payment = Payment.create(
            {"amount": {"value": 499 - 499 / 100 * float(promo), "currency": "RUB"},
             "payment_method_data": {"type": "bank_card"},
             "confirmation": {"type": "redirect", "return_url": "https://tag-location.ru"},
             "capture": True,
             "save_payment_method": False,
             "description": f'Оплата подписки на год {request.user.username}',
             "metadata": {
                 'orderNumber': str(uuid.uuid4())
             },
             "receipt": {
                 "customer": {
                     "full_name": "Ivanov Ivan Ivanovich",
                     "email": "email@email.ru",
                     "phone": "79211234567",
                     "inn": "6321341814"
                 },
                 "items": [
                     {
                         "description": f"Подписка для пользователя {request.user.username}",
                         "quantity": "1.00",
                         "amount": {
                             "value": 499 - 499 / 100 * float(promo),
                             "currency": "RUB"
                         },
                         "vat_code": "2",
                         "payment_mode": "full_payment",
                         "payment_subject": "commodity",
                         "country_of_origin_code": "CN",
                         "product_code": "44 4D 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                         "customs_declaration_number": "10714040/140917/0090376",
                         "excise": "20.00",
                         "supplier": {
                             "name": "string",
                             "phone": "string",
                             "inn": "string"
                         }
                     },
                 ]
             }
             }, str(uuid.uuid4()))
    else:
        payment = Payment.create(
            {"amount": {"value": 499, "currency": "RUB"},
             "payment_method_data": {"type": "bank_card"},
             "confirmation": {"type": "redirect", "return_url": "https://tag-location.ru"},
             "capture": True,
             "save_payment_method": False,
             "description": f'Оплата подписки на год {request.user.username}',
             "metadata": {
                 'orderNumber': str(uuid.uuid4())
             },
             "receipt": {
                 "customer": {
                     "full_name": "Ivanov Ivan Ivanovich",
                     "email": "email@email.ru",
                     "phone": "79211234567",
                     "inn": "6321341814"
                 },
                 "items": [
                     {
                         "description": f"Подписка для пользователя {request.user.username}",
                         "quantity": "1.00",
                         "amount": {
                             "value": 499,
                             "currency": "RUB"
                         },
                         "vat_code": "2",
                         "payment_mode": "full_payment",
                         "payment_subject": "commodity",
                         "country_of_origin_code": "CN",
                         "product_code": "44 4D 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                         "customs_declaration_number": "10714040/140917/0090376",
                         "excise": "20.00",
                         "supplier": {
                             "name": "string",
                             "phone": "string",
                             "inn": "string"
                         }
                     },
                 ]
             }
             }, str(uuid.uuid4()))

    user = CustomUser.objects.get(pk=request.user.pk)
    user.rebill_id = payment.id
    user.save()

    return redirect(payment.confirmation.confirmation_url)

def pay_year(request):
    if request.GET.get('promo'):
        try:
            promo = Promo.objects.filter(title=request.GET.get('promo'))[0].percent
        except:
            promo = 0
        payment = Payment.create(
            {"amount": {"value": 999 - 999 / 100 * float(promo), "currency": "RUB"},
             "payment_method_data": {"type": "bank_card"},
             "confirmation": {"type": "redirect", "return_url": "https://tag-location.ru"},
             "capture": True,
             "save_payment_method": False,
             "description": f'Оплата подписки на год {request.user.username}',
             "metadata": {
                 'orderNumber': str(uuid.uuid4())
             },
             "receipt": {
                 "customer": {
                     "full_name": "Ivanov Ivan Ivanovich",
                     "email": "email@email.ru",
                     "phone": "79211234567",
                     "inn": "6321341814"
                 },
                 "items": [
                     {
                         "description": f"Подписка для пользователя {request.user.username}",
                         "quantity": "1.00",
                         "amount": {
                             "value": 999 - 999 / 100 * float(promo),
                             "currency": "RUB"
                         },
                         "vat_code": "2",
                         "payment_mode": "full_payment",
                         "payment_subject": "commodity",
                         "country_of_origin_code": "CN",
                         "product_code": "44 4D 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                         "customs_declaration_number": "10714040/140917/0090376",
                         "excise": "20.00",
                         "supplier": {
                             "name": "string",
                             "phone": "string",
                             "inn": "string"
                         }
                     },
                 ]
             }
             }, str(uuid.uuid4()))
    else:
        payment = Payment.create(
            {"amount": {"value": 999, "currency": "RUB"},
             "payment_method_data": {"type": "bank_card"},
             "confirmation": {"type": "redirect", "return_url": "https://tag-location.ru"},
             "capture": True,
             "save_payment_method": False,
             "description": f'Оплата подписки на год {request.user.username}',
             "metadata": {
                 'orderNumber': str(uuid.uuid4())
             },
             "receipt": {
                 "customer": {
                     "full_name": "Ivanov Ivan Ivanovich",
                     "email": "email@email.ru",
                     "phone": "79211234567",
                     "inn": "6321341814"
                 },
                 "items": [
                     {
                         "description": f"Подписка для пользователя {request.user.username}",
                         "quantity": "1.00",
                         "amount": {
                             "value": 999,
                             "currency": "RUB"
                         },
                         "vat_code": "2",
                         "payment_mode": "full_payment",
                         "payment_subject": "commodity",
                         "country_of_origin_code": "CN",
                         "product_code": "44 4D 01 00 21 FA 41 00 23 05 41 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 12 00 AB 00",
                         "customs_declaration_number": "10714040/140917/0090376",
                         "excise": "20.00",
                         "supplier": {
                             "name": "string",
                             "phone": "string",
                             "inn": "string"
                         }
                     },
                 ]
             }
             }, str(uuid.uuid4()))

    user = CustomUser.objects.get(pk=request.user.pk)
    user.rebill_id = payment.id
    user.save()

    return redirect(payment.confirmation.confirmation_url)

def pay_one(request):
    payment = Payment.create(
        {"amount": {"value": 149, "currency": "RUB"},
         "payment_method_data": {"type": "bank_card"},
         "confirmation": {"type": "redirect", "return_url": "https://tag-location.ru"},
         "capture": True,
         "save_payment_method": True,
         "description": f'Оплата разовой подписки {request.user.username}'
         }, str(uuid.uuid4()))

    user = CustomUser.objects.get(pk=request.user.pk)
    user.rebill_id = payment.id
    user.save()

    return redirect(payment.confirmation.confirmation_url)
@csrf_exempt
def pay_webhook_handler(request):
    event_json = json.loads(request.body)
    if event_json['object']['status'] == 'succeeded':
        user = CustomUser.objects.get(rebill_id=event_json['object']['id'])
        if event_json['object']['amount']['value'] == "499.00":
            user.status = 'mounth'
            user.created_pay = None
            user.created_pay = timezone.now() + timedelta(days=30)
        elif event_json['object']['amount']['value'] == "149.00":
            user.attempts += 1
        else:
            user.status = 'year'
            user.created_pay = None
            user.created_pay = timezone.now() + timedelta(days=90)
        user.extension = True
        user.save()
    return HttpResponse('ok')


def pay_stop(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    user.extension = False
    user.save()
    return redirect('lk')

def user_login(request):
    username = request.GET.get('login-username')
    password = request.GET.get('login-password')
    print(username, password)
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})