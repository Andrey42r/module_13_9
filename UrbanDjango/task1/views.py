from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Create your views here.

def menu_page(request):
    return render(request, 'third_task/menu.html')


def main_page(request):
    return render(request, 'third_task/main_page.html')


def go_reg(request):
    return render(request, 'fifth_task/registration_page.html')


def bin_page(request):
    cont = 'Извините, ваша корзина пуста'
    context = {
        'cont': cont,
    }
    return render(request, 'fifth_task/bin_page.html', context)


def page_2(request):
    title = 'Новые автомобили'
    list_car = ['Автомобили российских марок', 'Автомобили зарубежных марок', 'Автомобили ручной сборки']
    context = {
        'title': title,
        'list_car': list_car,
    }
    return render(request, 'third_task/additional_page_1.html', context)


def page_3(request):
    title = 'Подержанные автомобили'
    list_car2 = ['Автомобили от собственников', 'Автомобили под заказ', 'Автомобили из автосалонов']
    context = {
        'title': title,
        'list_car2': list_car2,
    }
    return render(request, 'third_task/additional_page_2.html', context)


def button(request):
    return render(request, 'third_task/main_page.html')


def games(request):
    Games = Game.objects.all()
    result = f'{Game.title}|{Game.description}. Стоимость: {Game.cost}'
    context = {
        'result': result,
        'Games': Games,
    }
    return render(request, 'fifth_task/games.html', context)


def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        users = Buyer.objects.all()
        info = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in users and password == repeat_password and age >= '18':
                users.append(username)
                print(f'Updated names: {users}')
                return HttpResponse(f'Приветствуем, {username}!')

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

            elif age < '18':
                info['error'] = 'Вы должны быть старше 18'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

            elif username in users:
                info['error'] = 'Пользователь уже существует'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

    else:
        form = UserRegister()
        info = {'form': form}
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_html(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        users = Buyer.objects.all()
        info = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in users and password == repeat_password and age >= '18':
                users.append(username)
                print(f'Updated names: {users}')
                return HttpResponse(f'Приветствуем, {username}!')

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

            elif age < '18':
                info['error'] = 'Вы должны быть старше 18'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

            elif username in users:
                info['error'] = 'Пользователь уже существует'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

    else:
        form = UserRegister()
        info = {'form': form}
    return render(request, 'fifth_task/registration_page.html', context=info)