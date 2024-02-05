import math
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView, ListView, DetailView
from yookassa import Payment

from index.models import Question, People, Location, Images, Video, Hashtag
from tag import settings
from users.forms import RegistrationForm, LoginForm
from users.models import CustomUser, Wishlist


class IndexView(ListView):
    template_name = 'index.html'
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people'] = People.objects.all()
        context['registration_form'] = RegistrationForm(prefix='registration')
        context['login_form'] = LoginForm(prefix='login')
        return context

    def post(self, request, *args, **kwargs):
        registration_form = RegistrationForm(request.POST, prefix='registration')

        if request.POST.get('login-username'):
            username = request.POST.get('login-username')
            password = request.POST.get('login-password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('lk')
            else:
                messages.error(request, 'Invalid login credentials. Please try again.')
        elif request.POST.get('name'):
            email = EmailMessage(
                'Форма "Найдем локацию на любой вкус"',
                f'Имя: {request.POST.get("name")}\nНомер телефон: {request.POST.get("phone")}\nГород: {request.POST.get("city")}\nОписание: {request.POST.get("desc")}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )

            # Отправляем email
            email.send(fail_silently=False)
            return redirect('/')

        else:
            uploaded_file = request.FILES['fileInput']

            email = EmailMessage(
                'Форма "Заявка на добавление фото"',
                f'Имя: {request.POST.get("first_name")}\nФамилия: {request.POST.get("last_name")}\nАдрес: {request.POST.get("address")}\nОписание: {request.POST.get("description")}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)

            # Отправляем email
            email.send(fail_silently=False)
            return redirect('/')


class LK(TemplateView):
    template_name = 'lk.html'


class Locate(ListView):
    model = Location
    template_name = 'location.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Пользователь не авторизован, перенаправляем на страницу с ошибкой
            return redirect('error')  # Здесь 'error' - это имя URL для страницы с ошибкой

        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.request.user.status != 'free':
            return ['location.html']
        else:
            return ['location_free.html']

    def get_queryset(self):
        if self.request.user.status == 'free':
            hashtags = Hashtag.objects.filter(title=self.request.user.save_hashtag)
            location_query = Location.objects.filter(city=self.request.user.city, hashtag__in=hashtags) if len(hashtags) > 0 else Location.objects.filter(city=self.request.user.city)
        else:
            location_query = Location.objects.filter(city=self.request.user.city)

        if self.request.user.save_hashtag == 'None' and self.request.user.status == 'free':
            return location_query.order_by('id')[:9]
        else:
            return location_query.order_by('id')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(pk=self.request.user.pk)
        try:
            if user.created_pay < timezone.now():
                user.status = 'free'
                user.created_pay = datetime.now()
                user.save()
        except:
            pass

        context['wishlist_location_pks'] = []

        for i in Wishlist.objects.filter(user=self.request.user):
            context['wishlist_location_pks'].append(i.location.pk)

        context['img'] = Images.objects.all()
        context['video'] = Video.objects.all()
        context['hashtag'] = Hashtag.objects.all()
        loc_filter = Location.objects.filter(city=self.request.user.city)
        if self.request.user.status == 'free':
            hashtags = Hashtag.objects.filter(title=self.request.user.save_hashtag)
            loc_filter = loc_filter.filter(hashtag__in=hashtags) if len(hashtags) > 0 else loc_filter

        context['loc_count'] = math.ceil(len(loc_filter) / 9)

        return context

class LocationDetailView(DetailView):
    model = Location
    template_name = 'location-item.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Пользователь не авторизован, перенаправляем на страницу с ошибкой
            return redirect('error')  # Здесь 'error' - это имя URL для страницы с ошибкой

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['img'] = Images.objects.all()
        context['video'] = Video.objects.all()
        context['locations'] = Location.objects.filter(city=self.request.user.city).exclude(pk=self.object.pk)
        context['wishlist'] = [item.location.pk for item in Wishlist.objects.filter(user=CustomUser.objects.get(pk=self.request.user.pk))]
        if self.request.user.status == 'free':
            if self.request.user.attempts > 0:
                user = CustomUser.objects.get(pk=self.request.user.pk)
                user.attempts -= 1
                user.save()
                context['address'] = True
            else:
                context['address'] = False
        return context

class LocationFree(TemplateView):
    template_name = 'location_free.html'

class LocationItem(TemplateView):
    template_name = 'location_item.html'

def filter_location(request):
    get = request.GET.getlist('hashtag[]')
    city = request.GET.getlist('city')
    page = request.GET.getlist('page', None)
    if request.user.status == 'free':
        user = CustomUser.objects.get(pk=request.user.pk)
        try:
            user.save_hashtag = get[0]
            user.save()
        except:
            pass

    if len(get) < 1:
        location = Location.objects.filter(city=city[0]).order_by('id')
        if request.user.status == 'free' and request.user.save_hashtag != 'None':
            location = location.filter(hashtag__title__contains=request.user.save_hashtag)
    else:
        hashtags = Hashtag.objects.filter(title__in=get)
        location = Location.objects.filter(hashtag__in=hashtags, city=city[0]).distinct().order_by('id')

    if page:
        paginator = Paginator(location, 9)
        page = paginator.get_page(int(page[0]))
        location_ids = list(page.object_list.values_list('pk', flat=True))
    else:
        page = location
        location_ids = list(location.values_list('pk', flat=True))


    template = loader.get_template('location_filter.html')
    context = {}
    context['request'] = request
    context['hashtags'] = page
    context['img'] = Images.objects.all()
    context['video'] = Video.objects.all()
    context['wishlist'] = [item.location.pk for item in Wishlist.objects.filter(user=CustomUser.objects.get(pk=request.user.pk))]
    html = template.render(context)

    data = {'html': html, 'pk':location_ids, 'coordinates' : [(i.latitude, i.longitude, i.pk) for i in location], 'count':math.ceil(len(location)/9), 'len_max':len(location)}
    return JsonResponse(data)

def save_filter_location(request):
    get = request.GET.getlist('hashtag[]')
    user = CustomUser.objects.get(pk=request.user.pk)
    if len(user.save_hashtag) < 2:
        user.save_hashtag = get[0]
        user.save()

    city = request.GET.getlist('city')


    if len(get) < 1:
        location = Location.objects.filter(city=city[0])
        locations_pk = Location.objects.filter(city=city[0]).distinct().values_list('pk', flat=True)
    else:
        hashtags = Hashtag.objects.filter(title__in=get)
        location = Location.objects.filter(hashtag__in=hashtags, city=city[0]).distinct()
        locations_pk = Location.objects.filter(hashtag__in=hashtags, city=city[0]).distinct().values_list('pk',
                                                                                                          flat=True)

    location_ids = list(locations_pk)

    template = loader.get_template('location_filter.html')
    context = {}
    context['hashtags'] = location
    context['img'] = Images.objects.all()
    context['video'] = Video.objects.all()
    html = template.render(context)

    data = {'html': html, 'pk': location_ids}
    return JsonResponse(data)

def voronka(request):
    tag = request.GET.getlist('data[tag]')
    city = request.GET.getlist('data[city]')
    rayon = request.GET.getlist('data[rayon]')
    resolution = request.GET.getlist('data[resolution]')
    email = request.GET.getlist('data[email]')

    random_password = get_random_string(length=12)
    hashed_password = make_password(random_password)
    try:
        CustomUser.objects.create(username=''.join(email),
                                  email=''.join(email),
                                  city=''.join(city),
                                  password=hashed_password,
                                  save_hashtag='None')

        text = f"""Тэги: {''.join(tag)}
        Город: {''.join(city)}
        Районы: {''.join(rayon)}
        Разрешение: {''.join(resolution)}
        Почта: {''.join(email)}"""
        send_mail('Обратная связь', text, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        send_mail('Данные авторизации', f"Email: {''.join(email)}\nПароль: {random_password}", settings.EMAIL_HOST_USER,
                  [''.join(email)])
    except:
        user = CustomUser.objects.filter(username=''.join(email))[0]
        text = f"""Тэги: {''.join(tag)}
        Город: {''.join(city)}
        Районы: {''.join(rayon)}
        Разрешение: {''.join(resolution)}
        Почта: {''.join(email)}"""
        send_mail('Обратная связь', text, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        send_mail('Данные авторизации', f"Email: {''.join(email)}\nПароль: {user.password}", settings.EMAIL_HOST_USER,
                  [''.join(email)])


    return JsonResponse({'result':'success'})


def error_view(request):
    return render(request, 'error.html')