from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from .forms import UserCreationFormCustom


def welcome(request):
    # проверка аутентификации пользователя
    if request.user.is_authenticated:
        # Возвращается страница если вошли
        return render(request, "core/welcome.html")
    # если  не вошли в систему, перенаправляет на вход в систему
    return redirect('/login')


def login(request):
    # Создаем пустую форму аутентификации
    form = AuthenticationForm()
    if request.method == "POST":
        # Добавляем полученные данные в форму
        form = AuthenticationForm(data=request.POST)
        # Если форма действительна
        if form.is_valid():
            # Восстановление подтвержденных учетных данных
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Мы проверяем учетные данные пользователя
            user = authenticate(username=username, password=password)

            # Если пользователь с таким именем и паролем существует
            if user is not None:
                # Мы входим в систему вручную
                do_login(request, user)
                # И мы перенаправляем вас на домашнюю страницу
                return redirect('/')

    # Если мы дойдем до конца, то получим форму
    return render(request, "authentication/login.html", {'form': form})


def register(request):
    # Создаем пустую форму аутентификации
    form = UserCreationFormCustom()
    if request.method == "POST":
        # Добавляем полученные данные в форму
        form = UserCreationFormCustom(data=request.POST)
        # Если форма действительна
        if form.is_valid():
            # Создайте новую учетную запись пользователя
            user = form.save()

            # Если пользователь создан правильно
            if user is not None:
                # Мы входим в систему вручную
                do_login(request, user)
                # И мы перенаправляем вас на домашнюю страницу
                return redirect('/')

    # Если мы хотим, мы удаляем поля справки
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # если мы дойдем до конца, то получим форму
    return render(request, "authentication/register.html", {'form': form})


def logout(request):
    # Мы выходим из системы с помощью этой функции
    do_logout(request)
    # Мы перенаправляем
    return redirect('/')